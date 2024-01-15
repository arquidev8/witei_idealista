
#VERSION DE PRODUCCION

# import requests
# import time
# import re
# from ftplib import FTP
# import json
# import xmltodict
#
# def remove_postal_code(address):
#     pattern = r'\b\d{5}\b,?$'
#     address = re.sub(pattern, '', address)
#     return address.rstrip(', ')
#
# def download_xml(url, save_path):
#     response = requests.get(url)
#     with open(save_path, 'wb') as xml_file:
#         xml_file.write(response.content)
#
#
# def remove_duplicates(json_dict):
#    unique_properties = []
#    property_references = set()
#
#    for property in json_dict['customerProperties']:
#        property_reference = property['propertyReference']
#        if property_reference not in property_references:
#            property_references.add(property_reference)
#            unique_properties.append(property)
#
#    json_dict['customerProperties'] = unique_properties
#
#    return json_dict
#
#
#
# def remove_empty_descriptions(descriptions):
#    return [description for description in descriptions if description['descriptionText']]
#
#
# def transform_xml_to_json(xml_file_path):
#     with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
#         data_dict = xmltodict.parse(xml_file.read())
#
#     # Resto del código para la transformación XML a JSON
#     json_dict = {}  # Asegúrate de inicializar tu diccionario aquí
#
#     # Mapea los campos XML a los campos JSON
#     json_dict["customerCountry"] = "Spain"
#     json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1"  # Reemplaza con tu propio código
#     json_dict["customerReference"] = "Witei"  # Reemplaza con tu propia referencia
#     json_dict["customerContact"] = {
#      "contactName": "HannanPiper",
#      "contactEmail": "sxkn@inbox.witei.com",
#      "contactPrimaryPhonePrefix": "34",
#      "contactPrimaryPhoneNumber": "931595880",
#     }
#
#     # Mapea los campos restantes
#     json_dict["customerProperties"] = []
#
#     # Itera sobre cada propiedad en la lista
#     for property in data_dict["root"]["property"]:
#      property_dict = {}
#
#      property_dict["propertyCode"] = property.get("id", "")
#      property_dict["propertyReference"] = property.get("ref", "")
#      property_dict["propertyVisibility"] = "idealista"
#
#      operationPrice = int(property.get("price", "") or 0)
#
#      property_dict["propertyOperation"] = {
#          "operationType": property.get("price_freq", ""),
#          "operationPrice": operationPrice,
#      }
#
#      # Verifica si price_freq está vacío o no está presente
#      if not property_dict["propertyOperation"]["operationType"]:
#          # Si está vacío, asigna el valor predeterminado "rent"
#          property_dict["propertyOperation"]["operationType"] = "rent"
#      elif property_dict["propertyOperation"]["operationType"] == "month":
#          # Si es "month", cambia a "rent"
#          property_dict["propertyOperation"]["operationType"] = "rent"
#
#
#      addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#      addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#      property_dict["propertyAddress"] = {
#       "addressVisibility": "street",
#       "addressStreetName": property.get("location_detail", ""),
#       "addressUrbanization": property.get("town", ""),
#       "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#       "addressTown": property.get("town", ""),
#       "addressCountry": property.get("country", ""),
#       "addressCoordinatesPrecision": "exact",
#       "addressCoordinatesLatitude": addressCoordinatesLatitude,
#       "addressCoordinatesLongitude": addressCoordinatesLongitude,
#      }
#
#      if property_dict["propertyAddress"]["addressStreetName"] is not None:
#       property_dict["propertyAddress"]["addressStreetName"] = remove_postal_code(
#        property_dict["propertyAddress"]["addressStreetName"])
#
#      # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#      property_dict["propertyAddress"] = {k: v for k, v in property_dict["propertyAddress"].items() if v}
#
#
#      type_value = property.get("type", "").lower()
#
#      if type_value in ["piso", "casa", "apartamento", "vivienda", "penthouse", "duplex", "studio",
#                        "building", "industrial", "apartment", "mansion"]:
#          type_value = "flat"
#      elif type_value == "parking":
#          type_value = "garage"
#      elif type_value == "office":
#          type_value = "office"
#      elif type_value == "terreno":
#          type_value = "land"
#      elif type_value == "shop":
#          type_value = "premises"
#      elif type_value == "villa":
#          type_value = "rustic_village"
#
#      featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get(
#          "surface_area", {}).get("built") else None
#      featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get(
#          "surface_area", {}).get("plot") else None
#      featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
#      featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1
#
#      # Lógica para land
#      if type_value == "land":
#          # Verifica si featuresAreaPlot tiene un valor no nulo y no es 0
#          if featuresAreaPlot is not None and featuresAreaPlot != 0:
#              property_dict["propertyFeatures"] = {
#                  "featuresType": type_value,
#                  "featuresAreaConstructed": featuresAreaConstructed,
#                  "featuresAreaPlot": featuresAreaPlot,
#              }
#      else:
#          # Lógica para otros tipos de propiedad
#          property_dict["propertyFeatures"] = {
#              "featuresType": type_value,
#              "featuresAreaConstructed": featuresAreaConstructed,
#              "featuresAreaPlot": featuresAreaPlot,
#              "featuresBathroomNumber": featuresBathroomNumber,
#              "featuresBedroomNumber": featuresBedroomNumber,
#          }
#
#          # Elimina los campos con valor None o cero en "propertyFeatures"
#          property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None and v != 0}
#
#
#      # Si featuresAreaConstructed es 1 o featuresAreaPlot es 0, salta la adición de property_dict a json_dict["customerProperties"]
#      if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1 and property_dict["propertyFeatures"].get("featuresAreaPlot") != 0:
#          json_dict["customerProperties"].append(property_dict)
#
#      def convert_to_float(value):
#       try:
#        return float(value.replace(',', '.'))
#       except ValueError:
#        return 0.0
#
#      try:
#       featuresEnergyCertificatePerformance = convert_to_float(
#        property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#      except AttributeError:
#       print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#      if featuresEnergyCertificatePerformance == 999.0:
#       featuresEnergyCertificatePerformance = None
#
#      featuresRooms = int(property.get("beds", "")) if property.get("beds") else 1
#      featuresAreaUsable = property.get("surface_area", {}).get("usable", None)
#      energy_rating = property.get("energy_rating", {}).get("consumption", "")
#
#      if energy_rating != "X":
#       property_dict["propertyFeatures"] = {
#        "featuresType": type_value,
#        "featuresAreaConstructed": featuresAreaConstructed,
#        # "featuresAreaUsable": featuresAreaUsable,
#        "featuresBathroomNumber": featuresBathroomNumber,
#        "featuresBedroomNumber": featuresBedroomNumber,
#        "featuresEnergyCertificateRating": energy_rating,
#        "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#        "featuresRooms": featuresRooms,
#       }
#      else:
#       property_dict["propertyFeatures"] = {
#        "featuresType": type_value,
#        "featuresAreaConstructed": featuresAreaConstructed,
#        # "featuresAreaUsable": featuresAreaUsable,
#        "featuresBathroomNumber": featuresBathroomNumber,
#        "featuresBedroomNumber": featuresBedroomNumber,
#        "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#        "featuresRooms": featuresRooms,
#       }
#
#      # Agrega featuresAreaPlot solo si la propiedad es de tipo "land"
#      if type_value == "land" and featuresAreaPlot is not None and featuresAreaPlot != 0:
#          property_dict["propertyFeatures"]["featuresAreaPlot"] = featuresAreaPlot
#      elif "featuresAreaPlot" in property_dict["propertyFeatures"]:
#          del property_dict["propertyFeatures"]["featuresAreaPlot"]
#
#      # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#      if type_value == "flat":
#       property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(
#        property_dict["propertyFeatures"].get("featuresBathroomNumber", 1))
#       property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(
#        property_dict["propertyFeatures"].get("featuresBedroomNumber", 1))
#
#      # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#      if type_value == "flat":
#       property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(
#        property_dict["propertyFeatures"].get("featuresBathroomNumber", 1)) or 1
#       property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(
#        property_dict["propertyFeatures"].get("featuresBedroomNumber", 1)) or 1
#       property_dict["propertyFeatures"]["featuresRooms"] = int(
#        property_dict["propertyFeatures"].get("featuresRooms", 1)) or 1
#       property_dict["propertyFeatures"]["featuresAreaConstructed"] = int(
#        property_dict["propertyFeatures"].get("featuresAreaConstructed")) if property_dict["propertyFeatures"].get(
#        "featuresAreaConstructed") is not None else 1
#
#      # Si la propiedad no es de tipo "flat", elimina los campos featuresBathroomNumber, featuresBedroomNumber y featuresRooms
#      if type_value != "flat":
#       property_dict["propertyFeatures"].pop("featuresBathroomNumber", None)
#       property_dict["propertyFeatures"].pop("featuresBedroomNumber", None)
#       property_dict["propertyFeatures"].pop("featuresRooms", None)
#
#      # Elimina los campos con valor None en "propertyFeatures"
#      property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None}
#
#      property_dict["propertyDescriptions"] = [
#          {
#              "descriptionLanguage": "spanish",
#              "descriptionText": property.get("desc", {}).get("es", "")
#          },
#          {
#              "descriptionLanguage": "english",
#              "descriptionText": property.get("desc", {}).get("en", "")
#          },
#          {
#              "descriptionLanguage": "catalan",
#              "descriptionText": property.get("desc", {}).get("ca", "")
#          },
#          {
#              "descriptionLanguage": "russian",
#              "descriptionText": property.get("desc", {}).get("ru", "")
#          },
#          {
#              "descriptionLanguage": "french",
#              "descriptionText": property.get("desc", {}).get("fr", "")
#          },
#          {
#              "descriptionLanguage": "italian",
#              "descriptionText": property.get("desc", {}).get("it", "")
#          },
#          {
#              "descriptionLanguage": "german",
#              "descriptionText": property.get("desc", {}).get("de", "")
#          },
#      ]
#
#      # Llama a la función remove_empty_descriptions para eliminar las descripciones vacías
#      descriptions = remove_empty_descriptions(property_dict["propertyDescriptions"])
#
#      # Agrega las descripciones al diccionario de la propiedad
#      property_dict["propertyDescriptions"] = descriptions
#
#
#
#      property_dict["propertyImages"] = []
#      for image in property.get("images", {}).get("image", []):
#       try:
#        image_dict = {
#         "imageOrder": int(image.get("@id", "") or 0),
#         # "imageLabel": "property",
#         "imageUrl": image.get("url", "")
#        }
#        property_dict["propertyImages"].append(image_dict)
#       except AttributeError:
#        pass
#
#      property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#      video_url = property.get("video_url", "")
#      if video_url:  # Si videoUrl no está vacío
#       property_dict["propertyVideos"] = [
#        {
#         "videoOrder": 1,
#         "videoUrl": video_url
#        }
#       ]
#
#      if 'propertyVideos' in property_dict:
#       property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict["propertyVideos"]]
#
#
#      # Si featuresAreaConstructed es 1, salta la adición de property_dict a json_dict["customerProperties"]
#      if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1:
#       json_dict["customerProperties"].append(property_dict)
#
#
#
#     json_dict = remove_duplicates(json_dict)
#
#     return json_dict
#
#
# def upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path):
#     with FTP(ftp_host) as ftp:
#         ftp.login(user=ftp_user, passwd=ftp_password)
#         ftp.cwd(ftp_destination_folder)
#         with open(json_file_path, 'rb') as file:
#             ftp.storbinary('STOR ' + json_file_path, file)
#
# # Configuración del enlace XML y el temporizador (40 minutos = 2400 segundos)
# xml_url = 'https://app.witei.com/pro/interconnection/xml/d1e8a7f70b7e4546/'
# download_interval = 43200
#
# while True:
#     try:
#         # Descarga el archivo XML
#         xml_file_path = 'd1e8a7f70b7e4546.xml'
#         download_xml(xml_url, xml_file_path)
#
#         # Transforma el XML a JSON
#         json_dict = transform_xml_to_json(xml_file_path)
#
#         # Configuración de FTP
#         ftp_host = 'ftp2.idealista.com'
#         ftp_user = 'hannanpiper'
#         ftp_password = 'ViamLapBa'
#         ftp_destination_folder = '/'
#         json_file_path = 'ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json'
#
#         # Convierte el diccionario a JSON usando json.dumps()
#         json_data = json.dumps(json_dict)
#
#         # Escribe los datos JSON en un archivo de salida
#         with open(json_file_path, "w") as json_file:
#             json_file.write(json_data)
#
#         # # Guarda una copia del archivo JSON con un nombre diferente
#         # json_copy_path = 'copia_' + json_file_path
#         # with open(json_copy_path, "w") as json_copy_file:
#         #  json_copy_file.write(json_data)
#
#         # Sube el archivo JSON por FTP
#         upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path)
#
#         print('Proceso completado con éxito.')
#
#     except Exception as e:
#         print(f"Error en el proceso: {e}")
#
#     # Espera antes de volver a descargar el archivo XML
#     time.sleep(download_interval)






#VERSION TEST

import requests
import time
import re
from ftplib import FTP
import json
import xmltodict

def remove_postal_code(address):
    pattern = r'\b\d{5}\b,?$'
    address = re.sub(pattern, '', address)
    return address.rstrip(', ')

def download_xml(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as xml_file:
        xml_file.write(response.content)


def remove_duplicates(json_dict):
   unique_properties = []
   property_references = set()

   for property in json_dict['customerProperties']:
       property_reference = property['propertyReference']
       if property_reference not in property_references:
           property_references.add(property_reference)
           unique_properties.append(property)

   json_dict['customerProperties'] = unique_properties

   return json_dict



def remove_empty_descriptions(descriptions):
   return [description for description in descriptions if description['descriptionText']]


def transform_xml_to_json(xml_file_path):
    with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    # Resto del código para la transformación XML a JSON
    json_dict = {}  # Asegúrate de inicializar tu diccionario aquí

    # Mapea los campos XML a los campos JSON
    json_dict["customerCountry"] = "Spain"
    json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1"  # Reemplaza con tu propio código
    json_dict["customerReference"] = "Witei"  # Reemplaza con tu propia referencia
    json_dict["customerContact"] = {
     "contactName": "HannanPiper",
     "contactEmail": "sxkn@inbox.witei.com",
     "contactPrimaryPhonePrefix": "34",
     "contactPrimaryPhoneNumber": "931595880",
    }

    # Mapea los campos restantes
    json_dict["customerProperties"] = []

    # Itera sobre cada propiedad en la lista
    for property in data_dict["root"]["property"]:
     property_dict = {}

     property_dict["propertyCode"] = property.get("id", "")
     property_dict["propertyReference"] = property.get("ref", "")
     property_dict["propertyVisibility"] = "idealista"

     operationPrice = int(property.get("price", "") or 0)

     property_dict["propertyOperation"] = {
         "operationType": property.get("price_freq", ""),
         "operationPrice": operationPrice,
     }

     # Verifica si price_freq está vacío o no está presente
     if not property_dict["propertyOperation"]["operationType"]:
         # Si está vacío, asigna el valor predeterminado "rent"
         property_dict["propertyOperation"]["operationType"] = "rent"
     elif property_dict["propertyOperation"]["operationType"] == "month":
         # Si es "month", cambia a "rent"
         property_dict["propertyOperation"]["operationType"] = "rent"


     addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
     addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)

     property_dict["propertyAddress"] = {
      "addressVisibility": "street",
      "addressStreetName": property.get("location_detail", ""),
      "addressUrbanization": property.get("town", ""),
      "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
      "addressTown": property.get("town", ""),
      "addressCountry": property.get("country", ""),
      "addressCoordinatesPrecision": "exact",
      "addressCoordinatesLatitude": addressCoordinatesLatitude,
      "addressCoordinatesLongitude": addressCoordinatesLongitude,
     }

     if property_dict["propertyAddress"]["addressStreetName"] is not None:
      property_dict["propertyAddress"]["addressStreetName"] = remove_postal_code(
       property_dict["propertyAddress"]["addressStreetName"])

     # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
     property_dict["propertyAddress"] = {k: v for k, v in property_dict["propertyAddress"].items() if v}


     type_value = property.get("type", "").lower()

     if type_value in ["piso", "casa", "apartamento", "vivienda", "penthouse", "duplex", "studio",
                       "building", "industrial", "apartment", "mansion"]:
         type_value = "flat"
     elif type_value == "parking":
         type_value = "garage"
     elif type_value == "office":
         type_value = "office"
     elif type_value == "terreno":
         type_value = "land"
     elif type_value == "shop":
         type_value = "premises"
     elif type_value == "villa":
         type_value = "rustic_village"

     featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get(
         "surface_area", {}).get("built") else None
     featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get(
         "surface_area", {}).get("plot") else None
     featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
     featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1

     # Lógica para land
     if type_value == "land":
         # Verifica si featuresAreaPlot tiene un valor no nulo y no es 0
         if featuresAreaPlot is not None and featuresAreaPlot != 0:
             property_dict["propertyFeatures"] = {
                 "featuresType": type_value,
                 "featuresAreaConstructed": featuresAreaConstructed,
                 "featuresAreaPlot": featuresAreaPlot,
             }
     else:
         # Lógica para otros tipos de propiedad
         property_dict["propertyFeatures"] = {
             "featuresType": type_value,
             "featuresAreaConstructed": featuresAreaConstructed,
             "featuresAreaPlot": featuresAreaPlot,
             "featuresBathroomNumber": featuresBathroomNumber,
             "featuresBedroomNumber": featuresBedroomNumber,
         }

         # Elimina los campos con valor None o cero en "propertyFeatures"
         property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None and v != 0}


     # Si featuresAreaConstructed es 1 o featuresAreaPlot es 0, salta la adición de property_dict a json_dict["customerProperties"]
     if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1 and property_dict["propertyFeatures"].get("featuresAreaPlot") != 0:
         json_dict["customerProperties"].append(property_dict)

     def convert_to_float(value):
      try:
       return float(value.replace(',', '.'))
      except ValueError:
       return 0.0

     try:
      featuresEnergyCertificatePerformance = convert_to_float(
       property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
     except AttributeError:
      print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")

     if featuresEnergyCertificatePerformance == 999.0:
      featuresEnergyCertificatePerformance = None

     featuresRooms = int(property.get("beds", "")) if property.get("beds") else 1
     featuresAreaUsable = property.get("surface_area", {}).get("usable", None)
     energy_rating = property.get("energy_rating", {}).get("consumption", "")

     if energy_rating != "X":
      property_dict["propertyFeatures"] = {
       "featuresType": type_value,
       "featuresAreaConstructed": featuresAreaConstructed,
       # "featuresAreaUsable": featuresAreaUsable,
       "featuresBathroomNumber": featuresBathroomNumber,
       "featuresBedroomNumber": featuresBedroomNumber,
       "featuresEnergyCertificateRating": energy_rating,
       "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
       "featuresRooms": featuresRooms,
      }
     else:
      property_dict["propertyFeatures"] = {
       "featuresType": type_value,
       "featuresAreaConstructed": featuresAreaConstructed,
       # "featuresAreaUsable": featuresAreaUsable,
       "featuresBathroomNumber": featuresBathroomNumber,
       "featuresBedroomNumber": featuresBedroomNumber,
       "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
       "featuresRooms": featuresRooms,
      }

     # Agrega featuresAreaPlot solo si la propiedad es de tipo "land"
     if type_value == "land" and featuresAreaPlot is not None and featuresAreaPlot != 0:
         property_dict["propertyFeatures"]["featuresAreaPlot"] = featuresAreaPlot
     elif "featuresAreaPlot" in property_dict["propertyFeatures"]:
         del property_dict["propertyFeatures"]["featuresAreaPlot"]

     # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
     if type_value == "flat":
      property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(
       property_dict["propertyFeatures"].get("featuresBathroomNumber", 1))
      property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(
       property_dict["propertyFeatures"].get("featuresBedroomNumber", 1))

     # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
     if type_value == "flat":
      property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(
       property_dict["propertyFeatures"].get("featuresBathroomNumber", 1)) or 1
      property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(
       property_dict["propertyFeatures"].get("featuresBedroomNumber", 1)) or 1
      property_dict["propertyFeatures"]["featuresRooms"] = int(
       property_dict["propertyFeatures"].get("featuresRooms", 1)) or 1
      property_dict["propertyFeatures"]["featuresAreaConstructed"] = int(
       property_dict["propertyFeatures"].get("featuresAreaConstructed")) if property_dict["propertyFeatures"].get(
       "featuresAreaConstructed") is not None else 1

     # Si la propiedad no es de tipo "flat", elimina los campos featuresBathroomNumber, featuresBedroomNumber y featuresRooms
     if type_value != "flat":
      property_dict["propertyFeatures"].pop("featuresBathroomNumber", None)
      property_dict["propertyFeatures"].pop("featuresBedroomNumber", None)
      property_dict["propertyFeatures"].pop("featuresRooms", None)

     # Elimina los campos con valor None en "propertyFeatures"
     property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None}

     property_dict["propertyDescriptions"] = [
         {
             "descriptionLanguage": "spanish",
             "descriptionText": property.get("desc", {}).get("es", "")
         },
         {
             "descriptionLanguage": "english",
             "descriptionText": property.get("desc", {}).get("en", "")
         },
         {
             "descriptionLanguage": "catalan",
             "descriptionText": property.get("desc", {}).get("ca", "")
         },
         {
             "descriptionLanguage": "russian",
             "descriptionText": property.get("desc", {}).get("ru", "")
         },
         {
             "descriptionLanguage": "french",
             "descriptionText": property.get("desc", {}).get("fr", "")
         },
         {
             "descriptionLanguage": "italian",
             "descriptionText": property.get("desc", {}).get("it", "")
         },
         {
             "descriptionLanguage": "german",
             "descriptionText": property.get("desc", {}).get("de", "")
         },
     ]

     # Llama a la función remove_empty_descriptions para eliminar las descripciones vacías
     descriptions = remove_empty_descriptions(property_dict["propertyDescriptions"])

     # Agrega las descripciones al diccionario de la propiedad
     property_dict["propertyDescriptions"] = descriptions



     property_dict["propertyImages"] = []
     for image in property.get("images", {}).get("image", []):
      try:
       image_dict = {
        "imageOrder": int(image.get("@id", "") or 0),
        # "imageLabel": "property",
        "imageUrl": image.get("url", "")
       }
       property_dict["propertyImages"].append(image_dict)
      except AttributeError:
       pass

     property_dict["propertyUrl"] = property.get("url", {}).get("es", "")

     video_url = property.get("video_url", "")
     if video_url:  # Si videoUrl no está vacío
      property_dict["propertyVideos"] = [
       {
        "videoOrder": 1,
        "videoUrl": video_url
       }
      ]

     if 'propertyVideos' in property_dict:
      property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict["propertyVideos"]]


     # Si featuresAreaConstructed es 1, salta la adición de property_dict a json_dict["customerProperties"]
     if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1:
      json_dict["customerProperties"].append(property_dict)

     #####################
     # # Si ya tienes 450 propiedades, sal del bucle
     # if len(json_dict["customerProperties"]) >= 700:
     #      break
     #
     # # Añade la propiedad solo si no has alcanzado la cantidad límite
     # json_dict["customerProperties"].append(property_dict)

     # Añadir propiedades adicionales por número de referencia
    additional_properties = [
        # Lista de propiedades adicionales con sus números de referencia
        {"propertyReference": "HPA-9095", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-6025", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9013", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9016", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9018", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9028MB2", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9029MB3", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9030MB4", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-2233CR", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9031", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9034", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9035", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9040APN", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9042", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9046", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9077", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9078", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9080FKM", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9084", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9085DPT", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9086", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9089", "propertyVisibility": "idealista", },
        {"propertyReference": "HPA-9095", "propertyVisibility": "idealista", },
        {"propertyReference": "HP-9100", "propertyVisibility": "idealista", },
        # ... Añade más propiedades según sea necesario
    ]

    for additional_property in additional_properties:
        # Añade la propiedad sin verificar el límite
        json_dict["customerProperties"].append(additional_property)

        # Rompe el bucle solo si ya tienes 500 propiedades
        if len(json_dict["customerProperties"]) <= 450:
            break


    json_dict = remove_duplicates(json_dict)

    return json_dict


def upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path):
    with FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd(ftp_destination_folder)
        with open(json_file_path, 'rb') as file:
            ftp.storbinary('STOR ' + json_file_path, file)

# Configuración del enlace XML y el temporizador (40 minutos = 2400 segundos)
xml_url = 'https://app.witei.com/pro/interconnection/xml/d1e8a7f70b7e4546/'
download_interval = 43200

while True:
    try:
        # Descarga el archivo XML
        xml_file_path = 'd1e8a7f70b7e4546.xml'
        download_xml(xml_url, xml_file_path)

        # Transforma el XML a JSON
        json_dict = transform_xml_to_json(xml_file_path)

        # Configuración de FTP
        ftp_host = 'ftp2.idealista.com'
        ftp_user = 'hannanpiper'
        ftp_password = 'ViamLapBa'
        ftp_destination_folder = '/'
        json_file_path = 'ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json'

        # Convierte el diccionario a JSON usando json.dumps()
        json_data = json.dumps(json_dict)

        # Escribe los datos JSON en un archivo de salida
        with open(json_file_path, "w") as json_file:
            json_file.write(json_data)

        # # Guarda una copia del archivo JSON con un nombre diferente
        # json_copy_path = 'copia_' + json_file_path
        # with open(json_copy_path, "w") as json_copy_file:
        #  json_copy_file.write(json_data)

        # Sube el archivo JSON por FTP
        upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path)

        print('Proceso completado con éxito.')

    except Exception as e:
        print(f"Error en el proceso: {e}")

    # Espera antes de volver a descargar el archivo XML
    time.sleep(download_interval)



