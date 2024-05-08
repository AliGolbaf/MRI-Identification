'''
    1. Identifying MRI sequences based on (TE and TR)
'''

class Identifying_MRI_Sequences_Series_Description:
    
    ################################################################################    
    # T1 Charactristics
    def check(self, series_description, empty_var):
        
        self.series_description = series_description
        self.empty_var = empty_var
        
        # change self.series_description to lower case
        self.series_description = str.lower(self.series_description)
        
        # t1
        if "t1" in self.series_description: 
            if "gad" not in self.series_description:                
                if "c" not in self.series_description:                
                    if "mprage" not in self.series_description:
                        var = "T1"
                        self.empty_var.append(var)
                
        # t1c
        if "t1" in self.series_description:
            
            if "gad" in self.series_description:
                var = "T1C"
                self.empty_var.append(var)
                
            if not self.empty_var:
                if "c" in self.series_description: 
                    var = "T1C"
                    self.empty_var.append(var)
            
            if not self.empty_var:
                if "mprage" in self.series_description:
                    var = "T1C"
                    self.empty_var.append(var)
    
        # t2
        if "t2" in self.series_description:
            if "flair" not in self.series_description:
                var = "T2"
                self.empty_var.append(var)
        
        # dwi
        if "dwi" in self.series_description:
            var = "DWI"
            self.empty_var.append(var)
            
        # flair
        if "flair" in self.series_description:
            if not self.empty_var:
                var = "FLAIR"
                self.empty_var.append(var)
        
        return self.empty_var
        

    
 