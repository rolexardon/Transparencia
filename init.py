# -*- coding: latin-1 -*-
import sys, os
try:
	import settings
	sys.path.append(os.path.join(settings.ROOT_PATH, '..'))
	os.environ['DJANGO_SETTINGS_MODULE'] = 'Transparencia.settings'
	
	from django.db import transaction
	from barrios import *
	from Transparencia.Administration.models import *


	""" Ingresar Departamentos, Municipios, Aldeas, Caserios y barrios """
	def numero_a_texto(num, longitud):
		retorno = str(num)
		while len(retorno) < longitud:
			retorno = '0' + retorno
		return retorno
	with transaction.commit_on_success():

		for d in barrios_data:
		    #guardar el departamento...
			depto = Departamento( codigo=numero_a_texto(d[0],2), nombre = d[1] )
			try:
				depto.save()
			except Exception, e:
				print e
				transaction.rollback()
			else:	
		#guardar los municipios...
				transaction.commit()
				for m in d[2]:
					muni = Municipio( codigo=numero_a_texto(m[0],2), nombre = m[1], departamento = depto )
					try:
						muni.save()
					except Exception, e:
						print e
						transaction.rollback()
					else:
		                #guardar las aldeas...
						transaction.commit()
						for a in m[2]:
							ald = Aldea( codigo=numero_a_texto(a[0],3), nombre = a[1], municipio = muni )
							try:
								ald.save()
							except Exception, e:
								print e
								transaction.rollback()
							
							else:
		                        			transaction.commit()
		                        #guardar caserios...
								for c in a[2]:
									cas = Caserio( codigo=numero_a_texto(c[0],4), nombre = c[1], aldea = ald )
		                            
									try:
										cas.save()
									except Exception,e:
										print e
										transaction.rollback()
		                                #transaction.rollback()
									else:
		                                				transaction.commit()
		                                #finalmente los barrios (si hay)
										for b in c[2]:
											bar = Barrio( codigo=numero_a_texto(b[0],5), nombre = b[1], caserio = cas )
											try:
												bar.save()
											except Exception, e:
												print e
												transaction.rollback()
											else:  
												transaction.commit()

				print 'Se ingreso el departamento %s con sus municipios, aldeas, caserios y barrios' % (d[1])
except ImportError:
	sys.stderr.write('Error: Cannot initialize environment.\n')
	sys.exit(1)
	
	
