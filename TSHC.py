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
    #print(end="\n")
    with open(pln_file_name,'r') as tfile_digger:
        for pln in tfile_digger.readlines():
            pln=pln.lower()
            if '.pln' in pln:
                #print(pln)
                try:
                    plan_to_input="{}".format(pln)
                    plan_to_input_remove_n = plan_to_input.rstrip('\n')
                    #print("\t[+]"+plan_to_input, end="")
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
                                        #print("\t",complete_tC_path)
                                        check_PT1=os.path.isfile(complete_tC_path)
                                        #print("@check_PT1", check_PT1)
                                        if os.path.isfile(complete_tC_path):
                                            #print("\t\t TC_Path=", complete_tC_path,end="\n")
                                            with open(complete_tC_path,'r') as tfile:
                                                line_count=0
                                                for line in tfile.readlines():
                                                    ex_driver_catch = re.findall(r'[p-xP-X]:\\', line)
                                                    line_count = line_count + 1
                                                    #print(ex_driver_catch)
                                                    if len(ex_driver_catch) >= 1:
                                                        print(ex_driver_catch, line_count, complete_tC_path)


                                    elif len(script_tname_split_list) <= 1:
                                        TC_Name = (script_tname_split_list[0]).rstrip()
                                        #print("\t TC_Name is {}".format(TC_Name))
                                        tfile_name = file_Name_Path(plan_to_input, 'file_path')
                                        complete_tC_path = tfile_name + TC_Name
                                        complete_tC_path = complete_tC_path.replace(" ", "")
                                        #print("\t",complete_tC_path)
                                        check_PT2 = os.path.isfile(complete_tC_path)
                                        #print("@CheckPT2", check_PT2)
                                        if os.path.isfile(complete_tC_path):
                                            #print("\t\t TC_Path=", complete_tC_path,end="\n")
                                            with open(complete_tC_path,'r') as tfile:
                                                line_count=0
                                                for line in tfile.readlines():
                                                    ex_driver_catch = re.findall(r'[p-xP-X]:\\', line)
                                                    line_count = line_count + 1
                                                    #print(ex_driver_catch)
                                                    if len(ex_driver_catch)>=1:
                                                        print(ex_driver_catch,line_count, complete_tC_path)



                                except:
                                    print('\t TFileinsidePlnfile: Could not open the test file from the location {}'.format(complete_tC_path))
                except:
                    print('\tPlnFile: Could not open the pln file from the location {}'.format(pln))
            if '.t' in pln:
                pln=pln.lower()
                plan_to_input = "{}".format(pln)
                plan_to_input_remove_n = plan_to_input.rstrip('\n')
                check_TO = os.path.isfile(plan_to_input_remove_n)
                #print("@CheckTO", check_TO)
                if os.path.isfile(plan_to_input_remove_n):
                    with open(plan_to_input_remove_n,'r') as tfile_1stlevel:
                        line_count=0
                        for line in tfile_1stlevel:
                            ex_driver_catch = re.findall(r'[p-xP-X]:\\', line)
                            line_count = line_count + 1
                            #print(ex_driver_catch)
                            if len(ex_driver_catch)>=1:
                                print(ex_driver_catch,line_count, plan_to_input_remove_n)

            # if 'TC' in pln:
            #     try:
            #         plan_to_input = "{}".format(pln)
            #         plan_to_input_remove_n = plan_to_input.rstrip('\n')
            #         check_TO = os.path.isfile(plan_to_input_remove_n)
            #         # print("@CheckTO", check_TO)
            #         #if os.path.isfile(plan_to_input_remove_n):
            #         with open(plan_to_input_remove_n, 'r') as tfile_1stlevel:
            #             line_count = 0
            #             for line in tfile_1stlevel:
            #                 ex_driver_catch = re.findall(r'[p-xP-X]:\\', line)
            #                 line_count = line_count + 1
            #                 # print(ex_driver_catch)
            #                 if len(ex_driver_catch) >= 1:
            #                     print(ex_driver_catch, line_count, plan_to_input_remove_n)
            #     except:
            #         print("This could be a different file and not .t file: {}".format(pln))









planfile_open_read("BHC_Feeder_Masterplan.txt")
#Master_plan_feeder.txt
#BHC_Feeder_Masterplan.txt


###########################Rough Area####################
#Back up for ex_driver_catch
# try:
#     ex_driver_catch = re.findall('[p-xP-X]:', line)
#     print(ex_driver_catch)
#     if ex_driver_catch in line:
#         print('The test file with the path {} is accessing external driver file @ {}'.format(complete_tC_path, line))
# except:
#     print('Finding External Drive files script failed')





