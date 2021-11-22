import folium
import webbrowser
import math

satellites = {

    '1w': {
        'name': '1 °W - Intelsat 1002',
        'date_of_release': '2006-06-16'
    },

    '3w': {
        'name': '3W - ABS 3A',
        'date_of_release': '2006-06-16'
    },

    '8w': {
        'name': '8 °W - Eutelsat 8 West B',
        'date_of_release': '2006-06-16'
    },

    '11w': {
        'name': '11 °W - Express AM44',
        'date_of_release': '2006-06-16'
    },

    '14w': {
        'name': '14 °W - Express AM8',
        'date_of_release': '2006-06-16'
    },

    '15w': {
        'name': '15 °W - Telstar 12 Vantage',
        'date_of_release': '2006-06-16'
    },

    '18w': {
        'name': '18 °W - Intelsat 37e',
        'date_of_release': '2006-06-16'
    },

    '22w': {
        'name': '22 °W - SES 4',
        'date_of_release': '2006-06-16'
    },

    '24.5w': {
        'name': '24.5 °W - Intelsat 905',
        'date_of_release': '2006-06-16'
    },

    '27.5w': {
        'name': '27.5 °W - INTELSAT 901',
        'date_of_release': '2006-06-16'
    },

    '30w': {
        'name': '30 °W - Hispasat 30W-6',
        'date_of_release': '2006-06-16'
    },

    '31.5w': {
        'name': '31.5 °W - Intelsat 25',
        'date_of_release': '2006-06-16'
    },

    '34.5w': {
        'name': '34.5 °W - Intelsat 35e',
        'date_of_release': '2006-06-16'
    },

    '36w': {
        'name': '36 °W - Hispasat 36W-1',
        'date_of_release': '2006-06-16'
    },

    '37.5w': {
        'name': '37.5 °W - StarOne C12 (NSS 10)',
        'date_of_release': '2006-06-16'
    },

    '40.5w': {
        'name': '40.5 °W - SES 6',
        'date_of_release': '2006-06-16'
    },

    '43w': {
        'name': '43 °W - Intelsat 11',
        'date_of_release': '2006-06-16'
    },

    '45w': {
        'name': '45 °W - Intelsat 14',
        'date_of_release': '2006-06-16'
    },

    '47.5w': {
        'name': '47.5 °W - SES 14',
        'date_of_release': '2006-06-16'
    },

    '53w': {
        'name': '53 °W - Intelsat 23',
        'date_of_release': '2006-06-16'
    },

    '55.5w': {
        'name': '55.5 °W - Intelsat 34',
        'date_of_release': '2006-06-16'
    },

    '61w': {
        'name': '61 °W - Amazonas',
        'date_of_release': '2006-06-16'
    },

    '63w': {
        'name': '63 °W - Telstar 19V',
        'date_of_release': '2006-06-16'
    },

    '65w': {
        'name': '65 °W - StarOne C2',
        'date_of_release': '2006-06-16'
    },

    '65.1w': {
        'name': '65.1 °W - Eutelsat 65 West A',
        'date_of_release': '2006-06-16'
    },

    '67w': {
        'name': '67 °W - SES 10',
        'date_of_release': '2006-06-16'
    },

    '70w': {
        'name': '70 °W - StarOne D2/C4',
        'date_of_release': '2006-06-16'
    },

    '71.8w': {
        'name': '71.8 °W - ARSAT-1',
        'date_of_release': '2006-06-16'
    },

    '74w': {
        'name': '74 °W - Hispasat 74W 1',
        'date_of_release': '2006-06-16'
    },

    '75w': {
        'name': '75 °W - StarOne C3',
        'date_of_release': '2006-06-16'
    },

    '81w': {
        'name': '81 °W - ARSAT-2',
        'date_of_release': '2006-06-16'
    },

    '84w': {
        'name': '84 °W - StarOne D1',
        'date_of_release': '2006-06-16'
    },

    '87.2w': {
        'name': '87.2 °W - Tupac Katari',
        'date_of_release': '2006-06-16'
    },

    '89w': {
        'name': '89 °W - Galaxy 28',
        'date_of_release': '2006-06-16'
    },

    '92w': {
        'name': '92 °W - StarOne C1',
        'date_of_release': '2006-06-16'
    },

    '95w': {
        'name': '95 °W - Galaxy 3C',
        'date_of_release': '2006-06-16'
    },

    '97w': {
        'name': '97 °W - Galaxy 19',
        'date_of_release': '2006-06-16'
    },

    '107.3w': {
        'name': '107.3 °W - Anik G1',
        'date_of_release': '2006-06-16'
    },

    '113w': {
        'name': '113 °W - Eutelsat 113 West A',
        'date_of_release': '2006-06-16'
    },

    '114.9w': {
        'name': '97 °W - Galaxy 19',
        'date_of_release': '2006-06-16'
    },

    '117w': {
        'name': '117 °W - Eutelsat 117 West A',
        'date_of_release': '2006-06-16'
    }
}


class SkewSat:

    def __init__(self,rx_lat:float, rx_log:float,tx_log:float) -> None:
        self._rx_log = rx_log # LOGITUDE DA ANTENA
        self._rx_lat = rx_lat # LATITUDE DA ANTENA
        self._tx_log = tx_log # LOGITUDE DO SATÉLITE
        self._tx_lat = 0      # LATITUDE DA SATÉLITE

        self._R0 = 6.371      # RAIO DA TERRA
        self._h_tx = 35.786   # ALTURA DO SATÉLITE
        self.map = folium.Map(location=[rx_lat, rx_log], zoom_start=15)

    
    def checkValues(self) -> int:
        # Insira a longitude do receptor
        # (formato decimal, positivo = leste, negativo = oeste,
        # valores inválidos entre -180 e 180 graus).
        if self._rx_log == 0.0 or self._rx_log < -180.0 or self._rx_log > 180.0:
            return -1

        # Insira a latitude do receptor
        # em (formato decimal, positivo = nor, negativo = sul,
        # valores inválidos entre -90
        if self._rx_lat == 0.0 or self._rx_lat < -90 or self._rx_lat > 180:
            return -2

        # Insira a longitude do satélite
        # no (formato decimal, positivo = leste, negativo = oeste,
        # valores inválidos entre -180 e 180 graus).
        if self._tx_log == 0 or self._tx_log < -180 or self._tx_log > 180:
            return -3

        result = -1
        if self._tx_log > 0:
            sat = str(self._tx_log)
            sat = sat.replace('+', '')
            sat = sat + 'o'
        else:
            sat = str(self._tx_log)
            sat = sat.replace('-', '')
            sat = sat + 'w'

        if not(sat in satellites):
            return -4

        # TODAS AS COORDENADAS ESTÃO CORRETAS
        return 1


    # DELTA = RX_LOGITUDE - TX_LOGITUDE
    def getDelta(self) -> float:
        return self._rx_log - self._tx_log


    # CALCULAR AZIMUTE 
    def getAzimuth(self) -> float:
        az = 0
        result = self.checkValues()
        if result:
            delta = self._rx_log - self._tx_log

            az = math.atan(
               (
                   math.tan( (math.pi / 180) * delta ) /
                   math.sin( (math.pi / 180) * self._rx_lat )
               )
            ) * (180/math.pi) +180


            if self._rx_lat < 0: az -= 180

            if az < 0: az += 360

        return az

    def getElevation(self) -> float:
        el = 0
        result = self.checkValues()
        if result:
            delta = self._rx_log - self._tx_log

            num = (
                math.cos(self._rx_lat*(math.pi/180)) *
                math.cos(delta*(math.pi/180)) -
                self._R0 / ( self._R0 + self._h_tx)
            )

            den = (
                math.sqrt(
                    1 - math.pow(
                            math.cos( self._rx_lat * (math.pi/180) ) *
                            math.cos( delta * (math.pi/180) )
                        , 2 )
                )
            )

            el = (180/math.pi) * math.atan(num/den)

        return el

    def convertElevationToOffset(self, elevation):
        return elevation - 20.5

    def getSkewLNBF(self) -> float:
        skew = 0
        result = self.checkValues()
        if result:
            # 57.295779513082 equivale 1 radiano em graus
            delta = (self._tx_log - self._rx_log) / 57.29578

            skew = -57.29578 * math.atan( (math.sin(delta)) / math.tan(self._rx_lat/57.29578) )

            if skew < 0: skew + 90
            else: skew - 90

        return skew

    def skewLnbfDegreesToHours(self, skew:float = 0 ) -> float:
        skew_h = 0
        if skew:
            skew_h = (skew * 2) / 60 # CONVERTATENDO GRAUS PARA MNUTOS E depois para horas

            if skew < 0: skew_h = abs(skew_h) + 6 # POSITIVO, ENTÃO É + 6 (DIREITA)
            else: skew = abs(skew_h) - 6 # NEGATIVO, ENTÃO É + 6 (ESQUERDA)

        return skew_h

    def to_point(self, msg='', msg_preview='Mais detalhes!', clr='blue', zoom_start=15) -> bool:
        tp = False
        azimuth = self.getAzimuth()  # AZIMUTE VERDADEIRO
        elevation = self.getElevation()  # ELEVAÇÃO DE ANTENA
        elevation_offset = elevation - 20.5
        skew_LNBF = self.getSkewLNBF()
        skew_LNBF_h = self.skewLnbfDegreesToHours(skew_LNBF)

        if azimuth != 0 and elevation != 0 and skew_LNBF != 0:
            tp = True
            msg = f'''
                <h2>Dados para apontamento</h2>
                <b>RX latitude:</b> {self._rx_lat} | <b>RX longitude:</b> {self._rx_log} <br>
                <b>Satelite:</b> </b>{self._tx_log}<br>
                <b>Azimuth Verdadeiro:</b> </b>{azimuth:.1f}º<br>
                <b>Elevação:</b> {elevation:.1f}º | <b>Elevação Offset:</b> {elevation_offset:.1f}º <br>
                <b>Inclinação do LNBF:</b> {skew_LNBF:.1f}° | <b>Inclinação do LNBF (h):</b> ~ {skew_LNBF_h:.0f}h
            '''

            iframe = folium.IFrame(msg)
            popup = folium.Popup(
                iframe,
                min_width=420,
                max_width=500
            )

            folium.Marker(
                [self._rx_lat, self._rx_log],
                zoom_start=zoom_start,
                popup=popup,
                tooltip=msg_preview,
                icon=folium.Icon(color=clr)
            ).add_to(self.map)
        return tp

    def set_row_for_satellite(self, color='red'):
        result = self.checkValues()
        if result:
            points_rx = [self._rx_lat, self._rx_log]
            points_tx = [self._tx_lat, self._tx_log]

            points = [points_rx, points_tx]

            folium.PolyLine(points, color=color).add_to(self.map)
        return result == 1

    def open_map(self, path='SkewSatMap.html'):
        resul = self.checkValues()
        if resul:
            self.to_point()
            self.set_row_for_satellite()
            html_page = f'{path}'
            self.map.add_child(folium.LatLngPopup())
            self.map.save(html_page)
            # open in browser.
            new = 2
            webbrowser.open(html_page, new=new)
        return resul == 1
