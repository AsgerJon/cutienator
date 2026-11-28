"""
QSensorManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qsensormanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QSensor, QSensorBackend, QSensorBackendFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSensor = WAIT['QSensor']
  QSensorBackendFactory = WAIT['QSensorBackendFactory']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSensorManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSensorManager: a plain Python object standing in
  front of one C++ QSensorManager.

  C++ hands a QSensorManager around as a copy, so every C++ QSensorManager
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSensorManager that has a ritual and that Python can
  call so far, 5 names in all: 'registerBackend', 'unregisterBackend',
  'isBackendRegistered', 'createBackend', 'setDefaultBackend'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSensorManager::~QSensorManager()': the destructor: Python removes
    its C++ QSensorManager by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSensorManager is created at the first use, not by
    'QSensorManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSensorManager back gives a copy the ritual made for
    Python, in a new cute QSensorManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArray, QSensorBackendFactory)
  @overload(QByteArray, QByteArray, NoneType)
  def registerBackend(
      type: QByteArray,
      identifier: QByteArray,
      factory: Optional[QSensorBackendFactory],
  ) -> None:
    """
    Calls Qt's 'void QSensorManager::registerBackend(const QByteArray &type,
    const QByteArray &identifier, QSensorBackendFactory *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensormanager.html#registerBackend

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    factory : Optional[QSensorBackendFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensorManager::registerBackend(const QByteArray &type, const
    #      QByteArray &identifier, QSensorBackendFactory *factory)
    Rituals.call(
        'ritual_ZN14QSensorManager15registerBackendERK10QByteArrayS2_P21QSe'
        'nsorBackendFactory',
        CuteMixin._valueOf(type), CuteMixin._valueOf(identifier),
        CuteMixin._addressOf(factory),
    )

  @staticmethod
  @overload(QByteArray, QByteArray)
  def unregisterBackend(type: QByteArray, identifier: QByteArray) -> None:
    """
    Calls Qt's 'void QSensorManager::unregisterBackend(const QByteArray
    &type, const QByteArray &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensormanager.html#unregisterBackend

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSensorManager::unregisterBackend(const QByteArray &type, const
    #      QByteArray &identifier)
    Rituals.call(
        'ritual_ZN14QSensorManager17unregisterBackendERK10QByteArrayS2_',
        CuteMixin._valueOf(type), CuteMixin._valueOf(identifier),
    )

  @staticmethod
  @overload(QByteArray, QByteArray)
  def isBackendRegistered(type: QByteArray, identifier: QByteArray) -> bool:
    """
    Calls Qt's 'bool QSensorManager::isBackendRegistered(const QByteArray
    &type, const QByteArray &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensormanager.html#isBackendRegistered

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QSensorManager::isBackendRegistered(const QByteArray &type, const
    #      QByteArray &identifier)
    return Rituals.call(
        'ritual_ZN14QSensorManager19isBackendRegisteredERK10QByteArrayS2_',
        CuteMixin._valueOf(type), CuteMixin._valueOf(identifier),
    )

  @staticmethod
  @overload(QSensor)
  @overload(NoneType)
  def createBackend(sensor: Optional[QSensor]) -> Optional[QSensorBackend]:
    """
    Calls Qt's 'QSensorBackend *QSensorManager::createBackend(QSensor
    *sensor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensormanager.html#createBackend

    Parameters
    ----------

    sensor : Optional[QSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSensorBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorBackend *QSensorManager::createBackend(QSensor *sensor)
    address = Rituals.call(
        'ritual_ZN14QSensorManager13createBackendEP7QSensor',
        CuteMixin._addressOf(sensor),
    )
    from . import QSensorBackend
    return QSensorBackend._cuteAt(address)

  @staticmethod
  @overload(QByteArray, QByteArray)
  def setDefaultBackend(type: QByteArray, identifier: QByteArray) -> None:
    """
    Calls Qt's 'void QSensorManager::setDefaultBackend(const QByteArray
    &type, const QByteArray &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensormanager.html#setDefaultBackend

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSensorManager::setDefaultBackend(const QByteArray &type, const
    #      QByteArray &identifier)
    Rituals.call(
        'ritual_ZN14QSensorManager17setDefaultBackendERK10QByteArrayS2_',
        CuteMixin._valueOf(type), CuteMixin._valueOf(identifier),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSensorManager'

  #  Qt's '~QSensorManager()'. Naming it makes this a value class: Python
  #  owns every C++ QSensorManager behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSensorManagerD1Ev'

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
