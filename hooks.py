import re


CALLOUT_RE = re.compile(r'^\s*>\s*\[!(?P<type>[A-Za-z0-9_-]+)\](?P<collapse>[+-])?\s*(?P<title>.*)$')
FENCE_RE = re.compile(r'^\s*(```|~~~)')


def on_page_markdown(markdown, page, config, files):
    lines = markdown.splitlines()
    out = []
    in_fence = False

    i = 0
    while i < len(lines):
        line = lines[i]

        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if not in_fence:
            m = CALLOUT_RE.match(line)
            if m:
                ctype = m.group('type').lower()
                collapse = m.group('collapse')
                title = m.group('title').strip()
                title = title or None

                if collapse:
                    prefix = '???+' if collapse == '+' else '???'
                else:
                    prefix = '!!!'

                if title:
                    out.append(f'{prefix} {ctype} "{title}"')
                else:
                    out.append(f'{prefix} {ctype}')

                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if next_line.lstrip().startswith('>'):
                        content = next_line.lstrip()[1:]
                        if content.startswith(' '):
                            content = content[1:]
                        out.append('    ' + content)
                        i += 1
                    else:
                        break
                continue

        out.append(line)
        i += 1

    result = '\n'.join(out)
    if markdown.endswith('\n'):
        result += '\n'
    return result
