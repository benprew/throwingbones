% Yule Log-Rolling (perl advent calendar)
---

Over the Christmas holiday I wrote a few posts for the Perl advent
calendar. I\'d like to share them here, if only for posterity. I believe
you should be able to view the [archived
original](http://perladvent.pm.org/2006/17/).\
\
\
Perl Advent Calendar 2006-12-17\
Yule Log-Rolling\
by Ben Prew\
\
When running automated processes, I find it incredibly useful to have
some sort of logging setup, so that I can see how long certain parts of
processing take. Or, even more importantly, if the process dies, I can
better determine what it was doing shortly before it bit the dust.\
\
At work, we have many automated and semi-automated processes that run at
a scheduled time. These processes all log to the same directory, which
makes it easier to find them. Also, I would like to automatically rotate
new files when they show up in this directory, and not have to deal with
any sort of configuration file.\
\
I could have done this with logrotate, or some other process, but I like
doing things in Perl, and I didn\'t want to interfere with existing
archiving processes on the box. With Logfile::Rotate I can eat my bûche
de Nöel and have it too.\
\
If I wanted to write a separate script to rotate all the log files for
me, it might look something like mod17e.pl (external):\
\
1 \#!/usr/bin/perl;\
2\
3 use Logfile::Rotate;\
4\
5 my \@logs = map {\
6 my \$file = \$\_;\
7 Logfile::Rotate-\>new(\
8 File =\> \$file,\
9 Gzip =\> \'lib\',\
10 Dir =\> \'/var/logs/dev.old\',\
11 Post =\> sub { unlink \$file } ); } ;\
12\
13 for (\@logs) { \$\_-\>rotate() }\
\
The default behavior is to leave an empty log file in the directory, but
all my processes will create their own files, if needed, so I would
rather just remove the file. This was easy to add with the Post
argument.\
\
Another benefit of Logfile::Rotate is that unlike an external binary, I
can embed it in my existing code. All of our current logging is done
though a mix-in, so I\'ve got a single point of contact for each process
that runs, regardless of where it logs to.\
\
This method is called log(), and it handles all the logging for each
file, as well as knowing which file to log to. This also gives me more
flexibility in how each log is rotated. A rotation could be triggered by
the process catching a signal, the number of logged messages exceeding
some threshold, the time elapsed since last rotation, or the log growing
too large (in an effort to avoid filling the partition), etc.\
\
So, if I wanted to rotate each log file at 100 Mb, regardless of when it
was last rotated, the code might look something like mod17i.pl
(internal):\
\
1 sub log\
2 {\
3 my (\$self, \$message) = \@\_;\
4\
5 \# logging stuff here.\
6\
7 if ( ( -s \$self-\>filename ) \> 100\_000\_000) {\
8 Logfile::Rotate-\>new(\
9 File =\> \$self-\>file\_name,\
10 Gzip =\> \'lib\',\
11 Dir =\> \'/var/logs/dev.old\',\
12 )-\>rotate;\
13 }\
14 }\
\
Having the log files rotate themselves, how great is that! Now we don\'t
have any other external scripts or configurations to maintain. Of
course, the downside to this approach is the implicit stat() on each
call to log(), but it shouldn\'t add too much overhead. This can even be
alleviated if there is only one process that writes to the log file,
since you could then have a counter that is initialized to the current
size of the file and then adds the size of the message to the counter.
Then, once the counter reached 100\_000\_000, you could rotate the log
file.\
SEE ALSO\
Log::Dispatch::FileRotate, logrotate(8)
