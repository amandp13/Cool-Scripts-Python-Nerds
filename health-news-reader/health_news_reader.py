# Read news-updates with Python3
# using two important and popular python pacakages requests and json
import requests
import json
import datetime
# function for speech
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
# main programme
if __name__ == "__main__":
    print("\n********** Here is Today's Health News ***********")
    now= datetime.datetime.now()
    print('\nDATE: 'f'{now:%d-%m-%Y | %H:%M }')
    speak("Here is Today's health news")
# define URL
    url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        speak(str(i))
        print('(',i,')',content['title'],'\n')
        speak(content['title'])
        print('->',content['description'])
        if(content['description']):
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    speak("thank you for listening..")
    print('\n********** Thank you for listening..... ***********')

