#pip install playsound==1.2.2 add this to the report
from playsound import playsound
import random;

def mergeSort(product_id):

    
    if len(product_id)>1:
        middle=len(product_id)//2
        start = product_id[:middle]
        end = product_id[middle:]
        print("Splitting",product_id)
        print("Left Half:",start)
        print("Right Half:",end)
        playsound("boing_poing.wav")
        print()

        mergeSort(start)
        mergeSort(end)

        startCount=0
        endCount=0
        newCount=0

        while startCount<len(start) and endCount<len(end):
            if start[startCount] < end[endCount]:
                product_id[newCount]=start[startCount]
                startCount+=1
            else:
                product_id[newCount]=end[endCount]
                endCount+=1
            newCount+=1
            
        while startCount<len(start):
            product_id[newCount]=start[startCount]
            startCount+=1
            newCount+=1
        while endCount<len(end):
            product_id[newCount]=end[endCount]
            endCount+=1
            newCount+=1
        
        print("Merging",start,end,"=", product_id)
        playsound("boing_poing.wav")
        print()
        



product_id=[]
num=int(input("How many numbers would you like in the product id array: "))

for i in range(num):
    product_id.append(random.randrange(1,100))
print("\nThe array is the following:\n",product_id)
print()
mergeSort(product_id)
print("\n\n\n")
print("Sorted Array:\n",product_id)
playsound("applause_y.wav")