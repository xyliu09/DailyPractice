import collections
import heapq
import unittest

from parameterized import parameterized


class Solution:
    def __init__(self, keys, languages):
        self.keys = keys.split(', ')
        self.key_set = set(self.keys)
        self.languages = languages
        self.language_set = set(languages)

    def _prepare_key_set(self):
        hq = []
        self.key_set = set()
        for key in self.keys:
            language_key, score = key.split(';')[0], key.split(';')[1]
            heapq.heappush(hq, (-float(score.split('=')[-1]), language_key))
            self.key_set.add(language_key)
        return hq

    def parse_accept_language(self):
        accepted = []
        for key in self.keys:
            if key in self.language_set:
                accepted.append(key)
        return accepted

    def _prepare_look_up(self):
        other_languages = []

        dic = collections.defaultdict(list)
        for language in self.languages:
            if language in self.key_set:
                dic[language] = [language]
            elif language.split('-')[0] in self.key_set:
                dic[language.split('-')[0]].append(language)
            else:
                other_languages.append(language)

        if "*" in self.key_set:
            dic["*"] = other_languages
        return dic

    def parse_accept_language2(self):
        dic = self._prepare_look_up()
        accepted = []
        for key in self.keys:
            accepted += dic[key]
        return accepted

    def parse_accept_language3(self):
        return self.parse_accept_language2()

    def parse_accept_language4(self):
        hq = self._prepare_key_set()
        dic = self._prepare_look_up()
        accepted = []
        while hq:
            _, language_key = heapq.heappop(hq)
            accepted += dic.get(language_key, [])
        return accepted


class TestSolution1(unittest.TestCase):
    @parameterized.expand([
        ["valid_input", "en-US, fr-CA, fr-FR", ["fr-FR", "en-US"], ["en-US", "fr-FR"]],
        ["empty_input", "", [], []],
        ["empty_keys", "", ["fr-FR"], []],
        ["empty_languages", "en-US, fr-CA, fr-FR", [], []],
    ])
    def test_parse_accept_language(self, name, keys, languages, results):
        parser = Solution(keys, languages)
        self.assertEqual(parser.parse_accept_language(), results)

    @parameterized.expand([
        ["en", ["en-US", "fr-CA", "fr-FR"], ["en-US"]],
        ["fr", ["en-US", "fr-CA", "fr-FR"], ["fr-CA", "fr-FR"]],
        ["fr-FR, fr", ["en-US", "fr-CA", "fr-FR"], ["fr-FR", "fr-CA"]],
    ])
    def test_parse_accept_language_2(self, keys, languages, expected_results):
        parser = Solution(keys, languages)
        self.assertEqual(parser.parse_accept_language2(), expected_results)

    @parameterized.expand([
        ["en-US, *", ["en-US", "fr-CA", "fr-FR"], ["en-US", "fr-CA", "fr-FR"]],
        ["fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"], ["fr-FR", "fr-CA", "en-US"]],
        ["fr-FR, fr", ["en-US", "fr-CA", "fr-FR"], ["fr-FR", "fr-CA"]]
    ])
    def test_parse_accept_language_3(self, keys, languages, expected_results):
        parser = Solution(keys, languages)
        self.assertEqual(parser.parse_accept_language3(), expected_results)

    @parameterized.expand([
        ["fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"], ["fr-FR", "fr-BG", "fr-CA"]],
        ["fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"], ["fr-FR", "fr-BG", "en-US", "fr-CA"]],
        ["fr-FR;q=1, fr-CA;q=0.8, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"], ["fr-FR", "fr-CA", "fr-BG", "en-US"]]
    ])
    def test_parse_accept_language_4(self, keys, languages, expected_results):
        parser = Solution(keys, languages)
        self.assertEqual(parser.parse_accept_language4(), expected_results)


if __name__ == '__main__':
    unittest.main()
