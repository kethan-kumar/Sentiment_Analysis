import math

from sentimentNewsAnalysis.MongoDB_DAO import MongoDB_DAO


class DataRetriever:

    def __init__(self):
        self.mongoDb = MongoDB_DAO("ProcessedDb")
        self.per_document_count_list = []
        self.list_of_keys = ["canada", "rain", "hot", "cold"]
        self.searchQueryCount = {}
        print("Retrieve Tweets and News Articles ...")
        self.totalDocuments = self.mongoDb.retrieve_tweets("Twitter_Search_Collection")

        for item in self.list_of_keys:
            self.searchQueryCount[item] = 0
        self.display_count_keywords_in_documents()
        self.display_count_keywords_in_each_documents()

    def display_count_keywords_in_documents(self):
        print("Total size of document is:" + str(self.totalDocuments.count()))
        self.count_occurrence_in_docs()
        print("=====================-Output Overall Keyword Count in all documents=================================-")
        print("|%s| ==== |%s| ===== |%s| ===== |%s|\n" % ("Search query", "Documents containing term(df)",
                                                          "Total Documents(N)/ numberof documents term appeared(df)",
                                                          "Log10(N/df)"))
        for item in self.list_of_keys:
            if self.searchQueryCount[item] != 0:
                print("|%s| ==== |%s| ===== |%s| ===== |%s|\n" % (item, self.searchQueryCount[item],
                                                                  str(self.totalDocuments.count()) + "/" + str(
                                                                      self.searchQueryCount[item]),
                                                                  math.log10(self.totalDocuments.count() /
                                                                             self.searchQueryCount[
                                                                                 item])))

    def display_count_keywords_in_each_documents(self):
        print("=====================Output Overall Keyword Count in each document=================================-")
        highest_freq_count_tracker = {}
        highest_freq_document_tracker = {}
        for keyword in self.list_of_keys:
            print("TERM:" + keyword)
            highest_freq_count_tracker[keyword] = -1
            highest_freq_document_tracker[keyword] = {}

            print("|%s| ==== |%s| ===== |%s| ===== |%s|\n" % (
                keyword + " appeared in" + str(self.searchQueryCount[keyword]) +
                "documents", "Total Words (m)",
                "Frequency (f )", "relative frequency(f/m)"))
            print("\n")
            for dict_count in self.per_document_count_list:

                print("|%s| ==== |%s| ===== |%s| ====== |%s|\n" % (dict_count["document_text"],
                                                                   dict_count["total_words"], dict_count["frequency"],
                                                                   dict_count["relative_frequency"]))
                if dict_count["document_text"].find(keyword) > -1:
                    if highest_freq_count_tracker[keyword] < dict_count["relative_frequency"]:
                        highest_freq_count_tracker[keyword] = dict_count["relative_frequency"]
                        highest_freq_document_tracker[keyword] = dict_count

        print("=========== Highest relative count for each keyword ==========")
        print("|%s| ******* |%s| ******* |%s| ******* |%s|\n" % ("Article text", "Keyword", "Frequency",
                                                                 "relative frequency(f/m)"))
        for article in highest_freq_document_tracker:
            dict_article = highest_freq_document_tracker[article]
            print("|%s| ******* |%s| ******* |%s| ******* |%s|\n" % (dict_article["document_text"],
                                                                     dict_article["frequency"],
                                                                     dict_article["keyword"],
                                                                     dict_article["relative_frequency"]))

    def count_occurrence_in_docs(self):
        counter = 0

        for document in self.totalDocuments:
            for keyword in self.list_of_keys:
                if document["text"].lower().find(keyword) > -1:
                    self.searchQueryCount[keyword] = self.searchQueryCount[keyword] + 1
                    counter = counter + 1
                    self.count_occurrence_within_each_doc(document["text"].lower(), keyword, counter)
        print(self.per_document_count_list)

    def count_occurrence_within_each_doc(self, text, keyword, counter):
        word_count = text.count(keyword)
        self.per_document_count_list.append({"articleNo.": "Article #" + str(counter),
                                             "document_text": text,
                                             "total_words": len(text.split(" ")),
                                             "frequency": word_count,
                                             "relative_frequency": word_count / len(text.split(" ")),
                                             "keyword": keyword})
