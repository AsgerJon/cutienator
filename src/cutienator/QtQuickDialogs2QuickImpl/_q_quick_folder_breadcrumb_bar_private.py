"""
QQuickFolderBreadcrumbBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderBreadcrumbBarPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QUrl, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickFileDialogImpl, QQuickFolderBreadcrumbBar
  from . import QQuickFolderDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderBreadcrumbBarPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFolderBreadcrumbBarPrivate: a plain Python
  object standing in front of one C++ QQuickFolderBreadcrumbBarPrivate.

  What exists
  -----------

  Every function of Qt's QQuickFolderBreadcrumbBarPrivate that has a ritual
  and that Python can call so far, 30 names in all: 'q_func',
  'createDelegateItem', 'folderBaseName', 'crumbPathsForFolder',
  'repopulate', 'crumbClicked', 'folderChanged', 'cancelUpButton',
  'executeUpButton', 'goUp', 'cancelTextField', 'executeTextField',
  'toggleTextFieldVisibility', 'textFieldAccepted',
  'textFieldVisibleChanged', 'textFieldActiveFocusChanged',
  'handleTextFieldShown', 'handleTextFieldHidden', 'ungrabEditPathShortcut',
  'asFileDialog', 'asFolderDialog', 'isFileDialog', 'dialogFolder',
  'setDialogFolder', 'getContentWidth', 'getContentHeight', 'resizeContent',
  'itemGeometryChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFolderBreadcrumbBar
    *QQuickFolderBreadcrumbBarPrivate::q_func() const': takes in Python what
    'QQuickFolderBreadcrumbBar *QQuickFolderBreadcrumbBarPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickFolderBreadcrumbBarPrivate is created at the first use, not
    by 'QQuickFolderBreadcrumbBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderBreadcrumbBarPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def folderBaseName(folderPath: str) -> str:
    """
    Calls Qt's 'QString
    QQuickFolderBreadcrumbBarPrivate::folderBaseName(const QString
    &folderPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    folderPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFolderBreadcrumbBarPrivate::folderBaseName(const QString
    #      &folderPath)
    return Rituals.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate14folderBaseNameERK7QSt'
        'ring',
        folderPath,
    )

  @staticmethod
  @overload(QUrl)
  def crumbPathsForFolder(folder: QUrl) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQuickFolderBreadcrumbBarPrivate::crumbPathsForFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QQuickFolderBreadcrumbBarPrivate::crumbPathsForFolder(const QUrl
    #      &folder)
    address = Rituals.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate19crumbPathsForFolderER'
        'K4QUrl',
        CuteMixin._valueOf(folder),
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderBreadcrumbBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def asFileDialog(self) -> Optional[QQuickFileDialogImpl]:
    """
    Calls Qt's 'QQuickFileDialogImpl
    *QQuickFolderBreadcrumbBarPrivate::asFileDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#asFileDialog

    Returns
    -------

    Optional[QQuickFileDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImpl *QQuickFolderBreadcrumbBarPrivate::asFileDialog()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12asFileDialogEv',
    )
    from . import QQuickFileDialogImpl
    return QQuickFileDialogImpl._cuteAt(address)

  def asFolderDialog(self) -> Optional[QQuickFolderDialogImpl]:
    """
    Calls Qt's 'QQuickFolderDialogImpl
    *QQuickFolderBreadcrumbBarPrivate::asFolderDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Returns
    -------

    Optional[QQuickFolderDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImpl
    #      *QQuickFolderBreadcrumbBarPrivate::asFolderDialog() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate14asFolderDialogEv',
    )
    from . import QQuickFolderDialogImpl
    return QQuickFolderDialogImpl._cuteAt(address)

  def isFileDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderBreadcrumbBarPrivate::isFileDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#isFileDialog
    """
    #  bool QQuickFolderBreadcrumbBarPrivate::isFileDialog() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12isFileDialogEv',
    )

  def dialogFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderBreadcrumbBarPrivate::dialogFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#dialogFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderBreadcrumbBarPrivate::dialogFolder() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate12dialogFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFolderBreadcrumbBarPrivate::getContentWidth()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  qreal QQuickFolderBreadcrumbBarPrivate::getContentWidth() const
    ritual = (
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate15getContentWidthEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QQuickFolderBreadcrumbBarPrivate15getContentWidt'
          'hEv')
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickFolderBreadcrumbBarPrivate::getContentHeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  qreal QQuickFolderBreadcrumbBarPrivate::getContentHeight() const
    ritual = (
        'ritual_ZNK32QQuickFolderBreadcrumbBarPrivate16getContentHeightEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QQuickFolderBreadcrumbBarPrivate16getContentHeig'
          'htEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setDialogFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::setDialogFolder(const
    QUrl &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderBreadcrumbBarPrivate::setDialogFolder(const QUrl
    #      &folder)
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate15setDialogFolderERK4QU'
        'rl',
        self._valueOf(folder),
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

  def q_func(self) -> Optional[QQuickFolderBreadcrumbBar]:
    """
    Calls Qt's 'QQuickFolderBreadcrumbBar
    *QQuickFolderBreadcrumbBarPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#q_func

    Returns
    -------

    Optional[QQuickFolderBreadcrumbBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderBreadcrumbBar *QQuickFolderBreadcrumbBarPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate6q_funcEv',
    )
    from . import QQuickFolderBreadcrumbBar
    return QQuickFolderBreadcrumbBar._cuteAt(address)

  @overload(QQmlComponent, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def createDelegateItem(
      self,
      component: Optional[QQmlComponent],
      initialProperties: QMap[str, QVariant],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickFolderBreadcrumbBarPrivate::createDelegateItem(QQmlComponent
    *component, const QVariantMap &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

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
    #  QQuickItem *QQuickFolderBreadcrumbBarPrivate::createDelegateItem(
    #      QQmlComponent *component, const QVariantMap &initialProperties)
    address = self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate18createDelegateItemEP1'
        '3QQmlComponentRK4QMapI7QString8QVariantE',
        self._addressOf(component), self._valueOf(initialProperties),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def repopulate(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::repopulate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#repopulate
    """
    #  void QQuickFolderBreadcrumbBarPrivate::repopulate()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate10repopulateEv',
    )

  def crumbClicked(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::crumbClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#crumbClicked
    """
    #  void QQuickFolderBreadcrumbBarPrivate::crumbClicked()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate12crumbClickedEv',
    )

  def folderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::folderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::folderChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate13folderChangedEv',
    )

  def cancelUpButton(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::cancelUpButton()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::cancelUpButton()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate14cancelUpButtonEv',
    )

  @overload()
  @overload(bool)
  def executeUpButton(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::executeUpButton(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickFolderBreadcrumbBarPrivate::executeUpButton(bool complete)
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate15executeUpButtonEb',
        complete,
    )

  def goUp(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::goUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html#goUp
    """
    #  void QQuickFolderBreadcrumbBarPrivate::goUp()
    self.uglySide.call('ritual_ZN32QQuickFolderBreadcrumbBarPrivate4goUpEv')

  def cancelTextField(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::cancelTextField()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::cancelTextField()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate15cancelTextFieldEv',
    )

  @overload()
  @overload(bool)
  def executeTextField(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::executeTextField(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickFolderBreadcrumbBarPrivate::executeTextField(bool complete)
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate16executeTextFieldEb',
        complete,
    )

  def toggleTextFieldVisibility(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::toggleTextFieldVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::toggleTextFieldVisibility()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate25toggleTextFieldVisibi'
        'lityEv',
    )

  def textFieldAccepted(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::textFieldAccepted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::textFieldAccepted()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate17textFieldAcceptedEv',
    )

  def textFieldVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::textFieldVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::textFieldVisibleChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate23textFieldVisibleChang'
        'edEv',
    )

  def textFieldActiveFocusChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::textFieldActiveFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::textFieldActiveFocusChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate27textFieldActiveFocusC'
        'hangedEv',
    )

  def handleTextFieldShown(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::handleTextFieldShown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::handleTextFieldShown()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate20handleTextFieldShownE'
        'v',
    )

  def handleTextFieldHidden(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::handleTextFieldHidden()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::handleTextFieldHidden()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate21handleTextFieldHidden'
        'Ev',
    )

  def ungrabEditPathShortcut(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::ungrabEditPathShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::ungrabEditPathShortcut()
    self.uglySide.call(
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate22ungrabEditPathShortcu'
        'tEv',
    )

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBarPrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html
    """
    #  void QQuickFolderBreadcrumbBarPrivate::resizeContent()
    ritual = 'ritual_ZN32QQuickFolderBreadcrumbBarPrivate13resizeContentEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate13resizeContentEv')
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

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
    #  void QQuickFolderBreadcrumbBarPrivate::itemGeometryChanged(QQuickItem
    #      *item, QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate19itemGeometryChangedEP'
        '10QQuickItem20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate19itemGeometryCha'
          'ngedEP10QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBarPrivate::itemImplicitWidthChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate24itemImplicitWidthChan'
        'gedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate24itemImplicitWid'
          'thChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBarPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbarprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBarPrivate::itemImplicitHeightChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN32QQuickFolderBreadcrumbBarPrivate25itemImplicitHeightCha'
        'ngedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickFolderBreadcrumbBarPrivate25itemImplicitHei'
          'ghtChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))
