"""Extract the agreed training prose from the published essay HTML."""

from pathlib import Path
import sys

from bs4 import BeautifulSoup


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: extract_essay.py INPUT_HTML OUTPUT_MD")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    soup = BeautifulSoup(input_path.read_text(encoding="utf-8"), "html.parser")
    title = soup.select_one("main h1")
    article = soup.find("article")
    if title is None or article is None:
        raise RuntimeError("Expected the published essay title and article body.")

    blocks = [f"# {title.get_text(' ', strip=True)}"]
    for child in article.find_all(recursive=False):
        if child.name == "hr":
            break
        if child.name not in {"h2", "p"} or child.find("img") is not None:
            continue
        for footnote in child.find_all("sup"):
            footnote.extract()
        text = " ".join(child.get_text(" ", strip=True).split())
        if not text:
            continue
        blocks.append(f"## {text}" if child.name == "h2" else text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"Wrote {len(blocks) - 1} body blocks to {output_path}")


if __name__ == "__main__":
    main()
