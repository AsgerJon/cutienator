"""
QQuickPagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickPanePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickPage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPagePrivate(QQuickPanePrivate):
  """
  The cute side of Qt's QQuickPagePrivate: a plain Python object standing in
  front of one C++ QQuickPagePrivate.

  It is built on the cute 'QQuickPanePrivate', as Qt's QQuickPagePrivate is
  built on Qt's QQuickPanePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPagePrivate that has a ritual and that Python
  can call so far, 8 names in all: 'q_func', 'relayout', 'resizeContent',
  'itemVisibilityChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemGeometryChanged', 'itemDestroyed'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPage *QQuickPagePrivate::q_func() const': takes in
    Python what 'QQuickPage *QQuickPagePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickPagePrivate is created at the first use, not by
    'QQuickPagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPagePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPagePrivate'

  #  A C++ QQuickPagePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPagePrivate'

  #  The functions Qt calls itself that QQuickPagePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemVisibilityChanged': (
          ('_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

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

  def q_func(self) -> Optional[QQuickPage]:
    """
    Calls Qt's 'QQuickPage *QQuickPagePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpageprivate.html#q_func

    Returns
    -------

    Optional[QQuickPage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPage *QQuickPagePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickPagePrivate6q_funcEv')
    from . import QQuickPage
    return QQuickPage._cuteAt(address)

  def relayout(self) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::relayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpageprivate.html#relayout
    """
    #  void QQuickPagePrivate::relayout()
    self.uglySide.call('ritual_ZN17QQuickPagePrivate8relayoutEv')

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#resizeContent
    """
    #  void QQuickPagePrivate::resizeContent()
    ritual = 'ritual_ZN17QQuickPagePrivate13resizeContentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPagePrivate13resizeContentEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::itemVisibilityChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#itemVisibilityChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPagePrivate::itemVisibilityChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPagePrivate21itemVisibilityChangedEP10QQuic'
          'kItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPagePrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickPagePrivate24itemImplicitWidthChangedEP10QQuickIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPagePrivate24itemImplicitWidthChangedEP10QQ'
          'uickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#itemImplicitHeightChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPagePrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN17QQuickPagePrivate25itemImplicitHeightChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPagePrivate25itemImplicitHeightChangedEP10Q'
          'QuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPagePrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickItem20Q'
        'QuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPagePrivate19itemGeometryChangedEP10QQuickI'
          'tem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPagePrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpageprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPagePrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN17QQuickPagePrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPagePrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))
