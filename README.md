# curl.py

A Python script mimicking basic `curl` functionality using python's `requests` module

## Arguments: 

* `-o, --output`: File path to save the response (default if no file provided)
* `-v, --verbose`: Display the final request details before execution
* `-x, --headers`: Add custom headers
* `-u, --url`: Target URL for the request
* `-m, --method`: HTTP request method(`GET`, `POST`, `PUT`, `DELETE`)
* `-p, --params`: Provide query parameters in JSON format
* `-j, --json`: Provide a JSON request body

## Example Usage:

```bash
python3 curl.py -m GET -u http://target_ip:port/ -v -o res.txt

python3 curl.py -m POST -u https://httpbin.org/ -p '{"name":"alice", "role":"developer"}' -v
```

## Prerequisites:

This script requires python3 and the `requests` package (all other imported modules are included with standard python)

Install the required package using pip:

```bash
pip install requests
```
