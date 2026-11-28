"""
QQuickVerticalHeaderView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVerticalHeaderView to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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
  from . import QQuickVerticalHeaderViewPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickVerticalHeaderView(QQuickHeaderViewBase):
  """
  The cute side of Qt's QQuickVerticalHeaderView: a plain Python object
  standing in front of one C++ QQuickVerticalHeaderView.

  It is built on the cute 'QQuickHeaderViewBase', as Qt's
  QQuickVerticalHeaderView is built on Qt's QQuickHeaderViewBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickVerticalHeaderView that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'd_func',
  'movableRows', 'setMovableRows', 'movableRowsChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickVerticalHeaderView::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickVerticalHeaderView::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickVerticalHeaderViewPrivate
    *QQuickVerticalHeaderView::d_func() const': takes in Python what
    'QQuickVerticalHeaderViewPrivate *QQuickVerticalHeaderView::d_func()'
    takes.
  - Qt's 'QQuickVerticalHeaderView::~QQuickVerticalHeaderView()': the
    destructor: Python never removes a C++ QQuickVerticalHeaderView.
  - Qt's 'QQuickVerticalHeaderView::QQuickVerticalHeaderView(
    QQuickVerticalHeaderViewPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickVerticalHeaderView is created at the first use, not by
    'QQuickVerticalHeaderView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickVerticalHeaderView.
  - Qt tells when it has removed the C++ QQuickVerticalHeaderView. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickVerticalHeaderView::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickverticalheaderview.html#tr

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
    #  QString QQuickVerticalHeaderView::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickVerticalHeaderView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVerticalHeaderView'

  #  A C++ QQuickVerticalHeaderView Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickVerticalHeaderView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickVerticalHeaderView::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickVerticalHeaderView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickVerticalHeaderView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def movableRows(self) -> bool:
    """
    Calls Qt's 'bool QQuickVerticalHeaderView::movableRows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html#movableRows
    """
    #  bool QQuickVerticalHeaderView::movableRows() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickVerticalHeaderView11movableRowsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMovableRows(self, movableRows: bool) -> None:
    """
    Calls Qt's 'void QQuickVerticalHeaderView::setMovableRows(bool
    movableRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html#setMovableRows

    Parameters
    ----------

    movableRows : bool
      Passed on as it is.
    """
    #  void QQuickVerticalHeaderView::setMovableRows(bool movableRows)
    self.uglySide.call(
        'ritual_ZN24QQuickVerticalHeaderView14setMovableRowsEb', movableRows,
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
    'QQuickVerticalHeaderView::QQuickVerticalHeaderView(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickVerticalHeaderView::QQuickVerticalHeaderView(QQuickItem *parent)
    self._noteCreation(QQuickVerticalHeaderView, lambda: Rituals.call(
        'ritual_ZN24QQuickVerticalHeaderViewC1EP10QQuickItem',
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

  def d_func(self) -> Optional[QQuickVerticalHeaderViewPrivate]:
    """
    Calls Qt's 'QQuickVerticalHeaderViewPrivate
    *QQuickVerticalHeaderView::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html#d_func

    Returns
    -------

    Optional[QQuickVerticalHeaderViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickVerticalHeaderViewPrivate *QQuickVerticalHeaderView::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickVerticalHeaderView6d_funcEv',
    )
    from . import QQuickVerticalHeaderViewPrivate
    return QQuickVerticalHeaderViewPrivate._cuteAt(address)

  def movableRowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVerticalHeaderView::movableRowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickverticalheaderview.html#movableRowsChanged
    """
    #  void QQuickVerticalHeaderView::movableRowsChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickVerticalHeaderView18movableRowsChangedEv',
    )
