import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
epic1 = pd.read_csv(name+'_indegreecentrality.csv', delimiter=',')
epic2 = pd.read_csv(name+'_outdegreecentrality.csv', delimiter=',')
epic3 = pd.read_csv(name+'_eigenvectorcentrality.csv', delimiter=',')
epic4 = pd.read_csv(name+'_clusteringCentrality.csv', delimiter=',')
epic5 = pd.read_csv(name+'_enhancedInDegreeCentrality.csv', delimiter=',')
plt.figure(figsize=(15, 5), dpi=80)
val1 = epic1['col2']
n1,x1,_1 = plt.hist(val1,bins=np.linspace(0.001, max(val1), 100), visible=False)
plt.plot(n1)
val2 = epic2['col2']
n2,x2,_2 = plt.hist(val2,bins=np.linspace(0.001, max(val2), 100), visible=False)
plt.plot(n2)
val3 = epic3['col2']
n3,x3,_3 = plt.hist(val3,bins=np.linspace(0.002, max(val3), 100), visible=False)
plt.plot(n3)
val3 = epic3['col2']
n3,x3,_3 = plt.hist(val3,bins=np.linspace(0.002, max(val3), 100), visible=False)
plt.plot(n3)
val3 = epic4['col1']
n4,x4,_4 = plt.hist(val4,bins=np.linspace(0.002, max(val4), 100), visible=False)
plt.plot(n4)
val5 = epic5['col2']
n5,x5,_5 = plt.hist(val5,bins=np.linspace(0.002, max(val5), 100), visible=False)
plt.plot(n5)

plt.xlabel('Bin Number')
plt.ylabel('Frequency')
plt.title('Epinion Centrality')
plt.legend(['Indegree', 'Outdegree', 'Eigenvector', 'Clustering', 'Enhanced indegree'])
plt.grid()
plt.show()