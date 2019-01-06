import numpy as np

# made matrix with any spesification data
a = np.array(([1,2,3],[3,4,5]), dtype = float)

# Made array with function
def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return (kolom+baris)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)

# Made array or matrix with iterable
iterable = (x*x for x in range(5))

d = np.fromiter(iterable, dtype = int)

# multitype array
dtipe = [('nama','S255'), ('tinggi', int)]
data = [
    ('ucup', 150),
    ('otong', 160),
    ('mario', 170)
]

e = np.array(data, dtype = dtipe)

print(e)