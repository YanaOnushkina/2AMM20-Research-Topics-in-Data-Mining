import pysubgroup as ps  # from: https://github.com/flemmerich/pysubgroup/tree/master/pysubgroup/tests
import pandas as pd
from Algorithm2 import stable_recalculate

# Load the example dataset
data = []
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave1_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave2_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave3_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave4_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave5_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave6_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave7_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave8_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave9_full.csv"))
data.append(pd.read_csv("data/BrexitAttitudes_Data_wave10_full.csv"))

# ps.NumericTarget() -> read the documentation
target = ps.BinaryTarget('BrexitID', 'a Remainer')

full_rules = []

for x in data:
    searchspace = ps.create_selectors(x, ignore=['BrexitID'])
    task = ps.SubgroupDiscoveryTask(
        x,
        target,
        searchspace,
        result_set_size=10,
        depth=10,
        qf=ps.WRAccQF())
    result = ps.BeamSearch(10).execute(task)
    rules = result.to_dataframe()
    full_rules.append(rules)

for rules in full_rules:
    print(rules.to_string())

stable_recalculate(full_rules, data)


# rules.to_csv("./rules/Rules wave10")

# x = data[8][data[8]['EURef2016'] == 'Remain']
# x = x[x['profile_gross_personal'] == 'Not Asked or missing']
# print(x['BrexitID'].value_counts())
#
# print(data[8]['BrexitID'].value_counts())
