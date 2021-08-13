import sys
import antigravity as ag

def get_geo_hash(lat, long, datedow):
    try:
        ag.geohash(float(lat), float(long), b'{datedow}')
    except Exception as err:
        print(err, file=sys.stderr)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Error. Wrong number of arguments. Usage example: python3 geohashing.py 55.78200894108994 49.125151809367615 2021-08-13-35499.85', file=sys.stderr)
        sys.exit(1)
    get_geo_hash(sys.argv[1], sys.argv[2], sys.argv[3])
