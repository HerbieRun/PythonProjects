def is_leaf(root):
    return type(root) == str

def is_binary_node(root):
    return type(root) == list and len(root) == 2

def is_prefix_tree(root,count=0):
    if count == 0 and is_binary_node(root) == False:
        return False
    
    elif is_leaf(root) == True: 
        return True
    
    elif len(root)==2:
        return is_prefix_tree(root[0],count+1) and is_prefix_tree(root[1],count+1)
    
    else:
        return False

def decode(root, code_str):
    result = ''
    while len(code_str)>0:
        result = result + decode_char(root,code_str)[0]
        code_str = decode_char(root,code_str)[1]
    return result

# helper function    
def decode_char(root,code_str):
    if is_leaf(root):
        return (root,code_str)
    if code_str[0] == '0':
        return decode_char(root[0],code_str[1:])
    else:
        return decode_char(root[1],code_str[1:])

def build_code_table(root):
    code_table = {}
    partial_codeword = ''
    if is_leaf(root):
        result['root'] = find_codewords(root,code_table,partial_codeword)[2]
    else:
        return find_codewords(root,code_table,partial_codeword)

def find_codewords(root,code_table,partial_codeword):
    if is_leaf(root):
    else:
        root[0] = 
    
    
