from tape import datasets

dataset = datasets.SecondaryStructureDataset(
    data_path='./data',
    split='train'
)

print("Dataset downloaded!")
