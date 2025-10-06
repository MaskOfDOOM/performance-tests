import xml.etree.ElementTree as EL

xml_data = """
<user>
    <id>1</id>
    <first_name>Doe</first_name>
    <last_name>John</last_name>
    <address>
        <street>Razina</street>
        <city>Moscow</city>
        <zip>101000</zip>
    </adress>
</user>
"""

root = EL.fromstring(xml_data)

print('User ID:', root.find('id').text)