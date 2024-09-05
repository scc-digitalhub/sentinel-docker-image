from cdsetool.credentials import Credentials
from cdsetool.download import download_features
from cdsetool.monitor import StatusMonitor

features = [{'type': 'Feature', 'id': '5179b7e6-b104-499a-a884-8342709764b0', 'geometry': {'type': 'Polygon', 'coordinates': [[[13.843748, 44.628178], [14.299472, 46.245007], [10.965346, 46.646072], [10.607134, 45.028782], [13.843748, 44.628178]]]}, 'properties': {'collection': 'SENTINEL-1', 'status': 'ONLINE', 'license': {'licenseId': 'unlicensed', 'hasToBeSigned': 'never', 'grantedCountries': None, 'grantedOrganizationCountries': None, 'grantedFlags': None, 'viewService': 'public', 'signatureQuota': -1, 'description': {'shortName': 'No license'}}, 'parentIdentifier': None, 'title': 'S1A_IW_SLC__1SDV_20231212T051925_20231212T051952_051617_063B7D_3126.SAFE', 'description': 'The Sentinel-1 mission is the European Radar Observatory for the Copernicus joint initiative of the European Commission (EC) and the European Space Agency (ESA). The Sentinel-1 mission includes C-band imaging operating in four exclusive imaging modes with different resolution (down to 5 m) and coverage (up to 400 km). It provides dual polarization capability, short revisit times and rapid product delivery. Additionally, precise measurements of spacecraft position and attitude are available for every observation [https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1].', 'organisationName': None, 'startDate': '2023-12-12T05:19:25.473266Z', 'completionDate': '2023-12-12T05:19:52.454498Z', 'productType': 'IW_SLC__1S', 'processingLevel': 'LEVEL1', 'platform': 'S1A', 'instrument': 'SAR', 'resolution': 0, 'sensorMode': 'IW', 'orbitNumber': 51617, 'quicklook': None, 'thumbnail': 'https://catalogue.dataspace.copernicus.eu/get-object?path=/Sentinel-1/SAR/IW_SLC__1S/2023/12/12/S1A_IW_SLC__1SDV_20231212T051925_20231212T051952_051617_063B7D_3126.SAFE/preview/thumbnail.png', 'updated': '2023-12-12T06:42:45.498170Z', 'published': '2023-12-12T06:30:32.469071Z', 'snowCover': 0, 'cloudCover': 0, 'gmlgeometry': '<gml:Polygon srsName="EPSG:4326"><gml:outerBoundaryIs><gml:LinearRing><gml:coordinates>13.843748,44.628178 14.299472,46.245007 10.965346,46.646072 10.607134,45.028782 13.843748,44.628178</gml:coordinates></gml:LinearRing></gml:outerBoundaryIs></gml:Polygon>', 'centroid': {'type': 'Point', 'coordinates': [12.4317812951919, 45.64066564209]}, 'productIdentifier': '/eodata/Sentinel-1/SAR/IW_SLC__1S/2023/12/12/S1A_IW_SLC__1SDV_20231212T051925_20231212T051952_051617_063B7D_3126.SAFE', 'orbitDirection': 'DESCENDING', 'timeliness': 'NRT-3h', 'relativeOrbitNumber': 95, 'processingBaseline': 3.71, 'polarisation': 'VV&VH', 'swath': 'IW1,IW2,IW3', 'services': {'download': {'url': 'https://catalogue.dataspace.copernicus.eu/download/5179b7e6-b104-499a-a884-8342709764b0', 'mimeType': 'application/octet-stream', 'size': 8283015128}}, 'links': [{'rel': 'self', 'type': 'application/json', 'title': 'GeoJSON link for 5179b7e6-b104-499a-a884-8342709764b0', 'href': 'https://catalogue.dataspace.copernicus.eu/resto/collections/SENTINEL-1/5179b7e6-b104-499a-a884-8342709764b0.json'}]}, 'Name': '095 202710 IW3'}, {'type': 'Feature', 'id': '7c94c2f9-1b4e-4bb8-b373-5d5dd4a25a3a', 'geometry': {'type': 'Polygon', 'coordinates': [[[10.317101, 43.875561], [13.504453, 44.275791], [13.14915, 45.893536], [9.868135, 45.493038], [10.317101, 43.875561]]]}, 'properties': {'collection': 'SENTINEL-1', 'status': 'ONLINE', 'license': {'licenseId': 'unlicensed', 'hasToBeSigned': 'never', 'grantedCountries': None, 'grantedOrganizationCountries': None, 'grantedFlags': None, 'viewService': 'public', 'signatureQuota': -1, 'description': {'shortName': 'No license'}}, 'parentIdentifier': None, 'title': 'S1A_IW_SLC__1SDV_20231213T170659_20231213T170726_051639_063C47_9EFE.SAFE', 'description': 'The Sentinel-1 mission is the European Radar Observatory for the Copernicus joint initiative of the European Commission (EC) and the European Space Agency (ESA). The Sentinel-1 mission includes C-band imaging operating in four exclusive imaging modes with different resolution (down to 5 m) and coverage (up to 400 km). It provides dual polarization capability, short revisit times and rapid product delivery. Additionally, precise measurements of spacecraft position and attitude are available for every observation [https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1].', 'organisationName': None, 'startDate': '2023-12-13T17:06:59.168045Z', 'completionDate': '2023-12-13T17:07:26.149277Z', 'productType': 'IW_SLC__1S', 'processingLevel': 'LEVEL1', 'platform': 'S1A', 'instrument': 'SAR', 'resolution': 0, 'sensorMode': 'IW', 'orbitNumber': 51639, 'quicklook': None, 'thumbnail': 'https://catalogue.dataspace.copernicus.eu/get-object?path=/Sentinel-1/SAR/IW_SLC__1S/2023/12/13/S1A_IW_SLC__1SDV_20231213T170659_20231213T170726_051639_063C47_9EFE.SAFE/preview/thumbnail.png', 'updated': '2023-12-13T18:20:18.438064Z', 'published': '2023-12-13T18:19:10.885487Z', 'snowCover': 0, 'cloudCover': 0, 'gmlgeometry': '<gml:Polygon srsName="EPSG:4326"><gml:outerBoundaryIs><gml:LinearRing><gml:coordinates>10.317101,43.875561 13.504453,44.275791 13.14915,45.893536 9.868135,45.493038 10.317101,43.875561</gml:coordinates></gml:LinearRing></gml:outerBoundaryIs></gml:Polygon>', 'centroid': {'type': 'Point', 'coordinates': [11.7069367293826, 44.8880448790214]}, 'productIdentifier': '/eodata/Sentinel-1/SAR/IW_SLC__1S/2023/12/13/S1A_IW_SLC__1SDV_20231213T170659_20231213T170726_051639_063C47_9EFE.SAFE', 'orbitDirection': 'ASCENDING', 'timeliness': 'NRT-3h', 'relativeOrbitNumber': 117, 'processingBaseline': 3.71, 'polarisation': 'VV&VH', 'swath': 'IW1,IW2,IW3', 'services': {'download': {'url': 'https://catalogue.dataspace.copernicus.eu/download/7c94c2f9-1b4e-4bb8-b373-5d5dd4a25a3a', 'mimeType': 'application/octet-stream', 'size': 8137853152}}, 'links': [{'rel': 'self', 'type': 'application/json', 'title': 'GeoJSON link for 7c94c2f9-1b4e-4bb8-b373-5d5dd4a25a3a', 'href': 'https://catalogue.dataspace.copernicus.eu/resto/collections/SENTINEL-1/7c94c2f9-1b4e-4bb8-b373-5d5dd4a25a3a.json'}]}, 'Name': '117 249427 IW2'}, {'type': 'Feature', 'id': '2b36fd47-a170-4ade-8c39-bfb4ca81be4f', 'geometry': {'type': 'Polygon', 'coordinates': [[[9.937226, 45.36879], [13.19666, 45.766773], [12.834831, 47.3834], [9.474743, 46.984745], [9.937226, 45.36879]]]}, 'properties': {'collection': 'SENTINEL-1', 'status': 'ONLINE', 'license': {'licenseId': 'unlicensed', 'hasToBeSigned': 'never', 'grantedCountries': None, 'grantedOrganizationCountries': None, 'grantedFlags': None, 'viewService': 'public', 'signatureQuota': -1, 'description': {'shortName': 'No license'}}, 'parentIdentifier': None, 'title': 'S1A_IW_SLC__1SDV_20231213T170724_20231213T170750_051639_063C47_67DD.SAFE', 'description': 'The Sentinel-1 mission is the European Radar Observatory for the Copernicus joint initiative of the European Commission (EC) and the European Space Agency (ESA). The Sentinel-1 mission includes C-band imaging operating in four exclusive imaging modes with different resolution (down to 5 m) and coverage (up to 400 km). It provides dual polarization capability, short revisit times and rapid product delivery. Additionally, precise measurements of spacecraft position and attitude are available for every observation [https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1].', 'organisationName': None, 'startDate': '2023-12-13T17:07:24.001221Z', 'completionDate': '2023-12-13T17:07:50.976286Z', 'productType': 'IW_SLC__1S', 'processingLevel': 'LEVEL1', 'platform': 'S1A', 'instrument': 'SAR', 'resolution': 0, 'sensorMode': 'IW', 'orbitNumber': 51639, 'quicklook': None, 'thumbnail': 'https://catalogue.dataspace.copernicus.eu/get-object?path=/Sentinel-1/SAR/IW_SLC__1S/2023/12/13/S1A_IW_SLC__1SDV_20231213T170724_20231213T170750_051639_063C47_67DD.SAFE/preview/thumbnail.png', 'updated': '2023-12-13T18:36:10.205857Z', 'published': '2023-12-13T18:20:22.719015Z', 'snowCover': 0, 'cloudCover': 0, 'gmlgeometry': '<gml:Polygon srsName="EPSG:4326"><gml:outerBoundaryIs><gml:LinearRing><gml:coordinates>9.937226,45.36879 13.19666,45.766773 12.834831,47.3834 9.474743,46.984745 9.937226,45.36879</gml:coordinates></gml:LinearRing></gml:outerBoundaryIs></gml:Polygon>', 'centroid': {'type': 'Point', 'coordinates': [11.3579555678787, 46.3796799532099]}, 'productIdentifier': '/eodata/Sentinel-1/SAR/IW_SLC__1S/2023/12/13/S1A_IW_SLC__1SDV_20231213T170724_20231213T170750_051639_063C47_67DD.SAFE', 'orbitDirection': 'ASCENDING', 'timeliness': 'NRT-3h', 'relativeOrbitNumber': 117, 'processingBaseline': 3.71, 'polarisation': 'VV&VH', 'swath': 'IW1,IW2,IW3', 'services': {'download': {'url': 'https://catalogue.dataspace.copernicus.eu/download/2b36fd47-a170-4ade-8c39-bfb4ca81be4f', 'mimeType': 'application/octet-stream', 'size': 8138926549}}, 'links': [{'rel': 'self', 'type': 'application/json', 'title': 'GeoJSON link for 2b36fd47-a170-4ade-8c39-bfb4ca81be4f', 'href': 'https://catalogue.dataspace.copernicus.eu/resto/collections/SENTINEL-1/2b36fd47-a170-4ade-8c39-bfb4ca81be4f.json'}]}, 'Name': '117 249428 IW2'}]

username, password = "alattaruolo@fbk.eu","2CKb!#urVFbGUa4"
products_dir = "/home/mithra/Documents/donwload_sentinel_test/"
credentials = Credentials(username, password)
options = {"tmpdir": products_dir,'credentials': credentials, 'concurrency': 1,}
#options = {"tmpdir": products_dir,'credentials': credentials, 'concurrency': 1, 'monitor': StatusMonitor()}
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ start downloading @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
list(download_features(features, products_dir, options))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ end downloading @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
