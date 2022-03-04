n = int(input("enter the number of inputs:"))
newlist = []
for i in range(0,n):
    product = input("enter the product name:")
    price = input("enter the product price:")
    gst = input("enter the product gst:")
    productlist={
        "product_name": product,
        "product_price": price,
        "product_gst": gst
    }
    newlist.append(productlist)
    productlist.copy()
    print(newlist)