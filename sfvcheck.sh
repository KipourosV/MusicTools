#!/bin/bash
clear
echo "checking..."
echo "1970s"
python sfvcheck.py /mnt/storage/Music/1970s > /mnt/storage/Music/1970s/sfvcheck
echo "1980s"
python sfvcheck.py /mnt/storage/Music/1980s > /mnt/storage/Music/1980s/sfvcheck
echo "1990"
python sfvcheck.py /mnt/storage/Music/1990s/1990 > /mnt/storage/Music/1990s/1990/sfvcheck
echo "1991"
python sfvcheck.py /mnt/storage/Music/1990s/1991 > /mnt/storage/Music/1990s/1991/sfvcheck
echo "1992"
python sfvcheck.py /mnt/storage/Music/1990s/1992 > /mnt/storage/Music/1990s/1992/sfvcheck
echo "1993"
python sfvcheck.py /mnt/storage/Music/1990s/1993 > /mnt/storage/Music/1990s/1993/sfvcheck
echo "1994"
python sfvcheck.py /mnt/storage/Music/1990s/1994 > /mnt/storage/Music/1990s/1994/sfvcheck
echo "1995"
python sfvcheck.py /mnt/storage/Music/1990s/1995 > /mnt/storage/Music/1990s/1995/sfvcheck
echo "1996"
python sfvcheck.py /mnt/storage/Music/1990s/1996 > /mnt/storage/Music/1990s/1996/sfvcheck
echo "1997"
python sfvcheck.py /mnt/storage/Music/1990s/1997 > /mnt/storage/Music/1990s/1997/sfvcheck
echo "1998"
python sfvcheck.py /mnt/storage/Music/1990s/1998 > /mnt/storage/Music/1990s/1998/sfvcheck
echo "1999"
python sfvcheck.py /mnt/storage/Music/1990s/1999 > /mnt/storage/Music/1990s/1999/sfvcheck
echo "Finished"
