import csv
from playwright.sync_api import sync_playwright, expect
from tqdm import tqdm


class ScrapingFromYoutube:
    def __init__(self, urls: list):
        self.urls = urls

    def __write_csv(self, data: dict):
        with open(f"youtube.csv", 'a') as file:
            meta = ["url", "links"]
            writer = csv.DictWriter(file, fieldnames=meta)
            writer.writerow(data)

    def __first_connect(self):
        self.page.goto("https://www.youtube.com/")

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            self.page = context.new_page()
            self.__first_connect()
            self.page.wait_for_timeout(500)
            self.page1 = context.new_page()

            for url in tqdm(self.urls):
                self.page1.goto(url)
                self.page.wait_for_timeout(500)

                try:
                    self.page1.get_by_label("Описание").click() # !!!
                    self.page.wait_for_timeout(500)

                    links = []
                    for i in self.page1.locator("yt-channel-external-link-view-model").all():
                        links.append(i.get_by_role('link').inner_text())
                    result = {"url": url, "links": links}
                    self.__write_csv(result)

                except Exception as e:
                    print(e)


if __name__ == '__main__':
    urls = [
        "https://www.youtube.com/@AsafevStas",
        "https://www.youtube.com/@ODSAIRu",
        "https://www.youtube.com/@vincengarcia",
        "https://www.youtube.com/@vselennayaplus",
        "https://www.youtube.com/@PaulDavids"
    ]
    ScrapingFromYoutube(urls=urls).run()
