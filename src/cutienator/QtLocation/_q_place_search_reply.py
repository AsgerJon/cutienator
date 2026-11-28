"""
QPlaceSearchReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacesearchreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlaceSearchRequest, QPlaceSearchResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']
  QPlaceSearchResult = WAIT['QPlaceSearchResult']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceSearchReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceSearchReply: a plain Python object standing in
  front of one C++ QPlaceSearchReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceSearchReply is built
  on Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceSearchReply that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'type', 'results',
  'request', 'previousPageRequest', 'nextPageRequest', 'setResults',
  'setRequest', 'setPreviousPageRequest', 'setNextPageRequest'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceSearchReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlaceSearchReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceSearchReply::~QPlaceSearchReply()': the destructor: Python
    never removes a C++ QPlaceSearchReply.
  - Qt's 'QPlaceSearchReplyPrivate *QPlaceSearchReply::d_func()': gives
    'QPlaceSearchReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceSearchReplyPrivate *QPlaceSearchReply::d_func() const':
    gives 'QPlaceSearchReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceSearchReply is created at the first use, not by
    'QPlaceSearchReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceSearchReply.
  - Qt tells when it has removed the C++ QPlaceSearchReply. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPlaceSearchReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#tr

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
    #  QString QPlaceSearchReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QPlaceSearchReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchReply'

  #  A C++ QPlaceSearchReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceSearchReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceSearchReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceSearchReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QPlaceSearchReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'QPlaceReply::Type QPlaceSearchReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  QPlaceReply::Type QPlaceSearchReply::type() const
    ritual = 'ritual_ZNK17QPlaceSearchReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPlaceSearchReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def results(self) -> QList[QPlaceSearchResult]:
    """
    Calls Qt's 'QList<QPlaceSearchResult> QPlaceSearchReply::results()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#results

    Returns
    -------

    QList[QPlaceSearchResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceSearchResult> QPlaceSearchReply::results() const
    address = self.uglySide.call('ritual_ZNK17QPlaceSearchReply7resultsEv')
    from . import QPlaceSearchResult
    return QList[QPlaceSearchResult]._cuteOwning(address)

  def request(self) -> QPlaceSearchRequest:
    """
    Calls Qt's 'QPlaceSearchRequest QPlaceSearchReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#request

    Returns
    -------

    QPlaceSearchRequest
      A new cute QPlaceSearchRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceSearchRequest QPlaceSearchReply::request() const
    address = self.uglySide.call('ritual_ZNK17QPlaceSearchReply7requestEv')
    from . import QPlaceSearchRequest
    return QPlaceSearchRequest._cuteOwning(address)

  def previousPageRequest(self) -> QPlaceSearchRequest:
    """
    Calls Qt's 'QPlaceSearchRequest QPlaceSearchReply::previousPageRequest()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreply.html#previousPageRequest

    Returns
    -------

    QPlaceSearchRequest
      A new cute QPlaceSearchRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceSearchRequest QPlaceSearchReply::previousPageRequest() const
    address = self.uglySide.call(
        'ritual_ZNK17QPlaceSearchReply19previousPageRequestEv',
    )
    from . import QPlaceSearchRequest
    return QPlaceSearchRequest._cuteOwning(address)

  def nextPageRequest(self) -> QPlaceSearchRequest:
    """
    Calls Qt's 'QPlaceSearchRequest QPlaceSearchReply::nextPageRequest()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreply.html#nextPageRequest

    Returns
    -------

    QPlaceSearchRequest
      A new cute QPlaceSearchRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceSearchRequest QPlaceSearchReply::nextPageRequest() const
    address = self.uglySide.call(
        'ritual_ZNK17QPlaceSearchReply15nextPageRequestEv',
    )
    from . import QPlaceSearchRequest
    return QPlaceSearchRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPlaceSearchResult])
  def setResults(self, results: QList[QPlaceSearchResult]) -> None:
    """
    Calls Qt's 'void QPlaceSearchReply::setResults(const
    QList<QPlaceSearchResult> &results)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#setResults

    Parameters
    ----------

    results : QList[QPlaceSearchResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceSearchReply::setResults(const QList<QPlaceSearchResult>
    #      &results)
    self.uglySide.call(
        'ritual_ZN17QPlaceSearchReply10setResultsERK5QListI18QPlaceSearchRe'
        'sultE',
        self._valueOf(results),
    )

  @overload(QPlaceSearchRequest)
  def setRequest(self, request: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void QPlaceSearchReply::setRequest(const QPlaceSearchRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchreply.html#setRequest

    Parameters
    ----------

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QPlaceSearchReply::setRequest(const QPlaceSearchRequest &request)
    self.uglySide.call(
        'ritual_ZN17QPlaceSearchReply10setRequestERK19QPlaceSearchRequest',
        self._valueOf(request),
    )

  @overload(QPlaceSearchRequest)
  def setPreviousPageRequest(self, previous: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void QPlaceSearchReply::setPreviousPageRequest(const
    QPlaceSearchRequest &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreply.html#setPreviousPageRequest

    Parameters
    ----------

    previous : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QPlaceSearchReply::setPreviousPageRequest(const
    #      QPlaceSearchRequest &previous)
    self.uglySide.call(
        'ritual_ZN17QPlaceSearchReply22setPreviousPageRequestERK19QPlaceSea'
        'rchRequest',
        self._valueOf(previous),
    )

  @overload(QPlaceSearchRequest)
  def setNextPageRequest(self, next: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void QPlaceSearchReply::setNextPageRequest(const
    QPlaceSearchRequest &next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreply.html#setNextPageRequest

    Parameters
    ----------

    next : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QPlaceSearchReply::setNextPageRequest(const QPlaceSearchRequest
    #      &next)
    self.uglySide.call(
        'ritual_ZN17QPlaceSearchReply18setNextPageRequestERK19QPlaceSearchR'
        'equest',
        self._valueOf(next),
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
    Notes what was given, for Qt's
    'QPlaceSearchReply::QPlaceSearchReply(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreply.html#QPlaceSearchReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceSearchReply::QPlaceSearchReply(QObject *parent)
    self._noteCreation(QPlaceSearchReply, lambda: Rituals.call(
        'ritual_ZN17QPlaceSearchReplyC1EP7QObject',
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
