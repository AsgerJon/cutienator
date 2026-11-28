"""
QCategory3DAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qcategory3daxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCategory3DAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QStringList
from . import QAbstract3DAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCategory3DAxis


class QCategory3DAxisPrivate(QAbstract3DAxisPrivate):
  """
  The cute side of Qt's QCategory3DAxisPrivate: a plain Python object
  standing in front of one C++ QCategory3DAxisPrivate.

  It is built on the cute 'QAbstract3DAxisPrivate', as Qt's
  QCategory3DAxisPrivate is built on Qt's QAbstract3DAxisPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCategory3DAxisPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'setDataLabels',
  'allowZero', 'allowNegatives', 'allowMinMaxSame'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCategory3DAxis *QCategory3DAxisPrivate::q_func() const':
    takes in Python what 'QCategory3DAxis *QCategory3DAxisPrivate::q_func()'
    takes.
  - Qt's 'QCategory3DAxisPrivate::~QCategory3DAxisPrivate()': the destructor:
    Python never removes a C++ QCategory3DAxisPrivate.

  What to expect
  --------------

  - The C++ QCategory3DAxisPrivate is created at the first use, not by
    'QCategory3DAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCategory3DAxisPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCategory3DAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QCategory3DAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCategory3DAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setDataLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QCategory3DAxisPrivate::setDataLabels(const QStringList
    &labels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxisprivate.html#setDataLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCategory3DAxisPrivate::setDataLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN22QCategory3DAxisPrivate13setDataLabelsERK5QListI7QString'
        'E',
        self._valueOf(labels),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCategory3DAxisPrivate::QCategory3DAxisPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxisprivate.html#QCategory3DAxisPrivate
    """
    #  QCategory3DAxisPrivate::QCategory3DAxisPrivate()
    self._noteCreation(QCategory3DAxisPrivate, lambda: Rituals.call(
        'ritual_ZN22QCategory3DAxisPrivateC1Ev',
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

  def q_func(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QCategory3DAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcategory3daxisprivate.html#q_func

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QCategory3DAxisPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QCategory3DAxisPrivate6q_funcEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def allowZero(self) -> bool:
    """
    Calls Qt's 'bool QCategory3DAxisPrivate::allowZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxisprivate.html#allowZero
    """
    #  bool QCategory3DAxisPrivate::allowZero()
    ritual = 'ritual_ZN22QCategory3DAxisPrivate9allowZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QCategory3DAxisPrivate9allowZeroEv'
    return self.uglySide.call(ritual)

  def allowNegatives(self) -> bool:
    """
    Calls Qt's 'bool QCategory3DAxisPrivate::allowNegatives()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxisprivate.html#allowNegatives
    """
    #  bool QCategory3DAxisPrivate::allowNegatives()
    ritual = 'ritual_ZN22QCategory3DAxisPrivate14allowNegativesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QCategory3DAxisPrivate14allowNegativesEv'
    return self.uglySide.call(ritual)

  def allowMinMaxSame(self) -> bool:
    """
    Calls Qt's 'bool QCategory3DAxisPrivate::allowMinMaxSame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategory3daxisprivate.html#allowMinMaxSame
    """
    #  bool QCategory3DAxisPrivate::allowMinMaxSame()
    ritual = 'ritual_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv'
    return self.uglySide.call(ritual)
