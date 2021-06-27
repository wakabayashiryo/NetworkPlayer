# The back up managment for volumio network audio player

- ## How to backup (Linux Enviroment)
    - Insert the SD card for backup into the slot
    - Confirm device name of the SD card   
        >  sudo fdisk -l

        ~~~
        ディスク /dev/sdb: 3.7 GiB, 3959422976 バイト, 7733248 セクタ
        単位: セクタ (1 * 512 = 512 バイト)
        セクタサイズ (論理 / 物理): 512 バイト / 512 バイト
        I/O サイズ (最小 / 推奨): 512 バイト / 512 バイト
        ディスクラベルのタイプ: dos
        ディスク識別子: 0xb7678f2f

        デバイス   起動 開始位置 最後から  セクタ サイズ Id タイプ
        /dev/sdb1  *           1   125000  125000    61M  c W95 FAT32 (LBA)
        /dev/sdb2         125001  4882812 4757812   2.3G 83 Linux
        /dev/sdb3        4882813  7732421 2849609   1.4G 83 Linux
        ~~~

    - Create backup as img file
        > sudo dd bs=100M if=/dev/mmcblk0 of=volumioyyyymmdd.img status=progress  conv=fsync   

        if=The Device name of SD card for backup   
        of=img file name and its path   
        bs=Buffer Size   
        status=progress Display the progress   
        - example   
            > sudo dd bs=100M if=/dev/mmcblk0 of=volumio20190511.img status=progress conv=fsync   

    - Move the img file to samba server folder and write version history    
    
- ## How to restore (Linux Enviroment)
    **Restore to the same size SD card as the one you backed up**
    - Insert the destination SD card into the slot
    - Confirme device of the SD card   
        >  sudo fdisk -l

        ~~~
        ディスク /dev/sdb: 3.7 GiB, 3959422976 バイト, 7733248 セクタ
        単位: セクタ (1 * 512 = 512 バイト)
        セクタサイズ (論理 / 物理): 512 バイト / 512 バイト
        I/O サイズ (最小 / 推奨): 512 バイト / 512 バイト
        ディスクラベルのタイプ: dos
        ディスク識別子: 0xb7678f2f

        デバイス   起動 開始位置 最後から  セクタ サイズ Id タイプ
        /dev/sdb1  *           1   125000  125000    61M  c W95 FAT32 (LBA)
        /dev/sdb2         125001  4882812 4757812   2.3G 83 Linux
        /dev/sdb3        4882813  7732421 2849609   1.4G 83 Linux
        ~~~

    - Restore backup from img file to SD card
        > sudo dd bs=100M if=volumioyyyymmdd.img of=/dev/mmcblk0  status=progress conv=fsync    
    
        if=The backup of img file   
        of=The device name of the destination SD card   
        bs=Buffer Size   
        status=progress Display the progress   
        
        - example   
            > sudo dd bs=100M if=volumio20190511.img of=/dev/mmcblk0 status=progress  conv=fsync    conv=fsync

    - ## Histrory
        |data|ver.|file name|difference|remark|
        |:---|:---|:--------|:---------|:-----|
        |2019/5/11|1.00|volumio20190511.img|create initial backup|
        |2019/5/18|0.99|volumio20190518.img|downgraded to version 2.526, confirmed stable|
        |2019/5/19|1.01|volumio20190519.img|upgrade to 2.575 and fix bug of connection by 2.4GHz band|
        |2019/6/9|1.10|volumio20190609.img|upgrade to 2.586 and add change specification of hardware|
        |2020/2/8|1.11|volumio20200208.img|upgrade to 2.699 and Regular backup|
        |2020/8/29|1.12|volumio20200829.img|upgrade to 2.806 and Regular backup|
        |2021/3/7|1.13|volumio20210307.img|minor backup|
        |2021/6/27|1.14|volumio20210627.img|change ssh connection method to public key auth|

