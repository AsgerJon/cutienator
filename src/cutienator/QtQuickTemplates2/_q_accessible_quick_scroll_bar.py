"""
QAccessibleQuickScrollBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickscrollbar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickScrollBar to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from . import QAccessibleQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QQuickScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickScrollBar = WAIT['QQuickScrollBar']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickScrollBar(QAccessibleQuickControl):
  """
  The cute side of Qt's QAccessibleQuickScrollBar: a plain Python object
  standing in front of one C++ QAccessibleQuickScrollBar.

  It is built on the cute 'QAccessibleQuickControl', as Qt's
  QAccessibleQuickScrollBar is built on Qt's QAccessibleQuickControl, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickScrollBar that has a ritual and that
  Python can call so far, 10 names in all: 'attributeValue', 'currentValue',
  'setCurrentValue', 'maximumValue', 'minimumValue', 'minimumStepSize',
  'scrollBar', 'maximumPositionValue', 'normalizeValue', 'denormalizeValue'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QAccessible::Attribute>
    QAccessibleQuickScrollBar::attributeKeys() const': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickScrollBar is created at the first use, not by
    'QAccessibleQuickScrollBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickScrollBar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickScrollBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Attribute)
  def attributeValue(self, key: QAccessible.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAccessibleQuickScrollBar::attributeValue(QAccessible::Attribute key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#attributeValue

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      QAccessibleQuickScrollBar::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK25QAccessibleQuickScrollBar14attributeValueEN11QAccessib'
        'le9AttributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAccessibleQuickScrollBar14attributeValueEN11QAc'
          'cessible9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickScrollBar::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickScrollBar::currentValue() const
    ritual = 'ritual_ZNK25QAccessibleQuickScrollBar12currentValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickScrollBar12currentValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickScrollBar::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickScrollBar::maximumValue() const
    ritual = 'ritual_ZNK25QAccessibleQuickScrollBar12maximumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickScrollBar12maximumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickScrollBar::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickScrollBar::minimumValue() const
    ritual = 'ritual_ZNK25QAccessibleQuickScrollBar12minimumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickScrollBar12minimumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickScrollBar::minimumStepSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickScrollBar::minimumStepSize() const
    ritual = 'ritual_ZNK25QAccessibleQuickScrollBar15minimumStepSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickScrollBar15minimumStepSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def scrollBar(self) -> Optional[QQuickScrollBar]:
    """
    Calls Qt's 'QQuickScrollBar *QAccessibleQuickScrollBar::scrollBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#scrollBar

    Returns
    -------

    Optional[QQuickScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBar *QAccessibleQuickScrollBar::scrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickScrollBar9scrollBarEv',
    )
    from . import QQuickScrollBar
    return QQuickScrollBar._cuteAt(address)

  def maximumPositionValue(self) -> float:
    """
    Calls Qt's 'qreal QAccessibleQuickScrollBar::maximumPositionValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html
    """
    #  qreal QAccessibleQuickScrollBar::maximumPositionValue() const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickScrollBar20maximumPositionValueEv',
    )

  @overload(float)
  def normalizeValue(self, value: float) -> float:
    """
    Calls Qt's 'qreal QAccessibleQuickScrollBar::normalizeValue(qreal value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#normalizeValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  qreal QAccessibleQuickScrollBar::normalizeValue(qreal value) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickScrollBar14normalizeValueEd', value,
    )

  @overload(float)
  def denormalizeValue(self, value: float) -> float:
    """
    Calls Qt's 'qreal QAccessibleQuickScrollBar::denormalizeValue(qreal
    value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#denormalizeValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  qreal QAccessibleQuickScrollBar::denormalizeValue(qreal value) const
    return self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickScrollBar16denormalizeValueEd', value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleQuickScrollBar::setCurrentValue(const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleQuickScrollBar::setCurrentValue(const QVariant &value)
    ritual = (
        'ritual_ZN25QAccessibleQuickScrollBar15setCurrentValueERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAccessibleQuickScrollBar15setCurrentValueERK8QVa'
          'riant')
    self.uglySide.call(ritual, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickScrollBar)
  @overload(NoneType)
  def __init__(self, scrollBar: Optional[QQuickScrollBar]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickScrollBar::QAccessibleQuickScrollBar(QQuickScrollBar
    *scrollBar)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickscrollbar.html

    Parameters
    ----------

    scrollBar : Optional[QQuickScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickScrollBar::QAccessibleQuickScrollBar(QQuickScrollBar
    #      *scrollBar)
    self._noteCreation(QAccessibleQuickScrollBar, lambda: Rituals.call(
        'ritual_ZN25QAccessibleQuickScrollBarC1EP15QQuickScrollBar',
        self._addressOf(scrollBar),
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
