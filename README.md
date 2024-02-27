# CS361-Microservice

Microservice that makes an API call to the Avalanche API (https://api.avalanche.org/v2/public/products/map-layer/SAC) for the Sierra Avalanche Center. The get_avalanche_data.py is a Flask app designed to handle the calls.

If the Flask app is running locally, a request can be made to localhost (ex: http://localhost:5000/avalanche). The Flask app will then make an API call to the Avalanche API. It will review the result, and only send back the Avalanche report if is current. If the report is out of date, it will return an error message asking the user to try again later. If no data or the API call fails, an error is returned stating that the data is not available.  If successful, the Flask app will return the updated Avalanche report for the day in a JSON format. Users should consider passing the a successful result into a variable in order to parse through the Avalanche report. The request_data.py has a sample on how to make a request.


![alt text](https://github.com/calmextex/CS361-Microservice/blob/main/UML%20Diagram.jpeg)
