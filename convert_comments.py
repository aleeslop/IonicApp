import re

with open(r'c:\SuelvoSasi\src\App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML comments <!-- ... --> with JSX comments {/* ... */}
content = re.sub(r'<!--(.*?)-->', r'{/*\1*/}', content, flags=re.DOTALL)

with open(r'c:\SuelvoSasi\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Comments fixed")
