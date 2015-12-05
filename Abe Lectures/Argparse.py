
import argparse

parser = argparse.ArgumentParser(description="Tests a twitter classifier")

parser.add_argument("classifier", help="classifier module")

parser.add_argument("-c", "--config",
                    help="path to config file",
                    default="config.yaml")

parser.add_argument('-t', '--test', action='store_true', help='run tests', default=False)


def main(classifier, config="config.yaml", test=False):

    print(args.classifier)  # look at what was passed in as the classifier

    print(args.config)  # look at what was passed in as the config

    if test:
        import doctest
        doctest.testmod()
    else:
        with open(config) as f:
            config_data = yaml.load(f)
        dictConfig(config_data['logging'])
        #  more code logic here blah blah blah

if __name__ == "__main__":  # if you're running this file as script
    args = parser.parse_args()
    main(classifier=args.classifier, config=args.config, test=args.test)
