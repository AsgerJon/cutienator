"""
QMqttClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/6.12.0/QtMqtt/private/qmqttclient_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMqttClientPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObjectPrivate
from . import QMqttClient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QMqttClientPrivate(QObjectPrivate):
  """
  The cute side of Qt's QMqttClientPrivate: a plain Python object standing in
  front of one C++ QMqttClientPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QMqttClientPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMqttClientPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'setStateAndError',
  'setClientId'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMqttClient *QMqttClientPrivate::q_func() const': takes in
    Python what 'QMqttClient *QMqttClientPrivate::q_func()' takes.
  - Qt's 'QMqttClientPrivate::~QMqttClientPrivate()': the destructor: Python
    never removes a C++ QMqttClientPrivate.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'vtable for QMqttConnection',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QMqttClientPrivate is created at the first use, not by
    'QMqttClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMqttClientPrivate.
  - Each name of Qt's QMqttClientPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttClientPrivate'

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

  @overload(QMqttClient.ClientState)
  @overload(QMqttClient.ClientState, QMqttClient.ClientError)
  def setStateAndError(
      self,
      s: QMqttClient.ClientState,
      e: QMqttClient.ClientError = QMqttClient.ClientError.NoError,
  ) -> None:
    """
    Calls Qt's 'void
    QMqttClientPrivate::setStateAndError(QMqttClient::ClientState s,
    QMqttClient::ClientError e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclientprivate.html#setStateAndError

    Parameters
    ----------

    s : QMqttClient.ClientState
      Passed on as its number.

    e : QMqttClient.ClientError
      Passed on as its number. May be left out, as in Qt: it is then
      QMqttClient.ClientError.NoError.
    """
    #  void QMqttClientPrivate::setStateAndError(QMqttClient::ClientState s,
    #      QMqttClient::ClientError e)
    self.uglySide.call(
        'ritual_ZN18QMqttClientPrivate16setStateAndErrorEN11QMqttClient11Cl'
        'ientStateENS0_11ClientErrorE',
        s.value, e.value,
    )

  @overload(str)
  def setClientId(self, id: str) -> None:
    """
    Calls Qt's 'void QMqttClientPrivate::setClientId(const QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclientprivate.html#setClientId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClientPrivate::setClientId(const QString &id)
    self.uglySide.call(
        'ritual_ZN18QMqttClientPrivate11setClientIdERK7QString', id,
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
    Qt's 'QMqttClientPrivate::QMqttClientPrivate(QMqttClient *c)': leans on
    'vtable for QMqttConnection', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttClientPrivate.__init__' has no cute function yet. Qt's "
        "'QMqttClientPrivate::QMqttClientPrivate(QMqttClient *c)': leans on "
        "'vtable for QMqttConnection', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QMqttClient]:
    """
    Calls Qt's 'QMqttClient *QMqttClientPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclientprivate.html#q_func

    Returns
    -------

    Optional[QMqttClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttClient *QMqttClientPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QMqttClientPrivate6q_funcEv')
    return QMqttClient._cuteAt(address)
