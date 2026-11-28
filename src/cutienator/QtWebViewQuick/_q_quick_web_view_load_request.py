"""
QQuickWebViewLoadRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebviewloadrequest_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebViewLoadRequest to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickWebView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtWebView import QWebViewLoadingInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebViewLoadingInfo = WAIT['QWebViewLoadingInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebViewLoadRequest(QObject):
  """
  The cute side of Qt's QQuickWebViewLoadRequest: a plain Python object
  standing in front of one C++ QQuickWebViewLoadRequest.

  It is built on the cute 'QObject', as Qt's QQuickWebViewLoadRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebViewLoadRequest that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'url',
  'status', 'errorString'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebViewLoadRequest::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickWebViewLoadRequest::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebViewLoadRequest::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickWebViewLoadRequest::~QQuickWebViewLoadRequest()': the
    destructor: Python never removes a C++ QQuickWebViewLoadRequest.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebViewLoadRequest is created at the first use, not by
    'QQuickWebViewLoadRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebViewLoadRequest.
  - Qt tells when it has removed the C++ QQuickWebViewLoadRequest. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickWebViewLoadRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebviewloadrequest.html#tr

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
    #  QString QQuickWebViewLoadRequest::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickWebViewLoadRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebViewLoadRequest'

  #  A C++ QQuickWebViewLoadRequest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebViewLoadRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebViewLoadRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewloadrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebViewLoadRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebViewLoadRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebViewLoadRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebviewloadrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebViewLoadRequest::url() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickWebViewLoadRequest3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> QQuickWebView.LoadStatus:
    """
    Calls Qt's 'QQuickWebView::LoadStatus QQuickWebViewLoadRequest::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewloadrequest.html#status

    Returns
    -------

    QQuickWebView.LoadStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickWebView.LoadStatus(number)' gives.
    """
    #  QQuickWebView::LoadStatus QQuickWebViewLoadRequest::status() const
    return QQuickWebView.LoadStatus(self.uglySide.call(
        'ritual_ZNK24QQuickWebViewLoadRequest6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQuickWebViewLoadRequest::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewloadrequest.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebViewLoadRequest::errorString() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickWebViewLoadRequest11errorStringEv',
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

  @overload(QWebViewLoadingInfo)
  def __init__(self, d: QWebViewLoadingInfo) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebViewLoadRequest::QQuickWebViewLoadRequest(const
    QWebViewLoadingInfo &d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebviewloadrequest.html

    Parameters
    ----------

    d : QWebViewLoadingInfo
      Passed on as a value: Qt reads the C++ QWebViewLoadingInfo, which stays
      Python's own.
    """
    #  QQuickWebViewLoadRequest::QQuickWebViewLoadRequest(const
    #      QWebViewLoadingInfo &d)
    self._noteCreation(QQuickWebViewLoadRequest, lambda: Rituals.call(
        'ritual_ZN24QQuickWebViewLoadRequestC1ERK19QWebViewLoadingInfo',
        self._valueOf(d),
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
