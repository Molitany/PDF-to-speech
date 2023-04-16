$PDF = $args[0]
If (-Not ($PDF -like "*.pdf"))
{
    "Have to give a pdf file as second argument."
    Exit -1
}
$PythonFile = Join-Path $PSScriptRoot '\read_pdf.py'
python $PythonFile $PDF
$WAV = $PDF.replace("pdf", "wav")
start $PDF
start $WAV