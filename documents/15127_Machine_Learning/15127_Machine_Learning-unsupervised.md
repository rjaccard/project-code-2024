#  Unsupervised Learning 

## Unsupervised Learning

How can systems learn when there are no labels available?
How to learn a meaningful internal representation for data examples? I.e., to represent them in a way that reflects the semantic structure of the overall collection of input patterns?
This question is the central focus of unsupervised learning.

In unsupervised learning, our data consists only of features (or inputs) x1, x2, . . . , xN, vectors in RD, and
there are no outputs yn available.

Unsupervised learning seems to play an important role in how living beings learn. Variants of it seem to be more common in the brain than supervised learning.

Two main directions in unsupervised learning are
- representation learning and 
- density estimation & generative models

## Examples

- Given ratings of movies and viewers, we use matrix factorization to extract useful features (see e.g. Netflix Prize).
- Learning word-representations using matrix-factorizations, word2vec (Mikolov et al. 2013).
- Given voting patterns of regions across Switzerland, we use PCA to extract useful features (Etter et al. 2014).

## Unsupervised Representation Learning & Generation 

**How Does It Work?** : Define A Unsupervised Or Self-Supervised Loss Function, For

- Compression & Reconstruction (e.g. Auto-Encoder)

- Consistency & Contrastive Learning (e.g. Noise-contrastive estimation)

- Generation (e.g. Auto-Encoder, Gaussian Mixture Model)

- Auto-Encoders (G) : Invertible networks, learned compression, normalizing flows

- Representation Learning, e.g. images, text, time-series, video. 

- Combining unsupervised representation learning (pre-training) with supervised learning

- Language Models & Sequence Models (G) : text generation, or sequence continuation, BERT video, audio & timeseries (auto-regressive, contrastive, ...)

- Generative Adversarial Networks (GAN) (G)

- Contrastive image-language pretraining (CLIP) : learns a joint representation space for images and text using contrastive learning

- Diffusion models (G) : new state-of-the-art in image generation; these models can be adapted to generate images from text prompts (e.g., DALL-E 2, Stable Diffusion, Midjourney)