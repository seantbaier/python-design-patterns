from reactivex import Observer, create


def get_qoutes():
    import contextlib
    import io

    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this  # noqa

    quotes = zen.getvalue().split("\n")[1:]
    return enumerate(quotes)


def push_quotes(obs, scheduler):
    quotes = get_qoutes()
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
    source = create(push_quotes)
    source.subscribe(ZenQuotesObserver())
