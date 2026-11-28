"""
QQuickWorkerScriptEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlWorkerScript/6.12.0/QtQmlWorkerScript/private/qquickworkerscript_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWorkerScriptEngine to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickWorkerScriptEngine(QThread):
  """
  The cute side of Qt's QQuickWorkerScriptEngine: a plain Python object
  standing in front of one C++ QQuickWorkerScriptEngine.

  It is built on the cute 'QThread', as Qt's QQuickWorkerScriptEngine is
  built on Qt's QThread, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWorkerScriptEngine that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'run'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWorkerScriptEngine::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickWorkerScriptEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 13 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QQuickWorkerScriptEngine.

  What to expect
  --------------

  - The C++ QQuickWorkerScriptEngine is created at the first use, not by
    'QQuickWorkerScriptEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWorkerScriptEngine.
  - Qt tells when it has removed the C++ QQuickWorkerScriptEngine. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWorkerScriptEngine that has no cute function yet,
    '__init__', 'executeUrl', 'registerWorkerScript', 'removeWorkerScript',
    'sendMessage', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWorkerScriptEngine'

  #  A C++ QQuickWorkerScriptEngine Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWorkerScriptEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWorkerScriptEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscriptengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWorkerScriptEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWorkerScriptEngine10metaObjectEv',
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
    Qt's 'QQuickWorkerScriptEngine::QQuickWorkerScriptEngine(QQmlEngine
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: no matching member function for
    call to 'connect'.
    """
    raise NotImplementedError(
        "'QQuickWorkerScriptEngine.__init__' has no cute function yet. Qt's "
        "'QQuickWorkerScriptEngine::QQuickWorkerScriptEngine(QQmlEngine "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching member "
        "function for call to 'connect'.")

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
    Calls Qt's 'void QQuickWorkerScriptEngine::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscriptengine.html#run
    """
    #  void QQuickWorkerScriptEngine::run()
    self.uglySide.call('ritual_ZN24QQuickWorkerScriptEngine3runEv')

  @staticmethod
  def executeUrl(*__, **_) -> Never:
    """
    Qt's 'void QQuickWorkerScriptEngine::executeUrl(int a0, const QUrl &a1)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: cannot initialize a parameter of type
    'QEvent *' with an rvalue of type 'WorkerLoadEvent *'.
    """
    raise NotImplementedError(
        "'QQuickWorkerScriptEngine.executeUrl' has no cute function yet. "
        "Qt's 'void QQuickWorkerScriptEngine::executeUrl(int a0, const QUrl "
        "&a1)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: cannot initialize a "
        "parameter of type 'QEvent *' with an rvalue of type "
        "'WorkerLoadEvent *'.")

  @staticmethod
  def registerWorkerScript(*__, **_) -> Never:
    """
    Qt's 'int
    QQuickWorkerScriptEngine::registerWorkerScript(QQuickWorkerScript *a0)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickWorkerScriptEnginePrivate'.
    """
    raise NotImplementedError(
        "'QQuickWorkerScriptEngine.registerWorkerScript' has no cute "
        "function yet. Qt's 'int "
        "QQuickWorkerScriptEngine::registerWorkerScript(QQuickWorkerScript "
        "*a0)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuickWorkerScriptEnginePrivate'.")

  @staticmethod
  def removeWorkerScript(*__, **_) -> Never:
    """
    Qt's 'void QQuickWorkerScriptEngine::removeWorkerScript(int a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickWorkerScriptEnginePrivate'.
    """
    raise NotImplementedError(
        "'QQuickWorkerScriptEngine.removeWorkerScript' has no cute function "
        "yet. Qt's 'void QQuickWorkerScriptEngine::removeWorkerScript(int "
        "a0)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: member access into "
        "incomplete type 'QQuickWorkerScriptEnginePrivate'.")

  @staticmethod
  def sendMessage(*__, **_) -> Never:
    """
    Qt's 'void QQuickWorkerScriptEngine::sendMessage(int a0, const QByteArray
    &a1)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: cannot initialize a parameter of type
    'QEvent *' with an rvalue of type 'WorkerDataEvent *'.
    """
    raise NotImplementedError(
        "'QQuickWorkerScriptEngine.sendMessage' has no cute function yet. "
        "Qt's 'void QQuickWorkerScriptEngine::sendMessage(int a0, const "
        "QByteArray &a1)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: cannot "
        "initialize a parameter of type 'QEvent *' with an rvalue of type "
        "'WorkerDataEvent *'.")
