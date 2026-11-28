"""
QGeoCodeReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeocodereply.h, Qt 6.12.0. Changes made here are lost.
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
  from ..QtPositioning import QGeoLocation, QGeoShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoLocation = WAIT['QGeoLocation']
  QGeoShape = WAIT['QGeoShape']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoCodeReply(QObject):
  """
  The cute side of Qt's QGeoCodeReply: a plain Python object standing in
  front of one C++ QGeoCodeReply.

  It is built on the cute 'QObject', as Qt's QGeoCodeReply is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoCodeReply that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'isFinished', 'error',
  'errorString', 'viewport', 'locations', 'limit', 'offset', 'abort',
  'finished', 'aborted', 'errorOccurred', 'setError', 'setFinished',
  'setViewport', 'addLocation', 'setLocations', 'setLimit', 'setOffset'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoCodeReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGeoCodeReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoCodeReply::~QGeoCodeReply()': the destructor: Python never
    removes a C++ QGeoCodeReply.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoCodeReply is created at the first use, not by
    'QGeoCodeReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoCodeReply.
  - Qt tells when it has removed the C++ QGeoCodeReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGeoCodeReply, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoCodeReply::Error' of Qt, with the 7 names Qt gives in it.
    """

    NoError = Kee[int](0)
    EngineNotSetError = Kee[int](1)
    CommunicationError = Kee[int](2)
    ParseError = Kee[int](3)
    UnsupportedOptionError = Kee[int](4)
    CombinationError = Kee[int](5)
    UnknownError = Kee[int](6)

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
    Calls Qt's 'QString QGeoCodeReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#tr

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
    #  QString QGeoCodeReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QGeoCodeReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCodeReply'

  #  A C++ QGeoCodeReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoCodeReply'

  #  The functions Qt calls itself that QGeoCodeReply is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'abort': (
          ('_ZN13QGeoCodeReply5abortEv',
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
    Calls Qt's 'const QMetaObject *QGeoCodeReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoCodeReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QGeoCodeReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QGeoCodeReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#isFinished
    """
    #  bool QGeoCodeReply::isFinished() const
    return self.uglySide.call('ritual_ZNK13QGeoCodeReply10isFinishedEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoCodeReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoCodeReply::error() const
    return QGeoCodeReply.Error(self.uglySide.call(
        'ritual_ZNK13QGeoCodeReply5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QGeoCodeReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoCodeReply::errorString() const
    return self.uglySide.call('ritual_ZNK13QGeoCodeReply11errorStringEv')

  def viewport(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoCodeReply::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#viewport

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoCodeReply::viewport() const
    address = self.uglySide.call('ritual_ZNK13QGeoCodeReply8viewportEv')
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def locations(self) -> QList[QGeoLocation]:
    """
    Calls Qt's 'QList<QGeoLocation> QGeoCodeReply::locations() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#locations

    Returns
    -------

    QList[QGeoLocation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoLocation> QGeoCodeReply::locations() const
    address = self.uglySide.call('ritual_ZNK13QGeoCodeReply9locationsEv')
    from ..QtPositioning import QGeoLocation
    return QList[QGeoLocation]._cuteOwning(address)

  def limit(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoCodeReply::limit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#limit
    """
    #  qsizetype QGeoCodeReply::limit() const
    return self.uglySide.call('ritual_ZNK13QGeoCodeReply5limitEv')

  def offset(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoCodeReply::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#offset
    """
    #  qsizetype QGeoCodeReply::offset() const
    return self.uglySide.call('ritual_ZNK13QGeoCodeReply6offsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Error, str)
  def setError(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setError(Error error, const QString
    &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setError

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoCodeReply::setError(Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN13QGeoCodeReply8setErrorENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(bool)
  def setFinished(self, finished: bool) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setFinished(bool finished)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setFinished

    Parameters
    ----------

    finished : bool
      Passed on as it is.
    """
    #  void QGeoCodeReply::setFinished(bool finished)
    self.uglySide.call('ritual_ZN13QGeoCodeReply11setFinishedEb', finished)

  @overload(QGeoShape)
  def setViewport(self, viewport: QGeoShape) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setViewport(const QGeoShape &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setViewport

    Parameters
    ----------

    viewport : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QGeoCodeReply::setViewport(const QGeoShape &viewport)
    self.uglySide.call(
        'ritual_ZN13QGeoCodeReply11setViewportERK9QGeoShape',
        self._valueOf(viewport),
    )

  @overload(QList[QGeoLocation])
  def setLocations(self, locations: QList[QGeoLocation]) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setLocations(const QList<QGeoLocation>
    &locations)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setLocations

    Parameters
    ----------

    locations : QList[QGeoLocation]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoCodeReply::setLocations(const QList<QGeoLocation> &locations)
    self.uglySide.call(
        'ritual_ZN13QGeoCodeReply12setLocationsERK5QListI12QGeoLocationE',
        self._valueOf(locations),
    )

  @overload(int)
  def setLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setLimit(qsizetype limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QGeoCodeReply::setLimit(qsizetype limit)
    self.uglySide.call('ritual_ZN13QGeoCodeReply8setLimitEx', limit)

  @overload(int)
  def setOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::setOffset(qsizetype offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#setOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QGeoCodeReply::setOffset(qsizetype offset)
    self.uglySide.call('ritual_ZN13QGeoCodeReply9setOffsetEx', offset)

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
    Notes what was given, for Qt's 'QGeoCodeReply::QGeoCodeReply(Error error,
    const QString &errorString, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#QGeoCodeReply

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
    #  QGeoCodeReply::QGeoCodeReply(Error error, const QString &errorString,
    #      QObject *parent)
    self._noteCreation(QGeoCodeReply, lambda: Rituals.call(
        'ritual_ZN13QGeoCodeReplyC1ENS_5ErrorERK7QStringP7QObject',
        error.value, errorString, self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QGeoCodeReply::QGeoCodeReply(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#QGeoCodeReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoCodeReply::QGeoCodeReply(QObject *parent)
    self._noteCreation(QGeoCodeReply, lambda: Rituals.call(
        'ritual_ZN13QGeoCodeReplyC1EP7QObject',
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

  def abort(self) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#abort
    """
    #  void QGeoCodeReply::abort()
    ritual = 'ritual_ZN13QGeoCodeReply5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QGeoCodeReply5abortEv'
    self.uglySide.call(ritual)

  def finished(self) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#finished
    """
    #  void QGeoCodeReply::finished()
    self.uglySide.call('ritual_ZN13QGeoCodeReply8finishedEv')

  def aborted(self) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::aborted()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#aborted
    """
    #  void QGeoCodeReply::aborted()
    self.uglySide.call('ritual_ZN13QGeoCodeReply7abortedEv')

  @overload(Error)
  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str = '') -> None:
    """
    Calls Qt's 'void QGeoCodeReply::errorOccurred(QGeoCodeReply::Error error,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGeoCodeReply::errorOccurred(QGeoCodeReply::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN13QGeoCodeReply13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(QGeoLocation)
  def addLocation(self, location: QGeoLocation) -> None:
    """
    Calls Qt's 'void QGeoCodeReply::addLocation(const QGeoLocation
    &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocodereply.html#addLocation

    Parameters
    ----------

    location : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QGeoCodeReply::addLocation(const QGeoLocation &location)
    self.uglySide.call(
        'ritual_ZN13QGeoCodeReply11addLocationERK12QGeoLocation',
        self._valueOf(location),
    )
