"""
QWebEngineNavigationRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginenavigationrequest.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineNavigationRequest(QObject):
  """
  The cute side of Qt's QWebEngineNavigationRequest: a plain Python object
  standing in front of one C++ QWebEngineNavigationRequest.

  It is built on the cute 'QObject', as Qt's QWebEngineNavigationRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineNavigationRequest that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject', 'tr', 'url',
  'isMainFrame', 'hasFormData', 'navigationType', 'isUserInitiated',
  'accept', 'reject', 'action', 'setAction', 'actionChanged', 'isAccepted'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineNavigationRequest::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWebEngineNavigationRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineNavigationRequest::~QWebEngineNavigationRequest()': the
    destructor: Python never removes a C++ QWebEngineNavigationRequest.
  - Qt's 'QWebEngineNavigationRequestPrivate
    *QWebEngineNavigationRequest::d_func()': gives
    'QWebEngineNavigationRequestPrivate', which has no cute class yet.
  - Qt's 'const QWebEngineNavigationRequestPrivate
    *QWebEngineNavigationRequest::d_func() const': gives
    'QWebEngineNavigationRequestPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineNavigationRequest is created at the first use, not by
    'QWebEngineNavigationRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineNavigationRequest.
  - Qt tells when it has removed the C++ QWebEngineNavigationRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWebEngineNavigationRequest, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class NavigationRequestAction(CuteNum):
    """
    The enum 'QWebEngineNavigationRequest::NavigationRequestAction' of Qt,
    with the 2 names Qt gives in it.
    """

    AcceptRequest = Kee[int](0)
    IgnoreRequest = Kee[int](255)

  class NavigationType(CuteNum):
    """
    The enum 'QWebEngineNavigationRequest::NavigationType' of Qt, with the 7
    names Qt gives in it.
    """

    LinkClickedNavigation = Kee[int](0)
    TypedNavigation = Kee[int](1)
    FormSubmittedNavigation = Kee[int](2)
    BackForwardNavigation = Kee[int](3)
    ReloadNavigation = Kee[int](4)
    OtherNavigation = Kee[int](5)
    RedirectNavigation = Kee[int](6)

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
    Calls Qt's 'QString QWebEngineNavigationRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#tr

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
    #  QString QWebEngineNavigationRequest::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QWebEngineNavigationRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineNavigationRequest'

  #  A C++ QWebEngineNavigationRequest Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineNavigationRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineNavigationRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineNavigationRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineNavigationRequest::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineNavigationRequest::url() const
    address = self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isMainFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineNavigationRequest::isMainFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#isMainFrame
    """
    #  bool QWebEngineNavigationRequest::isMainFrame() const
    return self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest11isMainFrameEv',
    )

  def hasFormData(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineNavigationRequest::hasFormData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#hasFormData
    """
    #  bool QWebEngineNavigationRequest::hasFormData() const
    return self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest11hasFormDataEv',
    )

  def navigationType(self) -> NavigationType:
    """
    Calls Qt's 'NavigationType QWebEngineNavigationRequest::navigationType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#navigationType

    Returns
    -------

    NavigationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NavigationType(number)'
      gives.
    """
    #  NavigationType QWebEngineNavigationRequest::navigationType() const
    return QWebEngineNavigationRequest.NavigationType(self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest14navigationTypeEv',
    ))

  def isUserInitiated(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineNavigationRequest::isUserInitiated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#isUserInitiated
    """
    #  bool QWebEngineNavigationRequest::isUserInitiated() const
    return self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest15isUserInitiatedEv',
    )

  def action(self) -> NavigationRequestAction:
    """
    Calls Qt's 'NavigationRequestAction QWebEngineNavigationRequest::action()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#action

    Returns
    -------

    NavigationRequestAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'NavigationRequestAction(number)' gives.
    """
    #  NavigationRequestAction QWebEngineNavigationRequest::action() const
    return QWebEngineNavigationRequest.NavigationRequestAction(
        self.uglySide.call(
            'ritual_ZNK27QWebEngineNavigationRequest6actionEv',
        ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineNavigationRequest::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#isAccepted
    """
    #  bool QWebEngineNavigationRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK27QWebEngineNavigationRequest10isAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(NavigationRequestAction)
  def setAction(self, action: NavigationRequestAction) -> None:
    """
    Calls Qt's 'void
    QWebEngineNavigationRequest::setAction(NavigationRequestAction action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#setAction

    Parameters
    ----------

    action : NavigationRequestAction
      Passed on as its number.
    """
    #  void QWebEngineNavigationRequest::setAction(NavigationRequestAction
    #      action)
    self.uglySide.call(
        'ritual_ZN27QWebEngineNavigationRequest9setActionENS_23NavigationRe'
        'questActionE',
        action.value,
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

  @overload(QUrl, NavigationType, bool, bool, bool)
  @overload(QUrl, NavigationType, bool, bool, bool, QObject)
  @overload(QUrl, NavigationType, bool, bool, bool, NoneType)
  def __init__(
      self,
      url: QUrl,
      navigationType: NavigationType,
      mainFrame: bool,
      formData: bool,
      userInitiated: bool,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineNavigationRequest::QWebEngineNavigationRequest(const QUrl
    &url, NavigationType navigationType, bool mainFrame, bool formData, bool
    userInitiated, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    navigationType : NavigationType
      Passed on as its number.

    mainFrame : bool
      Passed on as it is.

    formData : bool
      Passed on as it is.

    userInitiated : bool
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineNavigationRequest::QWebEngineNavigationRequest(const QUrl
    #      &url, NavigationType navigationType, bool mainFrame, bool
    #      formData, bool userInitiated, QObject *parent)
    self._noteCreation(QWebEngineNavigationRequest, lambda: Rituals.call(
        'ritual_ZN27QWebEngineNavigationRequestC1ERK4QUrlNS_14NavigationTyp'
        'eEbbbP7QObject',
        self._valueOf(url), navigationType.value, mainFrame, formData,
        userInitiated, self._addressOf(parent, 'QObject'),
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

  def accept(self) -> None:
    """
    Calls Qt's 'void QWebEngineNavigationRequest::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#accept
    """
    #  void QWebEngineNavigationRequest::accept()
    self.uglySide.call('ritual_ZN27QWebEngineNavigationRequest6acceptEv')

  def reject(self) -> None:
    """
    Calls Qt's 'void QWebEngineNavigationRequest::reject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#reject
    """
    #  void QWebEngineNavigationRequest::reject()
    self.uglySide.call('ritual_ZN27QWebEngineNavigationRequest6rejectEv')

  def actionChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineNavigationRequest::actionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenavigationrequest.html#actionChanged
    """
    #  void QWebEngineNavigationRequest::actionChanged()
    self.uglySide.call(
        'ritual_ZN27QWebEngineNavigationRequest13actionChangedEv',
    )
