"""
QGeoRouteReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoroutereply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QGeoRoute, QGeoRouteRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoRoute = WAIT['QGeoRoute']
  QGeoRouteRequest = WAIT['QGeoRouteRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoRouteReply(QObject):
  """
  The cute side of Qt's QGeoRouteReply: a plain Python object standing in
  front of one C++ QGeoRouteReply.

  It is built on the cute 'QObject', as Qt's QGeoRouteReply is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoRouteReply that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'isFinished', 'error',
  'errorString', 'request', 'routes', 'abort', 'finished', 'aborted',
  'errorOccurred', 'setError', 'setFinished', 'setRoutes', 'addRoutes'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoRouteReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGeoRouteReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoRouteReply::~QGeoRouteReply()': the destructor: Python never
    removes a C++ QGeoRouteReply.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoRouteReply is created at the first use, not by
    'QGeoRouteReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoRouteReply.
  - Qt tells when it has removed the C++ QGeoRouteReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGeoRouteReply, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoRouteReply::Error' of Qt, with the 6 names Qt gives in it.
    """

    NoError = Kee[int](0)
    EngineNotSetError = Kee[int](1)
    CommunicationError = Kee[int](2)
    ParseError = Kee[int](3)
    UnsupportedOptionError = Kee[int](4)
    UnknownError = Kee[int](5)

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
    Calls Qt's 'QString QGeoRouteReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#tr

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
    #  QString QGeoRouteReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QGeoRouteReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteReply'

  #  A C++ QGeoRouteReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoRouteReply'

  #  The functions Qt calls itself that QGeoRouteReply is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'abort': (
          ('_ZN14QGeoRouteReply5abortEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
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
    Calls Qt's 'const QMetaObject *QGeoRouteReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoRouteReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QGeoRouteReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QGeoRouteReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#isFinished
    """
    #  bool QGeoRouteReply::isFinished() const
    return self.uglySide.call('ritual_ZNK14QGeoRouteReply10isFinishedEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoRouteReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoRouteReply::error() const
    return QGeoRouteReply.Error(self.uglySide.call(
        'ritual_ZNK14QGeoRouteReply5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QGeoRouteReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRouteReply::errorString() const
    return self.uglySide.call('ritual_ZNK14QGeoRouteReply11errorStringEv')

  def request(self) -> QGeoRouteRequest:
    """
    Calls Qt's 'QGeoRouteRequest QGeoRouteReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#request

    Returns
    -------

    QGeoRouteRequest
      A new cute QGeoRouteRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteRequest QGeoRouteReply::request() const
    address = self.uglySide.call('ritual_ZNK14QGeoRouteReply7requestEv')
    from . import QGeoRouteRequest
    return QGeoRouteRequest._cuteOwning(address)

  def routes(self) -> QList[QGeoRoute]:
    """
    Calls Qt's 'QList<QGeoRoute> QGeoRouteReply::routes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#routes

    Returns
    -------

    QList[QGeoRoute]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoRoute> QGeoRouteReply::routes() const
    address = self.uglySide.call('ritual_ZNK14QGeoRouteReply6routesEv')
    from . import QGeoRoute
    return QList[QGeoRoute]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Error, str)
  def setError(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::setError(Error error, const QString
    &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#setError

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoRouteReply::setError(Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QGeoRouteReply8setErrorENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(bool)
  def setFinished(self, finished: bool) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::setFinished(bool finished)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#setFinished

    Parameters
    ----------

    finished : bool
      Passed on as it is.
    """
    #  void QGeoRouteReply::setFinished(bool finished)
    self.uglySide.call('ritual_ZN14QGeoRouteReply11setFinishedEb', finished)

  @overload(QList[QGeoRoute])
  def setRoutes(self, routes: QList[QGeoRoute]) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::setRoutes(const QList<QGeoRoute>
    &routes)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#setRoutes

    Parameters
    ----------

    routes : QList[QGeoRoute]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteReply::setRoutes(const QList<QGeoRoute> &routes)
    self.uglySide.call(
        'ritual_ZN14QGeoRouteReply9setRoutesERK5QListI9QGeoRouteE',
        self._valueOf(routes),
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

  @overload(Error, str)
  @overload(Error, str, QObject)
  @overload(Error, str, NoneType)
  def __init__(
      self,
      error: Error,
      errorString: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteReply::QGeoRouteReply(Error
    error, const QString &errorString, QObject *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#QGeoRouteReply

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoRouteReply::QGeoRouteReply(Error error, const QString
    #      &errorString, QObject *parent)
    self._noteCreation(QGeoRouteReply, lambda: Rituals.call(
        'ritual_ZN14QGeoRouteReplyC1ENS_5ErrorERK7QStringP7QObject',
        error.value, errorString, self._addressOf(parent, 'QObject'),
    ))

  @overload(QGeoRouteRequest)
  @overload(QGeoRouteRequest, QObject)
  @overload(QGeoRouteRequest, NoneType)
  def __init__(
      self,
      request: QGeoRouteRequest,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteReply::QGeoRouteReply(const
    QGeoRouteRequest &request, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#QGeoRouteReply

    Parameters
    ----------

    request : QGeoRouteRequest
      Passed on as a value: Qt reads the C++ QGeoRouteRequest, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoRouteReply::QGeoRouteReply(const QGeoRouteRequest &request,
    #      QObject *parent)
    self._noteCreation(QGeoRouteReply, lambda: Rituals.call(
        'ritual_ZN14QGeoRouteReplyC1ERK16QGeoRouteRequestP7QObject',
        self._valueOf(request), self._addressOf(parent, 'QObject'),
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

  def abort(self) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#abort
    """
    #  void QGeoRouteReply::abort()
    ritual = 'ritual_ZN14QGeoRouteReply5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QGeoRouteReply5abortEv'
    self.uglySide.call(ritual)

  def finished(self) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#finished
    """
    #  void QGeoRouteReply::finished()
    self.uglySide.call('ritual_ZN14QGeoRouteReply8finishedEv')

  def aborted(self) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::aborted()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#aborted
    """
    #  void QGeoRouteReply::aborted()
    self.uglySide.call('ritual_ZN14QGeoRouteReply7abortedEv')

  @overload(Error)
  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str = '') -> None:
    """
    Calls Qt's 'void QGeoRouteReply::errorOccurred(QGeoRouteReply::Error
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGeoRouteReply::errorOccurred(QGeoRouteReply::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QGeoRouteReply13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(QList[QGeoRoute])
  def addRoutes(self, routes: QList[QGeoRoute]) -> None:
    """
    Calls Qt's 'void QGeoRouteReply::addRoutes(const QList<QGeoRoute>
    &routes)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutereply.html#addRoutes

    Parameters
    ----------

    routes : QList[QGeoRoute]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteReply::addRoutes(const QList<QGeoRoute> &routes)
    self.uglySide.call(
        'ritual_ZN14QGeoRouteReply9addRoutesERK5QListI9QGeoRouteE',
        self._valueOf(routes),
    )
