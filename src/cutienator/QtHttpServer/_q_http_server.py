"""
QHttpServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractHttpServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHttpServerPrivate, QHttpServerRouter

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServer(QAbstractHttpServer):
  """
  The cute side of Qt's QHttpServer: a plain Python object standing in front
  of one C++ QHttpServer.

  It is built on the cute 'QAbstractHttpServer', as Qt's QHttpServer is built
  on Qt's QAbstractHttpServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpServer that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'd_func', 'router',
  'clearMissingHandler'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QHttpServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QHttpServerPrivate *QHttpServer::d_func() const': takes in
    Python what 'QHttpServerPrivate *QHttpServer::d_func()' takes.
  - Qt's 'QHttpServer::~QHttpServer()': the destructor: Python never removes
    a C++ QHttpServer.
  - Qt's 'const QHttpServerRouter *QHttpServer::router() const': takes in
    Python what 'QHttpServerRouter *QHttpServer::router()' takes.
  - Qt's 'void QHttpServer::setMissingHandlerImpl(const QObject *context,
    QtPrivate::QSlotObjectBase *handler)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'void QHttpServer::addAfterRequestHandlerImpl(const QObject
    *context, QtPrivate::QSlotObjectBase *handler)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'bool QHttpServer::handleRequest(const QHttpServerRequest &request,
    QHttpServerResponder &responder)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QHttpServer::missingHandler(const QHttpServerRequest &request,
    QHttpServerResponder &responder)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QHttpServer::sendResponse(QHttpServerResponse &&response,
    const QHttpServerRequest &request, QHttpServerResponder &&responder)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QHttpServer::sendResponse(QFuture<QHttpServerResponse>
    &&response, const QHttpServerRequest &request, QHttpServerResponder
    &&responder)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  12 of the 29 functions Qt declares: 10 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttpServer is created at the first use, not by
    'QHttpServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServer.
  - Qt tells when it has removed the C++ QHttpServer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QHttpServer that has no cute function yet,
    'addAfterRequestHandler', 'addAfterRequestHandlerImpl',
    'createRouteHandler', 'responseImpl', 'route', 'routeImpl',
    'sendResponse', 'setMissingHandler', 'setMissingHandlerImpl', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QHttpServer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserver.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QHttpServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QHttpServer10metaObjectEv')
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QHttpServer::QHttpServer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserver.html#QHttpServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHttpServer::QHttpServer(QObject *parent)
    self._noteCreation(QHttpServer, lambda: Rituals.call(
        'ritual_ZN11QHttpServerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QHttpServerPrivate]:
    """
    Calls Qt's 'QHttpServerPrivate *QHttpServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserver.html#d_func

    Returns
    -------

    Optional[QHttpServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerPrivate *QHttpServer::d_func()
    address = self.uglySide.call('ritual_ZN11QHttpServer6d_funcEv')
    from . import QHttpServerPrivate
    return QHttpServerPrivate._cuteAt(address)

  def router(self) -> Optional[QHttpServerRouter]:
    """
    Calls Qt's 'QHttpServerRouter *QHttpServer::router()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserver.html#router

    Returns
    -------

    Optional[QHttpServerRouter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerRouter *QHttpServer::router()
    address = self.uglySide.call('ritual_ZN11QHttpServer6routerEv')
    from . import QHttpServerRouter
    return QHttpServerRouter._cuteAt(address)

  def clearMissingHandler(self) -> None:
    """
    Calls Qt's 'void QHttpServer::clearMissingHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserver.html#clearMissingHandler
    """
    #  void QHttpServer::clearMissingHandler()
    self.uglySide.call('ritual_ZN11QHttpServer19clearMissingHandlerEv')

  @staticmethod
  def addAfterRequestHandler(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::addAfterRequestHandler': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServer.addAfterRequestHandler' has no cute function yet. "
        "Qt's 'QHttpServer::addAfterRequestHandler': a template: a pattern "
        "and no single function.")

  @staticmethod
  def addAfterRequestHandlerImpl(*__, **_) -> Never:
    """
    Qt's 'void QHttpServer::addAfterRequestHandlerImpl(const QObject
    *context, QtPrivate::QSlotObjectBase *handler)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpServer.addAfterRequestHandlerImpl' has no cute function yet. "
        "Qt's 'void QHttpServer::addAfterRequestHandlerImpl(const QObject "
        "*context, QtPrivate::QSlotObjectBase *handler)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def createRouteHandler(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::createRouteHandler': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServer.createRouteHandler' has no cute function yet. Qt's "
        "'QHttpServer::createRouteHandler': a template: a pattern and no "
        "single function.")

  @staticmethod
  def responseImpl(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::responseImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QHttpServer.responseImpl' has no cute function yet. Qt's "
        "'QHttpServer::responseImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def route(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::route': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QHttpServer.route' has no cute function yet. Qt's "
        "'QHttpServer::route': a template: a pattern and no single function."
    )

  @staticmethod
  def routeImpl(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::routeImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QHttpServer.routeImpl' has no cute function yet. Qt's "
        "'QHttpServer::routeImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def sendResponse(*__, **_) -> Never:
    """
    - Qt's 'void QHttpServer::sendResponse(QHttpServerResponse &&response,
      const QHttpServerRequest &request, QHttpServerResponder &&responder)':
      takes a type Python has no way to hand over yet.
    - Qt's 'void QHttpServer::sendResponse(QFuture<QHttpServerResponse>
      &&response, const QHttpServerRequest &request, QHttpServerResponder
      &&responder)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServer.sendResponse' has no cute function yet. Qt's 'void "
        "QHttpServer::sendResponse(QHttpServerResponse &&response, const "
        "QHttpServerRequest &request, QHttpServerResponder &&responder)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QHttpServer::sendResponse(QFuture<QHttpServerResponse> &&response, "
        "const QHttpServerRequest &request, QHttpServerResponder "
        "&&responder)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setMissingHandler(*__, **_) -> Never:
    """
    Qt's 'QHttpServer::setMissingHandler': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QHttpServer.setMissingHandler' has no cute function yet. Qt's "
        "'QHttpServer::setMissingHandler': a template: a pattern and no "
        "single function.")

  @staticmethod
  def setMissingHandlerImpl(*__, **_) -> Never:
    """
    Qt's 'void QHttpServer::setMissingHandlerImpl(const QObject *context,
    QtPrivate::QSlotObjectBase *handler)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpServer.setMissingHandlerImpl' has no cute function yet. Qt's "
        "'void QHttpServer::setMissingHandlerImpl(const QObject *context, "
        "QtPrivate::QSlotObjectBase *handler)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")
