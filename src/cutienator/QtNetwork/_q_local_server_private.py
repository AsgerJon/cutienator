"""
QLocalServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qlocalserver_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLocalServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLocalServer


class QLocalServerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QLocalServerPrivate: a plain Python object standing
  in front of one C++ QLocalServerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QLocalServerPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLocalServerPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func',
  '_qt_property_socketOptions_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLocalServer *QLocalServerPrivate::q_func() const': takes in
    Python what 'QLocalServer *QLocalServerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  8 of the 12 functions Qt declares: 8 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QLocalServerPrivate is created at the first use, not by
    'QLocalServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalServerPrivate.
  - Each name of Qt's QLocalServerPrivate that has no cute function yet,
    '_q_onNewConnection', 'closeServer', 'init', 'listen', 'removeServer',
    'setError', 'waitForNewConnection', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_socketOptions_offset() -> int:
    """
    Calls Qt's 'size_t
    QLocalServerPrivate::_qt_property_socketOptions_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserverprivate.html
    """
    #  size_t QLocalServerPrivate::_qt_property_socketOptions_offset()
    return Rituals.call(
        'ritual_ZN19QLocalServerPrivate33_qt_property_socketOptions_offsetE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalServerPrivate'

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
    'QLocalServerPrivate::QLocalServerPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserverprivate.html#QLocalServerPrivate
    """
    #  QLocalServerPrivate::QLocalServerPrivate()
    self._noteCreation(QLocalServerPrivate, lambda: Rituals.call(
        'ritual_ZN19QLocalServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QLocalServer]:
    """
    Calls Qt's 'QLocalServer *QLocalServerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserverprivate.html#q_func

    Returns
    -------

    Optional[QLocalServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLocalServer *QLocalServerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QLocalServerPrivate6q_funcEv')
    from . import QLocalServer
    return QLocalServer._cuteAt(address)

  @staticmethod
  def _q_onNewConnection(*__, **_) -> Never:
    """
    Qt's 'void QLocalServerPrivate::_q_onNewConnection()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate._q_onNewConnection' has no cute function yet. "
        "Qt's 'void QLocalServerPrivate::_q_onNewConnection()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def closeServer(*__, **_) -> Never:
    """
    Qt's 'void QLocalServerPrivate::closeServer()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.closeServer' has no cute function yet. Qt's "
        "'void QLocalServerPrivate::closeServer()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QLocalServerPrivate::init()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.init' has no cute function yet. Qt's 'void "
        "QLocalServerPrivate::init()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def listen(*__, **_) -> Never:
    """
    - Qt's 'bool QLocalServerPrivate::listen(const QString &name)': cannot be
      called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    - Qt's 'bool QLocalServerPrivate::listen(qintptr socketDescriptor)':
      cannot be called and cannot be called through the meta-object and
      cannot be copied: no header file has its code, Qt's source does not
      mark it or its class for use from outside Qt or writes it 'inline' or
      nowhere, and it is no signal, slot or invokable function giving back
      nothing, of a class built on QObject, and Qt's source has no code for
      it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.listen' has no cute function yet. Qt's 'bool "
        "QLocalServerPrivate::listen(const QString &name)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest. Qt's 'bool "
        "QLocalServerPrivate::listen(qintptr socketDescriptor)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def removeServer(*__, **_) -> Never:
    """
    Qt's 'bool QLocalServerPrivate::removeServer(const QString &name)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.removeServer' has no cute function yet. Qt's "
        "'bool QLocalServerPrivate::removeServer(const QString &name)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void QLocalServerPrivate::setError(const QString &function)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.setError' has no cute function yet. Qt's "
        "'void QLocalServerPrivate::setError(const QString &function)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def waitForNewConnection(*__, **_) -> Never:
    """
    Qt's 'void QLocalServerPrivate::waitForNewConnection(int msec, bool
    *timedOut)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalServerPrivate.waitForNewConnection' has no cute function "
        "yet. Qt's 'void QLocalServerPrivate::waitForNewConnection(int "
        "msec, bool *timedOut)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
