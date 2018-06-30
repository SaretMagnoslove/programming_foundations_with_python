import urllib.request

def readText():
    quotes = open(r"E:\Courses\udacity\programming_foundations_with_python\Lesson05Projects\movie_quotes.txt")
    content = quotes.read()
    quotes.close()
    checkProfanity(content)

def checkProfanity(text):
    connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+text)
    output = connection.read()
    print(output)
    connection.close()
    print('profanity alert') if "true" in output else ('safe text') if 'false' in output else ('I do not know')
readText()  
