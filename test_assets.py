import os
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all src and href attributes
matches = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', content)
broken = []
verified = []

for m in matches:
    if m.startswith('http://') or m.startswith('https://') or m.startswith('#') or m.startswith('mailto:'):
        continue
    # Strip any query parameters or hash
    clean_path = m.split('?')[0].split('#')[0]
    if not clean_path:
        continue
    if os.path.exists(clean_path):
        verified.append(clean_path)
    else:
        broken.append((m, clean_path))

print(f"Verified {len(verified)} local assets:")
for v in verified:
    print(f"  [OK] {v} ({os.path.getsize(v)} bytes)")

if broken:
    print(f"\nFound {len(broken)} broken assets:")
    for m, cp in broken:
        print(f"  [MISSING] {m} (checked: {cp})")
else:
    print("\nSUCCESS: ZERO broken local references in index.html!")
