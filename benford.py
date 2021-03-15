def benford_test(data_set):
    benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    total_count = 0
    data_count = [0]*9
    for i in data_set:
        data_count[i] += 1
        total_count += 1
    expected_counts = [round(p * total_count / 100) for p in benford]
    chi_square_stat = 0
    for data, expected in zip(data_count,expected_counts):
        diff = data - expected
        chi_square = diff * diff
        chi_square_stat += chi_square
    return chi_square_stat < 15.51 #Critical value at a P-value of 0.05 is 15.51