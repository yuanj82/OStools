while True:
    start = input("You can enter 'q' to exit, or enter any other character to continue.")
    if start == 'q':
        exit(0)
    gene= input(str("Please input id:"))

    def ID_converter(ID):
        with open("./ID.txt", "r+") as file:
            ID_corresponding_list = file.readlines()

        for ID in ID_corresponding_list:
            if gene in ID:
                print('RAP ID:{}'.format(ID.split('\t')[0]))
                print('MSU ID:{}'.format(ID.split('\t')[1]))
                global OS_ID
                OS_ID = ID.split('\t')[0]
                break
            else:
                continue
        else:
            print("sorry, ID not found!")
            
        print("ID conversion completed!")
        print()

    def extract_id():
        if OS_ID == 'None':
            print("can't")
            return
        else:
            pass
        id_list = []
        Processed_ID = OS_ID.replace('g', 't')
        Processed_ID_0 = Processed_ID + '-00'
        Processed_ID_1 = Processed_ID + '-01'
        id_list.append(Processed_ID_0)
        id_list.append(Processed_ID_1)
        print()
        print("Protein:")
        with open("./os.protein.fasta", "r") as protein:
            seq = protein.readlines()
        
        for protein_id in id_list:
            for i in range(len(seq)):
                if protein_id in seq[i]:
                    print(seq[i], end='')
                    print(seq[i+1])
                    break
        
            else:
                print(">{}:Unable to find protein sequence".format(protein_id))

    protein_switch = input("Do you need its protein sequence? y/N ")

    ID_converter(gene)

    if protein_switch == 'y':
        extract_id()
    if protein_switch == 'n' or 'N' :
        pass

