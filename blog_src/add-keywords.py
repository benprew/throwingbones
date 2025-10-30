#!/usr/bin/env python3

import os
import re
import glob
from datetime import datetime

def extract_date_and_title_from_filename(filename):
    """Extract date and title from filename like 2020-06-15-commit-pct-in-sar.org"""
    basename = os.path.basename(filename)
    
    # Match YYYY-MM-DD-rest.org pattern
    match = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.org$', basename)
    if match:
        date_str = match.group(1)
        title_slug = match.group(2)
        # Convert slug to title
        title = title_slug.replace('-', ' ').title()
        return date_str, title
    
    # Handle files without dates (like journal entries)
    if basename.endswith('.org'):
        title_slug = basename[:-4]  # Remove .org
        # Try to extract date from beginning
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', title_slug)
        if date_match:
            date_str = date_match.group(1)
            remaining = title_slug[len(date_str):].lstrip('-')
            if remaining:
                title = remaining.replace('-', ' ').title()
            else:
                title = f"Journal for {date_str}"
            return date_str, title
    
    return None, None

def suggest_tags(title, content):
    """Suggest tags based on title and content"""
    tags = []
    
    # Title-based suggestions
    title_lower = title.lower()
    if any(word in title_lower for word in ['testing', 'test']):
        tags.append('testing')
    if any(word in title_lower for word in ['sinatra', 'ruby', 'rails']):
        tags.append('ruby')
    if any(word in title_lower for word in ['commit', 'memory', 'sar', 'performance']):
        tags.append('systems')
    if any(word in title_lower for word in ['learning', 'notes', 'study']):
        tags.append('learning')
    if any(word in title_lower for word in ['perl', 'advent']):
        tags.append('perl')
    if any(word in title_lower for word in ['lisp', 'programming']):
        tags.append('programming')
    if any(word in title_lower for word in ['price', 'market', 'trading']):
        tags.append('economics')
    if any(word in title_lower for word in ['statistics', 'median', 'data']):
        tags.append('statistics')
    if any(word in title_lower for word in ['journal']):
        tags.append('journal')
    
    # Content-based suggestions
    content_lower = content.lower()
    if any(word in content_lower for word in ['software', 'code', 'programming', 'development']):
        if 'software-development' not in tags:
            tags.append('software-development')
    if any(word in content_lower for word in ['spanish', 'español']):
        tags.append('spanish')
    if any(word in content_lower for word in ['reading', 'book', 'read']):
        tags.append('reading')
    if any(word in content_lower for word in ['meta', 'blog', 'writing']):
        tags.append('meta')
    
    # Default tag if none found
    if not tags:
        tags.append('misc')
    
    return tags

def has_keywords(content):
    """Check if file already has org-mode keywords"""
    lines = content.split('\n')
    for line in lines[:10]:  # Check first 10 lines
        if line.startswith('#+'):
            return True
    return False

def add_keywords_to_file(filepath):
    """Add missing keywords to an org file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already has keywords
    if has_keywords(content):
        print(f"Skipping {filepath} - already has keywords")
        return
    
    date_str, title = extract_date_and_title_from_filename(filepath)
    if not date_str or not title:
        print(f"Skipping {filepath} - couldn't extract date/title")
        return
    
    # Suggest tags
    tags = suggest_tags(title, content)
    
    # Create header
    header = f"""#+TITLE: {title}
#+AUTHOR: Ben
#+DATE: {date_str}
#+TAGS: {' '.join(tags)}

"""
    
    # Remove leading dashes if present
    content = content.lstrip('-\n ')
    
    # Combine header and content
    new_content = header + content
    
    # Write back to file
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}")
    print(f"  Title: {title}")
    print(f"  Date: {date_str}")
    print(f"  Tags: {', '.join(tags)}")
    print()

def main():
    # Find all org files
    org_files = glob.glob('/home/ben/blog/org/*.org')
    
    for filepath in sorted(org_files):
        add_keywords_to_file(filepath)

if __name__ == '__main__':
    main()