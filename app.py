from flask import Flask, render_template, request, jsonify, make_response, session, url_for, redirect, flash, Markup
from urllib.request import urlopen
import simplejson
import pysolr
import time

app = Flask(__name__)
app.secret_key = "super secret key"
solr = pysolr.Solr('http://localhost:8983/solr/searchengine', timeout=10)
if(solr):
    print("Successfully connect to SoLR")
else:
    print("Failed to connect to SoLR")


@app.route('/home', methods=["POST","GET"])
def home():

    if request.args.get('search-btn'):
        
        query=request.args.get('search')
        start_time = time.time()  # Start measuring time
        results=solr.search(query,start=0,rows=40)
        end_time = time.time()  # End measuring time
        num_found=results.hits
        response_time = round(end_time - start_time,3)  # Calculate the response time
        return render_template('index.html',query=query,results=results,num_found=num_found,response_time=response_time)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
