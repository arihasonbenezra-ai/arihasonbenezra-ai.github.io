content = open('index.html').read()

old = '<a href="https://aribenezra.com/locked-in-case-study" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#8B1A1A;text-decoration:none;border:1px solid #8B1A1A;padding:8px 16px;border-radius:4px">Business Case Study ↗</a><a href="https://aribenezra.com/locked-in-ux-case-study" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#8B1A1A;text-decoration:none;border:1px solid #8B1A1A;padding:8px 16px;border-radius:4px">UX Case Study ↗</a>'

content = content.replace(old, '')
open('index.html', 'w').write(content)
print("Done")
