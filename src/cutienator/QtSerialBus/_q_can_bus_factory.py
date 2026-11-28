"""
QCanBusFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanbusfactory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QString
  from . import QCanBusDevice, QCanBusDeviceInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanBusFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanBusFactory: a plain Python object standing in
  front of one C++ QCanBusFactory.

  What exists
  -----------

  Every function of Qt's QCanBusFactory that has a ritual and that Python can
  call so far, 2 names in all: 'createDevice', 'availableDevices'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanBusFactory::~QCanBusFactory()': the destructor: Python never
    removes a C++ QCanBusFactory.

  What to expect
  --------------

  - The C++ QCanBusFactory is created at the first use, not by
    'QCanBusFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanBusFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanBusFactory'

  #  A C++ QCanBusFactory Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanBusFactory'

  #  The functions Qt calls itself that QCanBusFactory is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'availableDevices': (
          'QList<QCanBusDeviceInfo> '
          'QCanBusFactory::availableDevices(QString *) const',
      ),
  }

  #  The functions Qt calls itself that QCanBusFactory is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createDevice': (
          ('_ZNK14QCanBusFactory12createDeviceERK7QStringPS0_',
           ('address', 'address', 'QtSerialBus:QCanBusDevice'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QString)
  @overload(str, NoneType)
  def createDevice(
      self,
      interfaceName: str,
      errorMessage: Optional[QString],
  ) -> Optional[QCanBusDevice]:
    """
    Calls Qt's 'QCanBusDevice *QCanBusFactory::createDevice(const QString
    &interfaceName, QString *errorMessage) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusfactory.html#createDevice

    Parameters
    ----------

    interfaceName : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanBusDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanBusDevice *QCanBusFactory::createDevice(const QString
    #      &interfaceName, QString *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK14QCanBusFactory12createDeviceERK7QStringPS0_',
        interfaceName, self._addressOf(errorMessage),
    )
    from . import QCanBusDevice
    return QCanBusDevice._cuteAt(address)

  @overload(QString)
  @overload(NoneType)
  def availableDevices(
      self,
      errorMessage: Optional[QString],
  ) -> QList[QCanBusDeviceInfo]:
    """
    Calls Qt's 'QList<QCanBusDeviceInfo>
    QCanBusFactory::availableDevices(QString *errorMessage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusfactory.html#availableDevices

    Parameters
    ----------

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QCanBusDeviceInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanBusDeviceInfo> QCanBusFactory::availableDevices(QString
    #      *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK14QCanBusFactory16availableDevicesEP7QString',
        self._addressOf(errorMessage),
    )
    from . import QCanBusDeviceInfo
    return QList[QCanBusDeviceInfo]._cuteOwning(address)

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
