# this is a 24 point game .
# it will display all the combinations which can generate 24 points from the user input. 
# author: Liu Zhe
# date: june-3-2013

import sys
import re

def format_exp(s):
    s=re.sub('\+',' + ',s)
    s=re.sub('\-',' - ',s)
    s=re.sub('\*',' * ',s)
    s=re.sub('\/',' / ',s)
    return s

warning='''
The program will calcuate 24 point with 4 number.
Please input 4 arguments after command,
and every argument must a number. 
Example: calc24point.py 1 2 3 4
'''    
if len(sys.argv) != 5:
    print warning
    sys.exit()


nums1=[]
for arg in sys.argv[1:]:
    try:
        nums1.append(str(float(arg)))
    except ValueError:
        print 'Error: Invalid arguments.Every argument must be a number.'
        sys.exit()

all_nums=[]
for e1 in nums1:
    nums2=nums1[:]
    nums2.remove(e1)
    for e2 in nums2:
        nums3=nums2[:]
        nums3.remove(e2)
        for e3 in nums3:
            nums4=nums3[:]
            nums4.remove(e3)
            e4=nums4[0]
            cur_nums=[e1,e2,e3,e4]
            all_nums.append(cur_nums)

actions=('+','-','*','/')
all_actions=[]
for a1 in actions:
    for a2 in actions:
        for a3 in actions:
            cur_actions=[a1,a2,a3]
            all_actions.append(cur_actions)

count=0
for new_nums in all_nums:
    for new_actions in all_actions:
        all_exp=[]
        lb,rb=('(',')')
        all_exp.append(new_nums[0]+new_actions[0]+new_nums[1]+new_actions[1]+new_nums[2]+new_actions[2]+new_nums[3])
        all_exp.append(lb+new_nums[0]+new_actions[0]+new_nums[1]+rb+new_actions[1]+new_nums[2]+new_actions[2]+new_nums[3])
        all_exp.append(new_nums[0]+new_actions[0]+lb+new_nums[1]+new_actions[1]+new_nums[2]+rb+new_actions[2]+new_nums[3])
        all_exp.append(new_nums[0]+new_actions[0]+new_nums[1]+new_actions[1]+lb+new_nums[2]+new_actions[2]+new_nums[3]+rb)
        all_exp.append(lb*2+new_nums[0]+new_actions[0]+new_nums[1]+rb+new_actions[1]+new_nums[2]+rb+new_actions[2]+new_nums[3])
        all_exp.append(lb+new_nums[0]+new_actions[0]+lb+new_nums[1]+new_actions[1]+new_nums[2]+rb*2+new_actions[2]+new_nums[3])     
        all_exp.append(new_nums[0]+new_actions[0]+lb*2+new_nums[1]+new_actions[1]+new_nums[2]+rb+new_actions[2]+new_nums[3]+rb)
        all_exp.append(new_nums[0]+new_actions[0]+lb+new_nums[1]+new_actions[1]+lb+new_nums[2]+new_actions[2]+new_nums[3]+rb*2)
        all_exp.append(lb+new_nums[0]+new_actions[0]+new_nums[1]+rb+new_actions[1]+lb+new_nums[2]+new_actions[2]+new_nums[3]+rb)

        for exp in all_exp:
            try:
                if eval(exp)==24:
                    count=count+1
                    result=format_exp(exp)
                    if count%2==0:
                        print '%30s = 24'%(result)
                    else:
                        print '%30s = 24'%(result),
            except ZeroDivisionError:
                continue

if count==0:
    print '%s will never equal to 24'%(sys.argv[1:])
else:
    print "Total %d results"%(count)

    
            

                    
            
            

    

    
    
    
                
            
        
        

        






