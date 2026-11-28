"""
QCoapReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapreply_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCoapReplyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QIODevicePrivate
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QObject
  from ..QtNetwork import QHostAddress
  from . import QCoapMessage, QCoapReply, QCoapRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapMessage = WAIT['QCoapMessage']
  QCoapRequest = WAIT['QCoapRequest']
  QHostAddress = WAIT['QHostAddress']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapReplyPrivate(QIODevicePrivate):
  """
  The cute side of Qt's QCoapReplyPrivate: a plain Python object standing in
  front of one C++ QCoapReplyPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QCoapReplyPrivate is
  built on Qt's QIODevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapReplyPrivate that has a ritual and that Python
  can call so far, 8 names in all: '_q_setRunning', '_q_setContent',
  '_q_setNotified', '_q_setObserveCancelled', '_q_setFinished',
  '_q_setError', 'createCoapReply', 'q_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCoapReply *QCoapReplyPrivate::q_func() const': takes in
    Python what 'QCoapReply *QCoapReplyPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QCoapReplyPrivate is created at the first use, not by
    'QCoapReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapReplyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCoapRequest)
  @overload(QCoapRequest, QObject)
  @overload(QCoapRequest, NoneType)
  def createCoapReply(
      request: QCoapRequest,
      parent: Optional[QObject] = None,
  ) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapReplyPrivate::createCoapReply(const
    QCoapRequest &request, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#createCoapReply

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapReplyPrivate::createCoapReply(const QCoapRequest
    #      &request, QObject *parent)
    address = Rituals.call(
        'ritual_ZN17QCoapReplyPrivate15createCoapReplyERK12QCoapRequestP7QO'
        'bject',
        CuteMixin._valueOf(request), CuteMixin._addressOf(parent, 'QObject'),
    )
    from . import QCoapReply
    return QCoapReply._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapReplyPrivate'

  #  A C++ QCoapReplyPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapReplyPrivate'

  #  The functions Qt calls itself that QCoapReplyPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      '_q_setContent': (
          ('_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QCoap'
           'MessageN6QtCoap12ResponseCodeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('address', 'value', 'QtCoap:QCoapMessage'),
               ('int', 'enum', 'QtCoap:QtCoap.ResponseCode'),
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

  @overload(QCoapRequest)
  def __init__(self, request: QCoapRequest) -> None:
    """
    Notes what was given, for Qt's
    'QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &request)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#QCoapReplyPrivate

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.
    """
    #  QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &request)
    self._noteCreation(QCoapReplyPrivate, lambda: Rituals.call(
        'ritual_ZN17QCoapReplyPrivateC1ERK12QCoapRequest',
        self._valueOf(request),
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

  @overload(QByteArray, int)
  def _q_setRunning(self, a0: QByteArray, a1: int) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setRunning(const QCoapToken &a0,
    QCoapMessageId a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setRunning

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : int
      Passed on as it is.
    """
    #  void QCoapReplyPrivate::_q_setRunning(const QCoapToken &a0,
    #      QCoapMessageId a1)
    self.uglySide.call(
        'ritual_ZN17QCoapReplyPrivate13_q_setRunningERK10QByteArrayt',
        self._valueOf(a0), a1,
    )

  @overload(QHostAddress, QCoapMessage, QtCoap.ResponseCode)
  def _q_setContent(
      self,
      sender: QHostAddress,
      a1: QCoapMessage,
      a2: QtCoap.ResponseCode,
  ) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setContent(const QHostAddress
    &sender, const QCoapMessage &a1, QtCoap::ResponseCode a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setContent

    Parameters
    ----------

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    a1 : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.

    a2 : QtCoap.ResponseCode
      Passed on as its number.
    """
    #  void QCoapReplyPrivate::_q_setContent(const QHostAddress &sender,
    #      const QCoapMessage &a1, QtCoap::ResponseCode a2)
    ritual = (
        'ritual_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QC'
        'oapMessageN6QtCoap12ResponseCodeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddress'
          'RK12QCoapMessageN6QtCoap12ResponseCodeE')
    self.uglySide.call(
        ritual, self._valueOf(sender), self._valueOf(a1), a2.value,
    )

  def _q_setNotified(self) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setNotified()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setNotified
    """
    #  void QCoapReplyPrivate::_q_setNotified()
    self.uglySide.call('ritual_ZN17QCoapReplyPrivate14_q_setNotifiedEv')

  def _q_setObserveCancelled(self) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setObserveCancelled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setObserveCancelled
    """
    #  void QCoapReplyPrivate::_q_setObserveCancelled()
    self.uglySide.call(
        'ritual_ZN17QCoapReplyPrivate22_q_setObserveCancelledEv',
    )

  @overload()
  @overload(QtCoap.Error)
  def _q_setFinished(self, a0: QtCoap.Error = QtCoap.Error.Ok) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setFinished(QtCoap::Error a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setFinished

    Parameters
    ----------

    a0 : QtCoap.Error
      Passed on as its number. May be left out, as in Qt: it is then
      QtCoap.Error.Ok.
    """
    #  void QCoapReplyPrivate::_q_setFinished(QtCoap::Error a0)
    self.uglySide.call(
        'ritual_ZN17QCoapReplyPrivate14_q_setFinishedEN6QtCoap5ErrorE',
        a0.value,
    )

  @overload(QtCoap.ResponseCode)
  def _q_setError(self, code: QtCoap.ResponseCode) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode
    code)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setError

    Parameters
    ----------

    code : QtCoap.ResponseCode
      Passed on as its number.
    """
    #  void QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode code)
    self.uglySide.call(
        'ritual_ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap12ResponseCodeE',
        code.value,
    )

  @overload(QtCoap.Error)
  def _q_setError(self, a0: QtCoap.Error) -> None:
    """
    Calls Qt's 'void QCoapReplyPrivate::_q_setError(QtCoap::Error a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreplyprivate.html#_q_setError

    Parameters
    ----------

    a0 : QtCoap.Error
      Passed on as its number.
    """
    #  void QCoapReplyPrivate::_q_setError(QtCoap::Error a0)
    self.uglySide.call(
        'ritual_ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap5ErrorE',
        a0.value,
    )

  def q_func(self) -> Optional[QCoapReply]:
    """
    Calls Qt's 'QCoapReply *QCoapReplyPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreplyprivate.html#q_func

    Returns
    -------

    Optional[QCoapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReply *QCoapReplyPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QCoapReplyPrivate6q_funcEv')
    from . import QCoapReply
    return QCoapReply._cuteAt(address)
