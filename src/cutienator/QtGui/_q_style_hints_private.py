"""
QStyleHintsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstylehints_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStyleHintsPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccessibilityHints, QPlatformTheme, QStyleHints
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformTheme = WAIT['QPlatformTheme']
  QStyleHints = WAIT['QStyleHints']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleHintsPrivate(QObjectPrivate):
  """
  The cute side of Qt's QStyleHintsPrivate: a plain Python object standing in
  front of one C++ QStyleHintsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QStyleHintsPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleHintsPrivate that has a ritual and that Python
  can call so far, 6 names in all: 'q_func', 'colorScheme',
  'updateColorScheme', 'update', 'accessibilityHints', 'get'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStyleHints *QStyleHintsPrivate::q_func() const': takes in
    Python what 'QStyleHints *QStyleHintsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QStyleHintsPrivate is created at the first use, not by
    'QStyleHintsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleHintsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStyleHints)
  @overload(NoneType)
  def get(q: Optional[QStyleHints]) -> Optional[QStyleHintsPrivate]:
    """
    Calls Qt's 'QStyleHintsPrivate *QStyleHintsPrivate::get(QStyleHints *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehintsprivate.html#get

    Parameters
    ----------

    q : Optional[QStyleHints]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QStyleHintsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleHintsPrivate *QStyleHintsPrivate::get(QStyleHints *q)
    address = Rituals.call(
        'ritual_ZN18QStyleHintsPrivate3getEP11QStyleHints',
        CuteMixin._addressOf(q),
    )
    return QStyleHintsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleHintsPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QStyleHintsPrivate::colorScheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehintsprivate.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QStyleHintsPrivate::colorScheme() const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK18QStyleHintsPrivate11colorSchemeEv',
    ))

  def accessibilityHints(self) -> Optional[QAccessibilityHints]:
    """
    Calls Qt's 'QAccessibilityHints *QStyleHintsPrivate::accessibilityHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehintsprivate.html#accessibilityHints

    Returns
    -------

    Optional[QAccessibilityHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibilityHints *QStyleHintsPrivate::accessibilityHints() const
    address = self.uglySide.call(
        'ritual_ZNK18QStyleHintsPrivate18accessibilityHintsEv',
    )
    from . import QAccessibilityHints
    return QAccessibilityHints._cuteAt(address)

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

  def q_func(self) -> Optional[QStyleHints]:
    """
    Calls Qt's 'QStyleHints *QStyleHintsPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehintsprivate.html#q_func

    Returns
    -------

    Optional[QStyleHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleHints *QStyleHintsPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QStyleHintsPrivate6q_funcEv')
    from . import QStyleHints
    return QStyleHints._cuteAt(address)

  @overload(Qt.ColorScheme)
  def updateColorScheme(self, colorScheme: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QStyleHintsPrivate::updateColorScheme(Qt::ColorScheme
    colorScheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylehintsprivate.html#updateColorScheme

    Parameters
    ----------

    colorScheme : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QStyleHintsPrivate::updateColorScheme(Qt::ColorScheme
    #      colorScheme)
    self.uglySide.call(
        'ritual_ZN18QStyleHintsPrivate17updateColorSchemeEN2Qt11ColorScheme'
        'E',
        colorScheme.value,
    )

  @overload(QPlatformTheme)
  @overload(NoneType)
  def update(self, theme: Optional[QPlatformTheme]) -> None:
    """
    Calls Qt's 'void QStyleHintsPrivate::update(const QPlatformTheme
    *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylehintsprivate.html#update

    Parameters
    ----------

    theme : Optional[QPlatformTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleHintsPrivate::update(const QPlatformTheme *theme)
    self.uglySide.call(
        'ritual_ZN18QStyleHintsPrivate6updateEPK14QPlatformTheme',
        self._addressOf(theme),
    )
