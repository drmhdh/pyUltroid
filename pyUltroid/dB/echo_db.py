# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import udB


def get_stuff():
    a = udB.get("ECHO")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        udB.delete("ECHO")
    return {}


def add_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user not in k:
            k.append(user)
        x.update({chat: k})
    except BaseException:
        x.update({chat: [user]})
    return udB.set("ECHO", str(x))


def rem_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user in k:
            k.remove(user)
        x.update({chat: k})
    except BaseException:
        pass
    return udB.set("ECHO", str(x))


def check_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user in k:
            return True
        return
    except BaseException:
        return


def list_echo(chat):
    x = get_stuff()
    try:
        return x[chat]
    except BaseException:
        return
