content = open('index.html').read()
content = content.replace(
    '>View Demo ↗</a><a href="https://aribenezra.com/locked-in-case-study',
    '>Learn More ↗</a><a href="https://aribenezra.com/locked-in-case-study'
)
open('index.html', 'w').write(content)
print("Done")
