"""
QMagnetometer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qmagnetometer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QMagnetometerPrivate, QMagnetometerReading

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMagnetometer(QSensor):
  """
  The cute side of Qt's QMagnetometer: a plain Python object standing in
  front of one C++ QMagnetometer.

  It is built on the cute 'QSensor', as Qt's QMagnetometer is built on Qt's
  QSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMagnetometer that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'reading',
  'returnGeoValues', 'setReturnGeoValues', 'returnGeoValuesChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMagnetometer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMagnetometer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMagnetometer::~QMagnetometer()': the destructor: Python never
    removes a C++ QMagnetometer.
  - Qt's 'const QMagnetometerPrivate *QMagnetometer::d_func() const': takes
    in Python what 'QMagnetometerPrivate *QMagnetometer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMagnetometer is created at the first use, not by
    'QMagnetometer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMagnetometer.
  - Qt tells when it has removed the C++ QMagnetometer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QMagnetometer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#tr

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
    #  QString QMagnetometer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QMagnetometer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMagnetometer'

  #  A C++ QMagnetometer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMagnetometer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMagnetometer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMagnetometer::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QMagnetometer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reading(self) -> Optional[QMagnetometerReading]:
    """
    Calls Qt's 'QMagnetometerReading *QMagnetometer::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#reading

    Returns
    -------

    Optional[QMagnetometerReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMagnetometerReading *QMagnetometer::reading() const
    address = self.uglySide.call('ritual_ZNK13QMagnetometer7readingEv')
    from . import QMagnetometerReading
    return QMagnetometerReading._cuteAt(address)

  def returnGeoValues(self) -> bool:
    """
    Calls Qt's 'bool QMagnetometer::returnGeoValues() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#returnGeoValues
    """
    #  bool QMagnetometer::returnGeoValues() const
    return self.uglySide.call('ritual_ZNK13QMagnetometer15returnGeoValuesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setReturnGeoValues(self, returnGeoValues: bool) -> None:
    """
    Calls Qt's 'void QMagnetometer::setReturnGeoValues(bool
    returnGeoValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometer.html#setReturnGeoValues

    Parameters
    ----------

    returnGeoValues : bool
      Passed on as it is.
    """
    #  void QMagnetometer::setReturnGeoValues(bool returnGeoValues)
    self.uglySide.call(
        'ritual_ZN13QMagnetometer18setReturnGeoValuesEb', returnGeoValues,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QMagnetometer::QMagnetometer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#QMagnetometer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMagnetometer::QMagnetometer(QObject *parent)
    self._noteCreation(QMagnetometer, lambda: Rituals.call(
        'ritual_ZN13QMagnetometerC1EP7QObject',
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

  @overload(bool)
  def returnGeoValuesChanged(self, returnGeoValues: bool) -> None:
    """
    Calls Qt's 'void QMagnetometer::returnGeoValuesChanged(bool
    returnGeoValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometer.html#returnGeoValuesChanged

    Parameters
    ----------

    returnGeoValues : bool
      Passed on as it is.
    """
    #  void QMagnetometer::returnGeoValuesChanged(bool returnGeoValues)
    self.uglySide.call(
        'ritual_ZN13QMagnetometer22returnGeoValuesChangedEb',
        returnGeoValues,
    )

  def d_func(self) -> Optional[QMagnetometerPrivate]:
    """
    Calls Qt's 'QMagnetometerPrivate *QMagnetometer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometer.html#d_func

    Returns
    -------

    Optional[QMagnetometerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMagnetometerPrivate *QMagnetometer::d_func()
    address = self.uglySide.call('ritual_ZN13QMagnetometer6d_funcEv')
    from . import QMagnetometerPrivate
    return QMagnetometerPrivate._cuteAt(address)
