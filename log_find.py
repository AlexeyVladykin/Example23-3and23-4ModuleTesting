import sys
import re

ip4=("[0-9]+\\."*4)[:-2]
ip6=("[0-9a-fA-F]+:"*8)[:-1]
ip=f"({ip4}|{ip6})"
nv=0
filters=[]
found=[]
matchCounts={}
inversion=lambda s,i,l: not l[i+1](s,i+1,l)
dsplit=lambda s,i,l: l[i+1](s.split(": ",1)[0],i+1,l)
csplit=lambda s,i,l: l[i+1](s.split(": ",1)[1],i+1,l)
lmatching=lambda s,i,l: l[i+1]in s
matching=lambda s,i,l: l[i+1].search(s)!=None
def vmatching(s,i,l):
	l=l[i+1].findall(s)
	for k in l:
		matchCounts[l[0]]=(matchCounts[l[0]] if l[0]in matchCounts else 0)+1
	return len(l)!=0
def findInFile(file):
	found.clear()
	matchCounts.clear()
	if type(file)==type(""): f=open(file)
	[found.append(l.rstrip(" \t\r\n")) if l!='\n' and all(f[0](l,0,f) for f in filters) and not nv else 0 for l in f]
	if file!=f: f.close()
	return found

if __name__=="__main__":
	if len(sys.argv)<2 or sys.argv[1]=="-h":
		print(f"{sys.argv[0]} <file> [-nv] [-n[d|c]*] [-<d|c>*] [-r <something_r>] [-rv <something_r>] [-[v]ip4] [-[v]ip6] [-[v]ip] [[-a] <something_a>]\n\t-nv отключает показывание строк\n\t-n* то же что -* только отфильтровывает на ненахождение\n\t-d* то же что -* но ищет в примечаниях/тегах строки (до первого `: `)\n\t-с* то же что -* но в содержании строки (после первого `: `)\n\t-a (по умолчанию) фильтрует строки на содержание `something_a`\n\t-r фильтрует на нахождение re (python regex) `something_r`\n\t-rv это как -r но еще показывает все находимое с числом нахождений\n\t-vip* это как -ip* но еще показывает все находимое с числом нахождений\n\t-ip4 это сокращенное `-r {ip4}`\n\t-ip6 это сокращенное `-r {ip6}`\n\t-ip это сокращенное `-r {ip}`")
		exit()
	if len(sys.argv)<3:
		print(open(sys.argv[1]).read())
		exit()
	i = 2
	while len(sys.argv)>i:
		if sys.argv[i]=="-nv":
			nv=1
		elif sys.argv[i][0]=='-':
			l=[]
			i2=1
			if sys.argv[i][i2]=='n':
				l.append(inversion)
				i2+=1
			if sys.argv[i][i2]=='d':
				l.append(dsplit)
				i2+=1
			elif sys.argv[i][i2]=='c':
				l.append(csplit)
				i2+=1

			if sys.argv[i][i2:]=="ip4":
				l.append(matching)
				l.append(re.compile(ip4,re.DOTALL))
			elif sys.argv[i][i2:]=="vip4":
				l.append(vmatching)
				l.append(re.compile(ip4,re.DOTALL))
			elif sys.argv[i][i2:]=="ip6":
				l.append(matching)
				l.append(re.compile(ip6,re.DOTALL))
			elif sys.argv[i][i2:]=="vip6":
				l.append(vmatching)
				l.append(re.compile(ip6,re.DOTALL))
			elif sys.argv[i][i2:]=="ip":
				l.append(matching)
				l.append(re.compile(ip,re.DOTALL))
			elif sys.argv[i][i2:]=="vip":
				l.append(vmatching)
				l.append(re.compile(ip,re.DOTALL))
			elif len(sys.argv)==i+1:
				print(f"нету аргумента для `{sys.argv[i]}`")
				exit(1)
			else:
				if sys.argv[i][i2:]=='a':
					l.append(lmatching)
				elif sys.argv[i][i2:]=='r':
					l.append(matching)
				elif sys.argv[i][i2:]=="rv":
					l.append(vmatching)
				else: print(f"непонятно `{sys.argv[i][i2:]}`");exit(1)
				i+=1

				if sys.argv[i-1][i2]=='r': l.append(re.compile(sys.argv[i],re.DOTALL))
				else: l.append(sys.argv[i])
			filters.append(l)
		else: filters.append([lmatching, sys.argv[i]])
		i+=1
	[print(l) for l in findInFile(sys.argv[1])]
	print(f"\n{len(found)} непустых строк найдено")
	if len(matchCounts)>0:
		matchCounts = [(v,k) for k,v in matchCounts.items()]
		matchCounts.sort()
		print(f"числа нахождений:")
		for p in matchCounts:
			print(f"\t`{p[1]}`: {p[0]}")