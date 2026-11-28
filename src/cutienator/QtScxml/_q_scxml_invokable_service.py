"""
QScxmlInvokableService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

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


class QScxmlInvokableService(QObject):
  """
  The cute side of Qt's QScxmlInvokableService: a plain Python object
  standing in front of one C++ QScxmlInvokableService.

  It is built on the cute 'QObject', as Qt's QScxmlInvokableService is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlInvokableService that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'parentStateMachine', 'start', 'id', 'name', 'postEvent'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlInvokableService::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScxmlInvokableService::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScxmlInvokableServicePrivate
    *QScxmlInvokableService::d_func() const': takes in Python what
    'QScxmlInvokableServicePrivate *QScxmlInvokableService::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlInvokableService is created at the first use, not by
    'QScxmlInvokableService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInvokableService.
  - Qt tells when it has removed the C++ QScxmlInvokableService. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QScxmlInvokableService::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokableservice.html#tr

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
    #  QString QScxmlInvokableService::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QScxmlInvokableService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInvokableService'

  #  A C++ QScxmlInvokableService Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlInvokableService'

  #  The functions Qt calls itself that QScxmlInvokableService is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN22QScxmlInvokableService5startEv',
           ('bool', 'number', ''),
           ()),
      ),
      'id': (
          ('_ZNK22QScxmlInvokableService2idEv',
           ('address', 'text', ''),
           ()),
      ),
      'name': (
          ('_ZNK22QScxmlInvokableService4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'postEvent': (
          ('_ZN22QScxmlInvokableService9postEventEP11QScxmlEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:QScxmlEvent'),
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
    Calls Qt's 'const QMetaObject *QScxmlInvokableService::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlInvokableService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QScxmlInvokableService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentStateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine
    *QScxmlInvokableService::parentStateMachine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservice.html#parentStateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlInvokableService::parentStateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK22QScxmlInvokableService18parentStateMachineEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  def id(self) -> str:
    """
    Calls Qt's 'QString QScxmlInvokableService::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokableservice.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlInvokableService::id() const
    return self.uglySide.call('ritual_ZNK22QScxmlInvokableService2idEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlInvokableService::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokableservice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlInvokableService::name() const
    return self.uglySide.call('ritual_ZNK22QScxmlInvokableService4nameEv')

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

  @overload(QScxmlStateMachine, QScxmlInvokableServiceFactory)
  @overload(QScxmlStateMachine, NoneType)
  @overload(NoneType, QScxmlInvokableServiceFactory)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parentStateMachine: Optional[QScxmlStateMachine],
      parent: Optional[QScxmlInvokableServiceFactory],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlInvokableService::QScxmlInvokableService(QScxmlStateMachine
    *parentStateMachine, QScxmlInvokableServiceFactory *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservice.html#QScxmlInvokableService

    Parameters
    ----------

    parentStateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QScxmlInvokableServiceFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlInvokableService::QScxmlInvokableService(QScxmlStateMachine
    #      *parentStateMachine, QScxmlInvokableServiceFactory *parent)
    self._noteCreation(QScxmlInvokableService, lambda: Rituals.call(
        'ritual_ZN22QScxmlInvokableServiceC1EP18QScxmlStateMachineP29QScxml'
        'InvokableServiceFactory',
        self._addressOf(parentStateMachine), self._addressOf(parent),
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
    Calls Qt's 'QScxmlInvokableServicePrivate
    *QScxmlInvokableService::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokableservice.html#d_func

    Returns
    -------

    Optional[QScxmlInvokableServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlInvokableServicePrivate *QScxmlInvokableService::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QScxmlInvokableService6d_funcEv',
    )
    from . import QScxmlInvokableServicePrivate
    return QScxmlInvokableServicePrivate._cuteAt(address)

  def start(self) -> bool:
    """
    Calls Qt's 'bool QScxmlInvokableService::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokableservice.html#start
    """
    #  bool QScxmlInvokableService::start()
    return self.uglySide.call('ritual_ZN22QScxmlInvokableService5startEv')

  @overload(QScxmlEvent)
  @overload(NoneType)
  def postEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlInvokableService::postEvent(QScxmlEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableservice.html#postEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlInvokableService::postEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN22QScxmlInvokableService9postEventEP11QScxmlEvent',
        self._addressOf(event),
    )


#  Qt's 'QList<QScxmlInvokableService *>': the list of
#  QScxmlInvokableService, which 'QList[QScxmlInvokableService]' gives. It is
#  made here, so that there is one as soon as there can be a
#  QScxmlInvokableService.
QList.createKind(
    QScxmlInvokableService, 'address',
    make='ritual_list_make_QScxmlInvokableService_ptr',
    add='ritual_list_add_QScxmlInvokableService_ptr',
    size='ritual_list_size_QScxmlInvokableService_ptr',
    at='ritual_list_at_QScxmlInvokableService_ptr',
    drop='ritual_list_drop_QScxmlInvokableService_ptr',
)
