import chromadb
import chromadb.config
import chromadb.utils


class ChromaHttp:
    def __init__(self, host:str = 'localhost', port:int = 8000):
        settings = chromadb.config.Settings(
            anonymized_telemetry = False
        )

        self.client = chromadb.HttpClient(
            host=host,
            port=port,
            settings=settings
        )

        self._default_collection = 'default'

    def retrieve_documents(self, query:str|list ) -> list[dict]:

        collection = self.client.get_collection(name=self._default_collection)

        query_results = collection.query(
            query_texts= [query] if isinstance(query, str) else query
        )

        documents = []
        for documents_results in query_results["documents"]:
            documents.extend(documents_results)

        metadatas = []
        for metadatas_results in query_results['metadatas']:
            metadatas.extend(metadatas_results)

        distances = []
        for distances_results in query_results['distances']:
            distances.extend(distances_results)

        results = []

        for doc, meta, distance in zip(documents, metadatas, distances):

            result = {
                "document": doc,
                "metadata": meta,
                "distance": distance
            }
            results.append(result)

        return results

        

        