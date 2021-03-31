from math import log10

def benford_test(content, column_name='7_2009') -> tuple:
    """
    Takes the data and checks if the data
    satisy Benford's law by doing a Chi-Squared test
    """
    data_set = process_data(content, column_name)
    benford = [ 100*log10(1 + 1/n) for n in range(1, 10) ]
    total_count = 0
    data_count = [0]*9
    for i in data_set:
        data_count[i-1] += 1
        total_count += 1
    expected_counts = [round(p * total_count / 100) for p in benford]
    # Chi-Squared test
    chi_square_stat = 0
    for data, expected in zip(data_count,expected_counts):
        diff = data - expected
        chi_square = diff * diff
        chi_square_stat += chi_square / expected
    result = chi_square_stat < 15.51 #Critical value at a P-value of 0.05 is 15.51
    return result, data_count

def process_data(content, column_name) -> list:
    """
    Takes the content, looks for the given column name and collects the
    first digit of the data into a list and returns the list
    """
    if column_name in [x for x in content[0].split('\t')]:
        sep = '\t'
    elif column_name in [x for x in content[0].split(',')]:
        sep = ','
    
    for idx,i in enumerate(content[0].split(sep)):
        if column_name == i:
            break
    data_set = []
    for line in content[1:]:
        if line == '': #if the last line is empty
            continue
        val = line.split(sep)[idx]
        val = val[0] # Taking the first digit of the value
        data_set.append(int(val))
    return data_set