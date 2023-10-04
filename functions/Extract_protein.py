import os

def Extract_protein():
    current_path = os.path.abspath(__file__)
    root_path = os.path.dirname(current_path)
    PROTEINfile = os.path.join(root_path, '../data', 'os.protein.fasta')

    gene= input(str("Please input id:"))
    if gene == 'None':
        print("can't")
        return
    else:
        pass
    id_list = []
    Processed_ID = gene.replace('g', 't')
    Processed_ID_0 = Processed_ID + '-00'
    Processed_ID_1 = Processed_ID + '-01'
    id_list.append(Processed_ID_0)
    id_list.append(Processed_ID_1)
    print()
    print("Protein:")
    with open(PROTEINfile, "r") as protein:
        seq = protein.readlines()
    
    for protein_id in id_list:
        for i in range(len(seq)):
            if protein_id in seq[i]:
                print(seq[i], end='')
                print(seq[i+1])
                break
    
        else:
            print(">{}:Unable to find protein sequence".format(protein_id))