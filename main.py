import pandas as pd

#Loading datas
data = pd.read_excel(r'excel\Axel LYO Vials.xlsx')

#Setting up Conditions

solutions = [' lsg', ' lösung', ' losung', ' loesung', ' solut', ' sol.', ' soln', ' THF', ' ethyl acetate', ' dmf', ' dimethylformamide'
' dioxane', ' tetrahydrofuran',' diethylether', ' diethyl ether', ' MTBE', ' methyltertbutylether', ' ethyl acetate', ' toluene', ' toluol', ' aceton', 
' dcm', ' dichloromethan', ' methylenchlorid', 'WT%', 'WT %']
exclusion_solutions = ['anisol']

hydride = ['hydrid']   
exclusion_hydride = ['anhydrid']

refrigeration = ['cooling', 'freezer']
risk = ['1', '4.2', '4.3', '5.1A', '5.2']
cas_number = ['302-01-2', '60-34-4', '10025-87-3', '75-35-4', '75-77-4', '1113-78-6', '10294-34-5', '10294-33-4'] #Hydrazine,, Methylhydrazine, Oxalyl chloride, 1,1-dichloroethylene, TMS-Cl, TRI-SEC-Butylborane, Boron trichloride, BBr3 => résultats sécurité depuis 2021

#Preparing filters
filter_name_sol = data['Product Name'].str.contains('|'.join(solutions), na=False, case=False)
filter_name_hydride = data['Product Name'].str.contains('|'.join(hydride), na=False, case=False)
filter_exclusion_solutions = data['Product Name'].str.contains('|'.join(exclusion_solutions), na=False, case=False)
filter_exclusion_hydride = data['Product Name'].str.contains('|'.join(exclusion_hydride), na=False, case=False)
filter_refrigeration = data['Refrigeration'].str.contains('|'.join(refrigeration), case=False, na=False)
filter_storageclass = data['Storage Class'] == '|'.join(risk)
filter_cas = data['CAS Number'].str.contains('|'.join(cas_number), na=False, case=False)

#create a new filtered Dataframe
filtered_data = data[(filter_name_sol&~filter_exclusion_solutions)|(filter_name_hydride&~filter_exclusion_hydride)|filter_refrigeration|filter_storageclass|filter_cas]

#Find duplicates
duplicates = data.groupby(data['Str. ID'].tolist(), as_index=False).size()
filter_duplicates = duplicates['size'] > 5

#Filtering duplicates
ID_over_x = duplicates[filter_duplicates]
filter_ID_over_x = data['Str. ID'].isin(ID_over_x['index'])
filtered_duplicates = data[filter_ID_over_x]


#Write results on excel document
with pd.ExcelWriter("excel/Filtered_recheck.xlsx") as writer:
    filtered_data.to_excel(writer, sheet_name="Filter")
    filtered_duplicates.to_excel(writer, sheet_name="duplicates")


