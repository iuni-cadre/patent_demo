import pandas as pd
from wordcloud import WordCloud

import matplotlib.pyplot as plt
import sys

def create_word_cloud(input_files, input_dir, output_dir):
    patents = pd.read_csv(input_dir + '/' + input_files[0])
    text = patents.Patent_title.str.cat(sep=', ')
    wc = WordCloud().generate(text)
    plt.figure(figsize=[15,7.5])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
 
    plot_output_png = output_dir + '/' + 'coffee.png'
    wc.to_file(plot_output_png)
    print('Plot generated at ' + plot_output_png)


if __name__ == "__main__":
    # Required cadre boilerplate to get commandline arguments:
    try:
        _input_filenames = sys.argv[1].split(',')
        _input_dir = sys.argv[2]
        _output_dir = sys.argv[3]
    except IndexError:
        print("Missing Parameter")
        sys.exit(1)
    except Exception as error:
        print(error)
        print("Unknown Error")
        sys.exit(1)

    #  calling create_plot function
    create_word_cloud(_input_filenames, _input_dir, _output_dir)
