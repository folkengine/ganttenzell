import json
import plotly.express as px
import plotly.figure_factory as ff


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def main():
    # Usage
    data = read_json_file('data/case_one.json')
    print(data["chargingSchedulePeriod"])

    profiles = read_json_file('data/case_one_profiles.json')
    print(profiles)
    #
    # limits = []
    # start_period = []
    #
    # for period in data["chargingSchedulePeriod"]:
    #     limits.append(period["limit"])
    #     start_period.append(period["startPeriod"])
    #
    # fig = px.bar(x=start_period, y=limits)
    # fig.write_html('composite.html', auto_open=True)

    # Prepare data for Gantt chart
    gantt_data = []
    for period in data["chargingSchedulePeriod"]:
        task = {
            'Task': f'Charging period {period["startPeriod"]}',
            'Start': period["startPeriod"],
            'Finish': period["startPeriod"] + period["limit"],
            'Resource': 'Charging'
        }
        gantt_data.append(task)

    # Create Gantt chart
    fig = ff.create_gantt(gantt_data, index_col='Resource', show_colorbar=True, group_tasks=True)

    # Display Gantt chart
    fig.show()


if __name__ == "__main__":
    main()

    # fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    # fig.write_html('first_figure.html', auto_open=True)
