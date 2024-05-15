import random
from copy import deepcopy
import json

from pygeoapi.process import hello_world
from pygeoapi.process.base import ProcessorExecuteError

random.seed()

PROCESS_METADATA = deepcopy(hello_world.PROCESS_METADATA)

PROCESS_METADATA["id"] = "hello-geo-world"
PROCESS_METADATA["title"]["en"] = "Hello GeoWorld"
PROCESS_METADATA["outputs"] = {
    "echo": {
        "title": "Hello, world",
        "description": 'A "hello world" echo with the name and (optional)'
        " message submitted for processing",
        "schema": {
            "type": "object",
            "contentMediaType": "application/json",
            "format": "FeatureGeoJSON",
            "$ref": "https://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/featureCollectionGeoJSON.yaml",
        },
    }
}


class HelloGeoWorldProcessor(hello_world.HelloWorldProcessor):

    def _random_point_coordinates(self):
        random_x = round(random.uniform(9.945, 10.04), 3)
        random_y = round(random.uniform(53.475, 53.541), 3)

        return {"type": "Point", "coordinates": [random_y, random_x]}

    def execute(self, data):
        mimetype = "application/json"
        name = data.get("name")

        if name is None:
            raise ProcessorExecuteError("Cannot process without a name")

        message = data.get("message", "")
        value = f"Hello {name}! {message}".strip()

        outputs = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "id": f"echo_{name}",
                    "geometry": self._random_point_coordinates(),
                    "properties": {
                        "name": "echo",
                        "value": value,
                    },
                }
            ],
        }

        return mimetype, outputs


class HelloGeoWorldCmd():

    def __init__(self):
        pass

    def _random_point_coordinates(self):
        random_x = round(random.uniform(9.945, 10.04), 3)
        random_y = round(random.uniform(53.475, 53.541), 3)

        return {"type": "Point", "coordinates": [random_y, random_x]}


    def execute(self, data):
        
        data: dict = json.loads(data)
        
        name = data.get("inputs").get("name")

        if name is None:
            raise ProcessorExecuteError("Cannot process without a name")

        message = data.get("message", "")
        value = f"Hello {name}! {message}".strip()

        outputs = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "id": f"echo_{name}",
                    "geometry": self._random_point_coordinates(),
                    "properties": {
                        "name": "echo",
                        "value": value,
                    },
                }
            ],
        }

        return outputs
