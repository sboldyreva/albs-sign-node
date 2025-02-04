# -*- mode:python; coding:utf-8; -*-
# author: Eugene Zamriy <ezamriy@cloudlinux.com>
# created: 2018-03-31

"""
CloudLinux Build System builds sign node configuration storage.
"""

from .utils.config import BaseConfig
from .utils.file_utils import normalize_path

__all__ = ["SignNodeConfig"]


DEFAULT_MASTER_URL = 'http://web_server:8000/api/v1/'
DEFAULT_PULP_HOST = "http://pulp"
DEFAULT_PULP_USER = "pulp"
DEFAULT_PULP_PASSWORD = "test_pwd"
DEFAULT_PULP_CHUNK_SIZE = 8388608  # 8 MiB


class SignNodeConfig(BaseConfig):
    def __init__(self, config_file=None, **cmd_args):
        """
        Builds sign node configuration initialization.

        Parameters
        ----------
        config_file : str, optional
            Configuration file path.
        cmd_args : dict
            Command line arguments.
        """
        default_config = {
            "development_mode": False,
            "pgp_keys": {},
            "master_url": DEFAULT_MASTER_URL,
            "node_id": self.generate_node_id(postfix=".sign"),
            "working_dir": "/srv/alternatives/sign_node",
            "pulp_host": DEFAULT_PULP_HOST,
            "pulp_user": DEFAULT_PULP_USER,
            "pulp_password": DEFAULT_PULP_PASSWORD,
            "pulp_chunk_size": DEFAULT_PULP_CHUNK_SIZE,
        }
        schema = {
            "development_mode": {"type": "boolean", "default": False},
            "pgp_keys": {
                "type": "dict",
                "required": True,
                "empty": False,
            },
            "node_id": {"type": "string", "required": True},
            "master_url": {"type": "string", "required": True},
            "working_dir": {"type": "string", "required": True,
                            "coerce": normalize_path},
            "pulp_host": {"type": "string", "nullable": False},
            "pulp_user": {"type": "string", "nullable": False},
            "pulp_password": {"type": "string", "nullable": False},
            "pulp_chunk_size": {"type": "integer", "nullable": False},
            "jwt_token": {"type": "string", "nullable": True},
        }
        super(SignNodeConfig, self).__init__(
            default_config, config_file, schema, **cmd_args
        )
