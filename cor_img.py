import copy
import json
import pandas as pd
import shutil
import os    
def corrupted(img):

    df = pd.read_csv(r"C:\Users\NHI239\Downloads\imagespath.csv")
    
    img_paths = list(df['CorruptedImages'])
    #print("Corrupted Images:     ",img_paths)
    im = []
    corrupted_img_id = []
    #print("Deleting corrupted images")
    l = len(img)

    for i in range(l):
    
        if img[i]['file_name'] not in img_paths:
            im.append(img[i])
        else:
            corrupted_img_id.append(img[i]['id'])
            #print("corrupt image id: ", img[i]['id'])
       
    json_array['images'].extend(im)
    #print(json_array['images'])
    print("corrupt image id: ", corrupted_img_id)
    return corrupted_img_id


def annotations(annotate,c):
    
    a = []
    #print("Deleting corrupted image relations in annotations")
    le = len(annotate)
    for i in range(le):
    
        if annotate[i]['image_id'] not in c:
            a.append(annotate[i])
    json_array['annotations'].extend(a)
    return
    
def images(img,c):
    
    im = []
    #print("Deleting corrupted images")
    l = len(img)
    for i in range(l):
    
        if img[i]['id'] not in c:
            im.append(img[i])
                 
    json_array['images'].extend(im)
    return 
data = {}
data['info'] = {}
data['licenses']=[]
data['images']=[]
data['annotations']=[]
data['categories']=[]


data['info'] = {
        "description": "This is dataset.",
        "url": "https://annotation.nslhub.com",
        "version": "1.0",
        "year": 2020,
        "contributor": "Annotation NslHub",
        "date_created": "01/04/2021"
        }

data['licenses'].append({
            "url": "https://annotation.nslhub.com",
            "id": 1,
            "name": "Annotation NslHub"
        })

data_root = r"D:\deep_learning"
#output file name
with open(r"D:\OmniData\COCO_model1.json", 'w') as outfile:
    json.dump(data, outfile)
#output file name
output_file=open(r"D:\OmniData\COCO_model1.json") 
json_array = json.load(output_file)

output_file.close()

#input file name    
input_file=open(r"D:\OmniData\COCO_model.json") 
js = json.load(input_file)
input_file.close()

print(len(js['categories']))
print(len(js['annotations']))
print(len(js['images']))

print("started")
#print(js["images"])
c = corrupted(js["images"])
print("corrupted_images", c)
annotations(js["annotations"],c)        
json_array['categories'].extend(js["categories"])
print(len(json_array['categories']))
print(len(json_array['annotations']))
print(len(json_array['images']))
r=json_array['images']
#print(r)
for x in r:
    a=(x['file_name'])
    #print(type(a))
    path=r"D:\deep_learning"

    source=os.path.split(a)
    #print(source[1])
    #print(source)
    img_path=path+"\\images\\" +source[1]
    #files=os.listdir(source)
    #print(source)
    destination = r"D:\deep_learning\new"
    #for file in files:
      # print(file)
    shutil.copyfile(img_path, destination+"\\"+source[1])
#print(json_array['images'][1]['file_name'])
#print(json_array['images'][0])
#output file name            
with open(r"D:\OmniData\COCO_model1.json", 'w') as final_outfile:
    json.dump(json_array, final_outfile)
final_outfile.close()
