# apogee2_work_activity
These are materials related to a work session at Mach 30's Apogee 2 event that will compare LiveCode
to Python/Kivy

For the activity, there will be both LiveCode and Python/Kivy teams who will be developing rough
prototype apps per requirements provided by a stakeholder team. The apps will be developed on the
fly, and the intention is for us to gain experience in each of the "competing" platforms. We'll
gain much needed hands-on experience addressing a real need that Mach 30 has - rocket test stand
software.

To learn more about the Apogee II event and this work activity, please visit the [Apogee II page](http://mach30.org/events/apogee/apogee-ii/)

In the 'Server' folder is a TCP server (deviceserver.py) that takes a Shepard test stand data file
name as an argument. The following is the command line used to launch the server, looking at the
provided Shepard data CSV file.
```
deviceserver.py -f 2013_6_11_15_8_37.csv
```
More information on the use of the server can be found by passing the `-h` option.
```
deviceserver.py -h
```
The server will read the timestamps from the provided file and will handle sending the samples at
the correct rate. Other CSV files may be used with the server, but they must be placed in the
'Server' directory with the deviceserver.py file, and must have the data in columns separated by
commas. The first column should be the timestamp, the second the force measurement, and the third
the temperature measurement, if applicable.

You may need to install Python on Windows. Just grab the latest 2.7.x version from python.org if
you need it.

To connect to the server from a client, connect to the server at 'localhost' and port 9999 and send
the 'R' character. This should give you a dump of the data back, with the proper delay between each
sample. Once a data dump is finished, you can send 'R' again to get the same data dump again.
