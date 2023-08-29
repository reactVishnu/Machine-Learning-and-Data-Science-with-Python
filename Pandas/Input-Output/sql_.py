import pandas as pd
from sqlalchemy import create_engine

import numpy as np

conn = create_engine('sqlite:///:memory')

# df = pd.DataFrame(np.array(np.random.randint(0,16,(4,4))),columns=['a','b','c','d'])
# df.to_sql(name='test', con=conn, if_exists="replace",index=False)
# print(new_df)
new_df = pd.read_sql(con=conn, sql='test')
print(new_df)

print(pd.read_sql_query(sql='SELECT a,b,c FROM test', con=conn))
# pd.DataFrame.to_sql()