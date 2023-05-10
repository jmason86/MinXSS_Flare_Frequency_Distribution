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


def save_to_arxiv_format(df, filename):
    with open('all_names.txt', 'w') as file:
        file.write(','.join(df['Name'].values))


def save_to_mendeley_format(df, filename):
    open(filename, 'w').close()

    for name in df['Name']: 
        *first, last = name.split()
        
        with open(filename, 'a') as text_file:
            print('{}, {}'.format(last, ' '.join(first)), file=text_file)


# Students
df1 = pd.read_csv('./Student-authors.csv')
df1.columns = ['Name', 'ORCID']
filename = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/authors_students_phys1140.tex'
#save_to_tex_format(df1, filename)

# TAs
df2 = pd.read_csv('./TA_authors.csv')
df2.columns = ['Email', 'Name', 'ORCID']
filename = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/authors_tas_phys1140.tex'
#save_to_tex_format(df2, filename)

# Leads
names = ['James Paul Mason', 'Alexandra Werth', 'Colin G. West', 'Allison A. Youngblood', 'Donald L. Woodraska', 'Courtney Peck']
final_name = ['H. J. Lewandowski']

# Output all together
all_names_df = pd.concat([pd.Series(names), df1['Name'], df2['Name'], pd.Series(final_name)], axis=0).reset_index(drop=True)
all_names_df = pd.DataFrame({'Name': all_names_df})
filename_arxiv = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/author_names_for_arxiv.txt'
#save_to_arxiv_format(all_names_df, filename_arxiv)
filename_mendeley = '/Users/masonjp2/Dropbox/Apps/Overleaf/Flare Frequency Distribution (FFD)/author_names_for_mendeley.txt'
save_to_mendeley_format(all_names_df, filename_mendeley)


# Format should end up looking like: 
# \author[0000-0002-3783-5509]{James Paul Mason}
# \affiliation{\jhuapl}

