import json

sourcefile = open("data/infile.json", "rb")

json_data = json.load(sourcefile)

summaries = []
for article in json_data['PubmedArticle']:
    try:
        summaries.append({
            'id': article['MedlineCitation']['PMID'],
            'text': article['MedlineCitation']['Article']['Abstract']['AbstractText']
        })
    except KeyError:
        pass

json.dump(summaries, open('data/outfile.json', 'w'))
