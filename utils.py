from datetime import datetime
import requests


def get_next_trains(schedule, count=3):
    now = datetime.now()
    current_minutes = now.hour * 60 + now.minute

    result = []
    for time_str in schedule:
        hours, minutes = map(int, time_str.split(":"))
        train_minutes = hours * 60 + minutes

        if train_minutes > current_minutes:
            result.append(time_str)
            if len(result) >= count:
                return result

    return result


def get_travel_time(api_key, user_lat, user_lon, station_lat, station_lon):
    url = "https://api.openrouteservice.org/v2/directions/foot-walking"
    params = {
        "api_key": api_key,
        "start": f"{user_lon},{user_lat}",
        "end": f"{station_lon},{station_lat}"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        duration_seconds = data["features"][0]["properties"]["segments"][0]["duration"]
        duration_minutes = duration_seconds // 60
        return duration_minutes

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Ошибка в структуре ответа API: {e}")
        return None


def when_to_go_out(schedule, trv_time):
    now = datetime.now()
    current_time = now.hour * 60 + now.minute

    trains = get_next_trains(schedule, 14)

    if not trains:
        return None, None

    for time_str in trains:
        hours, minutes = map(int, time_str.split(":"))
        train_minutes = hours * 60 + minutes

        exit_time_in_minutes = train_minutes - trv_time - 5

        if exit_time_in_minutes > current_time:
            h, m = divmod(int(exit_time_in_minutes), 60)
            return f"{h:02d}:{m:02d}", time_str

    return None, None






