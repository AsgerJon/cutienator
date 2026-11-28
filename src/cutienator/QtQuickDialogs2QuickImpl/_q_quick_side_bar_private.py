"""
QQuickSideBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSideBarPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QStandardPaths

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF, QSize, QUrl, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickSideBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickSideBar = WAIT['QQuickSideBar']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSideBarPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickSideBarPrivate: a plain Python object standing
  in front of one C++ QQuickSideBarPrivate.

  What exists
  -----------

  Every function of Qt's QQuickSideBarPrivate that has a ritual and that
  Python can call so far, 28 names in all: 'q_func', 'get',
  'createDelegateItem', 'repopulate', 'buttonClicked', 'dialogFolder',
  'setDialogFolder', 'displayNameFromFolderPath', 'folderIconSource',
  'dialogIconSize', 'folderChanged', 'readSettings', 'writeSettings',
  'addFavorite', 'removeFavorite', 'showAddFavoriteDelegate',
  'setShowAddFavoriteDelegate', 'addFavoriteDelegateHovered',
  'setAddFavoriteDelegateHovered', 'addFavoriteIconUrl', 'initContextMenu',
  'handleContextMenuRequested', 'handleRemoveAction', 'getContentWidth',
  'getContentHeight', 'itemGeometryChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickSideBar *QQuickSideBarPrivate::q_func() const': takes
    in Python what 'QQuickSideBar *QQuickSideBarPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickSideBarPrivate is created at the first use, not by
    'QQuickSideBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSideBarPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickSideBar)
  @overload(NoneType)
  def get(
      sidebar: Optional[QQuickSideBar],
  ) -> Optional[QQuickSideBarPrivate]:
    """
    Calls Qt's 'QQuickSideBarPrivate *QQuickSideBarPrivate::get(QQuickSideBar
    *sidebar)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebarprivate.html#get

    Parameters
    ----------

    sidebar : Optional[QQuickSideBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSideBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSideBarPrivate *QQuickSideBarPrivate::get(QQuickSideBar
    #      *sidebar)
    address = Rituals.call(
        'ritual_ZN20QQuickSideBarPrivate3getEP13QQuickSideBar',
        CuteMixin._addressOf(sidebar),
    )
    return QQuickSideBarPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSideBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dialogFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickSideBarPrivate::dialogFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#dialogFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickSideBarPrivate::dialogFolder() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate12dialogFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload()
  def folderIconSource(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickSideBarPrivate::folderIconSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#folderIconSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickSideBarPrivate::folderIconSource() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate16folderIconSourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QStandardPaths.StandardLocation)
  def folderIconSource(
      self,
      stdLocation: QStandardPaths.StandardLocation,
  ) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQuickSideBarPrivate::folderIconSource(QStandardPaths::StandardLocation
    stdLocation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#folderIconSource

    Parameters
    ----------

    stdLocation : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickSideBarPrivate::folderIconSource(QStandardPaths::
    #      StandardLocation stdLocation) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate16folderIconSourceEN14QStandardPat'
        'hs16StandardLocationE',
        stdLocation.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def dialogIconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickSideBarPrivate::dialogIconSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#dialogIconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickSideBarPrivate::dialogIconSize() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate14dialogIconSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def showAddFavoriteDelegate(self) -> bool:
    """
    Calls Qt's 'bool QQuickSideBarPrivate::showAddFavoriteDelegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#showAddFavoriteDelegate
    """
    #  bool QQuickSideBarPrivate::showAddFavoriteDelegate() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate23showAddFavoriteDelegateEv',
    )

  def addFavoriteDelegateHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickSideBarPrivate::addFavoriteDelegateHovered()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html
    """
    #  bool QQuickSideBarPrivate::addFavoriteDelegateHovered() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate26addFavoriteDelegateHoveredEv',
    )

  def addFavoriteIconUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickSideBarPrivate::addFavoriteIconUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#addFavoriteIconUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickSideBarPrivate::addFavoriteIconUrl() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSideBarPrivate18addFavoriteIconUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickSideBarPrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#getContentWidth
    """
    #  qreal QQuickSideBarPrivate::getContentWidth() const
    ritual = 'ritual_ZNK20QQuickSideBarPrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickSideBarPrivate15getContentWidthEv'
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickSideBarPrivate::getContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#getContentHeight
    """
    #  qreal QQuickSideBarPrivate::getContentHeight() const
    ritual = 'ritual_ZNK20QQuickSideBarPrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickSideBarPrivate16getContentHeightEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setDialogFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::setDialogFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#setDialogFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickSideBarPrivate::setDialogFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate15setDialogFolderERK4QUrl',
        self._valueOf(folder),
    )

  @overload(bool)
  def setShowAddFavoriteDelegate(self, show: bool) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::setShowAddFavoriteDelegate(bool
    show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QQuickSideBarPrivate::setShowAddFavoriteDelegate(bool show)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate26setShowAddFavoriteDelegateEb',
        show,
    )

  @overload(bool)
  def setAddFavoriteDelegateHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::setAddFavoriteDelegateHovered(bool
    hovered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickSideBarPrivate::setAddFavoriteDelegateHovered(bool hovered)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate29setAddFavoriteDelegateHoveredEb',
        hovered,
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

  def q_func(self) -> Optional[QQuickSideBar]:
    """
    Calls Qt's 'QQuickSideBar *QQuickSideBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebarprivate.html#q_func

    Returns
    -------

    Optional[QQuickSideBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSideBar *QQuickSideBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickSideBarPrivate6q_funcEv')
    from . import QQuickSideBar
    return QQuickSideBar._cuteAt(address)

  @overload(QQmlComponent, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def createDelegateItem(
      self,
      component: Optional[QQmlComponent],
      initialProperties: QMap[str, QVariant],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickSideBarPrivate::createDelegateItem(QQmlComponent *component, const
    QVariantMap &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#createDelegateItem

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSideBarPrivate::createDelegateItem(QQmlComponent
    #      *component, const QVariantMap &initialProperties)
    address = self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate18createDelegateItemEP13QQmlCompone'
        'ntRK4QMapI7QString8QVariantE',
        self._addressOf(component), self._valueOf(initialProperties),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def repopulate(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::repopulate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#repopulate
    """
    #  void QQuickSideBarPrivate::repopulate()
    self.uglySide.call('ritual_ZN20QQuickSideBarPrivate10repopulateEv')

  def buttonClicked(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::buttonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#buttonClicked
    """
    #  void QQuickSideBarPrivate::buttonClicked()
    self.uglySide.call('ritual_ZN20QQuickSideBarPrivate13buttonClickedEv')

  @overload(str)
  def displayNameFromFolderPath(self, filePath: str) -> str:
    """
    Calls Qt's 'QString QQuickSideBarPrivate::displayNameFromFolderPath(const
    QString &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSideBarPrivate::displayNameFromFolderPath(const QString
    #      &filePath)
    return self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate25displayNameFromFolderPathERK7QStr'
        'ing',
        filePath,
    )

  def folderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::folderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#folderChanged
    """
    #  void QQuickSideBarPrivate::folderChanged()
    self.uglySide.call('ritual_ZN20QQuickSideBarPrivate13folderChangedEv')

  def readSettings(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::readSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#readSettings
    """
    #  void QQuickSideBarPrivate::readSettings()
    self.uglySide.call('ritual_ZN20QQuickSideBarPrivate12readSettingsEv')

  def writeSettings(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::writeSettings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#writeSettings
    """
    #  void QQuickSideBarPrivate::writeSettings() const
    self.uglySide.call('ritual_ZNK20QQuickSideBarPrivate13writeSettingsEv')

  @overload(QUrl)
  def addFavorite(self, favorite: QUrl) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::addFavorite(const QUrl
    &favorite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#addFavorite

    Parameters
    ----------

    favorite : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickSideBarPrivate::addFavorite(const QUrl &favorite)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate11addFavoriteERK4QUrl',
        self._valueOf(favorite),
    )

  @overload(QUrl)
  def removeFavorite(self, favorite: QUrl) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::removeFavorite(const QUrl
    &favorite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#removeFavorite

    Parameters
    ----------

    favorite : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickSideBarPrivate::removeFavorite(const QUrl &favorite)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate14removeFavoriteERK4QUrl',
        self._valueOf(favorite),
    )

  def initContextMenu(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::initContextMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#initContextMenu
    """
    #  void QQuickSideBarPrivate::initContextMenu()
    self.uglySide.call('ritual_ZN20QQuickSideBarPrivate15initContextMenuEv')

  @overload(QPointF)
  def handleContextMenuRequested(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::handleContextMenuRequested(QPointF
    pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickSideBarPrivate::handleContextMenuRequested(QPointF pos)
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate26handleContextMenuRequestedE7QPoin'
        'tF',
        self._valueOf(pos, 'QPointF'),
    )

  def handleRemoveAction(self) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::handleRemoveAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#handleRemoveAction
    """
    #  void QQuickSideBarPrivate::handleRemoveAction()
    self.uglySide.call(
        'ritual_ZN20QQuickSideBarPrivate18handleRemoveActionEv',
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickSideBarPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickSideBarPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN20QQuickSideBarPrivate19itemGeometryChangedEP10QQuickItem'
        '20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSideBarPrivate19itemGeometryChangedEP10QQui'
          'ckItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickSideBarPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickSideBarPrivate24itemImplicitWidthChangedEP10QQuic'
        'kItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSideBarPrivate24itemImplicitWidthChangedEP1'
          '0QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickSideBarPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickSideBarPrivate25itemImplicitHeightChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSideBarPrivate25itemImplicitHeightChangedEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))
