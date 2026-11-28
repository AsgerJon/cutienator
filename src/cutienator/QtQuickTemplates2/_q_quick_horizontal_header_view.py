"""
QQuickHorizontalHeaderView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickHorizontalHeaderView to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickHeaderViewBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickHorizontalHeaderViewPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHorizontalHeaderView(QQuickHeaderViewBase):
  """
  The cute side of Qt's QQuickHorizontalHeaderView: a plain Python object
  standing in front of one C++ QQuickHorizontalHeaderView.

  It is built on the cute 'QQuickHeaderViewBase', as Qt's
  QQuickHorizontalHeaderView is built on Qt's QQuickHeaderViewBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHorizontalHeaderView that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr', 'd_func',
  'movableColumns', 'setMovableColumns', 'movableColumnsChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickHorizontalHeaderView::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickHorizontalHeaderView::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickHorizontalHeaderViewPrivate
    *QQuickHorizontalHeaderView::d_func() const': takes in Python what
    'QQuickHorizontalHeaderViewPrivate *QQuickHorizontalHeaderView::d_func()'
    takes.
  - Qt's 'QQuickHorizontalHeaderView::~QQuickHorizontalHeaderView()': the
    destructor: Python never removes a C++ QQuickHorizontalHeaderView.
  - Qt's 'QQuickHorizontalHeaderView::QQuickHorizontalHeaderView(
    QQuickHorizontalHeaderViewPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickHorizontalHeaderView is created at the first use, not by
    'QQuickHorizontalHeaderView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHorizontalHeaderView.
  - Qt tells when it has removed the C++ QQuickHorizontalHeaderView. Every
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
    Calls Qt's 'QString QQuickHorizontalHeaderView::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhorizontalheaderview.html#tr

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
    #  QString QQuickHorizontalHeaderView::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickHorizontalHeaderView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHorizontalHeaderView'

  #  A C++ QQuickHorizontalHeaderView Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickHorizontalHeaderView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickHorizontalHeaderView::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickHorizontalHeaderView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickHorizontalHeaderView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def movableColumns(self) -> bool:
    """
    Calls Qt's 'bool QQuickHorizontalHeaderView::movableColumns() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html#movableColumns
    """
    #  bool QQuickHorizontalHeaderView::movableColumns() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickHorizontalHeaderView14movableColumnsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMovableColumns(self, movableColumns: bool) -> None:
    """
    Calls Qt's 'void QQuickHorizontalHeaderView::setMovableColumns(bool
    movableColumns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html#setMovableColumns

    Parameters
    ----------

    movableColumns : bool
      Passed on as it is.
    """
    #  void QQuickHorizontalHeaderView::setMovableColumns(bool
    #      movableColumns)
    self.uglySide.call(
        'ritual_ZN26QQuickHorizontalHeaderView17setMovableColumnsEb',
        movableColumns,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickHorizontalHeaderView::QQuickHorizontalHeaderView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickHorizontalHeaderView::QQuickHorizontalHeaderView(QQuickItem
    #      *parent)
    self._noteCreation(QQuickHorizontalHeaderView, lambda: Rituals.call(
        'ritual_ZN26QQuickHorizontalHeaderViewC1EP10QQuickItem',
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

  def d_func(self) -> Optional[QQuickHorizontalHeaderViewPrivate]:
    """
    Calls Qt's 'QQuickHorizontalHeaderViewPrivate
    *QQuickHorizontalHeaderView::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html#d_func

    Returns
    -------

    Optional[QQuickHorizontalHeaderViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHorizontalHeaderViewPrivate
    #      *QQuickHorizontalHeaderView::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickHorizontalHeaderView6d_funcEv',
    )
    from . import QQuickHorizontalHeaderViewPrivate
    return QQuickHorizontalHeaderViewPrivate._cuteAt(address)

  def movableColumnsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHorizontalHeaderView::movableColumnsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhorizontalheaderview.html
    """
    #  void QQuickHorizontalHeaderView::movableColumnsChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickHorizontalHeaderView21movableColumnsChangedEv',
    )
