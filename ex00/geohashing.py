import sys
import antigravity


def display_geohash(latitude, longitude, date):
    antigravity.geohash(latitude, longitude, date.encode())


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 ex00.py <latitude> <longitude> <date>")
        exit()

    try:
        user_latitude = float(sys.argv[1])
        user_longitude = float(sys.argv[2])
        date = sys.argv[3]
    except ValueError:
        print("Latitude and longitude must be numbers")
        exit()

    try:
        display_geohash(user_latitude, user_longitude, date)
    except:
        print("An error occurred")
        exit()
