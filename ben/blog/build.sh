#!/bin/bash

# set -x

for f in **/*.md; do
  out=$(dirname "$f")/$(basename "$f" .md).html
  echo "$out"
  pandoc -s -c ../../style.css "$f" -o "$out"
done

cat <<EOF >index.html
<html>
  <head>
    <title>throwingbones.com Blog</title>
    <link href="../style.css" rel="stylesheet" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  </head>
  <body>
    <ul>
EOF

for f in **/index.html; do
    TITLE=$(grep '^%' "${f%.html}.md" | head -n1)
    TITLE=${TITLE:1}
    if [[ -z $TITLE ]]; then
        echo "ERR: no title for $f" >&2
    fi
    DATE=$(echo "$f" | grep -Eo '[0-9]{4,}-[0-9]{2}')
    echo "<li>$DATE: <a href=\"$f\">$TITLE</a></li>"
done |sort -r >>index.html

cat <<EOF >>index.html
    </ul>
  </body>
</html>

EOF
