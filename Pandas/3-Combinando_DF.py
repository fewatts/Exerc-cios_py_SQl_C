import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index = [4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index = [8, 9, 10, 11])
#df1 = 	
#A	B	C	D
#0	A0	B0	C0	D0
#1	A1	B1	C1	D1
#2	A2	B2	C2	D2
#3	A3	B3	C3	D3

#df2 = 
#A	B	C	D
#4	A4	B4	C4	D4
#5	A5	B5	C5	D5
#6	A6	B6	C6	D6
#7	A7	B7	C7	D7

#df3 = 
#A	B	C	D
#4	A4	B4	C4	D4
#5	A5	B5	C5	D5
#6	A6	B6	C6	D6
#7	A7	B7	C7	D7

frames = [df1, df2, df3] #forma uma lista

FramesCombinados = pd.concat(frames) #ou framescombinados = pd.concat([df1, df2, df3])

#Frames combinados = 
#A	B	C	D
#0	A0	B0	C0	D0
#1	A1	B1	C1	D1
#2	A2	B2	C2	D2
#3	A3	B3	C3	D3
#4	A4	B4	C4	D4
#5	A5	B5	C5	D5
#6	A6	B6	C6	D6
#7	A7	B7	C7	D7
#8	A8	B8	C8	D8
#9	A9	B9	C9	D9
#10	A10	B10	C10	D10
#11	A11	B11	C11	D11

grupo = pd.concat([df1, df2, df3], keys=['f1', 'f2', 'f3'])

#grupo = 
#		A	B	C	D
#f1	0	A0	B0	C0	D0
#   1	A1	B1	C1	D1
#   2	A2	B2	C2	D2
#   3	A3	B3	C3	D3
#f2	4	A4	B4	C4	D4
#   5	A5	B5	C5	D5
#   6	A6	B6	C6	D6
#   7	A7	B7	C7	D7
#f3	8	A8	B8	C8	D8
#   9	A9	B9	C9	D9
#   10	A10	B10	C10	D10
#   11	A11	B11	C11	D11

grupo['A']

#Out:
#f1  
#    0      A0
#    1      A1
#    2      A2
#    3      A3
#f2  4      A4
#    5      A5
#    6      A6
#    7      A7
#f3  8      A8
#    9      A9
#    10    A10
#    11    A11
#Name: A, dtype: object

grupo.loc['f1']

#out:
#	A	B	C	D
#0	A0	B0	C0	D0
#1	A1	B1	C1	D1
#2	A2	B2	C2	D2
#3	A3	B3	C3	D3

#Outra maneira de concatenação

g2 = df1.append(df2)

#out:
#	A	B	C	D
#0	A0	B0	C0	D0
#1	A1	B1	C1	D1
#2	A2	B2	C2	D2
#3	A3	B3	C3	D3
#4	A4	B4	C4	D4
#5	A5	B5	C5	D5
#6	A6	B6	C6	D6
#7	A7	B7	C7	D7

g3 = g2.append(df3)

#out:
#	A	B	C	D
#0	A0	B0	C0	D0
#1	A1	B1	C1	D1
#2	A2	B2	C2	D2
#3	A3	B3	C3	D3
#4	A4	B4	C4	D4
#5	A5	B5	C5	D5
#6	A6	B6	C6	D6
#7	A7	B7	C7	D7
#8	A8	B8	C8	D8
#9	A9	B9	C9	D9
#10	A10	B10	C10	D10
#11	A11	B11	C11	D11

