"""
PieAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/pieanimation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means PieAnimation to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import ChartAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import PieSliceData, PieSliceItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  PieSliceData = WAIT['PieSliceData']
  PieSliceItem = WAIT['PieSliceItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PieAnimation(ChartAnimation):
  """
  The cute side of Qt's PieAnimation: a plain Python object standing in front
  of one C++ PieAnimation.

  It is built on the cute 'ChartAnimation', as Qt's PieAnimation is built on
  Qt's ChartAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PieAnimation that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'updateValue', 'addSlice',
  'removeSlice', 'updateCurrentValue'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PieAnimation::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PieAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PieAnimation::PieAnimation(PieChartItem *item, int duration,
    QEasingCurve &curve)': takes a type Python has no way to hand over yet.
  - Qt's 'PieAnimation::~PieAnimation()': the destructor: Python never
    removes a C++ PieAnimation.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PieAnimation is created at the first use, not by
    'PieAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PieAnimation.
  - Qt tells when it has removed the C++ PieAnimation. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's PieAnimation that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString PieAnimation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/pieanimation.html#tr

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
    #  QString PieAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12PieAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PieAnimation'

  #  A C++ PieAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PieAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PieAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/pieanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PieAnimation::metaObject() const
    address = self.uglySide.call('ritual_ZNK12PieAnimation10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'PieAnimation::PieAnimation(PieChartItem *item, int duration,
    QEasingCurve &curve)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'PieAnimation.__init__' has no cute function yet. Qt's "
        "'PieAnimation::PieAnimation(PieChartItem *item, int duration, "
        "QEasingCurve &curve)': takes a type Python has no way to hand over "
        "yet.")

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

  @overload(PieSliceItem, PieSliceData)
  @overload(NoneType, PieSliceData)
  def updateValue(
      self,
      sliceItem: Optional[PieSliceItem],
      newValue: PieSliceData,
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *PieAnimation::updateValue(PieSliceItem
    *sliceItem, const PieSliceData &newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/pieanimation.html#updateValue

    Parameters
    ----------

    sliceItem : Optional[PieSliceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newValue : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *PieAnimation::updateValue(PieSliceItem *sliceItem,
    #      const PieSliceData &newValue)
    address = self.uglySide.call(
        'ritual_ZN12PieAnimation11updateValueEP12PieSliceItemRK12PieSliceDa'
        'ta',
        self._addressOf(sliceItem), self._valueOf(newValue),
    )
    return ChartAnimation._cuteAt(address)

  @overload(PieSliceItem, PieSliceData, bool)
  @overload(NoneType, PieSliceData, bool)
  def addSlice(
      self,
      sliceItem: Optional[PieSliceItem],
      endValue: PieSliceData,
      startupAnimation: bool,
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *PieAnimation::addSlice(PieSliceItem
    *sliceItem, const PieSliceData &endValue, bool startupAnimation)'.

    Qt's own words: https://doc.qt.io/qt-6/pieanimation.html#addSlice

    Parameters
    ----------

    sliceItem : Optional[PieSliceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    endValue : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.

    startupAnimation : bool
      Passed on as it is.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *PieAnimation::addSlice(PieSliceItem *sliceItem, const
    #      PieSliceData &endValue, bool startupAnimation)
    address = self.uglySide.call(
        'ritual_ZN12PieAnimation8addSliceEP12PieSliceItemRK12PieSliceDatab',
        self._addressOf(sliceItem), self._valueOf(endValue),
        startupAnimation,
    )
    return ChartAnimation._cuteAt(address)

  @overload(PieSliceItem)
  @overload(NoneType)
  def removeSlice(
      self,
      sliceItem: Optional[PieSliceItem],
  ) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *PieAnimation::removeSlice(PieSliceItem
    *sliceItem)'.

    Qt's own words: https://doc.qt.io/qt-6/pieanimation.html#removeSlice

    Parameters
    ----------

    sliceItem : Optional[PieSliceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *PieAnimation::removeSlice(PieSliceItem *sliceItem)
    address = self.uglySide.call(
        'ritual_ZN12PieAnimation11removeSliceEP12PieSliceItem',
        self._addressOf(sliceItem),
    )
    return ChartAnimation._cuteAt(address)

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void PieAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/pieanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void PieAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN12PieAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12PieAnimation18updateCurrentValueERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(value))
