from fsbkup import Fsbkup
from pathlib import Path


def main():
    f = Fsbkup.from_file("sample_backup/all_namespaces/kind_debug/output-0")
    print(f"{len(f.documents)} documents found")
    script_dir = Path(__file__).parent
    output_dir = script_dir / "documents"
    output_dir.mkdir(exist_ok=True)
    for i, doc in enumerate(f.documents):
        with open(output_dir / f"doc_{i}.bin", 'wb') as of:
            of.write(doc.data)


if __name__ == "__main__":
    main()
