#!/usr/bin/env python3
""" Unittest module """

from typing import Dict
import unittest
from unittest.mock import patch, Mock, PropertyMock
from mock import MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_json) -> None:
        """ Test method returns correct output """
        endpoint = 'https://api.github.com/orgs/{}'.format(org)
        spec = GithubOrgClient(org)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result) -> None:
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        payload_gen = {
            "repos_url": "https://api.github.com/users/georgeeset/repos",
            "repos": [
                {
                    "id": 598049160,
                    "node_id": "R_kgDOI6WBiA",
                    "name": "AirBnB_clone",
                    "full_name": "georgeeset/AirBnB_clone",
                    "private": False,
                    "pushed_at": "2023-02-20T23:14:29Z",
                    "git_url": "git://github.com/georgeeset/AirBnB_clone.git",
                    "ssh_url": "git@github.com:georgeeset/AirBnB_clone.git",
                    "svn_url": "https://github.com/georgeeset/AirBnB_clone",
                    "size": 64,
                    "stargazers_count": 0,
                    "watchers_count": 0,
                    "language": "Python",
                    "disabled": False,
                    "open_issues_count": 0,
                },
                {
                    "id": 633537815,
                    "node_id": "R_kgDOJcMFFw",
                    "name": "AirBnB_clone_v3",
                    "full_name": "georgeeset/AirBnB_clone_v3",
                    "private": False,
                    "pushed_at": "2023-02-20T23:14:29Z",
                    "git_url": "git://github.com/georgeeset/AirBnB_clone.git",
                    "ssh_url": "git@github.com:georgeeset/AirBnB_clone.git",
                    "svn_url": "https://github.com/georgeeset/AirBnB_clone",
                    "size": 64,
                    "stargazers_count": 0,
                    "watchers_count": 0,
                    "language": "Python",
                    "disabled": False,
                    "open_issues_count": 0,
                    "allow_forking": True,
                 },

            ]
        }
        mock_get_json.return_value = payload_gen["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = payload_gen["repos_url"]
            self.assertEqual(
                GithubOrgClient("georgeeset").public_repos(),
                [
                    "AirBnB_clone",
                    "AirBnB_clone_v3",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        @parameterized.expand([
                ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
                ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
            ])
        def test_has_license(self, repo: Dict,
                             key: str, expected: bool
                             ) -> None:
            """Tests the `has_license` method."""
            gh_org_client = GithubOrgClient("google")
            client_has_licence = gh_org_client.has_license(repo, key)
            self.assertEqual(client_has_licence, expected)
