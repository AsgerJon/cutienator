"""
QHash stands for Qt's QHash.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ..cute import CuteMap


class QHash(CuteMap):
  """
  Qt's QHash: a value at each of its keys, kept in no order. Qt
  has one class of QHash for each kind of key and value, and
  'QHash[int, QByteArray]' is the class of one such kind, which C++
  writes 'QHash<int, QByteArray>'.

    found = QHash[int, QByteArray]({1: QByteArray(b'a')})
    len(found), found[1], 1 in found

  This file is written by hand: Qt's QHash is a pattern for classes
  and no class the dev tooling reads. Everything it does is in
  'cutienator.cute.CuteMap', which it shares with 'QMap'. The two
  are apart, as in Qt: a QHash is no QMap.

  Where the kinds come from
  -------------------------

  The class of a kind is completed at the end of the file of the class
  of its values, by 'QHash.createKind': the file of QByteArray ends with
  the making of 'QHash[int, QByteArray]'.
  Qt has a name of its own for one kind: 'QVariantHash' is
  'QHash[str, QVariant]'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for, which makes it a root; see
  #  'CuteMap'.
  __map_pattern__ = 'QHash'
