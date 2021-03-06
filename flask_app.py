from flask import Flask, render_template,request, redirect
from flask import session
from random import shuffle

from main import get_next_question, get_vopros_by_id, get_max_question, get_all_quischen

def index():
    session["N"] = 0
    session["rt_ar"] = 0
    session["ct"] = 0
    return render_template("index.html", victoriny=get_all_quischen())

def test():
    if request.method == "GET":
        if session ["N"] == get_max_question(session["n_vic"]):
            return finish()

        next_question_id = get_next_question(session["n_vic"],session["N"])
        vopros_data = get_vopros_by_id(next_question_id)

        vopros_id = vopros_data[0]
        vopros =vopros_data[1]
        right_answers = vopros_data[2]
        all_answers = [vopros_data[2],vopros_data[3],vopros_data[4], vopros_data[5]]
        shuffle(all_answers)

        session["N"] += 1
        return render_template("test.html",
                                vopros=vopros,all_answers=all_answers,
                                right_answer= right_answers)

    else:
        session["ct"] += 1
        if request.form.get("refresh")== request.form.get("rignt_answer"):
            session["rt_ar"] += 1
        return redirect("/test")

def finish():
      return render_template("finish.html", Baunti = session["rt_ar"],
                                                            Twix=session["ct"])

def setN():
    session["n_vic"] =  int(request.form.get("id_victoriny"))
    return redirect("test")

app = Flask(__name__,template_folder="",static_folder="")
app.config["SECRET_KEY"] = "aboda"

app.add_url_rule("/","index",index)
app.add_url_rule("/setN","setN",setN, methods=["POST"])
app.add_url_rule("/test","test",test,methods=["GET","POST"])
app.add_url_rule("/finish","finish",finish)
app.run()

