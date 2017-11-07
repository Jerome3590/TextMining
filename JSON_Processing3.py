import json
import csv

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


#Write to CSV
f = csv.writer(open('pubMed.csv', 'w', encoding='utf-8'))

# Write CSV Header
f.writerow(summaries[0].keys())

for x in summaries:
    f.writerow(x.values())

