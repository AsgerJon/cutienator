"""
QRgba64 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qrgba64.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QRgba64(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRgba64: a plain Python object standing in front of
  one C++ QRgba64.

  C++ hands a QRgba64 around as a copy, so every C++ QRgba64 behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRgba64 that has a ritual and that Python can call
  so far, 21 names in all: 'fromRgba64', 'fromRgba', 'fromArgb32',
  'isOpaque', 'isTransparent', 'red', 'green', 'blue', 'alpha', 'setRed',
  'setGreen', 'setBlue', 'setAlpha', 'red8', 'green8', 'blue8', 'alpha8',
  'toArgb32', 'toRgb16', 'premultiplied', 'unpremultiplied'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'quint64 QRgba64::operator unsigned long long() const': an operator
    Python has no name for.
  - Qt's 'QRgba64::~QRgba64()': the destructor: Python removes its C++
    QRgba64 by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 32 functions Qt declares: 6 private; 1 takes or gives a type that
  cannot be passed yet.

  What to expect
  --------------

  - The C++ QRgba64 is created at the first use, not by 'QRgba64(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRgba64 back gives a copy the ritual made for Python,
    in a new cute QRgba64.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromRgba64(c: int) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::fromRgba64(quint64 c)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#fromRgba64

    Parameters
    ----------

    c : int
      Passed on as it is.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::fromRgba64(quint64 c)
    address = Rituals.call('ritual_ZN7QRgba6410fromRgba64Ey', c)
    return QRgba64._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  def fromRgba64(red: int, green: int, blue: int, alpha: int) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::fromRgba64(quint16 red, quint16 green,
    quint16 blue, quint16 alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#fromRgba64

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.

    alpha : int
      Passed on as it is.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::fromRgba64(quint16 red, quint16 green, quint16 blue,
    #      quint16 alpha)
    address = Rituals.call(
        'ritual_ZN7QRgba6410fromRgba64Etttt', red, green, blue, alpha,
    )
    return QRgba64._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  def fromRgba(red: int, green: int, blue: int, alpha: int) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::fromRgba(quint8 red, quint8 green, quint8
    blue, quint8 alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#fromRgba

    Parameters
    ----------

    red : int
      Passed on as it is.

    green : int
      Passed on as it is.

    blue : int
      Passed on as it is.

    alpha : int
      Passed on as it is.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::fromRgba(quint8 red, quint8 green, quint8 blue,
    #      quint8 alpha)
    address = Rituals.call(
        'ritual_ZN7QRgba648fromRgbaEhhhh', red, green, blue, alpha,
    )
    return QRgba64._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromArgb32(rgb: int) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::fromArgb32(uint rgb)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#fromArgb32

    Parameters
    ----------

    rgb : int
      Passed on as it is.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::fromArgb32(uint rgb)
    address = Rituals.call('ritual_ZN7QRgba6410fromArgb32Ej', rgb)
    return QRgba64._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRgba64'

  #  Qt's '~QRgba64()'. Naming it makes this a value class: Python owns every
  #  C++ QRgba64 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QRgba64D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QRgba64::isOpaque() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#isOpaque
    """
    #  bool QRgba64::isOpaque() const
    return self.uglySide.call('ritual_ZNK7QRgba648isOpaqueEv')

  def isTransparent(self) -> bool:
    """
    Calls Qt's 'bool QRgba64::isTransparent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#isTransparent
    """
    #  bool QRgba64::isTransparent() const
    return self.uglySide.call('ritual_ZNK7QRgba6413isTransparentEv')

  def red(self) -> int:
    """
    Calls Qt's 'quint16 QRgba64::red() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#red
    """
    #  quint16 QRgba64::red() const
    return self.uglySide.call('ritual_ZNK7QRgba643redEv')

  def green(self) -> int:
    """
    Calls Qt's 'quint16 QRgba64::green() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#green
    """
    #  quint16 QRgba64::green() const
    return self.uglySide.call('ritual_ZNK7QRgba645greenEv')

  def blue(self) -> int:
    """
    Calls Qt's 'quint16 QRgba64::blue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#blue
    """
    #  quint16 QRgba64::blue() const
    return self.uglySide.call('ritual_ZNK7QRgba644blueEv')

  def alpha(self) -> int:
    """
    Calls Qt's 'quint16 QRgba64::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#alpha
    """
    #  quint16 QRgba64::alpha() const
    return self.uglySide.call('ritual_ZNK7QRgba645alphaEv')

  def red8(self) -> int:
    """
    Calls Qt's 'quint8 QRgba64::red8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#red8
    """
    #  quint8 QRgba64::red8() const
    return self.uglySide.call('ritual_ZNK7QRgba644red8Ev')

  def green8(self) -> int:
    """
    Calls Qt's 'quint8 QRgba64::green8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#green8
    """
    #  quint8 QRgba64::green8() const
    return self.uglySide.call('ritual_ZNK7QRgba646green8Ev')

  def blue8(self) -> int:
    """
    Calls Qt's 'quint8 QRgba64::blue8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#blue8
    """
    #  quint8 QRgba64::blue8() const
    return self.uglySide.call('ritual_ZNK7QRgba645blue8Ev')

  def alpha8(self) -> int:
    """
    Calls Qt's 'quint8 QRgba64::alpha8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#alpha8
    """
    #  quint8 QRgba64::alpha8() const
    return self.uglySide.call('ritual_ZNK7QRgba646alpha8Ev')

  def toArgb32(self) -> int:
    """
    Calls Qt's 'uint QRgba64::toArgb32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#toArgb32
    """
    #  uint QRgba64::toArgb32() const
    return self.uglySide.call('ritual_ZNK7QRgba648toArgb32Ev')

  def toRgb16(self) -> int:
    """
    Calls Qt's 'ushort QRgba64::toRgb16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#toRgb16
    """
    #  ushort QRgba64::toRgb16() const
    return self.uglySide.call('ritual_ZNK7QRgba647toRgb16Ev')

  def premultiplied(self) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::premultiplied() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#premultiplied

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::premultiplied() const
    address = self.uglySide.call('ritual_ZNK7QRgba6413premultipliedEv')
    return QRgba64._cuteOwning(address)

  def unpremultiplied(self) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QRgba64::unpremultiplied() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#unpremultiplied

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QRgba64::unpremultiplied() const
    address = self.uglySide.call('ritual_ZNK7QRgba6415unpremultipliedEv')
    return QRgba64._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRed(self, _red: int) -> None:
    """
    Calls Qt's 'void QRgba64::setRed(quint16 _red)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#setRed

    Parameters
    ----------

    _red : int
      Passed on as it is.
    """
    #  void QRgba64::setRed(quint16 _red)
    self.uglySide.call('ritual_ZN7QRgba646setRedEt', _red)

  @overload(int)
  def setGreen(self, _green: int) -> None:
    """
    Calls Qt's 'void QRgba64::setGreen(quint16 _green)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#setGreen

    Parameters
    ----------

    _green : int
      Passed on as it is.
    """
    #  void QRgba64::setGreen(quint16 _green)
    self.uglySide.call('ritual_ZN7QRgba648setGreenEt', _green)

  @overload(int)
  def setBlue(self, _blue: int) -> None:
    """
    Calls Qt's 'void QRgba64::setBlue(quint16 _blue)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#setBlue

    Parameters
    ----------

    _blue : int
      Passed on as it is.
    """
    #  void QRgba64::setBlue(quint16 _blue)
    self.uglySide.call('ritual_ZN7QRgba647setBlueEt', _blue)

  @overload(int)
  def setAlpha(self, _alpha: int) -> None:
    """
    Calls Qt's 'void QRgba64::setAlpha(quint16 _alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#setAlpha

    Parameters
    ----------

    _alpha : int
      Passed on as it is.
    """
    #  void QRgba64::setAlpha(quint16 _alpha)
    self.uglySide.call('ritual_ZN7QRgba648setAlphaEt', _alpha)

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
    Notes what was given, for Qt's 'QRgba64::QRgba64()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrgba64.html#QRgba64
    """
    #  QRgba64::QRgba64()
    self._noteCreation(QRgba64, lambda: Rituals.call(
        'ritual_ZN7QRgba64C1Ev',
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
