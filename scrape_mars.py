#Imports & Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

#Site Navigation


def init_browser():
    executable_path = {
        "executable_path": "/Users/rogerlefort/Google Drive/Repositories/MIssion-to-Mars/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)


def scrape():
    """Scrapes various websites for information about Mars, and returns data in a dictionary"""

    browser = init_browser()


    mars_data = {}

    # visit the NASA Mars News site and scrape headlines
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    title = news_soup.find('div', class_='content_title').text
    teaser_text = news_soup.find('div', class_='article_teaser_body').text

    mars_data["nasa_headline"] = title
    mars_data["nasa_teaser"] = teaser_text

    # visit the JPL website and scrape the featured image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(1)

    try:
        # Scraping the URL for link
        feat_img_url = image_soup.find('figure', class_='lede').a['href']
        feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'

        image_path = f'https://www.jpl.nasa.gov{feat_img_url}'
        mars_data["feature_image_src"] = image_path
    except:
        image_path = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17900_hires.jpg'
        mars_data["feature_image_src"] = image_path

    # visit the mars weather report twitter and scrape the latest tweet
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')

    first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    mars_data["weather_summary"] = first_tweet

    # visit space facts and scrap the mars facts table
    url = 'https://space-facts.com/mars/'
    table = pd.read_html(url)

    time.sleep(1)

    mars_facts = table[0]
    mars_only_table = mars_facts.drop(columns={'Earth'})
    renamed_mars_only_table = mars_only_table.rename(
        columns={'Mars - Earth Comparison': 'Property', 'Mars': 'Value'})
    final_mars_facts = renamed_mars_only_table.set_index('Property')

    mars_facts_html = final_mars_facts.to_html(header=True, index=True)
    mars_data["fact_table"] = mars_facts_html

    # scrape images of Mars' hemispheres from the USGS site
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'html.parser')


    # Retreiving all items that contain mars hemispheres information
    items = hemisphere_soup.find_all('div', class_='item')

    # Creating list for hemisphere urls
    hemisphere_image_urls = []

    # Store the main_url
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items:
        # Store title
        title = i.find('h3').text

        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']

        # Visit the link that contains the full image website
        browser.visit(hemispheres_main_url + partial_img_url)

        # HTML Object of individual hemisphere information website
        partial_img_html = browser.html

        # Parse HTML with Beautiful Soup for every individual hemisphere information website
        soup = BeautifulSoup(partial_img_html, 'html.parser')

        # Retrieve full image source
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']

        # Append the retreived information into a list of dictionaries
        hemisphere_image_urls.append({"title": title, "img_url": img_url})

        mars_data["hemisphere_imgs"] = hemisphere_image_urls

    browser.quit()

    return mars_data

    print(mars_data)
