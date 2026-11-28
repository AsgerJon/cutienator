"""
QRestAccessManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qrestaccessmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QRestAccessManagerPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QNetworkReply, QRestAccessManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkReply = WAIT['QNetworkReply']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRestAccessManagerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QRestAccessManagerPrivate: a plain Python object
  standing in front of one C++ QRestAccessManagerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QRestAccessManagerPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRestAccessManagerPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'handleReplyFinished',
  'verifyThreadAffinity', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRestAccessManagerPrivate::~QRestAccessManagerPrivate()': the
    destructor: Python never removes a C++ QRestAccessManagerPrivate.
  - Qt's 'QNetworkReply *QRestAccessManagerPrivate::executeRequest(ReqOpRef
    requestOperation, const QObject *context, QtPrivate::QSlotObjectBase
    *rawSlot)': takes a type Python has no way to hand over yet.
  - Qt's 'const QRestAccessManager *QRestAccessManagerPrivate::q_func()
    const': takes in Python what 'QRestAccessManager
    *QRestAccessManagerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QRestAccessManagerPrivate is created at the first use, not by
    'QRestAccessManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRestAccessManagerPrivate.
  - Each name of Qt's QRestAccessManagerPrivate that has no cute function
    yet, 'createActiveRequest', 'executeRequest', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QRestAccessManagerPrivate, each a class in
  #  here as in C++.

  class CallerInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRestAccessManagerPrivate::CallerInfo: a plain
    Python object standing in front of one C++
    QRestAccessManagerPrivate::CallerInfo.

    What exists
    -----------

    No function of Qt's QRestAccessManagerPrivate::CallerInfo yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What to expect
    --------------

    - The C++ QRestAccessManagerPrivate::CallerInfo is created at the first
      use, not by 'QRestAccessManagerPrivate::CallerInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QRestAccessManagerPrivate::CallerInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRestAccessManagerPrivate::CallerInfo'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRestAccessManagerPrivate'

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
    'QRestAccessManagerPrivate::QRestAccessManagerPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanagerprivate.html
    """
    #  QRestAccessManagerPrivate::QRestAccessManagerPrivate()
    self._noteCreation(QRestAccessManagerPrivate, lambda: Rituals.call(
        'ritual_ZN25QRestAccessManagerPrivateC1Ev',
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

  @overload(QNetworkReply)
  @overload(NoneType)
  def handleReplyFinished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QRestAccessManagerPrivate::handleReplyFinished(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanagerprivate.html#handleReplyFinished

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRestAccessManagerPrivate::handleReplyFinished(QNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN25QRestAccessManagerPrivate19handleReplyFinishedEP13QNetw'
        'orkReply',
        self._addressOf(reply),
    )

  @overload(QObject)
  @overload(NoneType)
  def verifyThreadAffinity(self, contextObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QRestAccessManagerPrivate::verifyThreadAffinity(const
    QObject *contextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanagerprivate.html

    Parameters
    ----------

    contextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRestAccessManagerPrivate::verifyThreadAffinity(const QObject
    #      *contextObject)
    self.uglySide.call(
        'ritual_ZN25QRestAccessManagerPrivate20verifyThreadAffinityEPK7QObj'
        'ect',
        self._addressOf(contextObject, 'QObject'),
    )

  def q_func(self) -> Optional[QRestAccessManager]:
    """
    Calls Qt's 'QRestAccessManager *QRestAccessManagerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanagerprivate.html#q_func

    Returns
    -------

    Optional[QRestAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRestAccessManager *QRestAccessManagerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QRestAccessManagerPrivate6q_funcEv',
    )
    from . import QRestAccessManager
    return QRestAccessManager._cuteAt(address)

  @staticmethod
  def createActiveRequest(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply
    *QRestAccessManagerPrivate::createActiveRequest(QNetworkReply *reply,
    const QObject *contextObject, QtPrivate::SlotObjUniquePtr slot)': the
    compiler refuses its ritual as it would be written here: call to deleted
    constructor of 'QtPrivate::SlotObjUniquePtr' (aka
    'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>').
    """
    raise NotImplementedError(
        "'QRestAccessManagerPrivate.createActiveRequest' has no cute "
        "function yet. Qt's 'QNetworkReply "
        "*QRestAccessManagerPrivate::createActiveRequest(QNetworkReply "
        "*reply, const QObject *contextObject, QtPrivate::SlotObjUniquePtr "
        "slot)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QtPrivate::SlotObjUniquePtr' "
        "(aka 'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>')."
    )

  @staticmethod
  def executeRequest(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManagerPrivate::executeRequest(ReqOpRef
      requestOperation, const QObject *context, QtPrivate::QSlotObjectBase
      *rawSlot)': takes a type Python has no way to hand over yet.
    - Qt's 'QNetworkReply
      *QRestAccessManagerPrivate::executeRequest(ReqOpRefJson
      requestOperation, const QJsonDocument &jsonDoc, const QNetworkRequest
      &request, const QObject *context, QtPrivate::QSlotObjectBase
      *rawSlot)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: use of undeclared
      identifier 'warnNoAccessManager'; did you mean 'QRestAccessManager'?.
    """
    raise NotImplementedError(
        "'QRestAccessManagerPrivate.executeRequest' has no cute function "
        "yet. Qt's 'QNetworkReply "
        "*QRestAccessManagerPrivate::executeRequest(ReqOpRef "
        "requestOperation, const QObject *context, "
        "QtPrivate::QSlotObjectBase *rawSlot)': takes a type Python has no "
        "way to hand over yet. Qt's 'QNetworkReply "
        "*QRestAccessManagerPrivate::executeRequest(ReqOpRefJson "
        "requestOperation, const QJsonDocument &jsonDoc, const "
        "QNetworkRequest &request, const QObject *context, "
        "QtPrivate::QSlotObjectBase *rawSlot)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'warnNoAccessManager'; did "
        "you mean 'QRestAccessManager'?.")
