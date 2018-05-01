def Score(Matrix, weight):
    res = (100-85)/len(weight)
    for i in range(len(weight)):
        res += weight[i] * Matrix[i] * 0.85
    return res

'''          A   B   C   D   E   F    '''
Matrix = [[  0,  0,  0,  0,  0,1/5],
          [  1,  0,1/3,1/3,1/4,1/5],
          [  0,1/3,  0,1/3,1/4,1/5],
          [  0,1/3,1/3,  0,1/4,1/5],
          [  0,1/3,1/3,1/3,  0,1/5],
          [  0,  0,  0,  0,1/4,  0]
          ]
          
Page = []
for i in range(len(Matrix)):
    Page.append(100/len(Matrix))

itera = 0
while (itera < 20):
    print(itera)
    itera+=1
    new_page = []
    for i in range(len(Matrix)):
        tem = Score(Matrix[i],Page)
        new_page.append(tem)
    Page = new_page
    print(Page)
print(Page)
