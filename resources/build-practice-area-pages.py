#!/usr/bin/env python3
"""Convert Vincent-authored .docx practice-area articles into Astro markdown.

Vincent drops .docx files into site/src/content/practice-areas/. This script:

  1. Parses each .docx and extracts the article body + SEO metadata
     (the "SEO title / Meta description / Suggested URL slug" block at the top).
  2. Updates the matching <slug>.md stub: preserves frontmatter, replaces the
     body, fills in seoTitle / seoDescription, flips `draft: true` -> `draft: false`.
  3. For docx files with no existing stub (e.g. "The New Jersey Law Against
     Discrimination.docx"), creates a fresh stub with default frontmatter.

Stdlib-only (zipfile + xml.etree + re). Idempotent — re-run any time Vincent
updates a .docx and the markdown refreshes.

Run:  python build-practice-area-pages.py
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

PRACTICE_DIR = Path(
    r'C:\Users\steve\OneDrive\Desktop\firm-website\site\src\content\practice-areas'
)

# Vincent's docx filename -> my stub slug
DOCX_TO_SLUG = {
    'Age Discrimination.docx': 'age-discrimination',
    'Breach of Employment Contract.docx': 'breach-of-employment-contract',
    'Disability Discrimination.docx': 'disability-discrimination',
    'FMLA Retaliation and Interference.docx': 'fmla-retaliation',
    'Failure to Provide a Religious Accommodation.docx': 'religious-accommodation-failure',
    'Hostile Work Environment.docx': 'hostile-work-environment',
    'LGBTQ Discrimination.docx': 'lgbtq-discrimination',
    'NY Paid Family Leave Violations.docx': 'paid-family-leave-violations',
    'Pregnancy Discrimination.docx': 'pregnancy-discrimination',
    'Prior Criminal Conviction Discrimination.docx': 'criminal-conviction-discrimination',
    'Race Discrimination at Work.docx': 'race-discrimination',
    'Religious Discrimination.docx': 'religious-discrimination',
    'Retaliation for Protected Activity.docx': 'retaliation',
    'Severance Negotiation.docx': 'severance-negotiation',
    'Sexual Assault.docx': 'sexual-assault',
    'Sexual Harassment in the Workplace.docx': 'sexual-harassment',
    'The New Jersey Law Against Discrimination.docx': 'new-jersey-law-against-discrimination',
    'Unpaid Minimum Wage and Overtime.docx': 'unpaid-minimum-wage-overtime',
    'Wage Theft.docx': 'wage-theft',
    'Whistleblower Retaliation.docx': 'whistleblower-retaliation',
    'Wrongful Termination.docx': 'wrongful-termination',
}

# Frontmatter defaults for any slug that doesn't already have a stub.
NEW_STUB_DEFAULTS = {
    'new-jersey-law-against-discrimination': {
        'name': 'New Jersey Law Against Discrimination',
        'tagline': "New Jersey's broadest employment-discrimination statute.",
        'priority': 21,
        'featured': False,
        'statutes': ['New Jersey Law Against Discrimination (N.J.S.A. 10:5-1 et seq.)'],
    },
}

# Bold-phrase -> practice-area slug, used to rewrite the "Related Fingerhut
# Law Pages" section into real internal links. Keys are lowercase.
RELATED_LINKS_MAP = {
    'age discrimination': 'age-discrimination',
    'breach of employment contract': 'breach-of-employment-contract',
    'disability discrimination': 'disability-discrimination',
    'disability discrimination & failure to accommodate': 'disability-discrimination',
    'fmla': 'fmla-retaliation',
    'fmla retaliation': 'fmla-retaliation',
    'fmla retaliation & interference': 'fmla-retaliation',
    'fmla retaliation and interference': 'fmla-retaliation',
    'failure to provide a religious accommodation': 'religious-accommodation-failure',
    'failure to accommodate religious practice': 'religious-accommodation-failure',
    'religious accommodation': 'religious-accommodation-failure',
    'hostile work environment': 'hostile-work-environment',
    'lgbtq discrimination': 'lgbtq-discrimination',
    'lgbtq+ discrimination': 'lgbtq-discrimination',
    'lgbtq+ workplace discrimination': 'lgbtq-discrimination',
    'paid family leave': 'paid-family-leave-violations',
    'paid family leave violations': 'paid-family-leave-violations',
    'ny paid family leave': 'paid-family-leave-violations',
    'ny paid family leave violations': 'paid-family-leave-violations',
    'new york paid family leave': 'paid-family-leave-violations',
    'pfl': 'paid-family-leave-violations',
    'criminal conviction discrimination': 'criminal-conviction-discrimination',
    'prior criminal conviction discrimination': 'criminal-conviction-discrimination',
    'race discrimination': 'race-discrimination',
    'race discrimination at work': 'race-discrimination',
    'religious discrimination': 'religious-discrimination',
    'retaliation': 'retaliation',
    'retaliation for protected activity': 'retaliation',
    'sexual harassment': 'sexual-harassment',
    'sexual harassment in the workplace': 'sexual-harassment',
    'sexual harassment & sexual assault': 'sexual-harassment',
    'nj lad': 'new-jersey-law-against-discrimination',
    'new jersey law against discrimination': 'new-jersey-law-against-discrimination',
    'unpaid minimum wage and overtime': 'unpaid-minimum-wage-overtime',
    'unpaid minimum wage & overtime': 'unpaid-minimum-wage-overtime',
    'minimum wage and overtime': 'unpaid-minimum-wage-overtime',
    'wage and hour': 'unpaid-minimum-wage-overtime',
    'wage theft': 'wage-theft',
    'whistleblower': 'whistleblower-retaliation',
    'whistleblower retaliation': 'whistleblower-retaliation',
    'wrongful termination': 'wrongful-termination',
    'pregnancy discrimination': 'pregnancy-discrimination',
    'pregnancy discrimination & caregiver retaliation': 'pregnancy-discrimination',
    'sexual assault': 'sexual-assault',
    'workplace sexual assault': 'sexual-assault',
    'severance': 'severance-negotiation',
    'severance negotiation': 'severance-negotiation',
}

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PKG = '{http://schemas.openxmlformats.org/package/2006/relationships}'


def parse_run(r_elem):
    """Convert a <w:r> run to a markdown text fragment."""
    text = ''
    for child in r_elem:
        tag = child.tag.replace(W, '')
        if tag == 't':
            text += child.text or ''
        elif tag == 'br':
            text += '\n'
        elif tag == 'tab':
            text += '\t'
    if not text:
        return ''
    rpr = r_elem.find(f'{W}rPr')
    bold = italic = False
    if rpr is not None:
        bold = rpr.find(f'{W}b') is not None
        italic = rpr.find(f'{W}i') is not None
    # Don't bold/italic pure whitespace.
    if not text.strip():
        return text
    if bold and italic:
        return f'***{text}***'
    if bold:
        return f'**{text}**'
    if italic:
        return f'*{text}*'
    return text


def parse_paragraph(p, hyperlinks):
    """Return (kind, text). kind in {empty, heading, list, paragraph}."""
    ppr = p.find(f'{W}pPr')
    style = None
    list_item = False
    if ppr is not None:
        pstyle = ppr.find(f'{W}pStyle')
        if pstyle is not None:
            style = pstyle.get(f'{W}val')
        if ppr.find(f'{W}numPr') is not None:
            list_item = True

    parts = []
    for child in p:
        tag = child.tag.replace(W, '')
        if tag == 'r':
            parts.append(parse_run(child))
        elif tag == 'hyperlink':
            rid = child.get(f'{R}id')
            inner = ''
            for r in child.findall(f'{W}r'):
                inner += parse_run(r)
            href = hyperlinks.get(rid, '')
            if href and inner:
                parts.append(f'[{inner.strip()}]({href})')
            else:
                parts.append(inner)
    text = ''.join(parts).strip()

    if not text:
        return ('empty', '')
    if style and style.startswith('Heading'):
        n_str = re.sub(r'\D', '', style) or '2'
        n = int(n_str)
        # Page H1 comes from frontmatter `name`. Demote Heading1/2 from docx
        # to H2, Heading3 to H3, and deeper headings cap at H4.
        if n <= 2:
            level = 2
        elif n == 3:
            level = 3
        else:
            level = min(n, 4)
        return ('heading', '#' * level + ' ' + text)
    if list_item:
        return ('list', '- ' + text)
    return ('paragraph', text)


def read_hyperlinks(zf):
    try:
        x = zf.read('word/_rels/document.xml.rels').decode('utf-8')
    except KeyError:
        return {}
    root = ET.fromstring(x)
    out = {}
    for rel in root.findall(f'{PKG}Relationship'):
        if 'hyperlink' in (rel.get('Type') or '').lower():
            out[rel.get('Id')] = rel.get('Target')
    return out


def convert_docx(docx_path):
    with zipfile.ZipFile(docx_path) as zf:
        doc_xml = zf.read('word/document.xml')
        hyperlinks = read_hyperlinks(zf)

    root = ET.fromstring(doc_xml)
    body = root.find(f'{W}body')
    paras = [parse_paragraph(p, hyperlinks) for p in body.findall(f'{W}p')]

    # Strip leading empty paragraphs.
    while paras and paras[0][0] == 'empty':
        paras.pop(0)
    # Drop the article-title heading (first heading paragraph).
    if paras and paras[0][0] == 'heading':
        paras.pop(0)
    while paras and paras[0][0] == 'empty':
        paras.pop(0)

    # Extract Vincent's SEO metadata block.
    seo = {}
    seo_keys = ['SEO title:', 'Meta description:', 'Suggested URL slug:']
    while paras:
        kind, text = paras[0]
        if any(k in text for k in seo_keys):
            for line in text.split('\n'):
                line = line.strip()
                m = re.search(r'\*\*\s*SEO title:\s*\*\*\s*(.+?)\s*$', line)
                if m:
                    seo['seoTitle'] = m.group(1).strip()
                    continue
                m = re.search(r'\*\*\s*Meta description:\s*\*\*\s*(.+?)\s*$', line)
                if m:
                    seo['seoDescription'] = m.group(1).strip()
                    continue
                m = re.search(r'\*\*\s*Suggested URL slug:\s*\*\*\s*`?([^`\s]*)\s*$', line)
                if m:
                    seo['suggestedSlug'] = m.group(1).strip().rstrip('`').rstrip('/')
                    continue
            paras.pop(0)
        else:
            break

    # Build markdown body.
    lines = []
    prev = None
    for kind, text in paras:
        if kind == 'empty':
            prev = 'empty'
            continue
        if kind == 'list':
            if prev != 'list':
                lines.append('')
            lines.append(text)
        else:
            if lines:
                lines.append('')
            lines.append(text)
        prev = kind

    body_md = '\n'.join(lines).strip() + '\n'
    body_md = bullet_lists(body_md)
    body_md = link_related_section(body_md)
    return seo, body_md


def bullet_lists(markdown):
    """Detect Vincent's colon-intro lists and convert the trailing short
    paragraphs into a real bulleted list.

    Pattern:
        Some intro ending with a colon:

        Short item one.

        Short item two.

        Short item three.

    becomes:

        Some intro ending with a colon:

        - Short item one.
        - Short item two.
        - Short item three.

    Requires at least 2 candidate items; otherwise leaves paragraphs alone.
    A candidate item is a single-line block under 320 chars, not a heading
    and not already a bullet.
    """
    blocks = [b for b in re.split(r'\n\s*\n', markdown) if b.strip()]
    out = []
    i = 0
    while i < len(blocks):
        block = blocks[i].strip()
        is_intro = (
            block.endswith(':')
            and not block.startswith('#')
            and not block.startswith('-')
        )
        if is_intro:
            items = []
            j = i + 1
            while j < len(blocks):
                cand = blocks[j].strip()
                if (
                    not cand
                    or cand.startswith('#')
                    or cand.startswith('-')
                    or '\n' in cand
                    or len(cand) > 320
                ):
                    break
                items.append(cand)
                j += 1
            if len(items) >= 2:
                out.append(block)
                out.append('\n'.join('- ' + it for it in items))
                i = j
                continue
        out.append(block)
        i += 1
    return '\n\n'.join(out) + '\n'


def link_related_section(markdown):
    """Rewrite every "Related Fingerhut Law Pages" section so that bold
    practice-area names become real internal links. Also strips Vincent's
    "Suggested internal links:" editorial scaffolding.

    Some docx files (e.g. race-discrimination) contain the related-links
    section twice — both occurrences get transformed.
    """
    section_pattern = re.compile(
        r'(###\s+Related Fingerhut Law Pages\s*\n)(.*?)(?=\n###\s|\Z)',
        re.DOTALL,
    )

    def transform_section(m):
        heading = m.group(1)
        section = m.group(2)
        section = re.sub(
            r'(?im)^\s*Suggested internal links:\s*',
            '',
            section,
        )

        def replace_phrase(mm):
            phrase = mm.group(1).strip()
            slug = RELATED_LINKS_MAP.get(phrase.lower())
            if slug:
                return f'[{phrase}](/practice-areas/{slug})'
            return mm.group(0)

        section = re.sub(r'\*\*([^*\n]+)\*\*', replace_phrase, section)
        return heading + section

    return section_pattern.sub(transform_section, markdown)


def yaml_escape(s):
    """Escape a string for safe insertion into a YAML double-quoted scalar."""
    return s.replace('\\', '\\\\').replace('"', '\\"')


def update_stub(slug, seo, body_md):
    md_path = PRACTICE_DIR / f'{slug}.md'
    if not md_path.exists():
        return create_new_stub(slug, seo, body_md)

    content = md_path.read_text(encoding='utf-8')
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n?(.*)$', content, re.DOTALL)
    if not m:
        print(f'  WARN: {slug}.md has no YAML frontmatter; replacing whole file.')
        return create_new_stub(slug, seo, body_md)
    fm = m.group(1)

    # Flip draft true -> false.
    fm = re.sub(r'^draft:\s*true\s*$', 'draft: false', fm, flags=re.MULTILINE)
    if not re.search(r'^draft:', fm, re.MULTILINE):
        fm = fm.rstrip() + '\ndraft: false'

    # Replace or insert seoTitle / seoDescription.
    if 'seoTitle' in seo:
        new = f'seoTitle: "{yaml_escape(seo["seoTitle"])}"'
        if re.search(r'^seoTitle:.*$', fm, re.MULTILINE):
            fm = re.sub(r'^seoTitle:.*$', new, fm, flags=re.MULTILINE)
        else:
            fm = fm.rstrip() + '\n' + new
    if 'seoDescription' in seo:
        new = f'seoDescription: "{yaml_escape(seo["seoDescription"])}"'
        if re.search(r'^seoDescription:.*$', fm, re.MULTILINE):
            fm = re.sub(r'^seoDescription:.*$', new, fm, flags=re.MULTILINE)
        else:
            fm = fm.rstrip() + '\n' + new

    out = f'---\n{fm.rstrip()}\n---\n\n{body_md}'
    md_path.write_text(out, encoding='utf-8', newline='\n')
    return 'updated'


def create_new_stub(slug, seo, body_md):
    md_path = PRACTICE_DIR / f'{slug}.md'
    defaults = NEW_STUB_DEFAULTS.get(slug, {})
    name = defaults.get('name') or slug.replace('-', ' ').title()
    tagline = defaults.get('tagline', '')
    priority = defaults.get('priority', 99)
    featured = defaults.get('featured', False)
    statutes = defaults.get('statutes', [])
    intake = seo.get('seoDescription', '')[:280]

    lines = ['---']
    lines.append(f'name: "{yaml_escape(name)}"')
    lines.append(f'tagline: "{yaml_escape(tagline)}"')
    lines.append(f'intakeSummary: "{yaml_escape(intake)}"')
    lines.append(f'priority: {priority}')
    lines.append(f'featured: {str(featured).lower()}')
    if statutes:
        lines.append('statutes:')
        for s in statutes:
            lines.append(f'  - "{yaml_escape(s)}"')
    lines.append('draft: false')
    if 'seoTitle' in seo:
        lines.append(f'seoTitle: "{yaml_escape(seo["seoTitle"])}"')
    if 'seoDescription' in seo:
        lines.append(f'seoDescription: "{yaml_escape(seo["seoDescription"])}"')
    lines.append('---')
    lines.append('')
    lines.append(body_md.rstrip())
    lines.append('')

    md_path.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    return 'created'


def main():
    updated, created, skipped, errors = [], [], [], []

    for docx_name, slug in DOCX_TO_SLUG.items():
        docx_path = PRACTICE_DIR / docx_name
        if not docx_path.exists():
            skipped.append(docx_name)
            continue
        try:
            seo, body_md = convert_docx(docx_path)
            result = update_stub(slug, seo, body_md)
            if result == 'updated':
                updated.append(slug)
            elif result == 'created':
                created.append(slug)
        except Exception as e:
            errors.append((docx_name, str(e)))
            import traceback
            traceback.print_exc()

    print('\n--- summary ---')
    print(f'Updated ({len(updated)}):')
    for s in sorted(updated):
        print(f'  {s}.md')
    print(f'Created ({len(created)}):')
    for s in sorted(created):
        print(f'  {s}.md')
    if skipped:
        print(f'Skipped — .docx not found ({len(skipped)}):')
        for n in skipped:
            print(f'  {n}')
    if errors:
        print(f'Errors ({len(errors)}):')
        for n, e in errors:
            print(f'  {n}: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
