"""
QQuickStackLayoutAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackLayoutAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickStackLayout
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickStackLayout = WAIT['QQuickStackLayout']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackLayoutAttached(QObject):
  """
  The cute side of Qt's QQuickStackLayoutAttached: a plain Python object
  standing in front of one C++ QQuickStackLayoutAttached.

  It is built on the cute 'QObject', as Qt's QQuickStackLayoutAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStackLayoutAttached that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'index',
  'setIndex', 'isCurrentItem', 'setIsCurrentItem', 'layout', 'setLayout',
  'indexChanged', 'isCurrentItemChanged', 'layoutChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStackLayoutAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickStackLayoutAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStackLayoutAttached is created at the first use, not by
    'QQuickStackLayoutAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackLayoutAttached.
  - Qt tells when it has removed the C++ QQuickStackLayoutAttached. Every
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
    Calls Qt's 'QString QQuickStackLayoutAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacklayoutattached.html#tr

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
    #  QString QQuickStackLayoutAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickStackLayoutAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackLayoutAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStackLayoutAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStackLayoutAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickStackLayoutAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickStackLayoutAttached::index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#index
    """
    #  int QQuickStackLayoutAttached::index() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickStackLayoutAttached5indexEv',
    )

  def isCurrentItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickStackLayoutAttached::isCurrentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#isCurrentItem
    """
    #  bool QQuickStackLayoutAttached::isCurrentItem() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickStackLayoutAttached13isCurrentItemEv',
    )

  def layout(self) -> Optional[QQuickStackLayout]:
    """
    Calls Qt's 'QQuickStackLayout *QQuickStackLayoutAttached::layout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#layout

    Returns
    -------

    Optional[QQuickStackLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackLayout *QQuickStackLayoutAttached::layout() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickStackLayoutAttached6layoutEv',
    )
    from . import QQuickStackLayout
    return QQuickStackLayout._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::setIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickStackLayoutAttached::setIndex(int index)
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached8setIndexEi', index,
    )

  @overload(bool)
  def setIsCurrentItem(self, isCurrentItem: bool) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::setIsCurrentItem(bool
    isCurrentItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#setIsCurrentItem

    Parameters
    ----------

    isCurrentItem : bool
      Passed on as it is.
    """
    #  void QQuickStackLayoutAttached::setIsCurrentItem(bool isCurrentItem)
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached16setIsCurrentItemEb',
        isCurrentItem,
    )

  @overload(QQuickStackLayout)
  @overload(NoneType)
  def setLayout(self, layout: Optional[QQuickStackLayout]) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::setLayout(QQuickStackLayout
    *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#setLayout

    Parameters
    ----------

    layout : Optional[QQuickStackLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackLayoutAttached::setLayout(QQuickStackLayout *layout)
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached9setLayoutEP17QQuickStackLayou'
        't',
        self._addressOf(layout),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, object: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackLayoutAttached::QQuickStackLayoutAttached(QObject *object)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickStackLayoutAttached::QQuickStackLayoutAttached(QObject *object)
    self._noteCreation(QQuickStackLayoutAttached, lambda: Rituals.call(
        'ritual_ZN25QQuickStackLayoutAttachedC1EP7QObject',
        self._addressOf(object, 'QObject'),
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

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#indexChanged
    """
    #  void QQuickStackLayoutAttached::indexChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached12indexChangedEv',
    )

  def isCurrentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::isCurrentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html
    """
    #  void QQuickStackLayoutAttached::isCurrentItemChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached20isCurrentItemChangedEv',
    )

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackLayoutAttached::layoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstacklayoutattached.html#layoutChanged
    """
    #  void QQuickStackLayoutAttached::layoutChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickStackLayoutAttached13layoutChangedEv',
    )
