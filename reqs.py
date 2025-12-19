import os
os.system('python -m pipreqsnb article.ipynb > requirements_tmp.txt')
with open('requirements_tmp.txt', 'r') as infile :
    small_reqs = infile.readlines()
    small_reqs = [r.strip().split('==') for r in small_reqs]
    small_reqs = {req[0]:req[1] for req in small_reqs if len(req)==2}

with open('reqs_orig.txt', 'r') as infile :
    big_reqs = [l.strip() for l in infile.readlines()]
    big_reqs = [r.strip().split('==') for r in big_reqs]
    big_reqs = {req[0]:req[1] for req in big_reqs if len(req)==2}

small_reqs.update({k:v for k,v in big_reqs.items() if k in small_reqs})
print('\n'.join([k + "==" + v for k,v in small_reqs.items()]))