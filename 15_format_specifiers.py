# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed points)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

print(f"{3.34721456:.3f}")
print(f"{3.34721456:20}")
print(f"{3.34721456:<20}")
print(f"{3.34721456:>20}")
print(f"{3.34721456:^20}")
print(f"{-3.34721456:+20}")
print(f"{3.34721456:+20}")
print(f"{3.34721456:=20}")
print(f"{334721456.43232:,.4f}")
