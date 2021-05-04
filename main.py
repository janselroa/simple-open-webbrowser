import webbrowser

salir = False
while not salir:
	try:
		url_files={'firefox':'C://Program Files/Mozilla Firefox/firefox.exe', 'chrome':'C://Program Files/Google/Chrome/Application/chrome.exe', 'brave':'C://Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'}
		navegador = input('navegador:\n').lower()
		enlace = input('enlace:\n')
		webbrowser.register(navegador, None, webbrowser.BackgroundBrowser(url_files[navegador]))
		webbrowser.get(navegador).open(enlace)
	except:
		print('no has expesificado bien alguno de los valores')	

	if input('quieres  salir del programa') =='si':
		salir=True	