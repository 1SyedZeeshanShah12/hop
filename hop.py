o
    ??c?	  ?                   @   sD   d dl Z d dlZd dlZdZejddd?Zee?add? Ze?  dS )?    Na?  

	##     ##     #######     ########  
	##     ##    ##     ##    ##     ## 
	##     ##    ##     ##    ##     ## 
	#########    ##     ##    ########  
	##     ##    ##     ##    ##        
	##     ##    ##     ##    ##        
	##     ##     #######     ##        

--------------------------------------------------
 Author: Muhammad Hamza
 Github: https://github.com/hop09
--------------------------------------------------z	uname -omT)?shellc                  C   s?  t ?d? tt? td? td? td? td? td? td? td? td	? td
?} | dkr~dtv rSt j?d?sLt ?d? t ?d? t ?d? d S t ?d? d S dtv rut j?d?snt ?d? t ?d? t ?d? d S t ?d? d S td? t?  d S | dkr?dtv r?t j?d?s?t ?d? t ?d? t ?d? d S t ?d? d S dtv r?t j?d?s?t ?d? t ?d? t ?d? d S t ?d? d S td? t?  d S td ? t?  d S )!N?clearz Update detailsz Latest version: 5.4z Update date: 13-09-2022z2--------------------------------------------------z [1] Version 5.3z [2] Version 5.4z	 [E] Exit? z Choose version: ?1Zaarch64Zh6453zOcurl -L https://github.com/hop09/libraries/blob/main/5.3/h6453?raw=true > h6453zchmod 777 h6453z./h6453ZarmZh3253zOcurl -L https://github.com/hop09/libraries/blob/main/5.3/h3253?raw=true > h3253zchmod 777 h3253z./h3253z( Cannot detect required aarchitecture...?2Zh6454zOcurl -L https://github.com/hop09/libraries/blob/main/5.4/h6454?raw=true > h6454zchmod 777 h6454z./h6454Zh3254zOcurl -L https://github.com/hop09/libraries/blob/main/5.4/h3254?raw=true > h3254zchmod 777 h3254z./h3254z Choose correct version ....)	?os?system?print?logo?input?
deviceArch?path?isfile?exit)ZchoiceVersion? r   ?hop.py?main   sV   











r   )	r   ?sys?
subprocessr
   Zcheck_outputZ	deviceArc?strr   r   r   r   r   r   ?<module>   s    
4