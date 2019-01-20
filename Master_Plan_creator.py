import os.path
import re

def listitemclubbed(listName):
    sentence = listName
    sent_str = ""
    for i in sentence:
        sent_str += str(i) + '\\'
    sent_str = sent_str[:-1]
    return sent_str+'\\'

def file_Name_Path(pln_path,request_for):
    planfile_directory_split_list=[]

    if request_for=="file_name":
        planfile_directory_split_list= str(pln_path).split("\\")
        planfile_Name=planfile_directory_split_list[-1]
        #print("{}"+"name is".format(testORplan),planfile_Name)
        return planfile_Name
    if request_for=="file_path":
        planfile_directory_split_list = str(pln_path).split("\\")
        path_name_list=planfile_directory_split_list[0:-1]
        planfile_path=listitemclubbed(path_name_list)
        #print("{}"+"path is".format(testORplan),planfile_path)
        return planfile_path
def planfile_open_read(pln_file_name):
    #pln_file_cleaned=pln_file_name.replace(r"\",'//')
    with open(pln_file_name,'r') as tfile_digger:
        for pln in tfile_digger.readlines():
            pln_TC=pln
            pln=pln.lower()
            if 'machine' in pln:
                print(pln)
            if len(pln) == 5 or len(pln) == 6 or len(pln) == 7:
                print(pln)
            if '.pln' in pln:
                try:
                    plan_to_input="{}".format(pln)
                    plan_to_input_remove_n = plan_to_input.rstrip('\n')
                    print("[+] ",plan_to_input, end="")
                    #return plan_to_input
                    with open(plan_to_input_remove_n, 'r') as pln_file:
                        for tname in pln_file.readlines():
                            if '.t' in tname:
                                try:
                                    #print(tname)
                                    script_tname_split_list = tname.split(":")
                                    if len(script_tname_split_list)>=2:
                                        TC_Name = (script_tname_split_list[1]).rstrip()
                                        #print("\t TC_Name is {}".format(TC_Name))
                                        tfile_name = file_Name_Path(plan_to_input, 'file_path')
                                        complete_tC_path = tfile_name + TC_Name
                                        complete_tC_path = complete_tC_path.replace(" ", "")
                                        if os.path.isfile(complete_tC_path):
                                            #print("\t\t TC_Path=",complete_tC_path, end="\n")
                                            print("\t[ ] ",complete_tC_path)
                                    if len(script_tname_split_list) <= 1:
                                        TC_Name = (script_tname_split_list[0]).rstrip()
                                        print("\t TC_Name is {}".format(TC_Name))
                                        tfile_name = file_Name_Path(plan_to_input, 'file_path')
                                        complete_tC_path = tfile_name + TC_Name
                                        complete_tC_path = complete_tC_path.replace(" ", "")
                                        #print("\t",complete_tC_path)
                                        if os.path.isfile(complete_tC_path):
                                            #print("\t\t TC_Path=", complete_tC_path,end="\n")
                                            print("\t[ ] ", complete_tC_path)

                                except:
                                    print('\t Could not open the test file from the location {}'.format(complete_tC_path))
                except:
                    print('Could not open the pln file from the location {}'.format(pln))
            if '.t' in pln:
                try:
                    plan_to_input = "{}".format(pln)
                    plan_to_input_remove_n = plan_to_input.rstrip('\n')
                    if os.path.isfile(plan_to_input_remove_n):
                        # print("\t\t TC_Path=", complete_tC_path,end="\n")
                        print(plan_to_input_remove_n)
                except:
                    print("Could not find the TC assigned under Pid in SCTM")

            if ' TC' in pln_TC:
                try:
                    plan_to_input = "{}".format(pln_TC)
                    plan_to_input_remove_n = plan_to_input.rstrip('\n')
                    print(plan_to_input_remove_n)

                    #if os.path.isfile(plan_to_input_remove_n)==False:
                        # print("\t\t TC_Path=", complete_tC_path,end="\n")

                        #pass

                except:
                    print("TC_Could not find the TC assigned under Pid in SCTM")


planfile_open_read("Master_plan_feeder.txt")
#Master_plan_feeder.txt
#BHC_Feeder_Masterplan.txt






