#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, request
from app import app
import json
from .questions import Questions

q = Questions()

app.jinja_env.globals.update(print_question_by_name=q.print_question_by_name)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def render_question():
    form = request.form.to_dict()
    
    print(form)

    # need the calculate method to return data in this form
    return json.dumps({
        "status":"ok",
        "data": [70000, 140000, 190000, 250000, 270000, 310000, 380000, 450000]
    })

# @app.route('/questions')
# def render_question():
#     return render_template("question.html")


@app.route("/get_template", methods=["GET"])
def get_template():
    question_number = request.args.get("question_number")
    return render_template("subtemplates/question_subtemplate.html", question=questions_list[int(question_number)])

