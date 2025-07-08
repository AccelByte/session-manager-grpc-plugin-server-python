#!/bin/bash

# Generate protobuf code
rm -rf src/app/proto/*_grpc.py \
        src/app/proto/*_pb2.py \
        src/app/proto/*_pb2.pyi \
        src/app/proto/*_pb2_grpc.py
protoc-wrapper -I/usr/include  \
        --proto_path=app/proto=src/app/proto \
        --python_out=src \
        --grpc-python_out=src \
        src/app/proto/*.proto
