from models.database import collection, async_client
from models.database import collection_tg, async_client
import bson

class BaseDAO:
    collection = None
    @classmethod
    async def find_all(cls, filter_by: dict):
        results = await cls.collection.find(filter_by)
        return results
            
    @classmethod
    async def find_one_by_id(cls, id: str):
        id = bson.ObjectId(id)
        result = await cls.collection.find_one({'_id': id})
        return result
    
    @classmethod
    async def find_one(cls, document):
        result = await cls.collection.find_one(document)
        return result
            
    @classmethod
    async def add(cls, document: dict):
        result = await cls.collection.insert_one(document)
        return result.inserted_id
            

class DocumentDAO(BaseDAO):
    collection = collection


class TgIdsDAO(BaseDAO):
    collection = collection_tg

    @classmethod
    async def update_ids(cls, field_id, new_arr):
        result = await cls.collection.updateOne({'field_id': field_id}, {'$set': {'tg_chat_ids': new_arr}})
        return result.inserted_id
    
    