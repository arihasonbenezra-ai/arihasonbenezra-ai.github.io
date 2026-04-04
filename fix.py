content = open('index.html').read()
content = content.replace(
    'https://lockedin-react.vercel.app',
    'https://aribenezra.com/lockedin'
)
open('index.html', 'w').write(content)
print("Done")
