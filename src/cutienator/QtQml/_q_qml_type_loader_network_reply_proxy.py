"""
QQmlTypeLoaderNetworkReplyProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlTypeLoaderNetworkReplyProxy to be private: it declares the
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


class QQmlTypeLoaderNetworkReplyProxy(QObject):
  """
  The cute side of Qt's QQmlTypeLoaderNetworkReplyProxy: a plain Python
  object standing in front of one C++ QQmlTypeLoaderNetworkReplyProxy.

  It is built on the cute 'QObject', as Qt's QQmlTypeLoaderNetworkReplyProxy
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTypeLoaderNetworkReplyProxy that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject', 'finished',
  'downloadProgress', 'manualFinished'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlTypeLoaderNetworkReplyProxy::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQmlTypeLoaderNetworkReplyProxy::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 1 leans on
  'QQmlTypeLoaderNetworkReplyProxy; 1 leans on 'vtable for
  QQmlTypeLoaderNetworkReplyProxy', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlTypeLoaderNetworkReplyProxy is created at the first use, not
    by 'QQmlTypeLoaderNetworkReplyProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeLoaderNetworkReplyProxy.
  - Qt tells when it has removed the C++ QQmlTypeLoaderNetworkReplyProxy.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlTypeLoaderNetworkReplyProxy that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QQmlTypeLoaderNetworkReplyProxy'

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
    *QQmlTypeLoaderNetworkReplyProxy::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloadernetworkreplyproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTypeLoaderNetworkReplyProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQmlTypeLoaderNetworkReplyProxy10metaObjectEv',
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
    Qt's 'QQmlTypeLoaderNetworkReplyProxy::QQmlTypeLoaderNetworkReplyProxy(
    QQmlTypeLoader *l, QObject *parent)': leans on 'vtable for
    QQmlTypeLoaderNetworkReplyProxy', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderNetworkReplyProxy.__init__' has no cute function "
        "yet. Qt's "
        "'QQmlTypeLoaderNetworkReplyProxy::QQmlTypeLoaderNetworkReplyProxy(Q"
        "QmlTypeLoader *l, QObject *parent)': leans on 'vtable for "
        "QQmlTypeLoaderNetworkReplyProxy', which Qt's source does not mark "
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

  def finished(self) -> None:
    """
    Calls Qt's 'void QQmlTypeLoaderNetworkReplyProxy::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloadernetworkreplyproxy.html#finished
    """
    #  void QQmlTypeLoaderNetworkReplyProxy::finished()
    self.uglySide.call(
        'ritual_ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv',
    )

  @overload(int, int)
  def downloadProgress(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64
    a0, qint64 a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloadernetworkreplyproxy.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 a0,
    #      qint64 a1)
    self.uglySide.call(
        'ritual_ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx',
        a0, a1,
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def manualFinished(self, a0: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloadernetworkreplyproxy.html

    Parameters
    ----------

    a0 : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply
    #      *a0)
    self.uglySide.call(
        'ritual_ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNet'
        'workReply',
        self._addressOf(a0),
    )
