"""
QCoapInternalReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapinternalreply_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapInternalReply to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QtCoap, QCoapInternalMessage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtNetwork import QHostAddress
  from . import QCoapInternalReplyPrivate, QCoapOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapOption = WAIT['QCoapOption']
  QHostAddress = WAIT['QHostAddress']


class QCoapInternalReply(QCoapInternalMessage):
  """
  The cute side of Qt's QCoapInternalReply: a plain Python object standing in
  front of one C++ QCoapInternalReply.

  It is built on the cute 'QCoapInternalMessage', as Qt's QCoapInternalReply
  is built on Qt's QCoapInternalMessage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapInternalReply that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'appendData',
  'hasMoreBlocksToSend', 'nextBlockToSend', 'addOption', 'setSenderAddress',
  'responseCode', 'senderAddress', 'd_func'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapInternalReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCoapInternalReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCoapInternalReplyPrivate *QCoapInternalReply::d_func()
    const': takes in Python what 'QCoapInternalReplyPrivate
    *QCoapInternalReply::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 2 not a gap; 2 leans on
  'QCoapInternalMessage; 1 leans on 'QCoapInternalReply.

  What to expect
  --------------

  - The C++ QCoapInternalReply is created at the first use, not by
    'QCoapInternalReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapInternalReply.
  - Qt tells when it has removed the C++ QCoapInternalReply. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapInternalReply that has no cute function yet,
    '__init__', 'createFromFrame', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapInternalReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapInternalReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapInternalReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QCoapInternalReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasMoreBlocksToSend(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalReply::hasMoreBlocksToSend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalreply.html#hasMoreBlocksToSend
    """
    #  bool QCoapInternalReply::hasMoreBlocksToSend() const
    return self.uglySide.call(
        'ritual_ZNK18QCoapInternalReply19hasMoreBlocksToSendEv',
    )

  def nextBlockToSend(self) -> int:
    """
    Calls Qt's 'int QCoapInternalReply::nextBlockToSend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalreply.html#nextBlockToSend
    """
    #  int QCoapInternalReply::nextBlockToSend() const
    return self.uglySide.call(
        'ritual_ZNK18QCoapInternalReply15nextBlockToSendEv',
    )

  def responseCode(self) -> QtCoap.ResponseCode:
    """
    Calls Qt's 'QtCoap::ResponseCode QCoapInternalReply::responseCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalreply.html#responseCode

    Returns
    -------

    QtCoap.ResponseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCoap.ResponseCode(number)' gives.
    """
    #  QtCoap::ResponseCode QCoapInternalReply::responseCode() const
    return QtCoap.ResponseCode(self.uglySide.call(
        'ritual_ZNK18QCoapInternalReply12responseCodeEv',
    ))

  def senderAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QCoapInternalReply::senderAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalreply.html#senderAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QCoapInternalReply::senderAddress() const
    address = self.uglySide.call(
        'ritual_ZNK18QCoapInternalReply13senderAddressEv',
    )
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def setSenderAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QCoapInternalReply::setSenderAddress(const QHostAddress
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalreply.html#setSenderAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QCoapInternalReply::setSenderAddress(const QHostAddress &address)
    self.uglySide.call(
        'ritual_ZN18QCoapInternalReply16setSenderAddressERK12QHostAddress',
        self._valueOf(address),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QCoapInternalReply::QCoapInternalReply(QObject *parent)': leans on
    'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate&,
    QObject*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapInternalReply.__init__' has no cute function yet. Qt's "
        "'QCoapInternalReply::QCoapInternalReply(QObject *parent)': leans "
        "on "
        "'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePri"
        "vate&, QObject*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QByteArray)
  def appendData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapInternalReply::appendData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalreply.html#appendData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapInternalReply::appendData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QCoapInternalReply10appendDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QCoapOption)
  def addOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void QCoapInternalReply::addOption(const QCoapOption
    &option)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalreply.html#addOption

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapInternalReply::addOption(const QCoapOption &option)
    ritual = 'ritual_ZN18QCoapInternalReply9addOptionERK11QCoapOption'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QCoapInternalReply9addOptionERK11QCoapOption'
    self.uglySide.call(ritual, self._valueOf(option))

  def d_func(self) -> Optional[QCoapInternalReplyPrivate]:
    """
    Calls Qt's 'QCoapInternalReplyPrivate *QCoapInternalReply::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalreply.html#d_func

    Returns
    -------

    Optional[QCoapInternalReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalReplyPrivate *QCoapInternalReply::d_func()
    address = self.uglySide.call('ritual_ZN18QCoapInternalReply6d_funcEv')
    from . import QCoapInternalReplyPrivate
    return QCoapInternalReplyPrivate._cuteAt(address)

  @staticmethod
  def createFromFrame(*__, **_) -> Never:
    """
    Qt's 'QCoapInternalReply *QCoapInternalReply::createFromFrame(const
    QByteArray &frame, QObject *parent)': leans on
    'QCoapInternalMessage::addOption(QCoapOption::OptionName, QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapInternalReply.createFromFrame' has no cute function yet. "
        "Qt's 'QCoapInternalReply "
        "*QCoapInternalReply::createFromFrame(const QByteArray &frame, "
        "QObject *parent)': leans on "
        "'QCoapInternalMessage::addOption(QCoapOption::OptionName, "
        "QByteArray const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
