"""
QAccessibleDoubleSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleDoubleSpinBox to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessible
from . import QAccessibleAbstractSpinBox

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDoubleSpinBox


class QAccessibleDoubleSpinBox(QAccessibleAbstractSpinBox):
  """
  The cute side of Qt's QAccessibleDoubleSpinBox: a plain Python object
  standing in front of one C++ QAccessibleDoubleSpinBox.

  It is built on the cute 'QAccessibleAbstractSpinBox', as Qt's
  QAccessibleDoubleSpinBox is built on Qt's QAccessibleAbstractSpinBox, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleDoubleSpinBox that has a ritual and that
  Python can call so far, 2 names in all: 'text', 'doubleSpinBox'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleAbstractSpinBox.

  What to expect
  --------------

  - The C++ QAccessibleDoubleSpinBox is created at the first use, not by
    'QAccessibleDoubleSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleDoubleSpinBox.
  - Each name of Qt's QAccessibleDoubleSpinBox that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleDoubleSpinBox'

  #  A C++ QAccessibleDoubleSpinBox Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleDoubleSpinBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleDoubleSpinBox::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledoublespinbox.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleDoubleSpinBox::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK24QAccessibleDoubleSpinBox4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAccessibleDoubleSpinBox4textEN11QAccessible4Tex'
          'tE')
    return self.uglySide.call(ritual, t.value)

  def doubleSpinBox(self) -> Optional[QDoubleSpinBox]:
    """
    Calls Qt's 'QDoubleSpinBox *QAccessibleDoubleSpinBox::doubleSpinBox()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledoublespinbox.html#doubleSpinBox

    Returns
    -------

    Optional[QDoubleSpinBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDoubleSpinBox *QAccessibleDoubleSpinBox::doubleSpinBox() const
    address = self.uglySide.call(
        'ritual_ZNK24QAccessibleDoubleSpinBox13doubleSpinBoxEv',
    )
    from . import QDoubleSpinBox
    return QDoubleSpinBox._cuteAt(address)

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
    Qt's 'QAccessibleDoubleSpinBox::QAccessibleDoubleSpinBox(QWidget
    *widget)': leans on 'non-virtual thunk to
    QAccessibleAbstractSpinBox::attributes(int, int*, int*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleDoubleSpinBox.__init__' has no cute function yet. Qt's "
        "'QAccessibleDoubleSpinBox::QAccessibleDoubleSpinBox(QWidget "
        "*widget)': leans on 'non-virtual thunk to "
        "QAccessibleAbstractSpinBox::attributes(int, int*, int*) const', "
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
