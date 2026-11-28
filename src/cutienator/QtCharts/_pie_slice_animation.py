"""
PieSliceAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/piesliceanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means PieSliceAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import ChartAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
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


class PieSliceAnimation(ChartAnimation):
  """
  The cute side of Qt's PieSliceAnimation: a plain Python object standing in
  front of one C++ PieSliceAnimation.

  It is built on the cute 'ChartAnimation', as Qt's PieSliceAnimation is
  built on Qt's ChartAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PieSliceAnimation that has a ritual and that Python
  can call so far, 5 names in all: 'setValue', 'updateValue',
  'currentSliceValue', 'interpolated', 'updateCurrentValue'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'PieSliceAnimation::~PieSliceAnimation()': the destructor: Python
    never removes a C++ PieSliceAnimation.

  What to expect
  --------------

  - The C++ PieSliceAnimation is created at the first use, not by
    'PieSliceAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PieSliceAnimation.
  - Qt tells when it has removed the C++ PieSliceAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PieSliceAnimation'

  #  A C++ PieSliceAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PieSliceAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      start: QVariant,
      end: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant PieSliceAnimation::interpolated(const QVariant
    &start, const QVariant &end, qreal progress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceanimation.html#interpolated

    Parameters
    ----------

    start : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    end : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant PieSliceAnimation::interpolated(const QVariant &start, const
    #      QVariant &end, qreal progress) const
    ritual = 'ritual_ZNK17PieSliceAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17PieSliceAnimation12interpolatedERK8QVariantS2_d')
    address = self.uglySide.call(
        ritual, self._valueOf(start), self._valueOf(end), progress,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PieSliceData, PieSliceData)
  def setValue(
      self,
      startValue: PieSliceData,
      endValue: PieSliceData,
  ) -> None:
    """
    Calls Qt's 'void PieSliceAnimation::setValue(const PieSliceData
    &startValue, const PieSliceData &endValue)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceanimation.html#setValue

    Parameters
    ----------

    startValue : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.

    endValue : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.
    """
    #  void PieSliceAnimation::setValue(const PieSliceData &startValue, const
    #      PieSliceData &endValue)
    self.uglySide.call(
        'ritual_ZN17PieSliceAnimation8setValueERK12PieSliceDataS2_',
        self._valueOf(startValue), self._valueOf(endValue),
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

  @overload(PieSliceItem)
  @overload(NoneType)
  def __init__(self, sliceItem: Optional[PieSliceItem]) -> None:
    """
    Notes what was given, for Qt's
    'PieSliceAnimation::PieSliceAnimation(PieSliceItem *sliceItem)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceanimation.html#PieSliceAnimation

    Parameters
    ----------

    sliceItem : Optional[PieSliceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  PieSliceAnimation::PieSliceAnimation(PieSliceItem *sliceItem)
    self._noteCreation(PieSliceAnimation, lambda: Rituals.call(
        'ritual_ZN17PieSliceAnimationC1EP12PieSliceItem',
        self._addressOf(sliceItem),
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

  @overload(PieSliceData)
  def updateValue(self, endValue: PieSliceData) -> None:
    """
    Calls Qt's 'void PieSliceAnimation::updateValue(const PieSliceData
    &endValue)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceanimation.html#updateValue

    Parameters
    ----------

    endValue : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.
    """
    #  void PieSliceAnimation::updateValue(const PieSliceData &endValue)
    self.uglySide.call(
        'ritual_ZN17PieSliceAnimation11updateValueERK12PieSliceData',
        self._valueOf(endValue),
    )

  def currentSliceValue(self) -> PieSliceData:
    """
    Calls Qt's 'PieSliceData PieSliceAnimation::currentSliceValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceanimation.html#currentSliceValue

    Returns
    -------

    PieSliceData
      A new cute PieSliceData around the copy Qt gave back. Python owns it.
    """
    #  PieSliceData PieSliceAnimation::currentSliceValue()
    address = self.uglySide.call(
        'ritual_ZN17PieSliceAnimation17currentSliceValueEv',
    )
    from . import PieSliceData
    return PieSliceData._cuteOwning(address)

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void PieSliceAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void PieSliceAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN17PieSliceAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17PieSliceAnimation18updateCurrentValueERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(value))
