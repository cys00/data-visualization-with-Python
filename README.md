# data-visualization-with-Python
I am using Twython Streamer to collect 10k real time tweets about Seattle. While Twitter API is collecting tweets, it might break up half way for connection issue. However, you can always concatenate multiple lists into one by load all the json files where you store your tweets. 

About the visualization part, i choose wordcloud with a mask of Space Needle, where you can visualize all the keywords about Seattle. Do remember to clean your data before use. I did remove all the punctuations, digits by using str.maketrans and translating the table, before lemmatizing/stemming and tokenizing all the words. They can all be completed with nltk. Check out details in my codes. 
