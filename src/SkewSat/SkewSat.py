import folium
import webbrowser
import math


class SkewSat():

    def __init__(self,rx_lat:float, rx_log:float,tx_lon:float) -> None:
        self._rx_log = rx_log # LOGITUDE DA ANTENA
        self._rx_lat = rx_lat # LATITUDE DA ANTENA
        self._tx_lon = tx_lon # LOGITUDE DO SATÉLITE
        self._tx_lat = 0      # LATITUDE DA SATÉLITE

        self._R0 = 6.371      # RAIO DA TERRA
        self._h_tx = 35.786   # ALTURA DO SATÉLITE

    
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
        if self._tx_log == 0 | self._tx_lon < -180 | self._tx_lon > 180:
            return -3

        # TODAS AS COORDENADAS ESTÃO CORRETAS
        return 1


    # DELTA = RX_LOGITUDE - TX_LOGITUDE
    def getDelta(self) -> float:
        return self._rx_log - self._tx_lon


    # CALCULAR AZIMUTE 
    def getAzimuth(self) -> float:
        az = 0
        
        delta = self._rx_log - self._tx_lon

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
        delta = self._rx_log - self._tx_lon

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

if __name__ == '__main__':

    rx_lat = -7.3758454
    rx_log = -40.9715357
    tx_log = -70

    sk = SkewSat( rx_lat, rx_log, tx_log )

    azimuth = sk.getAzimuth() # AZIMUTE VERDADEIRO
    elevation = sk.getElevation() # ELEVAÇÃO DE ANTENA
    elevation_offset = elevation - 20.5

    print( f'Azimute verdadeiro: {azimuth:.1f}°')
    print( f'Elevação: {elevation:.1f}°')
    print( f'Elevação (offset): {elevation_offset:.1f}°')