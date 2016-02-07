from numpy import arange
n0 = 2

def prim(n):

    prim_array = [n0]

    if n == 2:
        return prim_array
    else:
        for i in arange(3, n+1):
            write = True
            for j in prim_array:
                rest = i % j
                if rest == 0:
                    write = False
                    break
                elif rest != 0:
                    write = True

            if write:
                prim_array.append(i)

    return prim_array