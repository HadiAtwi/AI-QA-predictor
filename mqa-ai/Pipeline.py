from SLDVProcessor import SLDVProcessor
from FileHandler import FileHandler
from GraphBuilder import GraphBuilder
from EmbeddingGenerator import EmbeddingGenerator
from ModelPredictor import ModelPredictor

class Pipeline:
    def __init__(self, exe_path, slx_path, findings_list, rf_model_path, mlp_model_path):
        self.sldv_processor = SLDVProcessor(exe_path, slx_path, findings_list)
        self.rf_model_path = rf_model_path
        self.mlp_model_path = mlp_model_path

    def run(self, create_from_scratch=True, use_rf=True, use_mlp=False):
        if create_from_scratch:
            self.sldv_processor.run()
            data = FileHandler.read_json("C:\\Users\\hatwi\\Documents\\Thesis development environment\\Slice files\\NVEM2_evaluation_data.json")
            graph_builder = GraphBuilder(data)
            graphs, labels = graph_builder.build_graphs()
            emb_gen = EmbeddingGenerator()
            embeddings = emb_gen.generate_embeddings(graphs)
            FileHandler.save_pickle('embeddings.pkl', embeddings)
            FileHandler.save_pickle('labels.pkl', labels)
        else:
            embeddings = FileHandler.load_pickle('embeddings.pkl')
            labels = FileHandler.load_pickle('labels.pkl')

        if use_rf:
            predictor = ModelPredictor(embeddings, self.rf_model_path)
            predictions = predictor.predict_with_rf()
            FileHandler.write_json("predictions_rf.json", {"predictions": predictions})

        if use_mlp:
            predictor = ModelPredictor(embeddings, self.mlp_model_path)
            predictions = predictor.predict_with_mlp()
            FileHandler.write_json("predictions_mlp.json", {"predictions": predictions})
