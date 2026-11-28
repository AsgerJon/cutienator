"""
Qt3DCore::QDownloadNetworkWorker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadnetworkworker_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QDownloadNetworkWorker to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtNetwork import QNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkReply = WAIT['QNetworkReply']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDownloadNetworkWorker(QObject):
  """
  The cute side of Qt's Qt3DCore::QDownloadNetworkWorker: a plain Python
  object standing in front of one C++ Qt3DCore::QDownloadNetworkWorker.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QDownloadNetworkWorker
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QDownloadNetworkWorker that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject',
  'cancelAllRequests', 'onAllRequestsCancelled', 'onRequestFinished',
  'onDownloadProgressed'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QDownloadNetworkWorker::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QDownloadNetworkWorker::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void Qt3DCore::QDownloadNetworkWorker::submitRequest(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void Qt3DCore::QDownloadNetworkWorker::cancelRequest(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void Qt3DCore::QDownloadNetworkWorker::onRequestSubmited(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void Qt3DCore::QDownloadNetworkWorker::onRequestCancelled(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DCore::QDownloadNetworkWorker is created at the first use, not
    by 'Qt3DCore::QDownloadNetworkWorker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QDownloadNetworkWorker.
  - Qt tells when it has removed the C++ Qt3DCore::QDownloadNetworkWorker.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QDownloadNetworkWorker that has no cute
    function yet, '__init__', 'cancelRequest', 'onRequestCancelled',
    'onRequestSubmited', 'requestDownloaded', 'submitRequest', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QDownloadNetworkWorker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QDownloadNetworkWorker::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadnetworkworker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QDownloadNetworkWorker::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore22QDownloadNetworkWorker10metaObjectEv',
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
    Qt's 'Qt3DCore::QDownloadNetworkWorker::QDownloadNetworkWorker(QObject
    *parent)': leans on 'Qt3DCore::QDownloadNetworkWorker::cancelRequest(
    QSharedPointer<Qt3DCore::QDownloadRequest> const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DCore::QDownloadNetworkWorker::QDownloadNetworkWorker(QObject "
        "*parent)': leans on "
        "'Qt3DCore::QDownloadNetworkWorker::cancelRequest(QSharedPointer<Qt3"
        "DCore::QDownloadRequest> const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def cancelAllRequests(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QDownloadNetworkWorker::cancelAllRequests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadnetworkworker.html
    """
    #  void Qt3DCore::QDownloadNetworkWorker::cancelAllRequests()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QDownloadNetworkWorker17cancelAllRequestsEv',
    )

  def onAllRequestsCancelled(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QDownloadNetworkWorker::onAllRequestsCancelled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadnetworkworker.html
    """
    #  void Qt3DCore::QDownloadNetworkWorker::onAllRequestsCancelled()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QDownloadNetworkWorker22onAllRequestsCancelled'
        'Ev',
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def onRequestFinished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QDownloadNetworkWorker::onRequestFinished(QNetworkReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadnetworkworker.html

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QDownloadNetworkWorker::onRequestFinished(QNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QDownloadNetworkWorker17onRequestFinishedEP13Q'
        'NetworkReply',
        self._addressOf(reply),
    )

  @overload(int, int)
  def onDownloadProgressed(
      self,
      bytesReceived: int,
      bytesTotal: int,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QDownloadNetworkWorker::onDownloadProgressed(qint64
    bytesReceived, qint64 bytesTotal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadnetworkworker.html

    Parameters
    ----------

    bytesReceived : int
      Passed on as it is.

    bytesTotal : int
      Passed on as it is.
    """
    #  void Qt3DCore::QDownloadNetworkWorker::onDownloadProgressed(qint64
    #      bytesReceived, qint64 bytesTotal)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QDownloadNetworkWorker20onDownloadProgressedEx'
        'x',
        bytesReceived, bytesTotal,
    )

  @staticmethod
  def cancelRequest(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadNetworkWorker::cancelRequest(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.cancelRequest' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadNetworkWorker::cancelRequest(const "
        "Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def onRequestCancelled(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadNetworkWorker::onRequestCancelled(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.onRequestCancelled' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadNetworkWorker::onRequestCancelled(const "
        "Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def onRequestSubmited(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadNetworkWorker::onRequestSubmited(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.onRequestSubmited' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadNetworkWorker::onRequestSubmited(const "
        "Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def requestDownloaded(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.requestDownloaded' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const "
        "Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def submitRequest(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QDownloadNetworkWorker::submitRequest(const
    Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDownloadNetworkWorker.submitRequest' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QDownloadNetworkWorker::submitRequest(const "
        "Qt3DCore::QDownloadRequestPtr &request)': takes a type Python has "
        "no way to hand over yet.")
