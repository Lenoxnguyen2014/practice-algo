# Add <card_holder> <card_number> $: Add command will create a new credit card for the given card_holder, card_number, and limit. 
# It is guaranteed that the given card_holder didn't have a credit card before this operation.
# New cards start with a $0 balance.
# Cards numbers should be validated using basic validation.
# (Bonus) Card numbers should be validated using the Luhn 10 algorithm.
# Charge <card_holder> $: Charge command will increase the balance of the card associated with the provided name by the amount specified.
# Charges that would raise the balance over the limit are ignored as if they were declined.
# Charges against invalid cards are ignored.
# Credit <card_holder> $: Credit command will decrease the balance of the card associated with the provided name by the amount specified.
# Credits that would drop the balance below $0 will create a negative balance.
# Credits against invalid cards are ignored.
# Credit Card validation
# In order to ensure the credit card number is valid, we want to run some very basic validation.
# You need to ensure the string is only composed of digits [0-9] and is between 12 and 16 characters long (although most cards are 15 to 16, let's keep it simple).

# (Bonus) How the Luhn algorithm works:

# Starting with the rightmost digit, which is the check digit, and moving left, double the value of every second digit. 
# If the result of this doubling operation is greater than 9 (e.g., 8 * 2 = 16), then add the digits of the product (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9).
# Take the sum of all the digits.
# If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn algorithm, otherwise it is not valid.
# The last Unit Test will be testing for the Luhn algorithm.

# Luhn(number) = 7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 = 65 = 5 (mod 10) != 0

# Your Challenge

# Return the card holder names with the balance of the card associated with the provided name. The names in output should be displayed in lexicographical order.
# Display "error" instead of the balance if the credit card number does not pass validation.

# Example

# For

# operations = [["Add", "Tom", "4111111111111111", "$1000"],
# ["Add", "Lisa", "5454545454545454", "$3000"],
# ["Add", "Quincy", "12345678901234", "$2000"],
# ["Charge", "Tom", "$500"],
# ["Charge", "Tom", "$800"],
# ["Charge", "Lisa", "$7"],
# ["Credit", "Lisa", "$100"],
# ["Credit", "Quincy", "$200"]]
# the output should be

# creditCardProvider(operations) = [["Lisa", "$-93"],
# ["Quincy", "error"],
# ["Tom", "$500"]]
# Input/Output

# [execution time limit] 3 seconds (java)

# [input] array.array.string operations

# An array of operations. It is guaranteed that card limits and amounts of each operation are in the range [1, 3000]. It is also guaranteed that each card holder name will contain no more than 10 symbols and each card number will contain from 12 to 16 digits.

# Guaranteed constraints:
# 1 ≤ operations.length ≤ 10,
# 3 ≤ operations[i].length ≤ 4.

# [output] array.array.string

# Array of card holders and their card balances.

class Account:
    def __init__(self, operations):
        #make it this way so data is store globally and this should be private only in a class
        self.operations = operations
        self.card_holder = {}
        self.card_number = {}
        self.card_balance = {}
        self.card_limit = {}
        self.credit_balance = {}
        self.output = []
    
    def add(self, cardNum, name, cardLimit):
        isCardValid = "true" if self.cardValidator(cardNum) else "false"
        self.card_number[name] = cardNum + '_' + isCardValid
        self.card_limit[name] = int(cardLimit)
        return self.card_number, self.card_limit, self.card_balance
    
    def charge(self, amount, name):
        if self.card_number[name].split("_")[1] == "true":
            if self.credit_balance[name] + amount <= self.card_limit[name]:
                self.credit_balance[name] += amount
        return self.card_balance
    
    def credit(self, amount, name):
        if self.card_number[name].split("_")[1] == "true":
            self.credit_balance[name] -= amount

        return self.card_balance
    
    def cardValidator(self, cardNum):
        # Check the length of card between 12 and 16
        if len(cardNum) >= 12 and len(cardNum) <= 16:
            # All are digits in credit card number
            for c in cardNum:
                if not c.isdigit():
                    return False
        else:
            return False
    
        # Implement Luhn's Algorithm
        # to be honest, I know nothing about Luhn algo so this one I just copy 
        evenSum = 0
        oddSum = 0
        for i in range(len(cardNum)-1, -1, -1):
            if i % 2 == 0:
                x = int(cardNum[i]) * 2
                if x > 9:
                    evenSum += 1 + (x % 10)
                else:
                    evenSum += x
            else:
                oddSum += int(cardNum[i])
        total = oddSum + evenSum
        return True if total % 10 == 0 else False
         
    def creditCardProvider(self):
        # output append in each action to return output
        for p in operations:
            get_action = p[0]
            name = p[1]

            if len(p) == 4 and get_action == "Add":
                # run add function
                cardNum = p[2]
                cardLimit = p[3].split('$')[1]
                #when I create a card, I should create a credit_balance for each user
                self.credit_balance[name] = 0
                self.add(cardNum, name, cardLimit)

            if len(p) == 3:
                amount = int(p[2].split('$')[1])
                if get_action == 'Charge':
                    # run charge function
                    self.charge(amount, name)


                if get_action == 'Credit':
                    # run credit function
                    self.credit(amount, name)

        
        for user, bal in self.credit_balance.items():
            if self.card_number[user].split("_")[1] == "true":
                self.output.append([user, "$" + str(bal)])
            else:
                self.output.append([user, "Error"])
        return sorted(self.output)
    


operations = [["Add", "Tom", "4111111111111111", "$1000"],
["Add", "Lisa", "5454545454545454", "$3000"],
["Add", "Quincy", "12345678901234", "$2000"],
["Charge", "Tom", "$500"],
["Charge", "Tom", "$800"],
["Charge", "Lisa", "$7"],
["Credit", "Lisa", "$100"],
["Credit", "Quincy", "$200"]]

account = Account(operations)
result = account.creditCardProvider()

print(result)
        
