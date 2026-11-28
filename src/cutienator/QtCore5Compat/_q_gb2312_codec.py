"""
QGb2312Codec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGb2312Codec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QGb18030Codec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QGb2312Codec(QGb18030Codec):
  """
  The cute side of Qt's QGb2312Codec: a plain Python object standing in front
  of one C++ QGb2312Codec.

  It is built on the cute 'QGb18030Codec', as Qt's QGb2312Codec is built on
  Qt's QGb18030Codec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGb2312Codec that has a ritual and that Python can
  call so far, 5 names in all: '_name', '_aliases', '_mibEnum', 'name',
  'mibEnum'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QGb2312Codec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QGb2312Codec::convertFromUnicode(const QChar *a0, int
    a1, ConverterState *a2) const': names 'QTextCodec::ConverterState', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QGb2312Codec is created at the first use, not by
    'QGb2312Codec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGb2312Codec.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _name() -> QByteArray:
    """
    Calls Qt's 'QByteArray QGb2312Codec::_name()'.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#_name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGb2312Codec::_name()
    address = Rituals.call('ritual_ZN12QGb2312Codec5_nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def _aliases() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QGb2312Codec::_aliases()'.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#_aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QGb2312Codec::_aliases()
    address = Rituals.call('ritual_ZN12QGb2312Codec8_aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def _mibEnum() -> int:
    """
    Calls Qt's 'int QGb2312Codec::_mibEnum()'.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#_mibEnum
    """
    #  int QGb2312Codec::_mibEnum()
    return Rituals.call('ritual_ZN12QGb2312Codec8_mibEnumEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGb2312Codec'

  #  A C++ QGb2312Codec Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGb2312Codec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QGb2312Codec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGb2312Codec::name() const
    ritual = 'ritual_ZNK12QGb2312Codec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QGb2312Codec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QGb2312Codec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#mibEnum
    """
    #  int QGb2312Codec::mibEnum() const
    ritual = 'ritual_ZNK12QGb2312Codec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QGb2312Codec7mibEnumEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGb2312Codec::QGb2312Codec()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgb2312codec.html#QGb2312Codec
    """
    #  QGb2312Codec::QGb2312Codec()
    self._noteCreation(QGb2312Codec, lambda: Rituals.call(
        'ritual_ZN12QGb2312CodecC1Ev',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
