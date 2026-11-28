"""
QGraphsLinePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qgraphstheme_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGraphsLinePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QSharedData


class QGraphsLinePrivate(QSharedData):
  """
  The cute side of Qt's QGraphsLinePrivate: a plain Python object standing in
  front of one C++ QGraphsLinePrivate.

  It is built on the cute 'QSharedData', as Qt's QGraphsLinePrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGraphsLinePrivate around as a copy, so every C++
  QGraphsLinePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphsLinePrivate that has a ritual and that Python
  can call so far, 1 name in all: 'resetCustomBits'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphsLinePrivate::~QGraphsLinePrivate()': the destructor: Python
    removes its C++ QGraphsLinePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on
  'comparesEqual(QGraphsLinePrivate const&, QGraphsLinePrivate const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QGraphsLinePrivate is created at the first use, not by
    'QGraphsLinePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphsLinePrivate back gives a copy the ritual made
    for Python, in a new cute QGraphsLinePrivate.
  """

  #  The classes Qt writes inside QGraphsLinePrivate, each a class in here as
  #  in C++.

  class QGraphsLineCustomField(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphsLinePrivate::QGraphsLineCustomField: a plain
    Python object standing in front of one C++
    QGraphsLinePrivate::QGraphsLineCustomField.

    C++ hands a QGraphsLinePrivate::QGraphsLineCustomField around as a copy,
    so every C++ QGraphsLinePrivate::QGraphsLineCustomField behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QGraphsLinePrivate::QGraphsLineCustomField yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QGraphsLinePrivate::QGraphsLineCustomField::~QGraphsLineCustomField(
      )': the destructor: Python removes its C++
      QGraphsLinePrivate::QGraphsLineCustomField by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGraphsLinePrivate::QGraphsLineCustomField is created at the
      first use, not by 'QGraphsLinePrivate::QGraphsLineCustomField(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphsLinePrivate::QGraphsLineCustomField back
      gives a copy the ritual made for Python, in a new cute
      QGraphsLinePrivate::QGraphsLineCustomField.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphsLinePrivate::QGraphsLineCustomField'

    #  Qt's '~QGraphsLinePrivate::QGraphsLineCustomField()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QGraphsLinePrivate::QGraphsLineCustomField behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QGraphsLinePrivate22QGraphsLineCustomFieldD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGraphsLinePrivate::QGraphsLineCustomField::QGraphsLineCustomField()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphslineprivate-qgraphslinecustomfield.html
      """
      #  QGraphsLinePrivate::QGraphsLineCustomField::QGraphsLineCustomField()
      self._noteCreation(
          QGraphsLinePrivate.QGraphsLineCustomField, lambda: Rituals.call(
              'ritual_ZN18QGraphsLinePrivate22QGraphsLineCustomFieldC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphsLinePrivate'

  #  Qt's '~QGraphsLinePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGraphsLinePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGraphsLinePrivateD1Ev'

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
    'QGraphsLinePrivate::QGraphsLinePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphslineprivate.html#QGraphsLinePrivate
    """
    #  QGraphsLinePrivate::QGraphsLinePrivate()
    self._noteCreation(QGraphsLinePrivate, lambda: Rituals.call(
        'ritual_ZN18QGraphsLinePrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGraphsLinePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QGraphsLinePrivate::QGraphsLinePrivate(const QGraphsLinePrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphslineprivate.html#QGraphsLinePrivate

    Parameters
    ----------

    other : QGraphsLinePrivate
      Passed on as a value: Qt reads the C++ QGraphsLinePrivate, which stays
      Python's own.
    """
    #  QGraphsLinePrivate::QGraphsLinePrivate(const QGraphsLinePrivate
    #      &other)
    self._noteCreation(QGraphsLinePrivate, lambda: Rituals.call(
        'ritual_ZN18QGraphsLinePrivateC1ERKS_', self._valueOf(other),
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

  def resetCustomBits(self) -> None:
    """
    Calls Qt's 'void QGraphsLinePrivate::resetCustomBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphslineprivate.html#resetCustomBits
    """
    #  void QGraphsLinePrivate::resetCustomBits()
    self.uglySide.call('ritual_ZN18QGraphsLinePrivate15resetCustomBitsEv')
