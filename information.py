import  urllib3.request
import requests
def main():
    ans = input("What information you went to get? \n1. Headers \n2. Dns information \nEnter the Number: ")
    url = raw_input("Enter the url: ")
    if(ans==1):
        header(url)
    elif(ans==2):
        dns(url)
def header(url):
    http = urllib3.PoolManager()
    url =  http.request('GET',url)
    print(url.headers)
def dns(url):
    result = requests.get("https://api.hackertarget.com/hostsearch/?q={}".format(url))
    print(result.text)


main()