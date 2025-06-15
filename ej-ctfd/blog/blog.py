from selenium import webdriver
from selenium.webdriver.common.by import By
import re


def buscar(links, count, visited):
    try:
        links = driver.find_elements(By.CLASS_NAME, 'card-title')

        for i in links:
            link = i.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

            if link not in visited and '#' not in link:
                driver.get(link)
                visited.add(link)
                text = driver.find_element(By.CLASS_NAME, 'article-post').text
                results = re.findall('\\bURJC\\b', text)
                #results = re.findall('URJC', text)
                for match in results:
                    count = count + 1

                print(count)

            return count + buscar(links, count, visited)

    except Exception:
        pass


driver = webdriver.Chrome()
driver.get("https://r2-ctf-vulnerable.numa.host/")

count = 0
visited = set()
links = []

print(buscar(links, count, visited))
