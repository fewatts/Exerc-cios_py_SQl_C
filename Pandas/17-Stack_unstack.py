import pandas as pd

df = pd.read_csv('https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv')

df.head(4)

#       Name	        Team	Number	Position	Age	Height	Weight	College	Salary
#0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
#1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
#2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
#3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0

stack_df = df.stack()

#0    Name         Avery Bradley
#     Team        Boston Celtics
#     Number                 0.0
#     Position                PG
#     Age                   25.0
#                      ...      
#456  Age                   26.0
#     Height                 7-0
#     Weight               231.0
#     College             Kansas
#     Salary            947276.0
#Length: 4018, dtype: object

udf = stack_df.unstack()

#Name	Team	Number	Position	Age	Height	Weight	College	Salary
#0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
#1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
#2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
#3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
#4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0

