from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class BlogPostIndex(Document):
    class Index:
        name = 'blog-index'

    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'blog-index'


def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es,
         actions=(b.indexing()
                  for b in models.BlogPost.objects.all().iterator()))


def search(title):
    s = Search().query('term', title=title)
    response = s.execute()
    return response