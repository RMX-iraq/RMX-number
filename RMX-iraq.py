a
    �>`A  �                
   @   s�  d dl T d dlZe�d� e�d� d dlT d dlmZ d dlmZ ed� ed� e�d� ed	� ed
� dZdZ	e
d�Zed
� ed� e
d�Zed� z~eekr�ee	kr�ed� ed� e�d� nNed� ed
� ed� ed� ed� ed� ed� ed� ed� e�  W n. e�yJ Z zed� W Y dZ[n
dZ[0 0 e
d�Zed� ed� eed�Zee�ed�� eed�Zee�ed�� ed� e�d� dS )�    )�*Nzpip3 install phonenumbers�clear)�geocoder)�carrierz4[0;33m                                     welcome g      �?zR[0;33m          >>> Please enter the name and numbe Your performancer <<< [0;37m� zRMX-iraqZiraqz[0;32mEnter the name: [0;33mz![0;32mEnter the passwerd:[0;33mzVery well logged in�   zCheck the name and the passwerdg�������?u   ↓z[0;31mexit[0;37mz[1;91m ERROR: [1;97mz.Enter the phone number with the country code: �   u   ↓↓↓↓ZCHZenZROz$termux-open-url https://t.me/RMXiraq)�time�os�systemZphonenumbersr   r   �print�sleepZusernameZpasswerd�inputZsecret1Zsecret2�exit�	Exception�eZnumber�parseZ	ch_numberZdescription_for_numberZcrZname_for_number� r   r   �RMX-iraq.py�<module>   sX   





