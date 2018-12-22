# this program produces a list of stories and links to the guide.
from collections import defaultdict as dd

# dorn['SPEC']['date'] = (1, 125)
dorn = dd(lambda: dd(tuple))

fh = open('DORN.tsv')
for l in fh:
    (story, data, tup) = l.strip().split('\t')
    tpl = [int(x) for x in tup.split(",")]
    dorn[story][data] = tpl

#print (dorn)
    
url = {1:"http://www.beaconsociety.com/uploads/3/7/3/8/37380505/a_study_guide_to_sherlock_holmes_--_volume_1.pdf",
       2:"http://www.beaconsociety.com/uploads/3/7/3/8/37380505/a_study_guide_to_sherlock_holmes_--_volume_2.pdf" }

#offset ={1:12, 2:12}

###
### Print out
###

print("""
<html>
<body>""")

for story in dorn:
    print('<h3>{}</h3>'.format(story))
    for data in dorn[story]:
        print ('<p><a href="{3}#page={4}">{0}</a>  on p{1}, vol{2}'.format(data,
                                                                           dorn[story][data][1],
                                                                           dorn[story][data][0],
                                                                           url[dorn[story][data][0]],
                                                                           dorn[story][data][1] +12))

print("""
</body>
</html>""")
