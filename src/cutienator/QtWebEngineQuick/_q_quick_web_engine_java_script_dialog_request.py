"""
QQuickWebEngineJavaScriptDialogRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineJavaScriptDialogRequest to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineJavaScriptDialogRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineJavaScriptDialogRequest: a plain
  Python object standing in front of one C++
  QQuickWebEngineJavaScriptDialogRequest.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineJavaScriptDialogRequest is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineJavaScriptDialogRequest that has a
  ritual and that Python can call so far, 11 names in all: 'metaObject',
  'tr', 'message', 'defaultText', 'title', 'type', 'securityOrigin',
  'isAccepted', 'setAccepted', 'dialogAccept', 'dialogReject'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineJavaScriptDialogRequest::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineJavaScriptDialogRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineJavaScriptDialogRequest::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QQuickWebEngineJavaScriptDialogRequest::
    ~QQuickWebEngineJavaScriptDialogRequest()': the destructor: Python never
    removes a C++ QQuickWebEngineJavaScriptDialogRequest.
  - Qt's 'QQuickWebEngineJavaScriptDialogRequest::
    QQuickWebEngineJavaScriptDialogRequest(QSharedPointer<QtWebEngineCore::
    JavaScriptDialogController> controller, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineJavaScriptDialogRequest is created at the first
    use, not by 'QQuickWebEngineJavaScriptDialogRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineJavaScriptDialogRequest.
  - Qt tells when it has removed the C++
    QQuickWebEngineJavaScriptDialogRequest. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QQuickWebEngineJavaScriptDialogRequest that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineJavaScriptDialogRequest, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DialogType(CuteNum):
    """
    The enum 'QQuickWebEngineJavaScriptDialogRequest::DialogType' of Qt, with
    the 4 names Qt gives in it.
    """

    DialogTypeAlert = Kee[int](0)
    DialogTypeConfirm = Kee[int](1)
    DialogTypePrompt = Kee[int](2)
    DialogTypeBeforeUnload = Kee[int](3)

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineJavaScriptDialogRequest::QmlIsUncreatable' of
    Qt, with the 1 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
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
    Calls Qt's 'QString QQuickWebEngineJavaScriptDialogRequest::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html#tr

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
    #  QString QQuickWebEngineJavaScriptDialogRequest::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN38QQuickWebEngineJavaScriptDialogRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineJavaScriptDialogRequest'

  #  A C++ QQuickWebEngineJavaScriptDialogRequest Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineJavaScriptDialogRequest'

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
    *QQuickWebEngineJavaScriptDialogRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickWebEngineJavaScriptDialogRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def message(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineJavaScriptDialogRequest::message()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineJavaScriptDialogRequest::message() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest7messageEv',
    )

  def defaultText(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineJavaScriptDialogRequest::defaultText()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineJavaScriptDialogRequest::defaultText() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest11defaultTextEv',
    )

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineJavaScriptDialogRequest::title()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineJavaScriptDialogRequest::title() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest5titleEv',
    )

  def type(self) -> DialogType:
    """
    Calls Qt's 'DialogType QQuickWebEngineJavaScriptDialogRequest::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html#type

    Returns
    -------

    DialogType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DialogType(number)'
      gives.
    """
    #  DialogType QQuickWebEngineJavaScriptDialogRequest::type() const
    return QQuickWebEngineJavaScriptDialogRequest.DialogType(
        self.uglySide.call(
            'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest4typeEv',
        ))

  def securityOrigin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineJavaScriptDialogRequest::securityOrigin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineJavaScriptDialogRequest::securityOrigin() const
    address = self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest14securityOrigin'
        'Ev',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineJavaScriptDialogRequest::isAccepted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html
    """
    #  bool QQuickWebEngineJavaScriptDialogRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest10isAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineJavaScriptDialogRequest::setAccepted(bool
    accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineJavaScriptDialogRequest::setAccepted(bool
    #      accepted)
    self.uglySide.call(
        'ritual_ZN38QQuickWebEngineJavaScriptDialogRequest11setAcceptedEb',
        accepted,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineJavaScriptDialogRequest::
    QQuickWebEngineJavaScriptDialogRequest(QSharedPointer<QtWebEngineCore::
    JavaScriptDialogController> controller, QObject *parent)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineJavaScriptDialogRequest.__init__' has no cute "
        "function yet. Qt's "
        "'QQuickWebEngineJavaScriptDialogRequest::QQuickWebEngineJavaScriptD"
        "ialogRequest(QSharedPointer<QtWebEngineCore::JavaScriptDialogContro"
        "ller> controller, QObject *parent)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload()
  @overload(str)
  def dialogAccept(self, text: str = '') -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineJavaScriptDialogRequest::dialogAccept(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QQuickWebEngineJavaScriptDialogRequest::dialogAccept(const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN38QQuickWebEngineJavaScriptDialogRequest12dialogAcceptERK'
        '7QString',
        text,
    )

  def dialogReject(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineJavaScriptDialogRequest::dialogReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginejavascriptdialogrequest.html
    """
    #  void QQuickWebEngineJavaScriptDialogRequest::dialogReject()
    self.uglySide.call(
        'ritual_ZN38QQuickWebEngineJavaScriptDialogRequest12dialogRejectEv',
    )
