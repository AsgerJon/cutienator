"""
QGbkCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qgb18030codec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGbkCodec to be private: it declares the class in a header it
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


class QGbkCodec(QGb18030Codec):
  """
  The cute side of Qt's QGbkCodec: a plain Python object standing in front of
  one C++ QGbkCodec.

  It is built on the cute 'QGb18030Codec', as Qt's QGbkCodec is built on Qt's
  QGb18030Codec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGbkCodec that has a ritual and that Python can call
  so far, 6 names in all: '_name', '_aliases', '_mibEnum', 'name', 'aliases',
  'mibEnum'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QGbkCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QGbkCodec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QGbkCodec is created at the first use, not by 'QGbkCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGbkCodec.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _name() -> QByteArray:
    """
    Calls Qt's 'QByteArray QGbkCodec::_name()'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#_name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGbkCodec::_name()
    address = Rituals.call('ritual_ZN9QGbkCodec5_nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def _aliases() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QGbkCodec::_aliases()'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#_aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QGbkCodec::_aliases()
    address = Rituals.call('ritual_ZN9QGbkCodec8_aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def _mibEnum() -> int:
    """
    Calls Qt's 'int QGbkCodec::_mibEnum()'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#_mibEnum
    """
    #  int QGbkCodec::_mibEnum()
    return Rituals.call('ritual_ZN9QGbkCodec8_mibEnumEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGbkCodec'

  #  A C++ QGbkCodec Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGbkCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QGbkCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGbkCodec::name() const
    ritual = 'ritual_ZNK9QGbkCodec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QGbkCodec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def aliases(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QGbkCodec::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QGbkCodec::aliases() const
    address = self.uglySide.call('ritual_ZNK9QGbkCodec7aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QGbkCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#mibEnum
    """
    #  int QGbkCodec::mibEnum() const
    ritual = 'ritual_ZNK9QGbkCodec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QGbkCodec7mibEnumEv'
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
    Notes what was given, for Qt's 'QGbkCodec::QGbkCodec()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgbkcodec.html#QGbkCodec
    """
    #  QGbkCodec::QGbkCodec()
    self._noteCreation(QGbkCodec, lambda: Rituals.call(
        'ritual_ZN9QGbkCodecC1Ev',
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
