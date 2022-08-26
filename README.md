# postBL
This a simple python tool to detect time based sqli (POST based only). This tool takes three arguements, the raw request file directly copy-pasted from burpsuite, a list of time based sqli payloads, and the method of the request. The tool uses a delimiter named BHOOT in the post parameters as the injection point where you want to inject the payloads out of all the parameters. This BHOOT keyword must be specified in the params in the request file before running the tool.
# Clonning and installation
~ git clone https://github.com/dotslashed/postBL \
~ cd postBL \
~ python3 postblis.py raw_request.txt payloads.txt http \
\
![alt text](https://github.com/dotslashed/postBL/raw/main/postblisi.PNG)
\
\
\
\
\
\
\
Note: This tool is for educational and bug-bounty purposes only. The scripter is strictly not responsible for any miss usages of the tool. Thanks
