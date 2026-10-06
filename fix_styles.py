import re

with open(r'c:\SuelvoSasi\src\App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix inline styles for React (e.g. style="width: 100%;")
content = re.sub(r'style="width:\s*([^;]+);?"', r"style={{ width: '\1' }}", content)

with open(r'c:\SuelvoSasi\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed inline styles")
