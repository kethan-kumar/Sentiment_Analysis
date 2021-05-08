from sentimentAnalysis.SentimentAnalysis import SentimentAnalysis

if __name__ == '__main__':

    sentimentAnalysis = SentimentAnalysis()
    sentimentAnalysis.create_bow_each_tweet()
    sentimentAnalysis.display_output()
