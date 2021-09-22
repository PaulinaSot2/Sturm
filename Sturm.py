# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:37:49 2021

@author: Paulina Soto,Paulina García
"""

#STURM
def rootsint(fun, int1, int2):
    poly=[]
    poly.append(fun)
    #derivada de la función
    derivada=[]
    for i in range(len(fun)-1):
        aux_3=-(i-len(fun)+1)*fun[i]
        derivada.append(aux_3)
    n=len(derivada)
    poly.append(derivada)
    while n > 1 :
        n_1=len(poly)
        a=poly[n_1-2]
        b=poly[n_1-1]
        #división de polinomios
        f = list(a)
        m = b[0]
        for i in range(len(a)-(len(b)-1)):
            f[i] = f[i]/m
            co = f[i]
            if co != 0: 
                for j in range(1, len(b)):
                    f[i + j] += -b[j] * co
        b = -(len(b)-1)
        x=f[b:]
        while x[0]==0:
            x.pop(0)
        c=x
        for i in range(len(c)):
            c[i]=c[i]*-1
        poly.append(c)
        n=len(c)
    poly1=[]
    poly2=[]
    for i in range(len(poly)):
        aux=0
        r=len(poly[i])
        for l in range(r):
            aux=aux*int1+poly[i][l]
        poly1.append(aux)
        aux=0
        for k in range(r):
            aux=aux*int2+poly[i][k]
        poly2.append(aux)
    print(poly1)
    print(poly2)
    #cambio de signo
    change1=0
    for i in range(len(poly1)-1):
        if poly1[i]>0:
            if poly1[i+1]>0:
                change1+=0
            else:
                change1+=1
        else:
            if poly1[i+1]<0:
                change1+=0
            else:
                change1+=1
    change2=0
    for i in range(len(poly2)-1):
        if poly2[i]>0:
            if poly2[i+1]>0:
                change2+=0
            else:
                change2+=1
        else:
            if poly2[i+1]<0:
                change2+=0
            else:
                change2+=1
    
    print("Encontramos",change1-change2, "raíces en","(",int1,",", int2,")")
rootsint([1,3,2,-5,-3],-3, 2)
