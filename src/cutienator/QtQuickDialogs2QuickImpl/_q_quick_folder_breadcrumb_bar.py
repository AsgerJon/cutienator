"""
QQuickFolderBreadcrumbBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderBreadcrumbBar to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QFont, QKeyEvent
  from ..QtQml import QQmlComponent
  from . import QQuickFolderBreadcrumbBarPrivate
  from ..QtQuickTemplates2 import QQuickAbstractButton, QQuickDialog
  from ..QtQuickTemplates2 import QQuickTextField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickDialog = WAIT['QQuickDialog']
  QQuickTextField = WAIT['QQuickTextField']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderBreadcrumbBar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFolderBreadcrumbBar: a plain Python object
  standing in front of one C++ QQuickFolderBreadcrumbBar.

  What exists
  -----------

  Every function of Qt's QQuickFolderBreadcrumbBar that has a ritual and that
  Python can call so far, 28 names in all: 'metaObject', 'tr', 'dialog',
  'setDialog', 'buttonDelegate', 'setButtonDelegate', 'separatorDelegate',
  'setSeparatorDelegate', 'upButton', 'setUpButton', 'upButtonSpacing',
  'setUpButtonSpacing', 'textField', 'setTextField', 'dialogChanged',
  'buttonDelegateChanged', 'separatorDelegateChanged', 'upButtonChanged',
  'upButtonSpacingChanged', 'textFieldChanged', 'event', 'keyPressEvent',
  'componentComplete', 'itemChange', 'isContent', 'defaultFont',
  'accessibleRole', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFolderBreadcrumbBar::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickFolderBreadcrumbBar::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickFolderBreadcrumbBarPrivate
    *QQuickFolderBreadcrumbBar::d_func() const': takes in Python what
    'QQuickFolderBreadcrumbBarPrivate *QQuickFolderBreadcrumbBar::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFolderBreadcrumbBar is created at the first use, not by
    'QQuickFolderBreadcrumbBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderBreadcrumbBar.
  - Qt tells when it has removed the C++ QQuickFolderBreadcrumbBar. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickFolderBreadcrumbBar::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#tr

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
    #  QString QQuickFolderBreadcrumbBar::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderBreadcrumbBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFolderBreadcrumbBar::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderBreadcrumbBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickFolderBreadcrumbBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dialog(self) -> Optional[QQuickDialog]:
    """
    Calls Qt's 'QQuickDialog *QQuickFolderBreadcrumbBar::dialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#dialog

    Returns
    -------

    Optional[QQuickDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialog *QQuickFolderBreadcrumbBar::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickFolderBreadcrumbBar6dialogEv',
    )
    from ..QtQuickTemplates2 import QQuickDialog
    return QQuickDialog._cuteAt(address)

  def upButtonSpacing(self) -> int:
    """
    Calls Qt's 'int QQuickFolderBreadcrumbBar::upButtonSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#upButtonSpacing
    """
    #  int QQuickFolderBreadcrumbBar::upButtonSpacing() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickFolderBreadcrumbBar15upButtonSpacingEv',
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickFolderBreadcrumbBar::isContent(QQuickItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFolderBreadcrumbBar::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK25QQuickFolderBreadcrumbBar9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QQuickFolderBreadcrumbBar9isContentEP10QQuickIte'
          'm')
    return self.uglySide.call(ritual, self._addressOf(item))

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFolderBreadcrumbBar::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFolderBreadcrumbBar::defaultFont() const
    ritual = 'ritual_ZNK25QQuickFolderBreadcrumbBar11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QQuickFolderBreadcrumbBar11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickFolderBreadcrumbBar::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickFolderBreadcrumbBar::accessibleRole() const
    ritual = 'ritual_ZNK25QQuickFolderBreadcrumbBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QQuickFolderBreadcrumbBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialog)
  @overload(NoneType)
  def setDialog(self, dialog: Optional[QQuickDialog]) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::setDialog(QQuickDialog
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#setDialog

    Parameters
    ----------

    dialog : Optional[QQuickDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::setDialog(QQuickDialog *dialog)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar9setDialogEP12QQuickDialog',
        self._addressOf(dialog),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setButtonDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBar::setButtonDelegate(QQmlComponent *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#setButtonDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::setButtonDelegate(QQmlComponent
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar17setButtonDelegateEP13QQmlCom'
        'ponent',
        self._addressOf(delegate),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setSeparatorDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBar::setSeparatorDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::setSeparatorDelegate(QQmlComponent
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar20setSeparatorDelegateEP13QQml'
        'Component',
        self._addressOf(delegate),
    )

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def setUpButton(self, upButton: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickFolderBreadcrumbBar::setUpButton(QQuickAbstractButton *upButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#setUpButton

    Parameters
    ----------

    upButton : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::setUpButton(QQuickAbstractButton
    #      *upButton)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar11setUpButtonEP20QQuickAbstrac'
        'tButton',
        self._addressOf(upButton),
    )

  @overload(int)
  def setUpButtonSpacing(self, upButtonSpacing: int) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::setUpButtonSpacing(int
    upButtonSpacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#setUpButtonSpacing

    Parameters
    ----------

    upButtonSpacing : int
      Passed on as it is.
    """
    #  void QQuickFolderBreadcrumbBar::setUpButtonSpacing(int
    #      upButtonSpacing)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar18setUpButtonSpacingEi',
        upButtonSpacing,
    )

  @overload(QQuickTextField)
  @overload(NoneType)
  def setTextField(self, textField: Optional[QQuickTextField]) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::setTextField(QQuickTextField
    *textField)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#setTextField

    Parameters
    ----------

    textField : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::setTextField(QQuickTextField
    #      *textField)
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar12setTextFieldEP15QQuickTextFi'
        'eld',
        self._addressOf(textField),
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
    'QQuickFolderBreadcrumbBar::QQuickFolderBreadcrumbBar(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFolderBreadcrumbBar::QQuickFolderBreadcrumbBar(QQuickItem
    #      *parent)
    self._noteCreation(QQuickFolderBreadcrumbBar, lambda: Rituals.call(
        'ritual_ZN25QQuickFolderBreadcrumbBarC1EP10QQuickItem',
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

  def buttonDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickFolderBreadcrumbBar::buttonDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#buttonDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickFolderBreadcrumbBar::buttonDelegate()
    address = self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar14buttonDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def separatorDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *QQuickFolderBreadcrumbBar::separatorDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#separatorDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickFolderBreadcrumbBar::separatorDelegate()
    address = self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar17separatorDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def upButton(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton *QQuickFolderBreadcrumbBar::upButton()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#upButton

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton *QQuickFolderBreadcrumbBar::upButton()
    address = self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar8upButtonEv',
    )
    from ..QtQuickTemplates2 import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def textField(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField *QQuickFolderBreadcrumbBar::textField()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#textField

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickFolderBreadcrumbBar::textField()
    address = self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar9textFieldEv',
    )
    from ..QtQuickTemplates2 import QQuickTextField
    return QQuickTextField._cuteAt(address)

  def dialogChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::dialogChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#dialogChanged
    """
    #  void QQuickFolderBreadcrumbBar::dialogChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar13dialogChangedEv',
    )

  def buttonDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::buttonDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html
    """
    #  void QQuickFolderBreadcrumbBar::buttonDelegateChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar21buttonDelegateChangedEv',
    )

  def separatorDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::separatorDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html
    """
    #  void QQuickFolderBreadcrumbBar::separatorDelegateChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar24separatorDelegateChangedEv',
    )

  def upButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::upButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#upButtonChanged
    """
    #  void QQuickFolderBreadcrumbBar::upButtonChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar15upButtonChangedEv',
    )

  def upButtonSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::upButtonSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html
    """
    #  void QQuickFolderBreadcrumbBar::upButtonSpacingChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar22upButtonSpacingChangedEv',
    )

  def textFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::textFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#textFieldChanged
    """
    #  void QQuickFolderBreadcrumbBar::textFieldChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar16textFieldChangedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickFolderBreadcrumbBar::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFolderBreadcrumbBar::event(QEvent *event)
    ritual = 'ritual_ZN25QQuickFolderBreadcrumbBar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickFolderBreadcrumbBar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::keyPressEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderBreadcrumbBar::keyPressEvent(QKeyEvent *event)
    ritual = (
        'ritual_ZN25QQuickFolderBreadcrumbBar13keyPressEventEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickFolderBreadcrumbBar13keyPressEventEP9QKeyEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#componentComplete
    """
    #  void QQuickFolderBreadcrumbBar::componentComplete()
    ritual = 'ritual_ZN25QQuickFolderBreadcrumbBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickFolderBreadcrumbBar17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickFolderBreadcrumbBar::itemChange(ItemChange change,
    const ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickFolderBreadcrumbBar::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN25QQuickFolderBreadcrumbBar10itemChangeEN10QQuickItem10It'
        'emChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickFolderBreadcrumbBar10itemChangeEN10QQuickIt'
          'em10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickFolderBreadcrumbBarPrivate]:
    """
    Calls Qt's 'QQuickFolderBreadcrumbBarPrivate
    *QQuickFolderBreadcrumbBar::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderbreadcrumbbar.html#d_func

    Returns
    -------

    Optional[QQuickFolderBreadcrumbBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderBreadcrumbBarPrivate *QQuickFolderBreadcrumbBar::d_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickFolderBreadcrumbBar6d_funcEv',
    )
    from . import QQuickFolderBreadcrumbBarPrivate
    return QQuickFolderBreadcrumbBarPrivate._cuteAt(address)
