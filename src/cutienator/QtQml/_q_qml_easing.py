"""
QQmlEasing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlEasing to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEasing(QObject):
  """
  The cute side of Qt's QQmlEasing: a plain Python object standing in front
  of one C++ QQmlEasing.

  It is built on the cute 'QObject', as Qt's QQmlEasing is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlEasing that has a ritual and that Python can
  call so far, 3 names in all: 'metaObject', 'tr', 'valueForProgress'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlEasing::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlEasing::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlEasing::qt_qmlMarker_singleton()': one of Qt's own inner
    workings.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlEasing is created at the first use, not by 'QQmlEasing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlEasing.
  - Qt tells when it has removed the C++ QQmlEasing. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlEasing, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QQmlEasing::Type' of Qt, with the 47 names Qt gives in it.
    """

    Linear = Kee[int](0)
    InQuad = Kee[int](1)
    OutQuad = Kee[int](2)
    InOutQuad = Kee[int](3)
    OutInQuad = Kee[int](4)
    InCubic = Kee[int](5)
    OutCubic = Kee[int](6)
    InOutCubic = Kee[int](7)
    OutInCubic = Kee[int](8)
    InQuart = Kee[int](9)
    OutQuart = Kee[int](10)
    InOutQuart = Kee[int](11)
    OutInQuart = Kee[int](12)
    InQuint = Kee[int](13)
    OutQuint = Kee[int](14)
    InOutQuint = Kee[int](15)
    OutInQuint = Kee[int](16)
    InSine = Kee[int](17)
    OutSine = Kee[int](18)
    InOutSine = Kee[int](19)
    OutInSine = Kee[int](20)
    InExpo = Kee[int](21)
    OutExpo = Kee[int](22)
    InOutExpo = Kee[int](23)
    OutInExpo = Kee[int](24)
    InCirc = Kee[int](25)
    OutCirc = Kee[int](26)
    InOutCirc = Kee[int](27)
    OutInCirc = Kee[int](28)
    InElastic = Kee[int](29)
    OutElastic = Kee[int](30)
    InOutElastic = Kee[int](31)
    OutInElastic = Kee[int](32)
    InBack = Kee[int](33)
    OutBack = Kee[int](34)
    InOutBack = Kee[int](35)
    OutInBack = Kee[int](36)
    InBounce = Kee[int](37)
    OutBounce = Kee[int](38)
    InOutBounce = Kee[int](39)
    OutInBounce = Kee[int](40)
    InCurve = Kee[int](41)
    OutCurve = Kee[int](42)
    SineCurve = Kee[int](43)
    CosineCurve = Kee[int](44)
    BezierSpline = Kee[int](45)
    Bezier = Kee[int](45)

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
    Calls Qt's 'QString QQmlEasing::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasing.html#tr

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
    #  QString QQmlEasing::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQmlEasing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEasing'

  #  A C++ QQmlEasing Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlEasing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlEasing::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlEasing::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQmlEasing10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Type, float)
  def valueForProgress(self, type: Type, progress: float) -> float:
    """
    Calls Qt's 'qreal QQmlEasing::valueForProgress(QQmlEasing::Type type,
    qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasing.html#valueForProgress

    Parameters
    ----------

    type : Type
      Passed on as its number.

    progress : float
      Passed on as it is.
    """
    #  qreal QQmlEasing::valueForProgress(QQmlEasing::Type type, qreal
    #      progress) const
    return self.uglySide.call(
        'ritual_ZNK10QQmlEasing16valueForProgressENS_4TypeEd',
        type.value, progress,
    )

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
