from models.database import database_url_redis
import redis.asyncio as redis


class RedisDAO:
    @classmethod
    async def __connect(cls):
        r = await redis.from_url(database_url_redis)
        return r


class PubSubDAO:
    stopword = 'STOP'

    @classmethod
    async def __connect(cls):
        r = await redis.from_url(database_url_redis)
        return r

    @classmethod
    async def subscribe_getting_pub(cls, *names):
        r = await cls.__connect()
        async with r.pubsub() as pubsub:
            await pubsub.subscribe(*names)
            while True:
                message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=None)
                if message != None:
                    if message['data'].decode() == cls.stopword:
                        return
                    yield message['data'].decode()
    
    @classmethod
    async def send_in_pub(cls, name, message):
        r = await cls.__connect()
        await r.publish(name, message)


class KeyValueDAO(RedisDAO):
    @classmethod
    async def set_value(cls, key, value):
        r = await cls.__connect()
        async with r.pipeline() as pipe:
            await pipe.set(key, value).execute()

    @classmethod
    async def get_value(cls, key):
        r = await cls.__connect()
        async with r.pipeline() as pipe:
            q = await pipe.get(key).execute()
            return q
        
    @classmethod
    async def exist_key(cls, key):
        r = await cls.__connect()
        async with r.pipeline() as pipe:
            q = await pipe.exists(key).execute()
            return q