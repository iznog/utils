#!/bin/bash

pdfinicial=$1
ficheirops=${pdfinicial%.*}.ps
pdfa=${pdfinicial%.*}_a.pdf
pdftops $pdfinicial $ficheirops

gs -dPDFA -dBATCH -dNOPAUSE -dNOOUTERSAVE -dUseCIEColor -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sPDFACompatibilityPolicy=1 -sOutputFile=$pdfa $ficheirops
