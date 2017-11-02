import json
from Bio import Entrez

from elasticsearch import Elasticsearch


def search(query):
    Entrez.email = 'dixonrj@vcu.edu'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='10',
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
results = search('bone marrow cancer')
id_list = results['IdList']
papers = fetch_details(id_list)

#for i, paper in enumerate(papers['PubmedArticle']):
#    print("{}) {}".format(i+1, paper['MedlineCitation']['Article']['ArticleTitle']))

json_data = json.dumps(papers)

print(json_data)
#print(papers)

#connect to our cluster and load genome publications by looping through 'papers'
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es.search(index='med_pubs_api', filter_path=['PubmedArticle.MedlineCitation.PMID', 'PubmedArticle.MedlineCitation.Article.Abstract.AbstractText'])

for a, paper in enumerate(papers['PubmedArticle']):
    es.index("med_pubs_api", "bone_marrow", json_data)



