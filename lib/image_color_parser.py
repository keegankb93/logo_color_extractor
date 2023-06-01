from typing import Dict
from PIL import Image
from collections import Counter, OrderedDict
import io
import colorsys
from sklearn.cluster import KMeans
import numpy as np


class ImageColorParser:
    def __init__(self, image):
        self.image = image
        self.image_binary = Image.open(io.BytesIO(self.image.file.read()))
        self.pixel_data = list(self.image_binary.getdata())
        self.pixel_color_count = Counter(self.pixel_data)

    def sort_by_most_common(self) -> OrderedDict[str, int]:
        return OrderedDict(self.pixel_color_count.most_common())

    def calculate_color_commonality(self, num_colors):
        color_data = np.array(self.pixel_data)
        normalized_color_data = color_data / 255.0
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        kmeans.fit(normalized_color_data)
        centroids = kmeans.cluster_centers_
        denormalized_centroids = centroids * 255.0
        distances = np.linalg.norm(centroids, axis=1)
        return [x for _, x in sorted(zip(distances, denormalized_centroids), reverse=True)]

    def get_common_colors(self, num_colors=5) -> Dict[str, str]:
        colors: Dict[str: str] = {}

        for idx, common_color in enumerate(self.calculate_color_commonality(num_colors)):
            if idx == num_colors + 1:
                break
            rgb = np.char.mod('%d', common_color)
            print(rgb)
            colors[f"color{idx}"] = f"rgba({','.join(rgb)})"

        return colors
