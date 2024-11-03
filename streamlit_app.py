import streamlit as st
import pandas as pd
import lightgbm as lgb
from flask_cors import CORS
from flask import Flask, request

def process(dict):
    print(1)
    user_df = pd.DataFrame(dict)
    print(2)
    num_col = user_df.select_dtypes(exclude = ['object']).columns.to_list()
    print(3)
    categ_col = user_df.select_dtypes(include = ['object']).columns.to_list()
    print(4)
    user_df[categ_col] = user_df[categ_col].astype('category')
    print(5)
    print(user_df)
    pred = round(load_3.predict(user_df).item())
    print(6)
    return str(pred)


if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)

    @app.route('/foo')
    def serve_foo():
        print(request.form)
        user_dict = {'Agentype': [request.form.get('Agentype')], 'Year': [int(request.form.get('Year'))], 'Month': [int(request.form.get('Month'))],
                'Murder': [int(request.form.get('Murder'))], 'VicAge': [int(request.form.get('VicAge'))], 'VicSex': [request.form.get('VicSex')],
                'VicRace':[request.form.get('VicRace')], 'Weapon': [request.form.get('Weapon')],
                'Relationship': [request.form.get('Relationship')], 'Circumstance':[request.form.get('Circumstance')],
                'VicCount': [int(request.form.get('VicCount'))], 'Region':[request.form.get('Region')]}
        res = process(user_dict)
        return res

    app.run(port=8888)


# We'll never reach this part of the code the first time this file executes!

# Your normal Streamlit app goes here:
x = st.slider('Pick a number')
st.write('You picked:', x)