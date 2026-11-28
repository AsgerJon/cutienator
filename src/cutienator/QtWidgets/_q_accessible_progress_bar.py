"""
QAccessibleProgressBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleProgressBar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleValueInterface
from . import QAccessibleDisplay

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QProgressBar, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleProgressBar(QAccessibleDisplay, QAccessibleValueInterface):
  """
  The cute side of Qt's QAccessibleProgressBar: a plain Python object
  standing in front of one C++ QAccessibleProgressBar.

  It is built on the cute 'QAccessibleDisplay', as Qt's
  QAccessibleProgressBar is built on Qt's QAccessibleDisplay, and has
  everything that class has. It is built on the cute
  'QAccessibleValueInterface' as well, as Qt's QAccessibleProgressBar is
  built on Qt's QAccessibleValueInterface too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QAccessibleProgressBar that has a ritual and that
  Python can call so far, 6 names in all: 'currentValue', 'maximumValue',
  'minimumValue', 'minimumStepSize', 'setCurrentValue', 'progressBar'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleProgressBar::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleProgressBar is created at the first use, not by
    'QAccessibleProgressBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleProgressBar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleProgressBar'

  #  Qt's QAccessibleProgressBar is built on more than one class. The part of
  #  a C++ QAccessibleProgressBar that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleValueInterface':
          'ritual_cast_QAccessibleProgressBar_QAccessibleValueInterface',
  }

  #  A C++ QAccessibleProgressBar Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleProgressBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleProgressBar::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleProgressBar::currentValue() const
    ritual = 'ritual_ZNK22QAccessibleProgressBar12currentValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleProgressBar12currentValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleProgressBar::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleProgressBar::maximumValue() const
    ritual = 'ritual_ZNK22QAccessibleProgressBar12maximumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleProgressBar12maximumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleProgressBar::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleProgressBar::minimumValue() const
    ritual = 'ritual_ZNK22QAccessibleProgressBar12minimumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleProgressBar12minimumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleProgressBar::minimumStepSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleProgressBar::minimumStepSize() const
    ritual = 'ritual_ZNK22QAccessibleProgressBar15minimumStepSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QAccessibleProgressBar15minimumStepSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def progressBar(self) -> Optional[QProgressBar]:
    """
    Calls Qt's 'QProgressBar *QAccessibleProgressBar::progressBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#progressBar

    Returns
    -------

    Optional[QProgressBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProgressBar *QAccessibleProgressBar::progressBar() const
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleProgressBar11progressBarEv',
    )
    from . import QProgressBar
    return QProgressBar._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setCurrentValue(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleProgressBar::setCurrentValue(const QVariant
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#setCurrentValue

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleProgressBar::setCurrentValue(const QVariant &a0)
    ritual = 'ritual_ZN22QAccessibleProgressBar15setCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAccessibleProgressBar15setCurrentValueERK8QVaria'
          'nt')
    self.uglySide.call(ritual, self._valueOf(a0))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, o: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleProgressBar::QAccessibleProgressBar(QWidget *o)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleprogressbar.html#QAccessibleProgressBar

    Parameters
    ----------

    o : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleProgressBar::QAccessibleProgressBar(QWidget *o)
    self._noteCreation(QAccessibleProgressBar, lambda: Rituals.call(
        'ritual_ZN22QAccessibleProgressBarC1EP7QWidget', self._addressOf(o),
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
