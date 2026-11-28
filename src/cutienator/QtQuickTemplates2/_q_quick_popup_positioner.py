"""
QQuickPopupPositioner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopuppositioner_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupPositioner to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItemChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickPopup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickPopup = WAIT['QQuickPopup']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupPositioner(QQuickItemChangeListener):
  """
  The cute side of Qt's QQuickPopupPositioner: a plain Python object standing
  in front of one C++ QQuickPopupPositioner.

  It is built on the cute 'QQuickItemChangeListener', as Qt's
  QQuickPopupPositioner is built on Qt's QQuickItemChangeListener, and has
  everything that class has.

  C++ hands a QQuickPopupPositioner around as a copy, so every C++
  QQuickPopupPositioner behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickPopupPositioner that has a ritual and that
  Python can call so far, 10 names in all: 'popup', 'parentItem',
  'setParentItem', 'reposition', 'itemGeometryChanged', 'itemParentChanged',
  'itemChildRemoved', 'removeAncestorListeners', 'addAncestorListeners',
  'repositionPopupWindow'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickPopupPositioner::~QQuickPopupPositioner()': the destructor:
    Python removes its C++ QQuickPopupPositioner by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickPopupPositioner is created at the first use, not by
    'QQuickPopupPositioner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickPopupPositioner back gives a copy the ritual
    made for Python, in a new cute QQuickPopupPositioner.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupPositioner'

  #  A C++ QQuickPopupPositioner Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPopupPositioner'

  #  The functions Qt calls itself that QQuickPopupPositioner is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'reposition': (
          ('_ZN21QQuickPopupPositioner10repositionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QQuickPopupPositioner()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickPopupPositioner behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuickPopupPositionerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def popup(self) -> Optional[QQuickPopup]:
    """
    Calls Qt's 'QQuickPopup *QQuickPopupPositioner::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopuppositioner.html#popup

    Returns
    -------

    Optional[QQuickPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopup *QQuickPopupPositioner::popup() const
    address = self.uglySide.call('ritual_ZNK21QQuickPopupPositioner5popupEv')
    from . import QQuickPopup
    return QQuickPopup._cuteAt(address)

  def parentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopupPositioner::parentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#parentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopupPositioner::parentItem() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPopupPositioner10parentItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setParentItem(self, parent: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::setParentItem(QQuickItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#setParentItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPositioner::setParentItem(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN21QQuickPopupPositioner13setParentItemEP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QQuickPopup)
  @overload(NoneType)
  def __init__(self, popup: Optional[QQuickPopup]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupPositioner::QQuickPopupPositioner(QQuickPopup *popup)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#QQuickPopupPositioner

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPopupPositioner::QQuickPopupPositioner(QQuickPopup *popup)
    self._noteCreation(QQuickPopupPositioner, lambda: Rituals.call(
        'ritual_ZN21QQuickPopupPositionerC1EP11QQuickPopup',
        self._addressOf(popup),
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

  def reposition(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::reposition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#reposition
    """
    #  void QQuickPopupPositioner::reposition()
    ritual = 'ritual_ZN21QQuickPopupPositioner10repositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickPopupPositioner10repositionEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::itemGeometryChanged(QQuickItem
    *a0, QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPopupPositioner::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN21QQuickPopupPositioner19itemGeometryChangedEP10QQuickIte'
        'm20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPopupPositioner19itemGeometryChangedEP10QQu'
          'ickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      a0: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::itemParentChanged(QQuickItem *a0,
    QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#itemParentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPositioner::itemParentChanged(QQuickItem *a0,
    #      QQuickItem *parent)
    ritual = (
        'ritual_ZN21QQuickPopupPositioner17itemParentChangedEP10QQuickItemS'
        '1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPopupPositioner17itemParentChangedEP10QQuic'
          'kItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(parent))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildRemoved(
      self,
      a0: Optional[QQuickItem],
      child: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::itemChildRemoved(QQuickItem *a0,
    QQuickItem *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#itemChildRemoved

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPositioner::itemChildRemoved(QQuickItem *a0,
    #      QQuickItem *child)
    ritual = (
        'ritual_ZN21QQuickPopupPositioner16itemChildRemovedEP10QQuickItemS1'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPopupPositioner16itemChildRemovedEP10QQuick'
          'ItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(child))

  @overload(QQuickItem)
  @overload(NoneType)
  def removeAncestorListeners(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickPopupPositioner::removeAncestorListeners(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#removeAncestorListeners

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPositioner::removeAncestorListeners(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN21QQuickPopupPositioner23removeAncestorListenersEP10QQuic'
        'kItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def addAncestorListeners(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::addAncestorListeners(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#addAncestorListeners

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupPositioner::addAncestorListeners(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN21QQuickPopupPositioner20addAncestorListenersEP10QQuickIt'
        'em',
        self._addressOf(item),
    )

  def repositionPopupWindow(self) -> None:
    """
    Calls Qt's 'void QQuickPopupPositioner::repositionPopupWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuppositioner.html#repositionPopupWindow
    """
    #  void QQuickPopupPositioner::repositionPopupWindow()
    self.uglySide.call(
        'ritual_ZN21QQuickPopupPositioner21repositionPopupWindowEv',
    )
