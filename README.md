# nanoavionics

## Monitor

Script file is located in scripts folder by name monitor.exe , execution has to be done in cmd or windows terminal. <br>

|Flag|Explanation|
|----|-----------|
|-f  |filename   |
|-d  |directory  |
|-q  |query      |
|-m  |monitor    |
|-r  |reader     |
|-s  |chunk size |

###Sample commands <br>
- monitoring log files and printing out into promt last entries:<br>
`monitor.exe -f test -d ../log/ -m True`

- searching for specific query in log files and saving search results in seperate log file with timestamp:<br>
`monitor.exe -f test -d ../log/ -q somephrase -s 100`

- reads any size log file in specified chunks of lines and prints content into the promt:<br>
`monitor.exe -f test -d ../log/ -r True -s 100`

