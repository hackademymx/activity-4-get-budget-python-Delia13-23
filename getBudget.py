def getTotalBudget(people):
    
    suma = []
    for i in people:
        suma = suma + [j for k,j in i.items() if k == 'budget']
    
    return (sum(suma))

    
