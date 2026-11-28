"""
QAccessibleAbstractSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleAbstractSlider to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QAccessible, QAccessibleValueInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QAbstractSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QAccessibleAbstractSlider(QAccessibleWidgetV2, QAccessibleValueInterface):
  """
  The cute side of Qt's QAccessibleAbstractSlider: a plain Python object
  standing in front of one C++ QAccessibleAbstractSlider.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleAbstractSlider is built on Qt's QAccessibleWidgetV2, and has
  everything that class has. It is built on the cute
  'QAccessibleValueInterface' as well, as Qt's QAccessibleAbstractSlider is
  built on Qt's QAccessibleValueInterface too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QAccessibleAbstractSlider that has a ritual and that
  Python can call so far, 7 names in all: 'attributeValue', 'currentValue',
  'setCurrentValue', 'maximumValue', 'minimumValue', 'minimumStepSize',
  'abstractSlider'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleAbstractSlider::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.
  - Qt's 'QList<QAccessible::Attribute>
    QAccessibleAbstractSlider::attributeKeys() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleAbstractSlider.

  What to expect
  --------------

  - The C++ QAccessibleAbstractSlider is created at the first use, not by
    'QAccessibleAbstractSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleAbstractSlider.
  - Each name of Qt's QAccessibleAbstractSlider that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleAbstractSlider'

  #  Qt's QAccessibleAbstractSlider is built on more than one class. The part
  #  of a C++ QAccessibleAbstractSlider that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleValueInterface':
          'ritual_cast_QAccessibleAbstractSlider_QAccessibleValueInterface',
  }

  #  A C++ QAccessibleAbstractSlider Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleAbstractSlider'

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
    QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#attributeValue

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
    #      QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK25QAccessibleAbstractSlider14attributeValueEN11QAccessib'
        'le9AttributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAccessibleAbstractSlider14attributeValueEN11QAc'
          'cessible9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSlider::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSlider::currentValue() const
    ritual = 'ritual_ZNK25QAccessibleAbstractSlider12currentValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleAbstractSlider12currentValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSlider::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSlider::maximumValue() const
    ritual = 'ritual_ZNK25QAccessibleAbstractSlider12maximumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleAbstractSlider12maximumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSlider::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSlider::minimumValue() const
    ritual = 'ritual_ZNK25QAccessibleAbstractSlider12minimumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleAbstractSlider12minimumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleAbstractSlider::minimumStepSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleAbstractSlider::minimumStepSize() const
    ritual = 'ritual_ZNK25QAccessibleAbstractSlider15minimumStepSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleAbstractSlider15minimumStepSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def abstractSlider(self) -> Optional[QAbstractSlider]:
    """
    Calls Qt's 'QAbstractSlider *QAccessibleAbstractSlider::abstractSlider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#abstractSlider

    Returns
    -------

    Optional[QAbstractSlider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSlider *QAccessibleAbstractSlider::abstractSlider() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleAbstractSlider14abstractSliderEv',
    )
    from . import QAbstractSlider
    return QAbstractSlider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleAbstractSlider::setCurrentValue(const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleabstractslider.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleAbstractSlider::setCurrentValue(const QVariant &value)
    ritual = (
        'ritual_ZN25QAccessibleAbstractSlider15setCurrentValueERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAccessibleAbstractSlider15setCurrentValueERK8QVa'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAccessibleAbstractSlider::QAccessibleAbstractSlider(QWidget *w,
    QAccessible::Role r)': leans on 'non-virtual thunk to
    QAccessibleAbstractSlider::attributeKeys() const', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleAbstractSlider.__init__' has no cute function yet. "
        "Qt's 'QAccessibleAbstractSlider::QAccessibleAbstractSlider(QWidget "
        "*w, QAccessible::Role r)': leans on 'non-virtual thunk to "
        "QAccessibleAbstractSlider::attributeKeys() const', which Qt's "
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
