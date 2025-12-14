import pysolr

solr = pysolr.Solr(
    "http://localhost:8983/solr/cbo",
    always_commit=True,
    timeout=10
)
