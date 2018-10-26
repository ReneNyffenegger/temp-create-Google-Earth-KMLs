#
#  Currently used in:
#   o github / temp-Bibel-Voelkertafel
#
class Coord:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon



def start_folder(kml, name):
    kml.write('<Folder><name>{:s}</name><open>1</open>'.format(name))

def end_folder(kml):
    kml.write('</Folder>')

def pushpin(kml, name, coord, desc):
    kml.write('<Placemark><name>{:s}</name>'.format(name))

    if desc is not None:
       kml.write('<description>{:s}</description>'.format(desc))

    kml.write("""
<!--   <LookAt>
					<longitude>38.34803907965529</longitude>
					<latitude>33.2540199398231</latitude>
					<altitude>0</altitude>
					<heading>11.08435171895972</heading>
					<tilt>1.703726260245887</tilt>
					<range>4693076.838697146</range>
					<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
				</LookAt>-->
				<styleUrl>#m_ylw-pushpin</styleUrl>
				<Point>
					<gx:drawOrder>1</gx:drawOrder>
                                        <coordinates>{:f},{:f}</coordinates>
				</Point>
			</Placemark>""".format(coord.lon, coord.lat)
    )
