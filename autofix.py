import os
import re

directory = 'src/latex/book_on_digital'
# Fix rule 3: Punctuation directly following inline math block
pattern = re.compile(r'\$([^\$]+?)\$([,.;:])')

fixed_count = 0

for filename in os.listdir(directory):
    if not filename.endswith('.tex'):
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = pattern.subn(r'$\1\2$', content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {count} occurrences in {filename}')
        fixed_count += count

print(f'Total fixes applied: {fixed_count}')
