print('\t\t\t---->  𝖧𝖮𝖲𝖯𝖨𝖳𝖠𝖫  <-----')
import pandas as pd
import matplotlib.pyplot as plt

def excel():
 r=input('\t\t\tcsv file Name\n\t\t\t->')
 re=r+'.csv'
 print('----------------------------------------------------',re,'----------------------------------------------------')
 df=pd.read_csv(re)
 d=pd.DataFrame(df,columns=['ID','Name','Address','Disease','Room no.','Days','Amount'])
 print(d)
 print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
 
def iexcel():
 r=input('\t\t\tcsv file Name to export\n\t\t\t->')
 re=r+'.csv'
 d=pd.DataFrame(df,columns=['ID','Name','Address','Disease','Room no.','Days','Amount'])
 d.to_csv(re)

def sexcel():
 d=pd.DataFrame(df,columns=['ID','Name','Address','Disease','Room no.','Days','Amount'])
 d.to_csv('record.csv')
def menu():
 b=int(input('\t\t\t1.Use Exiting Record\n\t\t\t2.Create Record\n\t\t\t->'))
 if b==1:
  r=input('\t\t\tcsv file Name\n\t\t\t->')
  re=r+'.csv'
  print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋',re,'﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
  df=pd.read_csv(re)
  df=pd.DataFrame(df,columns=['ID','Name','Address','Disease','Room no.','Days','Amount'])
  print(df)
  print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
  while True:
    print('\t\t\t1.Function\n\t\t\t2.Plot graph\n\t\t\t3.Add or Drop\n\t\t\t4.Search\n\t\t\t5.Change\n\t\t\t6.Exit')   
    i=int(input('\t\t\tENTER NUMBER:'))
    print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋----')
 
    if i==1:
     print('\t\t\t1.SLICING\n\t\t\t2.Head\n\t\t\t3.Tail\n\t\t\t4.Max\n\t\t\t5.Min\n\t\t\t6.Total\n\t\t\t7.Mode\n\t\t\t8.Average\n\t\t\t9.Count\n\t\t\t0.Exit')
     s=int(input('\t\t\tChoose Function:'))
     if s==1:
      r=input('\t\t\tEnter Sr.no of Start row:')
      r1=input('\t\t\tEnter Sr.no of Endrow:')
      c=input('\t\t\tEnter label of Start column:')
      c1=input('\t\t\tEnter label ofEnd column:')
      l=df.loc[r:r1,c:c1]
      print('\t\t\t')
      print(l)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==2:
      h=int(input('\t\t\tNo. Rows?:'))
      H=df.head(h)
      print('\t\t\t')       
      print(H)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==3:
      t=int(input('\t\t\tNo. Rows?:'))
      T=df.tail(t)
      print('\t\t\t')
      print(T)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==4:
      c=input('\t\t\tcolumn:')
      M=df[c]
      x=M.max()
      print('\t\t\t')
      print('\t\t\tMaximum',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==5:
      c=input('\t\t\tcolumn:')
      Mi=df[c]
      x=Mi.min()
      print('\t\t\t')
      print('\t\t\tMinimum=',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==6:
      c=input('\t\t\tcolumn:')
      S=df[c]
      x=S.sum()
      print('\t\t\t')
      print('\t\t\tTotal=',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==7:
      Mo=df.mode()
      print('\t\t\t')
      print('\t\t\tMode=',Mo)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==8:
      print('\t\t\tColumn Name:')
      n=input('\t\t\t->')
      t=df[n]
      m=t.mean()
      print('\t\t\tMean=',m)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==9:
        f=df['ID']
        a=f.count()
        print('\t\t\tThere are',a,'records')
        e=input('\t\t\tPress Enter to continue') 
        continue 
     if s==0:
       print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
       
       continue
    if i==2:
     print(df)
     print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')  
     d=int(input('\t\t\t1.Bar\n\t\t\t2.line\n\t\t\t3.Exit\n\t\t\t->'))
     if d==1:
        print(df)
        X=input('\t\t\tColumn data for X axis\n\t\t\t->') 
        x=df[X]
        Y=input('\t\t\tColumn data for Y axis\n\t\t\t->')
        y=df[Y]
        c=input('\t\t\tColor:')
        plt.plot(x,y,color=c)
        plt.show()
        
     if d==2:
        X=input('\t\t\tColumn data for X axis\n\t\t\t->') 
        x=df[X]
        Y=input('\t\t\tColumn data for Y axis\n\t\t\t->')
        y=df[Y]
        c=input('\t\t\tColor:')
        plt.bar(x,y,color=c)
        plt.show()
       
     if d==3:
        e=input('\t\t\tPress Enter to continue') 
        continue
     else:
         print('------------------------✕--Wrong Entry--✕--------------------------')
         e=input('\t\t\tPress Enter to continue') 
         continue
    if i==3:
     print('\t\t\t1.Add\n\t\t\t2.Drop\n\t\t\t3.Exit')
     r=int(input('\t\t\t->'))
     if r==1:
        print('\t\t\tEnter ID Number ')
        g=int(input('\t\t\t->'))
     
        print('\t\t\tEnter Name ')
        h=input('\t\t\t->')
     
        print('\t\t\tEnter Address ')
        f=input('\t\t\t->')
        
        print('\t\t\tEnter Disease ')
        v=input('\t\t\t->')
        
        print('\t\t\tEnter Room no. ')
        k=int(input('\t\t\t->'))
     
        print('\t\t\tEnter Number of days ')
        j=int(input('\t\t\t->'))
        print('\t\t\tEnter Amount ')
        a=int(input('\t\t\t->'))
        f=df['ID']
        s=f.count()
        S=s+1
        df.loc[S]=[g,h,f,v,k,j,a]
        sexcel()
        print(df)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
    
     if r==2:
        e=int(input('\t\t\tSr.no?\n->'))   
        f=df.drop(e,axis=0)
        sexcel()
        print('\t\t\t',f)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
        
     
     
    if i==4:
     s=input('\t\t\tBy which column u want to Find\n\t\t\tID\n\t\t\tName\n\t\t\tAddress\n\t\t\tRoom\n\t\t\tNumber of Days\n\t\t\t->')
     if s=='ID':
         
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        print('\t\t\t',r)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Room':
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        print('\t\t\t',r)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Number of Days':
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        print('\t\t\t',r)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Name'or'Address':
       t=input('\t\t\tEnter Data\n\t\t\t->')
       e=df[s]
       r=df.loc[e==t]
       print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
       print('\t\t\t',r)
       print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
       e=input('\t\t\tPress Enter to continue') 
       continue
     else:
       print('------------------------✕--Wrong Entry--✕--------------------------')
       e=input('\t\t\tPress Enter to continue') 
       continue  
    if i==5:
     print(df)
     print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
     s=input('\t\t\t->By which column you want to Change<-\n\t\t\tID\n\t\t\tName\n\t\t\tAddress\n\t\t\tDisease\n\t\t\tRoom\n\t\t\tDays\n\t\t\tAmount \n\t\t\t->')
     if s=='ID':
       
        r=int(input('\t\t\tSr.no\n\t\t\t->'))
        t=int(input('\t\t\tEnter New Data\n\t\t\t->'))
        df.loc[r,s]=t
        sexcel()
        print('-----------------------------------------------------')
        print(df)
        e=input('\t\t\tPress Enter to continue') 
        continue 

        
     if s=='Room':
        r=int(input('\t\t\tSr.no\n\t\t\t->'))
        t=int(input('\t\t\tEnter New Data\n\t\t\t->'))
        df.loc[r,'Room no.']=t
        sexcel()
        print('-----------------------------------------------------')
        print(df)
        e=input('\t\t\tPress Enter to continue') 
        e=input('\t\t\tPress Enter to continue') 
        continue 
     if s=='Days':
        r=int(input('\t\t\tSr.no\n\t\t\t->'))
        t=int(input('\t\t\tEnter New Data\n\t\t\t->'))
        df.loc[r,s]=t
        sexcel()
        print('-----------------------------------------------------')
        print(df)
        e=input('\t\t\tPress Enter to continue') 
        continue 
     if s=='Amount':
        r=int(input('\t\t\tSr.no\n\t\t\t->'))
        t=int(input('\t\t\tEnter New Data\n\t\t\t->'))
        df.loc[r,s]=t
        sexcel()
        e=input('\t\t\tPress Enter to continue') 
        continue 
        print('-----------------------------------------------------')
        print(df)    
     if s=='Name'or'Address'or'Disease':
        r=int(input('\t\t\tSr.no\n\t\t\t->'))
        t=input('\t\t\tEnter New Data\n\t\t\t->')
        df.loc[r,s]=t
        sexcel()
        print(df)
        e=input('\t\t\tPress Enter to continue') 
        continue 
    if i==6:
       exit() 
    else :
     print('---------------------------------✕--Wrong Entry--✕------------------------------------')
     continue
 if b==0:
   print('\t\t\tThis project is created by Sachin')
   
 if b==2: 
   print('\t\t\tNumber of Data')
   s=int(input('\t\t\t->'))
   s=s+1
   S=range(1,s)
   df=pd.DataFrame({'ID':S,'Name':S,'Address':S,'Disease':S,'Room no.':S,'Days':S,'Amount':S},index=range(1,s))
   
   o=int(input('\t\t\tCharges per day\n\t\t\t->'))
   n=0
   s=s-1
   while n<s:
       n=n+1
       N=n-1
       print('\t\t\tEnter ID Number for',n,'Person','\t')
       g=int(input('\t\t\t->'))
       df.iat[N,0]=g
       print('\t\t\tEnter Name for',n,'\t')
       h=input('\t\t\t->')
       df.iat[N,1]=h
       print('\t\t\tEnter Address of',h,'\t')
       f=input('\t\t\t->')
       df.iat[N,2]=f
       print('\t\t\tEnter Disease of',h,'\t')
       c=input('\t\t\t->')
       df.iat[N,3]=c
       print('\t\t\tEnter Room no. of',h,'\t')
       k=int(input('\t\t\t->'))
       df.iat[N,4]=k
       print('\t\t\tEnter Number of days of',h,'\t')
       j=int(input('\t\t\t->'))
       df.iat[N,5]=j
       df.iat[N,6]=j*o
   print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
   print(df)
   print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
   while True:
    print('\t\t\t1.Function\n\t\t\t2.Export to Excel\n\t\t\t3.Plot graph\n\t\t\t4.Add or Drop\n\t\t\t5.Search\n\t\t\t6.Add Record to csv file\n\t\t\t7.Exit')   
    i=int(input('\t\t\tENTER NUMBER:'))
 
    if i==1:
     print('\t\t\t1.SLICING\n\t\t\t2.Head\n\t\t\t3.Tail\n\t\t\t4.Max\n\t\t\t5.Min\n\t\t\t6.Total\n\t\t\t7.Mode\n\t\t\t8.Average\n\t\t\t9.Exit')
     s=int(input('\t\t\tChoose Function:'))
     if s==1:
      r=input('\t\t\trow')
      c=input('\t\t\tcolumn')
      l=df.loc[r:c]
      print('\t\t\t')
      print(l)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==2:
      h=int(input('\t\t\tNo. Rows'))
      H=df.head(h)
      print('\t\t\t')       
      print(H)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==3:
      t=int(input('\t\t\tNo. Rows'))
      T=df.tail(t)
      print('\t\t\t')
      print(T)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==4:
      c=input('\t\t\tcolumn')
      M=df[c]
      x=M.max()
      print('\t\t\t')
      print('\t\t\tMaximum',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==5:
      c=input('\t\t\tcolumn')
      Mi=df.c
      x=Mi.min()
      print('\t\t\t')
      print('\t\t\tMinimun',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==6:
      c=input('\t\t\tcolumn')
      S=df[c]
      x=S.sum()
      print('\t\t\t')
      print('\t\t\tTotal',x)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==7:
      Mo=df.mode()
      print('\t\t\t')
      print('\t\t\tMode',Mo)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==8:
      print('\t\t\tColumn name')
      n=input('\t\t\t->')
      t=df[n]
      m=t.mean()
      print('\t\t\tMean',m)
      print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
      e=input('\t\t\tPress Enter to continue') 
      continue
     if s==9:
       print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')  
       continue
     else:
      print('---------------------------------✕--Wrong Entry--✕------------------------------------')
      continue
       
    
        
  
    if i==2:
     print('\t\t\tExport to csv')   
     iexcel()
     print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋ＤＯＮＥ﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
     e=input('\t\t\tPress Enter to continue') 
     continue
    if i==3:
     d=int(input('\t\t\t1.Bar\n\t\t\t2.line\n\t\t\t3.Exit\n\t\t\t->'))
     if d==1:
        print(df)
        X=input('\t\t\tColumn data for X axis') 
        x=df[X]
        Y=input('\t\t\tColumn data for Y axis')
        y=df[Y]
        c=input('\t\t\tColor')
        plt.plot(x,y,color=c)
        plt.show()
        e=input('\t\t\tPress Enter to continue') 
        continue
     if d==2:
        X=input('\t\t\tColumn data for X axis') 
        x=df[X]
        Y=input('\t\t\tColumn data for Y axis')
        y=df[Y]
        c=input('\t\t\tColor')
        plt.bar(x,y,color=c)
        plt.show()
        e=input('\t\t\tPress Enter to continue') 
        continue
     if d==3:
        e=input('\t\t\tPress Enter to continue') 
        continue
     else:
        print('------------------------✕--Wrong Entry--✕--------------------------')   
     if i==4:
      print('\t\t\t1.Add\n\t\t\t2.Drop\n\t\t\t3.Exit')
      r=int(input('\t\t\t->'))
      if r==1:
        print('\t\t\tEnter ID Number ')
        g=int(input('\t\t\t->'))
     
        print('\t\t\tEnter Name ')
        h=input('\t\t\t->')
     
        print('\t\t\tEnter Address ')
        f=input('\t\t\t->')
     
        print('\t\t\tEnter Room no. ')
        k=int(input('\t\t\t->'))
     
        print('\t\t\tEnter Number of days ')
        j=int(input('\t\t\t->'))
        a=j*o
        f=df['ID']
        s=f.count()
        S=s+1
        df.loc[S]=[g,h,f,k,j,a]
     
     
        print(df)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
    
     if r==2:
        e=int(input('\t\t\tSr.no-'))   
        f=df.drop(e,axis=0)
        print('\t\t\t',f)
        print('﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
        e=input('\t\t\tPress Enter to continue') 
        continue
     
     
    if i==5:
     s=input('\t\t\tBy which column u want to Find\n\t\t\t1.ID\n\t\t\t2.Name\n\t\t\t3.Address\n\t\t\t4.Room\n\t\t\t5.Number of Days\n\t\t\t->')
     if s=='ID':
         
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('\t\t\t',r)
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Room':
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('\t\t\t',r)
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Number of Days':
        d=int(input('\t\t\tEnter Data\n\t\t\t->'))
        e=df[s]
        r=df.loc[e==d]
        print('\t\t\t',r)
        e=input('\t\t\tPress Enter to continue') 
        continue
     if s=='Name'or'Address':
       t=input('\t\t\tEnter Data\n\t\t\t->')
       e=df[s]
       r=df.loc[e==t]
       print('\t\t\t',r)
       e=input('\t\t\tPress Enter to continue') 
       continue
     else:
       print('---------------------------------✕--Wrong Entry--✕------------------------------------') 
    if i==6:
     e=input('\t\t\tName of csv file\n\t\t\t->')
     ex=e+'.csv'
     csv=pd.read_csv(ex)
     ap=csv.append(df,ignore_index=True)
     print('\t\t\t',ap)
     ap.to_csv(ex)
     print('----------------------ＤＯＮＥ---------------------')
     e=input('\t\t\tPress Enter to continue') 
     continue
     
    if i==7:
     print('\t\t\tbyeeeeee')
     exit()
    
    
    else:
     print('---------------------------------✕--Wrong Entry--✕------------------------------------')
    continue
 else:
   print('---------------------------------✕--Wrong Entry--✕------------------------------------')
   menu()
p=input('Enter Password :')
if p=='oxford':
   menu()   
else:
   exit()