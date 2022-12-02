import pandas as pd

df = pd.read_csv('~/Desktop/Author List_November 15, 2022_13.47.csv')
df.columns = ['First Name', 'Last Name', 'email', 'Name to appear in Journal', 'ORCID']

#filename = 'authors_phys1140.txt'
filename = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/authors_phys1140.tex'
open(filename, 'w').close()

for i in range(len(df.index)): 
    name = df.iloc[i]['Name to appear in Journal']
    orcid = df.iloc[i]['ORCID']

    with open(filename, 'a') as text_file:
        if str(orcid) == 'nan': 
            print('\\author{{{}}}\n\\affiliation{{\\cu}}\n'.format(name), file=text_file)
        else: 
            print('\\author[{}]{{{}}}\n\\affiliation{{\\cu}}\n'.format(orcid, name), file=text_file)


# Format should end up looking like: 
# \author[0000-0002-3783-5509]{James Paul Mason}
# \affiliation{\jhuapl}

