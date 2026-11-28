"""
QScxmlEventBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlevent_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QScxmlEventBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlEventBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlEventBuilder: a plain Python object standing in
  front of one C++ QScxmlEventBuilder.

  C++ hands a QScxmlEventBuilder around as a copy, so every C++
  QScxmlEventBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScxmlEventBuilder that has a ritual and that Python
  can call so far, 2 names in all: 'init', 'submitError'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlEventBuilder::~QScxmlEventBuilder()': the destructor: Python
    removes its C++ QScxmlEventBuilder by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 3 leans on 'QScxmlEventBuilder; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QScxmlEventBuilder is created at the first use, not by
    'QScxmlEventBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlEventBuilder back gives a copy the ritual made
    for Python, in a new cute QScxmlEventBuilder.
  - Each name of Qt's QScxmlEventBuilder that has no cute function yet,
    'buildEvent', 'errorEvent', 'evaluate', 'generateId', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlEventBuilder'

  #  Qt's '~QScxmlEventBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QScxmlEventBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QScxmlEventBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlEventBuilder::QScxmlEventBuilder()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventbuilder.html#QScxmlEventBuilder
    """
    #  QScxmlEventBuilder::QScxmlEventBuilder()
    self._noteCreation(QScxmlEventBuilder, lambda: Rituals.call(
        'ritual_ZN18QScxmlEventBuilderC1Ev',
    ))

  @overload(
      QScxmlStateMachine, str, WAIT['QScxmlExecutableContent.DoneData'],
  )
  @overload(QScxmlStateMachine, str, NoneType)
  @overload(NoneType, str, WAIT['QScxmlExecutableContent.DoneData'])
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      stateMachine: Optional[QScxmlStateMachine],
      eventName: str,
      doneData: Optional[QScxmlExecutableContent.DoneData],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine *stateMachine,
    const QString &eventName, const QScxmlExecutableContent::DoneData
    *doneData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventbuilder.html#QScxmlEventBuilder

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    eventName : str
      Passed on as it is: a QString is made of it for the call.

    doneData : Optional[QScxmlExecutableContent.DoneData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine
    #      *stateMachine, const QString &eventName, const
    #      QScxmlExecutableContent::DoneData *doneData)
    self._noteCreation(QScxmlEventBuilder, lambda: Rituals.call(
        'ritual_ZN18QScxmlEventBuilderC1EP18QScxmlStateMachineRK7QStringPKN'
        '23QScxmlExecutableContent8DoneDataE',
        self._addressOf(stateMachine), eventName, self._addressOf(doneData),
    ))

  @overload(QScxmlStateMachine, WAIT['QScxmlExecutableContent.Send'])
  @overload(NoneType, WAIT['QScxmlExecutableContent.Send'])
  def __init__(
      self,
      stateMachine: Optional[QScxmlStateMachine],
      send: QScxmlExecutableContent.Send,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine *stateMachine,
    const QScxmlExecutableContent::Send &send)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventbuilder.html#QScxmlEventBuilder

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    send : QScxmlExecutableContent.Send
      Passed on as a value: Qt reads the C++ QScxmlExecutableContent::Send,
      which stays Python's own.
    """
    #  QScxmlEventBuilder::QScxmlEventBuilder(QScxmlStateMachine
    #      *stateMachine, const QScxmlExecutableContent::Send &send)
    self._noteCreation(QScxmlEventBuilder, lambda: Rituals.call(
        'ritual_ZN18QScxmlEventBuilderC1EP18QScxmlStateMachineRKN23QScxmlEx'
        'ecutableContent4SendE',
        self._addressOf(stateMachine), self._valueOf(send),
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

  def init(self) -> None:
    """
    Calls Qt's 'void QScxmlEventBuilder::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmleventbuilder.html#init
    """
    #  void QScxmlEventBuilder::init()
    self.uglySide.call('ritual_ZN18QScxmlEventBuilder4initEv')

  @overload(str, str)
  @overload(str, str, str)
  def submitError(self, type: str, msg: str, sendid: str = '') -> None:
    """
    Calls Qt's 'void QScxmlEventBuilder::submitError(const QString &type,
    const QString &msg, const QString &sendid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmleventbuilder.html#submitError

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    sendid : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QScxmlEventBuilder::submitError(const QString &type, const
    #      QString &msg, const QString &sendid)
    self.uglySide.call(
        'ritual_ZN18QScxmlEventBuilder11submitErrorERK7QStringS2_S2_',
        type, msg, sendid,
    )

  @staticmethod
  def buildEvent(*__, **_) -> Never:
    """
    Qt's 'QScxmlEvent *QScxmlEventBuilder::buildEvent()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'NoEvaluator'; did you mean
    'QScxmlExecutableContent::NoEvaluator'?.
    """
    raise NotImplementedError(
        "'QScxmlEventBuilder.buildEvent' has no cute function yet. Qt's "
        "'QScxmlEvent *QScxmlEventBuilder::buildEvent()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'NoEvaluator'; did you "
        "mean 'QScxmlExecutableContent::NoEvaluator'?.")

  @staticmethod
  def errorEvent(*__, **_) -> Never:
    """
    Qt's 'QScxmlEvent *QScxmlEventBuilder::errorEvent(QScxmlStateMachine
    *stateMachine, const QString &name, const QString &message, const QString
    &sendid)': leans on 'QScxmlEventBuilder::buildEvent()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QScxmlEventBuilder.errorEvent' has no cute function yet. Qt's "
        "'QScxmlEvent *QScxmlEventBuilder::errorEvent(QScxmlStateMachine "
        "*stateMachine, const QString &name, const QString &message, const "
        "QString &sendid)': leans on 'QScxmlEventBuilder::buildEvent()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def evaluate(*__, **_) -> Never:
    """
    - Qt's 'bool QScxmlEventBuilder::evaluate(const
      QScxmlExecutableContent::ParameterInfo &param, QScxmlStateMachine
      *stateMachine, QVariantMap &keyValues)': cannot be called and cannot be
      called through the meta-object and cannot be copied: no header file has
      its code, Qt's source does not mark it or its class for use from
      outside Qt or writes it 'inline' or nowhere, and it is no signal, slot
      or invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
    - Qt's 'bool QScxmlEventBuilder::evaluate(const
      QScxmlExecutableContent::Array<QScxmlExecutableContent::ParameterInfo>
      *params, QScxmlStateMachine *stateMachine, QVariantMap &keyValues)':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: unknown type name 'ParameterInfo'; did you
      mean 'QScxmlExecutableContent::ParameterInfo'?.
    """
    raise NotImplementedError(
        "'QScxmlEventBuilder.evaluate' has no cute function yet. Qt's 'bool "
        "QScxmlEventBuilder::evaluate(const "
        "QScxmlExecutableContent::ParameterInfo &param, QScxmlStateMachine "
        "*stateMachine, QVariantMap &keyValues)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest. Qt's 'bool "
        "QScxmlEventBuilder::evaluate(const "
        "QScxmlExecutableContent::Array<QScxmlExecutableContent::ParameterIn"
        "fo> *params, QScxmlStateMachine *stateMachine, QVariantMap "
        "&keyValues)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'ParameterInfo'; did you mean "
        "'QScxmlExecutableContent::ParameterInfo'?.")

  @staticmethod
  def generateId(*__, **_) -> Never:
    """
    Qt's 'QString QScxmlEventBuilder::generateId() const': leans on
    'QScxmlEventBuilder::idCounter', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlEventBuilder.generateId' has no cute function yet. Qt's "
        "'QString QScxmlEventBuilder::generateId() const': leans on "
        "'QScxmlEventBuilder::idCounter', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
