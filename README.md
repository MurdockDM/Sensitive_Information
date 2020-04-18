## Practice: Sensitive Information

Create a class to represent a patient of a doctor's office. The **`Patient`** class will accept the following information during initialization

1. Social security number
1. Date of birth
1. Health insurance account number
1. First name
1. Last name
1. Address

The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of `full_name`. Address should have a getter and setter.

```py
cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
