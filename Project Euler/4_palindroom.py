l1 = []
l2 = []

def generate():
    for i in range(800, 999):
        l1.append(i)
    return l1

def main(l1):
    l2 = l1
    for a in range(0, len(l1)):
        
        for b in range(0, len(l2)):
            if str(l1[a]*l2[b]) == str(l1[a]*l2[b])[::-1]:
                print "found: " + str(l1[a]*l2[b])

if __name__ == '__main__':
    main(generate())
            
            
                
    
    
