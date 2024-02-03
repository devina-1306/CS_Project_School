#importing required modules
import os
import os.path
import csv
from tabulate import tabulate
#importing functions created in another file
from functions_final import *

#creating logindata file
if os.path.isfile('logindata.txt'):
    print('logindata already exists')
else:
    f=open('logindata.txt','w' , newline='')
    cw=csv.writer(f,delimiter=',')
    fields=['username','email_id','password','playlist_id','user_type']
    cw.writerow(fields)
    #Adding Admin's data to login data
    l=[['devina goel','devina13@gmail.com','loginadmin1','1','admin'],['srishti paul','srishti7@gmail.com','loginadmin2','2','admin'],\
['shreenidhi','shreenidhi@gmail.com','loginadmin3','3','admin']]
    for rec in l:
        cw.writerow(rec)
    f.close()

#creating songs file
if os.path.isfile('songs.txt'):
    print('songs already exists')
else:
    f=open('songs.txt','w' , newline='')
    cw=csv.writer(f,delimiter=',')
    fields=['song_id','songname','artist','album','decade','mood','genre']
    cw.writerow(fields)
    f.close()

#creating file for list of playlists
if os.path.isfile('playlist.txt'):
    print('playlist already exists')
else:
    f=open('playlist.txt','w' , newline='')
    cw=csv.writer(f,delimiter=',')
    fields=['playlist_id','username','playlistname']
    cw.writerow(fields)
    f.close()
a='*'*83
b='WELCOME TO PLAYLISTX'.center(83)
c='*'*83
print(a,b,c,sep='\n')
while True:
    print("1: Sign Up")
    print("2: Sign In")
    print('0: Log Out')
    z=int(input("ENTER YOUR CHOICE: "))
    if z==1:
        #code for sign up
        u=input('enter username: ')
        if username(u)=="username not available":
            print("username already exists")
            continue
        else:
            p=input('enter password: ')
            c=input('confirm password: ')
            if password(p,c)!=True:
                print(password(p,c))
                continue
            else:
                e=input('enter email ID: ')
                if email_id(e)!=True:
                    print(email_id(e))
                    continue
                else:
                    i=playlist_id()
                    ut='user'
                    f=open('logindata.txt','a')
                    cw=csv.writer(f,delimiter=',')
                    rec=[u,e,p,i,ut]
                    cw.writerow(rec)
                    f.close()
                    print('signed up successfully')
                    continue
    elif z==2:
        #code for signing in
        while True:
            print("SIGN IN BY:","1: Username","2: Email","0: Exit",sep='\n')
            n=int(input('ENTER YOUR CHOICE: '))
            if n==1:
                m=input('enter username: ')
                p=input('enter password: ')
                i=signin(m,p,n)
                if i!='login successful':
                    print(i)
                    print('please try again or create a new account')
                    continue
                else:
                    print(i)
                    f=open('logindata.txt','r')
                    cr=csv.reader(f)
                    fields=next(cr)
                    for rec in cr:
                        if rec!=[]:
                            if rec[0]==m:
                                a=rec[4]
                    f.close()
                    if a=='user':
                        #sub menu for user
                        while True:
                            print('1: Search','2: Create Playlist','3: View Playlist','4: Edit Playlist','0: Log Out',sep='\n')
                            l=int(input('ENTER YOUR CHOICE: '))
                            if l==1:
                                print(search())
                                continue
                            elif l==2:
                                n=input('enter playlist name: ')
                                playlist_name(n)
                                continue
                            elif l==3:
                                g=open('logindata.txt','r')
                                cr=csv.reader(g,lineterminator='\n')
                                fields=next(cr)
                                for rec in cr:
                                    if rec!=[]:
                                        if rec[0]==m:
                                            t=rec[3]
                                g.close()
                                r=input('enter playlist name to be viewed: ')
                                view_playlist(r,t)
                            elif l==4:
                                #sub menu for editing playlist
                                while True:
                                    print('1: Delete Playlist','2: Delete From Playlist','3: Add To Playlist','0: Exit',sep='\n')
                                    d=int(input('ENTER YOUR CHOICE: '))
                                    if d==1:
                                        g=open('logindata.txt','r')
                                        cr=csv.reader(g,lineterminator='\n')
                                        fields=next(cr)
                                        for rec in cr:
                                            if rec!=[]:
                                                if rec[0]==m:
                                                    t=rec[3]
                                        g.close()
                                        r=input('enter name of playlist to be deleted: ')
                                        delete_playlist(r,t)                                 
                                    elif d==2:
                                        r=input('enter name of the playlist from which song is to be deleted: ')
                                        delete_songp(r)
                                    elif d==3:
                                        r=input('enter name of the playlist to which song is to added: ')
                                        add_songp(r)
                                    elif d==0:
                                        break
                                    else:
                                        print('enter a valid choice')
                                        continue
                            elif l==0:
                                break
                            else:
                                print('enter a valid choice')
                                continue
                    elif a=='admin':
                        #sub menu for admin
                        while True:
                            print('1: View Logindata','2: Edit Songs File','3: View All Playlists Name','0: Exit',sep='\n')
                            l=int(input('ENTER YOUR CHOICE: '))
                            if l==1:
                                f1=open('logindata.txt','r')
                                cr=csv.reader(f1,lineterminator='\n')
                                fields=next(cr)
                                data=[]                            
                                for rec in cr:
                                    if rec!=[]:
                                        data.append(rec)
                                x=tabulate(data,fields,tablefmt='pretty')
                                print(x)
                                f1.close()
                            elif l==2:
                                #sub menu for editing song file
                                while True:
                                    print('1: Add Song','2: Delete Song','3: Update Song','4: View Songs','0: Exit',sep='\n')
                                    d=int(input('ENTER YOUR CHOICE: '))
                                    if d==1:
                                        addsong()
                                    elif d==2:
                                        deletesong()
                                    elif d==3:
                                        updatesong()
                                    elif d==4:
                                        f1=open('songs.txt','r')
                                        cr=csv.reader(f1,lineterminator='\n')
                                        fields=['song_id','songname','artist','album','decade','mood','genre']
                                        data=[]
                                        l2=next(cr)
                                        for rec in cr:
                                            if rec!=[]:
                                                data.append(rec)
                                        x=tabulate(data,fields,tablefmt='pretty')
                                        print(x)
                                        f1.close()
                                    elif d==0:
                                        break
                                    else:
                                        print('enter a valid choice')
                                        continue
                            elif l==3:                            
                                f1=open('playlist.txt','r')
                                cr=csv.reader(f1,lineterminator='\n')
                                fields=next(cr)
                                data=[]                            
                                for rec in cr:
                                    if rec!=[]:
                                        data.append(rec)
                                x=tabulate(data,fields,tablefmt='pretty')
                                print(x)
                                f1.close()
                            elif l==0:
                                break
                            else:
                                print('enter a valid choice')
                                continue
            elif n==2:
                #signing in using email id
                m=input('enter email: ')
                p=input('enter password: ')
                i=signin(m,p,n)
                print(i)
                if i!='login successful':
                    print('please try again or create a new account')
                    continue
                else:
                    print(i)
                    f=open('logindata.txt','r')
                    cr=csv.reader(f,lineterminator='\n')
                    fields=next(cr)
                    for rec in cr:
                        if rec!=[]:
                            if rec[1]==m:
                                a=rec[4]
                    f.close()
                    if a=='user':
                        #sub menu for user
                        while True:
                            print('1: Search','2: Create Playlist','3: View Playlist','4: Edit Playlist','0: Log Out',sep='\n')
                            l=int(input('ENTER YOUR CHOICE: '))
                            if l==1:
                                print(search())
                                continue
                            elif l==2:
                                n=input('enter playlist name: ')
                                playlist_name(n)
                                continue
                            elif l==3:
                                g=open('logindata.txt','r')
                                cr=csv.reader(g,lineterminator='\n')
                                fields=next(cr)
                                for rec in cr:
                                    if rec!=[]:
                                        if rec[1]==m:
                                            t=rec[3]
                                g.close()
                                r=input('enter playlist name to be viewed: ')
                                view_playlist(r,t)
                            elif l==4:
                                #sub menu for editing playlist
                                while True:
                                    print('1: Delete Playlist','2: Delete From Playlist','3: Add To Playlist','0: Exit',sep='\n')
                                    d=int(input('ENTER YOUR CHOICE: '))
                                    if d==1:
                                        g=open('logindata.txt','r')
                                        cr=csv.reader(g,lineterminator='\n')
                                        fields=next(cr)
                                        for rec in cr:
                                            if rec!=[]:                                                
                                                if rec[1]==m:
                                                    t=rec[3]
                                        g.close()
                                        r=input('enter name of playlist to be deleted: ')
                                        delete_playlist(r,t)                                 
                                    elif d==2:
                                        r=input('enter name of the playlist from which song is to be deleted: ')
                                        delete_songp(r)
                                    elif d==3:
                                        r=input('enter name of the playlist to which song is to added: ')
                                        add_songp(r)
                                    elif d==0:
                                        break
                                    else:
                                        print('enter a valid choice')
                                        continue
                            elif l==0:                                
                                break
                            else:
                                print('enter a valid choice')
                                continue
                    elif a=='admin':
                        #sub menu for admin
                        while True:
                            print('1: View Logindata','2: Edit Song File','3: View All Playlists Name','0: Exit',sep='\n')
                            l=int(input('ENTER YOUR CHOICE: '))
                            if l==1:
                                f1=open('logindata.txt','r')
                                cr=csv.reader(f1,lineterminator='\n')
                                fields=next(cr)
                                data=[]                            
                                for rec in cr:
                                    if rec!=[]:
                                        data.append(rec)
                                x=tabulate(data,fields,tablefmt='pretty')
                                print(x)
                                f1.close()
                            elif l==2:
                                #sub menu for editing song file
                                while True:
                                    print('1: Add Song','2: Delete Song','3: Update Song','4: View Songs','0: Exit',sep='\n')
                                    d=int(input('ENTER YOUR CHOICE: '))
                                    if d==1:
                                        addsong()
                                    elif d==2:
                                        deletesong()
                                    elif d==3:
                                        updatesong()
                                    elif d==4:
                                        f1=open('songs.txt','r')
                                        cr=csv.reader(f1,lineterminator='\n')
                                        fields=next(cr)
                                        data=[]                            
                                        for rec in cr:
                                            if rec!=[]:
                                                data.append(rec)
                                        x=tabulate(data,fields,tablefmt='pretty')
                                        print(x)
                                        f1.close()
                                    elif d==0:
                                        break
                                    else:
                                        print('enter a valid choice')
                                        continue
                            elif l==3:                            
                                f1=open('playlist.txt','r')
                                cr=csv.reader(f1,lineterminator='\n')
                                fields=next(cr)
                                data=[]                            
                                for rec in cr:
                                    if rec!=[]:
                                        data.append(rec)
                                x=tabulate(data,fields,tablefmt='pretty')
                                print(x)
                                f1.close()
                            elif l==0:                                
                                break
                            else:
                                print('enter a valid choice')
                                continue
                        
            elif n==0:
                break
    #ending program
    elif z==0:
            print('*'*83)
            print('YOU HAVE BEEN LOGGED OUT'.center(83))
            print('*'*83)
            break
    else:
        print('enter a valid choice')
        continue
