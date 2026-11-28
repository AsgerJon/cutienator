"""
QQuickPopupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate
from . import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QPointF
  from ..QtGui import QEventPoint, QHoverEvent, QMouseEvent, QPalette
  from ..QtGui import QTouchEvent
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem, QQuickWindow
  from . import QQuickPopupAnchors, QQuickPopupPositioner
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPalette = WAIT['QPalette']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickItem = WAIT['QQuickItem']
  QQuickWindow = WAIT['QQuickWindow']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickPopupPrivate: a plain Python object standing in
  front of one C++ QQuickPopupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickPopupPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. Qt's
  QQuickPopupPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickPopupPrivate> as well, which is not
  reflected. Qt's QQuickPopupPrivate is built on Qt's
  QQuickPaletteProviderPrivateBase<QQuickPopup, QQuickPopupPrivate> as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickPopupPrivate that has a ritual and that Python
  can call so far, 49 names in all: 'q_func', 'get', 'init', 'closeOrReject',
  'tryClose', 'contains', 'acceptTouch', 'blockInput', 'handlePress',
  'handleMove', 'handleRelease', 'handleReleaseWithoutGrab', 'handleUngrab',
  'handleMouseEvent', 'handleHoverEvent', 'handleTouchEvent', 'windowInsets',
  'windowInsetsTopLeft', 'setEffectivePosFromWindowPos', 'reposition',
  'usePopupWindow', 'adjustPopupItemParentAndWindow', 'createOverlay',
  'createDimmer', 'destroyDimmer', 'toggleOverlay', 'updateContentPalettes',
  'resolvedPopupType', 'showDimmer', 'hideDimmer', 'resizeDimmer',
  'prepareEnterTransition', 'prepareExitTransition',
  'finalizeEnterTransition', 'finalizeExitTransition', 'opened',
  'popupWindowFlags', 'setPopupWindowFlags', 'getMargins', 'setTopMargin',
  'setLeftMargin', 'setRightMargin', 'setBottomMargin', 'getAnchors',
  'getPositioner', 'setWindow', 'itemDestroyed', 'defaultPalette',
  'updateChildrenPalettes'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPopup *QQuickPopupPrivate::q_func() const': takes in
    Python what 'QQuickPopup *QQuickPopupPrivate::q_func()' takes.
  - Qt's 'QQmlListProperty<QObject> QQuickPopupPrivate::contentData()': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem>
    QQuickPopupPrivate::contentChildren()': gives a type Python has no way to
    take yet.

  What to expect
  --------------

  - The C++ QQuickPopupPrivate is created at the first use, not by
    'QQuickPopupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupPrivate.
  - Each name of Qt's QQuickPopupPrivate that has no cute function yet,
    'contentChildren', 'contentData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickPopupPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TransitionState(CuteNum):
    """
    The enum 'QQuickPopupPrivate::TransitionState' of Qt, with the 3 names Qt
    gives in it.
    """

    NoTransition = Kee[int](0)
    EnterTransition = Kee[int](1)
    ExitTransition = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPopup)
  @overload(NoneType)
  def get(popup: Optional[QQuickPopup]) -> Optional[QQuickPopupPrivate]:
    """
    Calls Qt's 'QQuickPopupPrivate *QQuickPopupPrivate::get(QQuickPopup
    *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#get

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPopupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupPrivate *QQuickPopupPrivate::get(QQuickPopup *popup)
    address = Rituals.call(
        'ritual_ZN18QQuickPopupPrivate3getEP11QQuickPopup',
        CuteMixin._addressOf(popup),
    )
    return QQuickPopupPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupPrivate'

  #  A C++ QQuickPopupPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPopupPrivate'

  #  The functions Qt calls itself that QQuickPopupPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'acceptTouch': (
          ('_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QEventPoint'),
           )),
      ),
      'blockInput': (
          ('_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'handlePress': (
          ('_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleMove': (
          ('_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleRelease': (
          ('_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleReleaseWithoutGrab': (
          ('_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoi'
           'nt',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QEventPoint'),
           )),
      ),
      'handleUngrab': (
          ('_ZN18QQuickPopupPrivate12handleUngrabEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resolvedPopupType': (
          ('_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv',
           ('int', 'enum', 'QtQuickTemplates2:QQuickPopup.PopupType'),
           ()),
      ),
      'showDimmer': (
          ('_ZN18QQuickPopupPrivate10showDimmerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hideDimmer': (
          ('_ZN18QQuickPopupPrivate10hideDimmerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeDimmer': (
          ('_ZN18QQuickPopupPrivate12resizeDimmerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'prepareEnterTransition': (
          ('_ZN18QQuickPopupPrivate22prepareEnterTransitionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'prepareExitTransition': (
          ('_ZN18QQuickPopupPrivate21prepareExitTransitionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'finalizeEnterTransition': (
          ('_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finalizeExitTransition': (
          ('_ZN18QQuickPopupPrivate22finalizeExitTransitionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'opened': (
          ('_ZN18QQuickPopupPrivate6openedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'getPositioner': (
          ('_ZN18QQuickPopupPrivate13getPositionerEv',
           ('address', 'address', 'QtQuickTemplates2:QQuickPopupPositioner'),
           ()),
      ),
      'itemDestroyed': (
          ('_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'defaultPalette': (
          ('_ZNK18QQuickPopupPrivate14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'updateChildrenPalettes': (
          ('_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPalette'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def contains(self, scenePos: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::contains(const QPointF &scenePos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#contains

    Parameters
    ----------

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickPopupPrivate::contains(const QPointF &scenePos) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate8containsERK7QPointF',
        self._valueOf(scenePos, 'QPointF'),
    )

  @overload(QQuickItem, QPointF)
  @overload(NoneType, QPointF)
  def blockInput(self, item: Optional[QQuickItem], point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::blockInput(QQuickItem *item, const
    QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#blockInput

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7Q'
          'PointF')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._valueOf(point, 'QPointF'),
    )

  def windowInsets(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickPopupPrivate::windowInsets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#windowInsets

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickPopupPrivate::windowInsets() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate12windowInsetsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def windowInsetsTopLeft(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPopupPrivate::windowInsetsTopLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#windowInsetsTopLeft

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPopupPrivate::windowInsetsTopLeft() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate19windowInsetsTopLeftEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def usePopupWindow(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::usePopupWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#usePopupWindow
    """
    #  bool QQuickPopupPrivate::usePopupWindow() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate14usePopupWindowEv',
    )

  @overload(QQmlComponent, QQuickPopup, QQuickItem)
  @overload(QQmlComponent, QQuickPopup, NoneType)
  @overload(QQmlComponent, NoneType, QQuickItem)
  @overload(QQmlComponent, NoneType, NoneType)
  @overload(NoneType, QQuickPopup, QQuickItem)
  @overload(NoneType, QQuickPopup, NoneType)
  @overload(NoneType, NoneType, QQuickItem)
  @overload(NoneType, NoneType, NoneType)
  def createDimmer(
      self,
      component: Optional[QQmlComponent],
      popup: Optional[QQuickPopup],
      parent: Optional[QQuickItem],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopupPrivate::createDimmer(QQmlComponent
    *component, QQuickPopup *popup, QQuickItem *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#createDimmer

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopupPrivate::createDimmer(QQmlComponent *component,
    #      QQuickPopup *popup, QQuickItem *parent) const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate12createDimmerEP13QQmlComponentP11QQ'
        'uickPopupP10QQuickItem',
        self._addressOf(component), self._addressOf(popup),
        self._addressOf(parent),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def resolvedPopupType(self) -> QQuickPopup.PopupType:
    """
    Calls Qt's 'QQuickPopup::PopupType
    QQuickPopupPrivate::resolvedPopupType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#resolvedPopupType

    Returns
    -------

    QQuickPopup.PopupType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickPopup.PopupType(number)' gives.
    """
    #  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
    ritual = 'ritual_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv'
    return QQuickPopup.PopupType(self.uglySide.call(ritual))

  def popupWindowFlags(self) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags QQuickPopupPrivate::popupWindowFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#popupWindowFlags

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags QQuickPopupPrivate::popupWindowFlags() const
    return Qt.WindowFlags(self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate16popupWindowFlagsEv',
    ))

  def getMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickPopupPrivate::getMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#getMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickPopupPrivate::getMargins() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPopupPrivate10getMarginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickPopupPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickPopupPrivate::defaultPalette() const
    ritual = 'ritual_ZNK18QQuickPopupPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickPopupPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setEffectivePosFromWindowPos(self, windowPos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setEffectivePosFromWindowPos(const
    QPointF &windowPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html

    Parameters
    ----------

    windowPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPopupPrivate::setEffectivePosFromWindowPos(const QPointF
    #      &windowPos)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate28setEffectivePosFromWindowPosERK7QPo'
        'intF',
        self._valueOf(windowPos, 'QPointF'),
    )

  @overload(Qt.WindowFlags)
  def setPopupWindowFlags(self, flags: Qt.WindowFlags) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setPopupWindowFlags(Qt::WindowFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#setPopupWindowFlags

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QQuickPopupPrivate::setPopupWindowFlags(Qt::WindowFlags flags)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate19setPopupWindowFlagsE6QFlagsIN2Qt10W'
        'indowTypeEE',
        flags.value,
    )

  @overload(float)
  @overload(float, bool)
  def setTopMargin(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setTopMargin(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#setTopMargin

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupPrivate::setTopMargin(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate12setTopMarginEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftMargin(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setLeftMargin(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#setLeftMargin

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupPrivate::setLeftMargin(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate13setLeftMarginEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightMargin(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setRightMargin(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#setRightMargin

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupPrivate::setRightMargin(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate14setRightMarginEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomMargin(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setBottomMargin(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#setBottomMargin

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupPrivate::setBottomMargin(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate15setBottomMarginEdb', value, reset,
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::setWindow(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPrivate::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate9setWindowEP12QQuickWindow',
        self._addressOf(window),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupPrivate::QQuickPopupPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#QQuickPopupPrivate
    """
    #  QQuickPopupPrivate::QQuickPopupPrivate()
    self._noteCreation(QQuickPopupPrivate, lambda: Rituals.call(
        'ritual_ZN18QQuickPopupPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickPopup]:
    """
    Calls Qt's 'QQuickPopup *QQuickPopupPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#q_func

    Returns
    -------

    Optional[QQuickPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopup *QQuickPopupPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQuickPopupPrivate6q_funcEv')
    return QQuickPopup._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#init
    """
    #  void QQuickPopupPrivate::init()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate4initEv')

  def closeOrReject(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::closeOrReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#closeOrReject
    """
    #  void QQuickPopupPrivate::closeOrReject()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate13closeOrRejectEv')

  @overload(QPointF, QQuickPopup.ClosePolicy)
  def tryClose(self, pos: QPointF, flags: QQuickPopup.ClosePolicy) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::tryClose(const QPointF &pos,
    QQuickPopup::ClosePolicy flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#tryClose

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    flags : QQuickPopup.ClosePolicy
      Passed on as its number.
    """
    #  bool QQuickPopupPrivate::tryClose(const QPointF &pos,
    #      QQuickPopup::ClosePolicy flags)
    return self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate8tryCloseERK7QPointF6QFlagsIN11QQuick'
        'Popup15ClosePolicyFlagEE',
        self._valueOf(pos, 'QPointF'), flags.value,
    )

  @overload(QEventPoint)
  def acceptTouch(self, point: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::acceptTouch(const
    QTouchEvent::TouchPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#acceptTouch

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
    #      &point)
    ritual = 'ritual_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint')
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handlePress(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handlePress(QQuickItem *item, const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handlePress

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickPopupPrivate::handlePress(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointF'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7Q'
          'PointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handleMove(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleMove(QQuickItem *item, const
    QPointF &point, ulong timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#handleMove

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QP'
          'ointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handleRelease(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleRelease(QQuickItem *item,
    const QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleRelease

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickPopupPrivate::handleRelease(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPoin'
        'tFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK'
          '7QPointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QEventPoint)
  def handleReleaseWithoutGrab(self, a0: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleReleaseWithoutGrab(const
    QEventPoint &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleReleaseWithoutGrab

    Parameters
    ----------

    a0 : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint
    #      &a0)
    ritual = (
        'ritual_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEvent'
        'Point')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11'
          'QEventPoint')
    return self.uglySide.call(ritual, self._valueOf(a0))

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleUngrab
    """
    #  void QQuickPopupPrivate::handleUngrab()
    ritual = 'ritual_ZN18QQuickPopupPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate12handleUngrabEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QMouseEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def handleMouseEvent(
      self,
      item: Optional[QQuickItem],
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleMouseEvent(QQuickItem *item,
    QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleMouseEvent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopupPrivate::handleMouseEvent(QQuickItem *item,
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate16handleMouseEventEP10QQuickItemP11QM'
        'ouseEvent',
        self._addressOf(item), self._addressOf(event),
    )

  @overload(QQuickItem, QHoverEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QHoverEvent)
  @overload(NoneType, NoneType)
  def handleHoverEvent(
      self,
      item: Optional[QQuickItem],
      event: Optional[QHoverEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleHoverEvent(QQuickItem *item,
    QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleHoverEvent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopupPrivate::handleHoverEvent(QQuickItem *item,
    #      QHoverEvent *event)
    return self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate16handleHoverEventEP10QQuickItemP11QH'
        'overEvent',
        self._addressOf(item), self._addressOf(event),
    )

  @overload(QQuickItem, QTouchEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def handleTouchEvent(
      self,
      item: Optional[QQuickItem],
      event: Optional[QTouchEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::handleTouchEvent(QQuickItem *item,
    QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#handleTouchEvent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopupPrivate::handleTouchEvent(QQuickItem *item,
    #      QTouchEvent *event)
    return self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate16handleTouchEventEP10QQuickItemP11QT'
        'ouchEvent',
        self._addressOf(item), self._addressOf(event),
    )

  def reposition(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::reposition()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#reposition
    """
    #  void QQuickPopupPrivate::reposition()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate10repositionEv')

  def adjustPopupItemParentAndWindow(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::adjustPopupItemParentAndWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html
    """
    #  void QQuickPopupPrivate::adjustPopupItemParentAndWindow()
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate30adjustPopupItemParentAndWindowEv',
    )

  def createOverlay(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::createOverlay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#createOverlay
    """
    #  void QQuickPopupPrivate::createOverlay()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate13createOverlayEv')

  def destroyDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::destroyDimmer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#destroyDimmer
    """
    #  void QQuickPopupPrivate::destroyDimmer()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate13destroyDimmerEv')

  def toggleOverlay(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::toggleOverlay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#toggleOverlay
    """
    #  void QQuickPopupPrivate::toggleOverlay()
    self.uglySide.call('ritual_ZN18QQuickPopupPrivate13toggleOverlayEv')

  @overload(QPalette)
  def updateContentPalettes(self, parentPalette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::updateContentPalettes(const QPalette
    &parentPalette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#updateContentPalettes

    Parameters
    ----------

    parentPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickPopupPrivate::updateContentPalettes(const QPalette
    #      &parentPalette)
    self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate21updateContentPalettesERK8QPalette',
        self._valueOf(parentPalette),
    )

  def showDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::showDimmer()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#showDimmer
    """
    #  void QQuickPopupPrivate::showDimmer()
    ritual = 'ritual_ZN18QQuickPopupPrivate10showDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate10showDimmerEv'
    self.uglySide.call(ritual)

  def hideDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::hideDimmer()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#hideDimmer
    """
    #  void QQuickPopupPrivate::hideDimmer()
    ritual = 'ritual_ZN18QQuickPopupPrivate10hideDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate10hideDimmerEv'
    self.uglySide.call(ritual)

  def resizeDimmer(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::resizeDimmer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#resizeDimmer
    """
    #  void QQuickPopupPrivate::resizeDimmer()
    ritual = 'ritual_ZN18QQuickPopupPrivate12resizeDimmerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate12resizeDimmerEv'
    self.uglySide.call(ritual)

  def prepareEnterTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::prepareEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#prepareEnterTransition
    """
    #  bool QQuickPopupPrivate::prepareEnterTransition()
    ritual = 'ritual_ZN18QQuickPopupPrivate22prepareEnterTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate22prepareEnterTransitionEv'
    return self.uglySide.call(ritual)

  def prepareExitTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopupPrivate::prepareExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#prepareExitTransition
    """
    #  bool QQuickPopupPrivate::prepareExitTransition()
    ritual = 'ritual_ZN18QQuickPopupPrivate21prepareExitTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate21prepareExitTransitionEv'
    return self.uglySide.call(ritual)

  def finalizeEnterTransition(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::finalizeEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#finalizeEnterTransition
    """
    #  void QQuickPopupPrivate::finalizeEnterTransition()
    ritual = 'ritual_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv'
    self.uglySide.call(ritual)

  def finalizeExitTransition(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::finalizeExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#finalizeExitTransition
    """
    #  void QQuickPopupPrivate::finalizeExitTransition()
    ritual = 'ritual_ZN18QQuickPopupPrivate22finalizeExitTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate22finalizeExitTransitionEv'
    self.uglySide.call(ritual)

  def opened(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::opened()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#opened
    """
    #  void QQuickPopupPrivate::opened()
    ritual = 'ritual_ZN18QQuickPopupPrivate6openedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate6openedEv'
    self.uglySide.call(ritual)

  def getAnchors(self) -> Optional[QQuickPopupAnchors]:
    """
    Calls Qt's 'QQuickPopupAnchors *QQuickPopupPrivate::getAnchors()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupprivate.html#getAnchors

    Returns
    -------

    Optional[QQuickPopupAnchors]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupAnchors *QQuickPopupPrivate::getAnchors()
    address = self.uglySide.call(
        'ritual_ZN18QQuickPopupPrivate10getAnchorsEv',
    )
    from . import QQuickPopupAnchors
    return QQuickPopupAnchors._cuteAt(address)

  def getPositioner(self) -> Optional[QQuickPopupPositioner]:
    """
    Calls Qt's 'QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#getPositioner

    Returns
    -------

    Optional[QQuickPopupPositioner]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
    ritual = 'ritual_ZN18QQuickPopupPrivate13getPositionerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickPopupPrivate13getPositionerEv'
    address = self.uglySide.call(ritual)
    from . import QQuickPopupPositioner
    return QQuickPopupPositioner._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QPalette)
  def updateChildrenPalettes(self, parentPalette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickPopupPrivate::updateChildrenPalettes(const
    QPalette &parentPalette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupprivate.html#updateChildrenPalettes

    Parameters
    ----------

    parentPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
    #      &parentPalette)
    ritual = (
        'ritual_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPa'
          'lette')
    self.uglySide.call(ritual, self._valueOf(parentPalette))

  @staticmethod
  def contentChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem>
    QQuickPopupPrivate::contentChildren()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuickPopupPrivate.contentChildren' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuickItem> "
        "QQuickPopupPrivate::contentChildren()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def contentData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPopupPrivate::contentData()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPopupPrivate.contentData' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPopupPrivate::contentData()': "
        "gives a type Python has no way to take yet.")
