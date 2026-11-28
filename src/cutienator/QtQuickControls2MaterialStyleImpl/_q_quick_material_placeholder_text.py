"""
QQuickMaterialPlaceholderText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialplaceholdertext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMaterialPlaceholderText to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickMaterialPlaceholderText(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMaterialPlaceholderText: a plain Python object
  standing in front of one C++ QQuickMaterialPlaceholderText.

  What exists
  -----------

  Every function of Qt's QQuickMaterialPlaceholderText that has a ritual and
  that Python can call so far, 24 names in all: 'metaObject', 'isFilled',
  'setFilled', 'largestHeight', 'controlHasActiveFocus', 'controlHasText',
  'controlImplicitBackgroundHeight', 'controlHeight', 'verticalPadding',
  'filledChanged', 'largestHeightChanged', 'controlHasActiveFocusChanged',
  'controlHasTextChanged', 'controlImplicitBackgroundHeightChanged',
  'verticalPaddingChanged', 'adjustTransformOrigin', 'shouldFloat',
  'shouldAnimate', 'updateY', 'updateX', 'normalTargetY', 'normalTargetX',
  'floatingTargetX', 'componentComplete'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMaterialPlaceholderText::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickMaterialPlaceholderText::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  14 of the 40 functions Qt declares: 10 leans on
  'QQuickMaterialPlaceholderText; 2 not a gap; 2 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickMaterialPlaceholderText is created at the first use, not by
    'QQuickMaterialPlaceholderText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMaterialPlaceholderText.
  - Qt tells when it has removed the C++ QQuickMaterialPlaceholderText. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMaterialPlaceholderText that has no cute function
    yet, '__init__', 'controlActiveFocusChanged', 'floatingTargetY',
    'setControlHasActiveFocus', 'setControlHasText', 'setControlHeight',
    'setControlImplicitBackgroundHeight', 'setFloatingLeftPadding',
    'setVerticalPadding', 'updateFocusAnimation', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMaterialPlaceholderText'

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
    *QQuickMaterialPlaceholderText::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMaterialPlaceholderText::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFilled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialPlaceholderText::isFilled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#isFilled
    """
    #  bool QQuickMaterialPlaceholderText::isFilled() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText8isFilledEv',
    )

  def largestHeight(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialPlaceholderText::largestHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#largestHeight
    """
    #  int QQuickMaterialPlaceholderText::largestHeight() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText13largestHeightEv',
    )

  def controlHasActiveFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialPlaceholderText::controlHasActiveFocus()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  bool QQuickMaterialPlaceholderText::controlHasActiveFocus() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText21controlHasActiveFocusEv',
    )

  def controlHasText(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialPlaceholderText::controlHasText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#controlHasText
    """
    #  bool QQuickMaterialPlaceholderText::controlHasText() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText14controlHasTextEv',
    )

  def controlImplicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal
    QQuickMaterialPlaceholderText::controlImplicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  qreal QQuickMaterialPlaceholderText::controlImplicitBackgroundHeight()
    #      const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText31controlImplicitBackgrou'
        'ndHeightEv',
    )

  def controlHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialPlaceholderText::controlHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#controlHeight
    """
    #  qreal QQuickMaterialPlaceholderText::controlHeight() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText13controlHeightEv',
    )

  def verticalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialPlaceholderText::verticalPadding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#verticalPadding
    """
    #  qreal QQuickMaterialPlaceholderText::verticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText15verticalPaddingEv',
    )

  def shouldFloat(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialPlaceholderText::shouldFloat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#shouldFloat
    """
    #  bool QQuickMaterialPlaceholderText::shouldFloat() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText11shouldFloatEv',
    )

  def shouldAnimate(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialPlaceholderText::shouldAnimate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#shouldAnimate
    """
    #  bool QQuickMaterialPlaceholderText::shouldAnimate() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText13shouldAnimateEv',
    )

  def normalTargetY(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialPlaceholderText::normalTargetY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#normalTargetY
    """
    #  qreal QQuickMaterialPlaceholderText::normalTargetY() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText13normalTargetYEv',
    )

  def normalTargetX(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialPlaceholderText::normalTargetX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#normalTargetX
    """
    #  qreal QQuickMaterialPlaceholderText::normalTargetX() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText13normalTargetXEv',
    )

  def floatingTargetX(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialPlaceholderText::floatingTargetX()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#floatingTargetX
    """
    #  qreal QQuickMaterialPlaceholderText::floatingTargetX() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickMaterialPlaceholderText15floatingTargetXEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFilled(self, filled: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::setFilled(bool filled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#setFilled

    Parameters
    ----------

    filled : bool
      Passed on as it is.
    """
    #  void QQuickMaterialPlaceholderText::setFilled(bool filled)
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText9setFilledEb', filled,
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
    Qt's
    'QQuickMaterialPlaceholderText::QQuickMaterialPlaceholderText(QQuickItem
    *parent)': leans on 'QQuickMaterialPlaceholderText::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickMaterialPlaceholderText::QQuickMaterialPlaceholderText(QQuic"
        "kItem *parent)': leans on "
        "'QQuickMaterialPlaceholderText::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def filledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::filledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#filledChanged
    """
    #  void QQuickMaterialPlaceholderText::filledChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText13filledChangedEv',
    )

  def largestHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::largestHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::largestHeightChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText20largestHeightChangedEv',
    )

  def controlHasActiveFocusChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialPlaceholderText::controlHasActiveFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::controlHasActiveFocusChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText28controlHasActiveFocusCha'
        'ngedEv',
    )

  def controlHasTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::controlHasTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::controlHasTextChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText21controlHasTextChangedEv',
    )

  def controlImplicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialPlaceholderText::controlImplicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::
    #      controlImplicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText38controlImplicitBackgroun'
        'dHeightChangedEv',
    )

  def verticalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialPlaceholderText::verticalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::verticalPaddingChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText22verticalPaddingChangedEv',
    )

  def adjustTransformOrigin(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::adjustTransformOrigin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::adjustTransformOrigin()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText21adjustTransformOriginEv',
    )

  def updateY(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::updateY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#updateY
    """
    #  void QQuickMaterialPlaceholderText::updateY()
    self.uglySide.call('ritual_ZN29QQuickMaterialPlaceholderText7updateYEv')

  def updateX(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::updateX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html#updateX
    """
    #  void QQuickMaterialPlaceholderText::updateX()
    self.uglySide.call('ritual_ZN29QQuickMaterialPlaceholderText7updateXEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialPlaceholderText::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialplaceholdertext.html
    """
    #  void QQuickMaterialPlaceholderText::componentComplete()
    self.uglySide.call(
        'ritual_ZN29QQuickMaterialPlaceholderText17componentCompleteEv',
    )

  @staticmethod
  def controlActiveFocusChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::controlActiveFocusChanged()':
    leans on 'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.controlActiveFocusChanged' has no "
        "cute function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::controlActiveFocusChanged()': leans "
        "on 'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def floatingTargetY(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickMaterialPlaceholderText::floatingTargetY() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'controlTopInset'.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.floatingTargetY' has no cute "
        "function yet. Qt's 'qreal "
        "QQuickMaterialPlaceholderText::floatingTargetY() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'controlTopInset'.")

  @staticmethod
  def setControlHasActiveFocus(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::setControlHasActiveFocus(bool
    controlHasActiveFocus)': leans on
    'QQuickMaterialPlaceholderText::controlHasActiveFocusChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setControlHasActiveFocus' has no "
        "cute function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setControlHasActiveFocus(bool "
        "controlHasActiveFocus)': leans on "
        "'QQuickMaterialPlaceholderText::controlHasActiveFocusChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setControlHasText(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::setControlHasText(bool
    controlHasText)': leans on
    'QQuickMaterialPlaceholderText::controlHasTextChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setControlHasText' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setControlHasText(bool "
        "controlHasText)': leans on "
        "'QQuickMaterialPlaceholderText::controlHasTextChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setControlHeight(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::setControlHeight(qreal
    controlHeight)': leans on
    'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setControlHeight' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setControlHeight(qreal "
        "controlHeight)': leans on "
        "'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setControlImplicitBackgroundHeight(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickMaterialPlaceholderText::setControlImplicitBackgroundHeight(qreal
    controlImplicitBackgroundHeight)': leans on
    'QQuickMaterialPlaceholderText::controlImplicitBackgroundHeightChanged(
    )', which Qt's source does not mark for use from outside Qt and has no
    code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setControlImplicitBackgroundHeight' "
        "has no cute function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setControlImplicitBackgroundHeight(q"
        "real controlImplicitBackgroundHeight)': leans on "
        "'QQuickMaterialPlaceholderText::controlImplicitBackgroundHeightChan"
        "ged()', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setFloatingLeftPadding(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::setFloatingLeftPadding(int
    floatingLeftPadding)': leans on
    'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setFloatingLeftPadding' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setFloatingLeftPadding(int "
        "floatingLeftPadding)': leans on "
        "'QQuickMaterialPlaceholderText::updateFocusAnimation(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setVerticalPadding(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::setVerticalPadding(qreal
    verticalPadding)': leans on
    'QQuickMaterialPlaceholderText::verticalPaddingChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.setVerticalPadding' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::setVerticalPadding(qreal "
        "verticalPadding)': leans on "
        "'QQuickMaterialPlaceholderText::verticalPaddingChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateFocusAnimation(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialPlaceholderText::updateFocusAnimation(bool
    createIfNeeded)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'animationEasingCurve'.
    """
    raise NotImplementedError(
        "'QQuickMaterialPlaceholderText.updateFocusAnimation' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialPlaceholderText::updateFocusAnimation(bool "
        "createIfNeeded)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'animationEasingCurve'.")
