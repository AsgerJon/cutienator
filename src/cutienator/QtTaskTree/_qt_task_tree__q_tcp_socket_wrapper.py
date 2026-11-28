"""
QtTaskTree::QTcpSocketWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtcpsocketwrappertask.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject
  from ..QtNetwork import QHostAddress, QTcpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QHostAddress = WAIT['QHostAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTcpSocketWrapper(QObject):
  """
  The cute side of Qt's QtTaskTree::QTcpSocketWrapper: a plain Python object
  standing in front of one C++ QtTaskTree::QTcpSocketWrapper.

  It is built on the cute 'QObject', as Qt's QtTaskTree::QTcpSocketWrapper is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QTcpSocketWrapper that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'setAddress', 'setPort', 'setData', 'socket', 'start', 'started', 'done',
  'event'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QTcpSocketWrapper::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtTaskTree::QTcpSocketWrapper::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtTaskTree::QTcpSocketWrapper::~QTcpSocketWrapper()': the
    destructor: Python never removes a C++ QtTaskTree::QTcpSocketWrapper.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtTaskTree::QTcpSocketWrapper is created at the first use, not by
    'QtTaskTree::QTcpSocketWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QTcpSocketWrapper.
  - Qt tells when it has removed the C++ QtTaskTree::QTcpSocketWrapper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QtTaskTree::QTcpSocketWrapper::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#tr

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
    #  QString QtTaskTree::QTcpSocketWrapper::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapper2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QTcpSocketWrapper'

  #  A C++ QtTaskTree::QTcpSocketWrapper Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtTaskTree_QTcpSocketWrapper'

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
    *QtTaskTree::QTcpSocketWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QTcpSocketWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree17QTcpSocketWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def socket(self) -> Optional[QTcpSocket]:
    """
    Calls Qt's 'QTcpSocket *QtTaskTree::QTcpSocketWrapper::socket() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#socket

    Returns
    -------

    Optional[QTcpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTcpSocket *QtTaskTree::QTcpSocketWrapper::socket() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree17QTcpSocketWrapper6socketEv',
    )
    from ..QtNetwork import QTcpSocket
    return QTcpSocket._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def setAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTcpSocketWrapper::setAddress(const
    QHostAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#setAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QtTaskTree::QTcpSocketWrapper::setAddress(const QHostAddress
    #      &address)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapper10setAddressERK12QHostAddr'
        'ess',
        self._valueOf(address),
    )

  @overload(int)
  def setPort(self, port: int) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTcpSocketWrapper::setPort(quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#setPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QtTaskTree::QTcpSocketWrapper::setPort(quint16 port)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapper7setPortEt', port,
    )

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTcpSocketWrapper::setData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QtTaskTree::QTcpSocketWrapper::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapper7setDataERK10QByteArray',
        self._valueOf(data),
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
    'QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html
    """
    #  QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper()
    self._noteCreation(QTcpSocketWrapper, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapperC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QTcpSocketWrapper::QTcpSocketWrapper(QObject *parent)
    self._noteCreation(QTcpSocketWrapper, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapperC1EP7QObject',
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
    Calls Qt's 'void QtTaskTree::QTcpSocketWrapper::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#start
    """
    #  void QtTaskTree::QTcpSocketWrapper::start()
    self.uglySide.call('ritual_ZN10QtTaskTree17QTcpSocketWrapper5startEv')

  def started(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTcpSocketWrapper::started()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#started
    """
    #  void QtTaskTree::QTcpSocketWrapper::started()
    self.uglySide.call('ritual_ZN10QtTaskTree17QTcpSocketWrapper7startedEv')

  @overload(QtTaskTree.DoneResult)
  def done(self, result: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QTcpSocketWrapper::done(QtTaskTree::DoneResult result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#done

    Parameters
    ----------

    result : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QTcpSocketWrapper::done(QtTaskTree::DoneResult
    #      result)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree17QTcpSocketWrapper4doneENS_10DoneResultE',
        result.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QTcpSocketWrapper::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtcpsocketwrapper.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QTcpSocketWrapper::event(QEvent *event)
    ritual = 'ritual_ZN10QtTaskTree17QTcpSocketWrapper5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QtTaskTree17QTcpSocketWrapper5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
