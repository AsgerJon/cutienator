"""
QPlaceReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacereply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlaceReplyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceReplyPrivate = WAIT['QPlaceReplyPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceReply(QObject):
  """
  The cute side of Qt's QPlaceReply: a plain Python object standing in front
  of one C++ QPlaceReply.

  It is built on the cute 'QObject', as Qt's QPlaceReply is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceReply that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'isFinished', 'type',
  'errorString', 'error', 'abort', 'finished', 'contentUpdated', 'aborted',
  'errorOccurred', 'setFinished', 'setError'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPlaceReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceReply::~QPlaceReply()': the destructor: Python never removes
    a C++ QPlaceReply.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceReply is created at the first use, not by
    'QPlaceReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceReply.
  - Qt tells when it has removed the C++ QPlaceReply. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPlaceReply, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QPlaceReply::Error' of Qt, with the 10 names Qt gives in it.
    """

    NoError = Kee[int](0)
    PlaceDoesNotExistError = Kee[int](1)
    CategoryDoesNotExistError = Kee[int](2)
    CommunicationError = Kee[int](3)
    ParseError = Kee[int](4)
    PermissionsError = Kee[int](5)
    UnsupportedError = Kee[int](6)
    BadArgumentError = Kee[int](7)
    CancelError = Kee[int](8)
    UnknownError = Kee[int](9)

  class Type(CuteNum):
    """
    The enum 'QPlaceReply::Type' of Qt, with the 7 names Qt gives in it.
    """

    Reply = Kee[int](0)
    DetailsReply = Kee[int](1)
    SearchReply = Kee[int](2)
    SearchSuggestionReply = Kee[int](3)
    ContentReply = Kee[int](4)
    IdReply = Kee[int](5)
    MatchReply = Kee[int](6)

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
    Calls Qt's 'QString QPlaceReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#tr

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
    #  QString QPlaceReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QPlaceReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceReply'

  #  A C++ QPlaceReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceReply'

  #  The functions Qt calls itself that QPlaceReply is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK11QPlaceReply4typeEv',
           ('int', 'enum', 'QtLocation:QPlaceReply.Type'),
           ()),
      ),
      'abort': (
          ('_ZN11QPlaceReply5abortEv',
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
    Calls Qt's 'const QMetaObject *QPlaceReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QPlaceReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QPlaceReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#isFinished
    """
    #  bool QPlaceReply::isFinished() const
    return self.uglySide.call('ritual_ZNK11QPlaceReply10isFinishedEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QPlaceReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QPlaceReply::type() const
    ritual = 'ritual_ZNK11QPlaceReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QPlaceReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlaceReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceReply::errorString() const
    return self.uglySide.call('ritual_ZNK11QPlaceReply11errorStringEv')

  def error(self) -> Error:
    """
    Calls Qt's 'QPlaceReply::Error QPlaceReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  QPlaceReply::Error QPlaceReply::error() const
    return QPlaceReply.Error(self.uglySide.call(
        'ritual_ZNK11QPlaceReply5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFinished(self, finished: bool) -> None:
    """
    Calls Qt's 'void QPlaceReply::setFinished(bool finished)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#setFinished

    Parameters
    ----------

    finished : bool
      Passed on as it is.
    """
    #  void QPlaceReply::setFinished(bool finished)
    self.uglySide.call('ritual_ZN11QPlaceReply11setFinishedEb', finished)

  @overload(Error, str)
  def setError(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QPlaceReply::setError(QPlaceReply::Error error, const
    QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#setError

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceReply::setError(QPlaceReply::Error error, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN11QPlaceReply8setErrorENS_5ErrorERK7QString',
        error.value, errorString,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPlaceReply::QPlaceReply(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#QPlaceReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceReply::QPlaceReply(QObject *parent)
    self._noteCreation(QPlaceReply, lambda: Rituals.call(
        'ritual_ZN11QPlaceReplyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QPlaceReplyPrivate)
  @overload(QPlaceReplyPrivate, QObject)
  @overload(QPlaceReplyPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QPlaceReplyPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceReply::QPlaceReply(QPlaceReplyPrivate *a0, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#QPlaceReply

    Parameters
    ----------

    a0 : Optional[QPlaceReplyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceReply::QPlaceReply(QPlaceReplyPrivate *a0, QObject *parent)
    self._noteCreation(QPlaceReply, lambda: Rituals.call(
        'ritual_ZN11QPlaceReplyC1EP18QPlaceReplyPrivateP7QObject',
        self._addressOf(a0), self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QPlaceReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#abort
    """
    #  void QPlaceReply::abort()
    ritual = 'ritual_ZN11QPlaceReply5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QPlaceReply5abortEv'
    self.uglySide.call(ritual)

  def finished(self) -> None:
    """
    Calls Qt's 'void QPlaceReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#finished
    """
    #  void QPlaceReply::finished()
    self.uglySide.call('ritual_ZN11QPlaceReply8finishedEv')

  def contentUpdated(self) -> None:
    """
    Calls Qt's 'void QPlaceReply::contentUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#contentUpdated
    """
    #  void QPlaceReply::contentUpdated()
    self.uglySide.call('ritual_ZN11QPlaceReply14contentUpdatedEv')

  def aborted(self) -> None:
    """
    Calls Qt's 'void QPlaceReply::aborted()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#aborted
    """
    #  void QPlaceReply::aborted()
    self.uglySide.call('ritual_ZN11QPlaceReply7abortedEv')

  @overload(Error)
  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str = '') -> None:
    """
    Calls Qt's 'void QPlaceReply::errorOccurred(QPlaceReply::Error error,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacereply.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QPlaceReply::errorOccurred(QPlaceReply::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN11QPlaceReply13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )
