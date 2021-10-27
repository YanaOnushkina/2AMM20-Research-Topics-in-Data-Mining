import pysubgroup as ps  # from: https://github.com/flemmerich/pysubgroup/tree/master/pysubgroup/tests
import pandas as pd
from Algorithm2 import stable_recalculate

# Load the example dataset
data = []
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave1_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave2_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave3_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave4_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave5_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave6_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave7_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave8_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave9_clean_nohindsite.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave10_clean_nohindsite.csv"))

# ps.NumericTarget() -> read the documentation
target = ps.BinaryTarget('BrexitID', 'a Remainer')

full_rules = []

for x in data:
    searchspace = ps.create_selectors(x, ignore=['BrexitID'])
    task = ps.SubgroupDiscoveryTask(
        x,
        target,
        searchspace,
        result_set_size=100,
        depth=10,
        qf=ps.WRAccQF())
    result = ps.BeamSearch(100).execute(task)
    rules = result.to_dataframe()
    full_rules.append(rules)

for rules in full_rules:
    print(rules.to_string())

stable_recalculate(full_rules)


# rules.to_csv("./rules/Rules wave10")

# x = data[8][data[8]['Poscountry'] == 'Somewhat negative effect']
# print(x['BrexitID'].value_counts())
#
# print(data[8]['BrexitID'].value_counts())
