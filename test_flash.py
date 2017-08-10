from flash_firmware import *

flash = LoadFirmware()

flash.arm_filename = "M3_blink_slow.out"
flash.c28_filname = "C28_blink_slow.out"

flash.flash_firmware()

#flash_udc_firmware("M3_blink_slow.out", "C28_blink_slow.out")
#wait = input("DESLIGUE E LIGUE O UDC.")
#
#flash_udc_firmware("M3_blink_fast.out", "C28_blink_fast.out")
#wait = input("DESLIGUE E LIGUE O UDC.")
