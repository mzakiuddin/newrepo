#!usr/bin/python
import pandas as pd
import numpy as np
df = pd.read_excel('https://s3-us-west-2.amazonaws.com/dcind-interns/cleansing-input/CRM+Lead+Data+Report_20120110_DNB_Freshagug_list_part_26.xls')
list=[]
# middle name has nan as float so replacing all nans with empty string
df1 = df.replace(np.nan, '', regex=True)
df1 = df1.rename(columns={'ch_phone1': 'Ph_1', 'ch_phone2': 'Ph_2', 'Fname': 'First_Name', 'Mname': 'Middle_Name', 'Lname': 'Last_Name', 'Emailid': 'Email_id', 'Martial Status': 'Marital_Status',
                            'Sex': 'Gender', 'Landmarks': 'Address_1', 'State': 'State_Code', 'Zip': 'ZipCode', 'Faxno': 'Fax', 'Contact Name': 'Contact_Name', 'Web Address': 'Domain',
                            'Name 2': 'Name2', 'Email 2': 'Email2', 'Title 2': 'Title2', 'Company Name 2': 'Cname2', 'Address 2': 'Add2', 'City 2': 'City2', 'State 2': 'State2', 'Zip 2': 'Zip2',
                          'Company Name': 'Company', 'LEVEL': 'Level'})
df1 = df1[df1.Company != '']
for row in df1.iterrows():
    for ele in row:
        if isinstance(ele, pd.Series):

            #creating new series for the fields that are to be altered
            s1 = pd.Series()
            # the field Contact_Name is empty ,populating it by concatenation of first,middle and last name
            if ele['Contact_Name'] == '':
                fname = ele['First_Name']
                mname = ele['Middle_Name']
                lname = ele['Last_Name']
                ele['Contact_Name'] = str(fname) + ' ' + str(mname) + ' ' + str(lname)
            # the gender field is empty, populating it by considering the value in Prefix field
            if ele['First_Name'] == '' or ele['Middle_Name'] == '' or ele['Last_Name']:
                fullname = ele['Contact_Name']
                splitname = fullname.split(' ')
                if len(splitname) == 3:
                    ele['First_Name'] = splitname[0]
                    ele['Middle_Name'] = splitname[1]
                    ele['Last_Name'] = splitname[2]
                elif len(splitname) == 2:
                    ele['First_Name'] = splitname[0]
                    ele['Last_Name'] = splitname[1]
                elif len(splitname) == 1:
                    ele['First_Name'] = splitname[0]
            if ele['Prefix'] == 'Mr':
                ele['Gender'] = 'Male'
            elif ele['Prefix'] == 'Ms':
                ele['Gender'] = 'Female'



            list.append(ele)
            # These are the fields where the contact data of other person with the same company
            if ele['Name2'] != '' or ele['Email2'] != '' or ele['Title2'] != '' or ele['Cname2'] != '' or ele['Add2'] != '' or ele['City2'] != '' or ele['State2'] != '' or ele['Zip2'] != '':
                # if the second company exists then, will create a new company with that name
                if ele['Cname2'] != '':
                    comp2 = ele['Cname2']
                    s1['Company'] = comp2
                #if not, all the previous values are the same
                else:
                    comp2 = ele['Company']
                    s1['Company'] = comp2
                    s1['Address_1'] = ele['Address_1']
                    s1['City'] = ele['City']
                    s1['State_Code'] = ele['State_Code']
                    s1['ZipCode'] = ele['ZipCode']
                    s1['Country'] = ele['Country']
                    s1['Domain'] = ele['Domain']
                    s1['Technology'] = ele['Technology']
                #if a contact name exists, write a new record with this name and all the company details are the same
                if ele['Name2'] != '':
                    name2 = ele['Name2']
                    cont_name2 = name2.split(' ')
                    name2 = name2.replace("Mr", "") if "Mr" in name2 else name2
                    name2 = name2.replace("Ms", "") if "Ms" in name2 else name2
                    s1['Contact_Name'] = name2
                    # split the name to populate the fields
                    if len(cont_name2) == 4:
                        if cont_name2[0] == "Mr" or cont_name2[0] == "Ms":
                            s1['Prefix'] = cont_name2[0]
                            s1['First_Name'] = cont_name2[1]
                            s1['Middle_Name'] = cont_name2[2]
                            s1['Last_Name'] = cont_name2[3]
                            if s1['Prefix'] == 'Mr':
                                s1['Gender'] = 'Male'
                            elif s1['Prefix'] == 'Ms':
                                s1['Gender'] = 'Female'
                    elif len(cont_name2) == 3:
                        if cont_name2[0] == "Mr" or cont_name2[0] == "Ms":
                            s1['Prefix'] = cont_name2[0]
                            s1['First_Name'] = cont_name2[1]
                        # s1['Middle_Name'] = cont_name2[1]
                            s1['Last_Name'] = cont_name2[2]
                            if s1['Prefix'] == 'Mr':
                                s1['Gender'] = 'Male'
                            elif s1['Prefix'] == 'Ms':
                                s1['Gender'] = 'Female'
                        else:
                            s1['First_Name'] = cont_name2[0]
                            s1['Middle_Name'] = cont_name2[1]
                            s1['Last_Name'] = cont_name2[2]
                    elif len(cont_name2) == 2:
                        # if cont_name2[0] == "Mr" or cont_name2[0] == "Ms":
                        #     s1['Prefix'] = cont_name2[0]
                        s1['First_Name'] = cont_name2[0]
                        s1['Last_Name'] = cont_name2[1]
                    elif len(cont_name2) == 1:
                        s1['First_Name'] = cont_name2[0]
                else:#if the person is same , these details remain same
                    name2 = ele['Contact_Name']
                    s1['Contact_Name'] = ele['Contact_Name']
                    s1['First_Name'] = ele['First_Name']
                    s1['Middle_Name'] = ele['Middle_Name']
                    s1['Last_Name'] = ele['Last_Name']
                    s1['Prefix'] = ele['Prefix']
                    s1['Gender'] = ele['Gender']
                    s1['Email_id'] = ele['Email_id']

                #if email exists , assign as it is , unique for a person
                if ele['Email2'] != '':
                    email2 = ele['Email2']
                    s1['Email_id'] = email2
                #write a row if the person has two titles
                if ele['Title2'] != '':
                    title2 = ele['Title2']
                    s1['Title'] = title2
                # write a row if the company has two addresses
                if ele['Add2'] != '':
                    add2 = ele['Add2']
                    s1['Address_1'] = add2

                if ele['City2'] != '':
                    city2 = ele['City2']
                    s1['City'] = city2

                if ele['State2'] != '':
                    state2 = ele['State2']
                    s1['State_Code'] = state2

                if ele['Zip2'] != '':
                    zip2 = ele['Zip2']
                    s1['ZipCode'] = zip2

                if ele['Level'] == 'Manager-Level':
                    s1['Level'] = 'Managers, Supervisors'
                if ele['Level'] == 'VP-Level':
                    s1['Level'] = 'Vice Presidents'
                if ele['Level'] == 'C-Level':
                    s1['Level'] = 'Senior Officers, C-Level'
                if ele['Level'] == 'Director-Level':
                    s1['Level'] = 'Directors'
                if ele['Level'] == 'Staff':
                    s1['Level'] = 'Staff'


                list.append(s1)


req_flds = ['Prefix', 'Contact_Name', 'First_Name', 'Middle_Name', 'Last_Name', 'Title', 'Level', 'Designation','Speciality', 'Gender', 'Marital_Status', 'Company', 'Domain', 'Email_id', 'Ph_1', 'Ph_2',
       'Fax','Address_1', 'Address_2', 'Country', 'State', 'State_Code', 'City', 'ZipCode', 'Company_description','sub_industry', 'Industry', 'sic', 'naics', 'naics_description', 'Technology']


dataframe = pd.DataFrame(list, columns=req_flds)
print(dataframe)
# dataframe.to_csv('https://s3-us-west-2.amazonaws.com/dcind-interns/cleansing-input/CRM+Lead+Data+Report_20120110_DNB_Freshagug_list_part_26.csv', index=False)
dataframe.to_csv('pop.csv') 

#
# /home/harvest/Desktop/madamnew/securefolder1/MZData/All CSV/Master Data - VARIED FORMATS Clean









