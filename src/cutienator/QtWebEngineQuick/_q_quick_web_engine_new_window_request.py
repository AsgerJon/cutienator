"""
QQuickWebEngineNewWindowRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginenewwindowrequest_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineNewWindowRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtWebEngineCore import QWebEngineNewWindowRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickWebEngineView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWebEngineView = WAIT['QQuickWebEngineView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineNewWindowRequest(QWebEngineNewWindowRequest):
  """
  The cute side of Qt's QQuickWebEngineNewWindowRequest: a plain Python
  object standing in front of one C++ QQuickWebEngineNewWindowRequest.

  It is built on the cute 'QWebEngineNewWindowRequest', as Qt's
  QQuickWebEngineNewWindowRequest is built on Qt's
  QWebEngineNewWindowRequest, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineNewWindowRequest that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'openIn'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineNewWindowRequest::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineNewWindowRequest::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineNewWindowRequest::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineNewWindowRequest::QQuickWebEngineNewWindowRequest(
    DestinationType a0, const QRect &a1, const QUrl &a2, bool a3,
    QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineNewWindowRequest is created at the first use, not
    by 'QQuickWebEngineNewWindowRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineNewWindowRequest.
  - Qt tells when it has removed the C++ QQuickWebEngineNewWindowRequest.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWebEngineNewWindowRequest that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineNewWindowRequest, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineNewWindowRequest::QmlIsUncreatable' of Qt, with
    the 1 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    yes = Kee[int](1)

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
    Calls Qt's 'QString QQuickWebEngineNewWindowRequest::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginenewwindowrequest.html#tr

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
    #  QString QQuickWebEngineNewWindowRequest::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuickWebEngineNewWindowRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineNewWindowRequest'

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
    *QQuickWebEngineNewWindowRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginenewwindowrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineNewWindowRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineNewWindowRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQuickWebEngineNewWindowRequest::QQuickWebEngineNewWindowRequest(
    DestinationType a0, const QRect &a1, const QUrl &a2, bool a3,
    QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineNewWindowRequest.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickWebEngineNewWindowRequest::QQuickWebEngineNewWindowRequest(D"
        "estinationType a0, const QRect &a1, const QUrl &a2, bool a3, "
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

  @overload(QQuickWebEngineView)
  @overload(NoneType)
  def openIn(self, a0: Optional[QQuickWebEngineView]) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineNewWindowRequest::openIn(QQuickWebEngineView *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginenewwindowrequest.html#openIn

    Parameters
    ----------

    a0 : Optional[QQuickWebEngineView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineNewWindowRequest::openIn(QQuickWebEngineView *a0)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineNewWindowRequest6openInEP19QQuickWebEngi'
        'neView',
        self._addressOf(a0),
    )
