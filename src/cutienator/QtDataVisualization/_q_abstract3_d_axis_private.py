"""
QAbstract3DAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3daxis_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstract3DAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from . import QAbstract3DAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QAbstract3DAxisPrivate(QObject):
  """
  The cute side of Qt's QAbstract3DAxisPrivate: a plain Python object
  standing in front of one C++ QAbstract3DAxisPrivate.

  It is built on the cute 'QObject', as Qt's QAbstract3DAxisPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DAxisPrivate that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'setOrientation',
  'isDefaultAxis', 'setDefaultAxis', 'setRange', 'setMin', 'setMax',
  'updateLabels', 'allowZero', 'allowNegatives', 'allowMinMaxSame'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DAxisPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstract3DAxisPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate()': the destructor:
    Python never removes a C++ QAbstract3DAxisPrivate.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QAbstract3DAxisPrivate.

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
  - Qt tells when it has removed the C++ QAbstract3DAxisPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstract3DAxisPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
  __qt_part__ = 'QtDataVisualization'

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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DAxisPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3daxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstract3DAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis *q,
    QAbstract3DAxis::AxisType type)': leans on
    'QAbstract3DAxisPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstract3DAxisPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis "
        "*q, QAbstract3DAxis::AxisType type)': leans on "
        "'QAbstract3DAxisPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
