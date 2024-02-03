#importing required modules
import csv
import os
from tabulate import tabulate

#function for signing in
def signin(m,p,k):
    f=open('logindata.txt','r')
    cr=csv.reader(f,lineterminator='\n')
    fields=next(cr)
    reclist=[]
    for rec in cr:
        if rec!=[]:
            reclist.append(rec)
    pwd=''
    if k==1:
        for rec in reclist:
            if m in rec[0]:                
                pwd=rec[2]        
        if p==pwd:
            return 'login successful'
        else:
            return 'incorrect usrname or password'
    elif k==2:
        for rec in reclist:
            if m in rec[1]:
                pwd=rec[2]
        if p==pwd:
            return 'login successful'
        else:
            return 'incorrect password'
    f.close()

#function to check if the proper mail id is provided
def email_id(e):
    l_email=len(e)
    str1=e.split('@')
    l=len(str1)
    if l!=2:
        return 'invalid emailID'
    else:
        dom='@'+str1[1]
        l_dom=len(dom)
        sub=e[l_email-l_dom:]
        if sub==dom:
            if l_dom!=l_email:
                return True
            else:
                return False

#function to check if the username is unique
def username(u):
    f=open('logindata.txt','r')
    cr=csv.reader(f,lineterminator='\n')
    fields=next(cr)
    reclist=[]
    for rec in cr:
        if rec!=[]:
            if u in rec[0]:
                return 'username not available'
    else:
        return True
    f.close()

#function to check if entered password is valid or not 
def password(p,c):
    if len(p)<8:
        return 'password should atleast have 8 characters'
    elif p!=c:
        return 'passwords do not match'
    else:
        return True

#function to generate playlist id
def playlist_id():
    f=open('logindata.txt','r')
    cr=csv.reader(f,lineterminator='\n')
    x=0
    fields=next(cr)
    for rec in cr:
        if rec!=[]:
            if int(rec[3])>x:
                x=int(rec[3])
    i=x+1
    print("your playlist id: ",i)
    return i
    f.close()
    return i

#function to search for a record
def search():
    f=open('songs.txt','r')
    cr=csv.reader(f,lineterminator='\n')
    fields=next(cr)
    while True:
        print('1:name','2:artist','3:genre','4:album','5:mood','6:decade',sep='\n')
        n=int(input('enter your choice: '))
        #searching on the basis of song name
        if n==1:
            nm=input('enter song name: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[1]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        #searching on the basis of artist name
        elif n==2:
            nm=input('enter artist name: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[2]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        #searching on the basis of genre
        elif n==3:
            nm=input('enter genre: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[6]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        #searching on the basis of album name
        elif n==4:
            nm=input('enter album name: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[3]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        #searching on the basis on mood
        elif n==5:
            nm=input('enter mood: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[5]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        #searching on the basis on decade
        elif n==6:
            nm=input('enter decade: ')
            flag=False
            reclist=[]
            for rec in cr:
                if rec!=[]:
                    if rec[4]==nm:
                        reclist.append(rec)                    
            for a in reclist:
                print(a)
                t=input("is this the song? y/n: ")
                if t=='y':
                    flag=True
                    return a
                elif t=='n':
                    continue
                else:
                    return 'please enter a valid choice'
            if flag==False:
                return "song not available"
        else:
            return 'enter a valid choice'
        a=input('do you want to search again y/n: ')
        if a=='y':
            continue
        elif a=='n':
            f.close()
            break
        else:
            return 'enter a valid choice'

#adding song to the songs file(for admin)
def addsong():
    while True:
        f=open('songs.txt','a+' , newline='')
        cr=csv.reader(f,lineterminator='\n')        
        cw=csv.writer(f,delimiter=',')
        rec=[]
        s=int(input('enter song_id: '))
        sn=input('enter song name: ')
        a=input('enter artist: ')
        al=input('enter album: ')
        d=input('enter decade: ')
        m=input('enter mood: ')
        g=input('enter genre: ')
        rec=[s,sn,a,al,d,m,g]
        flag=True
        for ctr in cr:
            if ctr!=[]:
                if s==ctr[0]:
                    print('song id is not unique')
                    flag=False
                    break
        if flag==True:
            cw.writerow(rec)        
        print('-'*28+'record successfully inserted'+'-'*27)
        a=input('do you want enter more records y/n: ')
        if a=='y':
            continue
        elif a=='n':
            f.close()
            break
        else:
            print('enter a valid choice')
            continue

#function to delete a record(for admin)
def deletesong():
    while True:
        f=open('songs.txt','r')
        cr=csv.reader(f,lineterminator='\n')
        fields=['song_id','songname','artist','album','decade','mood','genre']
        reclist=[]
        l1=next(cr)
        sn=input('enter song_name to be deleted: ')
        a=input('artist of the song: ')
        for rec in cr:
            if rec!=[]:
                reclist.append(rec)
        f.close()
        g=open('songs.txt','w' , newline='')
        cw=csv.writer(g,delimiter=',')
        cw.writerow(fields)
        for r in reclist:
            if r!=[]:
                if r[1]==sn and r[2]==a:
                    print(r)
                    ans=input('do you want to delete this record? y/n: ')
                    if ans=='y':
                        print('-'*28+'record successfully deleted'+'-'*28)
                        pass
                    else:
                        print('-'*33+'record not deleted'+'-'*32)
                        cw.writerow(r)
                else:
                    cw.writerow(r)
        g.close()
        w=input('do you want to delete any other record? y/n: ')
        if w=='y':
            continue
        elif w=='n':
            break
        else:
            print('enter a valid choice')

#function to update a record(for admin)
def updatesong():
    while True:
        #checking if the record exists in the song file
        f=open('songs.txt','r')        
        cr=csv.reader(f,lineterminator='\n')
        fields=['song_id','songname','artist','album','decade','mood','genre']
        reclist=[]
        z=input('song_id of the song that is to be updated: ')
        flag=False
        for rec in cr:
            if rec!=[]:
                reclist.append(rec)
                if rec[0]==z:
                    a=rec
                    flag=True
        f.close()
        if flag==False:         
            print('-'*33+'record not found'+'-'*34) 
        else:
            print(a)
            l=input('do you want to update the record? y/n: ')
            print('what do you want to update ?')        
            print('1:song name','2:artist','3:album','4:mood','5:decade','6:genre',sep='\n')
            ctr=int(input('ENTER YOUR CHOICE: ')) 
            if l=='y':
                #updating song name in the record
                if ctr==1:
                    nm=input('enter new song name: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[1]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(g,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                #updating artist name in the record
                elif ctr==2:
                    nm=input('enter new artist name: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[2]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(g,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                #updating album name in the record
                elif ctr==3:
                    nm=input('enter new album name: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[3]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(g,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                #updating mood in the record
                elif ctr==4:
                    nm=input('enter new mood: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[5]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(g,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                #updating decade in the record
                elif ctr==5:
                    nm=input('enter new decade: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[4]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(f,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                #updating genre in the record
                elif ctr==6:
                    nm=input('enter new genre: ')
                    for rec in reclist:
                        if rec[0]==z:
                            rec[6]=nm
                    g=open('songs.txt','w' , newline='')
                    cw=csv.writer(g,delimiter=',')
                    cw.writerow(fields)
                    for i in range(1,len(reclist)):
                        cw.writerow(reclist[i])
                    print('-'*28+'record updated successfully'+'-'*28)
                    g.close()
                x=input('do you want to update more records? y/n: ')
                if x=='y':
                    continue
                elif x=='n':                    
                    break
                else:
                    print('enter a valid choice')
                    continue
            elif l=='n':
                print('record not updated')
                break
            else:
                print('enter a valid choice')
                continue

#function to create playlist (for user)
def playlist_name(n):
    j=0
    f=open('logindata.txt','r')
    cr=csv.reader(f,lineterminator='\n')
    l1=next(cr)
    m=input("by (username): ")
    for rec in cr:
        if rec!=[]:
            if rec[0]==m:
                j=rec[3]
    f.close()
    g=open('playlist.txt','a+',newline='')
    cr=csv.reader(g,lineterminator='\n')
    try:
        l2=next(cr)
    except StopIteration:
        l2=[]
        pass
    cw=csv.writer(g,delimiter=',')
    flag=True
    for rec in l2:
        if rec!=[]:
            if rec[1]==m and rec[2]==n:
                print('playlist already exists')
                flag=False    
    if flag==True:
        a=[j,m,n]
        cw.writerow(a)
        g.close()
        filename=n+'.txt'
        f1=open(filename,'w' , newline='')
        cw=csv.writer(f1,delimiter=',')
        fields=['song_id','songname','artist','album','decade','mood','genre']
        cw.writerow(fields)
        f1.close()
        print('-'*33+'playlist created'+'-'*34)
#function to add song to a playlist (for user)
def add_songp(n):
    while True:
        x=search()
        f=open('playlist.txt','r')
        cr=csv.reader(f,lineterminator='\n')
        l1=next(cr)
        reclist=[]
        for rec in cr:
            if rec!=[]:
                pln=rec[2]
                reclist.append(pln)
        if n not in reclist:
                print("playlist does not exist")
                break
        else:
            pass
        filename=n+'.txt'
        f1=open(filename,'a' , newline='')
        cw=csv.writer(f1,delimiter=',')
        if x!='song not available' and x!='please enter a valid choice':
            y=list(x)
            cw.writerow(y)            
            print('-'*30+"song successfully added"+'-'*30)
        else:
            print(x)
        f1.close()
        g=input("do you want to add more songs y/n: ")
        if g=='y':
            continue
        elif g=='n':
            break
        else:
            print('enter a valid choice')

#function to delete song from a playlist (for user)
def delete_songp(n):
    while True:        
        nm=input("enter song to be deleted: ")
        ar=input("enter name of the artist of the song: ")
        filename=n+'.txt'
        f1=open(filename,'r')
        cr=csv.reader(f1,lineterminator='\n')
        fields=['song_id','songname','artist','album','decade','mood','genre']
        reclist=[]
        flag=False
        l1=next(cr)
        print(l1)
        for rec in cr:
            if rec!=[]:
                reclist.append(rec)
                if rec[1]==nm and rec[2]==ar:
                    flag=True
        if reclist==[]:
            print("empty playlist")
        f1.close()
        if flag==False:
            print('record not found')
        else:
            g=open(filename,'w' , newline='')
            cw=csv.writer(g,delimiter=',')
            cw.writerow(fields)
            for r in reclist:
                if r!=[]:
                    if r[1]==nm and r[2]==ar:
                        print(r)
                        ans=input('do you want to delete this record? y/n: ')
                        if ans=='y':
                            print('-'*28+'record successfully deleted'+'-'*28)
                            pass
                        else:
                            print('-'*33+'record not deleted'+'-'*32)
                            cw.writerow(r)
                    else:
                        cw.writerow(r)
            g.close()
        d=input("do you want to select another song to remove? y/n: ")
        if d=='y':
            continue
        else:
            break

#function to view playlist
def view_playlist(r,t):
    g=open('playlist.txt','r')
    cr=csv.reader(g,lineterminator='\n')
    fields=next(cr)
    flag=False
    for rec in cr:
        if rec!=[]:
            if rec[2]==r and rec[0]==t:
                flag=True
    g.close()
    if flag==False:
        print('playlist does not exist')
    else:
        filename=r+'.txt'
        f1=open(filename,'r')
        cr=csv.reader(f1,lineterminator='\n')
        fields=next(cr)
        data=[]
        l=[]
        for rec in cr:
            if rec!=[]:
                l=[rec[1],rec[2]]
                data.append(l)                
        if data==[]:
            print('empty playlist')
        else:
            x=tabulate(data,[fields[1],fields[2]],tablefmt='pretty')
            print(x)
        f1.close()

# deleting playlist
def delete_playlist(r,t):    
    view_playlist(r,t)
    b=input('do you want to delete this playlist? y/n: ')
    filename=r+'.txt'
    if b=='y':
        os.remove(filename)      
        f=open('playlist.txt','r')
        cr=csv.reader(f,lineterminator='\n')
        fields=['playlist_id','username','playlistname']
        reclist=[]
        for rec in cr:
            if rec!=[]:
                reclist.append(rec)
        f.close()
        g=open('playlist.txt','w' , newline='')
        cw=csv.writer(g,delimiter=',')
        cw.writerow(fields)
        for i in range(1,len(reclist)):
            if rec[2]==r and rec[0]==t:
                pass
            else:
                cw.writerow(rec)
        print('-'*33+'playlist deleted'+'-'*34)
        g.close()
    elif b=='n':
        print('playlist not deleted')
    else:
        print('enter a valid choice')

    
