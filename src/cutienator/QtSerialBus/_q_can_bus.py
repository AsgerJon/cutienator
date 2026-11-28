"""
QCanBus binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanbus.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QString
  from . import QCanBusDevice, QCanBusDeviceInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanBus(QObject):
  """
  The cute side of Qt's QCanBus: a plain Python object standing in front of
  one C++ QCanBus.

  It is built on the cute 'QObject', as Qt's QCanBus is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCanBus that has a ritual and that Python can call
  so far, 6 names in all: 'metaObject', 'tr', 'instance', 'plugins',
  'availableDevices', 'createDevice'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCanBus::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QCanBus::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCanBus is created at the first use, not by 'QCanBus(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanBus.
  - Qt tells when it has removed the C++ QCanBus. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QCanBus::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#tr

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
    #  QString QCanBus::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QCanBus2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QCanBus]:
    """
    Calls Qt's 'QCanBus *QCanBus::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#instance

    Returns
    -------

    Optional[QCanBus]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanBus *QCanBus::instance()
    address = Rituals.call('ritual_ZN7QCanBus8instanceEv')
    return QCanBus._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanBus'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCanBus::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCanBus::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QCanBus10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def plugins(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCanBus::plugins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#plugins

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCanBus::plugins() const
    address = self.uglySide.call('ritual_ZNK7QCanBus7pluginsEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  @overload(str, QString)
  @overload(str, NoneType)
  def availableDevices(
      self,
      plugin: str,
      errorMessage: Optional[QString] = None,
  ) -> QList[QCanBusDeviceInfo]:
    """
    Calls Qt's 'QList<QCanBusDeviceInfo> QCanBus::availableDevices(const
    QString &plugin, QString *errorMessage) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#availableDevices

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QCanBusDeviceInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanBusDeviceInfo> QCanBus::availableDevices(const QString
    #      &plugin, QString *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK7QCanBus16availableDevicesERK7QStringPS0_',
        plugin, self._addressOf(errorMessage),
    )
    from . import QCanBusDeviceInfo
    return QList[QCanBusDeviceInfo]._cuteOwning(address)

  @overload()
  @overload(QString)
  @overload(NoneType)
  def availableDevices(
      self,
      errorMessage: Optional[QString] = None,
  ) -> QList[QCanBusDeviceInfo]:
    """
    Calls Qt's 'QList<QCanBusDeviceInfo> QCanBus::availableDevices(QString
    *errorMessage) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#availableDevices

    Parameters
    ----------

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QCanBusDeviceInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanBusDeviceInfo> QCanBus::availableDevices(QString
    #      *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK7QCanBus16availableDevicesEP7QString',
        self._addressOf(errorMessage),
    )
    from . import QCanBusDeviceInfo
    return QList[QCanBusDeviceInfo]._cuteOwning(address)

  @overload(str, str)
  @overload(str, str, QString)
  @overload(str, str, NoneType)
  def createDevice(
      self,
      plugin: str,
      interfaceName: str,
      errorMessage: Optional[QString] = None,
  ) -> Optional[QCanBusDevice]:
    """
    Calls Qt's 'QCanBusDevice *QCanBus::createDevice(const QString &plugin,
    const QString &interfaceName, QString *errorMessage) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#createDevice

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    interfaceName : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QCanBusDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanBusDevice *QCanBus::createDevice(const QString &plugin, const
    #      QString &interfaceName, QString *errorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK7QCanBus12createDeviceERK7QStringS2_PS0_',
        plugin, interfaceName, self._addressOf(errorMessage),
    )
    from . import QCanBusDevice
    return QCanBusDevice._cuteAt(address)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QCanBus::QCanBus(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanbus.html#QCanBus

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCanBus::QCanBus(QObject *parent)
    self._noteCreation(QCanBus, lambda: Rituals.call(
        'ritual_ZN7QCanBusC1EP7QObject', self._addressOf(parent, 'QObject'),
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
