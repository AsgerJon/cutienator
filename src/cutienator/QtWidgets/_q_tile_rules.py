"""
QTileRules binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdrawutil.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


class QTileRules(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTileRules: a plain Python object standing in front
  of one C++ QTileRules.

  C++ hands a QTileRules around as a copy, so every C++ QTileRules behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QTileRules yet. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTileRules::~QTileRules()': the destructor: Python removes its C++
    QTileRules by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTileRules is created at the first use, not by 'QTileRules(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTileRules back gives a copy the ritual made for
    Python, in a new cute QTileRules.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTileRules'

  #  Qt's '~QTileRules()'. Naming it makes this a value class: Python owns
  #  every C++ QTileRules behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QTileRulesD1Ev'

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

  @overload(Qt.TileRule, Qt.TileRule)
  def __init__(
      self,
      horizontalRule: Qt.TileRule,
      verticalRule: Qt.TileRule,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTileRules::QTileRules(Qt::TileRule
    horizontalRule, Qt::TileRule verticalRule)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qtilerules.html#QTileRules

    Parameters
    ----------

    horizontalRule : Qt.TileRule
      Passed on as its number.

    verticalRule : Qt.TileRule
      Passed on as its number.
    """
    #  QTileRules::QTileRules(Qt::TileRule horizontalRule, Qt::TileRule
    #      verticalRule)
    self._noteCreation(QTileRules, lambda: Rituals.call(
        'ritual_ZN10QTileRulesC1EN2Qt8TileRuleES1_',
        horizontalRule.value, verticalRule.value,
    ))

  @overload()
  @overload(Qt.TileRule)
  def __init__(self, rule: Qt.TileRule = Qt.TileRule.StretchTile) -> None:
    """
    Notes what was given, for Qt's 'QTileRules::QTileRules(Qt::TileRule
    rule)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtilerules.html#QTileRules

    Parameters
    ----------

    rule : Qt.TileRule
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.TileRule.StretchTile.
    """
    #  QTileRules::QTileRules(Qt::TileRule rule)
    self._noteCreation(QTileRules, lambda: Rituals.call(
        'ritual_ZN10QTileRulesC1EN2Qt8TileRuleE', rule.value,
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
