seq = []
for a in range(2, 101):
    for b in range(2, 101):
        seq.append(a**b)
seq = set(seq)
print len(seq)
    
            
            
