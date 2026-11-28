"""
QTapReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qtapsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTapReading(QSensorReading):
  """
  The cute side of Qt's QTapReading: a plain Python object standing in front
  of one C++ QTapReading.

  It is built on the cute 'QSensorReading', as Qt's QTapReading is built on
  Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTapReading that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'copyValuesFrom',
  'tapDirection', 'setTapDirection', 'isDoubleTap', 'setDoubleTap'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTapReading::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTapReading::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTapReading::~QTapReading()': the destructor: Python never removes
    a C++ QTapReading.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTapReading is created at the first use, not by
    'QTapReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTapReading.
  - Qt tells when it has removed the C++ QTapReading. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QTapReading, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class TapDirection(CuteNum):
    """
    The enum 'QTapReading::TapDirection' of Qt, with the 13 names Qt gives in
    it.
    """

    Undefined = Kee[int](0)
    X = Kee[int](1)
    Y = Kee[int](2)
    Z = Kee[int](4)
    X_Pos = Kee[int](17)
    Y_Pos = Kee[int](34)
    Z_Pos = Kee[int](68)
    X_Neg = Kee[int](257)
    Y_Neg = Kee[int](514)
    Z_Neg = Kee[int](1028)
    X_Both = Kee[int](273)
    Y_Both = Kee[int](546)
    Z_Both = Kee[int](1092)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTapReading::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTapReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTapReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTapReading'

  #  A C++ QTapReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTapReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTapReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTapReading::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTapReading10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tapDirection(self) -> TapDirection:
    """
    Calls Qt's 'TapDirection QTapReading::tapDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#tapDirection

    Returns
    -------

    TapDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TapDirection(number)'
      gives.
    """
    #  TapDirection QTapReading::tapDirection() const
    return QTapReading.TapDirection(self.uglySide.call(
        'ritual_ZNK11QTapReading12tapDirectionEv',
    ))

  def isDoubleTap(self) -> bool:
    """
    Calls Qt's 'bool QTapReading::isDoubleTap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#isDoubleTap
    """
    #  bool QTapReading::isDoubleTap() const
    return self.uglySide.call('ritual_ZNK11QTapReading11isDoubleTapEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TapDirection)
  def setTapDirection(self, tapDirection: TapDirection) -> None:
    """
    Calls Qt's 'void QTapReading::setTapDirection(TapDirection
    tapDirection)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#setTapDirection

    Parameters
    ----------

    tapDirection : TapDirection
      Passed on as its number.
    """
    #  void QTapReading::setTapDirection(TapDirection tapDirection)
    self.uglySide.call(
        'ritual_ZN11QTapReading15setTapDirectionENS_12TapDirectionE',
        tapDirection.value,
    )

  @overload(bool)
  def setDoubleTap(self, doubleTap: bool) -> None:
    """
    Calls Qt's 'void QTapReading::setDoubleTap(bool doubleTap)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#setDoubleTap

    Parameters
    ----------

    doubleTap : bool
      Passed on as it is.
    """
    #  void QTapReading::setDoubleTap(bool doubleTap)
    self.uglySide.call('ritual_ZN11QTapReading12setDoubleTapEb', doubleTap)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTapReading::QTapReading(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#QTapReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTapReading::QTapReading(QObject *parent)
    self._noteCreation(QTapReading, lambda: Rituals.call(
        'ritual_ZN11QTapReadingC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QSensorReading)
  @overload(NoneType)
  def copyValuesFrom(self, other: Optional[QSensorReading]) -> None:
    """
    Calls Qt's 'void QTapReading::copyValuesFrom(QSensorReading *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTapReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN11QTapReading14copyValuesFromEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTapReading14copyValuesFromEP14QSensorReading'
    self.uglySide.call(ritual, self._addressOf(other))
