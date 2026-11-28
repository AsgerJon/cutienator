"""
QToolBarAreaLayoutLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBarAreaLayoutLine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QSize


class QToolBarAreaLayoutLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QToolBarAreaLayoutLine: a plain Python object
  standing in front of one C++ QToolBarAreaLayoutLine.

  C++ hands a QToolBarAreaLayoutLine around as a copy, so every C++
  QToolBarAreaLayoutLine behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QToolBarAreaLayoutLine that has a ritual and that
  Python can call so far, 3 names in all: 'sizeHint', 'minimumSize', 'skip'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolBarAreaLayoutLine::~QToolBarAreaLayoutLine()': the destructor:
    Python removes its C++ QToolBarAreaLayoutLine by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 leans on 'QToolBarLayout.

  What to expect
  --------------

  - The C++ QToolBarAreaLayoutLine is created at the first use, not by
    'QToolBarAreaLayoutLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QToolBarAreaLayoutLine back gives a copy the ritual
    made for Python, in a new cute QToolBarAreaLayoutLine.
  - Each name of Qt's QToolBarAreaLayoutLine that has no cute function yet,
    'fitLayout', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QToolBarAreaLayoutLine'

  #  Qt's '~QToolBarAreaLayoutLine()'. Naming it makes this a value class:
  #  Python owns every C++ QToolBarAreaLayoutLine behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QToolBarAreaLayoutLineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutLine::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutline.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutLine::sizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutLine8sizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutLine::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutline.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutLine::minimumSize() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutLine11minimumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def skip(self) -> bool:
    """
    Calls Qt's 'bool QToolBarAreaLayoutLine::skip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayoutline.html#skip
    """
    #  bool QToolBarAreaLayoutLine::skip() const
    return self.uglySide.call('ritual_ZNK22QToolBarAreaLayoutLine4skipEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarAreaLayoutLine::QToolBarAreaLayoutLine()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutline.html#QToolBarAreaLayoutLine
    """
    #  QToolBarAreaLayoutLine::QToolBarAreaLayoutLine()
    self._noteCreation(QToolBarAreaLayoutLine, lambda: Rituals.call(
        'ritual_ZN22QToolBarAreaLayoutLineC1Ev',
    ))

  @overload(Qt.Orientation)
  def __init__(self, orientation: Qt.Orientation) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation
    orientation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutline.html#QToolBarAreaLayoutLine

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation
    #      orientation)
    self._noteCreation(QToolBarAreaLayoutLine, lambda: Rituals.call(
        'ritual_ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE',
        orientation.value,
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

  @staticmethod
  def fitLayout(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayoutLine::fitLayout()': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutLine.fitLayout' has no cute function yet. Qt's "
        "'void QToolBarAreaLayoutLine::fitLayout()': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
