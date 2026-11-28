"""
QWebEngineNewWindowRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginenewwindowrequest.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QUrl
  from . import QWebEnginePage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEnginePage = WAIT['QWebEnginePage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineNewWindowRequest(QObject):
  """
  The cute side of Qt's QWebEngineNewWindowRequest: a plain Python object
  standing in front of one C++ QWebEngineNewWindowRequest.

  It is built on the cute 'QObject', as Qt's QWebEngineNewWindowRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineNewWindowRequest that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'destination', 'requestedUrl', 'requestedGeometry', 'isUserInitiated',
  'openIn'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineNewWindowRequest::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWebEngineNewWindowRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineNewWindowRequest::~QWebEngineNewWindowRequest()': the
    destructor: Python never removes a C++ QWebEngineNewWindowRequest.
  - Qt's
    'QWebEngineNewWindowRequest::QWebEngineNewWindowRequest(DestinationType
    a0, const QRect &a1, const QUrl &a2, bool a3,
    QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineNewWindowRequest is created at the first use, not by
    'QWebEngineNewWindowRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineNewWindowRequest.
  - Qt tells when it has removed the C++ QWebEngineNewWindowRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineNewWindowRequest that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineNewWindowRequest, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DestinationType(CuteNum):
    """
    The enum 'QWebEngineNewWindowRequest::DestinationType' of Qt, with the 4
    names Qt gives in it.
    """

    InNewWindow = Kee[int](0)
    InNewTab = Kee[int](1)
    InNewDialog = Kee[int](2)
    InNewBackgroundTab = Kee[int](3)

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
    Calls Qt's 'QString QWebEngineNewWindowRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#tr

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
    #  QString QWebEngineNewWindowRequest::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QWebEngineNewWindowRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineNewWindowRequest'

  #  A C++ QWebEngineNewWindowRequest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineNewWindowRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineNewWindowRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineNewWindowRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineNewWindowRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def destination(self) -> DestinationType:
    """
    Calls Qt's 'DestinationType QWebEngineNewWindowRequest::destination()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#destination

    Returns
    -------

    DestinationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DestinationType(number)'
      gives.
    """
    #  DestinationType QWebEngineNewWindowRequest::destination() const
    return QWebEngineNewWindowRequest.DestinationType(self.uglySide.call(
        'ritual_ZNK26QWebEngineNewWindowRequest11destinationEv',
    ))

  def requestedUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineNewWindowRequest::requestedUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#requestedUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineNewWindowRequest::requestedUrl() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineNewWindowRequest12requestedUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestedGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWebEngineNewWindowRequest::requestedGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#requestedGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWebEngineNewWindowRequest::requestedGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineNewWindowRequest17requestedGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isUserInitiated(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineNewWindowRequest::isUserInitiated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#isUserInitiated
    """
    #  bool QWebEngineNewWindowRequest::isUserInitiated() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineNewWindowRequest15isUserInitiatedEv',
    )

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
    Qt's
    'QWebEngineNewWindowRequest::QWebEngineNewWindowRequest(DestinationType
    a0, const QRect &a1, const QUrl &a2, bool a3,
    QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineNewWindowRequest.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineNewWindowRequest::QWebEngineNewWindowRequest(Destination"
        "Type a0, const QRect &a1, const QUrl &a2, bool a3, "
        "QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject "
        "*a5)': takes a type Python has no way to hand over yet.")

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

  @overload(QWebEnginePage)
  @overload(NoneType)
  def openIn(self, a0: Optional[QWebEnginePage]) -> None:
    """
    Calls Qt's 'void QWebEngineNewWindowRequest::openIn(QWebEnginePage *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenewwindowrequest.html#openIn

    Parameters
    ----------

    a0 : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineNewWindowRequest::openIn(QWebEnginePage *a0)
    self.uglySide.call(
        'ritual_ZN26QWebEngineNewWindowRequest6openInEP14QWebEnginePage',
        self._addressOf(a0),
    )
