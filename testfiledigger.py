import os.path
import re

def listitemclubbed(listName):
    sentence = listName
    sent_str = ""
    for i in sentence:
        sent_str += str(i) + '\\'
    sent_str = sent_str[:-1]
    return sent_str+'\\'

def file_Name_Path(pln_path,request_for,testORplan=".pln"):
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
    print(end="\n")
    with open(pln_file_name,'r') as tfile_digger:
        for pln in tfile_digger.readlines():
            if '.pln' in pln:
                try:
                    plan_to_input="{}".format(pln)
                    plan_to_input_remove_n = plan_to_input.rstrip('\n')
                    print(plan_to_input, end="")
                    #return plan_to_input
                    with open(plan_to_input_remove_n, 'r') as pln_file:
                        for tname in pln_file.readlines():
                            if '.t' in tname:
                                try:
                                    #print(tname)
                                    script_tname_split_list = tname.split(":")
                                    if len(script_tname_split_list)>=2:
                                        TC_Name = (script_tname_split_list[1]).rstrip()
                                        print("\t TC_Name is {}".format(TC_Name))
                                        tfile_name = file_Name_Path(plan_to_input, 'file_path')
                                        complete_tC_path = tfile_name + TC_Name
                                        complete_tC_path = complete_tC_path.replace(" ", "")
                                        #print("\t",complete_tC_path)
                                        if os.path.isfile(complete_tC_path):
                                            print("\t\t TC_Path=",complete_tC_path, end="\n")
                                    if len(script_tname_split_list) <= 1:
                                        TC_Name = (script_tname_split_list[0]).rstrip()
                                        print("\t TC_Name is {}".format(TC_Name))
                                        tfile_name = file_Name_Path(plan_to_input, 'file_path')
                                        complete_tC_path = tfile_name + TC_Name
                                        complete_tC_path = complete_tC_path.replace(" ", "")
                                        #print("\t",complete_tC_path)
                                        if os.path.isfile(complete_tC_path):
                                            print("\t\t TC_Path=", complete_tC_path,end="\n")

                                except:
                                    print('\t Could not open the test file from the location {}'.format(complete_tC_path))


                except:
                    print('Could not open the pln file from the location {}'.format(pln))


# def main_file_open(main_file_name):
#     plan_to_input=planfile_open_read(main_file_name)
#     plan_to_input_remove_n=plan_to_input.rstrip('\n')
#     with open(plan_to_input_remove_n, 'r') as pln_file:
#         for tname in pln_file.readlines():
#             if '.t' in tname:
#                 print(tname)
#                 script_tname_split_list = tname.split(":")
#                 TC_Name = (script_tname_split_list[1]).rstrip()
#                 tfile_name = file_Name_Path(plan_to_input, 'file_path')
#                 complete_tC_path = tfile_name + TC_Name
#                 complete_tC_path=complete_tC_path.replace(" ","")
#                 if os.path.isfile(complete_tC_path):
#                     print(complete_tC_path)
#                     return complete_tC_path


planfile_open_read("23-1-18-mapping.txt")








