"""
QBig5Codec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbig5codec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBig5Codec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from ..QtCore import QList
from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QBig5Codec(QTextCodec):
  """
  The cute side of Qt's QBig5Codec: a plain Python object standing in front
  of one C++ QBig5Codec.

  It is built on the cute 'QTextCodec', as Qt's QBig5Codec is built on Qt's
  QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBig5Codec that has a ritual and that Python can
  call so far, 6 names in all: '_name', '_aliases', '_mibEnum', 'name',
  'aliases', 'mibEnum'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QBig5Codec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QBig5Codec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QBig5Codec is created at the first use, not by 'QBig5Codec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBig5Codec.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _name() -> QByteArray:
    """
    Calls Qt's 'QByteArray QBig5Codec::_name()'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#_name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QBig5Codec::_name()
    address = Rituals.call('ritual_ZN10QBig5Codec5_nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def _aliases() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QBig5Codec::_aliases()'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#_aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QBig5Codec::_aliases()
    address = Rituals.call('ritual_ZN10QBig5Codec8_aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def _mibEnum() -> int:
    """
    Calls Qt's 'int QBig5Codec::_mibEnum()'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#_mibEnum
    """
    #  int QBig5Codec::_mibEnum()
    return Rituals.call('ritual_ZN10QBig5Codec8_mibEnumEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBig5Codec'

  #  A C++ QBig5Codec Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBig5Codec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QBig5Codec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QBig5Codec::name() const
    ritual = 'ritual_ZNK10QBig5Codec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QBig5Codec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def aliases(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QBig5Codec::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QBig5Codec::aliases() const
    address = self.uglySide.call('ritual_ZNK10QBig5Codec7aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QBig5Codec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbig5codec.html#mibEnum
    """
    #  int QBig5Codec::mibEnum() const
    ritual = 'ritual_ZNK10QBig5Codec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QBig5Codec7mibEnumEv'
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
