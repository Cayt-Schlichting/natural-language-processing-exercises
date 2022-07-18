from requests import get
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Codeup Data Science - Jemison'}
topics = ["business","sports","technology","entertainment"]
urls = ['https://codeup.com/data-science/jobs-after-a-coding-bootcamp-part-1-data-science/',
        'https://codeup.com/data-science/math-in-data-science/',
        'https://codeup.com/data-science/transition-into-data-science/',
        'https://codeup.com/data-science/data-science-career/',
        'https://codeup.com/data-science/data-science-without-a-degree/']


def get_blog_articles(urls,headers):
    '''
    Given a list of URLs of Codeup blog articles, returns a list of dictionaries containing the url, blog title and blog content.
    '''
    blog_list = []
    for url in urls:
        #get page info
        response = get(url,headers=headers)
        #turn into soup object
        soup = BeautifulSoup(response.content,'html.parser')
        
        blog_dict = {
            'url': url,
            'title': soup.title.text,
            'content': soup.select('.entry-content')[0]
        }
        blog_list.append(blog_dict)
    return blog_list

def get_news_articles(topics,headers):
    '''
    Given a list of news topics, retrieve the title and content for all articles in that inshorts topic.
    '''
    base_url = 'https://inshorts.com/en/read/'
    article_list = []
    for t in topics:
        #create section url
        topic_url = base_url + t
        #get the content
        response = get(topic_url,headers=headers)
        #convert to soup
        soup = BeautifulSoup(response.content,'html.parser')
        #get the headline for each article in this topic - list of headlines
        headlines = soup.find_all(itemprop="headline")
        #get the content for each article - list of article bodies
        bodies = soup.find_all(itemprop="articleBody")
        
        #loop over the 'cards' 
        #but really just looping over the list of headlines and article bodies
        for title, content in zip(headlines, bodies):
            #add all to dictionary
            art_dict = {
                'title': title.text,
                'content': content.text,
                'category': t
            }
            #append this article to the list
            article_list.append(art_dict)
        
    return article_list