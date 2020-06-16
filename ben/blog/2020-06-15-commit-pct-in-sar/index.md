% Understanding 'commit%' in Sar
---

This post is my findings of what %commit means in sar output, why it can be over 100% and if it causes performance impacts.  I was looking at some examples at work where we would have %commits of 400% or more on a system that ran most of our job processing and trying to determine if that was a metric that we needed to be concerned about or not.

---

The default kernel config (`vm.overcommit_memory=0`, verified with `sysctl vm.overcommit_memory`) allows the kernel to overcommit memory without actually allocating it. This means a process can ask the kernel for some memory, the kernel can approve the request, but not actually allocate that memory until the process touches the memory.

In the case of 300% commit, it means that if all processes requesting memory all touch the memory the kernel says they can, you'd run out of memory, but it doesn't say much about how much actual memory is being used.

Since the oom-killer wasn't invoked during those times, I'm assuming it meant the processes didn't end up using all the memory they requested.

However, what could happen is that the file caches get pushed out of RAM, and since most of these files are NFS mounted, you would expect to see an increase in network traffic, because now file requests have to make a network connection instead of just writing to RAM.

Looking at sar, there does appear to be an increase in NFS read/write requests during that time (although the system is probably doing more work in general at that time)

`paste <(sar -r -f /var/log/sa/sa25 -s 09:00:00 -e 12:00:00) <(sar -n NFS -f /var/log/sa/sa25 -s 09:00:00 -e 12:00:00)`

Also, you can look at sar -R to see what it's doing with pages:

```
09:00:01 AM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit       09:00:01 AM   frmpg/s   bufpg/s   campg/s
09:10:01 AM  10434476  22445408     68.26     39028   5859092  27736404     84.36       09:10:01 AM   3785.69      0.70    136.54
09:20:01 AM   9674068  23205816     70.58     39216   6473732  40152764    122.12       09:20:01 AM   -318.65      0.08    257.56
09:30:01 AM  10108764  22771120     69.26     39524   6549068  24360088     74.09       09:30:01 AM    181.72      0.13     31.49
09:40:01 AM   7454844  25425040     77.33     39900   6664152  52412532    159.41       09:40:01 AM  -1109.98      0.16     48.13
09:50:01 AM   9987816  22892068     69.62     40072   6755176  24081988     73.24       09:50:01 AM   1059.18      0.07     38.06
10:00:01 AM   8643572  24236312     73.71     40296   6854760  34374092    104.54       10:00:01 AM   -562.15      0.09     41.65
10:10:01 AM   4799484  28080400     85.40     34544   9211052  52021380    158.22       10:10:01 AM  -1607.30     -2.41    985.22
10:20:01 AM   7045080  25834804     78.57     34712   9625184  24197952     73.60       10:20:01 AM    940.78      0.07    173.50
10:30:01 AM   6874768  26005116     79.09     35204   9850652  33695336    102.48       10:30:01 AM    -71.28      0.21     94.37
10:40:01 AM   1038856  31841028     96.84     34672   4663636 132264248    402.26       10:40:01 AM  -2440.70     -0.22  -2169.32
10:50:01 AM   2483432  30396452     92.45     34316   3789032 127326388    387.25       10:50:01 AM    604.98     -0.15   -366.28
11:00:01 AM   1050656  31829228     96.80     34584   4202224 135015484    410.63       11:00:01 AM   -600.63      0.11    173.21
11:10:01 AM   3281380  29598504     90.02     21908   2377984 133405108    405.73       11:10:01 AM    933.05     -5.30   -763.02
11:20:01 AM   2968336  29911548     90.97     22340   2721116 132674080    403.51       11:20:01 AM   -131.14      0.18    143.74
```
Here, you can see that as the commit% spikes to 400% at 10:40, that there are a lot of pages allocated (frmpg/s is negative), and a lot of cached pages deallocated (campg/s is negative).  This means processes were allocating a lot of RAM while the kernel was flushing disk cache, presumably to accommodate the requests by the processes.  After that, you can see that it slows down and actually has a net positive cache page allocation.

Unfortunately you can't tell how much page churn is happening, you can only tell if net allocations were +/-.

So, adding more RAM could increase the size of the file cache for file requests, which could improve performance.  But, the kbcached metric stays within an order of magnitude, while the commit bounces between 100 and 400%, so I wouldn't expect much of a change.

Here's a good article I found on memory allocation: [http://techblog.cloudperf.net/2016/07/how-linux-kernel-manages-application_18.html](http://techblog.cloudperf.net/2016/07/how-linux-kernel-manages-application_18.html)
