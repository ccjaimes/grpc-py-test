### First stage to pull dependencies and build grpc files
FROM python:3.12-alpine AS compile-image

WORKDIR /src

### Create a Virtual env to centralize all dependencies in a fresh singular folder within the container
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /src

### Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    
### Process to build necessary files for our app to function
COPY . /src
RUN python3 -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. protos/users.proto

### Second stage to pull minimum files to execute and expose service
FROM python:3.12-alpine AS expose-image

### Pull the virtual env with dependencies and minimum code files for our app to function
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /src/app.py /src/users_pb2.py /src/users_pb2_grpc.py /src/users_pb2.pyi /

CMD [ "python3", "app.py" ]