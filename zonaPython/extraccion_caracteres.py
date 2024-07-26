import xml.etree.ElementTree as ET

xml_string = """
-<TED version="1.0">
-<DD>
<RE>76451166-2</RE>
<TD>33</TD>
<F>249</F>
<FE>2023-09-22</FE>
<RR>77029472-K</RR>
<RSR>Elite Brands International Chile SPA</RSR>
<MNT>7568108</MNT>
<IT1>Arriendo Oficinas 1608-1609-1610 Edifici</IT1>
-<CAF version="1.0">
-<DA>
<RE>76451166-2</RE>
<RS>INMOBILIARIA E INVERSIONES INTERHAUS SPA</RS>
<TD>33</TD>
-<RNG>
<D>248</D>
<H>253</H>
</RNG>
<FA>2023-06-20</FA>
-<RSAPK>
<M>s4ydyEQCA0mMZuVp4jByiXxL/soymRVCUP/7uxG439d+1WOZmJGpS1CwyVRO+LjCYy/7zAlgT8uAuNOs+5cZnw==</M>
<E>Aw==</E>
</RSAPK>
<IDK>300</IDK>
</DA>
<FRMA algoritmo="SHA1withRSA">iMPxQcMUtfg3yrhevR8vXs1RuRAQni9YgL+8cnEq08Q7dUGXEjAEe9dnP6Chn9+KpbxAdLUQ8GAqtFM4CqyFIw==</FRMA>
</CAF>
<TSTED>2023-09-22T12:09:03</TSTED>
</DD>
<FRMT algoritmo="SHA1withRSA">eO6QDzMcr2r/24GgA6uxO8843tzBLpge3PF7E4IQOUtm0bSlm1TcVbYP64Mx4JRnJdcEuB2NfltIjlLKV366dg==</FRMT>
</TED>
"""
print(xml_string)
# Reemplazar '\n' con ''
xml_string_sin_saltos_de_linea = xml_string.replace('\n', '')

print(xml_string_sin_saltos_de_linea)