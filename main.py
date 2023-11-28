# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("tu_archivo.xml") as xml_file:
#    data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = data_dict["property"]["country"]
# json_dict["customerCode"] = "ilc1234567890123456789012345678901234567890" # Reemplaza con tu propio código
# json_dict["customerReference"] = "external software reference" # Reemplaza con tu propia referencia
# json_dict["customerSendDate"] = data_dict["property"]["date"]
# json_dict["customerContact"] = {
#    "contactName": "customer contact name", # Reemplaza con tu propio nombre
#    "contactEmail": "contact@idealista.com", # Reemplaza con tu propio correo electrónico
#    "contactPrimaryPhonePrefix": "34",
#    "contactPrimaryPhoneNumber": "910000000",
#    "contactSecondaryPhonePrefix": "34",
#    "contactSecondaryPhoneNumber": "910000002"
# }
#
# # Continúa con el resto de los campos...
#
# # Convierte el diccionario a JSON usando json.dumps()
# json_data = json.dumps(json_dict)
#
# # Escribe los datos JSON en un archivo de salida
# with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#    json_file.write(json_data)




# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#   data_dict = xmltodict.parse(xml_file.read())
# print(data_dict)
#
#
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = data_dict["root"]["property"]["country"]
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerSendDate"] = data_dict["root"]["property"]["date"]
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "+34",
#  "contactPrimaryPhoneNumber": "931595880",
#  "contactSecondaryPhonePrefix": "",
#  "contactSecondaryPhoneNumber": ""
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
# property_dict = {}
#
# property_dict["propertyCode"] = data_dict["root"]["property"]["id"]
# property_dict["propertyReference"] = data_dict["root"]["property"]["ref"]
# property_dict["propertyVisibility"] = "idealista"
#
# property_dict["propertyOperation"] = {
#  "operationType": data_dict["root"]["property"]["price_freq"],
#  "operationPrice": data_dict["root"]["property"]["price"],
#  "operationPriceCommunity": "",
#  "operationPriceParking": ""
# }
#
# property_dict["propertyContact"] = {
#  "contactName": "",
#  "contactEmail": "",
#  "contactPrimaryPhonePrefix": "",
#  "contactPrimaryPhoneNumber": "",
#  "contactSecondaryPhonePrefix": "",
#  "contactSecondaryPhoneNumber": ""
# }
#
# property_dict["propertyAddress"] = {
#  "addressVisibility": data_dict["root"]["property"]["wi_data"]["type_es"],
#  "addressStreetName": data_dict["root"]["property"]["location_detail"],
#  "addressStreetNumber": "",
#  "addressBlock": "",
#  "addressFloor": "",
#  "addressStair": "",
#  "addressDoor": "",
#  "addressUrbanization": data_dict["root"]["property"]["town"],
#  "addressPostalCode": data_dict["root"]["property"]["wi_data"]["postalcode"],
#  "addressNsiCode": "",
#  "addressTown": data_dict["root"]["property"]["town"],
#  "addressCountry": data_dict["root"]["property"]["country"],
#  "addressCoordinatesPrecision": "exact",
#  "addressCoordinatesLatitude": data_dict["root"]["property"]["location"]["latitude"],
#  "addressCoordinatesLongitude": data_dict["root"]["property"]["location"]["longitude"]
# }
#
# property_dict["propertyFeatures"] = {
#  "featuresType": data_dict["root"]["property"]["type"],
#  "featuresAreaConstructed": data_dict["root"]["property"]["surface_area"]["built"],
#  "featuresAreaUsable": data_dict["root"]["property"]["surface_area"]["built"],
#  "featuresBathroomNumber": data_dict["root"]["property"]["baths"],
#  "featuresBedroomNumber": data_dict["root"]["property"]["beds"],
#  "featuresBuiltYear": "",
#  "featuresConditionedAir": "",
#  "featuresConservation": "",
#  "featuresDoorman": "",
#  "featuresEnergyCertificateRating": data_dict["root"]["property"]["energy_rating"]["consumption"],
#  "featuresEnergyCertificatePerformance": data_dict["root"]["property"]["energy_rating"]["emissions"],
#  "featuresGarden": "",
#  "featuresOrientationEast": "",
#  "featuresOrientationWest": "",
#  "featuresOrientationNorth": "",
#  "featuresOrientationSouth": "",
#  "featuresPenthouse": "",
#  "featuresPool": "",
#  "featuresRooms": data_dict["root"]["property"]["beds"],
#  "featuresStorage": "",
#  "featuresStudio": "",
#  "featuresTerrace": "",
#  "featuresWardrobes": "",
#  "featuresParkingAvailable": "",
#  "featuresHeatingType": ""
# }
#
# property_dict["propertyDescriptions"] = [
#  {
#    "descriptionLanguage": "spanish",
#    "descriptionText": data_dict["root"]["property"]["desc"]["es"]
#  },
#  {
#    "descriptionLanguage": "italian",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "portuguese",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "english",
#    "descriptionText":  data_dict["root"]["property"]["desc"]["en"]
#  },
#  {
#    "descriptionLanguage": "german",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "french",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "russian",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "chinese",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "catalan",
#    "descriptionText": ""
#  }
# ]
#
#
# # Mapea las imágenes
# property_dict["propertyImages"] = []
# for image in data_dict["root"]["property"]["images"]["image"]:
#   image_dict = {
#       "imageOrder": image["@id"],
#       "imageLabel": "property",
#       "imageUrl": image["url"]
#   }
#   property_dict["propertyImages"].append(image_dict)
#
# property_dict["propertyVideos"] = [
#  {
#    "videoOrder": 1,
#    "videoUrl": data_dict["root"]["property"]["video_url"]
#  }
# ]
#
# property_dict["propertyVirtualTours"] = {
#  "virtualTour3D": {
#    "virtualTour3DType": "",
#    "virtualTourUrl": ""
#  },
#  "virtualTour": {
#    "virtualTourType": "",
#    "virtualTourUrl": ""
#  }
# }
#
# property_dict["propertyUrl"] = data_dict["root"]["property"]["url"]["es"]
#
# # Agrega el diccionario de propiedad a la lista de propiedades
# json_dict["customerProperties"].append(property_dict)
#
# # Convierte el diccionario a JSON usando json.dumps()
# json_data = json.dumps(json_dict)
#
# # Escribe los datos JSON en un archivo de salida
# with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#  json_file.write(json_data)
#
#
#




#VERSION FINAL SIN REVISION DE TIPOS

# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "+34",
#  "contactPrimaryPhoneNumber": "931595880",
#  "contactSecondaryPhonePrefix": "",
#  "contactSecondaryPhoneNumber": ""
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#  property_dict["propertyOperation"] = {
#  "operationType": property.get("price_freq", ""),
#  "operationPrice": property.get("price", ""),
#  "operationPriceCommunity": "",
#  "operationPriceParking": ""
#  }
#
#  property_dict["propertyContact"] = {
#  "contactName": "",
#  "contactEmail": "",
#  "contactPrimaryPhonePrefix": "",
#  "contactPrimaryPhoneNumber": "",
#  "contactSecondaryPhonePrefix": "",
#  "contactSecondaryPhoneNumber": ""
#  }
#
#  property_dict["propertyAddress"] = {
#  "addressVisibility": property.get("wi_data", {}).get("type_es", ""),
#  "addressStreetName": property.get("location_detail", ""),
#  "addressStreetNumber": "",
#  "addressBlock": "",
#  "addressFloor": "",
#  "addressStair": "",
#  "addressDoor": "",
#  "addressUrbanization": property.get("town", ""),
#  "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#  "addressNsiCode": "",
#  "addressTown": property.get("town", ""),
#  "addressCountry": property.get("country", ""),
#  "addressCoordinatesPrecision": "exact",
#  "addressCoordinatesLatitude": property.get("location", {}).get("latitude", ""),
#  "addressCoordinatesLongitude": property.get("location", {}).get("longitude", "")
#  }
#
#  property_dict["propertyFeatures"] = {
#  "featuresType": property.get("type", ""),
#  "featuresAreaConstructed": property.get("surface_area", {}).get("built", ""),
#  "featuresAreaUsable": property.get("surface_area", {}).get("built", ""),
#  "featuresBathroomNumber": property.get("baths", ""),
#  "featuresBedroomNumber": property.get("beds", ""),
#  "featuresBuiltYear": "",
#  "featuresConditionedAir": "",
#  "featuresConservation": "",
#  "featuresDoorman": "",
#  "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#  "featuresEnergyCertificatePerformance": property.get("energy_rating", {}).get("emissions", ""),
#  "featuresGarden": "",
#  "featuresOrientationEast": "",
#  "featuresOrientationWest": "",
#  "featuresOrientationNorth": "",
#  "featuresOrientationSouth": "",
#  "featuresPenthouse": "",
#  "featuresPool": "",
#  "featuresRooms": property.get("beds", ""),
#  "featuresStorage": "",
#  "featuresStudio": "",
#  "featuresTerrace": "",
#  "featuresWardrobes": "",
#  "featuresParkingAvailable": "",
#  "featuresHeatingType": ""
#  }
#
#  property_dict["propertyDescriptions"] = [
#  {
#    "descriptionLanguage": "spanish",
#    "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#    "descriptionLanguage": "italian",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "portuguese",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "english",
#    "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  {
#    "descriptionLanguage": "german",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "french",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "russian",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "chinese",
#    "descriptionText": ""
#  },
#  {
#    "descriptionLanguage": "catalan",
#    "descriptionText": ""
#  }
#  ]
#
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#      try:
#          image_dict = {
#              "imageOrder": image.get("@id", ""),
#              "imageLabel": "property",
#              "imageUrl": image.get("url", "")
#          }
#          property_dict["propertyImages"].append(image_dict)
#      except AttributeError:
#          pass
#
#  property_dict["propertyVideos"] = [
#  {
#    "videoOrder": 1,
#    "videoUrl": property.get("video_url", "")
#  }
#  ]
#
#
#  property_dict["propertyVirtualTours"] = {
#   "virtualTour3D": {
#     "virtualTour3DType": "",
#     "virtualTourUrl": ""
#   },
#   "virtualTour": {
#     "virtualTourType": "",
#     "virtualTourUrl": ""
#   }
#  }
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#
#  # Agrega el diccionario de propiedad a la lista de propiedades
#  json_dict["customerProperties"].append(property_dict)
#
# # Convierte el diccionario a JSON usando json.dumps()
# json_data = json.dumps(json_dict)
#
# # Escribe los datos JSON en un archivo de salida
# with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#     json_file.write(json_data)
#
#




#VERSION FINAL REVISION DE TIPOS
# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = "Spain"
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "34",
#  "contactPrimaryPhoneNumber": "931595880",
#
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#
#
#  operationPrice = int(property.get("price", "") or 0)
#
#  property_dict["propertyOperation"] = {
#      "operationType": property.get("price_freq", ""),
#      "operationPrice": operationPrice,
#  }
#
#  addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#  addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#  property_dict["propertyAddress"] = {
#  "addressVisibility": property.get("wi_data", {}).get("type_es", ""),
#  "addressStreetName": property.get("location_detail", ""),
#  "addressUrbanization": property.get("town", ""),
#  "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#  "addressTown": property.get("town", ""),
#  "addressCountry": property.get("country", ""),
#  "addressCoordinatesPrecision": "exact",
#  "addressCoordinatesLatitude": addressCoordinatesLatitude,
#  "addressCoordinatesLongitude": addressCoordinatesLongitude,
#  }
#
#  type_value = property.get("type", "").lower()
#
#  if type_value in ["piso", "casa", "apartamento", "vivienda"]:
#      type_value = "flat"
#  elif type_value == "parking":
#      type_value = "garage"
#
#  featuresAreaConstructed = int(property.get("surface_area", {}).get("built", "") or 0)
#  featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0)
#  featuresAreaUsable = int(property.get("surface_area", {}).get("usable", "") or 0)
#  featuresBathroomNumber = int(property.get("baths", "") or 0)
#  featuresBedroomNumber = int(property.get("beds", "") or 0)
#
#
#  def convert_to_float(value):
#      try:
#          return float(value.replace(',', '.'))
#      except ValueError:
#          return 0.0
#
#
#  try:
#      featuresEnergyCertificatePerformance = convert_to_float(
#          property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#  except AttributeError:
#      print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#  featuresRooms = int(property.get("beds", "") or 0)
#
#  property_dict["propertyFeatures"] = {
#      "featuresType": type_value,
#      "featuresAreaConstructed": featuresAreaConstructed,
#      "featuresAreaUsable": featuresAreaUsable,
#      "featuresBathroomNumber": featuresBathroomNumber,
#      "featuresBedroomNumber": featuresBedroomNumber,
#      "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#      "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#      "featuresRooms": featuresRooms,
#  }
#
#  property_dict["propertyDescriptions"] = [
#  {
#    "descriptionLanguage": "spanish",
#    "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#    "descriptionLanguage": "english",
#    "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  ]
#
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#      try:
#          image_dict = {
#              "imageOrder": image.get("@id", ""),
#              # "imageLabel": "property",
#              "imageUrl": image.get("url", "")
#          }
#          property_dict["propertyImages"].append(image_dict)
#      except AttributeError:
#          pass
#
#  property_dict["propertyVideos"] = [
#  {
#    "videoOrder": 1,
#    "videoUrl": property.get("video_url", "")
#  }
#  ]
#
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#
#  # Agrega el diccionario de propiedad a la lista de propiedades
#  json_dict["customerProperties"].append(property_dict)
#
# # Convierte el diccionario a JSON usando json.dumps()
# json_data = json.dumps(json_dict)
#
# # Escribe los datos JSON en un archivo de salida
# with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#     json_file.write(json_data)



#VERSION 21-11-2023

# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = "Spain"
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "34",
#  "contactPrimaryPhoneNumber": "931595880",
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#  operationPrice = int(property.get("price", "") or 0)
#
#  property_dict["propertyOperation"] = {
#     "operationType": property.get("price_freq", ""),
#     "operationPrice": operationPrice,
#  }
#
#  addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#  addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#  property_dict["propertyAddress"] = {
#  "addressVisibility": "street",
#  "addressStreetName": property.get("location_detail", ""),
#  "addressUrbanization": property.get("town", ""),
#  "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#  "addressTown": property.get("town", ""),
#  "addressCountry": property.get("country", ""),
#  "addressCoordinatesPrecision": "exact",
#  "addressCoordinatesLatitude": addressCoordinatesLatitude,
#  "addressCoordinatesLongitude": addressCoordinatesLongitude,
#  }
#
#  type_value = property.get("type", "").lower()
#
#  if type_value in ["piso", "casa", "apartamento", "vivienda", "shop", "penthouse", "duplex", "land", "villa", "studio", "building", "industrial", "apartment", "mansion"]:
#     type_value = "flat"
#  elif type_value == "parking":
#     type_value = "garage"
#  elif type_value == "office":
#     type_value = "office"
#
#  featuresAreaConstructed = int(property.get("surface_area", {}).get("built", "") or 0)
#  featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0)
#  featuresAreaUsable = int(property.get("surface_area", {}).get("usable", "") or 0)
#  featuresBathroomNumber = int(property.get("baths", "") or 0)
#  featuresBedroomNumber = int(property.get("beds", "") or 0)
#
#  def convert_to_float(value):
#     try:
#         return float(value.replace(',', '.'))
#     except ValueError:
#         return 0.0
#
#  try:
#     featuresEnergyCertificatePerformance = convert_to_float(
#         property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#  except AttributeError:
#     print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#  featuresRooms = int(property.get("beds", "") or 0)
#
#  property_dict["propertyFeatures"] = {
#     "featuresType": type_value,
#     "featuresAreaConstructed": featuresAreaConstructed,
#     "featuresAreaUsable": featuresAreaUsable,
#     "featuresBathroomNumber": featuresBathroomNumber,
#     "featuresBedroomNumber": featuresBedroomNumber,
#     "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#     "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#     "featuresRooms": featuresRooms,
#  }
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de 0 o None
#  property_dict["propertyFeatures"] = {
#     key: value for key, value in property_dict["propertyFeatures"].items() if value != 0 and value is not None
#  }
#
#  property_dict["propertyDescriptions"] = [
#  {
#   "descriptionLanguage": "spanish",
#   "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#   "descriptionLanguage": "english",
#   "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  ]
#
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#     try:
#         image_dict = {
#             "imageOrder": int(image.get("@id", "")or 0),
#             # "imageLabel": "property",
#             "imageUrl": image.get("url", "")
#         }
#         property_dict["propertyImages"].append(image_dict)
#     except AttributeError:
#         pass
#
#  property_dict["propertyVideos"] = [
#  {
#   "videoOrder": 1,
#   "videoUrl": property.get("video_url", "")
#  }
#  ]
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#  # Agrega el diccionario de propiedad a la lista de propiedades
#  json_dict["customerProperties"].append(property_dict)
#
# # Convierte el diccionario a JSON usando json.dumps()
# json_data = json.dumps(json_dict)
#
# # Escribe los datos JSON en un archivo de salida
# with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#     json_file.write(json_data)





#ULTIMO CODIGO FUNCIONAL
# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = "Spain"
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "34",
#  "contactPrimaryPhoneNumber": "931595880",
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#  operationPrice = int(property.get("price", "") or 0)
#
#  property_dict["propertyOperation"] = {
#   "operationType": property.get("price_freq", ""),
#   "operationPrice": operationPrice,
#  }
#
#  # Cambia "month" a "sale" en "operationType"
#  if property_dict["propertyOperation"]["operationType"] == "month":
#   property_dict["propertyOperation"]["operationType"] = "sale"
#
#
#  addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#  addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#  property_dict["propertyAddress"] = {
#   "addressVisibility": "street",
#   "addressStreetName": property.get("location_detail", ""),
#   "addressUrbanization": property.get("town", ""),
#   "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#   "addressTown": property.get("town", ""),
#   "addressCountry": property.get("country", ""),
#   "addressCoordinatesPrecision": "exact",
#   "addressCoordinatesLatitude": addressCoordinatesLatitude,
#   "addressCoordinatesLongitude": addressCoordinatesLongitude,
#  }
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#  property_dict["propertyAddress"] = {k: v for k, v in property_dict["propertyAddress"].items() if v}
#
#
#
#
#  type_value = property.get("type", "").lower()
#
#  if type_value in ["piso", "casa", "apartamento", "vivienda", "shop", "penthouse", "duplex", "land", "villa", "studio",
#                    "building", "industrial", "apartment", "mansion"]:
#   type_value = "flat"
#  elif type_value == "parking":
#   type_value = "garage"
#  elif type_value == "office":
#   type_value = "office"
#
#  featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get("surface_area",{}).get("built") else None
#  featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get("surface_area", {}).get("plot") else None
#  featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
#  featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1
#
#
#  def convert_to_float(value):
#   try:
#    return float(value.replace(',', '.'))
#   except ValueError:
#    return 0.0
#
#
#  try:
#   featuresEnergyCertificatePerformance = convert_to_float(property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#
#  except AttributeError:
#   print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#  featuresRooms = int(property.get("beds", "")) if property.get("beds") else 1
#
#  featuresAreaUsable = property.get("surface_area", {}).get("usable", None)
#
#  property_dict["propertyFeatures"] = {
#   "featuresType": type_value,
#   "featuresAreaConstructed": featuresAreaConstructed,
#   "featuresAreaUsable": featuresAreaUsable,
#   "featuresBathroomNumber": featuresBathroomNumber,
#   "featuresBedroomNumber": featuresBedroomNumber,
#   "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#   "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#   "featuresRooms": featuresRooms,
#  }
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1))
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1))
#
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresRooms"] = int(property_dict["propertyFeatures"].get("featuresRooms", 1)) or 1
#   property_dict["propertyFeatures"]["featuresAreaConstructed"] = int(property_dict["propertyFeatures"].get("featuresAreaConstructed")) if property_dict["propertyFeatures"].get("featuresAreaConstructed") is not None else 1
#
#
#  # Si la propiedad no es de tipo "flat", elimina los campos featuresBathroomNumber, featuresBedroomNumber y featuresRooms
#  if type_value != "flat":
#   property_dict["propertyFeatures"].pop("featuresBathroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresBedroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresRooms", None)
#
#  # Elimina los campos con valor None en "propertyFeatures"
#  property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None}
#
#
#  property_dict["propertyDescriptions"] = [
#  {
#  "descriptionLanguage": "spanish",
#  "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#  "descriptionLanguage": "english",
#  "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  ]
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#     try:
#         image_dict = {
#             "imageOrder": int(image.get("@id", "")or 0),
#             # "imageLabel": "property",
#             "imageUrl": image.get("url", "")
#         }
#         property_dict["propertyImages"].append(image_dict)
#     except AttributeError:
#         pass
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#  property_dict["propertyVideos"] = [
#   {
#    "videoOrder": 1,
#    "videoUrl": property.get("video_url", "")
#   }
#  ]
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#  property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict["propertyVideos"]]
#
#  # Agrega el diccionario de propiedad a la lista de propiedades
#  json_dict["customerProperties"].append(property_dict)
#
#  # Convierte el diccionario a JSON usando json.dumps()
#  json_data = json.dumps(json_dict)
#
#  # Escribe los datos JSON en un archivo de salida
#  with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#   json_file.write(json_data)
#




# import json
# import xmltodict
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = "Spain"
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "34",
#  "contactPrimaryPhoneNumber": "931595880",
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#  operationPrice = int(property.get("price", "") or 0)
#
#  property_dict["propertyOperation"] = {
#   "operationType": property.get("price_freq", ""),
#   "operationPrice": operationPrice,
#  }
#
#  # Cambia "month" a "sale" en "operationType"
#  if property_dict["propertyOperation"]["operationType"] == "month":
#   property_dict["propertyOperation"]["operationType"] = "sale"
#
#
#  addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#  addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#  property_dict["propertyAddress"] = {
#   "addressVisibility": "street",
#   "addressStreetName": property.get("location_detail", ""),
#   "addressUrbanization": property.get("town", ""),
#   "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#   "addressTown": property.get("town", ""),
#   "addressCountry": property.get("country", ""),
#   "addressCoordinatesPrecision": "exact",
#   "addressCoordinatesLatitude": addressCoordinatesLatitude,
#   "addressCoordinatesLongitude": addressCoordinatesLongitude,
#  }
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#  property_dict["propertyAddress"] = {k: v for k, v in property_dict["propertyAddress"].items() if v}
#
#  type_value = property.get("type", "").lower()
#
#  if type_value in ["piso", "casa", "apartamento", "vivienda", "penthouse", "duplex", "villa", "studio",
#                    "building", "industrial", "apartment", "mansion"]:
#      type_value = "flat"
#  elif type_value == "parking":
#      type_value = "garage"
#  elif type_value == "office":
#      type_value = "office"
#  elif type_value == "terreno":
#      type_value = "land"
#  elif type_value == "shop":
#      type_value = "premises"
#
#  featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get(
#      "surface_area", {}).get("built") else None
#  featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get(
#      "surface_area", {}).get("plot") else None
#  featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
#  featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1
#
#  # Lógica para land
#  if type_value == "land":
#      # Verifica si featuresAreaPlot tiene un valor no nulo y no es 0
#      if featuresAreaPlot is not None and featuresAreaPlot != 0:
#          property_dict["propertyFeatures"] = {
#              "featuresType": type_value,
#              "featuresAreaConstructed": featuresAreaConstructed,
#              "featuresAreaPlot": featuresAreaPlot,
#          }
#  else:
#      # Lógica para otros tipos de propiedad
#      property_dict["propertyFeatures"] = {
#          "featuresType": type_value,
#          "featuresAreaConstructed": featuresAreaConstructed,
#          "featuresAreaPlot": featuresAreaPlot,
#          "featuresBathroomNumber": featuresBathroomNumber,
#          "featuresBedroomNumber": featuresBedroomNumber,
#      }
#
#      # Elimina los campos con valor None o cero en "propertyFeatures"
#      property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if
#                                           v is not None and v != 0}
#
#  # Si featuresAreaConstructed es 1 o featuresAreaPlot es 0, salta la adición de property_dict a json_dict["customerProperties"]
#  if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1 and property_dict["propertyFeatures"].get("featuresAreaPlot") != 0:
#      json_dict["customerProperties"].append(property_dict)
#
#
#
#
#  def convert_to_float(value):
#   try:
#    return float(value.replace(',', '.'))
#   except ValueError:
#    return 0.0
#
#
#  try:
#   featuresEnergyCertificatePerformance = convert_to_float(property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#
#  except AttributeError:
#   print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#  featuresRooms = int(property.get("beds", "")) if property.get("beds") else 1
#  featuresAreaUsable = property.get("surface_area", {}).get("usable", None)
#
#  # property_dict["propertyFeatures"] = {
#  #  "featuresType": type_value,
#  #  "featuresAreaConstructed": featuresAreaConstructed,
#  #  "featuresAreaUsable": featuresAreaPlot,
#  #  "featuresBathroomNumber": featuresBathroomNumber,
#  #  "featuresBedroomNumber": featuresBedroomNumber,
#  #  "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#  #  "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#  #  "featuresRooms": featuresRooms,
#  # }
#
#  property_dict["propertyFeatures"] = {
#      "featuresType": type_value,
#      "featuresAreaConstructed": featuresAreaConstructed,
#      "featuresBathroomNumber": featuresBathroomNumber,
#      "featuresBedroomNumber": featuresBedroomNumber,
#      "featuresEnergyCertificateRating": property.get("energy_rating", {}).get("consumption", ""),
#      "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#      "featuresRooms": featuresRooms,
#  }
#
#  # Agrega featuresAreaPlot solo si la propiedad es de tipo "land"
#  if type_value == "land" and featuresAreaPlot is not None and featuresAreaPlot != 0:
#      property_dict["propertyFeatures"]["featuresAreaPlot"] = featuresAreaPlot
#  elif "featuresAreaPlot" in property_dict["propertyFeatures"]:
#      del property_dict["propertyFeatures"]["featuresAreaPlot"]
#
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1))
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1))
#
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresRooms"] = int(property_dict["propertyFeatures"].get("featuresRooms", 1)) or 1
#   property_dict["propertyFeatures"]["featuresAreaConstructed"] = int(property_dict["propertyFeatures"].get("featuresAreaConstructed")) if property_dict["propertyFeatures"].get("featuresAreaConstructed") is not None else 1
#
#
#  # Si la propiedad no es de tipo "flat", elimina los campos featuresBathroomNumber, featuresBedroomNumber y featuresRooms
#  if type_value != "flat":
#   property_dict["propertyFeatures"].pop("featuresBathroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresBedroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresRooms", None)
#
#  # Elimina los campos con valor None en "propertyFeatures"
#  property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None}
#
#
#
#  property_dict["propertyDescriptions"] = [
#  {
#  "descriptionLanguage": "spanish",
#  "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#  "descriptionLanguage": "english",
#  "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  ]
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#     try:
#         image_dict = {
#             "imageOrder": int(image.get("@id", "")or 0),
#             # "imageLabel": "property",
#             "imageUrl": image.get("url", "")
#         }
#         property_dict["propertyImages"].append(image_dict)
#     except AttributeError:
#         pass
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#  # property_dict["propertyVideos"] = [
#  #  {
#  #   "videoOrder": 1,
#  #   "videoUrl": property.get("video_url", "")
#  #  }
#  # ]
#
#  video_url = property.get("video_url", "")
#  if video_url:  # Si videoUrl no está vacío
#   property_dict["propertyVideos"] = [
#    {
#     "videoOrder": 1,
#     "videoUrl": video_url
#    }
#   ]
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#  # property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict["propertyVideos"]]
#  if 'propertyVideos' in property_dict:
#      property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict.get("propertyVideos", [])]
#
#
#
#  # Si featuresAreaConstructed es 1, salta la adición de property_dict a json_dict["customerProperties"]
#  if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1:
#   json_dict["customerProperties"].append(property_dict)
#
#  # Agrega el diccionario de propiedad a la lista de propiedades
#  # json_dict["customerProperties"].append(property_dict)
#
#  # Convierte el diccionario a JSON usando json.dumps()
#  json_data = json.dumps(json_dict)
#
#
#
#  # Escribe los datos JSON en un archivo de salida
#  with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#   json_file.write(json_data)
#
#
#



# import requests
# import time
# from xml.etree.ElementTree import fromstring
# import json
# import xmltodict
# import re
# from ftplib import FTP
# import json
# import xmltodict
#
#
# def remove_postal_code(address):
#  pattern = r'\b\d{5}\b,?$'
#  address = re.sub(pattern, '', address)
#  return address.rstrip(', ')
#
#
# def download_xml(url, save_path):
#  response = requests.get(url)
#  with open(save_path, 'wb') as xml_file:
#   xml_file.write(response.content)
#
# # Configuración del enlace XML y el temporizador (40 minutos = 2400 segundos)
# xml_url = 'https://app.witei.com/pro/interconnection/xml/d1e8a7f70b7e4546/'
# download_interval = 2400
#
# while True:
#  try:
#   # Descarga el archivo XML
#   xml_file_path = 'archivo.xml'
#   download_xml(xml_url, xml_file_path)
#
#   # ... (código existente para la conversión XML a JSON y transferencia FTP)
#
#   print('Proceso completado con éxito.')
#
#  except Exception as e:
#   print(f"Error en el proceso: {e}")
#
#  # Espera antes de volver a descargar el archivo XML
#  time.sleep(download_interval)
#
# #DESDE AQUI EMPIEZA LA TRANSFORMACION EN JSON
#
# # Abre el archivo XML y lee los datos en forma de un diccionario de Python usando xmltodict
# with open("d1e8a7f70b7e4546.xml", 'r', encoding='utf-8') as xml_file:
#  data_dict = xmltodict.parse(xml_file.read())
#
# # Crea un nuevo diccionario para el JSON
# json_dict = {}
#
# # Mapea los campos XML a los campos JSON
# json_dict["customerCountry"] = "Spain"
# json_dict["customerCode"] = "ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1" # Reemplaza con tu propio código
# json_dict["customerReference"] = "Witei" # Reemplaza con tu propia referencia
# json_dict["customerContact"] = {
#  "contactName": "HannanPiper",
#  "contactEmail": "info@hannanpiper.com",
#  "contactPrimaryPhonePrefix": "34",
#  "contactPrimaryPhoneNumber": "931595880",
# }
#
# # Mapea los campos restantes
# json_dict["customerProperties"] = []
#
# # Itera sobre cada propiedad en la lista
# for property in data_dict["root"]["property"]:
#  property_dict = {}
#
#  property_dict["propertyCode"] = property.get("id", "")
#  property_dict["propertyReference"] = property.get("ref", "")
#  property_dict["propertyVisibility"] = "idealista"
#
#  operationPrice = int(property.get("price", "") or 0)
#
#  property_dict["propertyOperation"] = {
#   "operationType": property.get("price_freq", ""),
#   "operationPrice": operationPrice,
#  }
#
#  # Cambia "month" a "sale" en "operationType"
#  if property_dict["propertyOperation"]["operationType"] == "month":
#   property_dict["propertyOperation"]["operationType"] = "sale"
#
#
#  addressCoordinatesLatitude = float(property.get("location", {}).get("latitude", "") or 0)
#  addressCoordinatesLongitude = float(property.get("location", {}).get("longitude", "") or 0)
#
#  property_dict["propertyAddress"] = {
#   "addressVisibility": "street",
#   "addressStreetName": property.get("location_detail", ""),
#   "addressUrbanization": property.get("town", ""),
#   "addressPostalCode": property.get("wi_data", {}).get("postalcode", ""),
#   "addressTown": property.get("town", ""),
#   "addressCountry": property.get("country", ""),
#   "addressCoordinatesPrecision": "exact",
#   "addressCoordinatesLatitude": addressCoordinatesLatitude,
#   "addressCoordinatesLongitude": addressCoordinatesLongitude,
#  }
#
#  if property_dict["propertyAddress"]["addressStreetName"] is not None:
#   property_dict["propertyAddress"]["addressStreetName"] = remove_postal_code(property_dict["propertyAddress"]["addressStreetName"])
#
#
#  # Crea un nuevo diccionario que solo incluya los campos que tienen un valor distinto de None o vacío
#  property_dict["propertyAddress"] = {k: v for k, v in property_dict["propertyAddress"].items() if v}
#
#
#  type_value = property.get("type", "").lower()
#
#  if type_value in ["piso", "casa", "apartamento", "vivienda", "shop", "penthouse", "duplex", "land", "villa", "studio",
#                    "building", "industrial", "apartment", "mansion"]:
#   type_value = "flat"
#  elif type_value == "parking":
#   type_value = "garage"
#  elif type_value == "office":
#   type_value = "office"
#
#  featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get("surface_area",{}).get("built") else None
#  featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get("surface_area", {}).get("plot") else None
#  featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
#  featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1
#
#
#  # Lógica para land
#  if type_value == "land":
#      property_dict["propertyFeatures"] = {
#          "featuresType": type_value,
#          "featuresAreaConstructed": featuresAreaConstructed,
#          "featuresAreaUsable": featuresAreaPlot,
#      }
#  else:
#      # Lógica para otros tipos de propiedad
#      property_dict["propertyFeatures"] = {
#          "featuresType": type_value,
#          "featuresAreaConstructed": featuresAreaConstructed,
#          "featuresAreaUsable": featuresAreaUsable,
#          "featuresBathroomNumber": featuresBathroomNumber,
#          "featuresBedroomNumber": featuresBedroomNumber,
#          # ... (otros campos específicos para otros tipos de propiedad)
#      }
#
#      # Elimina los campos con valor None o cero en "propertyFeatures"
#      property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if
#                                           v is not None and v != 0}
#
#  # ...
#
#  # Si featuresAreaConstructed es 1 o featuresAreaPlot es 0, salta la adición de property_dict a json_dict["customerProperties"]
#  if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1 and property_dict["propertyFeatures"].get(
#          "featuresAreaUsable") != 0:
#      json_dict["customerProperties"].append(property_dict)
#
#
#
#  def convert_to_float(value):
#   try:
#    return float(value.replace(',', '.'))
#   except ValueError:
#    return 0.0
#
#
#  try:
#   featuresEnergyCertificatePerformance = convert_to_float(
#    property.get("wi_data", {}).get("energy_rating_values", "").get("consumption_value", ""))
#  except AttributeError:
#   print("El valor devuelto por property.get('wi_data', {}) no es un diccionario.")
#
#  if featuresEnergyCertificatePerformance == 999:
#   featuresEnergyCertificatePerformance = None
#
#
#  featuresRooms = int(property.get("beds", "")) if property.get("beds") else 1
#  featuresAreaUsable = property.get("surface_area", {}).get("usable", None)
#  energy_rating = property.get("energy_rating", {}).get("consumption", "")
#
#  if energy_rating != "X":
#   property_dict["propertyFeatures"] = {
#    "featuresType": type_value,
#    "featuresAreaConstructed": featuresAreaConstructed,
#    "featuresAreaUsable": featuresAreaPlot,
#    "featuresBathroomNumber": featuresBathroomNumber,
#    "featuresBedroomNumber": featuresBedroomNumber,
#    "featuresEnergyCertificateRating": energy_rating,
#    "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#    "featuresRooms": featuresRooms,
#   }
#  else:
#   property_dict["propertyFeatures"] = {
#    "featuresType": type_value,
#    "featuresAreaConstructed": featuresAreaConstructed,
#    "featuresAreaUsable": featuresAreaUsable,
#    "featuresBathroomNumber": featuresBathroomNumber,
#    "featuresBedroomNumber": featuresBedroomNumber,
#    "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#    "featuresRooms": featuresRooms,
#   }
#
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1))
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1))
#
#
#  # Si la propiedad es de tipo "flat", establece "featuresBathroomNumber" y "featuresBedroomNumber" en 1 si sus valores son None, 0, o null
#  if type_value == "flat":
#   property_dict["propertyFeatures"]["featuresBathroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBathroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresBedroomNumber"] = int(property_dict["propertyFeatures"].get("featuresBedroomNumber", 1)) or 1
#   property_dict["propertyFeatures"]["featuresRooms"] = int(property_dict["propertyFeatures"].get("featuresRooms", 1)) or 1
#   property_dict["propertyFeatures"]["featuresAreaConstructed"] = int(property_dict["propertyFeatures"].get("featuresAreaConstructed")) if property_dict["propertyFeatures"].get("featuresAreaConstructed") is not None else 1
#
#
#  # Si la propiedad no es de tipo "flat", elimina los campos featuresBathroomNumber, featuresBedroomNumber y featuresRooms
#  if type_value != "flat":
#   property_dict["propertyFeatures"].pop("featuresBathroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresBedroomNumber", None)
#   property_dict["propertyFeatures"].pop("featuresRooms", None)
#
#  # Elimina los campos con valor None en "propertyFeatures"
#  property_dict["propertyFeatures"] = {k: v for k, v in property_dict["propertyFeatures"].items() if v is not None}
#
#
#
#  property_dict["propertyDescriptions"] = [
#  {
#  "descriptionLanguage": "spanish",
#  "descriptionText": property.get("desc", {}).get("es", "")
#  },
#  {
#  "descriptionLanguage": "english",
#  "descriptionText": property.get("desc", {}).get("en", "")
#  },
#  ]
#  property_dict["propertyImages"] = []
#  for image in property.get("images", {}).get("image", []):
#     try:
#         image_dict = {
#             "imageOrder": int(image.get("@id", "")or 0),
#             # "imageLabel": "property",
#             "imageUrl": image.get("url", "")
#         }
#         property_dict["propertyImages"].append(image_dict)
#     except AttributeError:
#         pass
#
#  property_dict["propertyUrl"] = property.get("url", {}).get("es", "")
#
#  video_url = property.get("video_url", "")
#  if video_url:  # Si videoUrl no está vacío
#   property_dict["propertyVideos"] = [
#    {
#     "videoOrder": 1,
#     "videoUrl": video_url
#    }
#   ]
#
#  if 'propertyVideos' in property_dict:
#        property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in property_dict["propertyVideos"]]
#
#  # Si featuresAreaConstructed es 1, salta la adición de property_dict a json_dict["customerProperties"]
#  if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1:
#   json_dict["customerProperties"].append(property_dict)
#
#  # Convierte el diccionario a JSON usando json.dumps()
#  json_data = json.dumps(json_dict)
#
#
#  # Escribe los datos JSON en un archivo de salida
#  with open("ilcc1ed9c9a4cff4a9ab424c5dd980602de9fac50c1.json", "w") as json_file:
#   json_file.write(json_data)
#
#











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
#      "contactEmail": "info@hannanpiper.com",
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
#       "operationType": property.get("price_freq", ""),
#       "operationPrice": operationPrice,
#      }
#
#      # Cambia "month" a "sale" en "operationType"
#      if property_dict["propertyOperation"]["operationType"] == "month":
#       property_dict["propertyOperation"]["operationType"] = "sale"
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
#      type_value = property.get("type", "").lower()
#
#      if type_value in ["piso", "casa", "apartamento", "vivienda", "shop", "penthouse", "duplex", "land", "villa",
#                        "studio",
#                        "building", "industrial", "apartment", "mansion"]:
#       type_value = "flat"
#      elif type_value == "parking":
#       type_value = "garage"
#      elif type_value == "office":
#       type_value = "office"
#
#      featuresAreaConstructed = int(property.get("surface_area", {}).get("built", 1)) if property.get("surface_area",
#                                                                                                      {}).get(
#       "built") else None
#      featuresAreaPlot = int(property.get("surface_area", {}).get("plot", "") or 0) if property.get("surface_area",
#                                                                                                    {}).get(
#       "plot") else None
#      featuresBathroomNumber = int(property.get("baths", "") or 0) if property.get("baths") else 1
#      featuresBedroomNumber = int(property.get("beds", "") or 0) if property.get("beds") else 1
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
#      if featuresEnergyCertificatePerformance == 999:
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
#        "featuresAreaUsable": featuresAreaUsable,
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
#        "featuresAreaUsable": featuresAreaUsable,
#        "featuresBathroomNumber": featuresBathroomNumber,
#        "featuresBedroomNumber": featuresBedroomNumber,
#        "featuresEnergyCertificatePerformance": featuresEnergyCertificatePerformance,
#        "featuresRooms": featuresRooms,
#       }
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
#       {
#        "descriptionLanguage": "spanish",
#        "descriptionText": property.get("desc", {}).get("es", "")
#       },
#       {
#        "descriptionLanguage": "english",
#        "descriptionText": property.get("desc", {}).get("en", "")
#       },
#      ]
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
#       property_dict["propertyVideos"] = [{k: v for k, v in video.items() if v} for video in
#                                          property_dict["propertyVideos"]]
#
#      # Si featuresAreaConstructed es 1, salta la adición de property_dict a json_dict["customerProperties"]
#      if property_dict["propertyFeatures"].get("featuresAreaConstructed") != 1:
#       json_dict["customerProperties"].append(property_dict)
#
#     return json_dict
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
# download_interval = 2400
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
#         # Guarda una copia del archivo JSON con un nombre diferente
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
     "contactEmail": "info@hannanpiper.com",
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

     # Cambia "month" a "sale" en "operationType"
     if property_dict["propertyOperation"]["operationType"] == "month":
      property_dict["propertyOperation"]["operationType"] = "sale"

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

     if type_value in ["piso", "casa", "apartamento", "vivienda", "penthouse", "duplex", "villa", "studio",
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
     ]
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

    return json_dict

def upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path):
    with FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd(ftp_destination_folder)
        with open(json_file_path, 'rb') as file:
            ftp.storbinary('STOR ' + json_file_path, file)

# Configuración del enlace XML y el temporizador (40 minutos = 2400 segundos)
xml_url = 'https://app.witei.com/pro/interconnection/xml/d1e8a7f70b7e4546/'
download_interval = 2400

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

        # Guarda una copia del archivo JSON con un nombre diferente
        json_copy_path = 'copia_' + json_file_path
        with open(json_copy_path, "w") as json_copy_file:
         json_copy_file.write(json_data)

        # Sube el archivo JSON por FTP
        upload_json_via_ftp(json_data, ftp_host, ftp_user, ftp_password, ftp_destination_folder, json_file_path)

        print('Proceso completado con éxito.')

    except Exception as e:
        print(f"Error en el proceso: {e}")

    # Espera antes de volver a descargar el archivo XML
    time.sleep(download_interval)
