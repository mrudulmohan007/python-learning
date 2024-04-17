print("This IT Organisation")
print("Find out your match")
print("Enter capitalised values")
DevOps = ["Jenkins","Ansible","Bash","Python","Puppet","Docker","Kubernetes","terraform"]
Development=("Nodejs","Angularjs","Java",".net","python")
cntr_emp1 = {"Name": "Santa", "skill":"blockhain","code":1024}
cntr_emp2 = {"Name": "rocky", "skill":"AI","code":1218}


usr_skill=input("Enter your desired skill: ")

if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps Team.")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print("We do not have the skills you searched, check and retry again ! ")