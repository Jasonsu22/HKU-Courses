from __future__ import annotations

import base64
import io
import random
import re
from collections import Counter

import pandas as pd
from wordcloud import WordCloud

from src.data_loader import FLAVORS


CLOUD_SAMPLE = 3000
CLOUD_COLORS = ["#c4622d", "#16345c", "#2c5f97", "#6d93c4", "#8a4a26"]

# Common English words plus wine-review filler that says nothing about taste.
STOP = set(
    """
    a about above across after again against all almost along also although always am among an and another any are
    around as at away back be because been before being below best between both but by can could did do does done
    down drink drinking during each either enough even ever every few find finish first flavor flavors for from full
    further get gives good great had has have here hint hints how however if in into is it its just keep last lead
    least less like little long made make many may more most much must near nearly needs new next nicely nose not note
    notes now of off offer offers on once one only or other our out over palate quite rather ready really s seems
    shows so some still such than that the their them then there these they this those through to too touch two under
    until up very was way well were what when where which while who whose will wine wines with within without would
    years yet you aromas aroma bottle bottling character feel mouth mouthfeel opens shows showing slightly hint
    alongside give given glass texture structure style vintage blend fruit fruits flavored
    """.split()
)


# Grape names that are also tasting words stay in the cloud.
FLAVOR_GRAPE_WORDS = {"apple", "orange", "melon"}


def variety_words(frame: pd.DataFrame) -> set[str]:
    """Every word used in a variety name, e.g. "cabernet" or "noir"; blends mention many of them."""
    words = {word for name in frame["variety"].unique() for word in re.findall(r"[a-z]+", name.lower())}
    return words - FLAVOR_GRAPE_WORDS


def word_counts(descriptions: pd.Series, limit: int = CLOUD_SAMPLE, skip: set[str] | None = None) -> tuple[Counter, int]:
    """Count meaningful words; `skip` drops extra words such as the variety names themselves."""
    skip = STOP | (skip or set())
    texts = descriptions.loc[descriptions.str.len().gt(0)]
    if len(texts) > limit:
        texts = texts.sample(limit, random_state=7)
    counts: Counter = Counter()
    for text in texts:
        counts.update(word for word in re.findall(r"[a-z]+", text.lower()) if len(word) > 2 and word not in skip)
    return counts, len(texts)


def word_cloud_image(counts: Counter) -> str:
    """Return the cloud as a data URI that an html.Img can show."""
    picker = random.Random(7)
    cloud = WordCloud(
        width=900,
        height=470,
        background_color=None,
        mode="RGBA",
        max_words=70,
        prefer_horizontal=0.95,
        relative_scaling=0.35,
        random_state=7,
        color_func=lambda *args, **kwargs: picker.choice(CLOUD_COLORS),
    ).generate_from_frequencies(dict(counts.most_common(150)))
    buffer = io.BytesIO()
    cloud.to_image().save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()


def highlight(description: str, flavors: list[str] | None = None) -> str:
    """Bold the flavor words in a review, as Markdown."""
    names = flavors or list(FLAVORS)
    pattern = "|".join(f"(?:{FLAVORS[name]}[a-z]*)" for name in names)
    return re.sub(pattern, lambda found: f"**{found.group(0)}**", description, flags=re.IGNORECASE)
