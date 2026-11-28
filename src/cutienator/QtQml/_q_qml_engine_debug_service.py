"""
QQmlEngineDebugService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlEngineDebugService to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlDebugService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QJSEngine, QQmlBoundSignal, QQmlDebugStatesDelegate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSEngine = WAIT['QJSEngine']
  QQmlBoundSignal = WAIT['QQmlBoundSignal']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEngineDebugService(QQmlDebugService):
  """
  The cute side of Qt's QQmlEngineDebugService: a plain Python object
  standing in front of one C++ QQmlEngineDebugService.

  It is built on the cute 'QQmlDebugService', as Qt's QQmlEngineDebugService
  is built on Qt's QQmlDebugService, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlEngineDebugService that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'objectCreated', 'createStatesDelegate', 'nextSignal'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlEngineDebugService::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlEngineDebugService::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlEngineDebugService::~QQmlEngineDebugService()': the destructor:
    Python never removes a C++ QQmlEngineDebugService.
  - Qt's 'void
    QQmlEngineDebugService::setStatesDelegateFactory(QQmlDebugStatesDelegate
    *(*)() factory)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlEngineDebugService is created at the first use, not by
    'QQmlEngineDebugService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlEngineDebugService.
  - Qt tells when it has removed the C++ QQmlEngineDebugService. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlEngineDebugService that has no cute function yet,
    'setStatesDelegateFactory', holds a function that raises
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
    Calls Qt's 'QString QQmlEngineDebugService::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlenginedebugservice.html#tr

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
    #  QString QQmlEngineDebugService::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQmlEngineDebugService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def createStatesDelegate() -> Optional[QQmlDebugStatesDelegate]:
    """
    Calls Qt's 'QQmlDebugStatesDelegate
    *QQmlEngineDebugService::createStatesDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenginedebugservice.html#createStatesDelegate

    Returns
    -------

    Optional[QQmlDebugStatesDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDebugStatesDelegate
    #      *QQmlEngineDebugService::createStatesDelegate()
    address = Rituals.call(
        'ritual_ZN22QQmlEngineDebugService20createStatesDelegateEv',
    )
    from . import QQmlDebugStatesDelegate
    return QQmlDebugStatesDelegate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEngineDebugService'

  #  A C++ QQmlEngineDebugService Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlEngineDebugService'

  #  The functions Qt calls itself that QQmlEngineDebugService is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'objectCreated': (
          ('_ZN22QQmlEngineDebugService13objectCreatedEP9QJSEngineP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QJSEngine'),
               ('address', 'address', 'QtCore:QObject'),
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
    Calls Qt's 'const QMetaObject *QQmlEngineDebugService::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenginedebugservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlEngineDebugService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlEngineDebugService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(float)
  @overload(float, QObject)
  @overload(float, NoneType)
  def __init__(
      self,
      version: float,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlEngineDebugService::QQmlEngineDebugService(float version, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenginedebugservice.html#QQmlEngineDebugService

    Parameters
    ----------

    version : float
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlEngineDebugService::QQmlEngineDebugService(float version, QObject
    #      *parent)
    self._noteCreation(QQmlEngineDebugService, lambda: Rituals.call(
        'ritual_ZN22QQmlEngineDebugServiceC1EfP7QObject',
        version, self._addressOf(parent, 'QObject'),
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

  @overload(QJSEngine, QObject)
  @overload(QJSEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def objectCreated(
      self,
      engine: Optional[QJSEngine],
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngineDebugService::objectCreated(QJSEngine *engine,
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenginedebugservice.html#objectCreated

    Parameters
    ----------

    engine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngineDebugService::objectCreated(QJSEngine *engine, QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN22QQmlEngineDebugService13objectCreatedEP9QJSEngineP7QObj'
        'ect',
        self._addressOf(engine), self._addressOf(object, 'QObject'),
    )

  @overload(QQmlBoundSignal)
  @overload(NoneType)
  def nextSignal(
      self,
      prev: Optional[QQmlBoundSignal],
  ) -> Optional[QQmlBoundSignal]:
    """
    Calls Qt's 'QQmlBoundSignal
    *QQmlEngineDebugService::nextSignal(QQmlBoundSignal *prev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenginedebugservice.html#nextSignal

    Parameters
    ----------

    prev : Optional[QQmlBoundSignal]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlBoundSignal]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBoundSignal *QQmlEngineDebugService::nextSignal(QQmlBoundSignal
    #      *prev)
    address = self.uglySide.call(
        'ritual_ZN22QQmlEngineDebugService10nextSignalEP15QQmlBoundSignal',
        self._addressOf(prev),
    )
    from . import QQmlBoundSignal
    return QQmlBoundSignal._cuteAt(address)

  @staticmethod
  def setStatesDelegateFactory(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlEngineDebugService::setStatesDelegateFactory(QQmlDebugStatesDelegate
    *(*)() factory)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEngineDebugService.setStatesDelegateFactory' has no cute "
        "function yet. Qt's 'void "
        "QQmlEngineDebugService::setStatesDelegateFactory(QQmlDebugStatesDel"
        "egate *(*)() factory)': takes a type Python has no way to hand "
        "over yet.")
