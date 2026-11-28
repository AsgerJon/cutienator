"""
QGeoPositionInfoSourceFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeopositioninfosourcefactory.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from . import QGeoAreaMonitorSource, QGeoPositionInfoSource
  from . import QGeoSatelliteInfoSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoPositionInfoSourceFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoPositionInfoSourceFactory: a plain Python object
  standing in front of one C++ QGeoPositionInfoSourceFactory.

  What exists
  -----------

  Every function of Qt's QGeoPositionInfoSourceFactory that has a ritual and
  that Python can call so far, 3 names in all: 'positionInfoSource',
  'satelliteInfoSource', 'areaMonitor'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPositionInfoSourceFactory::~QGeoPositionInfoSourceFactory()':
    the destructor: Python never removes a C++ QGeoPositionInfoSourceFactory.

  What to expect
  --------------

  - The C++ QGeoPositionInfoSourceFactory is created at the first use, not by
    'QGeoPositionInfoSourceFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoPositionInfoSourceFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPositionInfoSourceFactory'

  #  The functions Qt calls itself that QGeoPositionInfoSourceFactory is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'positionInfoSource': (
          'QGeoPositionInfoSource '
          '*QGeoPositionInfoSourceFactory::positionInfoSource(QObject *, '
          'const QVariantMap &)',
      ),
      'satelliteInfoSource': (
          'QGeoSatelliteInfoSource '
          '*QGeoPositionInfoSourceFactory::satelliteInfoSource(QObject *, '
          'const QVariantMap &)',
      ),
      'areaMonitor': (
          'QGeoAreaMonitorSource '
          '*QGeoPositionInfoSourceFactory::areaMonitor(QObject *, const '
          'QVariantMap &)',
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

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def positionInfoSource(
      self,
      parent: Optional[QObject],
      parameters: QMap[str, QVariant],
  ) -> Optional[QGeoPositionInfoSource]:
    """
    Calls Qt's 'QGeoPositionInfoSource
    *QGeoPositionInfoSourceFactory::positionInfoSource(QObject *parent, const
    QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourcefactory.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QGeoPositionInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPositionInfoSource
    #      *QGeoPositionInfoSourceFactory::positionInfoSource(QObject
    #      *parent, const QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN29QGeoPositionInfoSourceFactory18positionInfoSourceEP7QOb'
        'jectRK4QMapI7QString8QVariantE',
        self._addressOf(parent, 'QObject'), self._valueOf(parameters),
    )
    from . import QGeoPositionInfoSource
    return QGeoPositionInfoSource._cuteAt(address)

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def satelliteInfoSource(
      self,
      parent: Optional[QObject],
      parameters: QMap[str, QVariant],
  ) -> Optional[QGeoSatelliteInfoSource]:
    """
    Calls Qt's 'QGeoSatelliteInfoSource
    *QGeoPositionInfoSourceFactory::satelliteInfoSource(QObject *parent,
    const QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourcefactory.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QGeoSatelliteInfoSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoSatelliteInfoSource
    #      *QGeoPositionInfoSourceFactory::satelliteInfoSource(QObject
    #      *parent, const QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN29QGeoPositionInfoSourceFactory19satelliteInfoSourceEP7QO'
        'bjectRK4QMapI7QString8QVariantE',
        self._addressOf(parent, 'QObject'), self._valueOf(parameters),
    )
    from . import QGeoSatelliteInfoSource
    return QGeoSatelliteInfoSource._cuteAt(address)

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def areaMonitor(
      self,
      parent: Optional[QObject],
      parameters: QMap[str, QVariant],
  ) -> Optional[QGeoAreaMonitorSource]:
    """
    Calls Qt's 'QGeoAreaMonitorSource
    *QGeoPositionInfoSourceFactory::areaMonitor(QObject *parent, const
    QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfosourcefactory.html#areaMonitor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QGeoAreaMonitorSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoAreaMonitorSource
    #      *QGeoPositionInfoSourceFactory::areaMonitor(QObject *parent, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN29QGeoPositionInfoSourceFactory11areaMonitorEP7QObjectRK4'
        'QMapI7QString8QVariantE',
        self._addressOf(parent, 'QObject'), self._valueOf(parameters),
    )
    from . import QGeoAreaMonitorSource
    return QGeoAreaMonitorSource._cuteAt(address)
