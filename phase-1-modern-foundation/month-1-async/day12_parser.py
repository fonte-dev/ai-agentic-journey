from bs4 import BeautifulSoup

html_content = """
<html>
    <head><title>Therapist Directory</title></head>
    <body>
        <div class="doctor-card">
            <h2 class="name">Dr. Sarah Connor</h2>
            <p class="specialty">Trauma Specialist</p>
            <span class="status">Available</span>
        </div>
        <div class="doctor-card">
            <h2 class="name">Dr. Hannibal Lecter</h2>
            <span class="status">Booked</span>
        </div>
    </body>
</html>
"""


def safe_extract(element, tag_name, class_name):
    """
    Tries to find a tag. Returns text if found, 'Unknown' if not.
    """
    found = element.find(tag_name, class_=class_name)
    if found:
        return found.text.strip()
    return "Unknown"


def parse_doctors(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="doctor-card")

    print(f"Found {len(cards)} doctor cards.\n")

    results = []
    for card in cards:
        # USE THE HELPER HERE:
        name = safe_extract(card, "h2", "name")
        specialty = safe_extract(card, "p", "specialty")

        results.append({"name": name, "specialty": specialty})

    return results


if __name__ == "__main__":
    data = parse_doctors(html_content)
    for doc in data:
        print(doc)
