"""
QPieSlicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qpieslice_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPieSlicePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QPieSlice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPieSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPieSeries = WAIT['QtGraphs:QPieSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieSlicePrivate(QObjectPrivate):
  """
  The cute side of Qt's QPieSlicePrivate: a plain Python object standing in
  front of one C++ QPieSlicePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QPieSlicePrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieSlicePrivate that has a ritual and that Python
  can call so far, 10 names in all: 'get', 'setPercentage', 'setStartAngle',
  'setAngleSpan', 'updateData', 'updateSeries', 'handleSliceChange',
  'setLabelVisible', 'setLabelPosition', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPieSlicePrivate *QPieSlicePrivate::get(const QPieSlice
    *item)': takes in Python what 'QPieSlicePrivate
    *QPieSlicePrivate::get(QPieSlice *item)' takes.
  - Qt's 'QPieSlicePrivate::~QPieSlicePrivate()': the destructor: Python
    never removes a C++ QPieSlicePrivate.
  - Qt's 'const QPieSlice *QPieSlicePrivate::q_func() const': takes in Python
    what 'QPieSlice *QPieSlicePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QPieSlicePrivate is created at the first use, not by
    'QPieSlicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieSlicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPieSlice)
  @overload(NoneType)
  def get(item: Optional[QPieSlice]) -> Optional[QPieSlicePrivate]:
    """
    Calls Qt's 'QPieSlicePrivate *QPieSlicePrivate::get(QPieSlice *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#get

    Parameters
    ----------

    item : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPieSlicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlicePrivate *QPieSlicePrivate::get(QPieSlice *item)
    address = Rituals.call(
        'ritual_ZN16QPieSlicePrivate3getEP9QPieSlice',
        CuteMixin._addressOf(item),
    )
    return QPieSlicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieSlicePrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

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

  @overload(float)
  def setPercentage(self, percentage: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setPercentage(qreal percentage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setPercentage

    Parameters
    ----------

    percentage : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setPercentage(qreal percentage)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate13setPercentageEd', percentage,
    )

  @overload(float)
  def setStartAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setStartAngle(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setStartAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setStartAngle(qreal angle)
    self.uglySide.call('ritual_ZN16QPieSlicePrivate13setStartAngleEd', angle)

  @overload(float)
  def setAngleSpan(self, span: float) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setAngleSpan(qreal span)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#setAngleSpan

    Parameters
    ----------

    span : float
      Passed on as it is.
    """
    #  void QPieSlicePrivate::setAngleSpan(qreal span)
    self.uglySide.call('ritual_ZN16QPieSlicePrivate12setAngleSpanEd', span)

  @overload(bool)
  @overload(bool, bool)
  def setLabelVisible(
      self,
      visible: bool,
      forceHidden: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::setLabelVisible(bool visible, bool
    forceHidden)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setLabelVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    forceHidden : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPieSlicePrivate::setLabelVisible(bool visible, bool forceHidden)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate15setLabelVisibleEbb',
        visible, forceHidden,
    )

  @overload(QPieSlice.LabelPosition)
  def setLabelPosition(self, position: QPieSlice.LabelPosition) -> None:
    """
    Calls Qt's 'void
    QPieSlicePrivate::setLabelPosition(QPieSlice::LabelPosition position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#setLabelPosition

    Parameters
    ----------

    position : QPieSlice.LabelPosition
      Passed on as its number.
    """
    #  void QPieSlicePrivate::setLabelPosition(QPieSlice::LabelPosition
    #      position)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate16setLabelPositionEN9QPieSlice13LabelPo'
        'sitionE',
        position.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPieSlicePrivate::QPieSlicePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#QPieSlicePrivate
    """
    #  QPieSlicePrivate::QPieSlicePrivate()
    self._noteCreation(QPieSlicePrivate, lambda: Rituals.call(
        'ritual_ZN16QPieSlicePrivateC1Ev',
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

  @overload()
  @overload(bool)
  def updateData(self, clearHidden: bool = False) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::updateData(bool clearHidden)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#updateData

    Parameters
    ----------

    clearHidden : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QPieSlicePrivate::updateData(bool clearHidden)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate10updateDataEb', clearHidden,
    )

  @overload(QPieSeries)
  @overload(NoneType)
  def updateSeries(self, series: Optional[QPieSeries]) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::updateSeries(QPieSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#updateSeries

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSlicePrivate::updateSeries(QPieSeries *series)
    self.uglySide.call(
        'ritual_ZN16QPieSlicePrivate12updateSeriesEP10QPieSeries',
        self._addressOf(series),
    )

  def handleSliceChange(self) -> None:
    """
    Calls Qt's 'void QPieSlicePrivate::handleSliceChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiesliceprivate.html#handleSliceChange
    """
    #  void QPieSlicePrivate::handleSliceChange()
    self.uglySide.call('ritual_ZN16QPieSlicePrivate17handleSliceChangeEv')

  def q_func(self) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSlicePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiesliceprivate.html#q_func

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSlicePrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QPieSlicePrivate6q_funcEv')
    return QPieSlice._cuteAt(address)
