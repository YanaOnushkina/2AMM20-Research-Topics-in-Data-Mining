import pandas as pd


def stable_recalculate(subgroups_years, data):
    results = []
    for index, year in enumerate(subgroups_years):
        results.append({"year": index, "results": calculate_year(year, subgroups_years, data)})
    print(results)


def calculate_year(year, subgroup_years, data):
    results = []
    for index, row in year.iterrows():
        if index == 10:
            print("\n")
            break
        name, qualities = calculate_subgroup(row, subgroup_years, data)
        penalty = penalty_factor(qualities)
        new_quality = row['quality'] * penalty
        results.append(
            {"subgroup": name, "penalty": penalty, "old quality": row['quality'], "new_quality": new_quality})
    print(results)
    return results


def calculate_subgroup(subgroup, subgroup_years, data):
    # print(subgroup['subgroup'])
    subgroup_name = subgroup['subgroup']

    combined_qualities = []
    for i in range(0, 10):
        try:
            quality = subgroup_years[i].loc[subgroup_years[i]['subgroup'] == subgroup_name].iloc[0]['quality']
            # print(quality)
            combined_qualities.append(quality)
        except:
            print("exception")
            print(i + 1, subgroup_name)
            quality = manual_calculation(i, subgroup_name, data)
            combined_qualities.append(quality)
    print(subgroup_name, combined_qualities)

    return subgroup_name, combined_qualities


def penalty_factor(qualities):
    years = len(qualities)
    print(years)

    total_sum = 0

    for i in range(years):
        for j in range(years):
            if i != j:
                x = relative_similarity(qualities[i], qualities[j])
                total_sum += x

    print(1 / (years * (years - 1)) * total_sum, "\n")
    return 1 / (years * (years - 1)) * total_sum


def relative_similarity(i, j):
    if i == 0 and j == 0:
        return 1
    similarity = 1 - (abs(i - j) / max(i, j))
    return similarity


def manual_calculation(year, subgroup_name, data):
    rules = subgroup_name.split(" AND ")
    x = data[year]
    for rule in rules:
        print(rule, year)
        if "=" in rule:
            rule = rule.split("==")
        elif "<" in rule:
            rule = rule.split("<")
        type_var = rule[0]
        target = rule[1].replace("\'", "")
        print(type_var, target)
        x = x[x[type_var] == target]
        if x.empty:
            return 0.0

    x_series = x['BrexitID'].value_counts()
    positives_subgroup = x_series.get('a Remainer')
    instances_subgroup = x_series.sum()
    p_subgroup = positives_subgroup / instances_subgroup

    total_series = data[year]['BrexitID'].value_counts()
    positives_dataset = total_series.get('a Remainer')
    instances_dataset = total_series.sum()
    p_dataset = positives_dataset / instances_dataset

    return (instances_subgroup / instances_dataset) * (p_subgroup - p_dataset)
