import json
from Bio import Entrez


def search(query):
    Entrez.email = 'dixonrj@vcu.edu'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='3000',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'dixonrj@vcu.edu'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

#query medpub api and return results as json
results = search('bone marrow transplant')
id_list = results['IdList']
papers = fetch_details(id_list)

json_data = json.dumps(papers)

print(json_data)
json.dump(papers, open('data/infile.json', 'w'))
