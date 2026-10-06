import re

with open(r'c:\SuelvoSasi\src\App.jsx', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace all remaining lh3.googleusercontent links with unsplash placeholders
placeholders = [
    r'https://images.unsplash.com/photo-1545084930-b98a1a5b8109?auto=format&fit=crop&w=400&q=80',
    r'https://images.unsplash.com/photo-1582845689725-d71626fdfc97?auto=format&fit=crop&w=400&q=80',
    r'https://images.unsplash.com/photo-1632731557007-85be4ec73da2?auto=format&fit=crop&w=400&q=80'
]

for p in placeholders:
    c = re.sub(r'src="https://lh3\.googleusercontent\.com[^"]+"', f'src="{p}"', c, count=1)

with open(r'c:\SuelvoSasi\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(c)

print('Replaced broken imgs')
