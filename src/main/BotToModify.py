'''
Created on 23 May 2017

@author: zhi liang, renxing
'''
#Last update: 29/9
#######################################################
# Telegram Food Bot
# The bot can be found at: @FoodAtSG_bot on Telegram
# If you are testing, please replace token with
# your own one to prevent collision :)
#######################################################

import telepot
from telepot.delegate import pave_event_space, per_chat_id, create_open
import requests
from bs4 import BeautifulSoup

# Crawls yelp for results and obtains their ratings
def food_crawler(location, category, food_lst, url_lst, rating_lst, numreviews_lst):
    if category == 1:
        cat = ""
    elif category == 2:
        cat = "Chinese"
    elif category == 3:
        cat = "Cafes"
    elif category == 4:
        cat = "Japanese"
    elif category == 5:
        cat = "food_court"
    elif category == 6:
        cat = "halal"
    elif category == 7:
        cat = "desserts"
    else:
        cat = "Hotdogs"  # stands for fast food and takeaways
        
    url = "https://www.yelp.com.sg/search?find_desc=Restaurants&find_loc=" + location + ",+Singapore&start=0&cflt=" + cat
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    # Loop to find the particular element in html file
    for link in soup.findAll("a", {'class': 'biz-name js-analytics-click'}):

        # get title
        href = 'https://www.yelp.com.sg' + link.get('href')
        title = link.string

        # get ratings
        rating = link.parent.parent.parent.find('i', {'class': 'star-img'})
        if rating:
            rating = rating.get('title')
            rating = rating.split(' ', 1)[0]

        # get number of reviews
        numReviews = link.parent.parent.parent.find('span', {'class': 'review-count'})
        if numReviews:
            numReviews = numReviews.get_text().strip()

        if title not in food_lst:
            food_lst.append(title)
            url_lst.append(href)
            rating_lst.append(rating)
            numreviews_lst.append(numReviews)


# Generates an interactive reply based on what the user sent
def interactiveReply(category):
    if category == 1 or category == 2:
        reply = "Going for some decent food with friends or pak tor? ^_^?"
    elif category == 3:
        reply = "Up for some nice hot Cappuccino while choping seats to mug?"
    elif category == 4:
        reply = "Wa going to makan some delicious ramen or sushi? =)"
    elif category == 5:
        reply = "Chicken Rice, Laksa, Western food, you are gonna have a hard time choosing from all these."
    elif category == 6:
        reply = "Looking for some delicious nasi briyani or nasi lemak?"
    elif category == 7:
        reply = "Tau hua, Yogurt ice-cream, Bingsu, I am also drooling from looking at all these choices already..  "
    else:
        reply = "Seems like someone is planning to gain some weight today."
    return reply


# Scrapes location. If location not found, return None
def getLocation(location):
    url = "https://www.yelp.com.sg/search?find_desc=Restaurants&find_loc=" + location + ",+Singapore"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    print(soup)
    titleText = soup.find('span', {'class': 'query-location'})
    
    # check if search result is valid
    if titleText == None:
        return None
    text = titleText.get_text()
    if text == 'in Singapore':
        return None
    else:
        print(text)
        scraped_location = text.split(' ', 1)[1]  # Remove first word
        scraped_location = scraped_location[:-11]  # remove [, singapore]
        #  it's supposed to truncate [near] boon lay [, Singapore]
        #  Seems to work most of the time

    return scraped_location


# Returns a string of stars given a rating
def getStarsFromRating(rating):
    integerRating = -1  # default to this value if no rating given
    if rating:
        integerRating = int(2 * float(rating))
    # Because it's always .0 or .5, there will be no rounding error
    # Unfortunately, there is no half-star unicode character :(
    stringStars = ""
    for i in range(5):
        if i < integerRating // 2:
            stringStars = stringStars + '★'
        else:
            stringStars = stringStars + '☆'
    return stringStars


# Builds a string that will be displayed to the user eg. "*** 3/5 reviews"
def getRatingStatement(rating, reviews):
    # if there is no rating
    if not rating:
        return "No reviews yet"

    # remove .0 from rating
    if rating.endswith(".0"):
        rating = rating[:1]

    stringRating = getStarsFromRating(rating) + ' ' + rating + "/5 - " + reviews
    return stringRating


# ChatHandler
class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        self._count = 1
        self.food_lst = list()
        self.url_lst = list()
        self.rating_lst = list()
        self.numreviews_lst = list()
        self.location = ''
        self.scraped_location = ''
        self.category = 0

    def on_chat_message(self, msg):

        if not 'text' in msg:# Fixes a bug where program will crash if user sends a sticker
            print("no message found") 
            return
        
        # here are the hardcoded commands
        # /changelocation and /start - go to _count = 1
        if msg['text'] == "/start" or msg['text'] == "/changelocation":
            if msg['text'] == '/changelocation':
                self.sender.sendMessage("Cannot decide where to eat? Neh Mind, try again.") # Only sent if user keys in /changelocation
            self._count = 1

        # /changecategory - go to _count = 2 only if location is already input
        if msg['text'] == "/changecategory":

            if self._count <= 2:
                self.sender.sendMessage("You haven't set a location yet!")
                self._count = 1
            else:
                message = "Too many choices edi, if I am you, I also won't know where to makan.\nLocation - *" + self.scraped_location + "\nPick a category*\n *1* - Restaurants\
\n *2* - Chinese Restaurants\n *3* - Cafes\n *4* - Japanese Food\n\
 *5* - Food Courts\n *6* - Halal\n *7* - Desserts\n *8* - Takeaway and Fast Food\n \
/changelocation to set a different location\nEnter a *number* please"
                self.sender.sendMessage(message, parse_mode='Markdown')
                self._count = 3

                return

        # Start of main method

        if self._count == 1:
            self.sender.sendMessage("Where would you like to eat in Singapore?")

            self._count += 1
            return


        elif self._count == 2:

            self.location = msg['text']
            if self.location.isdigit():
                self.sender.sendMessage("Sorry, please enter a valid location\nPlease try again")
                return

            scrapedLocation = getLocation(self.location)
            if scrapedLocation == None:
                self.sender.sendMessage("Sorry, location was not found in search engine.\nPlease try again")
                return

            self.scraped_location = scrapedLocation
            message = " Location - *" + scrapedLocation + "\nPick a category*\n *1* - Restaurants\
\n *2* - Chinese Restaurants\n *3* - Cafes\n *4* - Japanese Food\n\
 *5* - Food Courts\n *6* - Halal\n *7* - Desserts\n *8* - Takeaway and Fast Food\n \
/changelocation to set a different location\nEnter a *number* please"
            self.sender.sendMessage(message, parse_mode='Markdown')

            self._count += 1
            return


        elif self._count == 3:

            try:
                self.category = int(msg['text'])
            except ValueError:
                self.sender.sendMessage("Please give me a number from the above category :)")
                return

            if self.category > 8 or self.category < 1:
                self.sender.sendMessage("Please give me a number between 1 to 8 :)")
                return
            reply = interactiveReply(self.category)

            locationMessage = reply + "\nLooking for places near " + self.scraped_location + "..."
            self.sender.sendMessage(locationMessage)
            food_crawler(self.location, self.category, self.food_lst, self.url_lst, self.rating_lst,
                         self.numreviews_lst)

            x = 0 # counter for the string array

            for food in self.food_lst:
                message = str(x + 1) + ': *' + food + '*' + "\n" \
                          + getRatingStatement(self.rating_lst[x], self.numreviews_lst[x]) + "\n" + self.url_lst[x]
                self.sender.sendMessage(message, parse_mode='Markdown')

                x += 1

            # once finished, reset the URLs
            self.food_lst = []
            self.url_lst = []

            self.sender.sendMessage("/changelocation to set a different location \n/changecategory to change category")

TOKEN = "398900728:AAEYokXaTW8RgArSG44VqLt_b4wqFu1sFTI"
 
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=120),
])
bot.message_loop(run_forever='Listening ...')
