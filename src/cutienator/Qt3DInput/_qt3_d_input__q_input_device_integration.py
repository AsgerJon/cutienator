"""
Qt3DInput::QInputDeviceIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QInputDeviceIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDeviceIntegration(QObject):
  """
  The cute side of Qt's Qt3DInput::QInputDeviceIntegration: a plain Python
  object standing in front of one C++ Qt3DInput::QInputDeviceIntegration.

  It is built on the cute 'QObject', as Qt's
  Qt3DInput::QInputDeviceIntegration is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputDeviceIntegration that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'initialize', 'createPhysicalDevice', 'physicalDevice', 'deviceNames',
  'inputAspect', 'onInitialize'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QInputDeviceIntegration::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DInput::QInputDeviceIntegration::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void Qt3DInput::QInputDeviceIntegration::registerBackendType(const
    QMetaObject &metaObject, const Qt3DCore::QBackendNodeMapperPtr
    &functor)': takes a type Python has no way to hand over yet.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DInput::QInputDeviceIntegration::jobsToExecute(qint64 time)': gives a
    type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::QInputDeviceIntegration::physicalDevices() const': gives a
    type Python has no way to take yet.
  - Qt's 'QInputDeviceIntegrationPrivate
    *Qt3DInput::QInputDeviceIntegration::d_func()': gives
    'Qt3DInput::QInputDeviceIntegrationPrivate', which has no cute class yet.
  - Qt's 'const QInputDeviceIntegrationPrivate
    *Qt3DInput::QInputDeviceIntegration::d_func() const': gives
    'Qt3DInput::QInputDeviceIntegrationPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 20 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 a template.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputDeviceIntegration is created at the first use,
    not by 'Qt3DInput::QInputDeviceIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputDeviceIntegration.
  - Qt tells when it has removed the C++ Qt3DInput::QInputDeviceIntegration.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QInputDeviceIntegration that has no cute
    function yet, '__init__', 'jobsToExecute', 'physicalDevices',
    'registerBackendType', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DInput::QInputDeviceIntegration::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html#tr

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
    #  QString Qt3DInput::QInputDeviceIntegration::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput23QInputDeviceIntegration2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QInputDeviceIntegration'

  #  The functions Qt calls itself that Qt3DInput::QInputDeviceIntegration is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'jobsToExecute': (
          'std::vector<Qt3DCore::QAspectJobPtr> '
          'Qt3DInput::QInputDeviceIntegration::jobsToExecute(qint64)',
      ),
      'physicalDevices': (
          'QList<Qt3DCore::QNodeId> '
          'Qt3DInput::QInputDeviceIntegration::physicalDevices() const',
      ),
      'deviceNames': (
          'QStringList Qt3DInput::QInputDeviceIntegration::deviceNames() '
          'const',
      ),
  }

  #  The functions Qt calls itself that Qt3DInput::QInputDeviceIntegration is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'createPhysicalDevice': (
          ('_ZN9Qt3DInput23QInputDeviceIntegration20createPhysicalDeviceERK'
           '7QString',
           ('address', 'address',
            'Qt3DInput:Qt3DInput.QAbstractPhysicalDevice'),
           (
               ('address', 'text', ''),
           )),
      ),
      'physicalDevice': (
          ('_ZNK9Qt3DInput23QInputDeviceIntegration14physicalDeviceEN8Qt3DC'
           'ore7QNodeIdE',
           ('address', 'address',
            'Qt3DInput:Qt3DInput.QAbstractPhysicalDeviceBackendNode'),
           (
               ('address', 'value', 'Qt3DCore:Qt3DCore.QNodeId'),
           )),
      ),
      'onInitialize': (
          ('_ZN9Qt3DInput23QInputDeviceIntegration12onInitializeEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject
    *Qt3DInput::QInputDeviceIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QInputDeviceIntegration::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QInputDeviceIntegration10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def physicalDevice(
      self,
      id: Qt3DCore.QNodeId,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDeviceBackendNode]:
    """
    Calls Qt's 'QAbstractPhysicalDeviceBackendNode
    *Qt3DInput::QInputDeviceIntegration::physicalDevice(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDeviceBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDeviceBackendNode
    #      *Qt3DInput::QInputDeviceIntegration::physicalDevice(Qt3DCore::
    #      QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QInputDeviceIntegration14physicalDeviceEN8Qt'
        '3DCore7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DInput.QAbstractPhysicalDeviceBackendNode._cuteAt(address)

  def deviceNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DInput::QInputDeviceIntegration::deviceNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html#deviceNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DInput::QInputDeviceIntegration::deviceNames() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QInputDeviceIntegration11deviceNamesEv',
    )
    return QStringList._cuteOwning(address)

  def inputAspect(self) -> Optional[Qt3DInput.QInputAspect]:
    """
    Calls Qt's 'QInputAspect
    *Qt3DInput::QInputDeviceIntegration::inputAspect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html#inputAspect

    Returns
    -------

    Optional[Qt3DInput.QInputAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputAspect *Qt3DInput::QInputDeviceIntegration::inputAspect() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput23QInputDeviceIntegration11inputAspectEv',
    )
    return Qt3DInput.QInputAspect._cuteAt(address)

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
    - Qt's
      'Qt3DInput::QInputDeviceIntegration::QInputDeviceIntegration(QObject
      *parent)': the class is abstract, so C++ cannot make one, and the C++
      class of ours does not fill in every function it leaves open.
    - Qt's 'Qt3DInput::QInputDeviceIntegration::QInputDeviceIntegration(
      QInputDeviceIntegrationPrivate &dd, QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputDeviceIntegration.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DInput::QInputDeviceIntegration::QInputDeviceIntegration(QObjec"
        "t *parent)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open. Qt's "
        "'Qt3DInput::QInputDeviceIntegration::QInputDeviceIntegration(QInput"
        "DeviceIntegrationPrivate &dd, QObject *parent)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(WAIT['Qt3DInput.QInputAspect'])
  @overload(NoneType)
  def initialize(self, aspect: Optional[Qt3DInput.QInputAspect]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QInputDeviceIntegration::initialize(Qt3DInput::QInputAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html#initialize

    Parameters
    ----------

    aspect : Optional[Qt3DInput.QInputAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QInputDeviceIntegration::initialize(Qt3DInput::
    #      QInputAspect *aspect)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QInputDeviceIntegration10initializeEPNS_12QIn'
        'putAspectE',
        self._addressOf(aspect),
    )

  @overload(str)
  def createPhysicalDevice(
      self,
      name: str,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDevice]:
    """
    Calls Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::QInputDeviceIntegration::createPhysicalDevice(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevice
    #      *Qt3DInput::QInputDeviceIntegration::createPhysicalDevice(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput23QInputDeviceIntegration20createPhysicalDevice'
        'ERK7QString',
        name,
    )
    return Qt3DInput.QAbstractPhysicalDevice._cuteAt(address)

  def onInitialize(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputDeviceIntegration::onInitialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputdeviceintegration.html
    """
    #  void Qt3DInput::QInputDeviceIntegration::onInitialize()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput23QInputDeviceIntegration12onInitializeEv',
    )

  @staticmethod
  def jobsToExecute(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DInput::QInputDeviceIntegration::jobsToExecute(qint64 time)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputDeviceIntegration.jobsToExecute' has no cute "
        "function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DInput::QInputDeviceIntegration::jobsToExecute(qint64 time)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def physicalDevices(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::QInputDeviceIntegration::physicalDevices() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputDeviceIntegration.physicalDevices' has no cute "
        "function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DInput::QInputDeviceIntegration::physicalDevices() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def registerBackendType(*__, **_) -> Never:
    """
    - Qt's 'void
      Qt3DInput::QInputDeviceIntegration::registerBackendType(const
      QMetaObject &metaObject, const Qt3DCore::QBackendNodeMapperPtr
      &functor)': takes a type Python has no way to hand over yet.
    - Qt's 'Qt3DInput::QInputDeviceIntegration::registerBackendType': a
      template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputDeviceIntegration.registerBackendType' has no "
        "cute function yet. Qt's 'void "
        "Qt3DInput::QInputDeviceIntegration::registerBackendType(const "
        "QMetaObject &metaObject, const Qt3DCore::QBackendNodeMapperPtr "
        "&functor)': takes a type Python has no way to hand over yet. Qt's "
        "'Qt3DInput::QInputDeviceIntegration::registerBackendType': a "
        "template: a pattern and no single function.")
