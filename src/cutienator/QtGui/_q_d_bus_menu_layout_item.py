"""
QDBusMenuLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMenuLayoutItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDBusPlatformMenu, QDBusPlatformMenuItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusPlatformMenu = WAIT['QDBusPlatformMenu']
  QDBusPlatformMenuItem = WAIT['QDBusPlatformMenuItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusMenuLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMenuLayoutItem: a plain Python object standing
  in front of one C++ QDBusMenuLayoutItem.

  C++ hands a QDBusMenuLayoutItem around as a copy, so every C++
  QDBusMenuLayoutItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMenuLayoutItem that has a ritual and that
  Python can call so far, 1 name in all: 'populate'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusMenuLayoutItem::~QDBusMenuLayoutItem()': the destructor:
    Python removes its C++ QDBusMenuLayoutItem by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'QDBusPlatformMenuItem.

  What to expect
  --------------

  - The C++ QDBusMenuLayoutItem is created at the first use, not by
    'QDBusMenuLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMenuLayoutItem back gives a copy the ritual made
    for Python, in a new cute QDBusMenuLayoutItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMenuLayoutItem'

  #  Qt's '~QDBusMenuLayoutItem()'. Naming it makes this a value class:
  #  Python owns every C++ QDBusMenuLayoutItem behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDBusMenuLayoutItemD1Ev'

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

  @overload(QDBusPlatformMenu, int, QStringList)
  @overload(NoneType, int, QStringList)
  def populate(
      self,
      menu: Optional[QDBusPlatformMenu],
      depth: int,
      propertyNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QDBusMenuLayoutItem::populate(const QDBusPlatformMenu
    *menu, int depth, const QStringList &propertyNames)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenulayoutitem.html#populate

    Parameters
    ----------

    menu : Optional[QDBusPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    depth : int
      Passed on as it is.

    propertyNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusMenuLayoutItem::populate(const QDBusPlatformMenu *menu, int
    #      depth, const QStringList &propertyNames)
    self.uglySide.call(
        'ritual_ZN19QDBusMenuLayoutItem8populateEPK17QDBusPlatformMenuiRK5Q'
        'ListI7QStringE',
        self._addressOf(menu), depth, self._valueOf(propertyNames),
    )

  @overload(QDBusPlatformMenuItem, int, QStringList)
  def populate(
      self,
      item: Optional[QDBusPlatformMenuItem],
      depth: int,
      propertyNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QDBusMenuLayoutItem::populate(const
    QDBusPlatformMenuItem *item, int depth, const QStringList
    &propertyNames)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenulayoutitem.html#populate

    Parameters
    ----------

    item : Optional[QDBusPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    depth : int
      Passed on as it is.

    propertyNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusMenuLayoutItem::populate(const QDBusPlatformMenuItem *item,
    #      int depth, const QStringList &propertyNames)
    self.uglySide.call(
        'ritual_ZN19QDBusMenuLayoutItem8populateEPK21QDBusPlatformMenuItemi'
        'RK5QListI7QStringE',
        self._addressOf(item), depth, self._valueOf(propertyNames),
    )
