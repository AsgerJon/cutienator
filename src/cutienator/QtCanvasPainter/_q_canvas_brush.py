"""
QCanvasBrush binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasbrush.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QCanvasBrush(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasBrush: a plain Python object standing in front
  of one C++ QCanvasBrush.

  C++ hands a QCanvasBrush around as a copy, so every C++ QCanvasBrush behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasBrush that has a ritual and that Python can
  call so far, 4 names in all: 'type', '__eq__', '__ne__', '__rlshift__'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasBrush::~QCanvasBrush()': the destructor: Python removes its
    C++ QCanvasBrush by it, and has no other use for it.
  - Qt's 'QCanvasBrush &QCanvasBrush::operator=(const QCanvasBrush &brush)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasBrush::QCanvasBrush(QCanvasBrush &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QCanvasBrush &QCanvasBrush::operator=(QCanvasBrush &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanvasBrush::swap(QCanvasBrush &other)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCanvasBrush is created at the first use, not by
    'QCanvasBrush(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasBrush back gives a copy the ritual made for
    Python, in a new cute QCanvasBrush.
  - Each name of Qt's QCanvasBrush that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QCanvasBrush, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BrushType(CuteNum, scoped=True):
    """
    The enum 'QCanvasBrush::BrushType' of Qt, with the 9 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Invalid = Kee[int](0)
    LinearGradient = Kee[int](1)
    RadialGradient = Kee[int](2)
    ConicalGradient = Kee[int](3)
    BoxGradient = Kee[int](4)
    BoxShadow = Kee[int](5)
    ImagePattern = Kee[int](6)
    GridPattern = Kee[int](7)
    Custom = Kee[int](1000)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasBrush'

  #  Qt's '~QCanvasBrush()'. Naming it makes this a value class: Python owns
  #  every C++ QCanvasBrush behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCanvasBrushD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> BrushType:
    """
    Calls Qt's 'BrushType QCanvasBrush::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#type

    Returns
    -------

    BrushType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BrushType(number)' gives.
    """
    #  BrushType QCanvasBrush::type() const
    return QCanvasBrush.BrushType(self.uglySide.call(
        'ritual_ZNK12QCanvasBrush4typeEv',
    ))

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
  def __eq__(self, rhs: QCanvasBrush) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasBrush &lhs, const QCanvasBrush
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#operator==

    Parameters
    ----------

    rhs : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasBrush &lhs, const QCanvasBrush &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QCanvasBrushS1_',
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
  def __ne__(self, rhs: QCanvasBrush) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasBrush &lhs, const QCanvasBrush
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#operator!=

    Parameters
    ----------

    rhs : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasBrush &lhs, const QCanvasBrush &rhs)
    return Rituals.call(
        'ritual_ZneRK12QCanvasBrushS1_',
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

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasBrush &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCanvasBrush &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QCanvasBrush',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QCanvasBrush::QCanvasBrush()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#QCanvasBrush
    """
    #  QCanvasBrush::QCanvasBrush()
    self._noteCreation(QCanvasBrush, lambda: Rituals.call(
        'ritual_ZN12QCanvasBrushC1Ev',
    ))

  @overload(THIS)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's 'QCanvasBrush::QCanvasBrush(const
    QCanvasBrush &brush)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrush.html#QCanvasBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasBrush::QCanvasBrush(const QCanvasBrush &brush)
    self._noteCreation(QCanvasBrush, lambda: Rituals.call(
        'ritual_ZN12QCanvasBrushC1ERKS_', self._valueOf(brush),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasBrush::swap(QCanvasBrush &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasBrush.swap' has no cute function yet. Qt's 'void "
        "QCanvasBrush::swap(QCanvasBrush &other)': takes a type Python has "
        "no way to hand over yet.")
