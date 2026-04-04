content = open('index.html').read()
content = content.replace(
    '{ id: \'proj-card-2\', links: \'<div class="project-card-links" style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><a href="https://scout-chat.vercel.app" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#F0EDE8;text-decoration:none;background:#8B1A1A;padding:8px 16px;border-radius:4px">View Demo ↗</a></div>\' }',
    '{ id: \'proj-card-2\', links: \'<div class="project-card-links" style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><a href="https://aribenezra.com/scout" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;color:#F0EDE8;text-decoration:none;background:#8B1A1A;padding:8px 16px;border-radius:4px">Learn More ↗</a></div>\' }'
)
open('index.html', 'w').write(content)
print("Done")
