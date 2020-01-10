import os
import pandas as pd
import numpy as np
# from sklearn.utils import shuffle
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import confusion_matrix
# import seaborn as sns
# import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support
from sklearn.externals import joblib

#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template,request
import json
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"
#db = SQLAlchemy(app)

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(db.engine, reflect=True)

# Save references to each table
#Samples_Metadata = Base.classes.sample_metadata
#Samples = Base.classes.samples

import pickle
model = joblib.load('finalproject.pkl')

@app.route("/")
def index():
    # """Return the homepage."""
    return render_template("index.html")


#@app.route("/names")
#def names():
#    """Return a list of sample names."""

    # Use Pandas to perform the sql query
#    stmt = db.session.query(Samples).statement
#    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
#    return jsonify(list(df.columns)[2:])
@app.route('/_getlyrics', methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        payload = json.loads(request.data)
        value = payload['value']
        print (value)
        print(model.predict(value))
        
        return 'success'
    return 'false'

if __name__ == "__main__":
    app.run(debug = True)

