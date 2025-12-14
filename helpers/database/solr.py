import os
import pysolr

SOLR_URL = os.getenv("SOLR_URL", "http://solr:8983/solr/cbo")

solr = pysolr.Solr(
    SOLR_URL,
    always_commit=True,
    timeout=10
)
