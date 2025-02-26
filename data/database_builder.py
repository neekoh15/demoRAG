import sys
import json
import time
import asyncio

import chromadb
import chromadb.config
#import pymilvus

from data_types import VectorDocument


class MilvusBuilder:
    def __init__(self, path:str='./database/milvus', data_path='./data/data.json'):
        pass


class ChromaBuilder:
    def __init__(self, path:str='./database/chroma', data_path='./data/data.json'):
        settings = chromadb.config.Settings(
            anonymized_telemetry = False
        )
        self.data:dict[str, VectorDocument] = json.load(open(data_path, 'r', encoding='utf-8'))
        self.client = chromadb.PersistentClient(path=path, settings=settings)

    def create_default_collection(self, default:str='default'):

        collection = self.client.create_collection(name=default)

        return collection
    
    async def populate_default_collection(self, default='default'):
        collection = self.client.get_collection(name=default)

        documents = [d["document"] for _,d in self.data.items()]
        metadatas = [d["metadata"] for _,d in self.data.items()]
        uuids = [d["uuid"] for _,d in self.data.items()]
        
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids= uuids
        )

if __name__ == "__main__":

    builder = ChromaBuilder()
    builder.create_default_collection()
    asyncio.run(
        builder.populate_default_collection()
    )
    