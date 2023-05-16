import requests
from bs4 import BeautifulSoup

# 함수
# input = URL
# output = 제목, 본문
# 기존: 제목함수, 본문함수 따로 제작하는 것이 좋음!
# -> why: 함수 만들 때 하나의 함수에 다수의 기능을 넣는것은 X
def get_news_title_and_content(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    print("="* 100)
    print(f"뉴스제목: {title}")
    print("="* 100)

    content = ""
    contents = doc.select("section > p")
    #contents.pop(-1)
    for tag in contents:
        content = content + tag.get_text()
    print(f"뉴스본문: {content}")

    return title, content