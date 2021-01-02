import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
list_250 = []
# Get the html
r = requests.get(url)

html_content = r.content
# print(html_content)

# Parse the html
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify)

title = soup.title
# print(title)
paras = soup.find_all('p')
# print(paras)
anchors = soup.find_all('a')
# print(anchors)
# elem = soup.select('.posterColumn')
# print(elem)
# for anchors in elem:
#     anchor = anchors.find_all('a')
# print(anchor)
# hreff = anchor.select('')
urls = [] 

for a_tags in anchors:
    url = a_tags.get('href')
    # if not url.startswith('http'):
        # url = "https://imdb.com"+url
    urls.append(url)
# print(urls)
# print(len(urls))
for i in urls[59:559]:
    i = "https://imdb.com"+i
    list_250.append(i)
    # print(i)
print(list_250)

# for link in soup.find_all('a'):
#     print(link.get('href'))

# main_table = soup.find_all("td",attrs={'class':'posterColumn'})
# # print(main_table)
# a_tags = main_table.find("a")
# print(a_tags)

# for a_tag in a_tags:
#     url = a_tag['href']
#     if not url.startswith('http'):
#         url = "https://imdb.com"+url
#     urls.append(url)

# print(urls)

# table = soup.find("td",attrs={'class':'posterColumn'})
# links = table.find_all("a")
# # tonight = forecast_items[0]
# print(links)

for link in list_250:
    myurl = link
    r = requests.get(myurl)

    html_content = r.content
    # print(html_content)

    # Parse the html
    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup.prettify)
    divs = soup.find_all('div', attrs={'class':'title_block'})
    print(divs)
    # div = soup.find_all('div', attrs={'class':'ratingValue'})
    # print(div)


    # wrapper = soup.find_all('div', attrs={'class':'title_wrapper'}).get_text()
    # name = divs.find(class_="ratingValue")
    # print(wrapper)
    # headings = soup.findAll("h1", {"class": "headingfour"})
    # print(headings)


