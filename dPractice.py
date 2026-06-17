import numpy as np
import time
size = 6
list1 = list(range(1,size+1))
list2 = list(range(1,size+1))

vec1 = np.array(list1)
vec2 = np.array(list2)

start_time = time.time()
sum_list = [a+b for a,b in zip(list1,list2)] #forget1 zip(l1,l2)
loop_time = time.time()-start_time
print (f"Total time taken for normal Loop: {loop_time:6f}")

start_time_vec = time.time()
vec_sum = vec1 + vec2
vector_time = time.time()-start_time_vec
print(f"Total time taken for vector Loop: {vector_time:6f}")

print(f"Vector Loop is {loop_time/vector_time:3f} times faster")

print(vec1@vec2) #dot product two vectors ki amne samne multiply aur phr us single array ka sum

vec3=vec1.reshape(3,-1) #reshaping rows,column add -1 for other to automate
print(vec3) 
print(np.arange(1,10)) # arange remember the spelling np.arange(1,10)
print(vec1)