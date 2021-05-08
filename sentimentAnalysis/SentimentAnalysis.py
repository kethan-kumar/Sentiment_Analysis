from sentimentAnalysis.DataRetriever import DataRetriever


class SentimentAnalysis:

    def __init__(self):
        print("-------------------Initializing App---------------")
        self.data_retriever = DataRetriever()
        self.list_of_tweets = self.data_retriever.document_retriever()
        self.list_of_positive_words = self.read_polarity_words("positiveWords", "positive")
        self.list_of_negative_words = self.read_polarity_words("negativeWords", "negative")
        self.list_combined_words = []
        self.list_combined_words.extend(self.list_of_negative_words)
        self.list_combined_words.extend(self.list_of_positive_words)
        self.output = []
        self.positive_tweets_counter = 0
        self.negative_tweets_counter = 0
        self.neutral_tweets_counter = 0

    def read_polarity_words(self, file_name, polarity):
        # CITATION: positive words taken from https://gist.github.com/mkulakowski2/4289437
        # CITATION: negative words taken from https://gist.github.com/mkulakowski2/4289441
        print("-----------------Fetching " + polarity + " words-----------")
        f = open(file_name, "r")
        file_contents = f.read()

        list_of_polarity_words = file_contents.split("\n")
        f.close()
        return list_of_polarity_words

    def tag_tweet(self, polarity, list_of_words, bow_dict, tweet):
        counter = 0
        print("---------Tagging tweets in progress-----------------")
        for word in list_of_words:
            if word in bow_dict:
                if polarity == "positive":
                    self.positive_tweets_counter = self.positive_tweets_counter + 1
                    counter = self.positive_tweets_counter
                elif polarity == "negative":
                    self.negative_tweets_counter = self.negative_tweets_counter + 1
                    counter = self.negative_tweets_counter
                self.output.append({'tweet_no': counter, 'message': tweet, 'match': word, 'polarity': polarity})

    def display_output(self):
        print("----------Output----------------------------------")
        [print("%s ---- %s -----%s ----- %s\n" % (item['tweet_no'], item['message'], item['match'], item['polarity']))
         for item in self.output]
        print("Total Positive tweets:" + str(self.positive_tweets_counter))
        print("Total Negative tweets:" + str(self.negative_tweets_counter))
        print("Total Neutral tweets:" + str(self.neutral_tweets_counter))

    def create_bow_each_tweet(self):
        print("----------Create Bag of Words For each tweet--------------------")
        for tweet in self.list_of_tweets:
            bag_of_word_tweet = self.count_bow(tweet)
            if bag_of_word_tweet is not None:
                print("--------------Tagging Positive tweets-----------")
                self.tag_tweet("positive", self.list_of_positive_words, bag_of_word_tweet, tweet)
                print("--------------Tagging Negative tweets-----------")
                self.tag_tweet("negative", self.list_of_negative_words, bag_of_word_tweet, tweet)
                print("--------------Tagging Neutral tweets-----------")

    def count_bow(self, twitter_text):
        bow_dictionary = self.create_each_bag_of_word(twitter_text)

        for item in twitter_text.split(" "):
            if item in bow_dictionary:
                bow_dictionary[item.lower()] = bow_dictionary[item.lower()] + 1

        return bow_dictionary

    def create_each_bag_of_word(self, tweet_message):
        print("----------Initializing Bag of Words--------------------")
        bow_dict = {}
        list_keys = tweet_message.split(" ")
        for key in list_keys:
            if key not in bow_dict:
                bow_dict[key.lower()] = 0

        return bow_dict
