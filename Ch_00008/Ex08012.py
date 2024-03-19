t = ['a', 'b', 'c', 'd', 'e', 'f']
l = len(t) # 6
l1 = l - 1
def delete_end(t):
    del t[l1]
delete_end(t)
def delete_head(t):
    del t[0]
delete_head(t)
#print(l1)
print(t)
