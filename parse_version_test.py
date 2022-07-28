from packaging.version import parse as parse_version

result = parse_version("2020.1.1") > parse_version("2020.1.1")
print(result)

result = parse_version("2020.1.0") > parse_version("2020.1.1")
print(result)