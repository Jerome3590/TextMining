# TextMining

![Text Mining Mind Map](https://user-images.githubusercontent.com/9680556/32329379-4e50d368-bfb3-11e7-9c14-5ad25b6d7d51.PNG)

Step 1. Get the data.
            - PyCharm w bipython package/pubmed API
            https://github.com/Jerome3590/TextMining/blob/master/BoneMarrow_medpub.py
           

Step 2. Explore the data
            - Elasticsearch with Kibana
            - Identify target fields of interest
            - Elasticsearch query with _sourcefilter
            - curl command to output file
            https://github.com/Jerome3590/TextMining/blob/master/MedPub_script.bash.sh
            https://github.com/Jerome3590/TextMining/blob/master/marrow.json
            
                
Step 3. Format the data for processing
            - Credit to PyRVA's ![Chris May](https://github.com/Chris-May) for helping me put this script together            
            https://github.com/Jerome3590/TextMining/blob/master/JSON_Processing.py (for Elasticsearch output)
            https://github.com/Jerome3590/TextMining/blob/master/JSON_Processing3.py (for pubmed API output)
            https://github.com/Jerome3590/TextMining/blob/master/outfile.json
            https://github.com/Jerome3590/TextMining/blob/master/pubMed.csv (CSV version)
            

Step 4. Choose NLP Model based on Requirements
            - Additional file processing depending on NLP model selection
            
    
Step 5. Perform NLP and Analyze Results with Databricks
