import urllib.request
crimefile1 = open("crops_url_list.txt", 'r')
yourResult1 = [line.strip() for line in crimefile1.readlines()]
count = len(yourResult1)
def image_request(url, file):
    response = urllib.request.urlopen(url)
    fh = open(file, "wb") #open the file for writing
    fh.write(response.read()) 
    
for i, url in enumerate(yourResult1):
    image_request(url, "image_name_" + str(i) + ".jpg")

crimefile2 = open("crops_url_list.txt", 'r')
yourResult2 = [line.strip() for line in crimefile2.readlines()]
count = len(yourResult2)

def image_request(url, file):
    response = urllib.request.urlopen(url)
    fh = open(file, "wb") #open the file for writing
    fh.write(response.read()) 
    
for i, url in enumerate(yourResult2):
    image_request(url, "crop_name_" + str(i) + ".jpg")
