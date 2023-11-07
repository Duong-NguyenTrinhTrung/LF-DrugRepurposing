import os
from Bio import Entrez
from bs4 import BeautifulSoup
import requests

# Set an email address for Entrez API
Entrez.email = "truong128@gmail.com"

def search_pubmed(query):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=1000)
    record = Entrez.read(handle)
    return record["IdList"]


def fetch_titles_and_abstracts(pubmed_ids):
    papers = []
    for idx, pubmed_id in enumerate(pubmed_ids, start=1):
        handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
        xml_data = handle.read()
        soup = BeautifulSoup(xml_data, "xml")

        # Try to find the Title and AbstractText, and handle cases where they're not found
        try:
            title = soup.find("ArticleTitle").text
        except AttributeError:
            title = "Title not available for PMID: " + pubmed_id

        try:
            abstract = soup.find("AbstractText").text
        except AttributeError:
            abstract = "Abstract not available for PMID: " + pubmed_id

        papers.append({"Title": title, "Abstract": abstract})
    return papers


def filter_papers(papers, keywords):
    filtered_papers = []
    for paper in papers:
        if all(keyword.lower() in paper["Abstract"].lower() for keyword in keywords):
            filtered_papers.append(paper)
    return filtered_papers


def save_titles_and_abstracts_to_file(papers, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, paper in enumerate(papers, start=1):
            file.write(f"{idx}. {paper['Title']}\n")
            file.write(f"Abstract: {paper['Abstract']}\n\n")


def main():
    keywords = ["Alzheimer", "drug", "In vitro", "screening", "assay", "cell"]
    query = " ".join(keywords)
    
    
    pubmed_ids = search_pubmed(query)
    
    if not pubmed_ids:
        print("No articles found for the specified keywords.")
        return
    
    
    papers = fetch_titles_and_abstracts(pubmed_ids)
    
    
    filtered_papers = filter_papers(papers, keywords)
    
# Save titles and abstracts to a text file with numbering and blank lines
    save_titles_and_abstracts_to_file(filtered_papers, "Alzheimer_drug_assay_cell_titles_and_abstracts_limit_1millions.txt")

    print(f"{len(filtered_papers)} titles and abstracts saved to titles_and_abstracts.txt")

if __name__ == "__main__":
    main()

##### Keywords could be used for searching:#####
# Alzheimer's disease
# Drug screening
# Compound screening
# Therapeutics
# Drug discovery
# High-throughput screening
# Large molecules
# Macromolecules
# Biomolecules
# Protein targets
# Amyloid beta
# Tau protein
# Neuroprotection
# Disease-modifying
# Small molecules
# Chemical libraries
# In vitro screening
# In vivo screening
# Drug development
# Preclinical studies