#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, request
from app import app
import json
from pprint import pprint as pp
from .questions import Questions
import numpy as np
from HH.litill_islendingur import litill_islendingur

q = Questions()

app.jinja_env.globals.update(print_question_by_name=q.print_question_by_name)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def render_question():
    form = request.form.to_dict()
    print(form)

    #TENGDAR BREYTUR
    manadarleg_laun_fyrir_skatt = int(form['monthly_pretax_salary_income'])
    hjuskaparstada = 1 if "einhleyp" in form['hjuskaparstada'] else 2
    busetuform = 1 if "leigi" in form['form_busetu'] else 2
    fjoldi_barna = int(form['number_of_children'])
    fjoldi_barna_undir_7 = int(form['children_under_7'])
    sereignaridgjald = float(form['lifeyrissjodur_framlag'].replace("%","")) / 100

    bakgrunnsuppl = {'hjuskaparstada': hjuskaparstada,  # '1: einhleypur, 2: einst. foreldri, 3: giftur/sambud '
                     'busetuform': busetuform,  # '1: eigin, 2: leigu/busetu, 3: hvorugt '
                     # [laun_a_manudi, fjarmagnstekjur, laun_maka, fjarmagnstekjur_maka]
                     'tekjur': [manadarleg_laun_fyrir_skatt, 0, 0, 0],
                     'eignir': 5000000.0,
                     'husnaedislan': 35000000,
                     'vaxtagjold': 2000000,
                     'husnaediskostnadur': 250000,
                     'fjoldi_heimilismanna': 3,
                     'heimilistekjur': 200000,  # tekjur annarra en viðkomandi/hjóna
                     'heimiliseignir': 5000000,  # eignir annarra en viðkomandi/hjóna
                     'fjoldi_barna': fjoldi_barna,
                     'fjoldi_barna_undir_7': fjoldi_barna_undir_7,
                     'idgjald': 0.04,
                     'sereignaridgjald': sereignaridgjald,
                     'serstakar': 0,
                     'ororkuhlutfall': 0,
                     'fyrsta_75_mat': 0,
                     'byr_einn': 0,
                     'hreyfihomlun': 0,
                     'medlag_fj': 0,
                     'aldur': 0,
                     'frestun_ellilifeyris': 0,
                     }

    # TODO: baeta inn i results:
    #1: tekjur eftir skatt
    #2: radstofunartekjur -> leggja saman allar breytur sem mynda radstofunartekjur


    arr = []
    for i in np.arange(300000,1000000,100000):
        bakgrunnsuppl['tekjur'][0] = i
        arr.append(litill_islendingur(bakgrunnsuppl))

    # print(arr)
    results = litill_islendingur(bakgrunnsuppl)

    # need the calculate method to return data in this form
    return json.dumps({
        "status":"ok",
        "radstofunartekjur": [70000, 140000, 190000, 250000, 270000, 310000, 380000, 450000],
        "results":results
    })

# @app.route('/questions')
# def render_question():
#     return render_template("question.html")


@app.route("/get_template", methods=["GET"])
def get_template():
    question_number = request.args.get("question_number")
    return render_template("subtemplates/question_subtemplate.html", question=questions_list[int(question_number)])

