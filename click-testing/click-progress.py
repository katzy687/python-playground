import time

import click
from click.termui import progressbar


def run_five(pbar):
    counter = 0
    while counter < 3:
        counter += 1
        print("hi")
        pbar.make_step(1)
        pbar.render_progress()
        time.sleep(1)


with click.progressbar(length=3, show_eta=False, label="uploading script") as pbar:
    run_five(pbar)
