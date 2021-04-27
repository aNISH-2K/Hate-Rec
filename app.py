import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud


consumerKey = "p4I1wgl2npsNdBDshu378Fjkd"
consumerSecret = "ulwcITBcrpPnb9EkwTukr7ERxLStRNudValhVWC68vlT8PdgGE"
accessToken = "3194988066-pW6mxUKNgjFvR4rNzuhbONp23wPRBVxDCop1S0g"
accessTokenSecret = "xR5oi8SxmOJDw0SJAL0qfBhEsCGwXZe6SAOyIca4biiyR"

#Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret) 
# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret) 
# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)

pickle_in = open("lr_model.pkl", "rb")
model = pickle.load(pickle_in)


def predictor(n):
    prediction = model.predict([['tweet']])
    print(prediction)
    return prediction




def main():
    st.title("Hate Speech Detection")
    html_temp = """ 

    """
    st.markdown(html_temp, unsafe_allow_html=True)
    image = Image.open('banner.jpg')
    st.image(image, caption='Hate Speech Recognition',use_column_width=True)
    st.title("Hate Speech Recognition")
    options = ["About","Hate Recognition"]
    choice = st.sidebar.selectbox("Choose any option from below dropdown", options)

    if choice == "About":
        st.subheader("Analyze the tweets of your favourite topics and trends!!")
        st.subheader("This tool perfoms the following activities")
        st.write("### Hate Recognition:\n1. Recognize the Tweet . \n2. Word cloud generation. ")
        #st.write("### B. Generate tweet data:\n1. Get the most liked tweet. \n2. Get the most liked re-tweet. ")

    elif choice == "Hate Recognition":
        tweet = st.text_area("Your query goes here...")
        Analyzer_choice = st.selectbox("Select the Activities",  ["Recognize the Tweet","Generate WordCloud" ])
        #tweet = st.text_input("Enter your tweet","Your Query goes here.")
        result=""
        if st.button("Analyze"):
            if Analyzer_choice == "Recognize the Tweet":
                result=predictor(tweet)

            elif Analyzer_choice == "Generate WordCloud":
                st.success("Generating word cloud!")
                def generate_wordcloud():
                    posts = api.search(tweet, count=10, lang='en', exclude='retweets',tweet_mode='extended')
                    df = pd.DataFrame([tweet.full_text for tweet in posts], columns = ['Tweets'])
                    allWords = ' '.join([twts for twts in df['Tweets']])
                    wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
                    plt.imshow(wordCloud, interpolation="bilinear")
                    plt.axis('off')
                    plt.savefig('WC.jpg')
                    img= Image.open("WC.jpg")
                    return img

                img=generate_wordcloud()
                st.image(img)
        

if __name__=='__main__':
    main()
    
