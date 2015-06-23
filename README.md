# apogee2_work_activity
These are materials related to a work session at Mach 30's Apogee 2 event that will compare LiveCode
to Python/Kivy

For the activity, there will be both LiveCode and Python/Kivy teams who will be developing rough
prototype apps per requirements provided by a stakeholder team. The apps will be developed on the
fly, and the intention is for us to gain experience in each of the "competing" platforms. We'll
gain much needed hands-on experience with a real need that Mach 30 has - rocket test stand software.

To learn more about the Apogee II event and this work activity, please visit the [Apogee II page](http://mach30.org/events/apogee/apogee-ii/)

In the server folder is a TCP server that just spits out the same 10 lines of (real) Shepard data 10 times over. There's no time lag between sending each line of the samples. In a future version I'll set it up so that you can specify a CSV file's path on the command line and it will handle sending the samples at the correct rate. At least this way you can get started. 

To use the server, change into the 'Server' directory and run [python deviceserver.py]. You may need to install Python on Windows. Just grab the latest 2.7.x version from python.org if you need it.

If you connect to the server at 'localhost' and port 9999 and send the 'R' character, you should get a dump of the data back. First column is time, second is thrust, third is temperature (disabled and so it shows 0.0).
