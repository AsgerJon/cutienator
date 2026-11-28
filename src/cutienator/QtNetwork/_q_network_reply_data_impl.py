"""
QNetworkReplyDataImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplydataimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyDataImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QNetworkReplyDataImplPrivate


class QNetworkReplyDataImpl(QNetworkReply):
  """
  The cute side of Qt's QNetworkReplyDataImpl: a plain Python object standing
  in front of one C++ QNetworkReplyDataImpl.

  It is built on the cute 'QNetworkReply', as Qt's QNetworkReplyDataImpl is
  built on Qt's QNetworkReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyDataImpl that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'abort', 'close',
  'bytesAvailable', 'isSequential', 'size', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkReplyDataImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkReplyDataImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkReplyDataImpl::~QNetworkReplyDataImpl()': the destructor:
    Python never removes a C++ QNetworkReplyDataImpl.
  - Qt's 'qint64 QNetworkReplyDataImpl::readData(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'const QNetworkReplyDataImplPrivate *QNetworkReplyDataImpl::d_func()
    const': takes in Python what 'QNetworkReplyDataImplPrivate
    *QNetworkReplyDataImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 leans on
  'QNetworkReplyDataImpl.

  What to expect
  --------------

  - The C++ QNetworkReplyDataImpl is created at the first use, not by
    'QNetworkReplyDataImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyDataImpl.
  - Qt tells when it has removed the C++ QNetworkReplyDataImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkReplyDataImpl that has no cute function yet,
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
  __qt_class__ = 'QNetworkReplyDataImpl'

  #  A C++ QNetworkReplyDataImpl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyDataImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkReplyDataImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkReplyDataImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkReplyDataImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyDataImpl::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#bytesAvailable
    """
    #  qint64 QNetworkReplyDataImpl::bytesAvailable() const
    ritual = 'ritual_ZNK21QNetworkReplyDataImpl14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyDataImpl14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyDataImpl::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#isSequential
    """
    #  bool QNetworkReplyDataImpl::isSequential() const
    ritual = 'ritual_ZNK21QNetworkReplyDataImpl12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyDataImpl12isSequentialEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyDataImpl::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#size
    """
    #  qint64 QNetworkReplyDataImpl::size() const
    ritual = 'ritual_ZNK21QNetworkReplyDataImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyDataImpl4sizeEv'
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
    Qt's 'QNetworkReplyDataImpl::QNetworkReplyDataImpl(QObject *parent, const
    QNetworkRequest &req, const QNetworkAccessManager::Operation op)': leans
    on 'QNetworkReplyDataImpl::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyDataImpl.__init__' has no cute function yet. Qt's "
        "'QNetworkReplyDataImpl::QNetworkReplyDataImpl(QObject *parent, "
        "const QNetworkRequest &req, const QNetworkAccessManager::Operation "
        "op)': leans on "
        "'QNetworkReplyDataImpl::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QNetworkReplyDataImpl::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#abort
    """
    #  void QNetworkReplyDataImpl::abort()
    ritual = 'ritual_ZN21QNetworkReplyDataImpl5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkReplyDataImpl5abortEv'
    self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyDataImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#close
    """
    #  void QNetworkReplyDataImpl::close()
    ritual = 'ritual_ZN21QNetworkReplyDataImpl5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkReplyDataImpl5closeEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QNetworkReplyDataImplPrivate]:
    """
    Calls Qt's 'QNetworkReplyDataImplPrivate
    *QNetworkReplyDataImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplydataimpl.html#d_func

    Returns
    -------

    Optional[QNetworkReplyDataImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyDataImplPrivate *QNetworkReplyDataImpl::d_func()
    address = self.uglySide.call('ritual_ZN21QNetworkReplyDataImpl6d_funcEv')
    from . import QNetworkReplyDataImplPrivate
    return QNetworkReplyDataImplPrivate._cuteAt(address)
