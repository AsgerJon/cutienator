"""
QNetworkReplyFileImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyfileimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyFileImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QNetworkReplyFileImplPrivate


class QNetworkReplyFileImpl(QNetworkReply):
  """
  The cute side of Qt's QNetworkReplyFileImpl: a plain Python object standing
  in front of one C++ QNetworkReplyFileImpl.

  It is built on the cute 'QNetworkReply', as Qt's QNetworkReplyFileImpl is
  built on Qt's QNetworkReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyFileImpl that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'abort', 'close',
  'bytesAvailable', 'isSequential', 'size', 'fileOpenFinished', 'd_func'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkReplyFileImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkReplyFileImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkReplyFileImpl::~QNetworkReplyFileImpl()': the destructor:
    Python never removes a C++ QNetworkReplyFileImpl.
  - Qt's 'qint64 QNetworkReplyFileImpl::readData(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'const QNetworkReplyFileImplPrivate *QNetworkReplyFileImpl::d_func()
    const': takes in Python what 'QNetworkReplyFileImplPrivate
    *QNetworkReplyFileImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 1 leans on
  'QNetworkReplyFileImpl; 1 leans on 'QNetworkFile.

  What to expect
  --------------

  - The C++ QNetworkReplyFileImpl is created at the first use, not by
    'QNetworkReplyFileImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyFileImpl.
  - Qt tells when it has removed the C++ QNetworkReplyFileImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkReplyFileImpl that has no cute function yet,
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
  __qt_class__ = 'QNetworkReplyFileImpl'

  #  A C++ QNetworkReplyFileImpl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyFileImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkReplyFileImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkReplyFileImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkReplyFileImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyFileImpl::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#bytesAvailable
    """
    #  qint64 QNetworkReplyFileImpl::bytesAvailable() const
    ritual = 'ritual_ZNK21QNetworkReplyFileImpl14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyFileImpl14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyFileImpl::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#isSequential
    """
    #  bool QNetworkReplyFileImpl::isSequential() const
    ritual = 'ritual_ZNK21QNetworkReplyFileImpl12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyFileImpl12isSequentialEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyFileImpl::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#size
    """
    #  qint64 QNetworkReplyFileImpl::size() const
    ritual = 'ritual_ZNK21QNetworkReplyFileImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyFileImpl4sizeEv'
    return self.uglySide.call(ritual)

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
    Qt's 'QNetworkReplyFileImpl::QNetworkReplyFileImpl(QNetworkAccessManager
    *manager, const QNetworkRequest &req, const
    QNetworkAccessManager::Operation op)': leans on
    'QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader, QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyFileImpl.__init__' has no cute function yet. Qt's "
        "'QNetworkReplyFileImpl::QNetworkReplyFileImpl(QNetworkAccessManager"
        " *manager, const QNetworkRequest &req, const "
        "QNetworkAccessManager::Operation op)': leans on "
        "'QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader, "
        "QByteArray const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def abort(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyFileImpl::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#abort
    """
    #  void QNetworkReplyFileImpl::abort()
    ritual = 'ritual_ZN21QNetworkReplyFileImpl5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkReplyFileImpl5abortEv'
    self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyFileImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#close
    """
    #  void QNetworkReplyFileImpl::close()
    ritual = 'ritual_ZN21QNetworkReplyFileImpl5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkReplyFileImpl5closeEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def fileOpenFinished(self, isOpen: bool) -> None:
    """
    Calls Qt's 'void QNetworkReplyFileImpl::fileOpenFinished(bool isOpen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#fileOpenFinished

    Parameters
    ----------

    isOpen : bool
      Passed on as it is.
    """
    #  void QNetworkReplyFileImpl::fileOpenFinished(bool isOpen)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyFileImpl16fileOpenFinishedEb', isOpen,
    )

  def d_func(self) -> Optional[QNetworkReplyFileImplPrivate]:
    """
    Calls Qt's 'QNetworkReplyFileImplPrivate
    *QNetworkReplyFileImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyfileimpl.html#d_func

    Returns
    -------

    Optional[QNetworkReplyFileImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyFileImplPrivate *QNetworkReplyFileImpl::d_func()
    address = self.uglySide.call('ritual_ZN21QNetworkReplyFileImpl6d_funcEv')
    from . import QNetworkReplyFileImplPrivate
    return QNetworkReplyFileImplPrivate._cuteAt(address)
