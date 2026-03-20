import random
win="победа"
draw="ничья"
lose="поражение"
names=["камен", "ножицы", "бумга"]
results=[[0 if i-n==0 else [-1,1][(i-n+(i<n))%2] for i in range(len(names))] for n in range(len(names))]
map={"камень":0,"ножницы":1,"бумага":2}
for i in range(len(names)): map[str(i)]=i
for i in range(len(names)): map[names[i]]=i
def turn():
	while 1:
		try:
			print(f"варианты:\n\t-: выход\n{'\n'.join([f"\t{i}: {names[i]}" for i in range(len(names))])}")
			inp=input("что используешь? ").lower()
			if inp in ["-","выход","exit","ничего","- выход","-: выход"]: break
			p=map[inp]
			b=random.randint(0,len(names)-1)
			print(f"\nиспользовано \"{names[p]}\"\nвраг использовал \"{names[b]}\"")
			print([lose,draw,win][results[p][b]+1]+"\n")
		except KeyboardInterrupt:break
		except:
			print(f"что за \"{inp}\"?\n\n")
if __name__=="__main__": turn()