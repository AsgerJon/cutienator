"""
QQuickStackView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QUrl, QVariant
  from ..QtGui import QTouchEvent
  from ..QtQml import QJSValue, QQmlComponent, QQmlV4Function
  from ..QtQuick import QQuickTransition
  from . import QQuickStackViewArg, QQuickStackViewAttached
  from . import QQuickStackViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QJSValue = WAIT['QJSValue']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlV4Function = WAIT['QQmlV4Function']
  QQuickStackViewArg = WAIT['QQuickStackViewArg']
  QQuickTransition = WAIT['QQuickTransition']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackView(QQuickControl):
  """
  The cute side of Qt's QQuickStackView: a plain Python object standing in
  front of one C++ QQuickStackView.

  It is built on the cute 'QQuickControl', as Qt's QQuickStackView is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStackView that has a ritual and that Python
  can call so far, 49 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'isBusy', 'depth', 'currentItem', 'initialItem',
  'setInitialItem', 'popEnter', 'setPopEnter', 'popExit', 'setPopExit',
  'pushEnter', 'setPushEnter', 'pushExit', 'setPushExit', 'replaceEnter',
  'setReplaceEnter', 'replaceExit', 'setReplaceExit', 'get', 'find', 'push',
  'pop', 'replace', 'pushItems', 'pushItem', 'popToItem', 'popToIndex',
  'popCurrentItem', 'replaceCurrentItem', 'isEmpty', 'clear', 'busyChanged',
  'depthChanged', 'currentItemChanged', 'popEnterChanged', 'popExitChanged',
  'pushEnterChanged', 'pushExitChanged', 'replaceEnterChanged',
  'replaceExitChanged', 'emptyChanged', 'componentComplete',
  'geometryChange', 'childMouseEventFilter', 'touchEvent', 'accessibleRole',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStackView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickStackView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickStackView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickStackView::~QQuickStackView()': the destructor: Python never
    removes a C++ QQuickStackView.
  - Qt's 'const QQuickStackViewPrivate *QQuickStackView::d_func() const':
    takes in Python what 'QQuickStackViewPrivate *QQuickStackView::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 64 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickStackView is created at the first use, not by
    'QQuickStackView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackView.
  - Qt tells when it has removed the C++ QQuickStackView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickStackView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LoadBehavior(CuteNum):
    """
    The enum 'QQuickStackView::LoadBehavior' of Qt, with the 2 names Qt gives
    in it.
    """

    DontLoad = Kee[int](0)
    ForceLoad = Kee[int](1)

  class Operation(CuteNum):
    """
    The enum 'QQuickStackView::Operation' of Qt, with the 5 names Qt gives in
    it.
    """

    Transition = Kee[int](-1)
    Immediate = Kee[int](0)
    PushTransition = Kee[int](1)
    ReplaceTransition = Kee[int](2)
    PopTransition = Kee[int](3)

  class Status(CuteNum):
    """
    The enum 'QQuickStackView::Status' of Qt, with the 4 names Qt gives in
    it.
    """

    Inactive = Kee[int](0)
    Deactivating = Kee[int](1)
    Activating = Kee[int](2)
    Active = Kee[int](3)

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
    Calls Qt's 'QString QQuickStackView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#tr

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
    #  QString QQuickStackView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickStackView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickStackViewAttached]:
    """
    Calls Qt's 'QQuickStackViewAttached
    *QQuickStackView::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickStackViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewAttached
    #      *QQuickStackView::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN15QQuickStackView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickStackViewAttached
    return QQuickStackViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackView'

  #  A C++ QQuickStackView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStackView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStackView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStackView::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickStackView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isBusy(self) -> bool:
    """
    Calls Qt's 'bool QQuickStackView::isBusy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#isBusy
    """
    #  bool QQuickStackView::isBusy() const
    return self.uglySide.call('ritual_ZNK15QQuickStackView6isBusyEv')

  def depth(self) -> int:
    """
    Calls Qt's 'int QQuickStackView::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#depth
    """
    #  int QQuickStackView::depth() const
    return self.uglySide.call('ritual_ZNK15QQuickStackView5depthEv')

  def currentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#currentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::currentItem() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStackView11currentItemEv',
    )
    return QQuickItem._cuteAt(address)

  def initialItem(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickStackView::initialItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#initialItem

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickStackView::initialItem() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStackView11initialItemEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def popEnter(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::popEnter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#popEnter

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::popEnter() const
    address = self.uglySide.call('ritual_ZNK15QQuickStackView8popEnterEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def popExit(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::popExit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#popExit

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::popExit() const
    address = self.uglySide.call('ritual_ZNK15QQuickStackView7popExitEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def pushEnter(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::pushEnter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushEnter

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::pushEnter() const
    address = self.uglySide.call('ritual_ZNK15QQuickStackView9pushEnterEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def pushExit(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::pushExit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushExit

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::pushExit() const
    address = self.uglySide.call('ritual_ZNK15QQuickStackView8pushExitEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def replaceEnter(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::replaceEnter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#replaceEnter

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::replaceEnter() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStackView12replaceEnterEv',
    )
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def replaceExit(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickStackView::replaceExit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#replaceExit

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickStackView::replaceExit() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStackView11replaceExitEv',
    )
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickStackView::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#isEmpty
    """
    #  bool QQuickStackView::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QQuickStackView7isEmptyEv')

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickStackView::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickStackView::accessibleRole() const
    ritual = 'ritual_ZNK15QQuickStackView14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickStackView14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QJSValue)
  def setInitialItem(self, item: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickStackView::setInitialItem(const QJSValue &item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#setInitialItem

    Parameters
    ----------

    item : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickStackView::setInitialItem(const QJSValue &item)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView14setInitialItemERK8QJSValue',
        self._valueOf(item),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPopEnter(self, enter: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setPopEnter(QQuickTransition *enter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#setPopEnter

    Parameters
    ----------

    enter : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setPopEnter(QQuickTransition *enter)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView11setPopEnterEP16QQuickTransition',
        self._addressOf(enter),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPopExit(self, exit: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setPopExit(QQuickTransition *exit)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#setPopExit

    Parameters
    ----------

    exit : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setPopExit(QQuickTransition *exit)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView10setPopExitEP16QQuickTransition',
        self._addressOf(exit),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPushEnter(self, enter: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setPushEnter(QQuickTransition *enter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#setPushEnter

    Parameters
    ----------

    enter : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setPushEnter(QQuickTransition *enter)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView12setPushEnterEP16QQuickTransition',
        self._addressOf(enter),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPushExit(self, exit: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setPushExit(QQuickTransition *exit)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#setPushExit

    Parameters
    ----------

    exit : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setPushExit(QQuickTransition *exit)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView11setPushExitEP16QQuickTransition',
        self._addressOf(exit),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setReplaceEnter(self, enter: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setReplaceEnter(QQuickTransition
    *enter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#setReplaceEnter

    Parameters
    ----------

    enter : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setReplaceEnter(QQuickTransition *enter)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView15setReplaceEnterEP16QQuickTransition',
        self._addressOf(enter),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setReplaceExit(self, exit: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickStackView::setReplaceExit(QQuickTransition
    *exit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#setReplaceExit

    Parameters
    ----------

    exit : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::setReplaceExit(QQuickTransition *exit)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView14setReplaceExitEP16QQuickTransition',
        self._addressOf(exit),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackView::QQuickStackView(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#QQuickStackView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStackView::QQuickStackView(QQuickItem *parent)
    self._noteCreation(QQuickStackView, lambda: Rituals.call(
        'ritual_ZN15QQuickStackViewC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(int)
  @overload(int, LoadBehavior)
  def get(
      self,
      index: int,
      behavior: LoadBehavior = LoadBehavior.DontLoad,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::get(int index,
    QQuickStackView::LoadBehavior behavior)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    behavior : LoadBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      LoadBehavior.DontLoad.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::get(int index,
    #      QQuickStackView::LoadBehavior behavior)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView3getEiNS_12LoadBehaviorE',
        index, behavior.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QJSValue)
  @overload(QJSValue, LoadBehavior)
  def find(
      self,
      callback: QJSValue,
      behavior: LoadBehavior = LoadBehavior.DontLoad,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::find(const QJSValue &callback,
    QQuickStackView::LoadBehavior behavior)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#find

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    behavior : LoadBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      LoadBehavior.DontLoad.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::find(const QJSValue &callback,
    #      QQuickStackView::LoadBehavior behavior)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView4findERK8QJSValueNS_12LoadBehaviorE',
        self._valueOf(callback), behavior.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def push(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickStackView::push(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#push

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::push(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView4pushEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def pop(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickStackView::pop(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pop

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::pop(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView3popEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def replace(self, args: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickStackView::replace(QQmlV4FunctionPtr args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#replace

    Parameters
    ----------

    args : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::replace(QQmlV4FunctionPtr args)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView7replaceEP14QQmlV4Function',
        self._addressOf(args),
    )

  @overload(QList[QQuickStackViewArg])
  @overload(QList[QQuickStackViewArg], Operation)
  def pushItems(
      self,
      args: QList[QQuickStackViewArg],
      operation: Operation = Operation.PushTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickStackView::pushItems(QList<QQuickStackViewArg> args, Operation
    operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushItems

    Parameters
    ----------

    args : QList[QQuickStackViewArg]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PushTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::pushItems(QList<QQuickStackViewArg> args,
    #      Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView9pushItemsE5QListI18QQuickStackViewArgEN'
        'S_9OperationE',
        self._valueOf(args), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  @overload(QQuickItem, QMap[str, QVariant], Operation)
  @overload(NoneType, QMap[str, QVariant], Operation)
  def pushItem(
      self,
      item: Optional[QQuickItem],
      properties: QMap[str, QVariant],
      operation: Operation = Operation.PushTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::pushItem(QQuickItem *item, const
    QVariantMap &properties, Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PushTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::pushItem(QQuickItem *item, const
    #      QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView8pushItemEP10QQuickItemRK4QMapI7QString8'
        'QVariantENS_9OperationE',
        self._addressOf(item), self._valueOf(properties), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQmlComponent, QMap[str, QVariant])
  @overload(QQmlComponent, QMap[str, QVariant], Operation)
  def pushItem(
      self,
      component: Optional[QQmlComponent],
      properties: QMap[str, QVariant],
      operation: Operation = Operation.PushTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::pushItem(QQmlComponent
    *component, const QVariantMap &properties, Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushItem

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PushTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::pushItem(QQmlComponent *component, const
    #      QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView8pushItemEP13QQmlComponentRK4QMapI7QStri'
        'ng8QVariantENS_9OperationE',
        self._addressOf(component), self._valueOf(properties),
        operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  @overload(QUrl, QMap[str, QVariant], Operation)
  def pushItem(
      self,
      url: QUrl,
      properties: QMap[str, QVariant],
      operation: Operation = Operation.PushTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::pushItem(const QUrl &url, const
    QVariantMap &properties, Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#pushItem

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PushTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::pushItem(const QUrl &url, const
    #      QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView8pushItemERK4QUrlRK4QMapI7QString8QVaria'
        'ntENS_9OperationE',
        self._valueOf(url), self._valueOf(properties), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, Operation)
  @overload(NoneType, Operation)
  def popToItem(
      self,
      item: Optional[QQuickItem],
      operation: Operation = Operation.PopTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::popToItem(QQuickItem *item,
    Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#popToItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PopTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::popToItem(QQuickItem *item, Operation
    #      operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView9popToItemEP10QQuickItemNS_9OperationE',
        self._addressOf(item), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(int)
  @overload(int, Operation)
  def popToIndex(
      self,
      index: int,
      operation: Operation = Operation.PopTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::popToIndex(int index, Operation
    operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#popToIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PopTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::popToIndex(int index, Operation
    #      operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView10popToIndexEiNS_9OperationE',
        index, operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload()
  @overload(Operation)
  def popCurrentItem(
      self,
      operation: Operation = Operation.PopTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::popCurrentItem(Operation
    operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#popCurrentItem

    Parameters
    ----------

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.PopTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::popCurrentItem(Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView14popCurrentItemENS_9OperationE',
        operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QList[QQuickStackViewArg])
  @overload(QList[QQuickStackViewArg], Operation)
  def replaceCurrentItem(
      self,
      args: QList[QQuickStackViewArg],
      operation: Operation = Operation.ReplaceTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::replaceCurrentItem(const
    QList<QQuickStackViewArg> &args, Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceCurrentItem

    Parameters
    ----------

    args : QList[QQuickStackViewArg]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.ReplaceTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::replaceCurrentItem(const
    #      QList<QQuickStackViewArg> &args, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView18replaceCurrentItemERK5QListI18QQuickSt'
        'ackViewArgENS_9OperationE',
        self._valueOf(args), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  @overload(QQuickItem, QMap[str, QVariant], Operation)
  @overload(NoneType, QMap[str, QVariant], Operation)
  def replaceCurrentItem(
      self,
      item: Optional[QQuickItem],
      properties: QMap[str, QVariant],
      operation: Operation = Operation.ReplaceTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::replaceCurrentItem(QQuickItem
    *item, const QVariantMap &properties, Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceCurrentItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.ReplaceTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::replaceCurrentItem(QQuickItem *item,
    #      const QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView18replaceCurrentItemEP10QQuickItemRK4QMa'
        'pI7QString8QVariantENS_9OperationE',
        self._addressOf(item), self._valueOf(properties), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QQmlComponent, QMap[str, QVariant])
  @overload(QQmlComponent, QMap[str, QVariant], Operation)
  def replaceCurrentItem(
      self,
      component: Optional[QQmlComponent],
      properties: QMap[str, QVariant],
      operation: Operation = Operation.ReplaceTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::replaceCurrentItem(QQmlComponent
    *component, const QVariantMap &properties, Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceCurrentItem

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.ReplaceTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::replaceCurrentItem(QQmlComponent
    #      *component, const QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView18replaceCurrentItemEP13QQmlComponentRK4'
        'QMapI7QString8QVariantENS_9OperationE',
        self._addressOf(component), self._valueOf(properties),
        operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  @overload(QUrl, QMap[str, QVariant], Operation)
  def replaceCurrentItem(
      self,
      url: QUrl,
      properties: QMap[str, QVariant],
      operation: Operation = Operation.ReplaceTransition,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStackView::replaceCurrentItem(const QUrl
    &url, const QVariantMap &properties, Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceCurrentItem

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.ReplaceTransition.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStackView::replaceCurrentItem(const QUrl &url, const
    #      QVariantMap &properties, Operation operation)
    address = self.uglySide.call(
        'ritual_ZN15QQuickStackView18replaceCurrentItemERK4QUrlRK4QMapI7QSt'
        'ring8QVariantENS_9OperationE',
        self._valueOf(url), self._valueOf(properties), operation.value,
    )
    return QQuickItem._cuteAt(address)

  @overload()
  @overload(Operation)
  def clear(self, operation: Operation = Operation.Immediate) -> None:
    """
    Calls Qt's 'void QQuickStackView::clear(Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#clear

    Parameters
    ----------

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.Immediate.
    """
    #  void QQuickStackView::clear(Operation operation)
    self.uglySide.call(
        'ritual_ZN15QQuickStackView5clearENS_9OperationE', operation.value,
    )

  def busyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::busyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#busyChanged
    """
    #  void QQuickStackView::busyChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView11busyChangedEv')

  def depthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::depthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#depthChanged
    """
    #  void QQuickStackView::depthChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView12depthChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#currentItemChanged
    """
    #  void QQuickStackView::currentItemChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView18currentItemChangedEv')

  def popEnterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::popEnterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#popEnterChanged
    """
    #  void QQuickStackView::popEnterChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView15popEnterChangedEv')

  def popExitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::popExitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#popExitChanged
    """
    #  void QQuickStackView::popExitChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView14popExitChangedEv')

  def pushEnterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::pushEnterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#pushEnterChanged
    """
    #  void QQuickStackView::pushEnterChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView16pushEnterChangedEv')

  def pushExitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::pushExitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#pushExitChanged
    """
    #  void QQuickStackView::pushExitChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView15pushExitChangedEv')

  def replaceEnterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::replaceEnterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceEnterChanged
    """
    #  void QQuickStackView::replaceEnterChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView19replaceEnterChangedEv')

  def replaceExitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::replaceExitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#replaceExitChanged
    """
    #  void QQuickStackView::replaceExitChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView18replaceExitChangedEv')

  def emptyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::emptyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#emptyChanged
    """
    #  void QQuickStackView::emptyChanged()
    self.uglySide.call('ritual_ZN15QQuickStackView12emptyChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickStackView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#componentComplete
    """
    #  void QQuickStackView::componentComplete()
    ritual = 'ritual_ZN15QQuickStackView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickStackView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickStackView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickStackView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickStackView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickStackView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickStackView::childMouseEventFilter(QQuickItem *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackview.html#childMouseEventFilter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickStackView::childMouseEventFilter(QQuickItem *a0, QEvent
    #      *a1)
    ritual = (
        'ritual_ZN15QQuickStackView21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickStackView21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickStackView::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackView::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN15QQuickStackView10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickStackView10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickStackViewPrivate]:
    """
    Calls Qt's 'QQuickStackViewPrivate *QQuickStackView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackview.html#d_func

    Returns
    -------

    Optional[QQuickStackViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewPrivate *QQuickStackView::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickStackView6d_funcEv')
    from . import QQuickStackViewPrivate
    return QQuickStackViewPrivate._cuteAt(address)
