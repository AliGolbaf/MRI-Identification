"""
Identification of MRIs based on their series description and (TR, TE)
written by: Ali Golbaf

"""
################################################################################
""" Libraries """
import pandas as pd
import os

################################################################################
""" Classes """
from Class_TR_TE import Identifying_MRI_Sequences_TR_TE as TRTE
from Class_Series_Description import Identifying_MRI_Sequences_Series_Description as SD
################################################################################
""" Input data """
path_to_tsv_folder = r"C:\Users\agolbaf\OneDrive - University of Plymouth\Temporary_Files\2024_05_04\University_of_Plymouth_Biomedical_Research_Laboratories\Data_Nifti\TSV_Files"
subjects = os.listdir(path_to_tsv_folder)

################################################################################
""" Main loop """
Data = []

for subject in subjects:
    
    path_to_tsv_file = os.path.join(path_to_tsv_folder,subject, "Edited_dicominfo_ses-001.tsv")
    data = pd.read_csv(path_to_tsv_file , sep='\t')
    
    """ dcm_dir_name, TR, TE, series_description """
    subject_names = data["dcm_dir_name"].values
    TRs = data["TR"].values
    TEs = data["TE"].values
    series_descriptions = data["series_description"].values
    
    """ Loop inside the file """
    for i in range(len(subject_names)):
        
        empty_var_tr_te = []
        empty_var_series_description = []
        
        subject_name = str(subject_names[i])
        TR = float(TRs[i]) * 1000  #(msec to sec)
        TE = float(TEs[i])
        series_description = str(series_descriptions[i])
        
        """ Check based on TR and TE """
        ########################################################################
        t1_t2_check_tr_te = TRTE().t1_t2_check(TR, TE, empty_var_tr_te)
        
        if not t1_t2_check_tr_te:
            t1_t2_check_tr_te = "-"
            
        """ Check based on series description """
        ########################################################################
        series_description_check = SD().check(series_description, empty_var_series_description)
        
        if not series_description_check:
            series_description_check = "-"
        
        row = [subject, 
               "ses-001",
               subject_name,
               series_description,
               t1_t2_check_tr_te,
               series_description_check]
        
        Data.append(row)


columns = ["Subject",
           "Session", 
           "dcm_dir_name",
           "series_description",
           "Check based on TR and TE (T1 Or T2)",
           "Check based on series description"]
        
# Sequence_List = 0
df = pd.DataFrame(Data, columns=columns)
df.to_csv('Sequence_List.csv', index=False)   
