
values = ['a','b']

def get_sequences(temp_sequence = None, current_depth = 0, max_depth = len(values)):
    
    if temp_sequence == None:
        temp_sequence = list()
        
    for val in values:
        
        new_sequence = temp_sequence.copy()
        new_sequence.append(val)
        
        if current_depth != max_depth-1:
            get_sequences(new_sequence, current_depth+1)
            
        else:
            
            print(new_sequence)

get_sequences()