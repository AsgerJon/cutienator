"""
QQuickMaterialTextContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialtextcontainer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMaterialTextContainer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QPainter
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMaterialTextContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickMaterialTextContainer: a plain Python object
  standing in front of one C++ QQuickMaterialTextContainer.

  What exists
  -----------

  Every function of Qt's QQuickMaterialTextContainer that has a ritual and
  that Python can call so far, 31 names in all: 'metaObject', 'isFilled',
  'setFilled', 'fillColor', 'setFillColor', 'outlineColor',
  'setOutlineColor', 'focusedOutlineColor', 'setFocusedOutlineColor',
  'focusAnimationProgress', 'setFocusAnimationProgress',
  'placeholderTextWidth', 'setPlaceholderTextWidth', 'controlHasActiveFocus',
  'controlHasText', 'placeholderHasText', 'horizontalPadding', 'paint',
  'placeholderTextHAlign', 'setPlaceholderTextHAlign', 'animateChanged',
  'controlHasActiveFocusChanged', 'controlHasTextChanged',
  'placeholderHasTextChanged', 'horizontalPaddingChanged',
  'shouldAnimateOutline', 'textControl', 'controlGotActiveFocus',
  'controlLostActiveFocus', 'updateFocusAnimation', 'componentComplete'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMaterialTextContainer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickMaterialTextContainer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 41 functions Qt declares: 5 leans on 'QQuickMaterialTextContainer;
  2 not a gap; 1 leans on 'vtable for QQuickMaterialTextContainer', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQuickMaterialTextContainer is created at the first use, not by
    'QQuickMaterialTextContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMaterialTextContainer.
  - Qt tells when it has removed the C++ QQuickMaterialTextContainer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMaterialTextContainer that has no cute function
    yet, '__init__', 'setControlHasActiveFocus', 'setControlHasText',
    'setHorizontalPadding', 'setPlaceholderHasText', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickMaterialTextContainer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PlaceHolderHAlignment(CuteNum):
    """
    The enum 'QQuickMaterialTextContainer::PlaceHolderHAlignment' of Qt, with
    the 4 names Qt gives in it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)
    AlignJustify = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMaterialTextContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMaterialTextContainer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMaterialTextContainer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFilled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialTextContainer::isFilled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#isFilled
    """
    #  bool QQuickMaterialTextContainer::isFilled() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer8isFilledEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialTextContainer::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialTextContainer::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def outlineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialTextContainer::outlineColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#outlineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialTextContainer::outlineColor() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer12outlineColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def focusedOutlineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickMaterialTextContainer::focusedOutlineColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickMaterialTextContainer::focusedOutlineColor() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer19focusedOutlineColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def focusAnimationProgress(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialTextContainer::focusAnimationProgress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  qreal QQuickMaterialTextContainer::focusAnimationProgress() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer22focusAnimationProgressEv',
    )

  def placeholderTextWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickMaterialTextContainer::placeholderTextWidth()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  qreal QQuickMaterialTextContainer::placeholderTextWidth() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer20placeholderTextWidthEv',
    )

  def controlHasActiveFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialTextContainer::controlHasActiveFocus()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  bool QQuickMaterialTextContainer::controlHasActiveFocus() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer21controlHasActiveFocusEv',
    )

  def controlHasText(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialTextContainer::controlHasText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#controlHasText
    """
    #  bool QQuickMaterialTextContainer::controlHasText() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer14controlHasTextEv',
    )

  def placeholderHasText(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialTextContainer::placeholderHasText()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  bool QQuickMaterialTextContainer::placeholderHasText() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer18placeholderHasTextEv',
    )

  def horizontalPadding(self) -> int:
    """
    Calls Qt's 'int QQuickMaterialTextContainer::horizontalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#horizontalPadding
    """
    #  int QQuickMaterialTextContainer::horizontalPadding() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer17horizontalPaddingEv',
    )

  def placeholderTextHAlign(self) -> PlaceHolderHAlignment:
    """
    Calls Qt's 'PlaceHolderHAlignment
    QQuickMaterialTextContainer::placeholderTextHAlign() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Returns
    -------

    PlaceHolderHAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PlaceHolderHAlignment(number)' gives.
    """
    #  PlaceHolderHAlignment
    #      QQuickMaterialTextContainer::placeholderTextHAlign() const
    return QQuickMaterialTextContainer.PlaceHolderHAlignment(
        self.uglySide.call(
            'ritual_ZNK27QQuickMaterialTextContainer21placeholderTextHAlign'
            'Ev',
        ))

  def shouldAnimateOutline(self) -> bool:
    """
    Calls Qt's 'bool QQuickMaterialTextContainer::shouldAnimateOutline()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  bool QQuickMaterialTextContainer::shouldAnimateOutline() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer20shouldAnimateOutlineEv',
    )

  def textControl(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMaterialTextContainer::textControl()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#textControl

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMaterialTextContainer::textControl() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickMaterialTextContainer11textControlEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFilled(self, filled: bool) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::setFilled(bool filled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#setFilled

    Parameters
    ----------

    filled : bool
      Passed on as it is.
    """
    #  void QQuickMaterialTextContainer::setFilled(bool filled)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer9setFilledEb', filled,
    )

  @overload(QColor)
  def setFillColor(self, fillColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::setFillColor(const QColor
    &fillColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#setFillColor

    Parameters
    ----------

    fillColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMaterialTextContainer::setFillColor(const QColor
    #      &fillColor)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer12setFillColorERK6QColor',
        self._valueOf(fillColor),
    )

  @overload(QColor)
  def setOutlineColor(self, outlineColor: QColor) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::setOutlineColor(const
    QColor &outlineColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#setOutlineColor

    Parameters
    ----------

    outlineColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMaterialTextContainer::setOutlineColor(const QColor
    #      &outlineColor)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer15setOutlineColorERK6QColor',
        self._valueOf(outlineColor),
    )

  @overload(QColor)
  def setFocusedOutlineColor(self, focusedOutlineColor: QColor) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::setFocusedOutlineColor(const QColor
    &focusedOutlineColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Parameters
    ----------

    focusedOutlineColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickMaterialTextContainer::setFocusedOutlineColor(const QColor
    #      &focusedOutlineColor)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer22setFocusedOutlineColorERK6'
        'QColor',
        self._valueOf(focusedOutlineColor),
    )

  @overload(float)
  def setFocusAnimationProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::setFocusAnimationProgress(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickMaterialTextContainer::setFocusAnimationProgress(qreal
    #      progress)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer25setFocusAnimationProgressE'
        'd',
        progress,
    )

  @overload(float)
  def setPlaceholderTextWidth(self, placeholderTextWidth: float) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::setPlaceholderTextWidth(qreal
    placeholderTextWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Parameters
    ----------

    placeholderTextWidth : float
      Passed on as it is.
    """
    #  void QQuickMaterialTextContainer::setPlaceholderTextWidth(qreal
    #      placeholderTextWidth)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer23setPlaceholderTextWidthEd',
        placeholderTextWidth,
    )

  @overload(PlaceHolderHAlignment)
  def setPlaceholderTextHAlign(
      self,
      placeHolderTextHAlign: PlaceHolderHAlignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::setPlaceholderTextHAlign(
    PlaceHolderHAlignment placeHolderTextHAlign)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Parameters
    ----------

    placeHolderTextHAlign : PlaceHolderHAlignment
      Passed on as its number.
    """
    #  void QQuickMaterialTextContainer::setPlaceholderTextHAlign(
    #      PlaceHolderHAlignment placeHolderTextHAlign)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer24setPlaceholderTextHAlignEN'
        'S_21PlaceHolderHAlignmentE',
        placeHolderTextHAlign.value,
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
    Qt's 'QQuickMaterialTextContainer::QQuickMaterialTextContainer(QQuickItem
    *parent)': leans on 'vtable for QQuickMaterialTextContainer', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialTextContainer.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickMaterialTextContainer::QQuickMaterialTextContainer(QQuickIte"
        "m *parent)': leans on 'vtable for QQuickMaterialTextContainer', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::paint(QPainter *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMaterialTextContainer::paint(QPainter *painter)
    ritual = 'ritual_ZN27QQuickMaterialTextContainer5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickMaterialTextContainer5paintEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))

  def animateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::animateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#animateChanged
    """
    #  void QQuickMaterialTextContainer::animateChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer14animateChangedEv',
    )

  def controlHasActiveFocusChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::controlHasActiveFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::controlHasActiveFocusChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer28controlHasActiveFocusChang'
        'edEv',
    )

  def controlHasTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::controlHasTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::controlHasTextChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer21controlHasTextChangedEv',
    )

  def placeholderHasTextChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::placeholderHasTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::placeholderHasTextChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer25placeholderHasTextChangedE'
        'v',
    )

  def horizontalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickMaterialTextContainer::horizontalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::horizontalPaddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer24horizontalPaddingChangedEv',
    )

  def controlGotActiveFocus(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::controlGotActiveFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::controlGotActiveFocus()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer21controlGotActiveFocusEv',
    )

  def controlLostActiveFocus(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::controlLostActiveFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html
    """
    #  void QQuickMaterialTextContainer::controlLostActiveFocus()
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer22controlLostActiveFocusEv',
    )

  @overload()
  @overload(bool)
  def updateFocusAnimation(self, createIfNeeded: bool = False) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::updateFocusAnimation(bool
    createIfNeeded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html

    Parameters
    ----------

    createIfNeeded : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickMaterialTextContainer::updateFocusAnimation(bool
    #      createIfNeeded)
    self.uglySide.call(
        'ritual_ZN27QQuickMaterialTextContainer20updateFocusAnimationEb',
        createIfNeeded,
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMaterialTextContainer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaterialtextcontainer.html#componentComplete
    """
    #  void QQuickMaterialTextContainer::componentComplete()
    ritual = 'ritual_ZN27QQuickMaterialTextContainer17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickMaterialTextContainer17componentCompleteEv')
    self.uglySide.call(ritual)

  @staticmethod
  def setControlHasActiveFocus(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialTextContainer::setControlHasActiveFocus(bool
    controlHasActiveFocus)': leans on
    'QQuickMaterialTextContainer::controlHasActiveFocusChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialTextContainer.setControlHasActiveFocus' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialTextContainer::setControlHasActiveFocus(bool "
        "controlHasActiveFocus)': leans on "
        "'QQuickMaterialTextContainer::controlHasActiveFocusChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setControlHasText(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialTextContainer::setControlHasText(bool
    controlHasText)': leans on
    'QQuickMaterialTextContainer::controlHasTextChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialTextContainer.setControlHasText' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialTextContainer::setControlHasText(bool "
        "controlHasText)': leans on "
        "'QQuickMaterialTextContainer::controlHasTextChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setHorizontalPadding(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialTextContainer::setHorizontalPadding(int
    horizontalPadding)': leans on
    'QQuickMaterialTextContainer::horizontalPaddingChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialTextContainer.setHorizontalPadding' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialTextContainer::setHorizontalPadding(int "
        "horizontalPadding)': leans on "
        "'QQuickMaterialTextContainer::horizontalPaddingChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setPlaceholderHasText(*__, **_) -> Never:
    """
    Qt's 'void QQuickMaterialTextContainer::setPlaceholderHasText(bool
    placeholderHasText)': leans on
    'QQuickMaterialTextContainer::placeholderHasTextChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMaterialTextContainer.setPlaceholderHasText' has no cute "
        "function yet. Qt's 'void "
        "QQuickMaterialTextContainer::setPlaceholderHasText(bool "
        "placeholderHasText)': leans on "
        "'QQuickMaterialTextContainer::placeholderHasTextChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
