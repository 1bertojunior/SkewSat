SkewSat
===========

### Pacote em Python para consultas de cálculos para apontamentos de parabólicas. Satellite Finder | SatFinder | Transponder satelite | is a tool which will help you to set up satellite dish. It will give you azimuth, elevation and LNB tilt for your location (based on GPS)

## Instalação
    pip install SkewSat

## Exemplo de Uso
#### Importando pacote
    from SkewSat import SkewSat

### Istancia da classe
    rx_lat = -7.0838699 # Latitude do receptor (antena)
    rx_log = -41.4668289 # Longitude do receptor (antena)
    tx_log = -70 # Longitude do Transmissor  (satélite)
    
    sk = SkewSat.SkewSat( rx_lat, rx_log, tx_log )

### Longitude de todos os satélites geoestacionários
    from satellites import satellites
    print(satellites)

### Azimute (verdadeiro)
    azimuth = sk.getAzimuth()

### Elevação da antena
    elevation = sk.getElevation()

### Elevação de antena Offset
    elevation_offset = sk.convertElevationToOffset(elevation)

### Inclinação LNBF (graus)
    skew_LNBF = sk.getSkewLNBF()

### Inclinação LNBF (horas)
    skew_LNBF_h = sk.skewLnbfDegreesToHours(skew_LNBF)

### Exemplo
    print( f'Satélite: {sk._tx_log}°')
    print( f'Azimute verdadeiro: {azimuth:.1f}°')
    print( f'Elevação: {elevation:.1f}°')
    print( f'Elevação (offset): {elevation_offset:.1f}°')
    print( f'Inclinação do LNBF: {skew_LNBF:.1f}°')
    print( f'Inclinação do LNBF (h): ~ {skew_LNBF_h:.0f}h')
#### Saída
    >>> Satélite: -70°
    >>> Azimute verdadeiro: 282.8°
    >>> Elevação: 55.8°
    >>> Elevação (offset): 35.3°
    >>> Inclinação do LNBF: -75.4°
    >>> Inclinação do LNBF (h): ~ 9h
### Criando mapa
    sk.open_map()
    

## Exemplo de saída
![Imagem da renderização do html de saída.](https://raw.githubusercontent.com/1bertojunior/SkewSat/main/img/exSkewSatMap.png)
