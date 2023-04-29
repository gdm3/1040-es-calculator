import pymongo, dns
global text
text = "PawskSmujwNjsohsrbhbad"
def Save():
  z = Check()
  print(z)
  print(z + 1)
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] +text[21]
  
  client = pymongo.MongoClient("mongodb+srv://Person:"+word+"@cluster0-u4jiy.mongodb.net/test?retryWrites=true&w=majority")
  db = client.beemoviecount

  data = db.beemoviecount
  
  result = db.beemoviecount.replace_one({ "num": str(z) }, { "num": str(Check() + 1) }, upsert=True)
  client.close()
def Check(): 
  word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[16] + text[21]


  client = pymongo.MongoClient("mongodb+srv://Person:"+word+"@cluster0-u4jiy.mongodb.net/test?retryWrites=true&w=majority")
  db = client.beemoviecount

  data = db.beemoviecount
  x = 0
  for x in data.find({}, { "_id": 0, "num": 1}):
      u = 0
  x = "'" + str(x) + "'"
  import re
  y = re.sub(r'[^\w\s]','',x)
  lst = [y]
  def convert(lst): 
      return ' '.join(lst).split()
  d = convert(lst)
  num = d[1]
  num = int(num)
  return num
  client.close()
