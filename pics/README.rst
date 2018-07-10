ILLUS.tsv
=========

In the file ILLUS.tsv, we have organised the data that we need, in regards to images. 

For each image, we have collected the following:
- A four letter abbreviation for the story title
- Text assoaciated with the image (image type, or caption)
- Source from which image was found
- Illustrator of the image
- A number / file name which can be used to link and display each image

For example, for a certain image for "The Speckled Band" by Josef Friedrich, the following data was collected:
SPEC	A HUGE MAN FRAMED HIMSELF IN THE APERTURE.	camden	Friedrich	spec-23

To display this in HTML, the ILLUS.tsv file was run through the follow python program:

.. 
	fh = open('/Users/nkusanda/desktop/sh-canon/pics/ILLUScamden')
	url{'camden': 'https://ignisart.com/camdenhouse/gallery/', 'vicweb': 'http://www.victorianweb.org/art/illustration/pagets/'}
	img{'camden': 'https://ignisart.com/camdenhouse/images/','vicweb': 'http://www.victorianweb.org/art/illustration/pagets/'}

	for l in fh:
    	(abr, text, src, illustrator, n) = l.strip().split('\t')
    	print("""<p>{0}, <a href='{1}{3}.htm'><img src='{2}{3}.jpg'>{4}</a> by {5}""".format(abr,
                                                                                 	url[src],
                                                                                	img[src],
                                                                                 	n,
                                                                                 	text,
                                                                                 	illustrator))
This program would print HTML code to display the images in ILLUS.tsv, as well as metadata such as the story abbreviation, assoaciated text, and the illustrator. For images from 'camden' however, an error was encountered, as certain images used the extension '.gif' instead of '.jpg'. To overcome this in the future, the extension would be included in the image number / file name. 
