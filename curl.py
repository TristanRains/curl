#This script tries to replicate the functionality of the curl command using python's requests module

'''
We start with importing the necessary modules
We will need argparse to parse arguments from the terminal
We will need sys to exit the program cleanly
We will use time to add a delay and datetime to determine the start and completion times for the request
We will use JSON to parse json headers and parameters
Finally, we will use requests to handle our requests
'''
import argparse
import sys
import time
import requests
import json
from datetime import datetime

'''
This function parse_args() parses our arguments and returns the final args result
We have the option of -v for verbosity, with store true so that it is false by default
We have included a description and help features which can be accessed with python3 curl.py -h
We have inlucded an optional -o to provide an output file
We have included the option of headers, parameters, and json data for requests
We also included the url and method
'''
def parse_args():
    parser = argparse.ArgumentParser(description="Make requests to a specified URL and save the response to a file.")
    parser.add_argument('-o', '--output', type=str, help="Output file path, example: -o results.txt")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-x', '--headers', type=json.loads, help="Headers for the request in JSON format, example syntax: '{'User-agent': 'Example'}'")
    parser.add_argument('-u', '--url', type=str, help="Target URL for the request, examples: http://mysite.com or https://ip_address:port_num")
    parser.add_argument('-m', '--method', type=str, help="Method to use. Examples: GET,POST,PUT,DELETE")
    parser.add_argument('-p', '--params', type=json.loads, default={}, help="Parameters to use. Use following syntax: '{'username': 'John', 'password': 'admin'}'")
    parser.add_argument('-j', '--json', type=json.loads, default={}, help="For making a request with a JSON body. Example syntax '{'username': 'John', 'role': 'admin'}'")
    args= parser.parse_args()
    return args

'''
The function MakeRequest() has the parsed arguments as its arguments. We start by simulating a delay and recording the current start time
We then go through each argument and perform the appropriate action depending on which arguments are entered, verbose mode repeats the selected arguments
We do this by making a request to the target url with requests, headers, parameters and verify set to True to ensure secure communication
We then write the results to a text file, if the output file option is left empty, we create a filename results.txt and write to that instead
We write the response text if it exists else No response
We also attempt to read any json in the response else response is not in valid JSON format
Finally, we write the response to the output file before printing the completion time and exiting cleanly with sys.exit(0)
'''
def MakeRequest(output, verbose, headers, url, method, params, json):
    time.sleep(1)
    print(f"Request made at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if verbose:
        print(f"Making request with headers: {headers} to {url}, with parameters: {params} and json body: {json}")
    if method.upper() == 'GET':
        print("Performing GET request")
        request = requests.get(url, headers=headers, verify=True)
    elif method.upper() == 'POST':
        print("Performing POST request")
        request = requests.post(url, headers=headers, params=params, data=json, verify=True)
    elif method.upper() == 'PUT':
        print("Performing PUT request")
        request = requests.put(url, headers=headers, verify=True)
    elif method.upper() == 'DELETE':
        print("Performing DELETE request")
        request = requests.delete(url, headers=headers, verify=True)
    if output:
        output = output
    else:
        print("No output file provided, saving to results.txt")
        output= "results.txt"
    with open(output, 'w') as f:
        response_text = request.text if request else "No response"
        response_status = request.status_code if request else "No status code"
        f.write(str(response_status)+"\n")
        f.write(str(response_text)+"\n")
        try:
            json_response = request.json()
            f.write("\n\nJSON Response:\n")
            f.write(str(json_response))
        except ValueError:
            print("Response is not in JSON format")
    print(f"Response written to {output}")
    print(f"Request completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sys.exit(0)

'''
In our main code block, we call the arg_parse function to parse any arguments
We then go through args to check which arguments are provided and print the chosen arguments
'''
if __name__ == "__main__":
    args = parse_args()
    print(f"Output file: {args.output}")
    if args.url:
        print(f"Target URL: {args.url}")
    if args.verbose:
        print("Verbose mode enabled")
    if args.headers:
        print(f"Headers enabled")
    if args.output:
        print(f"Output file path: {args.output}")
    if args.method:
        print(f"Method: {args.method}")
    if args.params:
        print(f"Selected parameters: {args.params}")
    if args.json:
        print(f"Chosen JSON body: \n{args.json}")
    MakeRequest(args.output, args.verbose, args.headers, args.url, args.method, args.params, args.json)
