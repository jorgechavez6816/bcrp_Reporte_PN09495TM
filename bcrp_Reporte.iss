Sub Main
	'Client.RunPython "C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Macros.ILB\bcrp_Reporte.py"
	Call TextImport()	'C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Archivos fuente.ILB\Reporte_PN09495TM.csv
End Sub


' Archivo - Asistente de importación: Texto delimitado
Function TextImport
	dbName = "Reporte_PN09495TM1.IMD"
	Client.ImportDelimFile "C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Archivos fuente.ILB\Reporte_PN09495TM.csv", dbName, FALSE, "", "C:\Users\Intel\Documents\Mis documentos IDEA\Samples\Definiciones de importación.ILB\Reporte_PN09495TM.RDF", TRUE
	Client.OpenDatabase (dbName)
End Function