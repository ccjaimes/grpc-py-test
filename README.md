# gRPC Client-Server Application with Python
This is a basic Python implementation of two apps communicating using the RPC protocol. The idea is that these apps can communicate using multiple stream patterns such as client-side, server-side and bidirectional streaming requests.
## How to run both apps?
### Server
The server is implemented in the ***app.py*** file. Before running it, you could define a specific port to listen setting the RPCPORT env variable, else it will be 50051 by default. You can optionally define a RUNNER env with a name that you want to greet with on your server.

To run the server, execute the command ***python app.py***
### Client
To run the client, execute the command ***python clientapp.py***. The app works interacting with the console directly. It will ask for a server URL in case is hosted in other instance, else just defaults to "localhost". 
