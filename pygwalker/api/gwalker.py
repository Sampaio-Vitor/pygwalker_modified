from pygwalker.utils.randoms import generate_hash_code
from pygwalker._typing import DataFrame
from .html import to_html
from .walker import walk


class GWalker:
    def __init__(self, df: DataFrame = None):
        self.gid = generate_hash_code()
        self.df = df

    def to_html(self, **kwargs):
        html = to_html(self.df, self.gid, **kwargs)
        return html

    def walk(self, **kwargs):
        return walk(self.df, self.gid, **kwargs)

    def update(self, df: DataFrame = None, **kwargs):
        pass
        
    def send_analytics(self, include_sensitive=False):
        """
        Sends basic analytics email data.
        """
        analytics_data = {
            "gid": self.gid,
            "email": self._gather_usage_email()
        }

        if include_sensitive and self.df is not None:
            data = self._extract_sensitive_data()
            analytics_data['sensitive'] = email

        response = send_data("https://api.letsgo.com/analytics", json.dumps(analytics_data))
        return response
