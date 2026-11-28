"""
QRhiScissor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRhiScissor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiScissor: a plain Python object standing in front
  of one C++ QRhiScissor.

  C++ hands a QRhiScissor around as a copy, so every C++ QRhiScissor behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiScissor that has a ritual and that Python can
  call so far, 3 names in all: 'setScissor', '__eq__', '__ne__'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::array<int, 4> QRhiScissor::scissor() const': gives a type
    Python has no way to take yet.
  - Qt's 'QRhiScissor::~QRhiScissor()': the destructor: Python removes its
    C++ QRhiScissor by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRhiScissor is created at the first use, not by
    'QRhiScissor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiScissor back gives a copy the ritual made for
    Python, in a new cute QRhiScissor.
  - Each name of Qt's QRhiScissor that has no cute function yet, 'scissor',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiScissor'

  #  Qt's '~QRhiScissor()'. Naming it makes this a value class: Python owns
  #  every C++ QRhiScissor behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QRhiScissorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int, int)
  def setScissor(self, x: int, y: int, w: int, h: int) -> None:
    """
    Calls Qt's 'void QRhiScissor::setScissor(int x, int y, int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiscissor.html#setScissor

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QRhiScissor::setScissor(int x, int y, int w, int h)
    self.uglySide.call('ritual_ZN11QRhiScissor10setScissorEiiii', x, y, w, h)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiScissor) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiScissor &a, const QRhiScissor &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiscissor.html#operator==

    Parameters
    ----------

    b : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  bool operator==(const QRhiScissor &a, const QRhiScissor &b)
    return Rituals.call(
        'ritual_ZeqRK11QRhiScissorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QRhiScissor) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiScissor &a, const QRhiScissor &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiscissor.html#operator!=

    Parameters
    ----------

    b : QRhiScissor
      Passed on as a value: Qt reads the C++ QRhiScissor, which stays
      Python's own.
    """
    #  bool operator!=(const QRhiScissor &a, const QRhiScissor &b)
    return Rituals.call(
        'ritual_ZneRK11QRhiScissorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    Notes what was given, for Qt's 'QRhiScissor::QRhiScissor()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiscissor.html#QRhiScissor
    """
    #  QRhiScissor::QRhiScissor()
    self._noteCreation(QRhiScissor, lambda: Rituals.call(
        'ritual_ZN11QRhiScissorC1Ev',
    ))

  @overload(int, int, int, int)
  def __init__(self, x: int, y: int, w: int, h: int) -> None:
    """
    Notes what was given, for Qt's 'QRhiScissor::QRhiScissor(int x, int y,
    int w, int h)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiscissor.html#QRhiScissor

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  QRhiScissor::QRhiScissor(int x, int y, int w, int h)
    self._noteCreation(QRhiScissor, lambda: Rituals.call(
        'ritual_ZN11QRhiScissorC1Eiiii', x, y, w, h,
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

  @staticmethod
  def scissor(*__, **_) -> Never:
    """
    Qt's 'std::array<int, 4> QRhiScissor::scissor() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiScissor.scissor' has no cute function yet. Qt's "
        "'std::array<int, 4> QRhiScissor::scissor() const': gives a type "
        "Python has no way to take yet.")
