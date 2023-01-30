fire_data = input()
water = int(input())

cells = {}
effort = 0
total_fire = 0

for fire in fire_data.split("#"):
    fire_type, value = fire.split(" = ")
    if fire_type == "High" and 81 <= int(value) <= 125:
        cells[fire_type] = int(value)
    elif fire_type == "Medium" and 51 <= int(value) <= 80:
        cells[fire_type] = int(value)
    elif fire_type == "Low" and 1 <= int(value) <= 50:
        cells[fire_type] = int(value)

put_out_cells = []

for fire_type, value in cells.items():
    if water >= value:
        water -= value
        effort += value * 0.25
        total_fire += value
        put_out_cells.append(f" - {value}")

print("Cells:")
for cell in put_out_cells:
    print(cell)

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")