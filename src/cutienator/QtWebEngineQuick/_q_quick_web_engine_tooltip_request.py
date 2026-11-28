"""
QQuickWebEngineTooltipRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineTooltipRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineTooltipRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineTooltipRequest: a plain Python object
  standing in front of one C++ QQuickWebEngineTooltipRequest.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineTooltipRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineTooltipRequest that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'x', 'y',
  'text', 'type', 'isAccepted', 'setAccepted'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineTooltipRequest::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineTooltipRequest::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineTooltipRequest::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineTooltipRequest::~QQuickWebEngineTooltipRequest()':
    the destructor: Python never removes a C++ QQuickWebEngineTooltipRequest.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineTooltipRequest is created at the first use, not by
    'QQuickWebEngineTooltipRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineTooltipRequest.
  - Qt tells when it has removed the C++ QQuickWebEngineTooltipRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWebEngineTooltipRequest, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineTooltipRequest::QmlIsUncreatable' of Qt, with
    the 1 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    yes = Kee[int](1)

  class RequestType(CuteNum):
    """
    The enum 'QQuickWebEngineTooltipRequest::RequestType' of Qt, with the 2
    names Qt gives in it.
    """

    Show = Kee[int](0)
    Hide = Kee[int](1)

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
    Calls Qt's 'QString QQuickWebEngineTooltipRequest::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#tr

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
    #  QString QQuickWebEngineTooltipRequest::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuickWebEngineTooltipRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineTooltipRequest'

  #  A C++ QQuickWebEngineTooltipRequest Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineTooltipRequest'

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
    *QQuickWebEngineTooltipRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineTooltipRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineTooltipRequest::x() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#x
    """
    #  int QQuickWebEngineTooltipRequest::x() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest1xEv',
    )

  def y(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineTooltipRequest::y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#y
    """
    #  int QQuickWebEngineTooltipRequest::y() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest1yEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineTooltipRequest::text() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineTooltipRequest::text() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest4textEv',
    )

  def type(self) -> RequestType:
    """
    Calls Qt's 'RequestType QQuickWebEngineTooltipRequest::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#type

    Returns
    -------

    RequestType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RequestType(number)'
      gives.
    """
    #  RequestType QQuickWebEngineTooltipRequest::type() const
    return QQuickWebEngineTooltipRequest.RequestType(self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest4typeEv',
    ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineTooltipRequest::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#isAccepted
    """
    #  bool QQuickWebEngineTooltipRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickWebEngineTooltipRequest10isAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineTooltipRequest::setAccepted(bool
    accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineTooltipRequest::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN29QQuickWebEngineTooltipRequest11setAcceptedEb', accepted,
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
  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineTooltipRequest::QQuickWebEngineTooltipRequest(const
    QString &text, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetooltiprequest.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineTooltipRequest::QQuickWebEngineTooltipRequest(const
    #      QString &text, QObject *parent)
    self._noteCreation(QQuickWebEngineTooltipRequest, lambda: Rituals.call(
        'ritual_ZN29QQuickWebEngineTooltipRequestC1ERK7QStringP7QObject',
        text, self._addressOf(parent, 'QObject'),
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
