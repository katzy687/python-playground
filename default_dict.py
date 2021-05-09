from collections import defaultdict

def get_attr_alias(attr_name):
    # get the attr_name back if an alias is not defined
    aliases = defaultdict(lambda: attr_name)
    aliases["ResourceModelName"] = "Model"
    aliases["FullAddress"] = "IP Address"

    return aliases[attr_name]

alias = get_attr_alias("ok")
print(alias)