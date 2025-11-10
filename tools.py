from crewai.tools import tool
from crewai_tools import SerperDevTool
import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# built-in CrewAI tool to search the internet and return the most relevant results
search_tool = SerperDevTool()


@tool
def scrape_tool(url: str):
    """
    Use this when you need to read the content of a website.
    Returns the content of a website. In case the website is not available, it returns no content.
    Input should be a 'url' string. (e.g https://en.wikipedia.org/wiki/2025_Cambodian%E2%80%93Thai_border_crisis)
    Output:
    """

    # opens a real browser and renders JavaScript, so we can get the final DOM
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        time.sleep(5)
        html = page.content()
        browser.close()

        # BeautifulSoup allows us to handle/manage HTMLs tags in a browser
        # parse HTML into a tree and simplify text extraction/cleaning
        soup = BeautifulSoup(html, "html.parser")

        # HTML tags to remove
        unwanted_tags = [
            "header",
            "footer",
            "nav",
            "aside",
            "script",
            "style",
            "noscript",
            "iframe",
            "form",
            "button",
            "input",
            "select",
            "textarea",
            "svg",
            "canvas",
            "audio",
            "video",
            "embed",
            "object",
        ]

        for tag in soup.find_all(unwanted_tags):
            # tag.decompose destroys the PageElement and its children
            tag.decompose()

        # returns text by removing HTML code
        content = soup.get_text(separator=" ")

        return content if content != "" else "No content"
