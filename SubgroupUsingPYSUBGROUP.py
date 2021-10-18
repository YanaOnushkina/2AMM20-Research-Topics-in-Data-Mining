import pysubgroup as ps #from: https://github.com/flemmerich/pysubgroup/tree/master/pysubgroup/tests
import pandas as pd

# Load the example dataset
data = pd.read_csv("data/BrexitAttitudes_Data_wave1.csv")

#ps.NumericTarget() -> read the documentation
target = ps.BinaryTarget('BrexitID', 'a Remainer')

searchspace = ps.create_selectors(data, ignore=['BrexitID'])
task = ps.SubgroupDiscoveryTask (
    data,
    target,
    searchspace,
    result_set_size=5,
    depth=4,
    qf=ps.WRAccQF())
result = ps.BeamSearch().execute(task)

rules = result.to_dataframe()

rules.to_csv("./rules/Rules wave1")

