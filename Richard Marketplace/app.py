from flask import Flask, request, render_template, session, redirect
import mysql.connector
import hashlib
import datetime
import os

app = Flask(__name__)
app.secret_key = b'v43gr8w46uh'

cnx = mysql.connector.connect(user='root',
                              password='123456',
                              host='127.0.0.1',
                              database='wad')


@app.route('/')
def home():  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    cursor.execute(f"select * from products where p_start <= '{time}' and p_end > '{time}' order by modified_time desc limit 3")
    promotions = cursor.fetchall()
    cursor.execute("select * from categories")
    categories = cursor.fetchall()
    cursor.execute("select * from products order by modified_time desc")
    catePros = cursor.fetchall()
    cursor.close()
    return render_template("home.html", promotions=promotions, categories=categories, catePros=catePros, time=time, buyer=session.get("buyerName"))


@app.route('/search', methods=['POST'])
def search():  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    keyword = request.form.get("keyword")
    cursor.execute(f"select * from products where name like '%{keyword}%' order by modified_time desc")
    products = cursor.fetchall()
    cursor.execute("select * from categories")
    categories = cursor.fetchall()
    cursor.close()
    return render_template("search.html", products=products, categories=categories, keyword=keyword, time=time, buyer=session.get("buyerName"))


@app.route('/prom')
def prom():  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    cursor.execute(f"select * from products where p_start <= '{time}' and p_end > '{time}' order by modified_time desc")
    products = cursor.fetchall()
    cursor.execute("select * from categories")
    categories = cursor.fetchall()
    cursor.close()
    return render_template("prom.html", products=products, categories=categories, time=time, buyer=session.get("buyerName"))


@app.route('/buyerRegister', methods=['GET', 'POST'])
def buyerRegister():  # put application's code here
    vars1 = ["Buyer Register", "/buyerRegister", "/buyerLogin"]
    vars2 = ["Buyer Login", "/buyerLogin", "/buyerRegister", "/vendorLogin"]
    if request.method == "GET":
        return render_template("register.html", vars=vars1)
    else:
        cursor = cnx.cursor()
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("phone")
        addr = request.form.get("addr")
        cursor.execute(f"select id from buyers where username = '{username}'")
        user = cursor.fetchone()
        print(user)
        if not user:
            hl = hashlib.md5()
            hl.update(password.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            cursor.execute(f"insert into buyers (username, password, email, phone, addr) values ('{username}', '{md5}', '{email}', '{phone}', '{addr}')")
            cnx.commit()
            cursor.close()
            return render_template("login.html", vars=vars2, notif1="Registering succeed! Please enter the username and password to log in.")
        else:
            cursor.close()
            return render_template("register.html", vars=vars1, notif="The user is already exist! Please change a username.")


@app.route('/vendorRegister', methods=['GET', 'POST'])
def vendorRegister():  # put application's code here
    vars1 = ["Vendor Register", "/vendorRegister", "/vendorLogin"]
    vars2 = ["Vendor Login", "/vendorLogin", "/vendorRegister", "/buyerLogin"]
    if request.method == "GET":
        return render_template("register.html", vars=vars1)
    else:
        cursor = cnx.cursor()
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("phone")
        addr = request.form.get("addr")
        cursor.execute(f"select id from vendors where username = '{username}'")
        user = cursor.fetchone()
        print(user)
        if not user:
            hl = hashlib.md5()
            hl.update(password.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            cursor.execute(f"insert into vendors (username, password, email, phone, addr) values ('{username}', '{md5}', '{email}', '{phone}', '{addr}')")
            cnx.commit()
            cursor.close()
            return render_template("login.html", vars=vars2, notif1="Registering succeed! Please enter the username and password to log in.")
        else:
            cursor.close()
            return render_template("register.html", vars=vars1, notif="The user is already exist! Please change a username.")


@app.route('/buyerLogin', methods=['GET', 'POST'])
def buyerLogin():  # put application's code here
    vars = ["Buyer Login", "/buyerLogin", "/buyerRegister", "/vendorLogin", "Vendor..."]
    if request.method == "GET":
        return render_template("login.html", vars=vars)
    else:
        cursor = cnx.cursor()
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute(f"select id, password from buyers where username = '{username}'")
        user = cursor.fetchone()
        cursor.close()
        if not user:
            return render_template("login.html", vars=vars, notif1="The user is not registered!")
        else:
            hl = hashlib.md5()
            hl.update(password.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            print(md5)
            id = user[0]
            passwordReal = user[1]
            if passwordReal != md5:
                return render_template("login.html", vars=vars, notif2="The password is wrong! Please enter again.")
            else:
                session["buyerId"] = id
                session["buyerName"] = username
                return redirect("/")


@app.route('/vendorLogin', methods=['GET', 'POST'])
def vendorLogin():  # put application's code here
    vars = ["Vendor Login", "/vendorLogin", "/vendorRegister", "/buyerLogin", "Buyer..."]
    if request.method == "GET":
        return render_template("login.html", vars=vars)
    else:
        cursor = cnx.cursor()
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute(f"select id, password from vendors where username = '{username}'")
        user = cursor.fetchone()
        cursor.close()
        if not user:
            return render_template("login.html", vars=vars, notif1="The user is not registered!")
        else:
            hl = hashlib.md5()
            hl.update(password.encode(encoding='utf8'))
            md5 = hl.hexdigest()
            print(md5)
            id = user[0]
            passwordReal = user[1]
            if passwordReal != md5:
                return render_template("login.html", vars=vars, notif2="The password is wrong! Please enter again.")
            else:
                session["vendorId"] = id
                session["vendorName"] = username
                return redirect("/orderManage")


@app.route('/buyerLogout')
def buyerLogout():  # put application's code here
    session.pop('buyerId')
    session.pop('buyerName')
    return redirect("/")


@app.route('/vendorLogout')
def vendorLogout():  # put application's code here
    session.pop('vendorId')
    session.pop('vendorName')
    return redirect("/vendorLogin")


@app.route('/info/<productId>')
def info(productId):  # put application's code here
    buyerId = session.get("buyerId")
    time = datetime.datetime.now()
    cursor = cnx.cursor()
    cursor.execute(f"select * from products where id = {productId}")
    product = cursor.fetchone()
    print(product)
    cursor.execute(f"select username from vendors where id = {product[2]}")
    vendor = cursor.fetchone()[0]
    print(vendor)
    cursor.execute(f"select name from categories where id = {product[7]}")
    category = cursor.fetchone()[0]
    print(category)
    like = ""
    if buyerId:
        cursor.execute(f"select status from likes where buyer_id = {buyerId} and product_id = {productId}")
        like = cursor.fetchone()
    print(like)
    cursor.execute(f"select c.*, b.username from comments c join buyers b on c.buyer_id = b.id where c.product_id = {productId} order by c.created_time desc")
    comments = cursor.fetchall()
    print(comments)
    cursor.close()
    return render_template("product_info.html", product=product, vendor=vendor, category=category, comments=comments, like=like, time=time, buyer=session.get("buyerName"))


@app.route('/comment/<productId>', methods=['POST'])
def comment(productId):  # put application's code here
    cursor = cnx.cursor()
    content = request.form.get("content")
    buyerId = session.get("buyerId")
    time = datetime.datetime.now()
    cursor.execute(f"insert into comments (buyer_id, product_id, content, created_time) values ({buyerId}, {productId}, '{content}', '{time}')")
    cnx.commit()
    cursor.execute(f"update products set modified_time = '{time}' where id = {productId}")
    cnx.commit()
    cursor.close()
    return redirect(f"/info/{productId}")


@app.route('/like/<productId>')
def like(productId):  # put application's code here
    cursor = cnx.cursor()
    buyerId = session.get("buyerId")
    time = datetime.datetime.now()
    cursor.execute(f"select likes, dislikes from products where id = {productId}")
    likeNum = cursor.fetchone()
    cursor.execute(f"select * from likes where buyer_id = {buyerId} and product_id = {productId}")
    likeRecord = cursor.fetchone()
    if not likeRecord:
        cursor.execute(f"insert into likes (buyer_id, product_id, status) values ({buyerId}, {productId}, 1)")
        cnx.commit()
        cursor.execute(f"update products set likes = {likeNum[0] + 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    elif likeRecord[3] == 1:
        cursor.execute(f"delete from likes where id = {likeRecord[0]}")
        cnx.commit()
        cursor.execute(f"update products set likes = {likeNum[0] - 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    else:
        cursor.execute(f"update likes set status = 1 where id = {likeRecord[0]}")
        cnx.commit()
        cursor.execute(f"update products set likes = {likeNum[0] + 1}, dislikes = {likeNum[1] - 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    cursor.close()
    return redirect(f"/info/{productId}")


@app.route('/dislike/<productId>')
def dislike(productId):  # put application's code here
    cursor = cnx.cursor()
    buyerId = session.get("buyerId")
    time = datetime.datetime.now()
    cursor.execute(f"select likes, dislikes from products where id = {productId}")
    likeNum = cursor.fetchone()
    cursor.execute(f"select * from likes where buyer_id = {buyerId} and product_id = {productId}")
    likeRecord = cursor.fetchone()
    if not likeRecord:
        cursor.execute(f"insert into likes (buyer_id, product_id, status) values ({buyerId}, {productId}, 0)")
        cnx.commit()
        cursor.execute(f"update products set dislikes = {likeNum[1] + 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    elif likeRecord[3] == 0:
        cursor.execute(f"delete from likes where id = {likeRecord[0]}")
        cnx.commit()
        cursor.execute(f"update products set dislikes = {likeNum[1] - 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    else:
        cursor.execute(f"update likes set status = 0 where id = {likeRecord[0]}")
        cnx.commit()
        cursor.execute(f"update products set likes = {likeNum[0] - 1}, dislikes = {likeNum[1] + 1}, modified_time = '{time}' where id = {productId}")
        cnx.commit()
    cursor.close()
    return redirect(f"/info/{productId}")


@app.route('/productManage')
def productManage():  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    vendor = session.get('vendorName')
    vendorId = session.get('vendorId')
    cursor.execute(f"select p.*, c.name from products p join categories c on p.category_id = c.id where p.vendor_id = '{vendorId}' order by p.modified_time desc")
    products = cursor.fetchall()
    cursor.close()
    return render_template("product_manage.html", products=products, time=time, vendor=vendor)


@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():  # put application's code here
    cursor = cnx.cursor()
    if request.method == "GET":
        vendor = session.get('vendorName')
        cursor.execute(f"select name from categories")
        categories = cursor.fetchall()
        check = ["", "", "", "", "checked"]
        vars = ["Upload", "/addProduct"]
        cursor.close()
        return render_template("product_edit.html", product=None, categories=categories, check=check, vars=vars, vendor=vendor)
    else:
        vendorId = session.get('vendorId')
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        categoryId = request.form.get("category_id")
        p_price = request.form.get("p_price")
        if p_price == "":
            p_price = None
        p_start = request.form.get("p_start")
        if p_start == "":
            p_start = None
        p_end = request.form.get("p_end")
        if p_end == "":
            p_end = None
        time = datetime.datetime.now()
        picture = request.files.get("picture")
        print(picture)
        src = ""
        if picture.filename != "":
            src = "/static/uploads/" + picture.filename
            path = os.path.abspath(os.path.dirname(__file__)) + src
            picture.save(path)
        cursor.execute("insert into products (name, vendor_id, description, price, category_id, modified_time, picture, p_price, p_start, p_end) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (name, vendorId, description, price, categoryId, time, src, p_price, p_start, p_end))
        cnx.commit()
        cursor.close()
        return redirect("/productManage")


@app.route('/editProduct/<productId>', methods=['GET', 'POST'])
def editProduct(productId):  # put application's code here
    cursor = cnx.cursor()
    if request.method == "GET":
        vendor = session.get('vendorName')
        cursor.execute(f"select * from products where id = {productId}")
        product = cursor.fetchone()
        cursor.execute(f"select name from categories")
        categories = cursor.fetchall()
        check = ["", "", "", "", ""]
        check[product[7] - 1] = "checked"
        vars = ["Modify", f"/editProduct/{productId}"]
        cursor.close()
        return render_template("product_edit.html", product=product, categories=categories, check=check, vars=vars, vendor=vendor)
    else:
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        categoryId = request.form.get("category_id")
        p_price = request.form.get("p_price")
        if p_price == "":
            p_price = None
        p_start = request.form.get("p_start")
        if p_start == "":
            p_start = None
        p_end = request.form.get("p_end")
        if p_end == "":
            p_end = None
        time = datetime.datetime.now()
        picture = request.files.get("picture")
        cursor.execute("update products set name=%s, description=%s, price=%s, category_id=%s, modified_time=%s, p_price=%s, p_start=%s, p_end=%s where id = %s",
                       (name, description, price, categoryId, time, p_price, p_start, p_end, productId))
        cnx.commit()
        if picture.filename != "":
            src = "/static/uploads/" + picture.filename
            path = os.path.abspath(os.path.dirname(__file__)) + src
            picture.save(path)
            cursor.execute(f"update products set picture='{src}' where id = {productId}")
            cnx.commit()
        cursor.close()
        return redirect("/productManage")


@app.route('/toDeleteProduct/<productId>')
def toDeleteProduct(productId):  # put application's code here
    vendor = session.get('vendorName')
    cursor = cnx.cursor()
    cursor.execute(f"select id, name, picture from products where id = {productId}")
    product = cursor.fetchone()
    cursor.close()
    return render_template("product_delete.html", product=product, vendor=vendor)


@app.route('/deleteProduct/<productId>')
def deleteProduct(productId):  # put application's code here
    cursor = cnx.cursor()
    cursor.execute(f"delete from products where id = {productId}")
    cnx.commit()
    cursor.execute(f"delete from carts where product_id = {productId}")
    cnx.commit()
    cursor.execute(f"delete from orders where product_id = {productId}")
    cnx.commit()
    cursor.close()
    return redirect("/productManage")


@app.route('/addCart/<productId>')
def addCart(productId):  # put application's code here
    buyerId = session.get("buyerId")
    quantity = request.args.get("quantity")
    cursor = cnx.cursor()
    cursor.execute(f"insert into carts (buyer_id, product_id, quantity) values ({buyerId}, {productId}, {quantity})")
    cnx.commit()
    cursor.close()
    return redirect("/cart")


@app.route('/cart')
def cart():  # put application's code here
    buyer = session.get("buyerName")
    buyerId = session.get("buyerId")
    time = datetime.datetime.now()
    cursor = cnx.cursor()
    cursor.execute(f"select p.*, c.id, c.quantity from carts c join products p on c.product_id = p.id where c.buyer_id = {buyerId} order by c.id desc")
    cartTemps = cursor.fetchall()
    carts = []
    total = 0
    for cartTemp in cartTemps:
        if cartTemp[11] and cartTemp[12] and cartTemp[11] <= time < cartTemp[12]:
            subTotal = cartTemp[14] * cartTemp[10]
        else:
            subTotal = cartTemp[14] * cartTemp[4]
        total += subTotal
        carts.append([cartTemp, subTotal])
    cursor.close()
    return render_template("cart.html", carts=carts, buyer=buyer, time=time, total=total)


@app.route('/plus/<cartId>')
def plus(cartId):  # put application's code here
    cursor = cnx.cursor()
    cursor.execute(f"select quantity from carts where id = {cartId}")
    quantity = cursor.fetchone()[0]
    if quantity < 100:
        cursor.execute(f"update carts set quantity = {quantity + 1} where id = {cartId}")
        cnx.commit()
    cursor.close()
    return redirect("/cart")


@app.route('/minus/<cartId>')
def minus(cartId):  # put application's code here
    cursor = cnx.cursor()
    cursor.execute(f"select quantity from carts where id = {cartId}")
    quantity = cursor.fetchone()[0]
    if quantity > 1:
        cursor.execute(f"update carts set quantity = {quantity - 1} where id = {cartId}")
        cnx.commit()
    cursor.close()
    return redirect("/cart")


@app.route('/order')
def order():  # put application's code here
    buyer = session.get("buyerName")
    buyerId = session.get("buyerId")
    cursor = cnx.cursor()
    cursor.execute(f"select o.*, p.picture from orders o join products p on o.product_id = p.id where o.buyer_id = {buyerId} order by o.id desc")
    orders = cursor.fetchall()
    cursor.close()
    return render_template("order.html", orders=orders, buyer=buyer)


@app.route('/orderManage')
def orderManage():  # put application's code here
    vendor = session.get("vendorName")
    vendorId = session.get("vendorId")
    cursor = cnx.cursor()
    cursor.execute(f"select o.*, p.picture from orders o join products p on o.product_id = p.id where o.vendor_id = {vendorId} order by o.id desc")
    orders = cursor.fetchall()
    cursor.close()
    return render_template("order_manage.html", orders=orders, vendor=vendor)


@app.route('/purchase/<productId>', methods=['GET', 'POST'])
def purchase(productId):  # put application's code here
    cursor = cnx.cursor()
    buyerId = session.get('buyerId')
    quantity = request.args.get("quantity")
    if request.method == "GET":
        time = datetime.datetime.now()
        cursor.execute(f"select price, p_price, p_start, p_end from products where id = {productId}")
        product = cursor.fetchone()
        if product[2] and product[3] and product[2] <= time < product[3]:
            price = product[1] * int(quantity)
        else:
            price = product[0] * int(quantity)
        vars = [f"/purchase/{productId}?quantity={quantity}&price={price}", f"/info/{productId}"]
        buyer = session.get('buyerName')
        cursor.execute(f"select addr from buyers where id = {buyerId}")
        addr = cursor.fetchone()[0]
        cursor.close()
        return render_template("payment.html", buyer=buyer, addr=addr, vars=vars, price=price)
    else:
        price = request.args.get("price")
        buyer = request.form.get("buyer")
        addr = request.form.get("addr")
        time = datetime.datetime.now()
        cursor.execute(f"select name, vendor_id from products where id = {productId}")
        product = cursor.fetchone()
        cursor.execute(f"insert into orders (track, created_time, addr, buyer, buyer_id, vendor_id, product_id, product, price, quantity) values ('Preparing', '{time}', '{addr}', '{buyer}', {buyerId}, {product[1]}, {productId}, '{product[0]}', {price}, {quantity})")
        cnx.commit()
        cursor.close()
        return redirect("/order")


@app.route('/purchaseCart/<cartId>', methods=['GET', 'POST'])
def purchaseCart(cartId):  # put application's code here
    cursor = cnx.cursor()
    buyerId = session.get('buyerId')
    price = request.args.get("price")
    if request.method == "GET":
        vars = [f"/purchaseCart/{cartId}?price={price}", "/cart"]
        buyer = session.get('buyerName')
        cursor.execute(f"select addr from buyers where id = {buyerId}")
        addr = cursor.fetchone()[0]
        cursor.close()
        return render_template("payment.html", buyer=buyer, addr=addr, vars=vars, price=price)
    else:
        buyer = request.form.get("buyer")
        addr = request.form.get("addr")
        time = datetime.datetime.now()
        cursor.execute(f"select product_id, quantity from carts where id = {cartId}")
        cart = cursor.fetchone()
        cursor.execute(f"select name, vendor_id from products where id = {cart[0]}")
        product = cursor.fetchone()
        cursor.execute(f"insert into orders (track, created_time, addr, buyer, buyer_id, vendor_id, product_id, product, price, quantity) values ('Preparing', '{time}', '{addr}', '{buyer}', {buyerId}, {product[1]}, {cart[0]}, '{product[0]}', {price}, {cart[1]})")
        cnx.commit()
        cursor.execute(f"delete from carts where id = {cartId}")
        cnx.commit()
        cursor.close()
        return redirect("/order")


@app.route('/purchaseAll', methods=['GET', 'POST'])
def purchaseAll():  # put application's code here
    cursor = cnx.cursor()
    buyerId = session.get('buyerId')
    if request.method == "GET":
        price = request.args.get("price")
        vars = [f"/purchaseAll", "/cart"]
        buyer = session.get('buyerName')
        cursor.execute(f"select addr from buyers where id = {buyerId}")
        addr = cursor.fetchone()[0]
        cursor.close()
        return render_template("payment.html", buyer=buyer, addr=addr, vars=vars, price=price)
    else:
        buyer = request.form.get("buyer")
        addr = request.form.get("addr")
        time = datetime.datetime.now()
        cursor.execute(f"select product_id, quantity, id from carts where buyer_id = {buyerId}")
        carts = cursor.fetchall()
        for cart in carts:
            cursor.execute(f"select name, vendor_id, price, p_price, p_start, p_end from products where id = {cart[0]}")
            product = cursor.fetchone()
            if product[4] and product[5] and product[4] <= time < product[5]:
                subTotal = product[3] * int(cart[1])
            else:
                subTotal = product[2] * int(cart[1])
            cursor.execute(f"insert into orders (track, created_time, addr, buyer, buyer_id, vendor_id, product_id, product, price, quantity) values ('Preparing', '{time}', '{addr}', '{buyer}', {buyerId}, {product[1]}, {cart[0]}, '{product[0]}', {subTotal}, {cart[1]})")
            cnx.commit()
            cursor.execute(f"delete from carts where id = {cart[2]}")
            cnx.commit()
        cursor.close()
        return redirect("/order")


@app.route('/toDeleteCart/<cartId>')
def toDeleteCart(cartId):  # put application's code here
    buyer = session.get('buyerName')
    cursor = cnx.cursor()
    cursor.execute(f"select c.id, p.name, p.picture from carts c join products p on c.product_id = p.id where c.id = {cartId}")
    cart = cursor.fetchone()
    cursor.close()
    return render_template("cart_delete.html", cart=cart, buyer=buyer)


@app.route('/deleteCart/<cartId>')
def deleteCart(cartId):  # put application's code here
    cursor = cnx.cursor()
    cursor.execute(f"delete from carts where id = {cartId}")
    cnx.commit()
    cursor.close()
    return redirect("/cart")


@app.route('/toReceive/<orderId>')
def toReceive(orderId):  # put application's code here
    buyer = session.get('buyerName')
    cursor = cnx.cursor()
    cursor.execute(f"select o.id, o.product, p.picture from orders o join products p on o.product_id = p.id where o.id = {orderId}")
    order = cursor.fetchone()
    cursor.close()
    return render_template("receive.html", order=order, buyer=buyer)


@app.route('/receive/<orderId>')
def receive(orderId):  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    cursor.execute(f"update orders set track = 'Completed', arrive_time = '{time}' where id = {orderId}")
    cnx.commit()
    cursor.close()
    return redirect("/order")


@app.route('/toDeliver/<orderId>')
def toDeliver(orderId):  # put application's code here
    vendor = session.get('vendorName')
    cursor = cnx.cursor()
    cursor.execute(f"select o.id, o.product, p.picture from orders o join products p on o.product_id = p.id where o.id = {orderId}")
    order = cursor.fetchone()
    cursor.close()
    return render_template("deliver.html", order=order, vendor=vendor)


@app.route('/deliver/<orderId>', methods=['POST'])
def deliver(orderId):  # put application's code here
    cursor = cnx.cursor()
    time = datetime.datetime.now()
    arriveTime = request.form.get("arrive_time")
    if arriveTime == "":
        arriveTime = None
    cursor.execute("update orders set track = 'Delivering', send_time = %s, arrive_time = %s where id = %s",
                   (time, arriveTime, orderId))
    cnx.commit()
    cursor.close()
    return redirect("/orderManage")


if __name__ == '__main__':
    app.run()
