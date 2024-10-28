import numpy.testing as npt
from pathlib import Path
from inflammation.compute_data import compute_standard_deviation_by_day
import math


def test_compute_standard_deviation_one_patient():
    patient_one = [0.0, 1.0, 0.0]
    file_1 = [patient_one]
    all_files = [file_1]
    standard_deviation_by_day = compute_standard_deviation_by_day(all_files)
    npt.assert_almost_equal(standard_deviation_by_day, [0, 0, 0.])


def test_compute_standard_deviation_two_patients_in_same_file():
    patient_one = [0.0, 1.0, 0.0]
    patient_two = [0.0, 2.0, 0.0]
    file_1 = [patient_one]
    file_2 = [patient_two]
    all_files = [file_1, file_2]
    standard_deviation_by_day = compute_standard_deviation_by_day(all_files)
    npt.assert_almost_equal(standard_deviation_by_day, [0, math.sqrt(0.25), 0.])


def test_analyse_data():
    from inflammation.compute_data import analyse_data
    path = Path.cwd() / "data"
    result = analyse_data(path)

    assert 'standard deviation by day' in result
    array_result = result['standard deviation by day']

    expected_output = [0.,0.22510286,0.18157299,0.1264423,0.9495481,0.27118211,
                       0.25104719,0.22330897,0.89680503,0.21573875,1.24235548,0.63042094,
                       1.57511696,2.18850242,0.3729574,0.69395538,2.52365162,0.3179312,
                       1.22850657,1.63149639,2.45861227,1.55556052,2.8214853,0.92117578,
                       0.76176979,2.18346188,0.55368435,1.78441632,0.26549221,1.43938417,
                       0.78959769,0.64913879,1.16078544,0.42417995,0.36019114,0.80801707,
                       0.50323031,0.47574665,0.45197398,0.22070227]
    npt.assert_array_almost_equal(array_result, expected_output)