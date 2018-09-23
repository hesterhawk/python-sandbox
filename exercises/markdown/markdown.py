import re

def parse_markdown(markdown):

    markdown = markdown.replace("\n", "")

    markdown = p(markdown)
    markdown = list(markdown)
    markdown = text(markdown, '_', '<em>', '</em>')
    markdown = text(markdown, '__', '<strong>', '</strong>')

    return head(markdown)

def p(markdown):
    if re.findall(r'\*\s(.*)', markdown) == [] and re.findall(r'^#*\s(.*)', markdown) == []:
        return '<p>' + markdown + '</p>'
    
    return markdown

def list(markdown):

    items = re.findall(r'\*\s(.*)', markdown)

    if items == []: return markdown

    items = re.split(r'\*\s', markdown)[1:]

    result = ['<li>' + item + '</li>' for item in items]
    result = "<ul>" + "".join(result) + "</ul>"

    return markdown.replace("* " + "* ".join(items), result)

def head(markdown):

    head = re.findall(r'^#*\s(.*)', markdown)

    if head != []:
        # stop make header untill occurs one of this char:
        line = re.split("\*|\<",head[0])
        h = re.search(r"^\#*", markdown).group(0)
        tag = "h" + str(len(h))

        return markdown.replace(h + " " + line[0], "<"+tag+">" + line[0] + "</"+tag+">")

    return markdown

def text(markdown, pattern, tag_open, tag_close):
    
    match = re.findall(r''+pattern+'(.*?)'+pattern, markdown)

    if match == []: return markdown

    for m in match:
        if m != '':
            markdown = re.sub(pattern + m + pattern, tag_open + m + tag_close, markdown)

    return markdown