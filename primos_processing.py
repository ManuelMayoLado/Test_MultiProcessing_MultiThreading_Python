import multiprocessing

#Función para comprobar si un número es primo
def es_primo(x):
	n=2
	while n<=x/2:
		if x%n==0:
			return False
		n+=1
	return True
	
#Todos los números primos en un rango
def primosEnRangoProc(x,y,q):
	lprimos = []
	ini=int(x)
	while x<=y:
		if es_primo(x):
			lprimos.append(x)
		x+=1
	q.put([ini])
	print("Process:",ini," - ",y," end")
	
#Todos los números primos en un rango
def primosEnRango(x,y,q):
	n_cpu = multiprocessing.cpu_count()
	r=int((y-x)/n_cpu)
	processes  = []
	for n in range(x,y,r):
		sig = min(n+r-1,y)
		process = multiprocessing.Process(target=primosEnRangoProc, args=(n,sig,q))
		processes.append(process)
	for p in processes:
		print("Process:",p)
		p.start()
	for p in processes:
		p.join()
	saida=[]
	print(q)
	while not q.empty():
		saida+=q.get()
	saida.sort()
	print(saida)
	return saida
	
def main():
	q=multiprocessing.Queue()
	primosEnRango(100000,110020,q)
		
if __name__ == "__main__":
	main()