import pkg_resources
import random

messages = ["work hard and play hard"]

def main():
    for entry_point in pkg_resources.iter_entry_points("motd_messages"):
        messages.extend(entry_point.load())

    print(random.choice(messages))

if __name__ == "__main__":
    main()
