import json
import plotly.express as px
import plotly.figure_factory as ff

import ocpp.utils
import ocpp.smart_charging


def main():
    # Usage
    data = ocpp.utils.read_json_file('data/case_one.json')

    print(data["chargingSchedulePeriod"])

    profiles = ocpp.utils.read_json_file('data/case_one_profiles.json')
    print(profiles)

    # Create a ProcessedData object
    processed_data = ocpp.smart_charging.ProcessedData(data, profiles)

    # Prepare data for Gantt chart
    gantt_data = processed_data.process_composite_schedule_as_ganntt()

    # Create Gantt chart
    fig = ff.create_gantt(gantt_data, index_col='Resource', show_colorbar=True, group_tasks=True)

    # Display Gantt chart
    fig.show()


if __name__ == "__main__":
    main()

    # fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    # fig.write_html('first_figure.html', auto_open=True)
