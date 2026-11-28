"""
QCoapConnectionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapConnectionPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QCoapConnection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCoapConnectionPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCoapConnectionPrivate: a plain Python object
  standing in front of one C++ QCoapConnectionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCoapConnectionPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapConnectionPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'sendRequest', 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapConnectionPrivate::~QCoapConnectionPrivate()': the destructor:
    Python never removes a C++ QCoapConnectionPrivate.
  - Qt's 'const QCoapConnection *QCoapConnectionPrivate::q_func() const':
    takes in Python what 'QCoapConnection *QCoapConnectionPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QCoapConnectionPrivate is created at the first use, not by
    'QCoapConnectionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapConnectionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapConnectionPrivate'

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
  @overload(QtCoap.SecurityMode)
  def __init__(
      self,
      security: QtCoap.SecurityMode = QtCoap.SecurityMode.NoSecurity,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapConnectionPrivate::QCoapConnectionPrivate(QtCoap::SecurityMode
    security)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnectionprivate.html#QCoapConnectionPrivate

    Parameters
    ----------

    security : QtCoap.SecurityMode
      Passed on as its number. May be left out, as in Qt: it is then
      QtCoap.SecurityMode.NoSecurity.
    """
    #  QCoapConnectionPrivate::QCoapConnectionPrivate(QtCoap::SecurityMode
    #      security)
    self._noteCreation(QCoapConnectionPrivate, lambda: Rituals.call(
        'ritual_ZN22QCoapConnectionPrivateC1EN6QtCoap12SecurityModeE',
        security.value,
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

  @overload(QByteArray, str, int)
  def sendRequest(self, request: QByteArray, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapConnectionPrivate::sendRequest(const QByteArray
    &request, const QString &host, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnectionprivate.html#sendRequest

    Parameters
    ----------

    request : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    host : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QCoapConnectionPrivate::sendRequest(const QByteArray &request,
    #      const QString &host, quint16 port)
    self.uglySide.call(
        'ritual_ZN22QCoapConnectionPrivate11sendRequestERK10QByteArrayRK7QS'
        'tringt',
        self._valueOf(request), host, port,
    )

  def q_func(self) -> Optional[QCoapConnection]:
    """
    Calls Qt's 'QCoapConnection *QCoapConnectionPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnectionprivate.html#q_func

    Returns
    -------

    Optional[QCoapConnection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapConnection *QCoapConnectionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QCoapConnectionPrivate6q_funcEv',
    )
    from . import QCoapConnection
    return QCoapConnection._cuteAt(address)
