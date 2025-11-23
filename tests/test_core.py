from stringheist.core import (
    slugify,
    similarity,
    best_match,
    render_template,
)


# ---------- SLUGGING ----------

def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_unicode():
    assert slugify("Café au lait") == "cafe-au-lait"


def test_slugify_empty():
    assert slugify("") == ""


# ---------- FUZZY MATCHING ----------

def test_similarity_identical():
    assert similarity("test", "test") == 1.0


def test_similarity_different():
    s = similarity("test", "tent")
    assert 0.0 < s < 1.0


def test_best_match_basic():
    choices = ["apple", "banana", "orange"]
    match, score = best_match("appl", choices)
    assert match == "apple"
    assert score > 0.7


def test_best_match_cutoff():
    match, score = best_match("zzz", ["apple", "banana"], cutoff=0.9)
    assert match is None
    assert score == 0.0


# ---------- TEMPLATING ----------

def test_render_template_simple():
    tpl = "Hello, {{ name }}!"
    ctx = {"name": "Karthik"}
    assert render_template(tpl, ctx) == "Hello, Karthik!"


def test_render_template_nested():
    tpl = "User: {{ user.name }}, Email: {{ user.email }}"
    ctx = {"user": {"name": "Karthik", "email": "karthik@example.com"}}
    assert render_template(tpl, ctx) == "User: Karthik, Email: karthik@example.com"


def test_render_template_missing_key_left_intact():
    tpl = "Hello, {{ name }}!"
    ctx = {}
    assert render_template(tpl, ctx) == "Hello, {{ name }}!"
