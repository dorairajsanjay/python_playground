#!/usr/bin/env python
# coding: utf-8

# In[104]:


import numpy as np

input_list =  ['oppo','oppo','blank','blank','blank','oppo','oppo','blank', 'blank',          'blank', 'obj', 'blank', 'obj', 'obj', 'blank','blank', 'blank', 'obj', 'blank', 'obj']
expected_list = ['oppo', 'oppo', '', '', '', 'oppo', 'oppo', '', '', '', 'obj', 'obj', 'obj', 'obj', '', '', '', 'obj', 'obj', 'obj']

# convert to numpy arrays and extract sub lists
npList1 = np.asarray(input_list)
l1,l2,l3 = npList1[:-2],npList1[1:-1],npList1[2:]
l2_copy = np.copy(l2)

# debug print
print("%12s %12s %12s %12s %12s %12s" % ("Iteration","l1==l3","l1[index]","l2[index]","l3[index]","l2_copy[index]"))
print("-"*80)

for i,val in np.ndenumerate(l1==l3):
    index = i[0]
    if val == True and l2[index] == 'blank' and l1[index] != 'blank':
        l2_copy[index] = l1[index]
    elif l2[index] == 'blank':
        l2_copy[index] = ""
        
    # debug
    print("%12s %12s %12s %12s %12s %12s" % (index,val,l1[index],l2[index],l3[index],l2_copy[index]))
    
generated_list = np.append( np.append(l1[0],l2_copy) ,l3[-1])

# display list with expected
print("\n\n%16s %16s %16s" % ("Input List", "Expected List", "Output List"))
print("-"*80)
for x,y,z in zip(input_list,expected_list, generated_list):
    print("%16s %16s %16s" % (x,y,z))


# In[ ]:




