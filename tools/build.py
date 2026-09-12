#!/usr/bin/env python3
"""Builds the 枕书 / PillowBook site: one page set per language, from the text
below plus the Markdown in content/<lang>/{privacy,support}.md. Run
`python3 tools/build.py` from the repo root; it writes
<lang>/index.html, <lang>/privacy.html, <lang>/support.html and the root
index.html (which sends the browser to its own language).

Everything here describes what the app actually does. When the app changes
(a new permission, a new purchase, a new place data is kept), change the text
here and rebuild — the privacy page in particular must never promise less
than the app does.
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["zh-Hans", "zh-Hant", "en", "ja"]
CONTACT = "pillowbook2026@gmail.com"

T = {}

T["zh-Hans"] = dict(
    app="枕书", lang_name="简体中文", html_lang="zh-Hans",
    nav_home="介绍", nav_privacy="隐私政策", nav_support="使用帮助",
    tagline="一个安静的 txt / EPUB 阅读器，书只在你的手机里。",
    home_intro="枕书是一个人在业余时间写的 iOS 阅读器。没有账号、没有广告，也没有任何统计或追踪；支持简体、繁體、English、日本語界面，横排与竖排阅读。",
    sections=[
        ("书库", [
            ("导入与传书", "从「文件」导入，或用 Wi-Fi 传书从电脑发到手机。目前支持 txt 和 EPUB。"),
            ("章节识别", "自动识别章节标题样式；没有章节信息的 txt 也能分出章节，还能重新识别。"),
            ("收藏、归档、藏书阁", "长按书本可以收藏、归档，或放进带锁的藏书阁——用面容 ID 或设备密码打开，只有你能看。"),
            ("你的书在你手里", "书只保存在你的手机里，没有账号，App 不会上传。"),
        ]),
        ("读书", [
            ("翻页与滚动", "左右翻页或上下滚动随你，还能自动翻页；书签、进度都按原文位置记录，换排版也不会丢。"),
            ("竖排阅读", "每本书可单独设为竖排，翻页、滚动、书签、朗读一样不少；右开本的书会提示你切换。"),
            ("字体与排版", "内置思源宋体（简 / 繁 / 日）、霞鹜文楷、资源圆体，也可用系统字体；字号、边距、字距、行距、段距都能调。"),
            ("注音与漫画", "EPUB 里的假名注音、拼音注音可显示；图片式漫画一页一图，居中显示。"),
        ]),
        ("外观", [
            ("阅读主题", "多种纸色，可自定义阅读背景；温暖、清冷两种底色一键切换。"),
            ("App 图标与配色", "多套图标和强调色随心切换。"),
            ("书封", "没有封面的书按书名自动生成封面，样式可选。"),
        ]),
        ("更多", [
            ("听书", "用系统离线语音朗读，不联网也能听；锁屏继续播放，听到哪书就翻到哪。"),
            ("阅读记录", "每天读了多久、连续读了几天，每本书的进度、时长一目了然。"),
            ("全文搜索", "不只搜书名和作者，书里的内容也能搜。"),
            ("没有广告", "远离烦人的广告。"),
        ]),
    ],
    home_purchases_h="内购",
    home_purchases="免费版书库最多放 5 本。「书库无上限」是一次性购买，永久有效，同一 Apple 账户的设备都可使用。「请开发者喝杯咖啡」是打赏，可重复，不解锁任何功能。购买都由 App Store 处理。",
    footer="枕书 · 由 Vincent 独立开发",
)

T["zh-Hant"] = dict(
    app="枕書", lang_name="繁體中文", html_lang="zh-Hant",
    nav_home="介紹", nav_privacy="隱私權政策", nav_support="使用說明",
    tagline="一個安靜的 txt / EPUB 閱讀器，書只在你的手機裡。",
    home_intro="枕書是一個人利用閒暇時間寫的 iOS 閱讀器。沒有帳號、沒有廣告，也沒有任何統計或追蹤；支援簡體、繁體、English、日本語介面，橫排與直排閱讀。",
    sections=[
        ("書庫", [
            ("匯入與傳書", "從「檔案」匯入，或用 Wi-Fi 傳書從電腦傳到手機。目前支援 txt 和 EPUB。"),
            ("章節辨識", "自動辨識章節標題樣式；沒有章節資訊的 txt 也能分出章節，還能重新辨識。"),
            ("收藏、歸檔、藏書閣", "長按書本可以收藏、歸檔，或放進有鎖的藏書閣——用 Face ID 或裝置密碼打開，只有你能看。"),
            ("你的書在你手裡", "書只保存在你的手機裡，沒有帳號，App 不會上傳。"),
        ]),
        ("讀書", [
            ("翻頁與捲動", "左右翻頁或上下捲動隨你，還能自動翻頁；書籤、進度都按原文位置記錄，換排版也不會丟。"),
            ("直排閱讀", "每本書可單獨設為直排，翻頁、捲動、書籤、朗讀一樣不少；右翻本的書會提示你切換。"),
            ("字體與排版", "內建思源宋體（簡 / 繁 / 日）、霞鶩文楷、資源圓體，也可用系統字體；字級、邊距、字距、行距、段距都能調。"),
            ("注音與漫畫", "EPUB 裡的假名注音、拼音注音可顯示；圖片式漫畫一頁一圖，置中顯示。"),
        ]),
        ("外觀", [
            ("閱讀主題", "多種紙色，可自訂閱讀背景；溫暖、清冷兩種底色一鍵切換。"),
            ("App 圖示與配色", "多套圖示和強調色隨心切換。"),
            ("書封", "沒有封面的書按書名自動產生封面，樣式可選。"),
        ]),
        ("更多", [
            ("聽書", "用系統離線語音朗讀，不連網也能聽；鎖定畫面繼續播放，聽到哪書就翻到哪。"),
            ("閱讀紀錄", "每天讀了多久、連續讀了幾天，每本書的進度、時長一目了然。"),
            ("全文搜尋", "不只搜書名和作者，書裡的內容也能搜。"),
            ("沒有廣告", "遠離煩人的廣告。"),
        ]),
    ],
    home_purchases_h="內購",
    home_purchases="免費版書庫最多放 5 本。「書庫無上限」是一次性購買，永久有效，同一 Apple 帳戶的裝置都可使用。「請開發者喝杯咖啡」是打賞，可重複，不解鎖任何功能。購買都由 App Store 處理。",
    footer="枕書 · 由 Vincent 獨立開發",
)

T["en"] = dict(
    app="PillowBook", lang_name="English", html_lang="en",
    nav_home="About", nav_privacy="Privacy Policy", nav_support="Support",
    tagline="A quiet txt / EPUB reader. Your books stay on your phone.",
    home_intro="PillowBook is an iOS reader built by one person in their spare time. No accounts, no ads, no analytics or tracking. The interface comes in Simplified Chinese, Traditional Chinese, English and Japanese, and text can be read horizontally or vertically.",
    sections=[
        ("Library", [
            ("Import and Wi-Fi Transfer", "Import from Files, or send books from a computer over Wi-Fi. txt and EPUB are supported."),
            ("Chapter detection", "Chapter headings are recognised automatically; a txt with no chapter marks still gets chapters, and you can re-detect with a different pattern."),
            ("Favourites, archive, Vault", "Long-press a book to favourite or archive it, or move it to the locked Vault, opened with Face ID or your passcode."),
            ("Your books, in your hands", "Books are stored on your phone only. No account, and the app never uploads them."),
        ]),
        ("Reading", [
            ("Pages or scrolling", "Turn pages or scroll, with optional auto-turn. Bookmarks and progress are kept as positions in the original text, so changing the layout never loses them."),
            ("Vertical reading", "Any book can be set to vertical columns, with paging, scrolling, bookmarks and read-aloud all working. Right-to-left books suggest the switch."),
            ("Fonts and layout", "Source Han Serif (SC / TC / JP), LXGW WenKai and Resource Han Rounded are built in; system fonts work too. Size, margins, letter, line and paragraph spacing are all adjustable."),
            ("Ruby and manga", "Furigana and pinyin in EPUBs can be shown; image-based manga is shown one page per picture, centred."),
        ]),
        ("Appearance", [
            ("Reading themes", "Several paper colours and a custom background; warm or cool base tone with one tap."),
            ("App icon and accent", "Multiple icons and accent colours to switch between."),
            ("Covers", "Books without a cover get one generated from the title, in a style you choose."),
        ]),
        ("More", [
            ("Read aloud", "Uses the system's offline voices, so it works without a connection; keeps playing on the lock screen, and the book follows along."),
            ("Reading log", "How long you read each day, your streak, and each book's progress and time."),
            ("Full-text search", "Search inside books, not just titles and authors."),
            ("No ads", "None, ever."),
        ]),
    ],
    home_purchases_h="In-app purchases",
    home_purchases="The free library holds 5 books. “Unlimited Library” is a one-time purchase that lasts forever and works on every device signed in to the same Apple Account. “Buy the Developer a Coffee” is a tip: repeatable, and it unlocks nothing. All purchases are handled by the App Store.",
    footer="PillowBook · made independently by Vincent",
)

T["ja"] = dict(
    app="まくらと本", lang_name="日本語", html_lang="ja",
    nav_home="紹介", nav_privacy="プライバシーポリシー", nav_support="ヘルプ",
    tagline="静かな txt / EPUB リーダー。本はあなたのスマートフォンの中だけに。",
    home_intro="まくらと本は、ひとりで余暇に作っている iOS の読書アプリです。アカウントも広告もなく、解析やトラッキングもありません。簡体字・繁体字・英語・日本語の画面、横書きと縦書きに対応しています。",
    sections=[
        ("本棚", [
            ("読み込みと Wi-Fi 転送", "「ファイル」から読み込むか、Wi-Fi でパソコンから送れます。対応形式は txt と EPUB。"),
            ("章の認識", "章見出しの形式を自動で認識。章情報のない txt でも章に分けられ、認識のやり直しもできます。"),
            ("お気に入り・アーカイブ・書庫", "本を長押しでお気に入りやアーカイブに。鍵付きの書庫に入れれば、Face ID または端末のパスコードであなただけが開けます。"),
            ("本はあなたの手元に", "本はスマートフォンの中にだけ保存。アカウントはなく、アプリがアップロードすることはありません。"),
        ]),
        ("読む", [
            ("めくりとスクロール", "横めくりでも縦スクロールでも。自動めくりもあります。ブックマークや進み具合は原文の位置で記録するので、組版を変えても失われません。"),
            ("縦書き", "本ごとに縦書きに設定できます。めくり・スクロール・ブックマーク・読み上げはそのまま。右開きの本は切り替えをおすすめします。"),
            ("フォントと組版", "源ノ明朝（簡 / 繁 / 日）、霞鶩文楷、資源圓體を内蔵、システムフォントも使えます。文字サイズ・余白・字間・行間・段落間を調整できます。"),
            ("ルビとマンガ", "EPUB のふりがな・ピンインを表示できます。画像形式のマンガは 1 ページ 1 枚、中央に表示します。"),
        ]),
        ("外観", [
            ("読書テーマ", "数種類の紙色と、自分で選べる背景。温かい・涼しい二つの基調をワンタップで切り替え。"),
            ("アプリアイコンと配色", "複数のアイコンとアクセントカラーを気分で。"),
            ("表紙", "表紙のない本には書名から表紙を生成。スタイルも選べます。"),
        ]),
        ("その他", [
            ("読み上げ", "iOS のオフライン音声で読み上げ。通信なしでも聞け、ロック画面でも再生が続き、聞いた所まで本も進みます。"),
            ("読書記録", "一日に読んだ時間、続いた日数、本ごとの進み具合と時間が一目でわかります。"),
            ("全文検索", "書名や著者だけでなく、本文の中も検索できます。"),
            ("広告なし", "わずらわしい広告はありません。"),
        ]),
    ],
    home_purchases_h="アプリ内課金",
    home_purchases="無料版の本棚には 5 冊まで入ります。「本棚無制限」は一度きりの購入で永久に有効、同じ Apple アカウントの端末すべてで使えます。「コーヒー一杯分の応援」は応援で、何度でも可能、機能の解除はありません。購入はすべて App Store が処理します。",
    footer="まくらと本 · Vincent が個人で開発",
)


def page(lang, name, title, body):
    t = T[lang]
    langs = " ".join(
        f'<a href="../{l}/{name}.html"{" class=\"current\"" if l == lang else ""}>{T[l]["lang_name"]}</a>' for l in LANGS)
    pages = " ".join(
        f'<a href="{p}.html"{" class=\"current\"" if p == name else ""}>{label}</a>'
        for p, label in (("index", t["nav_home"]), ("privacy", t["nav_privacy"]), ("support", t["nav_support"])))
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {t['app']}</title>
<link rel="stylesheet" href="../assets/style.css">
<link rel="icon" href="../assets/icon.png">
</head>
<body>
<header class="top">
  <a class="brand" href="index.html"><img src="../assets/icon.png" alt=""> {t['app']}</a>
  <nav class="langs">{langs}</nav>
  <nav class="pages">{pages}</nav>
</header>
<main>
{body}
</main>
<footer>{t['footer']} · <a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</body>
</html>
"""


def home(lang):
    t = T[lang]
    out = [f"<h1>{t['app']}</h1>", f"<p class=\"lead\">{t['tagline']}</p>", f"<p>{t['home_intro']}</p>"]
    for heading, items in t["sections"]:
        out.append(f"<h2>{heading}</h2><div class=\"grid\">")
        for h3, p in items:
            out.append(f"<div class=\"card raised\"><h3>{h3}</h3><p>{p}</p></div>")
        out.append("</div>")
    out.append(f"<h2>{t['home_purchases_h']}</h2><p>{t['home_purchases']}</p>")
    out.append(f"<hr><p class=\"note\"><a href=\"privacy.html\">{t['nav_privacy']}</a> · <a href=\"support.html\">{t['nav_support']}</a></p>")
    return page(lang, "index", t["nav_home"], "\n".join(out))


INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+|[\w.-]+\.html)\)"), r'<a href="\2">\1</a>'),
]


def inline(text):
    text = html.escape(text, quote=False)
    for rx, rep in INLINE:
        text = rx.sub(rep, text)
    return text


def markdown(md):
    """The small Markdown subset the legal drafts use: #/##/### headings,
    paragraphs, - and 1. lists (one level), **bold**, `code`, [text](url),
    two trailing spaces for a line break, > for the boxed summary."""
    out, para, lst, quote = [], [], None, []

    def flush_para():
        if para:
            out.append("<p>" + "<br>".join(inline(l.rstrip("\x00")) for l in para) + "</p>")
            para.clear()

    def flush_list():
        nonlocal lst
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{tag}>")
            lst = None

    def flush_quote():
        if quote:
            out.append('<div class="summary raised"><p>' + " ".join(inline(l) for l in quote) + "</p></div>")
            quote.clear()

    for raw in md.split("\n"):
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped:
            flush_para(); flush_list(); flush_quote(); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if m:
            flush_para(); flush_list(); flush_quote()
            out.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>"); continue
        if stripped.startswith("> "):
            flush_para(); flush_list(); quote.append(stripped[2:]); continue
        m = re.match(r"^(-|\d+\.)\s+(.*)$", stripped)
        if m:
            flush_para(); flush_quote()
            tag = "ul" if m.group(1) == "-" else "ol"
            if lst and lst[0] != tag:
                flush_list()
            if not lst:
                lst = (tag, [])
            lst[1].append(m.group(2)); continue
        flush_list(); flush_quote()
        # soft-wrapped lines join the previous one; two trailing spaces force <br>
        if para and not para[-1].endswith("\x00"):
            para[-1] = para[-1] + " " + stripped
        else:
            para.append(stripped)
        if line.endswith("  "):
            para[-1] += "\x00"
    flush_para(); flush_list(); flush_quote()
    return "\n".join(out)


def from_markdown(lang, name):
    path = os.path.join(ROOT, "content", lang, f"{name}.md")
    md = open(path, encoding="utf-8").read()
    title = re.search(r"^#\s+(.*)$", md, re.M).group(1)
    return page(lang, name, title, markdown(md))


def privacy(lang):
    return from_markdown(lang, "privacy")


def support(lang):
    return from_markdown(lang, "support")


ROOT_INDEX = """<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>枕书 · PillowBook · まくらと本</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/icon.png">
<script>
(function () {
  var l = (navigator.language || "zh-Hans").toLowerCase();
  var target = "zh-Hans";
  if (l.indexOf("ja") === 0) target = "ja";
  else if (l.indexOf("en") === 0) target = "en";
  else if (l.indexOf("zh") === 0 && /hant|tw|hk|mo/.test(l)) target = "zh-Hant";
  else if (l.indexOf("zh") !== 0) target = "en";
  location.replace(target + "/index.html");
})();
</script>
</head>
<body>
<main>
<h1>枕书 · PillowBook · まくらと本</h1>
<p class="lead"><a href="zh-Hans/index.html">简体中文</a> · <a href="zh-Hant/index.html">繁體中文</a> · <a href="en/index.html">English</a> · <a href="ja/index.html">日本語</a></p>
</main>
</body>
</html>
"""


def redirector(name):
    """Root-level privacy.html / support.html: one language-neutral address
    (for App Store Connect and links elsewhere) that sends the browser to its
    own language, with plain links as the no-script fallback."""
    links = " · ".join(f'<a href="{l}/{name}.html">{T[l]["lang_name"]}</a>' for l in LANGS)
    return ROOT_INDEX.replace('location.replace(target + "/index.html");', f'location.replace(target + "/{name}.html");') \
        .replace('<a href="zh-Hans/index.html">简体中文</a> · <a href="zh-Hant/index.html">繁體中文</a> · <a href="en/index.html">English</a> · <a href="ja/index.html">日本語</a>', links)


def main():
    for name in ("privacy", "support"):
        with open(os.path.join(ROOT, f"{name}.html"), "w", encoding="utf-8") as f:
            f.write(redirector(name))
    for lang in LANGS:
        d = os.path.join(ROOT, lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("index", home), ("privacy", privacy), ("support", support)):
            with open(os.path.join(d, f"{name}.html"), "w", encoding="utf-8") as f:
                f.write(fn(lang))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    print("built", len(LANGS) * 3 + 3, "pages")


if __name__ == "__main__":
    main()
