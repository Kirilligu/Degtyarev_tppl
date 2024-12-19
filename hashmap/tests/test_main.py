import pytest
from main import Dict

class TestDict:
    def test_iloc_invalid_key(self):
        dict = Dict()
        dict["value1"] = 1
        with pytest.raises(KeyError):
            dict.iloc["hello"]
    def test_ploc_invalid_index(self):
        dict = Dict()
        dict["value1"] = 1
        with pytest.raises(KeyError):
            dict.ploc[1]
    def test_ploc_invalid_key_length(self):
        dict = Dict()
        dict["value1"] = 1
        with pytest.raises(KeyError):
            dict.ploc["="]
    def test_valid_ploc_condition(self):
        dict = Dict()
        dict["value1"] = 1
        dict["value2"] = 2
        dict["value3"] = 3
        dict["1"] = 10
        dict["2"] = 20
        dict["3"] = 30
        dict["(1, 5)"] = 100
        dict["(5, 5)"] = 200
        dict["(10, 5)"] = 300
        dict["(1, 5, 3)"] = 400
        dict["(5, 5, 4)"] = 500
        dict["(10, 5, 5)"] = 600
        assert dict.ploc[">=1"] == {"1": 10, "2": 20, "3": 30}
        assert dict.ploc["<3"] == {"1": 10, "2": 20}
        assert dict.ploc[">0, >0"] == {"(1, 5)": 100, "(5, 5)": 200, "(10, 5)": 300}
        assert dict.ploc["<5, >=5, >=3"] == {"(1, 5, 3)": 400}
        assert dict.ploc["<>2"] == {"1": 10, "3": 30}
        assert dict.ploc["=2"] == {"2": 20}
        assert dict.ploc["<=2"] == {"1": 10, "2": 20}
    def test_iloc_out_of_range_index(self):
        dict = Dict()
        dict["value1"] = 1
        dict["value2"] = 2
        dict["value3"] = 3
        dict["1"] = 10
        dict["2"] = 20
        dict["3"] = 30
        dict["1, 5"] = 100
        dict["5, 5"] = 200
        dict["10, 5"] = 300
        with pytest.raises(IndexError):
            dict.iloc[10]

    def test_valid_iloc_indexing(self):
        dict = Dict()
        dict["value1"] = 1
        dict["value2"] = 2
        dict["value3"] = 3
        dict["1"] = 10
        dict["2"] = 20
        dict["3"] = 30
        dict["1, 5"] = 100
        dict["5, 5"] = 200
        dict["10, 5"] = 300
        assert dict.iloc[0] == 10
        assert dict.iloc[2] == 300
        assert dict.iloc[5] == 200
        assert dict.iloc[8] == 3
    def test_ploc_invalid_number_in_key(self):
        dict = Dict()
        dict["value1"] = 1
        with pytest.raises(KeyError):
            dict.ploc[">0..1"]
        with pytest.raises(KeyError):
            dict.ploc[">5, <0..4"]
        with pytest.raises(KeyError):
            dict.ploc[">5, <0..4, ="]
    def test_ploc_invalid_sign_in_key(self):
        dict = Dict()
        dict["value1"] = 1
        with pytest.raises(KeyError):
            dict.ploc[">>"]
        with pytest.raises(KeyError):
            dict.ploc["<<"]
