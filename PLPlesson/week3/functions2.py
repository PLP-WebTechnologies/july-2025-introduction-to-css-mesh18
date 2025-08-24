#positional arguments

def add(a,b):
    return a+b

print(f"the sum of two values are: {add(3,4)}")

def name(first_name,second_name):
  return f"{first_name} {second_name}"
print(f"Hey my name is: {name("Meshack","Magara")}")


#creating a user output

def create_user(username: str , email : str , isadmin : bool = False):
   role = "admin" if isadmin else "user"

   return{"username:": username, "email:":email, "role": role}

user1 = create_user("Johndoue","johndoe@gmail.com",False)
user2 = create_user("Asmith","asmith#43@gmail.com",True)

print(f"user1 = {user1}")
print(f" user2 = {user2}")

#Default Arguments
def greet(name,greeting = "hello"):
   return f"{greeting}, {name}"
print("outputting the value without passing the parameters:")
print(greet("Alice"))
print("outputting the value after passing the parameter values : ")
print(greet("bob","hi!"))

def book(title,author = "unknown",year = 2020):
   return f"{title} by {author}, published in {year}"
print("outputting the value without passing the parameters:")
print(book("python 101"))

print("outputting the value after passing the parameter values : ")
print(book("python 101","guido", 1991))

def connect (host, port = 80, use_ssl = False):
   return f"Connecting to {host}:{port} with SSL = {use_ssl}"

print(connect("localhost"))

#sending urgent messages

def send_message(to, message, urgent = False, attachments = None):
   if attachments is None:
      attachments = []
   status = "URGENT" if urgent else "normal"

   return f"To: {to} | {status} | {len(attachments)} attachments"

print(send_message("team@example.com","update",urgent = True))

print(send_message("team@example", "update",True,attachments = ["notes.pdf","emailcard"]))

def format_order(meal,side = "fries",quantity = 1):
   return f"order: {quantity} X {meal} with {side}"

print(format_order("Burger"))
print(format_order("Salad",quantity = 2))
print(format_order("pizza",side = "sides", quantity = 3))