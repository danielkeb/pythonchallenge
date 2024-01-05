student_dict={
    "student":["Daniel","John","meracle"],
    "score":[56, 76,98]

}

import pandas as pd

data=pd.DataFrame(student_dict)
#print(data.student)

for(key,value) in data.iterrows():
    if value.student =="Daniel":
        print(value.score)