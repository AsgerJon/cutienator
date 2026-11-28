"""
Qt3DExtras::QSpriteSheetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qspritesheetitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpriteSheetItem(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DExtras::QSpriteSheetItem: a plain Python object
  standing in front of one C++ Qt3DExtras::QSpriteSheetItem.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DExtras::QSpriteSheetItem is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSpriteSheetItem that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr', 'x', 'y',
  'width', 'height', 'setX', 'setY', 'setWidth', 'setHeight', 'xChanged',
  'yChanged', 'widthChanged', 'heightChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QSpriteSheetItem::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QSpriteSheetItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSpriteSheetItemPrivate
    *Qt3DExtras::QSpriteSheetItem::d_func() const': takes in Python what
    'QSpriteSheetItemPrivate *Qt3DExtras::QSpriteSheetItem::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSpriteSheetItem is created at the first use, not by
    'Qt3DExtras::QSpriteSheetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSpriteSheetItem.
  - Qt tells when it has removed the C++ Qt3DExtras::QSpriteSheetItem. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QSpriteSheetItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QSpriteSheetItem::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSpriteSheetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QSpriteSheetItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QSpriteSheetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QSpriteSheetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteSheetItem::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#x
    """
    #  int Qt3DExtras::QSpriteSheetItem::x() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras16QSpriteSheetItem1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteSheetItem::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#y
    """
    #  int Qt3DExtras::QSpriteSheetItem::y() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras16QSpriteSheetItem1yEv')

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteSheetItem::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#width
    """
    #  int Qt3DExtras::QSpriteSheetItem::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QSpriteSheetItem5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteSheetItem::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#height
    """
    #  int Qt3DExtras::QSpriteSheetItem::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QSpriteSheetItem6heightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::setX(int x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::setX(int x)
    self.uglySide.call('ritual_ZN10Qt3DExtras16QSpriteSheetItem4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::setY(int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::setY(int y)
    self.uglySide.call('ritual_ZN10Qt3DExtras16QSpriteSheetItem4setYEi', y)

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::setWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::setWidth(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem8setWidthEi', width,
    )

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::setHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::setHeight(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem9setHeightEi', height,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QSpriteSheetItem::QSpriteSheetItem(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#QSpriteSheetItem

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QSpriteSheetItem::QSpriteSheetItem(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QSpriteSheetItem, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItemC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(int)
  def xChanged(self, x: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::xChanged(int x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#xChanged

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::xChanged(int x)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem8xChangedEi', x,
    )

  @overload(int)
  def yChanged(self, y: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::yChanged(int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#yChanged

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::yChanged(int y)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem8yChangedEi', y,
    )

  @overload(int)
  def widthChanged(self, width: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::widthChanged(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#widthChanged

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::widthChanged(int width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem12widthChangedEi', width,
    )

  @overload(int)
  def heightChanged(self, height: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteSheetItem::heightChanged(int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#heightChanged

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteSheetItem::heightChanged(int height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem13heightChangedEi', height,
    )

  def d_func(self) -> Optional[Qt3DExtras.QSpriteSheetItemPrivate]:
    """
    Calls Qt's 'QSpriteSheetItemPrivate
    *Qt3DExtras::QSpriteSheetItem::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritesheetitem.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QSpriteSheetItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpriteSheetItemPrivate *Qt3DExtras::QSpriteSheetItem::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QSpriteSheetItem6d_funcEv',
    )
    return Qt3DExtras.QSpriteSheetItemPrivate._cuteAt(address)
