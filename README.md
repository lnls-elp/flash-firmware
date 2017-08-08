"# flash-firmware" 

dslite.bat : arquivo gerado pelo software Uniflash da Texas. Os arquivos em python foram inspirados nele, mas acho que não será mais necessário.

call_batch.py : script python que chama um arquivo .bat para ser executado (solução do Stack Overflow). Também não será necessário, estou deixando de referência se eventualmente precisar.

flash_firmware.py : módulo que tem uma função que grava os códigos no UDC a partir dos nomes dados dos arquivos .out (um para o ARM e outro para o C28). Os arquivos .out devem estar na pasta "user_files/images".

test_flash.py : script que testa a função de gravar. Grava um código que pisca os LEDs devagar e outro que pisca mais rápido.
