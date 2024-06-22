import json
import plotly.express as px

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def main():
    # Usage
    data = read_json_file('data/case_one.json')
    print(data)


if __name__ == "__main__":
    main()

    fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    fig.write_html('first_figure.html', auto_open=True)
