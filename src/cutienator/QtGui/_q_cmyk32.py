"""
QCmyk32 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcmyk_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QCmyk32 to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QCmyk32(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCmyk32: a plain Python object standing in front of
  one C++ QCmyk32.

  C++ hands a QCmyk32 around as a copy, so every C++ QCmyk32 behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCmyk32 that has a ritual and that Python can call
  so far, 11 names in all: 'cyan', 'magenta', 'yellow', 'black', 'toColor',
  'toUint', 'fromCmyk32', 'fromRgba', 'fromColor', '__eq__', '__ne__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCmyk32::~QCmyk32()': the destructor: Python removes its C++
    QCmyk32 by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCmyk32 is created at the first use, not by 'QCmyk32(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCmyk32 back gives a copy the ritual made for Python,
    in a new cute QCmyk32.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromCmyk32(cmyk: int) -> QCmyk32:
    """
    Calls Qt's 'QCmyk32 QCmyk32::fromCmyk32(uint cmyk)'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#fromCmyk32

    Parameters
    ----------

    cmyk : int
      Passed on as it is.

    Returns
    -------

    QCmyk32
      A new cute QCmyk32 around the copy Qt gave back. Python owns it.
    """
    #  QCmyk32 QCmyk32::fromCmyk32(uint cmyk)
    address = Rituals.call('ritual_ZN7QCmyk3210fromCmyk32Ej', cmyk)
    return QCmyk32._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromRgba(rgba: int) -> QCmyk32:
    """
    Calls Qt's 'QCmyk32 QCmyk32::fromRgba(QRgb rgba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#fromRgba

    Parameters
    ----------

    rgba : int
      Passed on as it is.

    Returns
    -------

    QCmyk32
      A new cute QCmyk32 around the copy Qt gave back. Python owns it.
    """
    #  QCmyk32 QCmyk32::fromRgba(QRgb rgba)
    address = Rituals.call('ritual_ZN7QCmyk328fromRgbaEj', rgba)
    return QCmyk32._cuteOwning(address)

  @staticmethod
  @overload(QColor)
  def fromColor(color: QColor) -> QCmyk32:
    """
    Calls Qt's 'QCmyk32 QCmyk32::fromColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#fromColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QCmyk32
      A new cute QCmyk32 around the copy Qt gave back. Python owns it.
    """
    #  QCmyk32 QCmyk32::fromColor(const QColor &color)
    address = Rituals.call(
        'ritual_ZN7QCmyk329fromColorERK6QColor', CuteMixin._valueOf(color),
    )
    return QCmyk32._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCmyk32'

  #  Qt's '~QCmyk32()'. Naming it makes this a value class: Python owns every
  #  C++ QCmyk32 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QCmyk32D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cyan(self) -> int:
    """
    Calls Qt's 'int QCmyk32::cyan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#cyan
    """
    #  int QCmyk32::cyan() const
    return self.uglySide.call('ritual_ZNK7QCmyk324cyanEv')

  def magenta(self) -> int:
    """
    Calls Qt's 'int QCmyk32::magenta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#magenta
    """
    #  int QCmyk32::magenta() const
    return self.uglySide.call('ritual_ZNK7QCmyk327magentaEv')

  def yellow(self) -> int:
    """
    Calls Qt's 'int QCmyk32::yellow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#yellow
    """
    #  int QCmyk32::yellow() const
    return self.uglySide.call('ritual_ZNK7QCmyk326yellowEv')

  def black(self) -> int:
    """
    Calls Qt's 'int QCmyk32::black() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#black
    """
    #  int QCmyk32::black() const
    return self.uglySide.call('ritual_ZNK7QCmyk325blackEv')

  def toColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCmyk32::toColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#toColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCmyk32::toColor() const
    address = self.uglySide.call('ritual_ZNK7QCmyk327toColorEv')
    from . import QColor
    return QColor._cuteOwning(address)

  def toUint(self) -> int:
    """
    Calls Qt's 'uint QCmyk32::toUint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#toUint
    """
    #  uint QCmyk32::toUint() const
    return self.uglySide.call('ritual_ZNK7QCmyk326toUintEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCmyk32) -> bool:
    """
    Calls Qt's 'bool operator==(const QCmyk32 &lhs, const QCmyk32 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#operator==

    Parameters
    ----------

    rhs : QCmyk32
      Passed on as a value: Qt reads the C++ QCmyk32, which stays Python's
      own.
    """
    #  bool operator==(const QCmyk32 &lhs, const QCmyk32 &rhs)
    return Rituals.call(
        'ritual_ZeqRK7QCmyk32S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QCmyk32) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCmyk32 &lhs, const QCmyk32 &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#operator!=

    Parameters
    ----------

    rhs : QCmyk32
      Passed on as a value: Qt reads the C++ QCmyk32, which stays Python's
      own.
    """
    #  bool operator!=(const QCmyk32 &lhs, const QCmyk32 &rhs)
    return Rituals.call(
        'ritual_ZneRK7QCmyk32S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCmyk32::QCmyk32()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#QCmyk32
    """
    #  QCmyk32::QCmyk32()
    self._noteCreation(QCmyk32, lambda: Rituals.call(
        'ritual_ZN7QCmyk32C1Ev',
    ))

  @overload(int, int, int, int)
  def __init__(
      self,
      cyan: int,
      magenta: int,
      yellow: int,
      black: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCmyk32::QCmyk32(int cyan, int magenta,
    int yellow, int black)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcmyk32.html#QCmyk32

    Parameters
    ----------

    cyan : int
      Passed on as it is.

    magenta : int
      Passed on as it is.

    yellow : int
      Passed on as it is.

    black : int
      Passed on as it is.
    """
    #  QCmyk32::QCmyk32(int cyan, int magenta, int yellow, int black)
    self._noteCreation(QCmyk32, lambda: Rituals.call(
        'ritual_ZN7QCmyk32C1Eiiii', cyan, magenta, yellow, black,
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
