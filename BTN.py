#coding=utf-8

#──────────────────────────────────────────────────
#  Coded By *Din-zUgex95
#  You may recode this script for learning,
#  If you want to reupload include the source !!!!
#──────────────────────────────────────────────────


#____Import Module
import os,sys,time


#____Color Code

#   \033[90m     -    Gray
#   \033[91m     -    Red
#   \033[92m     -    Green
#   \033[93m     -    Yellow
#   \033[94m     -    Dark Blue
#   \033[95m     -    Purple
#   \033[96m     -    Light Blue
#   \033[97m     -    White


#____Banner
banner="""\033[94m
  ────────────────────────────────
   \033[97m| \033[91m°°\033[041m\033[97m EXTRA KEY FOR TERMUX \033[0m\033[91m°° \033[97m|
   |   Youtube \033[91m: \033[90mDin-zUgex95    \033[97m|
   |   Github  \033[91m: \033[90m/Din-zUgex95   \033[97m|
  \033[94m────────────────────────────────"""

#____Selection Menu
menu="""   \033[94m|\033[93m1\033[94m| \033[97mFull Button
   \033[94m|\033[93m2\033[94m| \033[97mArrow Keys
  \033[94m_________________
   |\033[93m3\033[94m| \033[91mExit
"""

#____Extra Button
Key1 = "extra-keys = [['TAB','*','_','ESC','ALT','UP','END'],['HOME','-','/','CTRL','LEFT','DOWN','RIGHT']]"
Key2 = "extra-keys = [['CTRL','','','UP','DOWN','LEFT','RIGHT']]"

#____Make a Folder
os.system('mkdir /data/data/com.termux/files/home/.termux')
os.system("clear")
time.sleep(1.2)
print (banner)
print (menu)

#____Open Youtube
#def yt():
#    os.system("xdg-open https://youtube.com/Din-zUgex95")

def wait():
    print
    time.sleep(1)
    print "   \033[94m|  \033[97mWait  \033[94m|"
    time.sleep(4)

def succes():
    print "   \033[94m| \033[92mSucces \033[94m|"
    print
#    time.sleep(1)
#    yt()


#____Full Button
def full():
    wait()
    x = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
    x.write(Key1)
    x.close()
    os.system("termux-reload-settings")
    succes()

#____Arrow Only
def arrow():
    wait()
    x = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
    x.write(Key2)
    x.close()
    os.system("termux-reload-settings")
    succes()

#____Input
time.sleep(0.3)
c = raw_input("   \033[91m•\033[97m•\033[94m>\033[90m ")
if c in ['1']:
   full()
elif c in ['2']:
   arrow()
elif c in ['3']:
   print "   \033[94m| \033[91mExit\033[97m! \033[94m|\n"
else:
   print "   \033[94m| \033[91mError\033[97m! \033[94m|\n"












############################
##                        ##
## Youtube _ Din-zUgex95  ##
## Github  _ /Din-zUgex95 ##
##                        ##
############################
