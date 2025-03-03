import numpy as np
from karateclub import Graph2Vec

class EmbeddingGenerator:
    def __init__(self, dimensions=128, wl_iterations=4, epochs=5000, learning_rate=0.5):
        self.model = Graph2Vec(dimensions=dimensions, wl_iterations=wl_iterations, epochs=epochs, learning_rate=learning_rate)

    def generate_embeddings(self, graphs):
        self.model.fit(graphs)
        return np.array(self.model.get_embedding())
