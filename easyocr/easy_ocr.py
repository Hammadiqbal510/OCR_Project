import easyocr
import os
import re

reader = easyocr.Reader(['en'])

images=os.listdir(r'../NIC_Images')

def get_data(data:list):
    Name=Father_Name=Gender=Id_Number=D_O_Birth=D_O_Issue=D_O_Expiry='-'
    #name
    if "Name" in data:
        Name=data[data.index("Name")+1]
    elif "Father's name" in data:
        Name=data[data.index("Father's name")-1]
    #father name
    if "Father's name" in data:
        Father_Name=data[data.index("Father's name")+1]
    elif "Gender" in data:
        Father_Name=data[data.index("Gender")-1]
    else:
        Father_Name=(filter(lambda x: 'Father' in x, data))[0]

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
        'Father Name':Father_Name,
         'Gender':Gender, 
         'Id_Number':Id_Number, 
         'D_O_Birth':D_O_Birth, 
         'D_O_Issue':D_O_Issue, 
         'D_O_Expiry':D_O_Expiry}
    return data_dic


for i,j in enumerate(images):
    print(f"========== Image {i} Data  ==========")
    output = reader.readtext(rf'../NIC_Images/{j}')
    data=[]
    for a,b,c in output:
        data.append(b)
        print(b)
    print(get_data(data))
     
