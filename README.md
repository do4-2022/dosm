# dosm
DOSM DevOps System Monitor (Not to be confused with BDSM) is a system monitoring tool writtent in python that tracks various system informations (CPU usage, Disk Usage etc..)

## Worflow

Each person will work on his module. Everyone have to implements a package derived from the main frame. Those methods will be written in `./integrator/frame.py`.

### Logger

We will have two ways to communicate with the Logger :
- Metrics : Send a dictionnary / key->value object by the name of the metrics and the value. Te logger will retrieve the timestamp and write it on hi sown
Example : Chrome is consumming 54% CPU : ["cpu.chrome"][.54]

- Logs : Send a string with the name of the modul and the message

Methods :
- writeMetric
- readMetric
- readLog
- writeLog