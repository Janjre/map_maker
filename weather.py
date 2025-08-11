import requests


def get_july_weather(lat, lon):
    # Pick July 2020 as example year
    start_date = "2020-07-01"
    end_date = "2020-07-31"

    url = (
        "https://archive-api.open-meteo.com/v1/era5"
        f"?latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_mean,precipitation_sum"
        "&timezone=UTC"
    )

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    temps = data.get("daily", {}).get("temperature_2m_mean", [])
    rains = data.get("daily", {}).get("precipitation_sum", [])

    if not temps or not rains:
        return None, None

    avg_temp = sum(temps) / len(temps)
    avg_rain = sum(rains) / len(rains)  # mm/day

    return avg_temp, avg_rain


if __name__ == "__main__":
    lat = input("Enter latitude: ").strip()
    lon = input("Enter longitude: ").strip()

    try:
        avg_temp, avg_rain = get_july_weather(lat, lon)
        if avg_temp is None:
            print("No July data available for this location.")
        else:
            print(f"Average July temperature (2020): {avg_temp:.2f}°C")
            print(f"Average July daily rainfall (2020): {avg_rain:.2f} mm/day")
    except Exception as e:
        print(f"Error: {e}")
