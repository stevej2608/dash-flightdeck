#!/bin/bash

VOLT_CSS=../css/volt.css
SAFE_LIST="ct-bar chartist-tooltip ct-area ct-chart-line ct-end ct-grid ct-grid ct-grids ct-horizontal ct-horizontal ct-label ct-labels ct-line ct-point ct-series ct-series-a ct-series-b"

echo "purging css ..."

purgecss -v -keyframes -font --safelist $SAFE_LIST -css $VOLT_CSS --content \
    settings-min.html \
    transactions-min.html \
    dashboard/dashboard-min.html \
    examples/*.html --output temp \
    tables/bootstrap-tables-min.html

echo "filter css ..."

csstools filter --skip_comments ../css/bootstrap.css ./temp/volt.css -o ../css/volt-min.css

# Convert multipul blank lines into one

echo "clean css ..."

sed -i ':a; /^\n*$/{ s/\n//; N;  ba};' ../css/volt-min.css

