from flash_firmware import *

flash_udc_firmware("M3_blink_slow.out", "C28_blink_slow.out")
wait = input("DESLIGUE E LIGUE O UDC.")

flash_udc_firmware("M3_blink_fast.out", "C28_blink_fast.out")
wait = input("DESLIGUE E LIGUE O UDC.")