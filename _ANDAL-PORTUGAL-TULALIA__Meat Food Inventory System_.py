#Portugal, Jallen
#Tulalian Marcos
#Andal Maria
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkinter import*
from datetime import datetime


class MeatInventorySystem:

    def __init__(self,root):
        self.root=root
        self.root.title("Meat Food Invetory System")
        self.root.geometry("1225x800")
        self.root.configure(bg="white")
        title=Label(self.root,text="Meat Food Inventory System",font=("Poppins",30,"bold"),bg="#112D4E",fg="white",anchor="w",padx=15).place(x=0,y=0,relwidth=1)
              #ORDER DETAILS
        self.var_name = StringVar()
        self.var_meat_type = StringVar()
        self.var_quantities = IntVar()
        self.var_email = StringVar()
        self.var_totalprice = IntVar()
        self.var_paymet = IntVar()
        self.var_balance = IntVar()
        self.current_date = datetime.now().strftime("%Y-%m-%d")

              #ENVENTORY DETAILS
        self.var_add_meat = IntVar()
        self.var_remove_meat = IntVar()
        self.var_week_sales = IntVar()
        self.var_month_sales = IntVar()
        self.var_year_sales = IntVar()

                                # FRAME 1 ORDER DETAILS
        Frame1=Frame(self.root,bd=2,relief=RIDGE, bg="#DBE2EF")
        Frame1.place(x=25,y=70,width=600,height=350)
        title2=Label(Frame1,text="Order Details",font=("Poppins",18,"bold"),bg="#112D4E",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        self.price = Label(Frame1, text="1 Quantity/kg = ₱200",font=("Poppins",18,"bold"),bg="#112D4E",fg="white",anchor="w",padx=10).place(x=320,y=0,relwidth=1)
                
                                # Forms na
        self.name = Label(Frame1,text="Name",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.name.place(x=20,y=70)
                
        self.entry_name = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.var_name, bg = "white", fg = "black")
        self.entry_name.place(x=150,y=70,width=300)

        self.meat_type = Label(Frame1,text="Meat Type",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.meat_type.place(x=20,y=100)
                
        self.meat_type_entry = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.meat_type, bg = "white",fg = "black")
        self.meat_type_entry.place(x=150,y=100,width=300)
                
        self.quantity = Label(Frame1,text="Quantities",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.quantity.place(x=20,y=130)
                
        self.quantity_entry = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.var_quantities, bg ="white",fg = "black")
        self.quantity_entry.place(x=150,y=130,width=300)

        self.date = Label(Frame1,text="Date",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.date.place(x=20,y=160)
                
        self.date_today = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.current_date, bg ="white",fg = "black" ,state=DISABLED)
        self.date_today.place(x=150,y=160,width=300)

        self.totalprice = Label(Frame1,text="Total Price",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.totalprice.place(x=20,y=190)
                
        self.totalprice_entry = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.var_totalprice, bg ="white",fg = "black", state=DISABLED)
        self.totalprice_entry.place(x=150,y=190,width=300)

        self.balance = Label(Frame1,text="Change",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.balance.place(x=20,y=280)
                
        self.balance_entry = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.var_balance, bg ="white",fg = "black", state=DISABLED)
        self.balance_entry.place(x=150,y=280,width=100)

                                #ORDER DETAILS BUTTON
        enter_button = Button(Frame1,text = "Enter", font=("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.order_button )
        enter_button.place(x=300,y=273,width=100)

        self.paymet = Label(Frame1,text="Payments",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.paymet.place(x=20,y=220)

        self.payment_entry = Entry(Frame1,font = ("Poppins",15,"bold"), textvariable = self.var_paymet, bg ="white",fg = "black")
        self.payment_entry.place(x=150,y=220,width=300,height=25)


                                #FRAME 2 ENVENTORY DETAILS
        Frame2=Frame(self.root,bd=2,relief=RIDGE, bg="#DBE2EF")
        Frame2.place(x=650,y=70,width=550,height=350)
        title3=Label(Frame2,text="Inventory Details",font=("Poppins",18,"bold"),bg="#112D4E",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
                
        self.inventory = Label(Frame2,text="Stocks",font=("Poppins",18,"bold"),bg="#112D4E",fg="white")
        self.inventory.place(x=330,y=0)

        self.inventory_entry  = Entry(Frame2,font = ("Poppins",15,"bold"), bg = "white",fg = "black",state=DISABLED)
        self.inventory_entry.place(x=420,y=2,width=100)

        self.add_meat = Label(Frame2,text="Add Meat",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.add_meat.place(x=20,y=50)
                
        self.add_meat_entry = Entry(Frame2,font = ("Poppins",15,"bold"), textvariable = self.var_add_meat, bg = "white",fg = "black")
        self.add_meat_entry.place(x=170,y=50)
                
                                #ADD BUTTON
        add_button = Button(Frame2,text = "Add", font = ("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.add_stock)
        add_button.place(x=420,y=40,width=100)

        self.remove_meat = Label(Frame2,text="Remove Meat",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.remove_meat.place(x=20,y=100)

        self.remove_meat_entry = Entry(Frame2,font = ("Poppins",15,"bold"), textvariable = self.var_remove_meat, bg = "white", fg = "black",)
        self.remove_meat_entry.place(x=170,y=100)

                                #REMOVE BUTTON
        remove_button = Button(Frame2,text = "Remove", font = ("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.del_meat)
        remove_button.place(x=420,y=90,width=100)

        self.week_sale = Label(Frame2,text="Sales per Week",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.week_sale.place(x=20,y=155)

        self.week_sale_entry = Entry(Frame2,font = ("Poppins",15,"bold"), textvariable = self.var_week_sales, bg = "white", fg = "black", state=DISABLED)
        self.week_sale_entry.place(x=200,y=155,width=300)

                                #WEEK BUTTON
        week_button = Button(Frame2,text = "Week", font = ("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.total_sales_per_week)
        week_button.place(x=75,y=280,width=100)

        self.month_sale = Label(Frame2,text="Sales per Month",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.month_sale.place(x=20,y=194)

        self.month_sale_entry = Entry(Frame2,font = ("Poppins",15,"bold"), textvariable = self.var_month_sales, bg = "white", fg = "black", state=DISABLED)
        self.month_sale_entry.place(x=200,y=192,width=300)

                                #MONTH BUTTON
        month_button = Button(Frame2,text = "Month", font = ("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.monthly_sales)
        month_button.place(x=225,y=280,width=100)

        self.year_sale = Label(Frame2,text="Sales per Year",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
        self.year_sale.place(x=20,y=230)

        self.year_sale_entry = Entry(Frame2,font= ("Poppins",15,"bold"), textvariable = self.var_year_sales, bg = "white", fg = "black", state=DISABLED)
        self.year_sale_entry.place(x=200,y=230,width=300)
                                
                                #YEAR BUTTON
        year_button = Button(Frame2,text = "Year", font = ("Poppins",15,"bold"), bg = "#112D4E", fg = "#F9F7F7", command = self.yearly_sales)
        year_button.place(x=375,y=280,width=100)
                

                                # Frame 3 Customer Details
        Frame3=Frame(self.root,bd=2,relief=RIDGE, bg="#DBE2EF")
        Frame3.place(x=25,y=440,width=1175,height=225)
        title3=Label(Frame3,text="Customer Details",font=("Poppins",18,"bold"),bg="#112D4E",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


    def order_button(self):
      if self.entry_name.get() == "" or self.meat_type_entry.get() == "" or self.quantity_entry.get() == "" or self.payment_entry.get() == "" :
        messagebox.showerror("Error",f"Customer Details Must Required")

      else:
        try:
          con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
          cursor = con.cursor()
          tot_price = float(self.quantity_entry.get()) + 199 * float(self.quantity_entry.get())
          change =  float((self.payment_entry.get())) - (tot_price)
          stocks = "SELECT quantity FROM stocks WHERE id = 1"
          cursor.execute(stocks)
          stk = cursor.fetchone()
          stkleft = stk[0] - float(self.quantity_entry.get())
          con.commit()
          if stk[0] >= float(self.quantity_entry.get()):
            if tot_price <= float(self.payment_entry.get()):
              query = "INSERT INTO orders (customer_name, meat_type, quantity, total_price, payments, cchange, transaction_date) VALUES ('"+ self.entry_name.get() + "', '"+ self.meat_type_entry.get() +"', '" +self.quantity_entry.get() +"', '"+ str(tot_price) +"', '"+ self.payment_entry.get() +"', '"+ str(change) +"', '"+ str(self.current_date) +"')"
              self.totalprice_entry.config(state=NORMAL)
              self.totalprice_entry.delete(0,END)
              self.totalprice_entry.insert(0, tot_price)
              self.totalprice_entry.config(state=DISABLED)

              self.balance_entry.config(state=NORMAL)
              self.balance_entry.delete(0,END)
              self.balance_entry.insert(0, change)
              self.balance_entry.config(state=DISABLED)

              self.date_today.config(state=NORMAL)
              self.date_today.delete(0, END)
              self.date_today.insert(0, self.current_date)
              self.date_today.config(state=DISABLED)

              stock_order = "UPDATE stocks SET quantity = '" + str(stkleft) + "'  WHERE id = 1"
              cursor.execute(stock_order)
              con.commit()

              name_output = Label(text=f"Name: \t      {self.entry_name.get()}",font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              meat_output = Label(text=f"Meat Type:   {self.meat_type_entry.get()}", font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              quantity_output = Label(text=f"Quantity:      {self.quantity_entry.get()}", font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              payment_output = Label(text=f"Payments:    {self.payment_entry.get()}", font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              totalprice_output = Label(text=f"Total:           {tot_price}", font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              change_output = Label(text=f"Change:       {change}", font=("Poppins",15,"bold"),bg="#DBE2EF",fg="black")
              name_output.place(x=45,y=480)
              meat_output.place(x=45,y=510)
              quantity_output.place(x=45,y=540)
              payment_output.place(x=45,y=570)
              totalprice_output.place(x=45,y=600)
              change_output.place(x=45,y=630)
              cursor.execute(query)
              con.commit()
              cursor.close()
              if con.is_connected():
                messagebox.showwarning("Data",f"Data Is Save Successfully")
                                                  
            else:
              messagebox.showerror("ERROR",f"INCUFFICIENT PAYMENTS")
          else:
            messagebox.showerror("Error",f"Not Enough Stocks")
                                
        except Error as error:
          messagebox.showerror("ERROR",f"{error}")
                                
        finally:
          if con.is_connected():
            con.close()
            messagebox.showwarning("Data",f"Data Is Close")
        
    def add_stock(self):
      self.stock = self.add_meat_entry.get()
      try:
        con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
        cursor = con.cursor()
        stocks = "SELECT quantity FROM stocks WHERE id = 1"
        cursor.execute(stocks)
        stk = cursor.fetchone()
        totalquan = int(stk[0]) + int(self.stock)
        self.inventory_entry.config(state=NORMAL)
        self.inventory_entry.delete(0,END)
        self.inventory_entry.insert(0,totalquan)
        self.inventory_entry.config(state=DISABLED)
        messagebox.showwarning("Add Meat",f"Meat Add [ {self.stock} ]")
        totquan = float(totalquan) - float(self.quantity_entry.get())
        con.commit()
        query = "UPDATE stocks SET quantity = '" + str(float(totquan)) + "'  WHERE id = 1"
        cursor.execute(query)
        con.commit()
        cursor.close()
        if con.is_connected():
          messagebox.showwarning("Data",f"Data Is Save Successfully")


      except Error as error:
        messagebox.showerror("ERROR",f"{error}")
                        
      finally:
        if con.is_connected():
          con.close()
          messagebox.showwarning("Data",f"Data Is Close")
        
    def del_meat(self):
      self.stock = self.remove_meat_entry.get()
      try:
        con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
        cursor = con.cursor()
        stocks = "SELECT quantity FROM stocks WHERE id = 1"
        cursor.execute(stocks)
        stk = cursor.fetchone()
        totalquan = int(stk[0]) - int(self.stock)
        if totalquan > int(self.stock):
          self.inventory_entry.config(state=NORMAL)
          self.inventory_entry.delete(0,END)
          self.inventory_entry.insert(0,totalquan)
          self.inventory_entry.config(state=DISABLED)
          messagebox.showwarning("Remove Meat",f"Meat remove [ {self.stock} ]")
          con.commit()
          query = "UPDATE stocks SET quantity = '"+ str(totalquan) + "'  WHERE id = 1"
          cursor.execute(query)
          con.commit()
          cursor.close()
        else:
          messagebox.showerror("Error",f"Not Enough Stocks")
        if con.is_connected():
          messagebox.showwarning("Data",f"Data Is Save Successfully")

      except Error as error:
        messagebox.showerror("ERROR",f"{error}")
                        
      finally:
        if con.is_connected():
          con.close()
          messagebox.showwarning("Data",f"Data Is Close")
        
    def total_sales_per_week(self):

      try:
        con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
        cursor = con.cursor()
        query = "SELECT SUM(total_price), DAYNAME(CURDATE()) FROM orders GROUP BY WEEK(transaction_date)"
        cursor.execute(query)
        sales_data = cursor.fetchall()
        weeksale = sales_data[0][0]
        self.week_sale_entry.config(state=NORMAL)
        self.week_sale_entry.delete(0,END)
        self.week_sale_entry.insert(0,weeksale)
        self.week_sale_entry.config(state=DISABLED)
        messagebox.showinfo("Week Sales",f"{sales_data[0]}")
        sales = "UPDATE weeksales SET total_sales = '"+ str(weeksale) +"' WHERE id = 1"
        cursor.execute(sales)
        con.commit()
                #kapag wala pang naiinsert na sales
        # sales = "INSERT INTO monthsales (total_sales) VALUES (%s)"
        # cursor.execute(sales, (monthsale,))
        if con.is_connected():
          messagebox.showwarning("Data",f"Data Is Save Successfully")

      except Error as error:
        messagebox.showerror("ERROR",f"{error}")
                        
      finally:
        if con.is_connected():
          con.close()
          messagebox.showwarning("Data",f"Data Is Close")
                
    def monthly_sales(self):
      try:
        con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
        cursor = con.cursor()
        query = "SELECT SUM(total_price), MONTHNAME(CURDATE()) FROM orders GROUP BY MONTH(transaction_date)"
        cursor.execute(query)
        sales_data = cursor.fetchall()
        monthsale = sales_data[0][0]
        self.month_sale_entry.config(state=NORMAL)
        self.month_sale_entry.delete(0,END)
        self.month_sale_entry.insert(0,monthsale)
        self.month_sale_entry.config(state=DISABLED)
        messagebox.showinfo("Month Sales",f"{sales_data[0]}")
        sales = "UPDATE monthsales SET total_sales = '"+ str(monthsale) +"' WHERE id = 1"
        cursor.execute(sales)
        con.commit()
                #kapag wala pang naiinsert na sales
        # sales = "INSERT INTO monthsales (total_sales) VALUES (%s)"
        # cursor.execute(sales, (monthsale,))
        if con.is_connected():
          messagebox.showwarning("Data",f"Data Is Save Successfully")

      except Error as error:
        messagebox.showerror("ERROR",f"{error}")

      finally:
        if con.is_connected():
          con.close()
          messagebox.showwarning("Data",f"Data Is Close")
                
    def yearly_sales(self):
      try:
        con = mysql.connector.connect(host="localhost",database="meat_db",user="root",password="portugaljallen3")
        cursor = con.cursor()
        query = "SELECT SUM(total_price), YEAR(CURDATE()) FROM orders GROUP BY YEAR(transaction_date)"
        cursor.execute(query)
        sales_data = cursor.fetchall()
        yearsale = sales_data[0][0]
        self.year_sale_entry.config(state=NORMAL)
        self.year_sale_entry.delete(0,END)
        self.year_sale_entry.insert(0,yearsale)
        self.year_sale_entry.config(state=DISABLED)
        messagebox.showinfo("Year Sales",f"{sales_data[0]}")
        sales = "UPDATE yearsales SET total_sales = '"+ str(yearsale) +"' WHERE id = 1"
        cursor.execute(sales)
        con.commit()
                #kapag wala pang naiinsert na sales
        # sales = "INSERT INTO yearsales (total_sales) VALUES (%s)"
        # cursor.execute(sales, (yearsale,))
        if con.is_connected():
          messagebox.showwarning("Data",f"Data Is Save Successfully")

      except Error as error:
        messagebox.showerror("ERROR",f"{error}")
                        
      finally:
        if con.is_connected():
          con.close()
          messagebox.showwarning("Data",f"Data Is Close")
                


root=Tk()
obj=MeatInventorySystem(root)
root.mainloop()