import requests
# url =  "https://web.stanford.edu/class/archive/cs/cs103/cs103.1132/lectures/18/Small18.pdf"

for i in range(10,30):
    url=f"https://web.stanford.edu/class/archive/cs/cs103/cs103.1132/lectures/{i}/Small{i}.pdf"
    r = requests.get(url)
    print(f"Downloading slide {i}")
    open(f'pdfoutput/{i}.pdf', 'wb').write(r.content)