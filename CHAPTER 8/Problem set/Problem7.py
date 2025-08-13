def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n        
        
        
l = ["Prince","Ace","Nigga","ce","Freelance","cent"]

print(rem(l, "ce"))
