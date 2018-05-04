def Score(Matrix, weight):
    res = (100-85)/len(weight)
    for i in range(len(weight)):
        res += weight[i] * Matrix[i] * 0.85
    return res

'''          A   B   C   D   E   F    '''
'''Matrix = [[  0,  0,  0,  0,  0,  0],
          [  1,  0,1/3,1/3,1/4,  0],
          [  0,1/3,  0,1/3,1/4,  0],
          [  0,1/3,1/3,  0,1/4,  0],
          [  0,1/3,1/3,1/3,  0,  0],
          [  0,  0,  0,  0,1/4,  0]
          ]'''
f = open('graph.txt')
Matrix_ori = f.readline().split(',')
Matrix = []
a = [0,0,0,0,0,0]
for i in range(len(Matrix_ori)):

    a[i%6] = float(Matrix_ori[i])
    if i%6 == 5:
        Matrix.append(a)
        a = [0,0,0,0,0,0]
    

Page = []
for i in range(len(Matrix)):
    Page.append(100/len(Matrix))

itera = 0
while (True):

    itera+=1
    new_page = []
    for i in range(len(Matrix)):
        tem = Score(Matrix[i],Page)
        new_page.append(tem)
    if Page == new_page:
        break;
    Page = new_page

print("Page Score is:",Page)
print("Iteration time:",itera)
