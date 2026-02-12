from app.engine import ResearchEngine

if __name__ == "__main__":
    engine = ResearchEngine()

    while True:
        q = input("Ask question (or exit): ")

        if q.lower() == "exit":
            break

        answer = engine.run(q)

        print("\n--- Answer ---\n")
        print(answer)
