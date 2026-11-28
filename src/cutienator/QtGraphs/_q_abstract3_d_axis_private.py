"""
QAbstract3DAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qabstract3daxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstract3DAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAbstract3DAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAbstract3DAxisPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstract3DAxisPrivate: a plain Python object
  standing in front of one C++ QAbstract3DAxisPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstract3DAxisPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DAxisPrivate that has a ritual and that
  Python can call so far, 11 names in all: 'q_func', 'setOrientation',
  'isDefaultAxis', 'setDefaultAxis', 'setRange', 'setMin', 'setMax',
  'updateLabels', 'allowZero', 'allowNegatives', 'allowMinMaxSame'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstract3DAxis *QAbstract3DAxisPrivate::q_func() const':
    takes in Python what 'QAbstract3DAxis *QAbstract3DAxisPrivate::q_func()'
    takes.
  - Qt's 'QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate()': the destructor:
    Python never removes a C++ QAbstract3DAxisPrivate.

  What to expect
  --------------

  - The C++ QAbstract3DAxisPrivate is created at the first use, not by
    'QAbstract3DAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DAxisPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAbstract3DAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DAxisPrivate'

  #  The functions Qt calls itself that QAbstract3DAxisPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRange': (
          ('_ZN22QAbstract3DAxisPrivate8setRangeEffb',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
               ('float', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'setMin': (
          ('_ZN22QAbstract3DAxisPrivate6setMinEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'setMax': (
          ('_ZN22QAbstract3DAxisPrivate6setMaxEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'updateLabels': (
          ('_ZN22QAbstract3DAxisPrivate12updateLabelsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'allowZero': (
          ('_ZN22QAbstract3DAxisPrivate9allowZeroEv',
           ('bool', 'number', ''),
           ()),
      ),
      'allowNegatives': (
          ('_ZN22QAbstract3DAxisPrivate14allowNegativesEv',
           ('bool', 'number', ''),
           ()),
      ),
      'allowMinMaxSame': (
          ('_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

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

  @overload(QAbstract3DAxis.AxisOrientation)
  def setOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DAxisPrivate::setOrientation(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#setOrientation

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.
    """
    #  void QAbstract3DAxisPrivate::setOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation)
    self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate14setOrientationEN15QAbstract3DAx'
        'is15AxisOrientationE',
        orientation.value,
    )

  @overload(bool)
  def setDefaultAxis(self, isDefault: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DAxisPrivate::setDefaultAxis(bool isDefault)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#setDefaultAxis

    Parameters
    ----------

    isDefault : bool
      Passed on as it is.
    """
    #  void QAbstract3DAxisPrivate::setDefaultAxis(bool isDefault)
    self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate14setDefaultAxisEb', isDefault,
    )

  @overload(float, float)
  @overload(float, float, bool)
  def setRange(
      self,
      min: float,
      max: float,
      suppressWarnings: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QAbstract3DAxisPrivate::setRange(float min, float max,
    bool suppressWarnings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.

    suppressWarnings : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
    #      suppressWarnings)
    ritual = 'ritual_ZN22QAbstract3DAxisPrivate8setRangeEffb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstract3DAxisPrivate8setRangeEffb'
    self.uglySide.call(ritual, min, max, suppressWarnings)

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxisPrivate::setMin(float min)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxisprivate.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QAbstract3DAxisPrivate::setMin(float min)
    ritual = 'ritual_ZN22QAbstract3DAxisPrivate6setMinEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstract3DAxisPrivate6setMinEf'
    self.uglySide.call(ritual, min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QAbstract3DAxisPrivate::setMax(float max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxisprivate.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QAbstract3DAxisPrivate::setMax(float max)
    ritual = 'ritual_ZN22QAbstract3DAxisPrivate6setMaxEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstract3DAxisPrivate6setMaxEf'
    self.uglySide.call(ritual, max)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DAxis.AxisType)
  def __init__(self, type: QAbstract3DAxis.AxisType) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis::AxisType
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#QAbstract3DAxisPrivate

    Parameters
    ----------

    type : QAbstract3DAxis.AxisType
      Passed on as its number.
    """
    #  QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis::
    #      AxisType type)
    self._noteCreation(QAbstract3DAxisPrivate, lambda: Rituals.call(
        'ritual_ZN22QAbstract3DAxisPrivateC1EN15QAbstract3DAxis8AxisTypeE',
        type.value,
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

  def q_func(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QAbstract3DAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3daxisprivate.html#q_func

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QAbstract3DAxisPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate6q_funcEv',
    )
    return QAbstract3DAxis._cuteAt(address)

  def isDefaultAxis(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxisPrivate::isDefaultAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#isDefaultAxis
    """
    #  bool QAbstract3DAxisPrivate::isDefaultAxis()
    return self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate13isDefaultAxisEv',
    )

  def updateLabels(self) -> None:
    """
    Calls Qt's 'void QAbstract3DAxisPrivate::updateLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#updateLabels
    """
    #  void QAbstract3DAxisPrivate::updateLabels()
    ritual = 'ritual_ZN22QAbstract3DAxisPrivate12updateLabelsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstract3DAxisPrivate12updateLabelsEv'
    self.uglySide.call(ritual)

  def allowZero(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxisPrivate::allowZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#allowZero
    """
    #  bool QAbstract3DAxisPrivate::allowZero()
    return self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate9allowZeroEv',
    )

  def allowNegatives(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxisPrivate::allowNegatives()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#allowNegatives
    """
    #  bool QAbstract3DAxisPrivate::allowNegatives()
    return self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate14allowNegativesEv',
    )

  def allowMinMaxSame(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DAxisPrivate::allowMinMaxSame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#allowMinMaxSame
    """
    #  bool QAbstract3DAxisPrivate::allowMinMaxSame()
    return self.uglySide.call(
        'ritual_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv',
    )
