import re
speakers = ['sheldon','leonard','penny','howard','raj']
common_name = "dat/BBT1"
# fout = open("bbt1.all",'w')
# for i in range(1,18):
# 	if i < 10 :
# 		name = common_name + '.0' + i.__str__()
# 	else:
# 		name = common_name + '.'+ i.__str__()
# 	out_name = common_name +i.__str__()+ ".clean"
# 	f = open(name,'r')
# 	fout = open(out_name,'w')
	# for line in f:
	# 	line = line.lower().strip()
	# 	if ':' not in line:
	# 		continue
# 		else:
# 		
# 			line = re.sub(r'\(.*\)','',line)
# 			sp = line.split(':')
# 			if len(sp) < 2:
# 				continue
# 			speaker = sp[0].strip()
# 			if speaker not in speakers:
# 				continue
# 			fout.write(line+"\n")
# 		
def get_stopwords():
	f=open("stopwords_short.txt","r")
	stopwords=[]
	for line in f:
		if line == "":
			continue
		line = line.strip()
		stopwords.append(line)
	return stopwords
f = open("bbt1.all",'r')
fout = open("for_pos_no_stopwords_short.txt",'w')
stop = get_stopwords()
for line in f:
	line = line.lower().strip()
	if ':' not in line:
		continue
	sp = line.split(":")
	sp[1] = sp[1].strip()
	speech = re.findall(r'\w+', sp[1],flags = re.UNICODE | re.LOCALE) 
	to_print = ""
	for word in speech:
		if word in stop:
			continue
		to_print = to_print + word + " "
	if to_print == "":
		continue
	fout.write(to_print+"\n")
		
		