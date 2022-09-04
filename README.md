# nanoavionics

## monitor.exe
Script file is located in scripts folder by name monitor.exe , **execution has to be done in cmd or windows terminal**. <br>

|Flag|Explanation|
|----|-----------|
|-f  |filename   |
|-d  |directory  |
|-q  |query      |
|-m  |monitor    |
|-r  |reader     |
|-s  |chunk size |

### Sample commands <br>
1. monitoring log files and printing out into promt last entries:<br>
`monitor.exe -f test -d ../log/ -m True`

2. searching for specific query in log files and saving search results in seperate log file with timestamp:<br>
`monitor.exe -f test -d ../log/ -q somephrase -s 100`

2. reads any size log file in specified chunks of lines and prints content into the promt:<br>
`monitor.exe -f test -d ../log/ -r True -s 100`


## tle4m6p.exe
File is located in scripts folder by name tle4m6p.exe. To **execute click it twice** and give it a second to download and filter TLE messages
for M6P satellite. After script is done a new log file with timestamp is saved at the current woring directory.
