import threading
import sys

output=[] #Salida. Lista de números primos
max_threads = 4 #número de Threads máximos que se epueden crear

#Función para comprobar si un número es primo
def es_primo(x):
	n=2
	while n<=x/2:
		if x%n==0:
			return False
		n+=1
	return True

#Todos los números primos en un rango
def primos_en_rango_thread(x,y):
	while x<=y:
		if es_primo(x):
			output.append(x) #añadimos el primo a la lista output
		x+=1
	
#Todos los números primos en un rango
def primos_en_rango(x,y):
	#Calculo del tamaño de cada intervalo
	diff = y-x
	num_threads = max_threads if max_threads <= diff else diff+1
	t_intervalo=max(0,int((((y-x)+1)/num_threads))-1)
	threads = [] #lista con los threads
	r_final = x-1 #necesario para ajustar los rangos
	for n in range(num_threads):
		r_inicio = r_final+1 #inicio del rango
		r_final = r_inicio+t_intervalo #final del rango
		if ((y-r_inicio)+1)/(num_threads-n) >= 1 and ((y-r_inicio)+1)%(num_threads-n) != 0:
			r_final += 1 #si la división no es exacta sumamos 1 para ajustar
		r_final = min(r_final,y)
		print("> Thread {:>2}: {:>5} - {:>5}".format(n+1,r_inicio,r_final))
		thread = threading.Thread(target=primos_en_rango_thread, args=(r_inicio,r_final))
		threads.append(thread)
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	return output
	
def main():
	args = sys.argv
	try:
		r_inicio = max(int(args[1]),2)
		r_final = int(args[2])
		if r_inicio <= r_final:
			r_inicio = max(int(args[1]),2)
			r_final = int(args[2])
			lista_primos = primos_en_rango(r_inicio,r_final)
			print(lista_primos)
			return lista_primos
		else:
			print("Error con los números introducidos")
	except:
		print("Debes pasar como argumentos dos números")
		
if __name__ == "__main__":
	main()

