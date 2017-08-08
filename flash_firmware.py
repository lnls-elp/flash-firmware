import os


def flash_udc_firmware(ARM_filename,  C28_filename):
	print("flashing firmware...")
	try:
		os.system(" CMD /C \"ccs_base\\DebugServer\\bin\\DSLite\" flash -c user_files/configs/f28m36p63c2.ccxml -l user_files/settings/generated.ufsettings -e -f -v user_files/images/" + ARM_filename)
		os.system(" CMD /C \"ccs_base\\DebugServer\\bin\\DSLite\" flash -c user_files/configs/f28m36p63c2.ccxml -l user_files/settings/generated.ufsettings --core=1 -e -f -v user_files/images/" + C28_filename)
		print("FIRWARE GRAVADO.")
	except:
		print("ERRO AO GRAVAR FIRMWARE!")