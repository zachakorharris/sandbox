import imageio, os, sys
images = []
filenames = []

for filename in os.listdir('polkadots'):
    print filename
    images.append(imageio.imread('polkadots/' + filename))

imageio.mimsave('test.gif', images,fps=120)
