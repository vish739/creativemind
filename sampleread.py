import yaml

with open(r'sample.yml') as file:
    documents = yaml.full_load(file)
    #print(documents)
    print(documents.items)

#    for item, doc in documents.items():
#        print(item, ":", doc)

