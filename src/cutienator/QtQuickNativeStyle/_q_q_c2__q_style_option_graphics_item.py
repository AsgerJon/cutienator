"""
QQC2::QStyleOptionGraphicsItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionGraphicsItem to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTransform = WAIT['QTransform']


class QStyleOptionGraphicsItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionGraphicsItem: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionGraphicsItem.

  C++ hands a QQC2::QStyleOptionGraphicsItem around as a copy, so every C++
  QQC2::QStyleOptionGraphicsItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQC2::QStyleOptionGraphicsItem that has a ritual and
  that Python can call so far, 1 name in all: 'levelOfDetailFromTransform'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionGraphicsItem
    &QQC2::QStyleOptionGraphicsItem::operator=(const QStyleOptionGraphicsItem
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQC2::QStyleOptionGraphicsItem::~QStyleOptionGraphicsItem()': the
    destructor: Python removes its C++ QQC2::QStyleOptionGraphicsItem by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionGraphicsItem is created at the first use, not
    by 'QQC2::QStyleOptionGraphicsItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionGraphicsItem back gives a copy the
    ritual made for Python, in a new cute QQC2::QStyleOptionGraphicsItem.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionGraphicsItem, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionGraphicsItem::StyleOptionType' of Qt, with
    the 1 names Qt gives in it.
    """

    Type = Kee[int](15)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionGraphicsItem::StyleOptionVersion' of Qt, with
    the 1 names Qt gives in it.
    """

    Version = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTransform)
  def levelOfDetailFromTransform(worldTransform: QTransform) -> float:
    """
    Calls Qt's 'qreal
    QQC2::QStyleOptionGraphicsItem::levelOfDetailFromTransform(const
    QTransform &worldTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiongraphicsitem.html

    Parameters
    ----------

    worldTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  qreal QQC2::QStyleOptionGraphicsItem::levelOfDetailFromTransform(const
    #      QTransform &worldTransform)
    return Rituals.call(
        'ritual_ZN4QQC224QStyleOptionGraphicsItem26levelOfDetailFromTransfo'
        'rmERK10QTransform',
        CuteMixin._valueOf(worldTransform),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionGraphicsItem'

  #  Qt's '~QQC2::QStyleOptionGraphicsItem()'. Naming it makes this a value
  #  class: Python owns every C++ QQC2::QStyleOptionGraphicsItem behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC224QStyleOptionGraphicsItemD1Ev'

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
    'QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiongraphicsitem.html
    """
    #  QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem()
    self._noteCreation(QStyleOptionGraphicsItem, lambda: Rituals.call(
        'ritual_ZN4QQC224QStyleOptionGraphicsItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionGraphicsItem) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(const
    QStyleOptionGraphicsItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiongraphicsitem.html

    Parameters
    ----------

    other : QStyleOptionGraphicsItem
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionGraphicsItem,
      which stays Python's own.
    """
    #  QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(const
    #      QStyleOptionGraphicsItem &other)
    self._noteCreation(QStyleOptionGraphicsItem, lambda: Rituals.call(
        'ritual_ZN4QQC224QStyleOptionGraphicsItemC1ERKS0_',
        self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(int version)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiongraphicsitem.html

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(int version)
    self._noteCreation(QStyleOptionGraphicsItem, lambda: Rituals.call(
        'ritual_ZN4QQC224QStyleOptionGraphicsItemC1Ei', version,
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
