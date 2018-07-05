#
# Process the Canon
#
import nltk
import sys, re
from bs4 import BeautifulSoup

f = open('abbrev.tab')

abrv = {}

for l in f:
    (a,t) = l.strip().split('\t')
    abrv[a] = t


texts = ''
prev = ''
for a in abrv:
    print ("Processing {}".format(a), file=sys.stderr)
    f =  open('src/{}.html'.format(a), 
              encoding='utf-8', errors='ignore')
    for l in f:
        if prev.strip().endswith('</div></div></div>'):
            t = BeautifulSoup(l.strip(), 'lxml').text
            p = re.compile('first published in (.*?)\. ')
            m = p.search(t)
            if m:
                pub = m.group(1)
                for pu in pub.split(' and in '):
                    print (a, "PUBLISHED", pu, sep='\t')
            p = re.compile('This is the (\d+)')
            m = p.search(t)
            if m:
                print (a, "ORDER", m.group(1), sep='\t')
            p = re.compile('ollected in (.*?)\.')
            m = p.search(t)
            if m:
                print (a, "COLLECTION", m.group(1), sep='\t')
                
        prev = l
