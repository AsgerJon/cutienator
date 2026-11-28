"""
QtTaskTree::QNetworkReplyWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qnetworkreplywrappertask.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QtTaskTree
from ..QtNetwork import QNetworkAccessManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject
  from ..QtNetwork import QNetworkReply, QNetworkRequest, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QNetworkRequest = WAIT['QNetworkRequest']
  QSslError = WAIT['QSslError']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkReplyWrapper(QObject):
  """
  The cute side of Qt's QtTaskTree::QNetworkReplyWrapper: a plain Python
  object standing in front of one C++ QtTaskTree::QNetworkReplyWrapper.

  It is built on the cute 'QObject', as Qt's QtTaskTree::QNetworkReplyWrapper
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QNetworkReplyWrapper that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'setRequest', 'setOperation', 'setVerb', 'setData',
  'setNetworkAccessManager', 'reply', 'start', 'started', 'downloadProgress',
  'sslErrors', 'done', 'event'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QNetworkReplyWrapper::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtTaskTree::QNetworkReplyWrapper::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtTaskTree::QNetworkReplyWrapper::~QNetworkReplyWrapper()': the
    destructor: Python never removes a C++ QtTaskTree::QNetworkReplyWrapper.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtTaskTree::QNetworkReplyWrapper is created at the first use, not
    by 'QtTaskTree::QNetworkReplyWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QNetworkReplyWrapper.
  - Qt tells when it has removed the C++ QtTaskTree::QNetworkReplyWrapper.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QtTaskTree::QNetworkReplyWrapper::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#tr

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
    #  QString QtTaskTree::QNetworkReplyWrapper::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QNetworkReplyWrapper'

  #  A C++ QtTaskTree::QNetworkReplyWrapper Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtTaskTree_QNetworkReplyWrapper'

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
    *QtTaskTree::QNetworkReplyWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QNetworkReplyWrapper::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree20QNetworkReplyWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reply(self) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QtTaskTree::QNetworkReplyWrapper::reply()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#reply

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QtTaskTree::QNetworkReplyWrapper::reply() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree20QNetworkReplyWrapper5replyEv',
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkRequest)
  def setRequest(self, request: QNetworkRequest) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::setRequest(const
    QNetworkRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#setRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::setRequest(const
    #      QNetworkRequest &request)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper10setRequestERK15QNetwo'
        'rkRequest',
        self._valueOf(request),
    )

  @overload(QNetworkAccessManager.Operation)
  def setOperation(self, operation: QNetworkAccessManager.Operation) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QNetworkReplyWrapper::setOperation(QNetworkAccessManager::
    Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#setOperation

    Parameters
    ----------

    operation : QNetworkAccessManager.Operation
      Passed on as its number.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::setOperation(
    #      QNetworkAccessManager::Operation operation)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper12setOperationEN21QNetw'
        'orkAccessManager9OperationE',
        operation.value,
    )

  @overload(QByteArray)
  def setVerb(self, verb: QByteArray) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::setVerb(const
    QByteArray &verb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#setVerb

    Parameters
    ----------

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::setVerb(const QByteArray &verb)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper7setVerbERK10QByteArray',
        self._valueOf(verb),
    )

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::setData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper7setDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QNetworkAccessManager)
  @overload(NoneType)
  def setNetworkAccessManager(
      self,
      manager: Optional[QNetworkAccessManager],
  ) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QNetworkReplyWrapper::setNetworkAccessManager(
    QNetworkAccessManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::setNetworkAccessManager(
    #      QNetworkAccessManager *manager)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper23setNetworkAccessManag'
        'erEP21QNetworkAccessManager',
        self._addressOf(manager),
    )

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
    'QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html
    """
    #  QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper()
    self._noteCreation(QNetworkReplyWrapper, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapperC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QNetworkReplyWrapper::QNetworkReplyWrapper(QObject
    #      *parent)
    self._noteCreation(QNetworkReplyWrapper, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapperC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#start
    """
    #  void QtTaskTree::QNetworkReplyWrapper::start()
    self.uglySide.call('ritual_ZN10QtTaskTree20QNetworkReplyWrapper5startEv')

  def started(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::started()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#started
    """
    #  void QtTaskTree::QNetworkReplyWrapper::started()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper7startedEv',
    )

  @overload(int, int)
  def downloadProgress(self, bytesReceived: int, bytesTotal: int) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QNetworkReplyWrapper::downloadProgress(qint64 bytesReceived,
    qint64 bytesTotal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html

    Parameters
    ----------

    bytesReceived : int
      Passed on as it is.

    bytesTotal : int
      Passed on as it is.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::downloadProgress(qint64
    #      bytesReceived, qint64 bytesTotal)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper16downloadProgressExx',
        bytesReceived, bytesTotal,
    )

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QtTaskTree::QNetworkReplyWrapper::sslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::sslErrors(const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper9sslErrorsERK5QListI9QS'
        'slErrorE',
        self._valueOf(errors),
    )

  @overload(QtTaskTree.DoneResult)
  def done(self, result: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QNetworkReplyWrapper::done(QtTaskTree::DoneResult result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#done

    Parameters
    ----------

    result : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QNetworkReplyWrapper::done(QtTaskTree::DoneResult
    #      result)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree20QNetworkReplyWrapper4doneENS_10DoneResultE',
        result.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QNetworkReplyWrapper::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qnetworkreplywrapper.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QNetworkReplyWrapper::event(QEvent *event)
    ritual = 'ritual_ZN10QtTaskTree20QNetworkReplyWrapper5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QtTaskTree20QNetworkReplyWrapper5eventEP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(event))
