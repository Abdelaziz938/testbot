#################################
##Coder: CDT Abdelaziz Gohar
##Assignment: Initial Skeleton
##Date: 15 June 2020
#################################

# the mule bot is an echo bot for now, it repeats the words that the user sends.
# I implemented this on Facebook as instructed, i created a page called Army mule and it has the messenger bot
# the code is working, I still need to figuer out how to use Git, and commit comands to uploded to heroku
# I also made a code that tells you what is the Academic day based on the last year's and planning to add to the bot
# Basically, the user has to text and the bot will respond.
# I'm planing to add more features, once I solve the issue with heroku, i will lunch the bot for a close personals to test it as users.


from flask import Flask, request
import requests
import sys
import os
import json
from Credentials import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        return request.args.get('hub.challenge', 200)
    else:
        return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    log(data)

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]

                    send_message(sender_id, message_text)

                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
    log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()

#below is the Academic day tracker
"""
from tkinter import *
import random

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    if entered_text in day_One :
        output.insert(END,"Day one" +'                                     '+"TODAY'S QOUTE :"+'                                    '+ random.choice(qoutes))
    elif entered_text in study_Days :
        output.insert(END,"Study day" +'                                     '+"TODAY'S QOUTE :"+'                                    '+ random.choice(qoutes))
    elif  entered_text in day_Two :
        output.insert(END,"Day two" +'                                     '+"TODAY'S QOUTE :"+'                                    '+ random.choice(qoutes))
    else:
        output.insert(END,"Classes free" +'                                     '+"TODAY'S QOUTE :"+'                                    '+ random.choice(qoutes))



day_One = ["08/01","10/01","15/01","17/01","23/01","27/01","29/01","31/01","03/02","06/02","08/02","11/02","13/02","18/02","20/02","24/02","28/02","02/03","04/03","06/03","23/03","25/03","27/03","31/03","02/04","06/04","09/04","13/04","15/04","17/04","20/04","23/04","27/04","29/04","01/05","04/05","06/05","08/05"]
day_Two = ["09/01","13/01","16/01","21/01","24/01","28/01","30/01","04/02","07/02","10/02","14/02","19/02","21/02","25/02","27/02","03/03","05/03","17/03","19/03","24/03","26/03","30/03","03/04","07/04","10/04","14/04","16/04","21/04","24/04","05/05"]
study_Days = ["07/05","01/04","08/04","22/04","28/04","18/03","05/02","12/02","26/02","22/02"]
qoutes = ["We are what we repeatedly do. Excellence, therefore, is not an act but a habit. - Aristotle", "The best way out is always through. - Robert Frost","Do not wait to strike till the iron is hot; but make it hot by striking. - William B. Sprague","Great spirits have always encountered violent opposition from mediocre minds. - Albert Einstein","Whether you think you can or think you can’t, you’re right. - Henry Ford","I know for sure that what we dwell on is who we become. - Oprah Winfrey","You must be the change you want to see in the world. - Mahatma Gandhi","What you get by achieving your goals is not as important as what you become by achievingyour goals. – Goethe","You can get everything in life you want if you will just help enough other people get whatthey want. - Zig Ziglar","Whatever you do will be insignificant, but it is very important that you do it.- Mahatma Gandhi","Desire is the starting point of all achievement, not a hope, not a wish, but a keen pulsatingdesire which transcends everything. - Napoleon Hill","Failure is the condiment that gives success its flavor. - Truman Capote","Vision without action is daydream. Action without vision is nightmare. - Japanese Proverb","In any situation, the best thing you can do is the right thing; the next best thing you can do is the wrong thing; the worst thing you can do is nothing. - Theodore Roosevelt","If you keep saying things are going to be bad, you have a chance of being a prophet. - IsaacB. Singer","Success consists of doing the common things of life uncommonly well.- Unknown","Keep on going and the chances are you will stumble on something, perhaps when you areleast expecting it. I have never heard of anyone stumbling on something sitting down. - CharlesF. Kettering, Engineer and Inventor","Twenty years from now you will be more disappointed by the things that you didn't do thanby the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch thetrade winds in your sails. Explore. Dream. Discover.- Mark Twain","Losers visualize the penalties of failure. Winners visualize the rewards of success. -Unknown","Experience is what you get when you don't get what you want. - Dan Stanford","Setting an example is not the main means of influencing others; it is the only means. – Albert Einstein","A happy person is not a person in a certain set of circumstances, but rather a person with acertain set of attitudes. - Hugh Downs","Remember that happiness is a way of travel, not a destination. - Roy Goodman","If you want to test your memory, try to recall what you were worrying about one year agotoday. - E. Joseph Cossman","What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson","We judge of man's wisdom by his hope. - Ralph Waldo Emerson","The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain","Age is an issue of mind over matter. If you don't mind, it doesn't matter. - Mark Twain","Whenever you find yourself on the side of the majority, it's time to pause and reflect. - MarkTwain","Keep away from people who try to belittle your ambitions. Small people always do that, but the really great make you feel that you, too, can become great. - Mark Twain","The surest way not to fail is to determine to succeed. - Richard B. Sheridan","Take the first step in faith. You don't have to see the whole staircase, just take the first step.- Dr. Martin Luther King Jr","Act or accept. - Unanonymous","Many great ideas go unexecuted, and many great executioners are without ideas. One without the other is worthless. - Tim Blixseth","The world is more malleable than you think and it's waiting for you to hammer it into shape.- Bono","Sometimes you just got to give yourself what you wish someone else would give you. - DrPhil","Motivation is a fire from within. If someone else tries to light that fire under you, chances are it will burn very briefly. - Stephen R. Covey","People become really quite remarkable when they start thinking that they can do things.When they believe in themselves they have the first secret of success. - Norman Vincent Peale","Whenever you find whole world against you just turn around and lead the world. -Anonymous","Being defeated is only a temporary condition; giving up is what makes it permanent. -Marilyn vos Savant, Author and Advice Columnist","I can't understand why people are frightened by new ideas. I'm frightened by old ones. – John Cage","Setting an example is not the main means of influencing others; it is the only means. – Albert Einstein","The difference between ordinary and extraordinary is that little extra. - Unknown","The best way to predict the future is to create it. - Unknown","Anyone can do something when they WANT to do it. Really successful people do thingswhen they don't want to do it. - Dr. Phil","Success is the ability to go from failure to failure without losing your enthusiasm. - SirWinston Churchill","Success seems to be connected with action. Successful people keep moving. They makemistakes but don't quit.- Conrad Hilton","Attitudes are contagious. Make yours worth catching. - Unknown","Do not let what you cannot do interfere with what you can do. - John Wooden","Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better. - Samuel Beckett"]



def close() :
    window.destroy()
    exit()
window=Tk()
window.title("academic day predictor")
window.configure(background="black")
photo = PhotoImage(file= "C:\\Users\\Algamal\\Desktop\\project\\a.png")
Label (window, image=photo, bg="black") .grid(row=0, column=1, sticky=W)
Label (window, text="enter the date DD/MM:", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)
textentry = Entry(window, width=10, bg="white")
textentry.grid(row=2, column=1, sticky=W)
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)
Label (window, text="\nThat day will be:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)
output = Text(window, width=50, height=5, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)
Label (window, text="\nClick to extit:", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)
Button(window, text="EXIT", width=4, command=close).grid(row=7, column=0, sticky=W)

window.mainloop()
""" 