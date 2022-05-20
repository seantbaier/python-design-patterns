from reactivex import Observer, of


def get_quotes():
    import contextlib
    import io

    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this  # noqa

    quotes = zen.getvalue().split("\n")[1:]
    return enumerate(quotes)


def push_quotes(obs, scheduler):
    quotes = get_quotes()
    for q in quotes:
        if q:  # skip many
            obs.on_next(q)
    obs.on_completed()


class ZenQuotesObserver(Observer):
    def on_next(self, value):
        print(f"Recieved: {value}")

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print(f"Error Ocurred: {error}")


if __name__ == "__main__":
    zen_quotes = get_quotes()
    source = of(*zen_quotes)
    # composed = source.pipe.filter(lambda q: len(q[1]) > 0).subscribe(
    #     lambda value: print(f"Recieved: {value[0]} - {value[1]}")
    # )
