from getWord import getWordForGame as gWFG

url = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"

module = gWFG(url)
print(module.chooseRandom())