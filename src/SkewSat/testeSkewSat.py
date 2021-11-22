from SkewSat import SkewSat

# -7.0838699,-41.4668289,16.83z
rx_lat = -7.0838699 # Latitude do receptor (antena)
rx_log = -41.4668289 # Longitude do receptor (antena)
tx_log = -70 # Longitude do Transmissor  (satélite)

sk = SkewSat( rx_lat, rx_log, tx_log )
# print('Função checkValues: ', sk.checkValues())

azimuth = sk.getAzimuth() # AZIMUTE VERDADEIRO
elevation = sk.getElevation() # ELEVAÇÃO DE ANTENA
elevation_offset = sk.convertElevationToOffset(elevation)
skew_LNBF = sk.getSkewLNBF()
skew_LNBF_h = sk.skewLnbfDegreesToHours(skew_LNBF)

print( f'Satélite: {sk._tx_log}°')
print( f'Azimute verdadeiro: {azimuth:.1f}°')
print( f'Elevação: {elevation:.1f}°')
print( f'Elevação (offset): {elevation_offset:.1f}°')
print( f'Inclinação do LNBF: {skew_LNBF:.1f}°')
print( f'Inclinação do LNBF (h): ~ {skew_LNBF_h:.0f}h')

sk.open_map()