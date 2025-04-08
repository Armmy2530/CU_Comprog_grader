t_start = float(input())
t_room = float(input())
d_t = float(input())
material = int(input())
wind_speed = int(input())

k1 = 0.0
k2 = 0.0

if  (material == 1): k1 = 0.05
elif(material == 2): k1 = 0.02
elif(material == 3): k1 = 0.01
elif(material == 4): k1 = 0.015

if  (wind_speed == 1): k2 = 1.5
elif(wind_speed == 2): k2 = 1.0
elif(wind_speed == 3): k2 = 0.8

k = k1*k2
time_use = 0.0

t_new = t_start - (k * (t_start - t_room) * d_t)
time_use += d_t
while(abs(t_start - t_new)) > 0.001:
    t_start = t_new
    t_new = t_new - (k * (t_new - t_room) * d_t)
    time_use += d_t
print(round(time_use,2),round(t_new,3))