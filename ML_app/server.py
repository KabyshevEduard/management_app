import grpc
import protobuf_pb2_grpc
import protobuf_pb2
import asyncio
import logging

class PredictionServicer(protobuf_pb2_grpc.PredictionServiceServicer):
    async def MakePred(self, request, unused_context):
        #
        # Predictions
        #
        p = request.rating * request.message_id
        resp = protobuf_pb2.PredictResponse(p=p)
        return resp


async def serve():
    server = grpc.aio.server()
    protobuf_pb2_grpc.add_PredictionServiceServicer_to_server(PredictionServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())