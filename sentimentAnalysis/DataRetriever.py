from sentimentAnalysis.MongoDB_DAO import MongoDB_DAO


class DataRetriever:

    def document_retriever(self):
        collection_list = []
        mongodb_dao = MongoDB_DAO("ProcessedDb")
        for record in mongodb_dao.retrieve_tweets("Twitter_Search_Collection"):
            collection_list.append(record['text'])
        return collection_list
