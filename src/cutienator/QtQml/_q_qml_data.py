"""
QQmlData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldata_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractDeclarativeData
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QObjectPrivate
  from . import QQmlEngine, QQmlNotifierEndpoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QObjectPrivate = WAIT['QObjectPrivate']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlNotifierEndpoint = WAIT['QQmlNotifierEndpoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlData(QAbstractDeclarativeData):
  """
  The cute side of Qt's QQmlData: a plain Python object standing in front of
  one C++ QQmlData.

  It is built on the cute 'QAbstractDeclarativeData', as Qt's QQmlData is
  built on Qt's QAbstractDeclarativeData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlData that has a ritual and that Python can call
  so far, 37 names in all: 'init', 'destroyed', 'receivers',
  'isSignalConnected', 'setImplicitDestructible', 'notify', 'addNotify',
  'endpointCount', 'signalHasEndpoint', 'connectEndpoint',
  'disconnectNotifiers', 'hasBindingBit', 'setBindingBit', 'clearBindingBit',
  'hasPendingBindingBit', 'setPendingBindingBit', 'clearPendingBindingBit',
  'releaseDeferredData', 'get', 'keepAliveDuringGarbageCollection',
  'hasExtendedData', 'wasDeleted', 'markAsDeleted', 'setQueuedForDeletion',
  'flushPendingBinding', 'ensurePropertyCache', 'offsetForBit',
  'bitFlagForBit', 'clear', 'createQQmlData', 'createPropertyCache',
  'removeFromContext', 'clearBindings', 'clearSignalHandlers', 'hasBitSet',
  'clearBit', 'setBit'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlData::~QQmlData()': the destructor: Python never removes a C++
    QQmlData.
  - Qt's 'void QQmlData::signalEmitted(QAbstractDeclarativeData *a0, QObject
    *a1, int a2, void **a3)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlData::deferData(int objectIndex, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const
    QQmlRefPointer<QQmlContextData> &a2, const QString
    &inlineComponentName)': takes a type Python has no way to hand over yet.
  - Qt's 'QHash<QQmlAttachedPropertiesFunc, QObject *>
    *QQmlData::attachedProperties() const': gives
    'QHash<QQmlAttachedPropertiesFunc, QObject *>', which has no cute class
    yet.

  What has no ritual
  ------------------

  5 of the 53 functions Qt declares: 4 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QQmlData is created at the first use, not by 'QQmlData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlData.
  - Each name of Qt's QQmlData that has no cute function yet,
    'attachedProperties', 'deferData', 'growBits', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlData, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class DeleteNotifyList(CuteNum, scoped=True):
    """
    The enum 'QQmlData::DeleteNotifyList' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Yes = Kee[int](0)
    No = Kee[int](1)

  class Ownership(CuteNum):
    """
    The enum 'QQmlData::Ownership' of Qt, with the 2 names Qt gives in it.
    """

    DoesNotOwnMemory = Kee[int](0)
    OwnsMemory = Kee[int](1)

  #  The classes Qt writes inside QQmlData, each a class in here as in C++.

  class DeferredData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlData::DeferredData: a plain Python object
    standing in front of one C++ QQmlData::DeferredData.

    What exists
    -----------

    No function of Qt's QQmlData::DeferredData yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlData::DeferredData::~DeferredData()': the destructor: Python
      never removes a C++ QQmlData::DeferredData.

    What has no ritual
    ------------------

    2 of the 4 functions Qt declares: 2 forbidden.

    What to expect
    --------------

    - The C++ QQmlData::DeferredData is created at the first use, not by
      'QQmlData::DeferredData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlData::DeferredData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlData::DeferredData'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlData::DeferredData::DeferredData()', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldata-deferreddata.html#DeferredData
      """
      #  QQmlData::DeferredData::DeferredData()
      self._noteCreation(QQmlData.DeferredData, lambda: Rituals.call(
          'ritual_ZN8QQmlData12DeferredDataC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def init() -> None:
    """
    Calls Qt's 'void QQmlData::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#init
    """
    #  void QQmlData::init()
    Rituals.call('ritual_ZN8QQmlData4initEv')

  @staticmethod
  @overload(QAbstractDeclarativeData, QObject)
  @overload(QAbstractDeclarativeData, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def destroyed(
      a0: Optional[QAbstractDeclarativeData],
      a1: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlData::destroyed(QAbstractDeclarativeData *a0,
    QObject *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#destroyed

    Parameters
    ----------

    a0 : Optional[QAbstractDeclarativeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlData::destroyed(QAbstractDeclarativeData *a0, QObject *a1)
    Rituals.call(
        'ritual_ZN8QQmlData9destroyedEP24QAbstractDeclarativeDataP7QObject',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def destroyed(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlData::destroyed(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#destroyed

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlData::destroyed(QObject *a0)
    self.uglySide.call(
        'ritual_ZN8QQmlData9destroyedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @staticmethod
  @overload(QAbstractDeclarativeData, QObject, int)
  @overload(QAbstractDeclarativeData, NoneType, int)
  @overload(NoneType, QObject, int)
  @overload(NoneType, NoneType, int)
  def receivers(
      a0: Optional[QAbstractDeclarativeData],
      a1: Optional[QObject],
      a2: int,
  ) -> int:
    """
    Calls Qt's 'int QQmlData::receivers(QAbstractDeclarativeData *a0, const
    QObject *a1, int a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#receivers

    Parameters
    ----------

    a0 : Optional[QAbstractDeclarativeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : int
      Passed on as it is.
    """
    #  int QQmlData::receivers(QAbstractDeclarativeData *a0, const QObject
    #      *a1, int a2)
    return Rituals.call(
        'ritual_ZN8QQmlData9receiversEP24QAbstractDeclarativeDataPK7QObject'
        'i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1, 'QObject'), a2,
    )

  @staticmethod
  @overload(QAbstractDeclarativeData, QObject, int)
  @overload(QAbstractDeclarativeData, NoneType, int)
  @overload(NoneType, QObject, int)
  @overload(NoneType, NoneType, int)
  def isSignalConnected(
      a0: Optional[QAbstractDeclarativeData],
      a1: Optional[QObject],
      a2: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlData::isSignalConnected(QAbstractDeclarativeData
    *a0, const QObject *a1, int a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#isSignalConnected

    Parameters
    ----------

    a0 : Optional[QAbstractDeclarativeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : int
      Passed on as it is.
    """
    #  bool QQmlData::isSignalConnected(QAbstractDeclarativeData *a0, const
    #      QObject *a1, int a2)
    return Rituals.call(
        'ritual_ZN8QQmlData17isSignalConnectedEP24QAbstractDeclarativeDataP'
        'K7QObjecti',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1, 'QObject'), a2,
    )

  @staticmethod
  @overload(QQmlNotifierEndpoint, QObject, int, QQmlEngine)
  @overload(QQmlNotifierEndpoint, QObject, int, NoneType)
  @overload(QQmlNotifierEndpoint, NoneType, int, QQmlEngine)
  @overload(QQmlNotifierEndpoint, NoneType, int, NoneType)
  @overload(NoneType, QObject, int, QQmlEngine)
  @overload(NoneType, QObject, int, NoneType)
  @overload(NoneType, NoneType, int, QQmlEngine)
  @overload(NoneType, NoneType, int, NoneType)
  @overload(QQmlNotifierEndpoint, QObject, int, QQmlEngine, bool)
  @overload(QQmlNotifierEndpoint, QObject, int, NoneType, bool)
  @overload(QQmlNotifierEndpoint, NoneType, int, QQmlEngine, bool)
  @overload(QQmlNotifierEndpoint, NoneType, int, NoneType, bool)
  @overload(NoneType, QObject, int, QQmlEngine, bool)
  @overload(NoneType, QObject, int, NoneType, bool)
  @overload(NoneType, NoneType, int, QQmlEngine, bool)
  @overload(NoneType, NoneType, int, NoneType, bool)
  def connectEndpoint(
      endPoint: Optional[QQmlNotifierEndpoint],
      source: Optional[QObject],
      sourceSignal: int,
      engine: Optional[QQmlEngine],
      doNotify: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQmlData::connectEndpoint(QQmlNotifierEndpoint
    *endPoint, QObject *source, int sourceSignal, QQmlEngine *engine, bool
    doNotify)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#connectEndpoint

    Parameters
    ----------

    endPoint : Optional[QQmlNotifierEndpoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceSignal : int
      Passed on as it is.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    doNotify : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlData::connectEndpoint(QQmlNotifierEndpoint *endPoint, QObject
    #      *source, int sourceSignal, QQmlEngine *engine, bool doNotify)
    Rituals.call(
        'ritual_ZN8QQmlData15connectEndpointEP20QQmlNotifierEndpointP7QObje'
        'ctiP10QQmlEngineb',
        CuteMixin._addressOf(endPoint, 'QQmlNotifierEndpoint'),
        CuteMixin._addressOf(source, 'QObject'), sourceSignal,
        CuteMixin._addressOf(engine), doNotify,
    )

  @staticmethod
  @overload(QObjectPrivate, bool)
  @overload(NoneType, bool)
  def get(
      priv: Optional[QObjectPrivate],
      create: bool,
  ) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlData::get(QObjectPrivate *priv, bool create)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#get

    Parameters
    ----------

    priv : Optional[QObjectPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    create : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlData::get(QObjectPrivate *priv, bool create)
    address = Rituals.call(
        'ritual_ZN8QQmlData3getEP14QObjectPrivateb',
        CuteMixin._addressOf(priv, 'QObjectPrivate'), create,
    )
    return QQmlData._cuteAt(address)

  @staticmethod
  @overload(QObjectPrivate)
  @overload(NoneType)
  def get(priv: Optional[QObjectPrivate]) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlData::get(const QObjectPrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#get

    Parameters
    ----------

    priv : Optional[QObjectPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlData::get(const QObjectPrivate *priv)
    address = Rituals.call(
        'ritual_ZN8QQmlData3getEPK14QObjectPrivate',
        CuteMixin._addressOf(priv, 'QObjectPrivate'),
    )
    return QQmlData._cuteAt(address)

  @staticmethod
  @overload(QObject, bool)
  def get(object: Optional[QObject], create: bool) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlData::get(QObject *object, bool create)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#get

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    create : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlData::get(QObject *object, bool create)
    address = Rituals.call(
        'ritual_ZN8QQmlData3getEP7QObjectb',
        CuteMixin._addressOf(object, 'QObject'), create,
    )
    return QQmlData._cuteAt(address)

  @staticmethod
  @overload(QObject)
  def get(object: Optional[QObject]) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlData::get(const QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#get

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlData::get(const QObject *object)
    address = Rituals.call(
        'ritual_ZN8QQmlData3getEPK7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQmlData._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def keepAliveDuringGarbageCollection(object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQmlData::keepAliveDuringGarbageCollection(const QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldata.html#keepAliveDuringGarbageCollection

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlData::keepAliveDuringGarbageCollection(const QObject *object)
    return Rituals.call(
        'ritual_ZN8QQmlData32keepAliveDuringGarbageCollectionEPK7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def wasDeleted(a0: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQmlData::wasDeleted(const QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#wasDeleted

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlData::wasDeleted(const QObject *a0)
    return Rituals.call(
        'ritual_ZN8QQmlData10wasDeletedEPK7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )

  @staticmethod
  @overload(QObjectPrivate)
  def wasDeleted(a0: Optional[QObjectPrivate]) -> bool:
    """
    Calls Qt's 'bool QQmlData::wasDeleted(const QObjectPrivate *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#wasDeleted

    Parameters
    ----------

    a0 : Optional[QObjectPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlData::wasDeleted(const QObjectPrivate *a0)
    return Rituals.call(
        'ritual_ZN8QQmlData10wasDeletedEPK14QObjectPrivate',
        CuteMixin._addressOf(a0, 'QObjectPrivate'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def markAsDeleted(a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlData::markAsDeleted(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#markAsDeleted

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlData::markAsDeleted(QObject *a0)
    Rituals.call(
        'ritual_ZN8QQmlData13markAsDeletedEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def setQueuedForDeletion(a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlData::setQueuedForDeletion(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#setQueuedForDeletion

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlData::setQueuedForDeletion(QObject *a0)
    Rituals.call(
        'ritual_ZN8QQmlData20setQueuedForDeletionEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def flushPendingBinding(object: Optional[QObject], coreIndex: int) -> None:
    """
    Calls Qt's 'void QQmlData::flushPendingBinding(QObject *object, int
    coreIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#flushPendingBinding

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : int
      Passed on as it is.
    """
    #  void QQmlData::flushPendingBinding(QObject *object, int coreIndex)
    Rituals.call(
        'ritual_ZN8QQmlData19flushPendingBindingEP7QObjecti',
        CuteMixin._addressOf(object, 'QObject'), coreIndex,
    )

  @overload(int)
  def flushPendingBinding(self, coreIndex: int) -> None:
    """
    Calls Qt's 'void QQmlData::flushPendingBinding(int coreIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#flushPendingBinding

    Parameters
    ----------

    coreIndex : int
      Passed on as it is.
    """
    #  void QQmlData::flushPendingBinding(int coreIndex)
    self.uglySide.call(
        'ritual_ZN8QQmlData19flushPendingBindingEi', coreIndex,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def ensurePropertyCache(
      object: Optional[QObject],
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlData::ensurePropertyCache(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#ensurePropertyCache

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlData::ensurePropertyCache(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN8QQmlData19ensurePropertyCacheEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(int)
  def offsetForBit(bit: int) -> int:
    """
    Calls Qt's 'uint QQmlData::offsetForBit(int bit)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#offsetForBit

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  uint QQmlData::offsetForBit(int bit)
    return Rituals.call('ritual_ZN8QQmlData12offsetForBitEi', bit)

  @staticmethod
  @overload(int)
  def bitFlagForBit(bit: int) -> int:
    """
    Calls Qt's 'BindingBitsType QQmlData::bitFlagForBit(int bit)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#bitFlagForBit

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  BindingBitsType QQmlData::bitFlagForBit(int bit)
    return Rituals.call('ritual_ZN8QQmlData13bitFlagForBitEi', bit)

  @staticmethod
  @overload(QObjectPrivate)
  @overload(NoneType)
  def createQQmlData(priv: Optional[QObjectPrivate]) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlData::createQQmlData(QObjectPrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#createQQmlData

    Parameters
    ----------

    priv : Optional[QObjectPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlData::createQQmlData(QObjectPrivate *priv)
    address = Rituals.call(
        'ritual_ZN8QQmlData14createQQmlDataEP14QObjectPrivate',
        CuteMixin._addressOf(priv, 'QObjectPrivate'),
    )
    return QQmlData._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def createPropertyCache(
      object: Optional[QObject],
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlData::createPropertyCache(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#createPropertyCache

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlData::createPropertyCache(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN8QQmlData19createPropertyCacheEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def notify(self, index: int) -> Optional[QQmlNotifierEndpoint]:
    """
    Calls Qt's 'QQmlNotifierEndpoint *QQmlData::notify(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#notify

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlNotifierEndpoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlNotifierEndpoint *QQmlData::notify(int index) const
    address = self.uglySide.call('ritual_ZNK8QQmlData6notifyEi', index)
    from . import QQmlNotifierEndpoint
    return QQmlNotifierEndpoint._cuteAt(address)

  @overload(int)
  def signalHasEndpoint(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQmlData::signalHasEndpoint(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#signalHasEndpoint

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlData::signalHasEndpoint(int index) const
    return self.uglySide.call(
        'ritual_ZNK8QQmlData17signalHasEndpointEi', index,
    )

  @overload(int)
  def hasBindingBit(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QQmlData::hasBindingBit(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#hasBindingBit

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QQmlData::hasBindingBit(int a0) const
    return self.uglySide.call('ritual_ZNK8QQmlData13hasBindingBitEi', a0)

  @overload(int)
  def hasPendingBindingBit(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQmlData::hasPendingBindingBit(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#hasPendingBindingBit

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlData::hasPendingBindingBit(int index) const
    return self.uglySide.call(
        'ritual_ZNK8QQmlData20hasPendingBindingBitEi', index,
    )

  def hasExtendedData(self) -> bool:
    """
    Calls Qt's 'bool QQmlData::hasExtendedData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#hasExtendedData
    """
    #  bool QQmlData::hasExtendedData() const
    return self.uglySide.call('ritual_ZNK8QQmlData15hasExtendedDataEv')

  @overload(int)
  def hasBitSet(self, bit: int) -> bool:
    """
    Calls Qt's 'bool QQmlData::hasBitSet(int bit) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#hasBitSet

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  bool QQmlData::hasBitSet(int bit) const
    return self.uglySide.call('ritual_ZNK8QQmlData9hasBitSetEi', bit)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setImplicitDestructible(self) -> None:
    """
    Calls Qt's 'void QQmlData::setImplicitDestructible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldata.html#setImplicitDestructible
    """
    #  void QQmlData::setImplicitDestructible()
    self.uglySide.call('ritual_ZN8QQmlData23setImplicitDestructibleEv')

  @overload(QObject, int)
  @overload(NoneType, int)
  def setBindingBit(self, obj: Optional[QObject], a1: int) -> None:
    """
    Calls Qt's 'void QQmlData::setBindingBit(QObject *obj, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#setBindingBit

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlData::setBindingBit(QObject *obj, int a1)
    self.uglySide.call(
        'ritual_ZN8QQmlData13setBindingBitEP7QObjecti',
        self._addressOf(obj, 'QObject'), a1,
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def setPendingBindingBit(self, obj: Optional[QObject], a1: int) -> None:
    """
    Calls Qt's 'void QQmlData::setPendingBindingBit(QObject *obj, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#setPendingBindingBit

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlData::setPendingBindingBit(QObject *obj, int a1)
    self.uglySide.call(
        'ritual_ZN8QQmlData20setPendingBindingBitEP7QObjecti',
        self._addressOf(obj, 'QObject'), a1,
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def setBit(self, obj: Optional[QObject], bit: int) -> None:
    """
    Calls Qt's 'void QQmlData::setBit(QObject *obj, int bit)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#setBit

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bit : int
      Passed on as it is.
    """
    #  void QQmlData::setBit(QObject *obj, int bit)
    self.uglySide.call(
        'ritual_ZN8QQmlData6setBitEP7QObjecti',
        self._addressOf(obj, 'QObject'), bit,
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

  @overload(Ownership)
  def __init__(self, ownership: Ownership) -> None:
    """
    Notes what was given, for Qt's 'QQmlData::QQmlData(Ownership ownership)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#QQmlData

    Parameters
    ----------

    ownership : Ownership
      Passed on as its number.
    """
    #  QQmlData::QQmlData(Ownership ownership)
    self._noteCreation(QQmlData, lambda: Rituals.call(
        'ritual_ZN8QQmlDataC1ENS_9OwnershipE', ownership.value,
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

  @overload(int, QQmlNotifierEndpoint)
  @overload(int, NoneType)
  def addNotify(
      self,
      index: int,
      a1: Optional[QQmlNotifierEndpoint],
  ) -> None:
    """
    Calls Qt's 'void QQmlData::addNotify(int index, QQmlNotifierEndpoint
    *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#addNotify

    Parameters
    ----------

    index : int
      Passed on as it is.

    a1 : Optional[QQmlNotifierEndpoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlData::addNotify(int index, QQmlNotifierEndpoint *a1)
    self.uglySide.call(
        'ritual_ZN8QQmlData9addNotifyEiP20QQmlNotifierEndpoint',
        index, self._addressOf(a1, 'QQmlNotifierEndpoint'),
    )

  @overload(int)
  def endpointCount(self, index: int) -> int:
    """
    Calls Qt's 'int QQmlData::endpointCount(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#endpointCount

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QQmlData::endpointCount(int index)
    return self.uglySide.call('ritual_ZN8QQmlData13endpointCountEi', index)

  @overload(DeleteNotifyList)
  def disconnectNotifiers(self, doDelete: DeleteNotifyList) -> None:
    """
    Calls Qt's 'void QQmlData::disconnectNotifiers(DeleteNotifyList
    doDelete)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#disconnectNotifiers

    Parameters
    ----------

    doDelete : DeleteNotifyList
      Passed on as its number.
    """
    #  void QQmlData::disconnectNotifiers(DeleteNotifyList doDelete)
    self.uglySide.call(
        'ritual_ZN8QQmlData19disconnectNotifiersENS_16DeleteNotifyListE',
        doDelete.value,
    )

  @overload(int)
  def clearBindingBit(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlData::clearBindingBit(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#clearBindingBit

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlData::clearBindingBit(int a0)
    self.uglySide.call('ritual_ZN8QQmlData15clearBindingBitEi', a0)

  @overload(int)
  def clearPendingBindingBit(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlData::clearPendingBindingBit(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldata.html#clearPendingBindingBit

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlData::clearPendingBindingBit(int a0)
    self.uglySide.call('ritual_ZN8QQmlData22clearPendingBindingBitEi', a0)

  def releaseDeferredData(self) -> None:
    """
    Calls Qt's 'void QQmlData::releaseDeferredData()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#releaseDeferredData
    """
    #  void QQmlData::releaseDeferredData()
    self.uglySide.call('ritual_ZN8QQmlData19releaseDeferredDataEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#clear
    """
    #  void QQmlData::clear()
    self.uglySide.call('ritual_ZN8QQmlData5clearEv')

  def removeFromContext(self) -> None:
    """
    Calls Qt's 'void QQmlData::removeFromContext()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#removeFromContext
    """
    #  void QQmlData::removeFromContext()
    self.uglySide.call('ritual_ZN8QQmlData17removeFromContextEv')

  def clearBindings(self) -> None:
    """
    Calls Qt's 'void QQmlData::clearBindings()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#clearBindings
    """
    #  void QQmlData::clearBindings()
    self.uglySide.call('ritual_ZN8QQmlData13clearBindingsEv')

  def clearSignalHandlers(self) -> bool:
    """
    Calls Qt's 'bool QQmlData::clearSignalHandlers()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#clearSignalHandlers
    """
    #  bool QQmlData::clearSignalHandlers()
    return self.uglySide.call('ritual_ZN8QQmlData19clearSignalHandlersEv')

  @overload(int)
  def clearBit(self, bit: int) -> None:
    """
    Calls Qt's 'void QQmlData::clearBit(int bit)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldata.html#clearBit

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  void QQmlData::clearBit(int bit)
    self.uglySide.call('ritual_ZN8QQmlData8clearBitEi', bit)

  @staticmethod
  def attachedProperties(*__, **_) -> Never:
    """
    Qt's 'QHash<QQmlAttachedPropertiesFunc, QObject *>
    *QQmlData::attachedProperties() const': gives
    'QHash<QQmlAttachedPropertiesFunc, QObject *>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlData.attachedProperties' has no cute function yet. Qt's "
        "'QHash<QQmlAttachedPropertiesFunc, QObject *> "
        "*QQmlData::attachedProperties() const': gives "
        "'QHash<QQmlAttachedPropertiesFunc, QObject *>', which has no cute "
        "class yet.")

  @staticmethod
  def deferData(*__, **_) -> Never:
    """
    Qt's 'void QQmlData::deferData(int objectIndex, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const
    QQmlRefPointer<QQmlContextData> &a2, const QString
    &inlineComponentName)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlData.deferData' has no cute function yet. Qt's 'void "
        "QQmlData::deferData(int objectIndex, const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const "
        "QQmlRefPointer<QQmlContextData> &a2, const QString "
        "&inlineComponentName)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def growBits(*__, **_) -> Never:
    """
    Qt's 'BindingBitsType *QQmlData::growBits(QObject *obj, int bit)': takes
    or gives a type that cannot be passed yet: QQmlData::BindingBitsType *.
    """
    raise NotImplementedError(
        "'QQmlData.growBits' has no cute function yet. Qt's "
        "'BindingBitsType *QQmlData::growBits(QObject *obj, int bit)': "
        "takes or gives a type that cannot be passed yet: "
        "QQmlData::BindingBitsType *.")
