# NLP_Project
**Natural Language Processing Project Proposal**

*Mikail CEREN*

**Subject:**Sentiment Analysis

**Project Title:Sentiment Analysis for Political Parties**

**Project Description:** 
     This project is about political parties in Turkey. Sentiment analysis is very important for political leaders  because they want to know what people think about their political parties. The aim of this project is sentiment analysis about political parties in social media. So I will develop a software. I will use twitter data in my project. Firstly I will take tweets from [Twitter](www.twitter.com) using Twitter API. In this site a user comment for each political parties, stating his/her general opinion about the leaders especially with a related icon (positive, neutral, negative). I will gather all the data from related hash tags  of the site. I'll do the analysis of data using the techniques of sentiment analysis. After that I want to show results as charts.

**Project Requirements:** Java, Zemberek Library, The OpenNlp Library, Twitter API,Weka 

**Steps**
- Collect tweets from related hashtags and accounts using python tweepy library.
- Clean these tweets using perl.(@,#,digits v.s ...).
- Make sentence detection and tokenization using java zemberek library.
- Label each tweet as positive,negative or neutral.
- Create training data using OpenNLp for sentiment analysis.
- Try some classifier algorithms(for example:Naive Bayes) using Weka
- Test results using Weka.
