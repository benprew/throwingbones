#!/usr/bin/env python3

import os
import re
import glob
from datetime import datetime

# Tag migration mapping
TAG_MAPPING = {
    # Technology (combine software-development, programming, systems, testing, ruby, perl)
    'software-development': 'technology',
    'programming': 'technology', 
    'systems': 'technology',
    'testing': 'technology',
    'ruby': 'technology',
    'perl': 'technology',
    
    # Data Science
    'statistics': 'data-science',
    'economics': 'data-science',
    
    # Philosophy (philosophy, some meta posts)
    'philosophy': 'philosophy',
    
    # Languages
    'spanish': 'languages',
    
    # Learning (learning, reading - but reading could also be 'book-notes')
    'learning': 'learning',
    'reading': 'learning',  # Most reading posts are learning-related
    
    # Keep some as-is but clean up
    'journal': 'journal',
    'misc': 'misc',  # Will review these manually
    'meta': 'meta'   # Will review these manually
}

def get_tags_from_file(filepath):
    """Extract current tags from an org file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Look for #+TAGS: line
    match = re.search(r'^#\+TAGS:\s*(.+)$', content, re.MULTILINE)
    if match:
        tags = match.group(1).strip().split()
        return tags
    return []

def update_tags_in_file(filepath, new_tags):
    """Update the tags in an org file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the TAGS line
    new_tags_line = f"#+TAGS: {' '.join(new_tags)}"
    updated_content = re.sub(r'^#\+TAGS:\s*.*$', new_tags_line, content, flags=re.MULTILINE)
    
    with open(filepath, 'w') as f:
        f.write(updated_content)

def migrate_tags():
    """Migrate tags in all org files according to the mapping."""
    org_files = glob.glob('/home/ben/src/throwingbones/blog_src/org/*.org')
    
    migration_log = []
    
    for filepath in sorted(org_files):
        filename = os.path.basename(filepath)
        current_tags = get_tags_from_file(filepath)
        
        if not current_tags:
            print(f"⚠️  {filename}: No tags found")
            continue
            
        # Map old tags to new tags
        new_tags = []
        changes = []
        
        for old_tag in current_tags:
            if old_tag in TAG_MAPPING:
                new_tag = TAG_MAPPING[old_tag]
                if new_tag not in new_tags:  # Avoid duplicates
                    new_tags.append(new_tag)
                if old_tag != new_tag:
                    changes.append(f"{old_tag} → {new_tag}")
            else:
                # Keep unknown tags as-is
                if old_tag not in new_tags:
                    new_tags.append(old_tag)
                changes.append(f"{old_tag} (kept)")
        
        if changes:
            print(f"📝 {filename}")
            print(f"   Old: {' '.join(current_tags)}")
            print(f"   New: {' '.join(new_tags)}")
            print(f"   Changes: {', '.join(changes)}")
            print()
            
            # Update the file
            update_tags_in_file(filepath, new_tags)
            
            migration_log.append({
                'file': filename,
                'old_tags': current_tags,
                'new_tags': new_tags,
                'changes': changes
            })
        else:
            print(f"✅ {filename}: No changes needed")
    
    # Write migration log
    log_file = '/home/ben/src/throwingbones/blog_src/tag-migration-log.txt'
    with open(log_file, 'w') as f:
        f.write(f"Tag Migration Log - {datetime.now().isoformat()}\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Migration Mapping:\n")
        for old, new in TAG_MAPPING.items():
            f.write(f"  {old} → {new}\n")
        f.write("\n")
        
        f.write("File Changes:\n")
        for entry in migration_log:
            f.write(f"\n{entry['file']}:\n")
            f.write(f"  Old: {' '.join(entry['old_tags'])}\n")
            f.write(f"  New: {' '.join(entry['new_tags'])}\n")
            f.write(f"  Changes: {', '.join(entry['changes'])}\n")
    
    print(f"\n✅ Migration complete! Log saved to: {log_file}")
    print(f"📊 Migrated {len(migration_log)} files")
    
    # Show new tag distribution
    print("\n📈 New tag distribution:")
    tag_counts = {}
    for entry in migration_log:
        for tag in entry['new_tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {tag}: {count}")

if __name__ == '__main__':
    print("🏷️  Starting tag migration...")
    print("This will update tags in all org files according to the new taxonomy.")
    print()
    
    response = input("Continue? (y/N): ")
    if response.lower() != 'y':
        print("Migration cancelled.")
        exit(0)
    
    migrate_tags()