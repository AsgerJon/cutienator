"""
QGridLayoutBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGridLayoutBox to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QGridLayoutBox(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGridLayoutBox: a plain Python object standing in
  front of one C++ QGridLayoutBox.

  C++ hands a QGridLayoutBox around as a copy, so every C++ QGridLayoutBox
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGridLayoutBox that has a ritual and that Python can
  call so far, 4 names in all: 'add', 'combine', 'normalize', 'q_sizes'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGridLayoutBox::~QGridLayoutBox()': the destructor: Python removes
    its C++ QGridLayoutBox by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QGridLayoutBox is created at the first use, not by
    'QGridLayoutBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGridLayoutBox back gives a copy the ritual made for
    Python, in a new cute QGridLayoutBox.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGridLayoutBox'

  #  Qt's '~QGridLayoutBox()'. Naming it makes this a value class: Python
  #  owns every C++ QGridLayoutBox behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QGridLayoutBoxD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def q_sizes(self, which: int) -> float:
    """
    Calls Qt's 'const qreal &QGridLayoutBox::q_sizes(int which) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutbox.html#q_sizes

    Parameters
    ----------

    which : int
      Passed on as it is.
    """
    #  const qreal &QGridLayoutBox::q_sizes(int which) const
    return self.uglySide.call('ritual_ZNK14QGridLayoutBox7q_sizesEi', which)

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
    Notes what was given, for Qt's 'QGridLayoutBox::QGridLayoutBox()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutbox.html#QGridLayoutBox
    """
    #  QGridLayoutBox::QGridLayoutBox()
    self._noteCreation(QGridLayoutBox, lambda: Rituals.call(
        'ritual_ZN14QGridLayoutBoxC1Ev',
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

  @overload(THIS, int, float)
  def add(self, other: QGridLayoutBox, stretch: int, spacing: float) -> None:
    """
    Calls Qt's 'void QGridLayoutBox::add(const QGridLayoutBox &other, int
    stretch, qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutbox.html#add

    Parameters
    ----------

    other : QGridLayoutBox
      Passed on as a value: Qt reads the C++ QGridLayoutBox, which stays
      Python's own.

    stretch : int
      Passed on as it is.

    spacing : float
      Passed on as it is.
    """
    #  void QGridLayoutBox::add(const QGridLayoutBox &other, int stretch,
    #      qreal spacing)
    self.uglySide.call(
        'ritual_ZN14QGridLayoutBox3addERKS_id',
        self._valueOf(other), stretch, spacing,
    )

  @overload(THIS)
  def combine(self, other: QGridLayoutBox) -> None:
    """
    Calls Qt's 'void QGridLayoutBox::combine(const QGridLayoutBox &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutbox.html#combine

    Parameters
    ----------

    other : QGridLayoutBox
      Passed on as a value: Qt reads the C++ QGridLayoutBox, which stays
      Python's own.
    """
    #  void QGridLayoutBox::combine(const QGridLayoutBox &other)
    self.uglySide.call(
        'ritual_ZN14QGridLayoutBox7combineERKS_', self._valueOf(other),
    )

  def normalize(self) -> None:
    """
    Calls Qt's 'void QGridLayoutBox::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutbox.html#normalize
    """
    #  void QGridLayoutBox::normalize()
    self.uglySide.call('ritual_ZN14QGridLayoutBox9normalizeEv')
