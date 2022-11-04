def selectionSort(vals):
    n = len(vals)
    for index in range(0, n-1):
        #find smallest in index ~ n -1
        minIdx = index
        for i in range(index, n):
            if vals[i] < vals[minIdx]:
                minIdx = i
            
        vals[index], vals[minIdx] = vals[minIdx], vals[index]