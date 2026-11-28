"""
QPlaceContentReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacecontentreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlaceContent, QPlaceContentRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceContent = WAIT['QPlaceContent']
  QPlaceContentRequest = WAIT['QPlaceContentRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceContentReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceContentReply: a plain Python object standing in
  front of one C++ QPlaceContentReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceContentReply is built
  on Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceContentReply that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'type', 'content',
  'totalCount', 'request', 'previousPageRequest', 'nextPageRequest',
  'setContent', 'setTotalCount', 'setRequest', 'setPreviousPageRequest',
  'setNextPageRequest'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceContentReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlaceContentReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceContentReply::~QPlaceContentReply()': the destructor: Python
    never removes a C++ QPlaceContentReply.
  - Qt's 'QPlaceContentReplyPrivate *QPlaceContentReply::d_func()': gives
    'QPlaceContentReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceContentReplyPrivate *QPlaceContentReply::d_func()
    const': gives 'QPlaceContentReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceContentReply is created at the first use, not by
    'QPlaceContentReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceContentReply.
  - Qt tells when it has removed the C++ QPlaceContentReply. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPlaceContentReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#tr

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
    #  QString QPlaceContentReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPlaceContentReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceContentReply'

  #  A C++ QPlaceContentReply Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceContentReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceContentReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceContentReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlaceContentReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'QPlaceReply::Type QPlaceContentReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  QPlaceReply::Type QPlaceContentReply::type() const
    ritual = 'ritual_ZNK18QPlaceContentReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPlaceContentReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def content(self) -> QMap[int, QPlaceContent]:
    """
    Calls Qt's 'QPlaceContent::Collection QPlaceContentReply::content()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#content

    Returns
    -------

    QMap[int, QPlaceContent]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QPlaceContent::Collection QPlaceContentReply::content() const
    address = self.uglySide.call('ritual_ZNK18QPlaceContentReply7contentEv')
    from . import QPlaceContent
    return QMap[int, QPlaceContent]._cuteOwning(address)

  def totalCount(self) -> int:
    """
    Calls Qt's 'int QPlaceContentReply::totalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#totalCount
    """
    #  int QPlaceContentReply::totalCount() const
    return self.uglySide.call('ritual_ZNK18QPlaceContentReply10totalCountEv')

  def request(self) -> QPlaceContentRequest:
    """
    Calls Qt's 'QPlaceContentRequest QPlaceContentReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#request

    Returns
    -------

    QPlaceContentRequest
      A new cute QPlaceContentRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceContentRequest QPlaceContentReply::request() const
    address = self.uglySide.call('ritual_ZNK18QPlaceContentReply7requestEv')
    from . import QPlaceContentRequest
    return QPlaceContentRequest._cuteOwning(address)

  def previousPageRequest(self) -> QPlaceContentRequest:
    """
    Calls Qt's 'QPlaceContentRequest
    QPlaceContentReply::previousPageRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#previousPageRequest

    Returns
    -------

    QPlaceContentRequest
      A new cute QPlaceContentRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceContentRequest QPlaceContentReply::previousPageRequest() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlaceContentReply19previousPageRequestEv',
    )
    from . import QPlaceContentRequest
    return QPlaceContentRequest._cuteOwning(address)

  def nextPageRequest(self) -> QPlaceContentRequest:
    """
    Calls Qt's 'QPlaceContentRequest QPlaceContentReply::nextPageRequest()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#nextPageRequest

    Returns
    -------

    QPlaceContentRequest
      A new cute QPlaceContentRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceContentRequest QPlaceContentReply::nextPageRequest() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlaceContentReply15nextPageRequestEv',
    )
    from . import QPlaceContentRequest
    return QPlaceContentRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[int, QPlaceContent])
  def setContent(self, content: QMap[int, QPlaceContent]) -> None:
    """
    Calls Qt's 'void QPlaceContentReply::setContent(const
    QPlaceContent::Collection &content)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#setContent

    Parameters
    ----------

    content : QMap[int, QPlaceContent]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QPlaceContentReply::setContent(const QPlaceContent::Collection
    #      &content)
    self.uglySide.call(
        'ritual_ZN18QPlaceContentReply10setContentERK4QMapIi13QPlaceContent'
        'E',
        self._valueOf(content),
    )

  @overload(int)
  def setTotalCount(self, total: int) -> None:
    """
    Calls Qt's 'void QPlaceContentReply::setTotalCount(int total)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#setTotalCount

    Parameters
    ----------

    total : int
      Passed on as it is.
    """
    #  void QPlaceContentReply::setTotalCount(int total)
    self.uglySide.call(
        'ritual_ZN18QPlaceContentReply13setTotalCountEi', total,
    )

  @overload(QPlaceContentRequest)
  def setRequest(self, request: QPlaceContentRequest) -> None:
    """
    Calls Qt's 'void QPlaceContentReply::setRequest(const
    QPlaceContentRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentreply.html#setRequest

    Parameters
    ----------

    request : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  void QPlaceContentReply::setRequest(const QPlaceContentRequest
    #      &request)
    self.uglySide.call(
        'ritual_ZN18QPlaceContentReply10setRequestERK20QPlaceContentRequest',
        self._valueOf(request),
    )

  @overload(QPlaceContentRequest)
  def setPreviousPageRequest(self, previous: QPlaceContentRequest) -> None:
    """
    Calls Qt's 'void QPlaceContentReply::setPreviousPageRequest(const
    QPlaceContentRequest &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#setPreviousPageRequest

    Parameters
    ----------

    previous : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  void QPlaceContentReply::setPreviousPageRequest(const
    #      QPlaceContentRequest &previous)
    self.uglySide.call(
        'ritual_ZN18QPlaceContentReply22setPreviousPageRequestERK20QPlaceCo'
        'ntentRequest',
        self._valueOf(previous),
    )

  @overload(QPlaceContentRequest)
  def setNextPageRequest(self, next: QPlaceContentRequest) -> None:
    """
    Calls Qt's 'void QPlaceContentReply::setNextPageRequest(const
    QPlaceContentRequest &next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#setNextPageRequest

    Parameters
    ----------

    next : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  void QPlaceContentReply::setNextPageRequest(const QPlaceContentRequest
    #      &next)
    self.uglySide.call(
        'ritual_ZN18QPlaceContentReply18setNextPageRequestERK20QPlaceConten'
        'tRequest',
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
    'QPlaceContentReply::QPlaceContentReply(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentreply.html#QPlaceContentReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceContentReply::QPlaceContentReply(QObject *parent)
    self._noteCreation(QPlaceContentReply, lambda: Rituals.call(
        'ritual_ZN18QPlaceContentReplyC1EP7QObject',
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
