import hashlib

from common.config import CONFIG


def passwd2md5(passwd):
    passwd_str = CONFIG['server']['passwdStr']
    hl = hashlib.md5()
    hl.update((passwd + passwd_str).encode(encoding='utf-8'))
    return hl.hexdigest()
