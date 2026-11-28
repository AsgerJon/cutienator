"""
QToolBarAreaLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBarAreaLayoutItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayoutItem = WAIT['QLayoutItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBarAreaLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QToolBarAreaLayoutItem: a plain Python object
  standing in front of one C++ QToolBarAreaLayoutItem.

  C++ hands a QToolBarAreaLayoutItem around as a copy, so every C++
  QToolBarAreaLayoutItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QToolBarAreaLayoutItem that has a ritual and that
  Python can call so far, 6 names in all: 'skip', 'minimumSize', 'sizeHint',
  'realSizeHint', 'resize', 'extendSize'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolBarAreaLayoutItem::~QToolBarAreaLayoutItem()': the destructor:
    Python removes its C++ QToolBarAreaLayoutItem by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QToolBarAreaLayoutItem is created at the first use, not by
    'QToolBarAreaLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QToolBarAreaLayoutItem back gives a copy the ritual
    made for Python, in a new cute QToolBarAreaLayoutItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarAreaLayoutItem'

  #  Qt's '~QToolBarAreaLayoutItem()'. Naming it makes this a value class:
  #  Python owns every C++ QToolBarAreaLayoutItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QToolBarAreaLayoutItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def skip(self) -> bool:
    """
    Calls Qt's 'bool QToolBarAreaLayoutItem::skip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#skip
    """
    #  bool QToolBarAreaLayoutItem::skip() const
    return self.uglySide.call('ritual_ZNK22QToolBarAreaLayoutItem4skipEv')

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutItem::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutItem::minimumSize() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutItem11minimumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutItem::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutItem::sizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutItem8sizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def realSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutItem::realSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#realSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutItem::realSizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutItem12realSizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
  @overload(QLayoutItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QLayoutItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarAreaLayoutItem::QToolBarAreaLayoutItem(QLayoutItem *item)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#QToolBarAreaLayoutItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QToolBarAreaLayoutItem::QToolBarAreaLayoutItem(QLayoutItem *item)
    self._noteCreation(QToolBarAreaLayoutItem, lambda: Rituals.call(
        'ritual_ZN22QToolBarAreaLayoutItemC1EP11QLayoutItem',
        self._addressOf(item, 'QLayoutItem'),
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

  @overload(Qt.Orientation, int)
  def resize(self, o: Qt.Orientation, newSize: int) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutItem::resize(Qt::Orientation o, int
    newSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#resize

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.

    newSize : int
      Passed on as it is.
    """
    #  void QToolBarAreaLayoutItem::resize(Qt::Orientation o, int newSize)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutItem6resizeEN2Qt11OrientationEi',
        o.value, newSize,
    )

  @overload(Qt.Orientation, int)
  def extendSize(self, o: Qt.Orientation, extent: int) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutItem::extendSize(Qt::Orientation o,
    int extent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutitem.html#extendSize

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.

    extent : int
      Passed on as it is.
    """
    #  void QToolBarAreaLayoutItem::extendSize(Qt::Orientation o, int extent)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutItem10extendSizeEN2Qt11OrientationEi',
        o.value, extent,
    )
