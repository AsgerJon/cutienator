"""
QQmlTypeLoaderThread binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloaderthread_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlTypeLoaderThread to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlEngineExtensionInterface, QQmlExtensionInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngineExtensionInterface = WAIT['QQmlEngineExtensionInterface']
  QQmlExtensionInterface = WAIT['QQmlExtensionInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeLoaderThread(QQmlThread):
  """
  The cute side of Qt's QQmlTypeLoaderThread: a plain Python object standing
  in front of one C++ QQmlTypeLoaderThread.

  It is built on the cute 'QQmlThread', as Qt's QQmlTypeLoaderThread is built
  on Qt's QQmlThread, and has everything that class has.

  C++ hands a QQmlTypeLoaderThread around as a copy, so every C++
  QQmlTypeLoaderThread behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlTypeLoaderThread that has a ritual and that
  Python can call so far, 2 names in all: 'initializeExtensionMain',
  'initializeEngineExtensionMain'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeLoaderThread::~QQmlTypeLoaderThread()': the destructor:
    Python removes its C++ QQmlTypeLoaderThread by it, and has no other use
    for it.
  - Qt's 'void QQmlTypeLoaderThread::loadThread(const QQmlDataBlob::Ptr &b)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoaderThread::loadWithStaticDataThread(const
    QQmlDataBlob::Ptr &b, const QByteArray &a1)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlTypeLoaderThread::loadWithCachedUnitThread(const
    QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoaderThread::callCompletedMain(const
    QQmlDataBlob::Ptr &b)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlTypeLoaderThread::callDownloadProgressChangedMain(const
    QQmlDataBlob::Ptr &b, qreal p)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlTypeLoaderThread::dropThread(const QQmlDataBlob::Ptr &b)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  14 of the 23 functions Qt declares: 14 leans on 'QQmlThread.

  What to expect
  --------------

  - The C++ QQmlTypeLoaderThread is created at the first use, not by
    'QQmlTypeLoaderThread(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTypeLoaderThread back gives a copy the ritual
    made for Python, in a new cute QQmlTypeLoaderThread.
  - Each name of Qt's QQmlTypeLoaderThread that has no cute function yet,
    '__init__', 'callCompleted', 'callCompletedMain',
    'callDownloadProgressChanged', 'callDownloadProgressChangedMain', 'drop',
    'dropThread', 'initializeEngine', 'load', 'loadAsync', 'loadThread',
    'loadWithCachedUnit', 'loadWithCachedUnitAsync',
    'loadWithCachedUnitThread', 'loadWithStaticData',
    'loadWithStaticDataAsync', 'loadWithStaticDataThread',
    'networkAccessManager', 'networkReplyProxy', holds a function that raises
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
  __qt_class__ = 'QQmlTypeLoaderThread'

  #  Qt's '~QQmlTypeLoaderThread()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlTypeLoaderThread behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlTypeLoaderThreadD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoaderThread::QQmlTypeLoaderThread(QQmlTypeLoader
    *loader)': leans on 'QQmlThread::discardMessages()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.__init__' has no cute function yet. Qt's "
        "'QQmlTypeLoaderThread::QQmlTypeLoaderThread(QQmlTypeLoader "
        "*loader)': leans on 'QQmlThread::discardMessages()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QQmlExtensionInterface, str)
  @overload(QQmlExtensionInterface, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def initializeExtensionMain(
      self,
      iface: Optional[QQmlExtensionInterface],
      uri: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlTypeLoaderThread::initializeExtensionMain(QQmlExtensionInterface
    *iface, const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderthread.html#initializeExtensionMain

    Parameters
    ----------

    iface : Optional[QQmlExtensionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlTypeLoaderThread::initializeExtensionMain(
    #      QQmlExtensionInterface *iface, const char *uri)
    self.uglySide.call(
        'ritual_ZN20QQmlTypeLoaderThread23initializeExtensionMainEP22QQmlEx'
        'tensionInterfacePKc',
        self._addressOf(iface, 'QQmlExtensionInterface'), self._bytesOf(uri),
    )

  @overload(QQmlEngineExtensionInterface, str)
  @overload(QQmlEngineExtensionInterface, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def initializeEngineExtensionMain(
      self,
      iface: Optional[QQmlEngineExtensionInterface],
      uri: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeLoaderThread::initializeEngineExtensionMain(
    QQmlEngineExtensionInterface *iface, const char *uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderthread.html

    Parameters
    ----------

    iface : Optional[QQmlEngineExtensionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlTypeLoaderThread::initializeEngineExtensionMain(
    #      QQmlEngineExtensionInterface *iface, const char *uri)
    self.uglySide.call(
        'ritual_ZN20QQmlTypeLoaderThread29initializeEngineExtensionMainEP28'
        'QQmlEngineExtensionInterfacePKc',
        self._addressOf(iface, 'QQmlEngineExtensionInterface'),
        self._bytesOf(uri),
    )

  @staticmethod
  def callCompleted(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::callCompleted(const QQmlDataBlob::Ptr
    &b)': leans on
    'QQmlThread::internalPostMethodToMain(QQmlThread::Message*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.callCompleted' has no cute function yet. "
        "Qt's 'void QQmlTypeLoaderThread::callCompleted(const "
        "QQmlDataBlob::Ptr &b)': leans on "
        "'QQmlThread::internalPostMethodToMain(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def callCompletedMain(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::callCompletedMain(const
    QQmlDataBlob::Ptr &b)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.callCompletedMain' has no cute function yet. "
        "Qt's 'void QQmlTypeLoaderThread::callCompletedMain(const "
        "QQmlDataBlob::Ptr &b)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def callDownloadProgressChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::callDownloadProgressChanged(const
    QQmlDataBlob::Ptr &b, qreal p)': leans on
    'QQmlThread::internalPostMethodToMain(QQmlThread::Message*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.callDownloadProgressChanged' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::callDownloadProgressChanged(const "
        "QQmlDataBlob::Ptr &b, qreal p)': leans on "
        "'QQmlThread::internalPostMethodToMain(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def callDownloadProgressChangedMain(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::callDownloadProgressChangedMain(const
    QQmlDataBlob::Ptr &b, qreal p)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.callDownloadProgressChangedMain' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::callDownloadProgressChangedMain(const "
        "QQmlDataBlob::Ptr &b, qreal p)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def drop(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::drop(const QQmlDataBlob::Ptr &b)': leans
    on 'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.drop' has no cute function yet. Qt's 'void "
        "QQmlTypeLoaderThread::drop(const QQmlDataBlob::Ptr &b)': leans on "
        "'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def dropThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::dropThread(const QQmlDataBlob::Ptr &b)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.dropThread' has no cute function yet. Qt's "
        "'void QQmlTypeLoaderThread::dropThread(const QQmlDataBlob::Ptr "
        "&b)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def initializeEngine(*__, **_) -> Never:
    """
    - Qt's 'void
      QQmlTypeLoaderThread::initializeEngine(QQmlExtensionInterface *a0,
      const char *a1)': leans on
      'QQmlThread::internalCallMethodInMain(QQmlThread::Message*)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'void
      QQmlTypeLoaderThread::initializeEngine(QQmlEngineExtensionInterface
      *a0, const char *a1)': leans on
      'QQmlThread::internalCallMethodInMain(QQmlThread::Message*)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.initializeEngine' has no cute function yet. "
        "Qt's 'void "
        "QQmlTypeLoaderThread::initializeEngine(QQmlExtensionInterface *a0, "
        "const char *a1)': leans on "
        "'QQmlThread::internalCallMethodInMain(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'void "
        "QQmlTypeLoaderThread::initializeEngine(QQmlEngineExtensionInterface"
        " *a0, const char *a1)': leans on "
        "'QQmlThread::internalCallMethodInMain(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::load(const QQmlDataBlob::Ptr &b)': leans
    on 'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.load' has no cute function yet. Qt's 'void "
        "QQmlTypeLoaderThread::load(const QQmlDataBlob::Ptr &b)': leans on "
        "'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadAsync(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadAsync(const QQmlDataBlob::Ptr &b)':
    leans on 'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadAsync' has no cute function yet. Qt's "
        "'void QQmlTypeLoaderThread::loadAsync(const QQmlDataBlob::Ptr "
        "&b)': leans on "
        "'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadThread(const QQmlDataBlob::Ptr &b)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadThread' has no cute function yet. Qt's "
        "'void QQmlTypeLoaderThread::loadThread(const QQmlDataBlob::Ptr "
        "&b)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def loadWithCachedUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithCachedUnit(const
    QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': leans on
    'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithCachedUnit' has no cute function "
        "yet. Qt's 'void QQmlTypeLoaderThread::loadWithCachedUnit(const "
        "QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': "
        "leans on "
        "'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadWithCachedUnitAsync(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithCachedUnitAsync(const
    QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': leans on
    'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithCachedUnitAsync' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::loadWithCachedUnitAsync(const "
        "QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': "
        "leans on "
        "'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadWithCachedUnitThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithCachedUnitThread(const
    QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithCachedUnitThread' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::loadWithCachedUnitThread(const "
        "QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def loadWithStaticData(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithStaticData(const
    QQmlDataBlob::Ptr &b, const QByteArray &a1)': leans on
    'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithStaticData' has no cute function "
        "yet. Qt's 'void QQmlTypeLoaderThread::loadWithStaticData(const "
        "QQmlDataBlob::Ptr &b, const QByteArray &a1)': leans on "
        "'QQmlThread::internalCallMethodInThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadWithStaticDataAsync(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithStaticDataAsync(const
    QQmlDataBlob::Ptr &b, const QByteArray &a1)': leans on
    'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithStaticDataAsync' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::loadWithStaticDataAsync(const "
        "QQmlDataBlob::Ptr &b, const QByteArray &a1)': leans on "
        "'QQmlThread::internalPostMethodToThread(QQmlThread::Message*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadWithStaticDataThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderThread::loadWithStaticDataThread(const
    QQmlDataBlob::Ptr &b, const QByteArray &a1)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.loadWithStaticDataThread' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypeLoaderThread::loadWithStaticDataThread(const "
        "QQmlDataBlob::Ptr &b, const QByteArray &a1)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def networkAccessManager(*__, **_) -> Never:
    """
    Qt's 'QNetworkAccessManager *QQmlTypeLoaderThread::networkAccessManager()
    const': leans on 'QQmlThread::isThisThread() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.networkAccessManager' has no cute function "
        "yet. Qt's 'QNetworkAccessManager "
        "*QQmlTypeLoaderThread::networkAccessManager() const': leans on "
        "'QQmlThread::isThisThread() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def networkReplyProxy(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeLoaderNetworkReplyProxy
    *QQmlTypeLoaderThread::networkReplyProxy() const': leans on
    'QQmlThread::isThisThread() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderThread.networkReplyProxy' has no cute function yet. "
        "Qt's 'QQmlTypeLoaderNetworkReplyProxy "
        "*QQmlTypeLoaderThread::networkReplyProxy() const': leans on "
        "'QQmlThread::isThisThread() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
