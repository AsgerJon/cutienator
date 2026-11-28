"""
QQStyleKitFont binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitFont to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from ..QtQuickTemplates2 import QQuickTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont


class QQStyleKitFont(QObject):
  """
  The cute side of Qt's QQStyleKitFont: a plain Python object standing in
  front of one C++ QQStyleKitFont.

  It is built on the cute 'QObject', as Qt's QQStyleKitFont is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitFont that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'system', 'button', 'checkBox',
  'comboBox', 'groupBox', 'itemDelegate', 'label', 'radioButton', 'spinBox',
  'switchControl', 'tabBar', 'textArea', 'textField', 'toolBar',
  'fallbackFont', 'systemChanged', 'buttonChanged', 'checkBoxChanged',
  'comboBoxChanged', 'groupBoxChanged', 'itemDelegateChanged',
  'labelChanged', 'radioButtonChanged', 'spinBoxChanged',
  'switchControlChanged', 'tabBarChanged', 'textAreaChanged',
  'textFieldChanged', 'toolBarChanged', 'fallbackFontChanged',
  'fontForScope', 'isSet', 'markSet'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitFont::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQStyleKitFont::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  22 of the 58 functions Qt declares: 16 leans on 'QQStyleKitFont; 2 not a
  gap; 2 forbidden; 1 takes or gives a type that cannot be passed yet; 1
  leans on 'vtable for QQStyleKitFont', which Qt's source does not mark for
  use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitFont is created at the first use, not by
    'QQStyleKitFont(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitFont.
  - Qt tells when it has removed the C++ QQStyleKitFont. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitFont that has no cute function yet,
    '__init__', 'setButton', 'setCheckBox', 'setComboBox', 'setFallbackFont',
    'setFontForScope', 'setGroupBox', 'setItemDelegate', 'setLabel',
    'setRadioButton', 'setSpinBox', 'setSwitchControl', 'setSystem',
    'setTabBar', 'setTextArea', 'setTextField', 'setToolBar', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitFont'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitFont::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitFont::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def system(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::system() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#system

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::system() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont6systemEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def button(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#button

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::button() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont6buttonEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def checkBox(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::checkBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#checkBox

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::checkBox() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont8checkBoxEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def comboBox(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::comboBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#comboBox

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::comboBox() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont8comboBoxEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def groupBox(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::groupBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#groupBox

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::groupBox() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont8groupBoxEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def itemDelegate(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::itemDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#itemDelegate

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::itemDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK14QQStyleKitFont12itemDelegateEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def label(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#label

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::label() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont5labelEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def radioButton(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::radioButton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#radioButton

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::radioButton() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont11radioButtonEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def spinBox(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::spinBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#spinBox

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::spinBox() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont7spinBoxEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def switchControl(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::switchControl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#switchControl

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::switchControl() const
    address = self.uglySide.call(
        'ritual_ZNK14QQStyleKitFont13switchControlEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def tabBar(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::tabBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#tabBar

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::tabBar() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont6tabBarEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def textArea(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::textArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#textArea

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::textArea() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont8textAreaEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def textField(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::textField() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#textField

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::textField() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont9textFieldEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def toolBar(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::toolBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#toolBar

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::toolBar() const
    address = self.uglySide.call('ritual_ZNK14QQStyleKitFont7toolBarEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def fallbackFont(self) -> Optional[QQStyleKitFont]:
    """
    Calls Qt's 'QQStyleKitFont *QQStyleKitFont::fallbackFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#fallbackFont

    Returns
    -------

    Optional[QQStyleKitFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitFont *QQStyleKitFont::fallbackFont() const
    address = self.uglySide.call(
        'ritual_ZNK14QQStyleKitFont12fallbackFontEv',
    )
    return QQStyleKitFont._cuteAt(address)

  @overload(QQuickTheme.Scope)
  def fontForScope(self, scope: QQuickTheme.Scope) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#fontForScope

    Parameters
    ----------

    scope : QQuickTheme.Scope
      Passed on as its number.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
    address = self.uglySide.call(
        'ritual_ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE',
        scope.value,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(QQuickTheme.Scope)
  def isSet(self, scope: QQuickTheme.Scope) -> bool:
    """
    Calls Qt's 'bool QQStyleKitFont::isSet(QQuickTheme::Scope scope) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#isSet

    Parameters
    ----------

    scope : QQuickTheme.Scope
      Passed on as its number.
    """
    #  bool QQStyleKitFont::isSet(QQuickTheme::Scope scope) const
    return self.uglySide.call(
        'ritual_ZNK14QQStyleKitFont5isSetEN11QQuickTheme5ScopeE',
        scope.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitFont::QQStyleKitFont(QObject *parent)': leans on 'vtable
    for QQStyleKitFont', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.__init__' has no cute function yet. Qt's "
        "'QQStyleKitFont::QQStyleKitFont(QObject *parent)': leans on "
        "'vtable for QQStyleKitFont', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def systemChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::systemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#systemChanged
    """
    #  void QQStyleKitFont::systemChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont13systemChangedEv')

  def buttonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::buttonChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#buttonChanged
    """
    #  void QQStyleKitFont::buttonChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont13buttonChangedEv')

  def checkBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::checkBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#checkBoxChanged
    """
    #  void QQStyleKitFont::checkBoxChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont15checkBoxChangedEv')

  def comboBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::comboBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#comboBoxChanged
    """
    #  void QQStyleKitFont::comboBoxChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont15comboBoxChangedEv')

  def groupBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::groupBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#groupBoxChanged
    """
    #  void QQStyleKitFont::groupBoxChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont15groupBoxChangedEv')

  def itemDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::itemDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#itemDelegateChanged
    """
    #  void QQStyleKitFont::itemDelegateChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont19itemDelegateChangedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#labelChanged
    """
    #  void QQStyleKitFont::labelChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont12labelChangedEv')

  def radioButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::radioButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#radioButtonChanged
    """
    #  void QQStyleKitFont::radioButtonChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont18radioButtonChangedEv')

  def spinBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::spinBoxChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#spinBoxChanged
    """
    #  void QQStyleKitFont::spinBoxChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont14spinBoxChangedEv')

  def switchControlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::switchControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#switchControlChanged
    """
    #  void QQStyleKitFont::switchControlChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont20switchControlChangedEv')

  def tabBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::tabBarChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#tabBarChanged
    """
    #  void QQStyleKitFont::tabBarChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont13tabBarChangedEv')

  def textAreaChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::textAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#textAreaChanged
    """
    #  void QQStyleKitFont::textAreaChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont15textAreaChangedEv')

  def textFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::textFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#textFieldChanged
    """
    #  void QQStyleKitFont::textFieldChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont16textFieldChangedEv')

  def toolBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::toolBarChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#toolBarChanged
    """
    #  void QQStyleKitFont::toolBarChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont14toolBarChangedEv')

  def fallbackFontChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::fallbackFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitfont.html#fallbackFontChanged
    """
    #  void QQStyleKitFont::fallbackFontChanged()
    self.uglySide.call('ritual_ZN14QQStyleKitFont19fallbackFontChangedEv')

  @overload(QQuickTheme.Scope)
  def markSet(self, scope: QQuickTheme.Scope) -> None:
    """
    Calls Qt's 'void QQStyleKitFont::markSet(QQuickTheme::Scope scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitfont.html#markSet

    Parameters
    ----------

    scope : QQuickTheme.Scope
      Passed on as its number.
    """
    #  void QQStyleKitFont::markSet(QQuickTheme::Scope scope)
    self.uglySide.call(
        'ritual_ZN14QQStyleKitFont7markSetEN11QQuickTheme5ScopeE',
        scope.value,
    )

  @staticmethod
  def setButton(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setButton(const QFont &font)': leans on
    'QQStyleKitFont::buttonChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setButton' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setButton(const QFont &font)': leans on "
        "'QQStyleKitFont::buttonChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setCheckBox(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setCheckBox(const QFont &font)': leans on
    'QQStyleKitFont::checkBoxChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setCheckBox' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setCheckBox(const QFont &font)': leans on "
        "'QQStyleKitFont::checkBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setComboBox(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setComboBox(const QFont &font)': leans on
    'QQStyleKitFont::comboBoxChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setComboBox' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setComboBox(const QFont &font)': leans on "
        "'QQStyleKitFont::comboBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFallbackFont(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setFallbackFont(QQStyleKitFont *fallback)':
    leans on 'QQStyleKitFont::fallbackFontChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setFallbackFont' has no cute function yet. Qt's "
        "'void QQStyleKitFont::setFallbackFont(QQStyleKitFont *fallback)': "
        "leans on 'QQStyleKitFont::fallbackFontChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFontForScope(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setFontForScope(QQuickTheme::Scope scope,
    const QFont &font, void (QQStyleKitFont::*)() signal)': takes or gives a
    type that cannot be passed yet: void (QQStyleKitFont::*)().
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setFontForScope' has no cute function yet. Qt's "
        "'void QQStyleKitFont::setFontForScope(QQuickTheme::Scope scope, "
        "const QFont &font, void (QQStyleKitFont::*)() signal)': takes or "
        "gives a type that cannot be passed yet: void (QQStyleKitFont::*)()."
    )

  @staticmethod
  def setGroupBox(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setGroupBox(const QFont &font)': leans on
    'QQStyleKitFont::groupBoxChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setGroupBox' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setGroupBox(const QFont &font)': leans on "
        "'QQStyleKitFont::groupBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setItemDelegate(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setItemDelegate(const QFont &font)': leans on
    'QQStyleKitFont::itemDelegateChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setItemDelegate' has no cute function yet. Qt's "
        "'void QQStyleKitFont::setItemDelegate(const QFont &font)': leans "
        "on 'QQStyleKitFont::itemDelegateChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setLabel(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setLabel(const QFont &font)': leans on
    'QQStyleKitFont::labelChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setLabel' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setLabel(const QFont &font)': leans on "
        "'QQStyleKitFont::labelChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setRadioButton(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setRadioButton(const QFont &font)': leans on
    'QQStyleKitFont::radioButtonChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setRadioButton' has no cute function yet. Qt's "
        "'void QQStyleKitFont::setRadioButton(const QFont &font)': leans on "
        "'QQStyleKitFont::radioButtonChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSpinBox(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setSpinBox(const QFont &font)': leans on
    'QQStyleKitFont::spinBoxChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setSpinBox' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setSpinBox(const QFont &font)': leans on "
        "'QQStyleKitFont::spinBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSwitchControl(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setSwitchControl(const QFont &font)': leans on
    'QQStyleKitFont::switchControlChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setSwitchControl' has no cute function yet. Qt's "
        "'void QQStyleKitFont::setSwitchControl(const QFont &font)': leans "
        "on 'QQStyleKitFont::switchControlChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setSystem(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setSystem(const QFont &font)': leans on
    'QQStyleKitFont::systemChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setSystem' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setSystem(const QFont &font)': leans on "
        "'QQStyleKitFont::systemChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setTabBar(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setTabBar(const QFont &font)': leans on
    'QQStyleKitFont::tabBarChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setTabBar' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setTabBar(const QFont &font)': leans on "
        "'QQStyleKitFont::tabBarChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setTextArea(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setTextArea(const QFont &font)': leans on
    'QQStyleKitFont::textAreaChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setTextArea' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setTextArea(const QFont &font)': leans on "
        "'QQStyleKitFont::textAreaChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setTextField(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setTextField(const QFont &font)': leans on
    'QQStyleKitFont::textFieldChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setTextField' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setTextField(const QFont &font)': leans on "
        "'QQStyleKitFont::textFieldChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setToolBar(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitFont::setToolBar(const QFont &font)': leans on
    'QQStyleKitFont::toolBarChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitFont.setToolBar' has no cute function yet. Qt's 'void "
        "QQStyleKitFont::setToolBar(const QFont &font)': leans on "
        "'QQStyleKitFont::toolBarChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
