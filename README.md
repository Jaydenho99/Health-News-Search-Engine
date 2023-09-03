# Health-News-Search-Engine
Building Health News Search Engine using SOLR

Due to the overwhelming health information available, a health domain search engine is implemented to allow users to navigate and search for a wide range of health-related information. It is difficult to build an efficient search engine due to several challenges. Therefore, this search engine will only cover news articles of health-related information. The contents of the health-related information are limited to the following three sample queries.

Query: Issues related to covid

Description of relevant results: Relevant results should contain recent news articles that provide up-to-date information about covid-related topics such as covid vaccination, a new variant of covid and government legislation. Besides that, it should also cover scientific articles related to covid. The results containing healthy diet and other diseases except covid are less relevant.

Query: What is heart disease

Description of relevant results: Relevant results should contain relevant news articles that provide information about heart disease and cardiovascular disease and provide information on providing tips to reduce getting heart disease. The results containing vaccines and mental health are less relevant.

Query: Information about mental health

Description of relevant results: Relevant results should contain relevant news articles that provide an overview of mental health issues. The results containing vaccine and covid are less relevant.

## Design of Search Engine

1. Keyword Expansion
   Keyword expansion is a function that involves expanding the search queries or terms by including synonyms to improve retrieval accuracy. Some of the keyword expansion is done for the following terms
   covid -> corona, covid 19, coronavirus, SARS CoV 2, novel coronavirus
   cardiovascular -> heart related, cardiac, cardiovascular health, cardiopulmonary, cardiomyopathy, atherosclerosis, heart
   mental health -> emotional, mental, psychological, mind health, depression, suicide, suicidal, stress

2. Ranking and relevance score
   Provides the ranking and relevance score using the TF-IDF (Term Frequency-Inverse Document Frequency). TF-IDF technique will give a higher weightage score to terms that frequently appear in a document but are uncommon across the entire dataset. Documents with higher relevance scores are considered more relevant to the search query and placed at the top of the search results.

3. Highlighting words
   This feature highlights phrases or words in the search results based on user queries. This feature allows users to quickly identify the relevant parts within the document and provide a summary of why a specific document is significant.

4. Spell checker
   This feature helps users to correct misspelled words and retrieve accurate search results. The spell checker in this search engine will automatically suggest alternative words based on the highest term frequency in the indexed data.

5. Re-rank querying
   Improve the search results by enhancing the relevance and ordering of the search results based on specific criteria. In this search engine, the presence of the terms “covid”, “mental health”, “cardiovascular”, and “heart disease” in both the title and description fields are identified as the key relevance feature in the re-rank querying process.

## Interface

Query Output
![image](https://github.com/Jaydenho99/Health-News-Search-Engine/assets/77521676/2d948b02-b06d-4ab9-9d0c-05f58667f639)

![image](https://github.com/Jaydenho99/Health-News-Search-Engine/assets/77521676/2aa0364e-84c2-478f-afd1-7e6174f64f46)

![image](https://github.com/Jaydenho99/Health-News-Search-Engine/assets/77521676/4064e41d-1501-4f87-9c83-d74694a30a97)

Spell Checker
![image](https://github.com/Jaydenho99/Health-News-Search-Engine/assets/77521676/caaf26f5-f079-4b66-93d3-f9843e221fe0)




