#!/bin/bash

# Each of the html files in the ./volt/pages folder contains
# a sub-part of the complete settings-combined.html page. The
# full css stylesheet that containes all the rules required is
# in ./volt/css/volt.css

# This script iterrates through each sub-page.html file extracting
# from ./volt/css/volt.css only those rules that use used by the
# page. The result is stored in ./temp/volt.css

# ./temp/volt.css is then passed through csstools which filters
# out any rules & attributes that are allready defined in the
# standard boostrap.css or in the rules defined by the
# previously processed files.


CSS_BASE=../css/volt.css
CSS_FILTER_INPUTS="../css/bootstrap.css"
for VAR in "settings-buttons" "settings-sidebar" "settings-alerts" "settings-form" "settings-cards"
do
  HTML_FILE=$VAR.html
  echo "Processing $HTML_FILE"

  # Get the CSS needed to support $HTML_FILE

	purgecss -v -keyframes -font -css $CSS_BASE --content $HTML_FILE --output temp
  #mv ./temp/volt.css ./temp/$VAR-purged.css

  # Filter the purged CSS

  csstools filter --skip_comments $CSS_FILTER_INPUTS ./temp/volt.css -o ../css/$VAR.css

  # Convert multipul blank lines into one

  sed -i ':a; /^\n*$/{ s/\n//; N;  ba};' ./temp/$VAR.css

  rm ./temp/volt.css

  # Add the filtered css file to the input list on the next pass

  CSS_FILTER_INPUTS="$CSS_FILTER_INPUTS ../css/$VAR.css "

  echo ""
done

# Do the combine CSS for comparison

VAR=combined
HTML_FILE=$HTML_FOLDER/settings-$VAR.html
echo "Processing $HTML_FILE"

purgecss -v -keyframes -font -css $CSS_BASE --content $HTML_FILE --output temp
csstools filter --skip_comments ./volt/css/bootstrap.css ./temp/volt.css -o ./temp/$VAR.css
sed -i ':a; /^\n*$/{ s/\n//; N;  ba};' ./temp/$VAR.css

rm ./temp/volt.css

# Add the filtered css file to the input list on the next pass

CSS_FILTER_INPUTS="$CSS_FILTER_INPUTS ./temp/$VAR.css "