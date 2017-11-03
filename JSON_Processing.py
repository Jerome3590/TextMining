import json

sourcefile = open("data/marrow.json", "rb")

json_data = json.load(sourcefile)

summaries = []
for hit in json_data['hits']['hits']:
    for article in hit['_source']['PubmedArticle']:
        summaries.append({
            'id': article['MedlineCitation']['PMID'],
            'text': article['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
        })

json.dump(summaries, open('data/outfile.json', 'w'))
