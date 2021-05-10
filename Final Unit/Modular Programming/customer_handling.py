import json

def main():

    with open("customer_database.json") as file:
        customer_data = json.load(file)

    print(customer_data["customers"][0]["name"])

    for client in customer_data["customers"]:
        print("")
        print("")
        print("Checking client: ", client["name"])

        if payment_check(client["days_since_last_payment"]):
            print("Client recently paid: dispatching loot box (appending to purchase count)")
            send_email(client["email_address"], "Thanks for staying with us, your loot box has been dispatched")

            #check if new customer
            client_freshness = new_client_check(client["purchases"])
            if client_freshness == True:
                print("Client is new; dispatching gift box")
                send_email(client["email_address"], "Looks like you're new here, here is a litte something for you.")
            
        else:
            print("Client: ", client["name"], ", has not paid: no loot box")
            send_email(client["email_address"], "Looks like we haven't recieved a payment yet, hurry before the loot boxes are gone.")

#checks last payment
def payment_check(client_last_payment, cycle = 14):
    if client_last_payment > cycle:
        return False
    else:
        return True

#checks if new customer
def new_client_check(purchases_count):
    if purchases_count == 1:
        return True
    else:
        return False

#sends message to client if email provided
def send_email(client_email, message_content):
    if client_email == None:
        print("Client email missing, unable to send notification.")
    else:
        print("Sending email to: ", client_email, " message: ", message_content)

main()