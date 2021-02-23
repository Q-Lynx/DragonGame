from flask import Flask

from flask import request

from DragonGame import Dragon

dragons = {1:  Dragon("Wojtek",2), 2:  Dragon("Łukasz",1)}

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Smoki'
    

@app.route("/dragon/<dragon_id>", methods=['GET', 'POST'])
def dragon(dragon_id):
    if request.method == 'POST':
        data = dict(request.get_json())
        name = data['name']
        level = data['level']
        dragon = Dragon(name, level)
        did = int(dragon_id)
        dragons[did] = dragon
        return "Dragon {} was added with id: {}".format(dragons[did].name, did)
    elif request.method == 'GET':
        try:
            drag = dragons[int(dragon_id)]
            result = str(drag)
        except KeyError:
            result = "No dragon found"
        return result + "\n"
    else:
        raise Exception("Wrong HTTP method!")

if __name__ == "__main__":
    print(Dragon("Grzegorz"))

    app.run(host='127.0.0.1', port=5000)
  
