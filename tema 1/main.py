import numpy as np  # Importă modulul numpy cu aliasul np
import time  # Importă modulul time
# Această funcție primește un vector H și un indice i și realizează procesul de heapify (rearanjare într-un heap) a subarborelui cu rădăcina în nodul i.
def heapify(heap, i):
    if 2*i >= len(heap)-1:
        return
         #Verifică dacă nodul i are copii (nodurile 2i și 2i+1). Dacă nu are copii, se returnează.
    if heap[i] < heap[2*i] and heap[2*i] > heap[2*i + 1]:  # Verifică dacă nodul i este mai mic decât copilul său stâng și copilul său stâng este mai mare decât copilul său drept
        temp = heap[i]
        heap[i] = heap[2*i]
        heap[2*i] = temp
        heapify(heap, 2*i)
    elif heap[i] < heap[2*i + 1]:  # Verifică dacă nodul i este mai mic decât copilul său drept
        temp = heap[i]
        heap[i] = heap[2*i + 1]
        heap[2*i + 1] = temp
        heapify(heap, 2 * i + 1)

def heap_sort(arr):
    n = len(arr) - 1
    for i in range(int(np.ceil(n/2)), 0, -1):  # Parcurge vectorul de la jumătate către început
        heapify(arr, i)
    result = []
    for i in range(1, n):  # Parcurge vectorul de la 1 până la n-1
        result.append(arr[1])  # Adaugă în rezultat valoarea de pe poziția 1 (rădăcina heap-ului)
        arr[1] = 0  # Setează elementul de pe poziția 1 la 0 (elimină elementul din heap)
        heapify(arr, 1)  # Rearanjează heap-ul
    return result

def get_and_remove_max(arr):
    max_idx = 1
    for i in range(1, len(arr)):  # Parcurge vectorul de la 1 până la final
        if arr[i] > arr[max_idx]:  # Verifică dacă elementul curent este mai mare decât maximul curent
            max_idx = i
    max_val = arr[max_idx]  # Salvează valoarea maximă
    arr[max_idx] = 0  # Setează elementul maxim la 0 (elimină elementul din vector)
    return max_val

def selection_sort(arr):
    result = []
    for i in range(1, len(arr)):  # Parcurge vectorul de la 1 până la final
        result.append(get_and_remove_max(arr))  # Adaugă în rezultat valoarea maximă din vector
    return result

arr = [0] + np.random.permutation(10000)  # Inițializează vectorul cu o permutare aleatorie a numerelor de la 1 la 10000, adăugând 0 la început
arr1 = arr.copy()  # Copiază vectorul arr în vectorul arr1

t0 = time.time()  # Stochează timpul curent în secunde
sorted_arr_heap = heap_sort(arr)  # Sortează vectorul arr folosind Heap Sort și stochează rezultatul în sorted_arr_heap
t1 = time.time()  # Stochează timpul curent în secunde
sorted_arr_selection = selection_sort(arr1)  # Sortează vectorul arr1 folosind Selection Sort și stochează rezultatul în sorted_arr_selection
t2 = time.time()  # Stochează timpul curent în secunde

print("Heap Sort time:", t1 - t0)  # Afișează timpul de execuție algoritmului Heap Sort
print("Selection Sort time:", t2 - t1)  # Afișează timpul de execuție algoritmului Selection Sort
