from tempo.serve.model import Model
from tempo.serve.metadata import ModelFramework
import numpy as np

def test_default_types():
    model = Model("mymodel",local_folder="",uri="",platform=ModelFramework.SKLearn)
    assert len(model.model_spec.model_details.inputs) == 1
    assert model.model_spec.model_details.inputs[0] == np.ndarray
    assert len(model.model_spec.model_details.outputs) == 1
    assert model.model_spec.model_details.outputs[0] == np.ndarray