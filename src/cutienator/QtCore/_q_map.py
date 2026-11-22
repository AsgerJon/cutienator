"""
QMap stands for Qt's QMap.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ..cute import CuteMap


class QMap(CuteMap):
  """
  Qt's QMap: a value at each of its keys, kept in the order of the keys. Qt
  has one class of QMap for each kind of key and value, and
  'QMap[int, QVariant]' is the class of one such kind, which C++
  writes 'QMap<int, QVariant>'.

    found = QMap[int, QVariant]({1: QVariant('a')})
    len(found), found[1], 1 in found

  This file is written by hand: Qt's QMap is a pattern for classes
  and no class the dev tooling reads. Everything it does is in
  'cutienator.cute.CuteMap', which it shares with 'QHash'. The two
  are apart, as in Qt: a QMap is no QHash.

  Where the kinds come from
  -------------------------

  The class of a kind is completed at the end of the file of the class
  of its values, by 'QMap.createKind': the file of QVariant ends with
  the making of 'QMap[int, QVariant]'.
  Qt has a name of its own for one kind: 'QVariantMap' is
  'QMap[str, QVariant]'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for, which makes it a root; see
  #  'CuteMap'.
  __map_pattern__ = 'QMap'
