from lightkurve import search_targetpixelfile

pixefile = search_targetpixelfile("Kepler-553 c").download(quality_bitmask='hardest')

pixelfile.plot(frame=1)