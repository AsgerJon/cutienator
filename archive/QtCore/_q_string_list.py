"""
QStringList is Qt's list of text.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import QList


class QStringList(QList):
  """
  Qt's QStringList, its own name for 'QList<QString>': a list of text.
  'QList[str]' is this class.

    names = QStringList(['a', 'b'])
    names.append('c')
    len(names), names[0]

  This file is written by hand, as the file of 'QList' is. Text is a
  plain 'str' in cutienator and no cute class, so no class file ends
  with the making of this kind, as the file of QUrl ends with the
  making of 'QList[QUrl]'. Its rituals are written by hand as well, in
  'q_string_list.cpp' among the ritual files of QtCore.

  What to expect
  --------------

  Everything 'QList' says. An element that is no 'str' is refused with
  'TypeError'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringList'
  #  A list of this kind holds text, which crosses as text does.
  __element_name__ = 'str'
  __element_class__ = str
  __element_crossing__ = 'text'
  #  The rituals of the list.
  __list_rituals__ = dict(
      make='ritual_list_make_QString',
      add='ritual_list_add_QString',
      size='ritual_list_size_QString',
      at='ritual_list_at_QString',
      drop='ritual_list_drop_QString',
  )
  #  Python owns its lists, and this ritual removes one.
  __delete_ritual__ = 'ritual_list_drop_QString'


QList.collect(QStringList)
