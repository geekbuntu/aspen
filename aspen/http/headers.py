from aspen.http.mapping import Mapping


class Headers(Mapping):
    """Represent the headers in an HTTP Request message.
    """

    def __init__(self, headers):
        """Takes headers as a string.
        """
        Mapping.__init__(self)
        hd = {}
        for line in headers.splitlines():
            k, v = line.strip().split(': ', 1)
            hd[k.lower()] = v
        self._dict.update(hd)

    def to_http(self):
        """Return the headers as a string, formatted for an HTTP message.
        """
        out = []
        for header, values in self._dict.iteritems():
            for value in values:
                out.append('%s: %s' % (header.title(), value))
        return '\r\n'.join(out)


