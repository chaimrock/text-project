import argparse
import json
from text_analyzer import TextAnalyzer
from text_preprocessor import TextPreprocessor
from sentence import Sentence
from person import Person

def readargs(args=None):
    parser = argparse.ArgumentParser(
        prog='Text Analyzer project',
    )
    # General arguments
    parser.add_argument('-t', '--task',
                        help="task number",
                        required=True
                        )
    parser.add_argument('-s', '--sentences',
                        help="Sentence file path",
                        )
    parser.add_argument('-n', '--names',
                        help="Names file path",
                        )
    parser.add_argument('-r', '--removewords',
                        help="Words to remove file path",
                        )
    parser.add_argument('-p', '--preprocessed',
                        action='append',
                        help="json with preprocessed data",
                        )
    # Task specific arguments
    parser.add_argument('--maxk',
                        type=int,
                        help="Max k",
                        )
    parser.add_argument('--fixed_length',
                        type=int,
                        help="fixed length to find",
                        )
    parser.add_argument('--windowsize',
                        type=int,
                        help="Window size",
                        )
    parser.add_argument('--pairs',
                        help="json file with list of pairs",
                        )
    parser.add_argument('--threshold',
                        type=int,
                        help="graph connection threshold",
                        )
    parser.add_argument('--maximal_distance',
                        type=int,
                        help="maximal distance between nodes in graph",
                        )

    parser.add_argument('--qsek_query_path',
                        help="json file with query path",
                        )
    return parser.parse_args(args)

def main():
    args = readargs()
    analyzer = TextAnalyzer()
    if args.task == '1':
        analyzer.load_data(sentences_path=args.sentences, names_path=args.names, remove_path=args.removewords)
        result = analyzer.analyze_task1()
        print(json.dumps(result, indent=4))
    elif args.task == '2':
        if args.preprocessed:
            analyzer.load_data(preprocessed_path=args.preprocessed[0])
        else:
            analyzer.load_data(sentences_path=args.sentences, names_path=args.names, remove_path=args.removewords)
        result = analyzer.analyze_task2(max_k=args.maxk)
        print(json.dumps(result, indent=4))
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
