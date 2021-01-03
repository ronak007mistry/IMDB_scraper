import csv
import os
import requests
from bs4 import BeautifulSoup
import json
import petl as etl

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
list_250 = []
# Get the html
r = requests.get(url)

html_content = r.content

# Parse the html
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title
paras = soup.find_all('p')
anchors = soup.find_all('a')

urls = [] 

for a_tags in anchors:
    url = a_tags.get('href')

    urls.append(url)
)
for i in urls[59:559]:
    i = "https://imdb.com"+i
    list_250.append(i)
print(list_250)


title_of_movie = []
rating_of_movie = []
duration_of_movie = []
date_of_movie = []
summary_of_movie = []

for link in list_250:
    myurl = link
    r = requests.get(myurl)

    html_content = r.content

    # Parse the html
    soup = BeautifulSoup(html_content, 'html.parser')
    divs = soup.find('div', attrs={'class':'title_block'})

    movie_name = divs.h1.text
    movie_rating = divs.strong.span.text
    movie_duration = divs.time.text.strip()

    movie_release_date = soup.find('a', attrs={'title':'See more release dates'}).text
    movie_desc = soup.find('div', attrs={'class':'summary_text'}).text.strip()
    removing = movie_release_date.find('(')
    movie_release_date = movie_release_date[:removing].strip()

    title_of_movie.append(movie_name)
    rating_of_movie.append(movie_rating)
    duration_of_movie.append(movie_duration)
    date_of_movie.append(movie_release_date)
    summary_of_movie.append(movie_desc)



final = zip(title_of_movie,rating_of_movie,duration_of_movie,date_of_movie,summary_of_movie)
print(final)
new_list = []
for i in range(0,len(title_of_movie),2):
    new_list.append([title_of_movie[i], rating_of_movie[i], duration_of_movie[i], date_of_movie[i], summary_of_movie[i]])
print(list(final))
print(new_list)
y = list(final)
with open('finaldata.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(new_list)

print("Done with scraping")






