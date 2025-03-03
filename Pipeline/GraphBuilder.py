import networkx as nx
import numpy as np

class GraphBuilder:
    def __init__(self, data):
        self.data = data
        self.graphs = []
        self.labels = []

    def build_graphs(self):
        for data_index, block_slice in self.data.items():
            label = int(data_index.split(',')[1])
            self.labels.append(label)
            G = nx.DiGraph()
            sid_to_index = {}
            index_counter = 0
            all_sids = {block['SID'] for block in block_slice}
            main_block = block_slice[-1]

            def add_node(sid, block):
                node_index = sid_to_index.setdefault(sid, index_counter)
                G.add_node(node_index, **{k: block.get('PropertyDict', {}).get(k, '') for k in [
                    'OutputSignals', 'OutDataTypeStr', 'OutputDataType', 'UpperLimit', 'LowerLimit',
                    'OutMin', 'OutMax', 'Function', 'IntegrationMethod', 'SampleTime', 'LimitOutput',
                    'UpperSaturationLimit', 'LowerSaturationLimit', 'ICPrevOutput', 'ICPrevScaledInput', 'Operator'
                ]}, SID=sid, BlockType=block['BlockType'], Name=block['Name'],
                   is_main=(block['SID'] == main_block['SID']), SliceSize=len(block_slice) if block['SID'] == main_block['SID'] else None)

            for block in block_slice:
                add_node(block['SID'], block)
                for neighbor in block['DestinationBlockSIDs'] + block['SourceBlockSIDs']:
                    if neighbor in all_sids:
                        add_node(neighbor, next(b for b in block_slice if b['SID'] == neighbor))
                        G.add_edge(sid_to_index[block['SID']], sid_to_index[neighbor])

            self.graphs.append(G)
        return self.graphs, np.array(self.labels)
