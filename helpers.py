def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def findSubString(s, sub): 
    import re
    return [m.start() for m in re.finditer(sub, s)]

def extract_sig(codes):
    result = {}
    occ = findSubString(codes, '->')
    start = 0
    
    for i,end in enumerate(occ):
        
        # get the start / end of the code
        code = codes[start:end+5]
        sig = code[-3:]
        rel = code.split(':')[0]
        start = end+5
        result[rel] = sig

    # return the result
    return result

def extract_codes(codes):
    result = {}
    if type(codes) == float: return result
    occ = findOccurrences(codes, ')')
    for i,start in enumerate(occ):
        
        # get the end of the code
        end = len(codes)
        if i+1 < len(occ): end = occ[i+1]
        if codes[end-1].isdigit(): end = end - 2
        if codes[end-2] == ' ': end = end - 2

        # get the code and save it
        index = codes[start-1:start]
        code = codes[start+2:end]
        if '\n' in code: code = code.split('\n')[0]
        if len(code) > 1:
            result[index.lower()] = code.lower().strip()

    # return the result
    return result