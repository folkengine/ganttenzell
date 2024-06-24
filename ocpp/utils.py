import json


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def process_composite_schedule_as_ganntt(data):
    gantt_data = []
    for period in data["chargingSchedulePeriod"]:
        task = {
            'Task': f'Charging period {period["startPeriod"]}',
            'Start': period["startPeriod"],
            'Finish': period["startPeriod"] + period["limit"],
            'Resource': 'Charging'
        }
        gantt_data.append(task)

    return gantt_data
