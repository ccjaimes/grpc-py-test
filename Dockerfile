FROM python:3.12-alpine

WORKDIR /src
COPY requirements.txt /src

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf ~/.cache/pip
    
COPY . /src

RUN python3 -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. protos/users.proto && \
    rm -rf protos

CMD [ "python3", "app.py" ]