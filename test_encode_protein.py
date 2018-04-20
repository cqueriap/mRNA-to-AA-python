from encode_protein import translate


def test_encoding(input, output):
    peptide = translate(input)
    if peptide == output:
        print('Test passed.')
        print('Peptide: ' + peptide)
    else:
        print('Test failed.')
        print('Incorrect Peptide: ' + peptide)

def run_test(file_name):
    f = open(file_name)
    rna = f.readline().rstrip('\n')
    pep = f.readline().rstrip('\n')
    test_encoding(rna, pep)
    f.close()


def run_tests():
    run_test('shortRNA.txt')
    print()
    run_test('longRNA.txt')


def main():
    run_tests()


if __name__ == "__main__":
    main()