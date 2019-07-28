# Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

For this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. Below is an outline of the various steps:

## Step 1 - Scraping

Initial scraping was performed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter (See `mission_to_mars.ipynb`)

The following URLs were scrapped:

### NASA Mars News

* [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.


### JPL Mars Space Images - Featured Image

* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) to find the image url for the current Featured Mars Image.


### Mars Weather

* [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) to scrape the latest Mars weather tweet from the page.


### Mars Facts

* [Mars Facts webpage](https://space-facts.com/mars/) to scrape the table containing facts about the planet including Diameter, Mass, etc.


### Mars Hemispheres

* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mars' hemispheres.
```
- - -

## Step 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

- - -