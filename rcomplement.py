from typing import List, Set, Tuple

DNA_CHARACTERS: Set[str] = {"A", "T", "C", "G", "N"}
RNA_CHARACTERS: Set[str] = {"A", "U", "C", "G", "N"}


def validate_dna(dna_sequence: str) -> None:
    """Check if a DNA sequence is valid

    Parameters
    ----------
    dna_sequence : str
        A sequence of characters to be validated
    
    Raises
    ------
    ValueError
        If the sequence contains invalid characters
    """
    if not all(nt in DNA_CHARACTERS for nt in dna_sequence):
        if all(nt in RNA_CHARACTERS for nt in dna_sequence):
            raise ValueError(
                "Input sequence is likely RNA. Please enter a DNA sequence"
            )
        else:
            raise ValueError(
                f"Input sequence contains invalid characters: {sorted(list(set(dna_sequence) - DNA_CHARACTERS))}"
            )


def get_dna_reverse_complement(dna_sequence: str) -> str:
    """Compute the reverse complement of a DNA sequence

    This function also validates the input sequence to make sure it is a valid DNA sequence.

    Parameters
    ----------
    dna_sequence : str
        Input DNA sequence.

    Returns
    -------
    str
        Reverse complement of the input DNA sequence.
    """
    dna_sequence = dna_sequence.upper().replace("\n", "").replace("\r", "").strip()
    validate_dna(dna_sequence)
    complement = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}
    return "".join(complement[base] for base in reversed(dna_sequence))


def process_fasta(fasta_input: str) -> List[Tuple[str, str]]:
    """Convert a fasta file in text format into series of reverse complement DNA sequences

    Parameters
    ----------
    fasta_input : str
        A string in fasta format

    Returns
    -------
    List[Tuple[str, str]]
        A fasta formatted txt can contain multiple sequences, requiring the need for a list; the tuple is a pair of sequence
        description and the reverse complement DNA sequence.
    """
    output: List[Tuple[str, str]] = []
    current_description: str = ""
    current_sequence_buffer: str = ""
    for line in fasta_input.splitlines():
        if line.startswith(">"):
            if current_description != "":
                output.append(
                    (
                        current_description,
                        get_dna_reverse_complement(current_sequence_buffer),
                    )
                )
                current_sequence_buffer = ""
            current_description = line[1:]
        else:
            current_sequence_buffer += line.strip().replace("\n", "")

    if current_description != "":
        output.append(
            (current_description, get_dna_reverse_complement(current_sequence_buffer))
        )
    return output

