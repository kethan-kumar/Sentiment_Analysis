import MongoDB_DAO


class DataRetriever:

    def document_retriever(self):
        collection_list = []
        mongoDb = MongoDB_DAO("ProcessedDb")
        for record in mongoDb.retrieve_tweets("Twitter_Search_Collection"):
            collection_list.append(record['created_at'])

        return collection_list

