from SkewSat import SkewSat


rx_lat = -7.3758454
rx_log = -40.9715357
tx_log = -70

sk = SkewSat( rx_lat, rx_log, tx_log )
# print('Função checkValues: ', sk.checkValues())

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