import folium
import webbrowser
import math


class SkewSat():

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
        if self._rx_log == 0 | self._rx_log < -180 | self._rx_log > 180:
            return -1

        # Insira a latitude do receptor
        # em (formato decimal, positivo = nor, negativo = sul,
        # valores inválidos entre -90
        if self._rx_lat == 0 | self._rx_lat < -90 | self._rx_lat > 180:
            return -2 

        # Insira a longitude do satélite
        # no (formato decimal, positivo = leste, negativo = oeste,
        # valores inválidos entre -180 e 180 graus).
        if self._tx_log == 0 | self._tx_log < -180 | self._tx_log > 180:
            return -3

        # TODAS AS COORDENADAS ESTÃO CORRETAS
        return 1


    # DELTA = RX_LOGITUDE - TX_LOGITUDE
    def getDelta(self) -> float:
        return self._rx_log - self._tx_log


    # CALCULAR AZIMUTE 
    def getAzimuth(self) -> float:
        az = 0
        
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
        delta = self._rx_log - self._tx_log

        num = (
            math.cos(rx_lat*(math.pi/180)) *
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

    def getSkewLNBF(self) -> float:
        skew = 0
        # 57.295779513082 equivale 1 radiano em graus 
        delta = (self._tx_log - self._rx_log) / 57.29578

        skew = -57.29578 * math.atan( (math.sin(delta)) / math.tan(self._rx_lat/57.29578) )

        if skew < 0: skew + 90
        else: skew - 90

        return skew

    def skewLnbfDegreesToHours(self, skew:float = 0 ) -> float:
        skew_h = (skew * 2) / 60 # CONVERTATENDO GRAUS PARA MNUTOS E depois para horas

        if skew < 0: skew_h = abs(skew_h) + 6 # POSITIVO, ENTÃO É + 6 (DIREITA)
        else: skew = abs(skew_h) - 6 # NEGATIVO, ENTÃO É + 6 (ESQUERDA)

        return skew_h

    def to_point(self, msg='', msg_preview='Mais detalhes!', clr='red', zoom_start=15):
        azimuth = self.getAzimuth()  # AZIMUTE VERDADEIRO
        elevation = self.getElevation()  # ELEVAÇÃO DE ANTENA
        elevation_offset = elevation - 20.5
        skew_LNBF = self.getSkewLNBF()
        skew_LNBF_h = self.skewLnbfDegreesToHours(skew_LNBF)

        msg = f'''RX latitude: {self._rx_lat}\nRX longitude: {self._rx_log}\nSatelite: {self._tx_log}
            Elevação: {elevation:.1f}º\nElevação Offset: {elevation_offset:.1f}º\nAzimuth Verdadeiro: {azimuth:.1f}º
            Inclinação do LNBF: {skew_LNBF:.1f}°'
            Inclinação do LNBF (h): ~ {skew_LNBF_h:.0f}h'
            '''

        msg = f'''
            <h2>Dados para apontamento</h2>
            <b>RX latitude:</b> {self._rx_lat} | <b>RX longitude:</b> {self._rx_log} <br>
            <b>Satelite:</b> {self._tx_log}  <br>
            <b>Elevação:</b> {elevation:.1f}º | <b>Elevação Offset:</b> {elevation_offset:.1f}º <br>
            <b>Inclinação do LNBF:</b> {skew_LNBF:.1f}° | <b>Inclinação do LNBF (h):</b> ~ {skew_LNBF_h:.0f}h
        '''

        iframe = folium.IFrame(msg)
        popup = folium.Popup(
            iframe,
            min_width=400,
            max_width=500
        )


        folium.Marker(
            [self._rx_lat, self._rx_log],
            popup = popup
        ).add_to(self.map)

        # folium.Marker(
        #     [self._rx_lat, self._rx_log],
        #     zoom_start = zoom_start,
        #     popup = f'<i>{msg}</i>',
        #     min_width=500,
        #     max_width=500,
        #     tooltip = msg_preview,
        #     icon = folium.Icon( color = clr)
        # ).add_to(self.map)

    def set_row_for_satellite(self, color='red'):

        points_rx = [self._rx_lat, self._rx_log]
        points_tx = [self._tx_lat, self._tx_log]

        points = [points_rx, points_tx]

        folium.PolyLine(points, color=color).add_to(self.map)

    def open_map(self, path='SkewSatMap.html'):
        html_page = f'{path}'
        self.map.add_child(folium.LatLngPopup())
        self.map.save(html_page)
        # open in browser.
        new = 2
        webbrowser.open(html_page, new=new)


if __name__ == '__main__':

    rx_lat = -7.3758454
    rx_log = -40.9715357
    tx_log = -70

    sk = SkewSat( rx_lat, rx_log, tx_log )

    azimuth = sk.getAzimuth() # AZIMUTE VERDADEIRO
    elevation = sk.getElevation() # ELEVAÇÃO DE ANTENA
    elevation_offset = elevation - 20.5
    skew_LNBF = sk.getSkewLNBF()
    skew_LNBF_h = sk.skewLnbfDegreesToHours(skew_LNBF)

    print( f'Satélite: {sk._tx_log}°')
    print( f'Azimute verdadeiro: {azimuth:.1f}°')
    print( f'Elevação: {elevation:.1f}°')
    print( f'Elevação (offset): {elevation_offset:.1f}°')
    print( f'Inclinação do LNBF: {skew_LNBF:.1f}°')
    print( f'Inclinação do LNBF (h): ~ {skew_LNBF_h:.0f}h')

    sk.to_point()
    sk.set_row_for_satellite()
    sk.open_map()