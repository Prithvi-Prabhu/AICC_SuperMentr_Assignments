def fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)

    return fizz_count, buzz_count, fizzbuzz_count


def main():
    fizz, buzz, fizzbuzz_val = fizzbuzz()

    print("\n--- Counts ---")
    print(f"Fizz count: {fizz}")
    print(f"Buzz count: {buzz}")
    print(f"FizzBuzz count: {fizzbuzz_val}")


if __name__ == "__main__":
    main()