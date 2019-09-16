import sys

new_titles = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    ref = title = author = year = ''
     
    for i in range(len(lines)):
        line = lines[i] 
        if line.strip().startswith('@'):
            ref = line.strip()
        elif line.strip().startswith('title'):    
            title = line.strip()
        elif line.strip().startswith('author'):   
            author = line.strip()
        elif line.strip().startswith(('year', 'date')):   
            year = line.strip()           
            

        if ref and title and author and year:
            refindex = ref.index('{') 
            refstart = ref[:refindex + 1]
           
            a = author.split('{')[1].split(',')[0].lower()
            y = year.split('{')[1].split('}')[0][:4]
            t = title[title.index('=')+1:].replace('{', '').replace('}', '').lower()
            t = t.replace(' ', '-')
            t = t.replace(':', '')
            t = t.replace('.', '')

            nt = refstart + a + "-" + y + "-" + t
            nt = nt.replace('--', '-')
            new_titles.append(nt)
            
            ref = title = author = year = ''
        

    j = 0
    for i in range(len(lines)):
        line = lines[i]
        if line.strip().startswith('@'):
            print(new_titles[j].strip())
            j = j + 1
        else:
            print(line.strip())
             
