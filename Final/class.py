from Class_design import Theater

def main():
    a = Theater(5)
    a.reserve()
    a.reserve()
    a.reserve()
    a.unreserve(2)
    a.reserve()


if __name__ == "__main__":
    main()