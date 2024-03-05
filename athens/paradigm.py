from dataclasses import dataclass

class NormalDistribution:
    mean: float
    stddev: float


class ConstantDistribution:
    value: int


class BernoulliDistribution:
    p: float

Distribution = ConstantDistribution | NormalDistribution

class DirectoryParadigm:
    contents: (str, Distribution)[1]

class AsciiFile:
    size: int

class BinaryFile:
    size: int

FileParadigm = AsciiFile | BinaryFile

Paradigm = FileParadigm | DirectoryParadigm

def parse_paradigms(data: dict[str, any]) -> dict[str, Paradigm]:
    for name in iter(data):
        paradigm_data = data[name]
        print(name, " ", type(paradigm_data))
        if type(paradigm_data) != dict:
            print("found setting ", name)
            continue
        if "type" not in data:
            print("type not found")
            exit(1)
        print(name, " ", data["type"])
    
    return {}