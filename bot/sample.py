from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

default = 'Disculpa, no te entendí. Intenta de otra forma'
app = Flask(__name__) 
spanish_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter",
 logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                         'default_response': default,
                         'maximum_similarity_threshold': 0.90
                    },
                ])
trainer = ChatterBotCorpusTrainer(spanish_bot)
trainer.train("chatterbot.corpus.spanish")
trainer.train("data/data.yml")


@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     if userText.lower() == "sección 2" or  userText.lower() == "seccion 2" :
          return  "https://tesina-331906.oa.r.appspot.com/atls2"
     elif userText.lower() == "sección 3" or  userText.lower() == "seccion 3":
          return "https://tesina-331906.oa.r.appspot.com/apasels3"
     elif userText.lower() == "sección 4" or  userText.lower() == "seccion 4":
          return "https://tesina-331906.oa.r.appspot.com/fpvls4"
     elif userText.lower() == "sección 1" or  userText.lower() == "seccion 1":
          return "https://tesina-331906.oa.r.appspot.com/eels1"
     elif userText.lower() == "evaluación" or  userText.lower() == "evaluacion":
          return "https://forms.gle/TpT4UvoZBvKQ6kLU8"   
     responseText = str(spanish_bot.get_response(userText))
     if responseText == "What is AI?":
          return default
     else:
          return responseText


if __name__ == "__main__":
     app.run(debug = True)


