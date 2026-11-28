"""
CandlestickAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/candlestickanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means CandlestickAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import Candlestick, ChartAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Candlestick = WAIT['Candlestick']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CandlestickAnimation(QObject):
  """
  The cute side of Qt's CandlestickAnimation: a plain Python object standing
  in front of one C++ CandlestickAnimation.

  It is built on the cute 'QObject', as Qt's CandlestickAnimation is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CandlestickAnimation that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr',
  'addCandlestick', 'candlestickAnimation', 'candlestickChangeAnimation',
  'setAnimationStart', 'stopAll', 'removeCandlestickAnimation'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CandlestickAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int CandlestickAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'CandlestickAnimation::CandlestickAnimation(CandlestickChartItem
    *item, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
  - Qt's 'CandlestickAnimation::~CandlestickAnimation()': the destructor:
    Python never removes a C++ CandlestickAnimation.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ CandlestickAnimation is created at the first use, not by
    'CandlestickAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CandlestickAnimation.
  - Qt tells when it has removed the C++ CandlestickAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's CandlestickAnimation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

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
    Calls Qt's 'QString CandlestickAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestickanimation.html#tr

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
    #  QString CandlestickAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20CandlestickAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CandlestickAnimation'

  #  A C++ CandlestickAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CandlestickAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CandlestickAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CandlestickAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20CandlestickAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Candlestick)
  @overload(NoneType)
  def setAnimationStart(self, candlestick: Optional[Candlestick]) -> None:
    """
    Calls Qt's 'void CandlestickAnimation::setAnimationStart(Candlestick
    *candlestick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html#setAnimationStart

    Parameters
    ----------

    candlestick : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CandlestickAnimation::setAnimationStart(Candlestick *candlestick)
    self.uglySide.call(
        'ritual_ZN20CandlestickAnimation17setAnimationStartEP11Candlestick',
        self._addressOf(candlestick),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'CandlestickAnimation::CandlestickAnimation(CandlestickChartItem
    *item, int duration, QEasingCurve &curve)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'CandlestickAnimation.__init__' has no cute function yet. Qt's "
        "'CandlestickAnimation::CandlestickAnimation(CandlestickChartItem "
        "*item, int duration, QEasingCurve &curve)': takes a type Python "
        "has no way to hand over yet.")

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

  @overload(Candlestick)
  @overload(NoneType)
  def addCandlestick(self, candlestick: Optional[Candlestick]) -> None:
    """
    Calls Qt's 'void CandlestickAnimation::addCandlestick(Candlestick
    *candlestick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html#addCandlestick

    Parameters
    ----------

    candlestick : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CandlestickAnimation::addCandlestick(Candlestick *candlestick)
    self.uglySide.call(
        'ritual_ZN20CandlestickAnimation14addCandlestickEP11Candlestick',
        self._addressOf(candlestick),
    )

  @overload(Candlestick)
  @overload(NoneType)
  def candlestickAnimation(
      self,
      candlestick: Optional[Candlestick],
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation
    *CandlestickAnimation::candlestickAnimation(Candlestick *candlestick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html#candlestickAnimation

    Parameters
    ----------

    candlestick : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *CandlestickAnimation::candlestickAnimation(Candlestick
    #      *candlestick)
    address = self.uglySide.call(
        'ritual_ZN20CandlestickAnimation20candlestickAnimationEP11Candlesti'
        'ck',
        self._addressOf(candlestick),
    )
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  @overload(Candlestick)
  @overload(NoneType)
  def candlestickChangeAnimation(
      self,
      candlestick: Optional[Candlestick],
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation
    *CandlestickAnimation::candlestickChangeAnimation(Candlestick
    *candlestick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html

    Parameters
    ----------

    candlestick : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation
    #      *CandlestickAnimation::candlestickChangeAnimation(Candlestick
    #      *candlestick)
    address = self.uglySide.call(
        'ritual_ZN20CandlestickAnimation26candlestickChangeAnimationEP11Can'
        'dlestick',
        self._addressOf(candlestick),
    )
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  def stopAll(self) -> None:
    """
    Calls Qt's 'void CandlestickAnimation::stopAll()'.

    Qt's own words: https://doc.qt.io/qt-6/candlestickanimation.html#stopAll
    """
    #  void CandlestickAnimation::stopAll()
    self.uglySide.call('ritual_ZN20CandlestickAnimation7stopAllEv')

  @overload(Candlestick)
  @overload(NoneType)
  def removeCandlestickAnimation(
      self,
      candlestick: Optional[Candlestick],
  ) -> None:
    """
    Calls Qt's 'void
    CandlestickAnimation::removeCandlestickAnimation(Candlestick
    *candlestick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestickanimation.html

    Parameters
    ----------

    candlestick : Optional[Candlestick]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CandlestickAnimation::removeCandlestickAnimation(Candlestick
    #      *candlestick)
    self.uglySide.call(
        'ritual_ZN20CandlestickAnimation26removeCandlestickAnimationEP11Can'
        'dlestick',
        self._addressOf(candlestick),
    )
