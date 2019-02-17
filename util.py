import dpath


def create_list_of_nested_dict(input_data, leaf_names):
    leaf_names = leaf_names
    result = []
    for item in input_data:
        unused_keys = list(set(item.keys()) - set(leaf_names))
        item_nested_dict = []
        for key in unused_keys:
            item_nested_dict.append({key: item.get(key)})
        for name in reversed(leaf_names):
            key = item.get(name)
            item_nested_dict = {key: item_nested_dict}
        result.append(item_nested_dict)

    return result


def merge_dict_with_duplicated_keys(input_list):
    final_dict = {}
    for item in input_list:
        for key, value in item.items():
            if key in final_dict:
                final_dict_item = {key: final_dict.get(key)}
                dpath.util.merge(final_dict_item, item)
                final_dict.update(final_dict_item)
            else:
                final_dict.update(item)
    return final_dict


def create_final_dict(input_data, leaf_names):
    input_list = create_list_of_nested_dict(input_data, leaf_names)
    final_dict = merge_dict_with_duplicated_keys(input_list)
    return final_dict