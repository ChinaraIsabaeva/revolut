import unittest


from util import (
    merge_dict_with_duplicated_keys,
    create_list_of_nested_dict,
    create_final_dict,
    validate_keys_name
)


input_data = [
    {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
    },
    {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
    },
]

nested_dict = [
            {"EUR": {
                "FR": {
                    "Lyon": [
                        {
                            "amount": 11.4
                        }
                    ]
                }
            }},
            {"EUR": {
                "FR": {
                    "Paris": [
                        {
                            "amount": 20
                        }
                    ]
                }
            }}
        ]


final_result = {
    "EUR": {
        "FR": {
            "Lyon": [
                {
                    "amount": 11.4
                }
            ],
            "Paris": [
                {
                    "amount": 20
                }
            ]
        }
    }
}

leaf_names = ['currency', 'country', 'city']
wrong_leaf_names = ['currency', 'county', 'city']


class TestUtilMethods(unittest.TestCase):
    def test_merge(self):
        result = merge_dict_with_duplicated_keys(nested_dict)
        self.assertEqual(final_result, result)

    def test_create_nested_dict(self):
        result = create_list_of_nested_dict(input_data, leaf_names)
        for item in result:
            self.assertIn(item, nested_dict)

    def test_key_error(self):
        with self.assertRaises(ValueError) as exp:
            validate_keys_name(wrong_leaf_names, input_data[0])
            self.assertEquals(exp.msg, "Please provide valid keys")


if __name__ == '__main__':
    unittest.main()
