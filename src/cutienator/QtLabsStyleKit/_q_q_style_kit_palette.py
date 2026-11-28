"""
QQStyleKitPalette binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitPalette to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from ..QtQuickTemplates2 import QQuickTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitPalette(QObject):
  """
  The cute side of Qt's QQStyleKitPalette: a plain Python object standing in
  front of one C++ QQStyleKitPalette.

  It is built on the cute 'QObject', as Qt's QQStyleKitPalette is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitPalette that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'fallbackPalette',
  'systemChanged', 'checkBoxChanged', 'buttonChanged', 'comboBoxChanged',
  'groupBoxChanged', 'itemDelegateChanged', 'labelChanged',
  'radioButtonChanged', 'spinBoxChanged', 'switchControlChanged',
  'tabBarChanged', 'textAreaChanged', 'textFieldChanged', 'toolBarChanged',
  'fallbackPaletteChanged', 'isSet', 'markSet'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitPalette::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitPalette::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  21 of the 42 functions Qt declares: 16 leans on 'QQStyleKitPalette; 2 not a
  gap; 2 forbidden; 1 leans on 'vtable for QQStyleKitPalette', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQStyleKitPalette is created at the first use, not by
    'QQStyleKitPalette(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitPalette.
  - Qt tells when it has removed the C++ QQStyleKitPalette. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitPalette that has no cute function yet,
    '__init__', 'button', 'checkBox', 'comboBox', 'groupBox', 'itemDelegate',
    'label', 'radioButton', 'setFallbackPalette', 'spinBox', 'switchControl',
    'system', 'tabBar', 'textArea', 'textField', 'toolBar', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitPalette'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitPalette::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitpalette.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitPalette::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQStyleKitPalette10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fallbackPalette(self) -> Optional[QQStyleKitPalette]:
    """
    Calls Qt's 'QQStyleKitPalette *QQStyleKitPalette::fallbackPalette()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#fallbackPalette

    Returns
    -------

    Optional[QQStyleKitPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
    address = self.uglySide.call(
        'ritual_ZNK17QQStyleKitPalette15fallbackPaletteEv',
    )
    return QQStyleKitPalette._cuteAt(address)

  @overload(QQuickTheme.Scope)
  def isSet(self, scope: QQuickTheme.Scope) -> bool:
    """
    Calls Qt's 'bool QQStyleKitPalette::isSet(QQuickTheme::Scope scope)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitpalette.html#isSet

    Parameters
    ----------

    scope : QQuickTheme.Scope
      Passed on as its number.
    """
    #  bool QQStyleKitPalette::isSet(QQuickTheme::Scope scope) const
    return self.uglySide.call(
        'ritual_ZNK17QQStyleKitPalette5isSetEN11QQuickTheme5ScopeE',
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
    Qt's 'QQStyleKitPalette::QQStyleKitPalette(QObject *parent)': leans on
    'vtable for QQStyleKitPalette', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.__init__' has no cute function yet. Qt's "
        "'QQStyleKitPalette::QQStyleKitPalette(QObject *parent)': leans on "
        "'vtable for QQStyleKitPalette', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QQStyleKitPalette::systemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#systemChanged
    """
    #  void QQStyleKitPalette::systemChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette13systemChangedEv')

  def checkBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::checkBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#checkBoxChanged
    """
    #  void QQStyleKitPalette::checkBoxChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette15checkBoxChangedEv')

  def buttonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::buttonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#buttonChanged
    """
    #  void QQStyleKitPalette::buttonChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette13buttonChangedEv')

  def comboBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::comboBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#comboBoxChanged
    """
    #  void QQStyleKitPalette::comboBoxChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette15comboBoxChangedEv')

  def groupBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::groupBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#groupBoxChanged
    """
    #  void QQStyleKitPalette::groupBoxChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette15groupBoxChangedEv')

  def itemDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::itemDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#itemDelegateChanged
    """
    #  void QQStyleKitPalette::itemDelegateChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette19itemDelegateChangedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::labelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#labelChanged
    """
    #  void QQStyleKitPalette::labelChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette12labelChangedEv')

  def radioButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::radioButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#radioButtonChanged
    """
    #  void QQStyleKitPalette::radioButtonChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette18radioButtonChangedEv')

  def spinBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::spinBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#spinBoxChanged
    """
    #  void QQStyleKitPalette::spinBoxChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette14spinBoxChangedEv')

  def switchControlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::switchControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#switchControlChanged
    """
    #  void QQStyleKitPalette::switchControlChanged()
    self.uglySide.call(
        'ritual_ZN17QQStyleKitPalette20switchControlChangedEv',
    )

  def tabBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::tabBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#tabBarChanged
    """
    #  void QQStyleKitPalette::tabBarChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette13tabBarChangedEv')

  def textAreaChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::textAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#textAreaChanged
    """
    #  void QQStyleKitPalette::textAreaChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette15textAreaChangedEv')

  def textFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::textFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#textFieldChanged
    """
    #  void QQStyleKitPalette::textFieldChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette16textFieldChangedEv')

  def toolBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::toolBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#toolBarChanged
    """
    #  void QQStyleKitPalette::toolBarChanged()
    self.uglySide.call('ritual_ZN17QQStyleKitPalette14toolBarChangedEv')

  def fallbackPaletteChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::fallbackPaletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpalette.html#fallbackPaletteChanged
    """
    #  void QQStyleKitPalette::fallbackPaletteChanged()
    self.uglySide.call(
        'ritual_ZN17QQStyleKitPalette22fallbackPaletteChangedEv',
    )

  @overload(QQuickTheme.Scope)
  def markSet(self, scope: QQuickTheme.Scope) -> None:
    """
    Calls Qt's 'void QQStyleKitPalette::markSet(QQuickTheme::Scope scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitpalette.html#markSet

    Parameters
    ----------

    scope : QQuickTheme.Scope
      Passed on as its number.
    """
    #  void QQStyleKitPalette::markSet(QQuickTheme::Scope scope)
    self.uglySide.call(
        'ritual_ZN17QQStyleKitPalette7markSetEN11QQuickTheme5ScopeE',
        scope.value,
    )

  @staticmethod
  def button(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::button() const': leans on
    'QQStyleKitPalette::buttonChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.button' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::button() const': leans on "
        "'QQStyleKitPalette::buttonChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def checkBox(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::checkBox() const': leans on
    'QQStyleKitPalette::checkBoxChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.checkBox' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::checkBox() const': leans on "
        "'QQStyleKitPalette::checkBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def comboBox(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::comboBox() const': leans on
    'QQStyleKitPalette::comboBoxChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.comboBox' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::comboBox() const': leans on "
        "'QQStyleKitPalette::comboBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def groupBox(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::groupBox() const': leans on
    'QQStyleKitPalette::groupBoxChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.groupBox' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::groupBox() const': leans on "
        "'QQStyleKitPalette::groupBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def itemDelegate(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::itemDelegate() const': leans on
    'QQStyleKitPalette::itemDelegateChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.itemDelegate' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::itemDelegate() const': leans on "
        "'QQStyleKitPalette::itemDelegateChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def label(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::label() const': leans on
    'QQStyleKitPalette::labelChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.label' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::label() const': leans on "
        "'QQStyleKitPalette::labelChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def radioButton(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::radioButton() const': leans on
    'QQStyleKitPalette::radioButtonChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.radioButton' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::radioButton() const': leans on "
        "'QQStyleKitPalette::radioButtonChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFallbackPalette(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitPalette::setFallbackPalette(QQStyleKitPalette
    *fallback)': leans on 'QQStyleKitPalette::fallbackPaletteChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.setFallbackPalette' has no cute function yet. "
        "Qt's 'void QQStyleKitPalette::setFallbackPalette(QQStyleKitPalette "
        "*fallback)': leans on "
        "'QQStyleKitPalette::fallbackPaletteChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def spinBox(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::spinBox() const': leans on
    'QQStyleKitPalette::spinBoxChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.spinBox' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::spinBox() const': leans on "
        "'QQStyleKitPalette::spinBoxChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def switchControl(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::switchControl() const': leans on
    'QQStyleKitPalette::switchControlChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.switchControl' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::switchControl() const': leans "
        "on 'QQStyleKitPalette::switchControlChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def system(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::system() const': leans on
    'QQStyleKitPalette::systemChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.system' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::system() const': leans on "
        "'QQStyleKitPalette::systemChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tabBar(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::tabBar() const': leans on
    'QQStyleKitPalette::tabBarChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.tabBar' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::tabBar() const': leans on "
        "'QQStyleKitPalette::tabBarChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textArea(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::textArea() const': leans on
    'QQStyleKitPalette::textAreaChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.textArea' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::textArea() const': leans on "
        "'QQStyleKitPalette::textAreaChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textField(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::textField() const': leans on
    'QQStyleKitPalette::textFieldChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.textField' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::textField() const': leans on "
        "'QQStyleKitPalette::textFieldChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def toolBar(*__, **_) -> Never:
    """
    Qt's 'QQuickPalette *QQStyleKitPalette::toolBar() const': leans on
    'QQStyleKitPalette::toolBarChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPalette.toolBar' has no cute function yet. Qt's "
        "'QQuickPalette *QQStyleKitPalette::toolBar() const': leans on "
        "'QQStyleKitPalette::toolBarChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
