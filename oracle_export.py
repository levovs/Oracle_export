import os
import shutil
import cx_Oracle
import threading

def export_oracle():
  dir="Export" 
  print("Starting export...")                                                                              
  if os.path.exists(dir):                                                                    
     shutil.rmtree(dir)                                                                      
  if not os.path.exists(dir):                                                                
    os.makedirs(dir)                                                                         
  os.environ["NLS_LANG"] = ".UTF8"
  #login,password to connect to oracle 
  login="python1"
  password="12345678" 
  server="localhost"
  sid="xe"                                                         
  #con = cx_Oracle.connect('python1/12345678@localhost/xe')                                   
  con = cx_Oracle.connect('%login/%password@%server/%sid' % login,password,server,sid)                                   
  cur = con.cursor()                                                                         
  cur1 = con.cursor()                                                                        
  objectTypeChars=['PACKAGE','VIEW','PROCEDURE','FUNCTION','TYPE','JOB','TABLE']             
  for ii in (objectTypeChars):                                                               
     dir_res=dir+"\\"+ii                                                                     
     if not os.path.exists(dir_res):                                                                
       os.makedirs(dir_res)                                                                         
                                                                                                    
                                                                                                    
     cur.execute('select OBJECT_NAME from user_objects where OBJECT_TYPE= :1',(ii,))         
     for i in cur:                                                                                  
         print(i[0])                                                                                
         Val = str(i[0])                                                                            
         cur1.execute('select dbms_metadata.get_ddl(:1, :2) from dual',(ii,i[0],))           
         rec1 = cur1.fetchone()                                                                     
         with open(dir_res+"\\"+Val+".sql", "w") as f:                                              
           f.write(rec1[0].read())                                                                  
                                                                                             
  cur.close()                                                                                
  cur1.close()                                                                               
  con.close()                                                                                


def repeatit():
  threading.Timer(60.0, repeatit).start()
  export_oracle()

repeatit()


