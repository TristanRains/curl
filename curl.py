"""
This Python script replicates core curl command functionality
Parses headers, parameters, and JSON
"""

import argparse
import sys
import time
import requests
import json
from datetime import datetime

def parse_args():
    # Parse command-line arguments for HTTP request configurations
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
    
def MakeRequest(output, verbose, headers, url, method, params, json):
    #Execute the HTTP request and handle output formatting
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
    
if __name__ == "__main__":
    # print information regarding which commands have been selected before making the request
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
