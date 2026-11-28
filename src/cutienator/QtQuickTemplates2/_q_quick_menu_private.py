"""
QQuickMenuPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickPopup, QQuickPopupPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QEventPoint, QKeyEvent, QPalette, QPlatformMenu
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickAction, QQuickMenu, QQuickMenuItem
  from . import QQuickPopupPositioner
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QKeyEvent = WAIT['QKeyEvent']
  QPointF = WAIT['QPointF']
  QQuickAction = WAIT['QQuickAction']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickMenu = WAIT['QQuickMenu']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuPrivate(QQuickPopupPrivate):
  """
  The cute side of Qt's QQuickMenuPrivate: a plain Python object standing in
  front of one C++ QQuickMenuPrivate.

  It is built on the cute 'QQuickPopupPrivate', as Qt's QQuickMenuPrivate is
  built on Qt's QQuickPopupPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuPrivate that has a ritual and that Python
  can call so far, 58 names in all: 'q_func', 'get', 'init', 'nativeHandle',
  'maybeNativeHandle', 'rootMenu', 'useNativeMenu', 'createNativeMenu',
  'removeNativeMenu', 'syncWithNativeMenu', 'syncWithUseNativeMenu',
  'setNativeMenuVisible', 'makeEditMenu', 'itemAt', 'insertItem',
  'maybeCreateAndInsertNativeItem', 'moveItem', 'removeItem',
  'removeNativeItem', 'resetNativeData', 'recursivelyCreateNativeMenuItems',
  'printContentModelItems', 'beginCreateItem', 'completeCreateItem',
  'createItem', 'resizeItem', 'resizeItems', 'itemChildAdded',
  'itemSiblingOrderChanged', 'itemParentChanged', 'itemDestroyed',
  'itemGeometryChanged', 'getPositioner', 'prepareEnterTransition',
  'prepareExitTransition', 'blockInput', 'handlePress',
  'handleReleaseWithoutGrab', 'onItemHovered', 'onItemTriggered',
  'onItemActiveFocusChanged', 'onItemVisibleChanged', 'updateTextPadding',
  'updateCollapsedSeparators', 'currentSubMenu', 'setParentMenu',
  'resolveParentItem', 'popup', 'propagateKeyEvent', 'startHoverTimer',
  'stopHoverTimer', 'setCurrentIndex', 'activateNextItem',
  'activatePreviousItem', 'firstEnabledMenuItem', 'defaultPalette',
  'resolvedPopupType', 'resetContentItem'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMenu *QQuickMenuPrivate::q_func() const': takes in
    Python what 'QQuickMenu *QQuickMenuPrivate::q_func()' takes.
  - Qt's 'void
    QQuickMenuPrivate::contentData_append(QQmlListProperty<QObject> *prop,
    QObject *obj)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQuickMenuPrivate::contentData_count(QQmlListProperty<QObject> *prop)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QQuickMenuPrivate::contentData_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuickMenuPrivate::contentData_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickMenuPrivate is created at the first use, not by
    'QQuickMenuPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuPrivate.
  - Each name of Qt's QQuickMenuPrivate that has no cute function yet,
    'contentData_append', 'contentData_at', 'contentData_clear',
    'contentData_count', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuickMenuPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DestructionPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickMenuPrivate::DestructionPolicy' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Destroy = Kee[int](0)
    DoNotDestroy = Kee[int](1)

  class SyncPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickMenuPrivate::SyncPolicy' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Sync = Kee[int](0)
    DoNotSync = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMenu)
  @overload(NoneType)
  def get(menu: Optional[QQuickMenu]) -> Optional[QQuickMenuPrivate]:
    """
    Calls Qt's 'QQuickMenuPrivate *QQuickMenuPrivate::get(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#get

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMenuPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuPrivate *QQuickMenuPrivate::get(QQuickMenu *menu)
    address = Rituals.call(
        'ritual_ZN17QQuickMenuPrivate3getEP10QQuickMenu',
        CuteMixin._addressOf(menu),
    )
    return QQuickMenuPrivate._cuteAt(address)

  @staticmethod
  @overload(QQuickMenu)
  @overload(NoneType)
  def recursivelyCreateNativeMenuItems(menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void
    QQuickMenuPrivate::recursivelyCreateNativeMenuItems(QQuickMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::recursivelyCreateNativeMenuItems(QQuickMenu
    #      *menu)
    Rituals.call(
        'ritual_ZN17QQuickMenuPrivate32recursivelyCreateNativeMenuItemsEP10'
        'QQuickMenu',
        CuteMixin._addressOf(menu),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuPrivate'

  #  A C++ QQuickMenuPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuPrivate'

  #  The functions Qt calls itself that QQuickMenuPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemChildAdded': (
          ('_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemSiblingOrderChanged': (
          ('_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemGeometryChanged': (
          ('_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickItem20QQui'
           'ckGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
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

  def maybeNativeHandle(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QQuickMenuPrivate::maybeNativeHandle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#maybeNativeHandle

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QQuickMenuPrivate::maybeNativeHandle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate17maybeNativeHandleEv',
    )
    from ..QtGui import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def rootMenu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuPrivate::rootMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#rootMenu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuPrivate::rootMenu() const
    address = self.uglySide.call('ritual_ZNK17QQuickMenuPrivate8rootMenuEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def useNativeMenu(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::useNativeMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#useNativeMenu
    """
    #  bool QQuickMenuPrivate::useNativeMenu() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate13useNativeMenuEv',
    )

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuPrivate::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuPrivate::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate6itemAtEi', index,
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem, QPointF)
  @overload(NoneType, QPointF)
  def blockInput(self, item: Optional[QQuickItem], point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::blockInput(QQuickItem *item, const
    QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#blockInput

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickMenuPrivate::blockInput(QQuickItem *item, const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK17QQuickMenuPrivate10blockInputEP10QQuickItemRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QQuickMenuPrivate10blockInputEP10QQuickItemRK7QP'
          'ointF')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._valueOf(point, 'QPointF'),
    )

  def currentSubMenu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuPrivate::currentSubMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#currentSubMenu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuPrivate::currentSubMenu() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate14currentSubMenuEv',
    )
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def firstEnabledMenuItem(self) -> Optional[QQuickMenuItem]:
    """
    Calls Qt's 'QQuickMenuItem *QQuickMenuPrivate::firstEnabledMenuItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#firstEnabledMenuItem

    Returns
    -------

    Optional[QQuickMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItem *QQuickMenuPrivate::firstEnabledMenuItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate20firstEnabledMenuItemEv',
    )
    from . import QQuickMenuItem
    return QQuickMenuItem._cuteAt(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickMenuPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickMenuPrivate::defaultPalette() const
    ritual = 'ritual_ZNK17QQuickMenuPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickMenuPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def resolvedPopupType(self) -> QQuickPopup.PopupType:
    """
    Calls Qt's 'QQuickPopup::PopupType QQuickMenuPrivate::resolvedPopupType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#resolvedPopupType

    Returns
    -------

    QQuickPopup.PopupType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickPopup.PopupType(number)' gives.
    """
    #  QQuickPopup::PopupType QQuickMenuPrivate::resolvedPopupType() const
    ritual = 'ritual_ZNK17QQuickMenuPrivate17resolvedPopupTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickMenuPrivate17resolvedPopupTypeEv'
    return QQuickPopup.PopupType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setNativeMenuVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::setNativeMenuVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#setNativeMenuVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickMenuPrivate::setNativeMenuVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate20setNativeMenuVisibleEb', visible,
    )

  @overload(QQuickMenu)
  @overload(NoneType)
  def setParentMenu(self, parent: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::setParentMenu(QQuickMenu *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#setParentMenu

    Parameters
    ----------

    parent : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::setParentMenu(QQuickMenu *parent)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate13setParentMenuEP10QQuickMenu',
        self._addressOf(parent),
    )

  @overload(int, Qt.FocusReason)
  def setCurrentIndex(self, index: int, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::setCurrentIndex(int index,
    Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickMenuPrivate::setCurrentIndex(int index, Qt::FocusReason
    #      reason)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate15setCurrentIndexEiN2Qt11FocusReasonE',
        index, reason.value,
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
    Notes what was given, for Qt's 'QQuickMenuPrivate::QQuickMenuPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#QQuickMenuPrivate
    """
    #  QQuickMenuPrivate::QQuickMenuPrivate()
    self._noteCreation(QQuickMenuPrivate, lambda: Rituals.call(
        'ritual_ZN17QQuickMenuPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#q_func

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickMenuPrivate6q_funcEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#init
    """
    #  void QQuickMenuPrivate::init()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate4initEv')

  def nativeHandle(self) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QQuickMenuPrivate::nativeHandle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#nativeHandle

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QQuickMenuPrivate::nativeHandle()
    address = self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate12nativeHandleEv',
    )
    from ..QtGui import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  def createNativeMenu(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::createNativeMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#createNativeMenu
    """
    #  bool QQuickMenuPrivate::createNativeMenu()
    return self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate16createNativeMenuEv',
    )

  def removeNativeMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::removeNativeMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#removeNativeMenu
    """
    #  void QQuickMenuPrivate::removeNativeMenu()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate16removeNativeMenuEv')

  def syncWithNativeMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::syncWithNativeMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#syncWithNativeMenu
    """
    #  void QQuickMenuPrivate::syncWithNativeMenu()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate18syncWithNativeMenuEv')

  def syncWithUseNativeMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::syncWithUseNativeMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#syncWithUseNativeMenu
    """
    #  void QQuickMenuPrivate::syncWithUseNativeMenu()
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate21syncWithUseNativeMenuEv',
    )

  def makeEditMenu(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::makeEditMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#makeEditMenu
    """
    #  void QQuickMenuPrivate::makeEditMenu()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate12makeEditMenuEv')

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def insertItem(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::insertItem(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::insertItem(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate10insertItemEiP10QQuickItem',
        index, self._addressOf(item),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def maybeCreateAndInsertNativeItem(
      self,
      index: int,
      item: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::maybeCreateAndInsertNativeItem(int
    index, QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::maybeCreateAndInsertNativeItem(int index,
    #      QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate30maybeCreateAndInsertNativeItemEiP10Q'
        'QuickItem',
        index, self._addressOf(item),
    )

  @overload(int, int)
  def moveItem(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::moveItem(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#moveItem

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QQuickMenuPrivate::moveItem(int from, int to)
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate8moveItemEii', from_, to)

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  @overload(int, QQuickItem, DestructionPolicy)
  @overload(int, NoneType, DestructionPolicy)
  def removeItem(
      self,
      index: int,
      item: Optional[QQuickItem],
      destructionPolicy: DestructionPolicy = DestructionPolicy.DoNotDestroy,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::removeItem(int index, QQuickItem
    *item, DestructionPolicy destructionPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#removeItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    destructionPolicy : DestructionPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      DestructionPolicy.DoNotDestroy.
    """
    #  void QQuickMenuPrivate::removeItem(int index, QQuickItem *item,
    #      DestructionPolicy destructionPolicy)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate10removeItemEiP10QQuickItemNS_17Destru'
        'ctionPolicyE',
        index, self._addressOf(item), destructionPolicy.value,
    )

  @overload(int)
  @overload(int, SyncPolicy)
  def removeNativeItem(
      self,
      index: int,
      syncPolicy: SyncPolicy = SyncPolicy.Sync,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::removeNativeItem(int index,
    SyncPolicy syncPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#removeNativeItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    syncPolicy : SyncPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      SyncPolicy.Sync.
    """
    #  void QQuickMenuPrivate::removeNativeItem(int index, SyncPolicy
    #      syncPolicy)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate16removeNativeItemEiNS_10SyncPolicyE',
        index, syncPolicy.value,
    )

  def resetNativeData(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::resetNativeData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#resetNativeData
    """
    #  void QQuickMenuPrivate::resetNativeData()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate15resetNativeDataEv')

  def printContentModelItems(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::printContentModelItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#printContentModelItems
    """
    #  void QQuickMenuPrivate::printContentModelItems() const
    self.uglySide.call(
        'ritual_ZNK17QQuickMenuPrivate22printContentModelItemsEv',
    )

  def beginCreateItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuPrivate::beginCreateItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#beginCreateItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuPrivate::beginCreateItem()
    address = self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate15beginCreateItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def completeCreateItem(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::completeCreateItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#completeCreateItem
    """
    #  void QQuickMenuPrivate::completeCreateItem()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate18completeCreateItemEv')

  @overload(QQuickMenu)
  @overload(NoneType)
  def createItem(self, menu: Optional[QQuickMenu]) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuPrivate::createItem(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#createItem

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuPrivate::createItem(QQuickMenu *menu)
    address = self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate10createItemEP10QQuickMenu',
        self._addressOf(menu),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickAction)
  def createItem(
      self,
      action: Optional[QQuickAction],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuPrivate::createItem(QQuickAction
    *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#createItem

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuPrivate::createItem(QQuickAction *action)
    address = self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate10createItemEP12QQuickAction',
        self._addressOf(action),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def resizeItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::resizeItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#resizeItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::resizeItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate10resizeItemEP10QQuickItem',
        self._addressOf(item),
    )

  def resizeItems(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::resizeItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#resizeItems
    """
    #  void QQuickMenuPrivate::resizeItems()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate11resizeItemsEv')

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildAdded(
      self,
      item: Optional[QQuickItem],
      child: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::itemChildAdded(QQuickItem *item,
    QQuickItem *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#itemChildAdded

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::itemChildAdded(QQuickItem *item, QQuickItem
    #      *child)
    ritual = 'ritual_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1'
          '_')
    self.uglySide.call(ritual, self._addressOf(item), self._addressOf(child))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::itemSiblingOrderChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#itemSiblingOrderChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::itemSiblingOrderChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      item: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::itemParentChanged(QQuickItem *item,
    QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#itemParentChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::itemParentChanged(QQuickItem *item, QQuickItem
    #      *parent)
    ritual = (
        'ritual_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickIte'
          'mS1_')
    self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(parent),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN17QQuickMenuPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::itemGeometryChanged(QQuickItem *a0,
    QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMenuPrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickItem20Q'
        'QuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickI'
          'tem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(a0), self._valueOf(change), self._valueOf(diff),
    )

  def getPositioner(self) -> Optional[QQuickPopupPositioner]:
    """
    Calls Qt's 'QQuickPopupPositioner *QQuickMenuPrivate::getPositioner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#getPositioner

    Returns
    -------

    Optional[QQuickPopupPositioner]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupPositioner *QQuickMenuPrivate::getPositioner()
    ritual = 'ritual_ZN17QQuickMenuPrivate13getPositionerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMenuPrivate13getPositionerEv'
    address = self.uglySide.call(ritual)
    from . import QQuickPopupPositioner
    return QQuickPopupPositioner._cuteAt(address)

  def prepareEnterTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::prepareEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#prepareEnterTransition
    """
    #  bool QQuickMenuPrivate::prepareEnterTransition()
    ritual = 'ritual_ZN17QQuickMenuPrivate22prepareEnterTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMenuPrivate22prepareEnterTransitionEv'
    return self.uglySide.call(ritual)

  def prepareExitTransition(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::prepareExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#prepareExitTransition
    """
    #  bool QQuickMenuPrivate::prepareExitTransition()
    ritual = 'ritual_ZN17QQuickMenuPrivate21prepareExitTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMenuPrivate21prepareExitTransitionEv'
    return self.uglySide.call(ritual)

  @overload(QQuickItem, QPointF, int)
  @overload(NoneType, QPointF, int)
  def handlePress(
      self,
      item: Optional[QQuickItem],
      point: QPointF,
      timestamp: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::handlePress(QQuickItem *item, const
    QPointF &point, ulong timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#handlePress

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
    #  bool QQuickMenuPrivate::handlePress(QQuickItem *item, const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN17QQuickMenuPrivate11handlePressEP10QQuickItemRK7QPointFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate11handlePressEP10QQuickItemRK7QP'
          'ointFm')
    return self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QEventPoint)
  def handleReleaseWithoutGrab(self, eventPoint: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::handleReleaseWithoutGrab(const
    QEventPoint &eventPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#handleReleaseWithoutGrab

    Parameters
    ----------

    eventPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickMenuPrivate::handleReleaseWithoutGrab(const QEventPoint
    #      &eventPoint)
    ritual = (
        'ritual_ZN17QQuickMenuPrivate24handleReleaseWithoutGrabERK11QEventP'
        'oint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuPrivate24handleReleaseWithoutGrabERK11Q'
          'EventPoint')
    return self.uglySide.call(ritual, self._valueOf(eventPoint))

  def onItemHovered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::onItemHovered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#onItemHovered
    """
    #  void QQuickMenuPrivate::onItemHovered()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate13onItemHoveredEv')

  def onItemTriggered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::onItemTriggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#onItemTriggered
    """
    #  void QQuickMenuPrivate::onItemTriggered()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate15onItemTriggeredEv')

  def onItemActiveFocusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::onItemActiveFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#onItemActiveFocusChanged
    """
    #  void QQuickMenuPrivate::onItemActiveFocusChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate24onItemActiveFocusChangedEv',
    )

  def onItemVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::onItemVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#onItemVisibleChanged
    """
    #  void QQuickMenuPrivate::onItemVisibleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate20onItemVisibleChangedEv',
    )

  def updateTextPadding(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::updateTextPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#updateTextPadding
    """
    #  void QQuickMenuPrivate::updateTextPadding()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate17updateTextPaddingEv')

  def updateCollapsedSeparators(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::updateCollapsedSeparators()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#updateCollapsedSeparators
    """
    #  void QQuickMenuPrivate::updateCollapsedSeparators()
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate25updateCollapsedSeparatorsEv',
    )

  def resolveParentItem(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::resolveParentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#resolveParentItem
    """
    #  void QQuickMenuPrivate::resolveParentItem()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate17resolveParentItemEv')

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def popup(self, menuItem: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::popup(QQuickItem *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuprivate.html#popup

    Parameters
    ----------

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenuPrivate::popup(QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate5popupEP10QQuickItem',
        self._addressOf(menuItem),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def propagateKeyEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::propagateKeyEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#propagateKeyEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuPrivate::propagateKeyEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate17propagateKeyEventEP9QKeyEvent',
        self._addressOf(event),
    )

  def startHoverTimer(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::startHoverTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#startHoverTimer
    """
    #  void QQuickMenuPrivate::startHoverTimer()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate15startHoverTimerEv')

  def stopHoverTimer(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::stopHoverTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#stopHoverTimer
    """
    #  void QQuickMenuPrivate::stopHoverTimer()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate14stopHoverTimerEv')

  def activateNextItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::activateNextItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#activateNextItem
    """
    #  bool QQuickMenuPrivate::activateNextItem()
    return self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate16activateNextItemEv',
    )

  def activatePreviousItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuPrivate::activatePreviousItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#activatePreviousItem
    """
    #  bool QQuickMenuPrivate::activatePreviousItem()
    return self.uglySide.call(
        'ritual_ZN17QQuickMenuPrivate20activatePreviousItemEv',
    )

  def resetContentItem(self) -> None:
    """
    Calls Qt's 'void QQuickMenuPrivate::resetContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuprivate.html#resetContentItem
    """
    #  void QQuickMenuPrivate::resetContentItem()
    self.uglySide.call('ritual_ZN17QQuickMenuPrivate16resetContentItemEv')

  @staticmethod
  def contentData_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickMenuPrivate::contentData_append(QQmlListProperty<QObject> *prop,
    QObject *obj)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuPrivate.contentData_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickMenuPrivate::contentData_append(QQmlListProperty<QObject> "
        "*prop, QObject *obj)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def contentData_at(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQuickMenuPrivate::contentData_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuPrivate.contentData_at' has no cute function yet. Qt's "
        "'QObject "
        "*QQuickMenuPrivate::contentData_at(QQmlListProperty<QObject> "
        "*prop, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def contentData_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickMenuPrivate::contentData_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuPrivate.contentData_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuickMenuPrivate::contentData_clear(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def contentData_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickMenuPrivate::contentData_count(QQmlListProperty<QObject> *prop)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMenuPrivate.contentData_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickMenuPrivate::contentData_count(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")
