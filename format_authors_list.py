import pandas as pd


def sort_by_last_name(names, orcids):
    l2 = []

    # create 2d list of names
    for ele in names:
        l2.append(ele.split())
    
    names_sorted = []
    sorted_indices = sorted(range(len(l2)), key=lambda k: l2[k][-1])
    orcids_sorted = [orcids[i] for i in sorted_indices]

    # sort by last name
    for ele in sorted(l2, key=lambda x: x[-1]):
        names_sorted.append(' '.join(ele).title())
    
    #for i, ele in enumerate(sorted(l2, key=lambda x: x[-1]):
    #    names_sorted.append(' '.join(ele))

    return names_sorted, orcids_sorted

def save_to_tex_format(df, filename): 
    names_sorted, orcids_sorted = sort_by_last_name(df['Name'], df['ORCID'])
    open(filename, 'w').close()

    for i in range(len(df.index)): 
        name = names_sorted[i]
        orcid = orcids_sorted[i]

        with open(filename, 'a') as text_file:
            if str(orcid) == 'nan' or str(orcid) == ' ': 
                print('\\author{{{}}}\n\\affiliation{{\\cu}}\n'.format(name), file=text_file)
            else: 
                print('\\author[{}]{{{}}}\n\\affiliation{{\\cu}}\n'.format(orcid, name), file=text_file)



# Students
df = pd.read_csv('~/Desktop/Student-authors.csv')
df.columns = ['Name', 'ORCID']
filename = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/authors_students_phys1140.tex'
save_to_tex_format(df, filename)


# TAs
df = pd.read_csv('~/Desktop/TA_authors.csv')
df.columns = ['Email', 'Name', 'ORCID']
filename = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/authors_tas_phys1140.tex'
save_to_tex_format(df, filename)



# Format should end up looking like: 
# \author[0000-0002-3783-5509]{James Paul Mason}
# \affiliation{\jhuapl}

