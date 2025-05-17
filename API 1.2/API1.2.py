import socket  # Import the socket library

# Step 1: Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
server_address = ('postman-echo.com', 80)  # Address and port number
client_socket.connect(server_address)

# Step 3: Prepare POST request data
post_data = "name=Jack&age=28"  # The data thats being sent 

headers = [
    "POST /post HTTP/1.1",
    "Host: postman-echo.com",
    "Content-Type: application/x-www-form-urlencoded",
    f"Content-Length: {len(post_data)}",
    "", post_data  
]

# Combine headers and body
request = "\r\n".join(headers)

# Step 4: Send the request
client_socket.send(request.encode())  # Send data to the server

# Step 5: Receive the response
response = client_socket.recv(4096)  # Receive up to 4096 bytes
print("Response from server:")
print(response.decode())  # Print the response

# Step 6: Close the connection
client_socket.close()