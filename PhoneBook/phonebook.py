from Tkinter import *
from tkMessageBox import *
import sqlite3 

root2=Tk()
con=sqlite3.Connection('hrdb2')
cur=con.cursor()
cur.execute("PRAGMA foreign_keys=ON")
cur.execute("create table if not exists contact(contactid integer primary key autoincrement,fname varchar(15),mname varchar(15),lname varchar(15),company varchar(15),address varchar(30),city varchar(15),pin integer,website varchar(15),dob date)")
cur.execute("create table if not exists phone(contactid integer, contype varchar(15),phno number(10),primary key(contactid,phno),foreign key(contactid) references contact(contactid) on delete cascade)")
cur.execute("create table if not exists email(contactid integer,emailidtype varchar(15),emailid varchar(15),primary key(contactid,emailid),foreign key(contactid) references contact(contactid) on delete cascade)")
root2.title('splash screen')
root2.geometry('700x700')
Label(root2,text='PROJECT OF PYTHON AND DATABASE',font="times 20").grid(row=1,column=1)
Label(root2,text='DEVELOPED BY: SAISYAMA PARUCHURU',font="times 20").grid(row=2,column=1)
Label(root2,text='************************',font="times 20").grid(row=3,column=1)
Label(root2,text='MAKE MOUSE MOVEMENT ON SCREEN TO CLOSE!!!',fg="red",font="times 20").grid(row=4,column=1)
def close(e=1):
    root2.destroy()
root2.bind('<Motion>',close)
root2.mainloop()


root=Tk()
root.title('phonebook')
root.configure(background='#80b3ff')
a=PhotoImage(file='img4.gif')
Label(root,image=a).grid(row=1,column=2)
Label(root,text="PHONE BOOK",font="times 20 bold ").grid(row=2,column=2)
Label(root,text="First Name",font="times 15  italic").grid(row=3,column=1)
r1=Entry(root)
r1.grid(row=3,column=2)
Label(root,text="Middle Name",font="times 15  italic").grid(row=4,column=1)
r2=Entry(root)
r2.grid(row=4,column=2)
Label(root,text="Last Name",font="times 15  italic").grid(row=5,column=1)
r3=Entry(root)
r3.grid(row=5,column=2)
Label(root,text="Company Name",font="times 15  italic").grid(row=6,column=1)
r4=Entry(root)
r4.grid(row=6,column=2)
Label(root,text="Address",font="times 15  italic").grid(row=7,column=1)
r5=Entry(root)
r5.grid(row=7,column=2)
Label(root,text="City",font="times 15  italic").grid(row=8,column=1)
r6=Entry(root)
r6.grid(row=8,column=2)
Label(root,text="Pin Code",font="times 15  italic").grid(row=9,column=1)
r7=Entry(root)
r7.grid(row=9,column=2)
Label(root,text="Website Url",font="times 15  italic").grid(row=10,column=1)
r8=Entry(root)
r8.grid(row=10,column=2)
Label(root,text="DOB",font="times 15  italic").grid(row=11,column=1)
r9=Entry(root)
r9.grid(row=11,column=2)

Label(root,text="Select Phone Type",fg="red",font="times 15  italic").grid(row=12,column=1)
v1=IntVar()
a1=Radiobutton(root,text="Office",variable=v1,value=1)
a1.grid(row=12,column=2)
a2=Radiobutton(root,text="Home",variable=v1,value=2)
a2.grid(row=12,column=3)
a3=Radiobutton(root,text="Mobile",variable=v1,value=3)
a3.grid(row=12,column=4)

Label(root,text="Phone Number",font="times 15 italic").grid(row=13,column=1)
r10=Entry(root)
r10.grid(row=13,column=2)

Label(root,text="Select Email Type",fg="red",font="times 15  italic").grid(row=14,column=1)
v2=IntVar()
a4=Radiobutton(root,text="Office",variable=v2,value=4)
a4.grid(row=14,column=2)
a5=Radiobutton(root,text="Personal",variable=v2,value=5)
a5.grid(row=14,column=3)

Label(root,text="Email Id",font="times 15 italic").grid(row=15,column=1)
r11=Entry(root)
r11.grid(row=15,column=2)


def search_box():
    root3=Tk()
    root3.title('search box')
    root3.geometry('500x700')
    Label(root3,text='searching phone book',font="times 20 bold").grid(sticky=N+W+E+S)
    Label(root3,text='enter the name',font="times 15 italic").grid(row=1,column=0,sticky=W)
    e1=Entry(root3)
    e1.grid(row=1,column=0)
    lb=Listbox(root3,height='35',width='90')
    lb.grid() 
    cur.execute("select contactid curval from contact")
    b=cur.fetchall()
    c=len(b)
    #cur.execute("select contactid,fname,mname,lname from contact")
    #xx=cur.fetchall()
    #print xx
    
    for i in range(c):
        cur.execute("select fname,mname,lname from contact where contactid=? order by fname,mname,lname",(b[i][0],))
        z=cur.fetchall()
        #print z
        for i in range(len(z)):
            lb.insert(i,z[i][0]+" "+z[i][1]+" "+z[i][2])
##for searching
    def value(e=1):
        #s=e1.get()
        #uni=unicode(s)
        lb.delete(0,END)
        global p
        cur.execute("select contactid,fname,mname,lname from contact where(fname like (?) or mname like(?) or lname like(?)) order by fname,mname,lname",('%'+e1.get()+'%','%'+e1.get()+'%','%'+e1.get()+'%'))
        p=cur.fetchall()
        for i in range(len(p)):
            lb.insert(i,p[i][1]+" "+p[i][2]+" "+p[i][3])

  
    e1.bind("<KeyRelease>",value)    

##for double pressing         
    def getvalue(e=1):
        #q=(lb.get(ACTIVE))
        #print q
        #cur.execute("select contactid from contact where fname=?",(q[0],))
        #w=cur.fetchall()
        u=lb.curselection()
        u1=u[0]
        #print u
        #print w
        w=p[u1][0]
        cur.execute("select fname,mname,lname,company,address,city,pin,website,dob from contact where contactid=?",(w,))
        j1=cur.fetchall()
        cur.execute("select contype,phno from phone where contactid=?",(w,))
        j2=cur.fetchall()
        cur.execute("select emailidtype,emailid from email where contactid=?",(w,))
        j3=cur.fetchall()
        lb.delete(0,END)
        lb.insert(0,"FIRST NAME     :"+(str)(j1[0][0]))
        lb.insert(1,"MIDDLE NAME    :"+(str)(j1[0][1]))
        lb.insert(2,"LAST NAME      :"+(str)(j1[0][2]))
        lb.insert(3,"COMPANY        :"+(str)(j1[0][3]))
        lb.insert(4,"ADDRESS        :"+(str)(j1[0][4]))
        lb.insert(5,"CITY           :"+(str)(j1[0][5]))
        lb.insert(6,"PIN            :"+(str)(j1[0][6]))
        lb.insert(7,"WEBSITE URL    :"+(str)(j1[0][7]))
        lb.insert(8,"DATE OF BIRTH  :"+(str)(j1[0][8]))

        lb.insert(9,"PHONE DETAILS.............")
        lb.insert(10,(str)(j2[0][0])+"  :"+(str)(j2[0][1]))
        lb.insert(11,"EMAIL ADDRESS.............")
        lb.insert(12,(str)(j3[0][0])+"  :"+(str)(j3[0][1]))

        def delete():
            cur.execute("delete from contact where contactid=?",w[0])
            cur.execute("delete from phone where contactid=?",w[0])
            cur.execute("delete from email where contactid=?",w[0])
            con.commit()
            lb.delete(0,END)
            showinfo("delete","contact removed successfully")
            

        Button(root3,text="delete",command=delete).grid(row=3,column=0)


    lb.bind("<<ListboxSelect>>",getvalue)
    
    def close(e=1):
        root3.destroy()
    Button(root3,text='close',command=close).grid(row=3,column=0)
    root3.mainloop()

def close_main():
    root.destroy()

def save():
    t1={1:'Office',2:'Home',3:'Mobile',4:'Office',5:'Personal'}
    
    cur.execute("insert into contact(fname,mname,lname,company,address,city,pin,website,dob) values(?,?,?,?,?,?,?,?,?)",(r1.get(),r2.get(),r3.get(),r4.get(),r5.get(),r6.get(),r7.get(),r8.get(),r9.get()))
    cur.execute("select contactid curval from contact")
    t2=cur.fetchall()
    #print t2
    t3=len(t2)-1
    #print t3
    t4=t2[t3][0]
    #print t4
    cur.execute("insert into phone(contactid,contype,phno) values(?,?,?)",(t4,t1.get(v1.get()),r10.get()))
    cur.execute("insert into email(contactid,emailidtype,emailid) values(?,?,?)",(t4,t1.get(v2.get()),r11.get()))
    con.commit()
    showinfo("info ", "you have successfully saved the record")

    r1.delete(0,END)
    r2.delete(0,END)
    r3.delete(0,END)
    r4.delete(0,END)
    r5.delete(0,END)
    r6.delete(0,END)
    r7.delete(0,END)
    r8.delete(0,END)
    r9.delete(0,END)
    r10.delete(0,END)
    r11.delete(0,END)
    v1.set(0)
    v2.set(0)
    



def edit_record():
    def cur_sel(e=1):
        
        tuple_x=() #for empty tuple
        if lb.curselection()!=tuple_x:
            index_tuple=lb.curselection()[0]
            #print display_list[index_tuple]
            global primary_key
            primary_key=display_list[index_tuple][0]
            #print lb.get(lb.curselection())
            lb.delete(0,END)
            cur.execute("select * from contact where contactid=?",(primary_key,))
            contact_edit_tuple=cur.fetchall()
            cur.execute("select * from phone where contactid=?",(primary_key,))
            phone_edit_tuple=cur.fetchall()
            cur.execute("select * from email where contactid=?",(primary_key,))
            email_edit_tuple=cur.fetchall()
            #root4=Tk(className='edit phonebook')
            root4=Toplevel()
            root3.destroy()#destroying root search window at edit selection
            Label(root4,text='First Name',font='times 15').grid(row=1,column=0)
            e11=Entry(root4)
            e11.grid(row=1,column=1)

            Label(root4,text='Middle Name',font='times 15').grid(row=2,column=0)
            e22=Entry(root4)
            e22.grid(row=2,column=1)

            Label(root4,text='Last Name',font='times 15').grid(row=3,column=0)
            e33=Entry(root4)
            e33.grid(row=3,column=1)

            Label(root4,text='Company Name',font='times 15').grid(row=4,column=0)
            e44=Entry(root4)
            e44.grid(row=4,column=1)

            Label(root4,text='Address',font='times 15').grid(row=5,column=0)
            e55=Entry(root4)
            e55.grid(row=5,column=1)

            Label(root4,text='City',font='times 15').grid(row=6,column=0)
            e66=Entry(root4)
            e66.grid(row=6,column=1)

            Label(root4,text='Pincode',font='times 15').grid(row=7,column=0)
            e77=Entry(root4)
            e77.grid(row=7,column=1)

            Label(root4,text='Website URL',font='times 15').grid(row=8,column=0)
            e88=Entry(root4)
            e88.grid(row=8,column=1)

            Label(root4,text='Date of birth',font='times 15').grid(row=9,column=0)
            e99=Entry(root4)
            e99.grid(row=9,column=1)
            #radio button entries
            
            r1=StringVar(value='1')
            Label(root4,text='Select Phone Type:',font='times 18',fg='#0059b3').grid(row=10,column=0)
            Radiobutton(root4,text='office',variable=r1,value='Office').grid(row=10,column=1)
            Radiobutton(root4,text='Home',variable=r1,value='Home').grid(row=10,column=2)            
            Radiobutton(root4,text='Mobile',variable=r1,value='Mobile').grid(row=10,column=3)
    
            Label(root4,text='Phone Number',font='times 15').grid(row=11,column=0)
            e101=Entry(root4)
            e101.grid(row=11,column=1)

            #radio button entries
            r2=StringVar(value='1')
            Label(root4,text='Select Email Type:',font='times 18',fg='#0059b3').grid(row=12,column=0)
            Radiobutton(root4,text='Home',variable=r2,value='Home').grid(row=12,column=1)
            Radiobutton(root4,text='Personal',variable=r2,value='Personal').grid(row=12,column=2)
            Label(root4,text='Email',font='times 15').grid(row=13,column=0)
            e111=Entry(root4)
            e111.grid(row=13,column=1)
           
            
           # print 'to be radiobutton v1',phone_edit_tuple[0][1]
           # print 'to be radiobutton v2',email_edit_tuple[0][1]

            #defaulting the edit values
            if contact_edit_tuple!=[]:
                e11.insert(0,contact_edit_tuple[0][1])
                e22.insert(0,contact_edit_tuple[0][2])
                e33.insert(0,contact_edit_tuple[0][3])
                e44.insert(0,contact_edit_tuple[0][4])
                e55.insert(0,contact_edit_tuple[0][5])
                e66.insert(0,contact_edit_tuple[0][6])
                e77.insert(0,contact_edit_tuple[0][7])
                e88.insert(0,contact_edit_tuple[0][8])
                e99.insert(0,contact_edit_tuple[0][9])
            if phone_edit_tuple!=[]:    
                r1.set(value=str(phone_edit_tuple[0][1]))
                e101.insert(0,phone_edit_tuple[0][2])
            if email_edit_tuple!=[]:
                r2.set(value=str(email_edit_tuple[0][1]))
                e111.insert(0,email_edit_tuple[0][2])
            def get_edit_values():
               # print 'on edit dunction calls'
                #print r1.get()
                #print r2.get()
                cur.execute("update contact set fname=?,mname=?,lname=?,company=?,address=?,city=?,pin=?,website=?,dob=? where contactid=?",(e11.get(),e22.get(),e33.get(),e44.get(),e55.get(),e66.get(),e77.get(),e88.get(),e99.get(),primary_key))
                con.commit()
                if phone_edit_tuple==[]:
                    cur.execute("insert into phone values(?,?,?)",(primary_key,r1.get(),e101.get()))
                    con.commit()
                else:
                    cur.execute("update phone set contype=?,phno=? where contactid=?",(r1.get(),e101.get(),primary_key))
                    con.commit()

                if email_edit_tuple==[]:
                    cur.execute("insert into email values(?,?,?)",(primary_key,r2.get(),e111.get()))
                    con.commit()
                else:
                    cur.execute("update email set emailidtype=?,emailid=? where contactid=?",(r2.get(),e111.get(),primary_key))
                    con.commit()
                root4.destroy()
                showinfo("update",'record updated successfully')
            Button(root4,text='save',command=get_edit_values).grid(row=14,column=1)
                    
            
            

    def close_search():
        root3.destroy()
    def show(e=1):
        lb.configure(state=NORMAL)
        lb.delete(0,END)
        part=('%'+e12.get()+'%',)
        cur.execute('select contactid,fname,mname,lname from contact where fname like ? ',part)
        global display_list
        display_list=cur.fetchall()
        c=1
        for i in display_list:
            lb.insert(c,i[1]+' '+i[2]+' '+i[3])
            c=c+1
        lb.bind("<<ListboxSelect>>", cur_sel)


    
    root3=Tk(className='Search')
    root3.geometry('480x500')
    Label(root3,text='Searching Phone Book',bg='light blue',font='times 17').grid(row=0,column=1)
    Label(root3,text='Enter Name:').grid(row=1,column=0)
    e12=Entry(root3)
    e12.grid(row=1,column=1)
    
    Button(root3,text='Close',command=close_search).grid(row=3,column=0)
    lb=Listbox(root3,width=38,height=18,fg="blue",font='times 14',selectmode= SINGLE)
    lb.grid(row=2,column=1)
    cur.execute("select contactid curval from contact")
    b=cur.fetchall()
    c=len(b)
   
    
    for i in range(c):
        cur.execute("select fname,mname,lname from contact where contactid=? order by fname,mname,lname",(b[i][0],))
        z=cur.fetchall()
        #print z
        for i in range(len(z)):
            lb.insert(i,z[i][0]+" "+z[i][1]+" "+z[i][2])
    e12.bind("<KeyPress>",show)
        

Button(root,text="save",command=save).grid(row=16,column=1)
Button(root,text="search",command=search_box).grid(row=16,column=2)
Button(root,text="close",command=close_main).grid(row=16,column=3)
Button(root,text="edit",command=edit_record).grid(row=16,column=4)

root.mainloop()

    
