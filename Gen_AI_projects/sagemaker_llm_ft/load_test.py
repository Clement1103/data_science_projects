import json
import tarfile

input_data = [
    {'inputs':'How I Met Your Mother has been awarded as best sitcom.'},
    {'inputs':'7T MRI allowed researchers to visualize tumors with high precision.'},
    {'inputs':'The BTC value collapses.'},
    {'inputs':'Q-bits might be the future of computer calculus.'}
]

def create_json_files(input_data):
    for i, d in enumerate(input_data):
        with open(f'input{i+1}.json', 'w') as f:
            json.dump(d, f, indent=4)

def create_tar_file(input_files, output_filename = 'input.tar.gz'):
    with tarfile.open(output_filename, 'w:gz') as tar:
        for file in input_files:
            tar.add(file)

def main():
    create_json_files(input_data)
    input_files = [f'input{i+1}.json' for i in range(len(input_data))]
    create_tar_file(input_files)


if __name__ == '__main__':
    main()