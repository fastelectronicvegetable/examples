
import os
import numpy as np
import PIL
import clip
from PIL import Image
import torch
from .. import CLIPTextEncoder

cur_dir = os.path.dirname(os.path.abspath(__file__))

def test_clip_available_models():

    models = ['ViT-B/32', 'RN50']
    for model in models:
        _,_ = clip.load(model)

def test_clip_text_encoder():

    text = 'Han likes eating pizza'
    device='cpu'

    encoder = CLIPTextEncoder()
    embeddeding_np = encoder.encode(text)
    expected = np.load(os.path.join(cur_dir, 'expected.npy'))
    np.testing.assert_almost_equal(embeddeding_np, expected)

def test_clip_text_encoder_batch():

    text = np.array(['Han likes eating pizza', 'Han likes pizza'])
    device='cpu'

    encoder = CLIPTextEncoder()
    embeddeding_np = encoder.encode(text)
    expected = np.load(os.path.join(cur_dir, 'expected.npy'))
    np.testing.assert_almost_equal(embeddeding_np, expected)
