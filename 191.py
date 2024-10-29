#






age = 20
membership = True
expired_membership = False
referral_code = False
if(age >= 18 and membership and not expired_membership)or referral_code:
    print("discount applied!")
else:
    print("no discount")