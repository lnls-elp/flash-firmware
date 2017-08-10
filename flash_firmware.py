import os

class LoadFirmware:

    def __init__(self, arm_filename=None, c28_filname=None):

        self._arm = arm_filename
        self._c28 = c28_filname

    @property
    def arm_filename(self):
        return self._arm

    @arm_filename.setter
    def arm_filename(self, path):
        self._arm = path

    @property
    def c28_filename(self):
        return self._c28

    @c28_filename.setter
    def c28_filename(self, path):
        self._c28 = path

    def flash_firmware(self):
        print("flashing firmware...")
        try:
        	os.system(" CMD /C \"ccs_base\\DebugServer\\bin\\DSLite\" flash -c user_files/configs/f28m36p63c2.ccxml -l user_files/settings/generated.ufsettings -e -f -v user_files/images/" + self._arm)
        	os.system(" CMD /C \"ccs_base\\DebugServer\\bin\\DSLite\" flash -c user_files/configs/f28m36p63c2.ccxml -l user_files/settings/generated.ufsettings --core=1 -e -f -v user_files/images/" + self._c28)
        	print("FIRWARE GRAVADO.")
        except:
        	print("ERRO AO GRAVAR FIRMWARE!")
