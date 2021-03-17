"""
Multi-Threading

"""
import threading
import requests

class PrintingTask(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self) # executing parent's constructor
        self.name = name


    def run(self):
        for i in range(1, 11):
            print("My Name is {}. Copy #{}".format(self.name,i))

class NewsApi(threading.Thread):

    def run(self):
        url = "http://newsapi.org/v2/everything?q=tesla&from=2021-02-17&sortBy=publishedAt&apiKey=98766a5c3b92426bb38aa54d129a8e8f"
        response = requests.get(url)
        print(response.text)


def main():
    print("Main Started.")

    news = NewsApi()
    news.start()
    
    ob1 = PrintingTask(name="Utkarsh Bhardwaj")
    ob1.start()




    print("Main Stopped.")



if __name__ == '__main__':
    main()