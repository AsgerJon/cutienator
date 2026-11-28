"""
QRemoteObjectRegistry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectregistry.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject
from . import QRemoteObjectReplica

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QRemoteObjectNode, QRemoteObjectSourceLocationInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectNode = WAIT['QRemoteObjectNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectRegistry(QRemoteObjectReplica):
  """
  The cute side of Qt's QRemoteObjectRegistry: a plain Python object standing
  in front of one C++ QRemoteObjectRegistry.

  It is built on the cute 'QRemoteObjectReplica', as Qt's
  QRemoteObjectRegistry is built on Qt's QRemoteObjectReplica, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectRegistry that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr',
  'registerMetatypes', 'sourceLocations', 'pushToRegistryIfNeeded',
  'initialize', 'notifySourceLocationsChanged'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectRegistry::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QRemoteObjectRegistry::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectRegistry::~QRemoteObjectRegistry()': the destructor:
    Python never removes a C++ QRemoteObjectRegistry.
  - Qt's 'QBindable<QRemoteObjectSourceLocations>
    QRemoteObjectRegistry::bindableSourceLocations() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QRemoteObjectRegistry::remoteObjectAdded(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRemoteObjectRegistry::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRemoteObjectRegistry::addSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRemoteObjectRegistry::removeSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QRemoteObjectRegistryPrivate *QRemoteObjectRegistry::d_func()':
    gives 'QRemoteObjectRegistryPrivate', which has no cute class yet.
  - Qt's 'const QRemoteObjectRegistryPrivate *QRemoteObjectRegistry::d_func()
    const': gives 'QRemoteObjectRegistryPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectRegistry is created at the first use, not by
    'QRemoteObjectRegistry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectRegistry.
  - Qt tells when it has removed the C++ QRemoteObjectRegistry. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectRegistry that has no cute function yet,
    'addSource', 'bindableSourceLocations', 'remoteObjectAdded',
    'remoteObjectRemoved', 'removeSource', holds a function that raises
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
    Calls Qt's 'QString QRemoteObjectRegistry::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectregistry.html#tr

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
    #  QString QRemoteObjectRegistry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QRemoteObjectRegistry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def registerMetatypes() -> None:
    """
    Calls Qt's 'void QRemoteObjectRegistry::registerMetatypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#registerMetatypes
    """
    #  void QRemoteObjectRegistry::registerMetatypes()
    Rituals.call('ritual_ZN21QRemoteObjectRegistry17registerMetatypesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectRegistry'

  #  A C++ QRemoteObjectRegistry Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectRegistry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectRegistry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectRegistry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QRemoteObjectRegistry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceLocations(self) -> QHash[str, QRemoteObjectSourceLocationInfo]:
    """
    Calls Qt's 'QRemoteObjectSourceLocations
    QRemoteObjectRegistry::sourceLocations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#sourceLocations

    Returns
    -------

    QHash[str, QRemoteObjectSourceLocationInfo]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QRemoteObjectSourceLocations QRemoteObjectRegistry::sourceLocations()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QRemoteObjectRegistry15sourceLocationsEv',
    )
    from . import QRemoteObjectSourceLocationInfo
    return QHash[str, QRemoteObjectSourceLocationInfo]._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QRemoteObjectRegistry::QRemoteObjectRegistry(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#QRemoteObjectRegistry

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectRegistry::QRemoteObjectRegistry(QObject *parent)
    self._noteCreation(QRemoteObjectRegistry, lambda: Rituals.call(
        'ritual_ZN21QRemoteObjectRegistryC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QRemoteObjectNode, str)
  @overload(NoneType, str)
  @overload(QRemoteObjectNode, str, QObject)
  @overload(QRemoteObjectNode, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      node: Optional[QRemoteObjectNode],
      name: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectRegistry::QRemoteObjectRegistry(QRemoteObjectNode *node,
    const QString &name, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#QRemoteObjectRegistry

    Parameters
    ----------

    node : Optional[QRemoteObjectNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectRegistry::QRemoteObjectRegistry(QRemoteObjectNode *node,
    #      const QString &name, QObject *parent)
    self._noteCreation(QRemoteObjectRegistry, lambda: Rituals.call(
        'ritual_ZN21QRemoteObjectRegistryC1EP17QRemoteObjectNodeRK7QStringP'
        '7QObject',
        self._addressOf(node), name, self._addressOf(parent, 'QObject'),
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

  def pushToRegistryIfNeeded(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectRegistry::pushToRegistryIfNeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#pushToRegistryIfNeeded
    """
    #  void QRemoteObjectRegistry::pushToRegistryIfNeeded()
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectRegistry22pushToRegistryIfNeededEv',
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectRegistry::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html#initialize
    """
    #  void QRemoteObjectRegistry::initialize()
    ritual = 'ritual_ZN21QRemoteObjectRegistry10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRemoteObjectRegistry10initializeEv'
    self.uglySide.call(ritual)

  def notifySourceLocationsChanged(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectRegistry::notifySourceLocationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistry.html
    """
    #  void QRemoteObjectRegistry::notifySourceLocationsChanged()
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectRegistry28notifySourceLocationsChangedEv',
    )

  @staticmethod
  def addSource(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectRegistry::addSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistry.addSource' has no cute function yet. Qt's "
        "'void QRemoteObjectRegistry::addSource(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def bindableSourceLocations(*__, **_) -> Never:
    """
    Qt's 'QBindable<QRemoteObjectSourceLocations>
    QRemoteObjectRegistry::bindableSourceLocations() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistry.bindableSourceLocations' has no cute "
        "function yet. Qt's 'QBindable<QRemoteObjectSourceLocations> "
        "QRemoteObjectRegistry::bindableSourceLocations() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def remoteObjectAdded(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectRegistry::remoteObjectAdded(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistry.remoteObjectAdded' has no cute function "
        "yet. Qt's 'void QRemoteObjectRegistry::remoteObjectAdded(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def remoteObjectRemoved(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectRegistry::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistry.remoteObjectRemoved' has no cute function "
        "yet. Qt's 'void QRemoteObjectRegistry::remoteObjectRemoved(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def removeSource(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectRegistry::removeSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistry.removeSource' has no cute function yet. "
        "Qt's 'void QRemoteObjectRegistry::removeSource(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")
