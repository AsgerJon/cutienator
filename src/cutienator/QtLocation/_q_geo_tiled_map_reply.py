"""
QGeoTiledMapReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapReply to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QGeoTileSpec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoTileSpec = WAIT['QGeoTileSpec']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMapReply(QObject):
  """
  The cute side of Qt's QGeoTiledMapReply: a plain Python object standing in
  front of one C++ QGeoTiledMapReply.

  It is built on the cute 'QObject', as Qt's QGeoTiledMapReply is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapReply that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'isFinished',
  'error', 'errorString', 'isCached', 'tileSpec', 'mapImageData',
  'mapImageFormat', 'abort', 'finished', 'aborted', 'errorOccurred',
  'setError', 'setFinished', 'setCached', 'setMapImageData',
  'setMapImageFormat'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoTiledMapReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoTiledMapReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGeoTiledMapReply::~QGeoTiledMapReply()': the destructor: Python
    never removes a C++ QGeoTiledMapReply.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoTiledMapReply is created at the first use, not by
    'QGeoTiledMapReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapReply.
  - Qt tells when it has removed the C++ QGeoTiledMapReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGeoTiledMapReply, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QGeoTiledMapReply::Error' of Qt, with the 4 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    CommunicationError = Kee[int](1)
    ParseError = Kee[int](2)
    UnknownError = Kee[int](3)

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
    Calls Qt's 'QString QGeoTiledMapReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#tr

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
    #  QString QGeoTiledMapReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGeoTiledMapReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapReply'

  #  A C++ QGeoTiledMapReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMapReply'

  #  The functions Qt calls itself that QGeoTiledMapReply is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'abort': (
          ('_ZN17QGeoTiledMapReply5abortEv',
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
    Calls Qt's 'const QMetaObject *QGeoTiledMapReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoTiledMapReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGeoTiledMapReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QGeoTiledMapReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#isFinished
    """
    #  bool QGeoTiledMapReply::isFinished() const
    return self.uglySide.call('ritual_ZNK17QGeoTiledMapReply10isFinishedEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QGeoTiledMapReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QGeoTiledMapReply::error() const
    return QGeoTiledMapReply.Error(self.uglySide.call(
        'ritual_ZNK17QGeoTiledMapReply5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QGeoTiledMapReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoTiledMapReply::errorString() const
    return self.uglySide.call('ritual_ZNK17QGeoTiledMapReply11errorStringEv')

  def isCached(self) -> bool:
    """
    Calls Qt's 'bool QGeoTiledMapReply::isCached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#isCached
    """
    #  bool QGeoTiledMapReply::isCached() const
    return self.uglySide.call('ritual_ZNK17QGeoTiledMapReply8isCachedEv')

  def tileSpec(self) -> QGeoTileSpec:
    """
    Calls Qt's 'QGeoTileSpec QGeoTiledMapReply::tileSpec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#tileSpec

    Returns
    -------

    QGeoTileSpec
      A new cute QGeoTileSpec around the copy Qt gave back. Python owns it.
    """
    #  QGeoTileSpec QGeoTiledMapReply::tileSpec() const
    address = self.uglySide.call('ritual_ZNK17QGeoTiledMapReply8tileSpecEv')
    from . import QGeoTileSpec
    return QGeoTileSpec._cuteOwning(address)

  def mapImageData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QGeoTiledMapReply::mapImageData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#mapImageData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QGeoTiledMapReply::mapImageData() const
    address = self.uglySide.call(
        'ritual_ZNK17QGeoTiledMapReply12mapImageDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mapImageFormat(self) -> str:
    """
    Calls Qt's 'QString QGeoTiledMapReply::mapImageFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#mapImageFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoTiledMapReply::mapImageFormat() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoTiledMapReply14mapImageFormatEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Error, str)
  def setError(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::setError(Error error, const QString
    &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#setError

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTiledMapReply::setError(Error error, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapReply8setErrorENS_5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(bool)
  def setFinished(self, finished: bool) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::setFinished(bool finished)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#setFinished

    Parameters
    ----------

    finished : bool
      Passed on as it is.
    """
    #  void QGeoTiledMapReply::setFinished(bool finished)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapReply11setFinishedEb', finished,
    )

  @overload(bool)
  def setCached(self, cached: bool) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::setCached(bool cached)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#setCached

    Parameters
    ----------

    cached : bool
      Passed on as it is.
    """
    #  void QGeoTiledMapReply::setCached(bool cached)
    self.uglySide.call('ritual_ZN17QGeoTiledMapReply9setCachedEb', cached)

  @overload(QByteArray)
  def setMapImageData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::setMapImageData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#setMapImageData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QGeoTiledMapReply::setMapImageData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapReply15setMapImageDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(str)
  def setMapImageFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::setMapImageFormat(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#setMapImageFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTiledMapReply::setMapImageFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapReply17setMapImageFormatERK7QString', format,
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

  @overload(QGeoTileSpec)
  @overload(QGeoTileSpec, QObject)
  @overload(QGeoTileSpec, NoneType)
  def __init__(
      self,
      spec: QGeoTileSpec,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTiledMapReply::QGeoTiledMapReply(const QGeoTileSpec &spec, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#QGeoTiledMapReply

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGeoTiledMapReply::QGeoTiledMapReply(const QGeoTileSpec &spec, QObject
    #      *parent)
    self._noteCreation(QGeoTiledMapReply, lambda: Rituals.call(
        'ritual_ZN17QGeoTiledMapReplyC1ERK12QGeoTileSpecP7QObject',
        self._valueOf(spec), self._addressOf(parent, 'QObject'),
    ))

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
    Notes what was given, for Qt's
    'QGeoTiledMapReply::QGeoTiledMapReply(Error error, const QString
    &errorString, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#QGeoTiledMapReply

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
    #  QGeoTiledMapReply::QGeoTiledMapReply(Error error, const QString
    #      &errorString, QObject *parent)
    self._noteCreation(QGeoTiledMapReply, lambda: Rituals.call(
        'ritual_ZN17QGeoTiledMapReplyC1ENS_5ErrorERK7QStringP7QObject',
        error.value, errorString, self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QGeoTiledMapReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#abort
    """
    #  void QGeoTiledMapReply::abort()
    ritual = 'ritual_ZN17QGeoTiledMapReply5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QGeoTiledMapReply5abortEv'
    self.uglySide.call(ritual)

  def finished(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#finished
    """
    #  void QGeoTiledMapReply::finished()
    self.uglySide.call('ritual_ZN17QGeoTiledMapReply8finishedEv')

  def aborted(self) -> None:
    """
    Calls Qt's 'void QGeoTiledMapReply::aborted()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotiledmapreply.html#aborted
    """
    #  void QGeoTiledMapReply::aborted()
    self.uglySide.call('ritual_ZN17QGeoTiledMapReply7abortedEv')

  @overload(Error)
  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str = '') -> None:
    """
    Calls Qt's 'void
    QGeoTiledMapReply::errorOccurred(QGeoTiledMapReply::Error error, const
    QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmapreply.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGeoTiledMapReply::errorOccurred(QGeoTiledMapReply::Error error,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN17QGeoTiledMapReply13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )
