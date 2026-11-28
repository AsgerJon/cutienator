"""
QQuickStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2/qquickstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQuickStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStyle: a plain Python object standing in front
  of one C++ QQuickStyle.

  C++ hands a QQuickStyle around as a copy, so every C++ QQuickStyle behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickStyle that has a ritual and that Python can
  call so far, 3 names in all: 'name', 'setStyle', 'setFallbackStyle'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStyle::~QQuickStyle()': the destructor: Python removes its
    C++ QQuickStyle by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickStyle is created at the first use, not by
    'QQuickStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStyle back gives a copy the ritual made for
    Python, in a new cute QQuickStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def name() -> str:
    """
    Calls Qt's 'QString QQuickStyle::name()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyle.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStyle::name()
    return Rituals.call('ritual_ZN11QQuickStyle4nameEv')

  @staticmethod
  @overload(str)
  def setStyle(style: str) -> None:
    """
    Calls Qt's 'void QQuickStyle::setStyle(const QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyle.html#setStyle

    Parameters
    ----------

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStyle::setStyle(const QString &style)
    Rituals.call('ritual_ZN11QQuickStyle8setStyleERK7QString', style)

  @staticmethod
  @overload(str)
  def setFallbackStyle(style: str) -> None:
    """
    Calls Qt's 'void QQuickStyle::setFallbackStyle(const QString &style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstyle.html#setFallbackStyle

    Parameters
    ----------

    style : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStyle::setFallbackStyle(const QString &style)
    Rituals.call(
        'ritual_ZN11QQuickStyle16setFallbackStyleERK7QString', style,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStyle'

  #  Qt's '~QQuickStyle()'. Naming it makes this a value class: Python owns
  #  every C++ QQuickStyle behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQuickStyleD1Ev'

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
