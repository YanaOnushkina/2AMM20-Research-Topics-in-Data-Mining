import pandas as pd


def stable_recalculate(subgroups_years):
    results = []
    for index, year in enumerate(subgroups_years):
        results.append({"year": index, "results": calculate_year(year, subgroups_years)})
    print(results)


def calculate_year(year, subgroup_years):
    results = []
    for index, row in year.iterrows():
        if index == 10:
            print("\n")
            break
        name, qualities = calculate_subgroup(row, subgroup_years)
        penalty = penalty_factor(qualities)
        new_quality = row['quality'] * penalty
        results.append({"subgroup": name, "penalty": penalty, "old quality": row['quality'], "new_quality": new_quality})
    print(results)
    return results


def calculate_subgroup(subgroup, subgroup_years):
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
            combined_qualities.append(0.02)
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
    similarity = 1 - (abs(i - j) / max(i, j))
    return similarity
