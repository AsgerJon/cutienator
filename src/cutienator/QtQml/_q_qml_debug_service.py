"""
QQmlDebugService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugservice_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlDebugService to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QJSEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QJSEngine = WAIT['QJSEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDebugService(QObject):
  """
  The cute side of Qt's QQmlDebugService: a plain Python object standing in
  front of one C++ QQmlDebugService.

  It is built on the cute 'QObject', as Qt's QQmlDebugService is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDebugService that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'name', 'version',
  'state', 'setState', 'stateAboutToBeChanged', 'stateChanged',
  'messageReceived', 'engineAboutToBeAdded', 'engineAboutToBeRemoved',
  'engineAdded', 'engineRemoved', 'objectsForIds', 'idForObject',
  'objectForId', 'attachedToEngine', 'detachedFromEngine', 'messageToClient',
  'messagesToClient'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDebugService::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlDebugService::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDebugServicePrivate *QQmlDebugService::d_func()': gives
    'QQmlDebugServicePrivate', which has no cute class yet.
  - Qt's 'const QQmlDebugServicePrivate *QQmlDebugService::d_func() const':
    gives 'QQmlDebugServicePrivate', which has no cute class yet.
  - Qt's 'QQmlDebugService::~QQmlDebugService()': the destructor: Python
    never removes a C++ QQmlDebugService.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlDebugService is created at the first use, not by
    'QQmlDebugService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDebugService.
  - Qt tells when it has removed the C++ QQmlDebugService. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlDebugService, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QQmlDebugService::State' of Qt, with the 3 names Qt gives in
    it.
    """

    NotConnected = Kee[int](0)
    Unavailable = Kee[int](1)
    Enabled = Kee[int](2)

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
    Calls Qt's 'QString QQmlDebugService::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#tr

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
    #  QString QQmlDebugService::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlDebugService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def objectsForIds() -> QHash[int, QObject]:
    """
    Calls Qt's 'const QHash<int, QObject *>
    &QQmlDebugService::objectsForIds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#objectsForIds

    Returns
    -------

    QHash[int, QObject]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  const QHash<int, QObject *> &QQmlDebugService::objectsForIds()
    address = Rituals.call('ritual_ZN16QQmlDebugService13objectsForIdsEv')
    return QHash[int, QObject]._cuteOwning(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def idForObject(a0: Optional[QObject]) -> int:
    """
    Calls Qt's 'int QQmlDebugService::idForObject(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#idForObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlDebugService::idForObject(QObject *a0)
    return Rituals.call(
        'ritual_ZN16QQmlDebugService11idForObjectEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )

  @staticmethod
  @overload(int)
  def objectForId(id: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDebugService::objectForId(int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#objectForId

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDebugService::objectForId(int id)
    address = Rituals.call('ritual_ZN16QQmlDebugService11objectForIdEi', id)
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebugService'

  #  A C++ QQmlDebugService Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDebugService'

  #  The functions Qt calls itself that QQmlDebugService is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'stateAboutToBeChanged': (
          ('_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QQmlDebugService.State'),
           )),
      ),
      'stateChanged': (
          ('_ZN16QQmlDebugService12stateChangedENS_5StateE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QQmlDebugService.State'),
           )),
      ),
      'messageReceived': (
          ('_ZN16QQmlDebugService15messageReceivedERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'engineAboutToBeAdded': (
          ('_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'engineAboutToBeRemoved': (
          ('_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'engineAdded': (
          ('_ZN16QQmlDebugService11engineAddedEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
           )),
      ),
      'engineRemoved': (
          ('_ZN16QQmlDebugService13engineRemovedEP9QJSEngine',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
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
    Calls Qt's 'const QMetaObject *QQmlDebugService::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDebugService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlDebugService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'const QString &QQmlDebugService::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QQmlDebugService::name() const
    return self.uglySide.call('ritual_ZNK16QQmlDebugService4nameEv')

  def version(self) -> float:
    """
    Calls Qt's 'float QQmlDebugService::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#version
    """
    #  float QQmlDebugService::version() const
    return self.uglySide.call('ritual_ZNK16QQmlDebugService7versionEv')

  def state(self) -> State:
    """
    Calls Qt's 'State QQmlDebugService::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QQmlDebugService::state() const
    return QQmlDebugService.State(self.uglySide.call(
        'ritual_ZNK16QQmlDebugService5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(State)
  def setState(self, newState: State) -> None:
    """
    Calls Qt's 'void QQmlDebugService::setState(State newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#setState

    Parameters
    ----------

    newState : State
      Passed on as its number.
    """
    #  void QQmlDebugService::setState(State newState)
    self.uglySide.call(
        'ritual_ZN16QQmlDebugService8setStateENS_5StateE', newState.value,
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

  @overload(str, float)
  @overload(str, float, QObject)
  @overload(str, float, NoneType)
  def __init__(
      self,
      a0: str,
      version: float,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlDebugService::QQmlDebugService(const
    QString &a0, float version, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#QQmlDebugService

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    version : float
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlDebugService::QQmlDebugService(const QString &a0, float version,
    #      QObject *parent)
    self._noteCreation(QQmlDebugService, lambda: Rituals.call(
        'ritual_ZN16QQmlDebugServiceC1ERK7QStringfP7QObject',
        a0, version, self._addressOf(parent, 'QObject'),
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

  @overload(State)
  def stateAboutToBeChanged(self, a0: State) -> None:
    """
    Calls Qt's 'void QQmlDebugService::stateAboutToBeChanged(State a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#stateAboutToBeChanged

    Parameters
    ----------

    a0 : State
      Passed on as its number.
    """
    #  void QQmlDebugService::stateAboutToBeChanged(State a0)
    ritual = 'ritual_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQmlDebugService21stateAboutToBeChangedENS_5State'
          'E')
    self.uglySide.call(ritual, a0.value)

  @overload(State)
  def stateChanged(self, a0: State) -> None:
    """
    Calls Qt's 'void QQmlDebugService::stateChanged(State a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#stateChanged

    Parameters
    ----------

    a0 : State
      Passed on as its number.
    """
    #  void QQmlDebugService::stateChanged(State a0)
    ritual = 'ritual_ZN16QQmlDebugService12stateChangedENS_5StateE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlDebugService12stateChangedENS_5StateE'
    self.uglySide.call(ritual, a0.value)

  @overload(QByteArray)
  def messageReceived(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlDebugService::messageReceived(const QByteArray
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#messageReceived

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlDebugService::messageReceived(const QByteArray &a0)
    ritual = 'ritual_ZN16QQmlDebugService15messageReceivedERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQmlDebugService15messageReceivedERK10QByteArray')
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QJSEngine)
  @overload(NoneType)
  def engineAboutToBeAdded(self, engine: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::engineAboutToBeAdded(QJSEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#engineAboutToBeAdded

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
    ritual = 'ritual_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngin'
          'e')
    self.uglySide.call(ritual, self._addressOf(engine))

  @overload(QJSEngine)
  @overload(NoneType)
  def engineAboutToBeRemoved(self, engine: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::engineAboutToBeRemoved(QJSEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#engineAboutToBeRemoved

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
    ritual = (
        'ritual_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEng'
          'ine')
    self.uglySide.call(ritual, self._addressOf(engine))

  @overload(QJSEngine)
  @overload(NoneType)
  def engineAdded(self, a0: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::engineAdded(QJSEngine *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugservice.html#engineAdded

    Parameters
    ----------

    a0 : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::engineAdded(QJSEngine *a0)
    ritual = 'ritual_ZN16QQmlDebugService11engineAddedEP9QJSEngine'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlDebugService11engineAddedEP9QJSEngine'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QJSEngine)
  @overload(NoneType)
  def engineRemoved(self, a0: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::engineRemoved(QJSEngine *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#engineRemoved

    Parameters
    ----------

    a0 : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::engineRemoved(QJSEngine *a0)
    ritual = 'ritual_ZN16QQmlDebugService13engineRemovedEP9QJSEngine'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlDebugService13engineRemovedEP9QJSEngine'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QJSEngine)
  @overload(NoneType)
  def attachedToEngine(self, a0: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::attachedToEngine(QJSEngine *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#attachedToEngine

    Parameters
    ----------

    a0 : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::attachedToEngine(QJSEngine *a0)
    self.uglySide.call(
        'ritual_ZN16QQmlDebugService16attachedToEngineEP9QJSEngine',
        self._addressOf(a0),
    )

  @overload(QJSEngine)
  @overload(NoneType)
  def detachedFromEngine(self, a0: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::detachedFromEngine(QJSEngine *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#detachedFromEngine

    Parameters
    ----------

    a0 : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugService::detachedFromEngine(QJSEngine *a0)
    self.uglySide.call(
        'ritual_ZN16QQmlDebugService18detachedFromEngineEP9QJSEngine',
        self._addressOf(a0),
    )

  @overload(str, QByteArray)
  def messageToClient(self, name: str, message: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlDebugService::messageToClient(const QString &name,
    const QByteArray &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#messageToClient

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlDebugService::messageToClient(const QString &name, const
    #      QByteArray &message)
    self.uglySide.call(
        'ritual_ZN16QQmlDebugService15messageToClientERK7QStringRK10QByteAr'
        'ray',
        name, self._valueOf(message),
    )

  @overload(str, QList[QByteArray])
  def messagesToClient(self, name: str, messages: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlDebugService::messagesToClient(const QString &name,
    const QList<QByteArray> &messages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugservice.html#messagesToClient

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    messages : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlDebugService::messagesToClient(const QString &name, const
    #      QList<QByteArray> &messages)
    self.uglySide.call(
        'ritual_ZN16QQmlDebugService16messagesToClientERK7QStringRK5QListI1'
        '0QByteArrayE',
        name, self._valueOf(messages),
    )
