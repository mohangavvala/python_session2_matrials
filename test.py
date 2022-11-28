try:
    print("Hello")
    print(10/0)
except:
    print("Except handle")
else:
    print("else block")
finally:
    print("Cleanup code")
