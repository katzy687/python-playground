def get_contiguous_combos(string):
    results = []
    for i in range(len(string)):
        results.append(string[i])
        result = [string[i]]
        for j in range(i + 1, len(string)):
            result.append(string[j])
            results.append("".join(result))
    return results


print(get_contiguous_combos("lol"))
