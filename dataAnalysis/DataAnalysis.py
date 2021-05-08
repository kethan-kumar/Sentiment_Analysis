import DataRetriever
from datetime import datetime


class DataAnalysis:

    def __init__(self):
        print("-------------------Initializing App---------------")
        self.data_retriever = DataRetriever()
        list_docs_created_time = self.data_retriever.document_retriever()
        timestamp_store = "index,tweet_created_at\n"
        index = 0
        for created_time in list_docs_created_time:
            index=index+1
            dtime = created_time
            print("Creating date time from created at twitter string value")
            new_datetime = datetime.strftime(datetime.strptime(dtime, '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')

            print("Creating timestamp")
            tweet_datetime= datetime.strptime(new_datetime,'%Y-%m-%d %H:%M:%S')
            timestamp = datetime.timestamp(tweet_datetime)

            print("Appending to string")
            timestamp_store = timestamp_store+str(index)+','+str(timestamp)+'\n'

        print("Inserting timestamp contents into CSV file")
        f = open("timestamps.csv", "w+")
        f.write(str(timestamp_store))
        f.close()
