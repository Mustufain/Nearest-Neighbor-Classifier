import operator
import sys


training = sys.argv[1]
test = sys.argv[2]
answers = sys.argv[3]
train_dict = {}
train_class={}
test_dict={}
test_class={}


with open(training,"r") as training_file:
  row_count=0
  for row in training_file:
    row_count = row_count + 1
    train_dict[row_count] = map(int,row.split(" ")[1:])
    train_class[row_count] = row.split(" ")[:1]
    

with open(test,"r") as test_file:
  row_count = 0
  for row in test_file:
    row_count = row_count + 1
    test_dict[row_count] = map(int,row.split(" "))

with open(answers,"r") as answers_file:
  row_count = 0
  for row in answers_file:
    row_count = row_count + 1
    test_class[row_count] = row.split(" ")
    
#calculate distance

for key1,value1 in test_dict.items():         #First test data
  distance=[]
  test_train={}
  min_classlist=[]
  a=""
  for key2,value2 in train_dict.items():    
    
    
    dist =  sum(map(abs,map(operator.sub,test_dict[key1],train_dict[key2])))
    
    distance.append(sum(map(abs,map(operator.sub,test_dict[key1],train_dict[key2]))))
    
    test_train[key2] =  dist
    
    
  
  min_dist = min(distance)
  for key,value in test_train.items():
    if value==min_dist:
      min_classlist.append(train_class[key])
  
  for i in test_dict[key1]:
    j=str(a)+str(i)+" "
    a=j
  
  
  sys.stdout.write("Item: "+j+"prediction: "+ min(min_classlist)[0]+" correct: "+ test_class[key1][0])