from flask import Flask, render_template, request, jsonify, make_response, session, url_for, redirect, flash, Markup
from urllib.request import urlopen
import simplejson
import pysolr
import time
from flask_paginate import Pagination, get_page_args


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
        results=solr.search(query,start=0,rows=200)
        end_time = time.time()  # End measuring time


        per_page = 10
        page = int(request.args.get('page', 1))
        # Retrieve total number of items in collection
        num_found=results.hits

        # Calculate the start and end index for the current page
        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        # Extract values from the Results object
        formatted_results = []
        for result in results:
            formatted_result = {
                'title': str(result['title'][0]) if 'title' in result else '',
                'link': str(result['link'][0]) if 'link' in result else '',
                'description': str(result['description'][0]) if 'description' in result else '',
                'pubDate': str(result['pubDate'][0]) if 'pubDate' in result else '',
                'source_id': str(result['source_id'][0]) if 'source_id' in result else '',
                'country': str(result['country'][0]) if 'country' in result else ''
            }
            formatted_results.append(formatted_result)

        # Retrieve items for the current page using list slicing
        pagination_results = formatted_results[start_index:end_index]

        # Create pagination object using Flask-Paginate
        pagination = Pagination(page=page, per_page=per_page,
                                    total=num_found, css_framework='bootstrap4')
        
        
        
        response_time = round(end_time - start_time,3)  # Calculate the response time
        return render_template('index.html',query=query,results=pagination_results ,pagination=pagination,num_found=num_found,response_time=response_time)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)