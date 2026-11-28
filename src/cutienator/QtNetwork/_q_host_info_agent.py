"""
QHostInfoAgent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHostInfoAgent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QHostAddress, QHostInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']


class QHostInfoAgent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHostInfoAgent: a plain Python object standing in
  front of one C++ QHostInfoAgent.

  C++ hands a QHostInfoAgent around as a copy, so every C++ QHostInfoAgent
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHostInfoAgent that has a ritual and that Python can
  call so far, 2 names in all: 'lookup', 'reverseLookup'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHostInfoAgent::~QHostInfoAgent()': the destructor: Python removes
    its C++ QHostInfoAgent by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QHostInfoAgent is created at the first use, not by
    'QHostInfoAgent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHostInfoAgent back gives a copy the ritual made for
    Python, in a new cute QHostInfoAgent.
  - Each name of Qt's QHostInfoAgent that has no cute function yet,
    'fromName', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def lookup(hostName: str) -> QHostInfo:
    """
    Calls Qt's 'QHostInfo QHostInfoAgent::lookup(const QString &hostName)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfoagent.html#lookup

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QHostInfo
      A new cute QHostInfo around the copy Qt gave back. Python owns it.
    """
    #  QHostInfo QHostInfoAgent::lookup(const QString &hostName)
    address = Rituals.call(
        'ritual_ZN14QHostInfoAgent6lookupERK7QString', hostName,
    )
    from . import QHostInfo
    return QHostInfo._cuteOwning(address)

  @staticmethod
  @overload(QHostAddress)
  def reverseLookup(address: QHostAddress) -> QHostInfo:
    """
    Calls Qt's 'QHostInfo QHostInfoAgent::reverseLookup(const QHostAddress
    &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfoagent.html#reverseLookup

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    Returns
    -------

    QHostInfo
      A new cute QHostInfo around the copy Qt gave back. Python owns it.
    """
    #  QHostInfo QHostInfoAgent::reverseLookup(const QHostAddress &address)
    address = Rituals.call(
        'ritual_ZN14QHostInfoAgent13reverseLookupERK12QHostAddress',
        CuteMixin._valueOf(address),
    )
    from . import QHostInfo
    return QHostInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHostInfoAgent'

  #  Qt's '~QHostInfoAgent()'. Naming it makes this a value class: Python
  #  owns every C++ QHostInfoAgent behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QHostInfoAgentD1Ev'

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

  @staticmethod
  def fromName(*__, **_) -> Never:
    """
    Qt's 'QHostInfo QHostInfoAgent::fromName(const QString &hostName)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QHostInfoAgent.fromName' has no cute function yet. Qt's "
        "'QHostInfo QHostInfoAgent::fromName(const QString &hostName)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
