import sys
import re

"""
the functions perform the following:

- takes an input file and an output file
- reads the input file line by line
- if the line is a function, it creates a comment for it
    - the comment is in the form of:
        // @function function_name
        // @param param_name param_type
        ...
        // @returns
        
- if the line is a type, it creates a comment for it
    - the comment is in the form of:
        // @type type_name
        // @field field_name field_type
        ...
        
- writes the comments to the output file

"""

def getParams(line):
    params = []
    m = re.match(r'^((export\s+|method\s+)*\w+)\s*\(([^)]*)\)\s*=>', line)
    if m:
        param_string = m.group(3)
        if param_string:
            params = param_string.split(',')
            params = [p.split('=')[0].strip() if '=' in p else p for p in params]
            params = [p.split(' ')[-1].strip() + '\t' + p.split(' ')[0].strip() for p in params]
    return params

def create_comment(line):
    function_name = line.split('(')[0].strip()
    function_name = function_name.split(' ')[-1].strip()
    params = getParams(line)
    comment = '\n'
    comment += '// @function %s\n' % function_name
    for param in params:
        comment += '// @param \t %s\n' % param
    comment += '// @returns\n'
    return comment

def createComments(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        lines = f.readlines()
    comments = []
    fields  = ''
    depth = 0
    for line in lines:
        if depth == 0:
            if re.match(r'^(export +)?type',line):
                fields += line
                type_name = line.split('type')[1]
                comments.append('\n\n// @type {}'.format(type_name))
                depth += 1
            if re.match(r'^(export\s+|method\s+)*\w+\s*\([^)]*\) *=>', line):
                comment = create_comment(line)
                comments.append(comment)
            if depth == 0:
                comments.append(line)
        else:
            if line.startswith('    '):
                fields += line
                line = line.strip()
                m = re.match(r'(\w+)\s+(\w+)\s*(=\s*\w+)?', line)
                if m:
                    type_name, field_name, default = m.groups()
                    comments.append('// @field {} ({}) \n'.format(field_name, type_name))
            else:
                depth = 0
                comments.append(fields)
                fields = ''
    with open(outputFile, 'w') as f:
        f.writelines(comments)

if __name__ == '__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    if not len(sys.argv) == 3:
        print('Usage: python \\{} inputFile outputFile'.format(sys.argv[0 ]))
        sys.exit(1)
    else:
        createComments(inputFile, outputFile)
