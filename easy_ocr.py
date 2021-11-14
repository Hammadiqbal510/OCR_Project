import easyocr
import os

reader = easyocr.Reader(['en'])

images=os.listdir(r'NIC_Images')

def get_data(data:list):
    Name=Father_Name=Gender=Id_Number=D_O_Birth=D_O_Issue=D_O_Expiry='-'
    gaurdian='Father Name'
    #father name
    if list(filter(lambda x: 'Father' in x, data)):
        Father_Name=data[data.index(list(filter(lambda x: 'Father' in x, data))[0])+1]
    elif list(filter(lambda x: 'Husband' in x, data)):
        Father_Name=data[data.index((list(filter(lambda x: 'Husband' in x, data)))[0])+1]
        gaurdian="Husband Name"
        Gender='F'
    #name
    if "Name" in data:
        Name=data[data.index("Name")+1]
    if Name == "-":
        _name=list(filter(lambda x: 'Nam' in x, data))
        if _name and not bool(list(filter(lambda x: 'Father' in x, _name))):
            Name=data[data.index(list(filter(lambda x: 'Nam' in x, data))[0])+1]
        elif Father_Name != "-":
            Name=data[data.index(list(filter(lambda x: 'Father' in x, data))[0])-1]


    #gender
    if "F" in data:
        Gender='F'
    elif "M" in data:
        Gender='M'
    #id_number
    Id_Number=list(filter(lambda x: '-' in x, data))[0]
    #dates
    try:
        D_O_Birth,D_O_Issue,D_O_Expiry=list(filter(lambda x: '.' in x, data))
    except:pass
    #assign data
    data_dic={
        'Name':Name,
        gaurdian:Father_Name,
         'Gender':Gender, 
         'Identity Number':Id_Number, 
         'Date Of Birth':D_O_Birth, 
         'Date Of Issue':D_O_Issue, 
         'Date Of Expiry':D_O_Expiry}
    return data_dic

if not os.path.exists("output"):
    os.mkdir('output')
for i,j in enumerate(images):
    print(f"========== Image {j} Data fetching...  ==========")
    output = reader.readtext(rf'NIC_Images/{j}')
    data=[]
    for a,b,c in output:
        data.append(b)
        # print(b)
    print(get_data(data))
    f=open(f"output/{j.split(sep='.')[0]}.txt",'w')
    f.write("================data from image================\n")
    f.write(str(data))
    f.write("\n================extracted from data================\n")
    for i in get_data(data).items():
        f.write(str(i))
        f.write('\n')
    f.close()
     
