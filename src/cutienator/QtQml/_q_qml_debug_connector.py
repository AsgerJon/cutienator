"""
QQmlDebugConnector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugconnector_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlDebugConnector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QJSEngine, QQmlDebugService
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSEngine = WAIT['QJSEngine']
  QQmlDebugService = WAIT['QQmlDebugService']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDebugConnector(QObject):
  """
  The cute side of Qt's QQmlDebugConnector: a plain Python object standing in
  front of one C++ QQmlDebugConnector.

  It is built on the cute 'QObject', as Qt's QQmlDebugConnector is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDebugConnector that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'setPluginKey',
  'setServices', 'instance', 'dataStreamVersion', 'blockingMode', 'service',
  'addEngine', 'removeEngine', 'hasEngine', 'addService', 'removeService',
  'open', 'commandLineArguments'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDebugConnector::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlDebugConnector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QQmlDebugConnector is created at the first use, not by
    'QQmlDebugConnector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDebugConnector.
  - Qt tells when it has removed the C++ QQmlDebugConnector. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlDebugConnector::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#tr

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
    #  QString QQmlDebugConnector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQmlDebugConnector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def setPluginKey(key: str) -> None:
    """
    Calls Qt's 'void QQmlDebugConnector::setPluginKey(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#setPluginKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDebugConnector::setPluginKey(const QString &key)
    Rituals.call(
        'ritual_ZN18QQmlDebugConnector12setPluginKeyERK7QString', key,
    )

  @staticmethod
  @overload(QStringList)
  def setServices(services: QStringList) -> None:
    """
    Calls Qt's 'void QQmlDebugConnector::setServices(const QStringList
    &services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#setServices

    Parameters
    ----------

    services : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlDebugConnector::setServices(const QStringList &services)
    Rituals.call(
        'ritual_ZN18QQmlDebugConnector11setServicesERK5QListI7QStringE',
        CuteMixin._valueOf(services),
    )

  @staticmethod
  def instance() -> Optional[QQmlDebugConnector]:
    """
    Calls Qt's 'QQmlDebugConnector *QQmlDebugConnector::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#instance

    Returns
    -------

    Optional[QQmlDebugConnector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDebugConnector *QQmlDebugConnector::instance()
    address = Rituals.call('ritual_ZN18QQmlDebugConnector8instanceEv')
    return QQmlDebugConnector._cuteAt(address)

  @staticmethod
  def dataStreamVersion() -> int:
    """
    Calls Qt's 'int QQmlDebugConnector::dataStreamVersion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#dataStreamVersion
    """
    #  int QQmlDebugConnector::dataStreamVersion()
    return Rituals.call('ritual_ZN18QQmlDebugConnector17dataStreamVersionEv')

  @staticmethod
  def commandLineArguments() -> str:
    """
    Calls Qt's 'QString QQmlDebugConnector::commandLineArguments()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#commandLineArguments

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDebugConnector::commandLineArguments()
    return Rituals.call(
        'ritual_ZN18QQmlDebugConnector20commandLineArgumentsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebugConnector'

  #  A C++ QQmlDebugConnector Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDebugConnector'

  #  The functions Qt calls itself that QQmlDebugConnector is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'open': (
          'bool QQmlDebugConnector::open(const QVariantHash &)',
      ),
  }

  #  The functions Qt calls itself that QQmlDebugConnector is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'blockingMode': (
          ('_ZNK18QQmlDebugConnector12blockingModeEv',
           ('bool', 'number', ''),
           ()),
      ),
      'service': (
          ('_ZNK18QQmlDebugConnector7serviceERK7QString',
           ('address', 'address', 'QtQml:QQmlDebugService'),
           (
               ('address', 'text', ''),
           )),
      ),
      'addEngine': (
          ('_ZN18QQmlDebugConnector9addEngineEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'removeEngine': (
          ('_ZN18QQmlDebugConnector12removeEngineEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'hasEngine': (
          ('_ZNK18QQmlDebugConnector9hasEngineEP9QJSEngine',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'addService': (
          ('_ZN18QQmlDebugConnector10addServiceERK7QStringP16QQmlDebugServi'
           'ce',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtQml:QQmlDebugService'),
           )),
      ),
      'removeService': (
          ('_ZN18QQmlDebugConnector13removeServiceERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDebugConnector::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDebugConnector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlDebugConnector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def blockingMode(self) -> bool:
    """
    Calls Qt's 'bool QQmlDebugConnector::blockingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#blockingMode
    """
    #  bool QQmlDebugConnector::blockingMode() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlDebugConnector12blockingModeEv',
    )

  @overload(str)
  def service(self, name: str) -> Optional[QQmlDebugService]:
    """
    Calls Qt's 'QQmlDebugService *QQmlDebugConnector::service(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#service

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQmlDebugService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDebugService *QQmlDebugConnector::service(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlDebugConnector7serviceERK7QString', name,
    )
    from . import QQmlDebugService
    return QQmlDebugService._cuteAt(address)

  @overload(QJSEngine)
  @overload(NoneType)
  def hasEngine(self, engine: Optional[QJSEngine]) -> bool:
    """
    Calls Qt's 'bool QQmlDebugConnector::hasEngine(QJSEngine *engine) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#hasEngine

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlDebugConnector::hasEngine(QJSEngine *engine) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlDebugConnector9hasEngineEP9QJSEngine',
        self._addressOf(engine),
    )

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

  @overload(QJSEngine)
  @overload(NoneType)
  def addEngine(self, engine: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugConnector::addEngine(QJSEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#addEngine

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugConnector::addEngine(QJSEngine *engine)
    self.uglySide.call(
        'ritual_ZN18QQmlDebugConnector9addEngineEP9QJSEngine',
        self._addressOf(engine),
    )

  @overload(QJSEngine)
  @overload(NoneType)
  def removeEngine(self, engine: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugConnector::removeEngine(QJSEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#removeEngine

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugConnector::removeEngine(QJSEngine *engine)
    self.uglySide.call(
        'ritual_ZN18QQmlDebugConnector12removeEngineEP9QJSEngine',
        self._addressOf(engine),
    )

  @overload(str, QQmlDebugService)
  @overload(str, NoneType)
  def addService(
      self,
      name: str,
      service: Optional[QQmlDebugService],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDebugConnector::addService(const QString &name,
    QQmlDebugService *service)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#addService

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    service : Optional[QQmlDebugService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlDebugConnector::addService(const QString &name,
    #      QQmlDebugService *service)
    return self.uglySide.call(
        'ritual_ZN18QQmlDebugConnector10addServiceERK7QStringP16QQmlDebugSe'
        'rvice',
        name, self._addressOf(service),
    )

  @overload(str)
  def removeService(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlDebugConnector::removeService(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugconnector.html#removeService

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlDebugConnector::removeService(const QString &name)
    return self.uglySide.call(
        'ritual_ZN18QQmlDebugConnector13removeServiceERK7QString', name,
    )

  @overload(QHash[str, QVariant])
  def open(self, configuration: QHash[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool QQmlDebugConnector::open(const QVariantHash
    &configuration)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugconnector.html#open

    Parameters
    ----------

    configuration : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QQmlDebugConnector::open(const QVariantHash &configuration)
    return self.uglySide.call(
        'ritual_ZN18QQmlDebugConnector4openERK5QHashI7QString8QVariantE',
        self._valueOf(configuration),
    )
