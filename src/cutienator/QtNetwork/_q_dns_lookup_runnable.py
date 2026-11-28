"""
QDnsLookupRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDnsLookupRunnable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject, QRunnable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDnsLookupReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDnsLookupReply = WAIT['QDnsLookupReply']


class QDnsLookupRunnable(QObject, QRunnable):
  """
  The cute side of Qt's QDnsLookupRunnable: a plain Python object standing in
  front of one C++ QDnsLookupRunnable.

  It is built on the cute 'QObject', as Qt's QDnsLookupRunnable is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QRunnable' as well, as Qt's QDnsLookupRunnable is built on Qt's QRunnable
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDnsLookupRunnable that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'run', 'finished'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDnsLookupRunnable::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDnsLookupRunnable::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 14 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 not a gap; 1 a template; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 leans on 'QDnsLookupRunnable; 1 leans on
  'vtable for QDnsLookupRunnable', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDnsLookupRunnable is created at the first use, not by
    'QDnsLookupRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDnsLookupRunnable.
  - Qt tells when it has removed the C++ QDnsLookupRunnable. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDnsLookupRunnable that has no cute function yet,
    '__init__', 'decodeLabel', 'parseResponse', 'query', 'sendDnsOverTls',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsLookupRunnable'

  #  Qt's QDnsLookupRunnable is built on more than one class. The part of a
  #  C++ QDnsLookupRunnable that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QRunnable': 'ritual_cast_QDnsLookupRunnable_QRunnable',
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
    Calls Qt's 'const QMetaObject *QDnsLookupRunnable::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookuprunnable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDnsLookupRunnable::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QDnsLookupRunnable10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDnsLookupRunnable::QDnsLookupRunnable(const QDnsLookupPrivate
    *d)': leans on 'vtable for QDnsLookupRunnable', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDnsLookupRunnable.__init__' has no cute function yet. Qt's "
        "'QDnsLookupRunnable::QDnsLookupRunnable(const QDnsLookupPrivate "
        "*d)': leans on 'vtable for QDnsLookupRunnable', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def run(self) -> None:
    """
    Calls Qt's 'void QDnsLookupRunnable::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookuprunnable.html#run
    """
    #  void QDnsLookupRunnable::run()
    self.uglySide.call('ritual_ZN18QDnsLookupRunnable3runEv')

  @overload(QDnsLookupReply)
  def finished(self, reply: QDnsLookupReply) -> None:
    """
    Calls Qt's 'void QDnsLookupRunnable::finished(const QDnsLookupReply
    &reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookuprunnable.html#finished

    Parameters
    ----------

    reply : QDnsLookupReply
      Passed on as a value: Qt reads the C++ QDnsLookupReply, which stays
      Python's own.
    """
    #  void QDnsLookupRunnable::finished(const QDnsLookupReply &reply)
    self.uglySide.call(
        'ritual_ZN18QDnsLookupRunnable8finishedERK15QDnsLookupReply',
        self._valueOf(reply),
    )

  @staticmethod
  def decodeLabel(*__, **_) -> Never:
    """
    Qt's 'QDnsLookupRunnable::decodeLabel': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QDnsLookupRunnable.decodeLabel' has no cute function yet. Qt's "
        "'QDnsLookupRunnable::decodeLabel': a template: a pattern and no "
        "single function.")

  @staticmethod
  def parseResponse(*__, **_) -> Never:
    """
    Qt's 'void QDnsLookupRunnable::parseResponse(QDnsLookupReply *reply,
    ReplyBuffer &buffer, int responseLength)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'host'.
    """
    raise NotImplementedError(
        "'QDnsLookupRunnable.parseResponse' has no cute function yet. Qt's "
        "'void QDnsLookupRunnable::parseResponse(QDnsLookupReply *reply, "
        "ReplyBuffer &buffer, int responseLength)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'host'.")

  @staticmethod
  def query(*__, **_) -> Never:
    """
    Qt's 'void QDnsLookupRunnable::query(QDnsLookupReply *reply)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QDnsLookupRunnable.query' has no cute function yet. Qt's 'void "
        "QDnsLookupRunnable::query(QDnsLookupReply *reply)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def sendDnsOverTls(*__, **_) -> Never:
    """
    Qt's 'bool QDnsLookupRunnable::sendDnsOverTls(QDnsLookupReply *reply,
    QSpan<unsigned char> query, ReplyBuffer &response)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDnsLookupRunnable.sendDnsOverTls' has no cute function yet. Qt's "
        "'bool QDnsLookupRunnable::sendDnsOverTls(QDnsLookupReply *reply, "
        "QSpan<unsigned char> query, ReplyBuffer &response)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
