import pytest
from rcomplement import get_dna_reverse_complement, process_fasta, validate_dna


@pytest.mark.parametrize(
    "input, expected",
    [("ATCG", "CGAT"), ("ATCGATCG", "CGATCGAT"), ("ATCGATCGATCG", "CGATCGATCGAT")],
)
def test_reverse_complement(input: str, expected: str) -> None:
    assert get_dna_reverse_complement(input) == expected, (input, expected)


@pytest.mark.parametrize(
    "dna_sequence, expected",
    [("ATCG", "ok"), ("AkkasdfaowqelabdsZ", "invalid"), ("AUUGC", "RNA")],
)
def test_validate_dna(dna_sequence: str, expected: str):
    if expected == "ok":
        # this should raise no value error
        validate_dna(dna_sequence)
    elif expected == "invalid":
        with pytest.raises(ValueError):
            validate_dna(dna_sequence)
    elif expected == "RNA":
        with pytest.raises(ValueError):
            validate_dna(dna_sequence)
    else:
        raise AssertionError(f"Invalid test case: {dna_sequence}, {expected}")


def test_process_fasta():
    expected = [
        (
            "sequence A",
            "GACAACGCTTCAAAGAAGATGGCTCTAATATAGCCTAAAAGTGTTTTTTCTGGCAACAGAATATGAATATAATTTTAATTATATCACAATATTGGGGGTGTTTGTACTAGAGGACTTACC",
        ),
        (
            "sequence B",
            "CAGTCGTCGATCGATGCATAGACAACGCTTCAAAGAAGATGGCTCTAATATAGCCTAAAAGTGTAAAATCTGGCAACAGAATATGAATATAATTTTAATTATATCACAATATTGGGGGTGTTTGTACTAGAGCACTTACC",
        ),
    ]
    with open(
        "./test_fixtures/example_fasta.txt", "r"
    ) as f:
        output = process_fasta(f.read())
        for i, j in zip(output, expected):
            assert i[0] == j[0]
            assert i[1] == j[1]
