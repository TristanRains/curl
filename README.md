# curl.py

A Python script with mimicking basic 'curl' functionality using python's 'requests' module

arguments: -o/--output, -v/--verbose, -x/--headers, -u/--url, -m/--method, -p/--params, -j/--json

The output argumet is to provide an output file, a default file will be chosen if not provided

The verbose argument is to display final request before execution

The headers argument is to add custom headers

The url argument is to provide a target url

The method option is to provide a request method - GET, POST, PUT, DELETE

The params option is to provide parameters in json format

The json option is to provide a json body

Example use cases:

python3 curl.py -m GET -u http://target_ip:port/ -v -o res.txt

python3 curl.py -m GET -u https://google.com/ -v

python3 curl.py -m POST -u https://httpbin.org/ -p '{"name":"alice", "role":"developer"}' -v
