# postBL
This a simple python tool to detect time based sqli (POST based only). This tool takes three arguements, the raw request file directly copy-pasted from burpsuite, a list of time based sqli payloads, and the method of the request. The tool uses a delimiter named BHOOT in the post parameters as the injection point where you want to inject the payloads out of all the parameters. This BHOOT keyword must be specified in the params in the request file before running the tool. Note that the sample request file gives much delay in 1 unit time only. \
Lab links: https://github.com/skyblueee/sqli-labs-php7 , http://testphp.vulnweb.com/login.php
# Clonning and installation
~ git clone https://github.com/dotslashed/postBL \
~ cd postBL \
~ python3 postblis.py raw_request.txt payloads.txt http \
\
![alt text](https://github.com/dotslashed/postBL/raw/main/postblisi.PNG)
\
![alt text](https://github.com/dotslashed/postBL/raw/main/snip1.PNG)
\
\
\
\
\
\
Note: This tool is for educational and bug-bounty purposes only. The scripter is strictly not responsible for any miss usages of the tool. Thanks
