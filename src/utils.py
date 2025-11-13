from enum import Enum

data_type_labels = {
    "OCCUPANCY_DATE": "Date",
    "SERVICE_USER_COUNT": "Service User Count",
    "OCCUPIED_BEDS": "Occupied Beds",
    "UNOCCUPIED_BEDS": "Unoccupied Beds",
    "OCCUPIED_ROOMS": "Occupied Rooms",
    "UNOCCUPIED_ROOMS": "Unoccupied Rooms",
    "PROGRAM_ID": "Programs",
    "ORGANIZATION_ID": "Organizations",
    "LOCATION_ID": "Locations",
    "SHELTER_ID": "Shelters"
}


class TimeInterval(Enum):
    DAILY = 1
    MONTHLY = 2
    YEARLY = 3

date_intervals = {
    "Daily": TimeInterval.DAILY,
    "Monthly": TimeInterval.MONTHLY,
    "Yearly": TimeInterval.YEARLY
}