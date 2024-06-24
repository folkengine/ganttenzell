class ProcessedData:
    def __init__(self, composite_schedule, profiles):
        self.profiles = profiles
        self.chargingRateUnit = composite_schedule['chargingRateUnit']
        self.chargingSchedulePeriod = composite_schedule['chargingSchedulePeriod']
        self.duration = composite_schedule['duration']
        self.evseId = composite_schedule['evseId']
        self.scheduleStart = composite_schedule['scheduleStart']

    def process_composite_schedule_as_ganntt(self):
        gantt_data = []
        for period in self.chargingSchedulePeriod:
            task = {
                'Task': f'Charging period {period["startPeriod"]}',
                'Start': period["startPeriod"],
                'Finish': period["startPeriod"] + period["limit"],
                'Resource': 'Charging'
            }
            gantt_data.append(task)
        return gantt_data
