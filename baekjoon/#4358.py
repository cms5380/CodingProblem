import sys
input = sys.stdin.readline

treeDict = {}
n = 0
while True:
    tree = input().strip()
    if tree == '':
        break
    if tree not in treeDict:
        treeDict[tree] = 1
        
    else:
        treeDict[tree] += 1
    n += 1

treeList = list(treeDict.keys())
treeList.sort()
for tree in treeList:
    print(tree+' {:.4f}'.format(treeDict[tree]*100/n))