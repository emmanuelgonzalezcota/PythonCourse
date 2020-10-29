from platform import platform, machine, processor

print(platform())
print(platform(1))
print(platform(0, 1))

print("machine:")
print(machine())

print("processor:")
print(processor())