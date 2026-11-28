"""
QScxmlScxmlService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlScxmlService to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QScxmlInvokableService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QScxmlEvent, QScxmlInvokableServiceFactory
  from . import QScxmlInvokableServicePrivate, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlEvent = WAIT['QScxmlEvent']
  QScxmlInvokableServiceFactory = WAIT['QScxmlInvokableServiceFactory']
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlScxmlService(QScxmlInvokableService):
  """
  The cute side of Qt's QScxmlScxmlService: a plain Python object standing in
  front of one C++ QScxmlScxmlService.

  It is built on the cute 'QScxmlInvokableService', as Qt's
  QScxmlScxmlService is built on Qt's QScxmlInvokableService, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlScxmlService that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'd_func', 'start',
  'id', 'name', 'postEvent', 'stateMachine'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlScxmlService::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScxmlScxmlService::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScxmlInvokableServicePrivate *QScxmlScxmlService::d_func()
    const': takes in Python what 'QScxmlInvokableServicePrivate
    *QScxmlScxmlService::d_func()' takes.
  - Qt's 'QScxmlScxmlService::~QScxmlScxmlService()': the destructor: Python
    never removes a C++ QScxmlScxmlService.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlScxmlService is created at the first use, not by
    'QScxmlScxmlService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlScxmlService.
  - Qt tells when it has removed the C++ QScxmlScxmlService. Every call on
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
    Calls Qt's 'QString QScxmlScxmlService::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#tr

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
    #  QString QScxmlScxmlService::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QScxmlScxmlService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlScxmlService'

  #  A C++ QScxmlScxmlService Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlScxmlService'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlScxmlService::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlScxmlService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlScxmlService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def id(self) -> str:
    """
    Calls Qt's 'QString QScxmlScxmlService::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlScxmlService::id() const
    ritual = 'ritual_ZNK18QScxmlScxmlService2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QScxmlScxmlService2idEv'
    return self.uglySide.call(ritual)

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlScxmlService::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlScxmlService::name() const
    ritual = 'ritual_ZNK18QScxmlScxmlService4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QScxmlScxmlService4nameEv'
    return self.uglySide.call(ritual)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlScxmlService::stateMachine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlscxmlservice.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlScxmlService::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlScxmlService12stateMachineEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

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

  @overload(
      QScxmlStateMachine, QScxmlStateMachine, QScxmlInvokableServiceFactory,
  )
  @overload(QScxmlStateMachine, QScxmlStateMachine, NoneType)
  @overload(QScxmlStateMachine, NoneType, QScxmlInvokableServiceFactory)
  @overload(QScxmlStateMachine, NoneType, NoneType)
  @overload(NoneType, QScxmlStateMachine, QScxmlInvokableServiceFactory)
  @overload(NoneType, QScxmlStateMachine, NoneType)
  @overload(NoneType, NoneType, QScxmlInvokableServiceFactory)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      stateMachine: Optional[QScxmlStateMachine],
      parentStateMachine: Optional[QScxmlStateMachine],
      parent: Optional[QScxmlInvokableServiceFactory],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlScxmlService::QScxmlScxmlService(QScxmlStateMachine *stateMachine,
    QScxmlStateMachine *parentStateMachine, QScxmlInvokableServiceFactory
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlscxmlservice.html#QScxmlScxmlService

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentStateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QScxmlInvokableServiceFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlScxmlService::QScxmlScxmlService(QScxmlStateMachine
    #      *stateMachine, QScxmlStateMachine *parentStateMachine,
    #      QScxmlInvokableServiceFactory *parent)
    self._noteCreation(QScxmlScxmlService, lambda: Rituals.call(
        'ritual_ZN18QScxmlScxmlServiceC1EP18QScxmlStateMachineS1_P29QScxmlI'
        'nvokableServiceFactory',
        self._addressOf(stateMachine), self._addressOf(parentStateMachine),
        self._addressOf(parent),
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

  def d_func(self) -> Optional[QScxmlInvokableServicePrivate]:
    """
    Calls Qt's 'QScxmlInvokableServicePrivate *QScxmlScxmlService::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#d_func

    Returns
    -------

    Optional[QScxmlInvokableServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlInvokableServicePrivate *QScxmlScxmlService::d_func()
    address = self.uglySide.call('ritual_ZN18QScxmlScxmlService6d_funcEv')
    from . import QScxmlInvokableServicePrivate
    return QScxmlInvokableServicePrivate._cuteAt(address)

  def start(self) -> bool:
    """
    Calls Qt's 'bool QScxmlScxmlService::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#start
    """
    #  bool QScxmlScxmlService::start()
    ritual = 'ritual_ZN18QScxmlScxmlService5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QScxmlScxmlService5startEv'
    return self.uglySide.call(ritual)

  @overload(QScxmlEvent)
  @overload(NoneType)
  def postEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlScxmlService::postEvent(QScxmlEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlscxmlservice.html#postEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlScxmlService::postEvent(QScxmlEvent *event)
    ritual = 'ritual_ZN18QScxmlScxmlService9postEventEP11QScxmlEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QScxmlScxmlService9postEventEP11QScxmlEvent'
    self.uglySide.call(ritual, self._addressOf(event))
