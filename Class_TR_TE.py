'''
    1. Identifying MRI sequences based on (TE and TR)
'''

class Identifying_MRI_Sequences_TR_TE:
    
    ################################################################################    
    # T1 Charactristics
    def t1_t2_check(self, TR, TE, empty_var_tr_te):

        if TR < 800 and TE < 30:
            var = "T1"
            empty_var_tr_te.append(var)
        
        if TR > 2000 and TE > 80: 
            var = "T2"
            empty_var_tr_te.append(var)

        return empty_var_tr_te

 