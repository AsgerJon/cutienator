"""
QSpacerItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayoutItem, QSizePolicyPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QSizePolicy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QSpacerItem(QLayoutItem):
  """
  The cute side of Qt's QSpacerItem: a plain Python object standing in front
  of one C++ QSpacerItem.

  It is built on the cute 'QLayoutItem', as Qt's QSpacerItem is built on Qt's
  QLayoutItem, and has everything that class has.

  C++ hands a QSpacerItem around as a copy, so every C++ QSpacerItem behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSpacerItem that has a ritual and that Python can
  call so far, 10 names in all: 'changeSize', 'sizeHint', 'minimumSize',
  'maximumSize', 'expandingDirections', 'isEmpty', 'setGeometry', 'geometry',
  'spacerItem', 'sizePolicy'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSpacerItem::~QSpacerItem()': the destructor: Python removes its
    C++ QSpacerItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSpacerItem is created at the first use, not by
    'QSpacerItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSpacerItem back gives a copy the ritual made for
    Python, in a new cute QSpacerItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpacerItem'

  #  Qt's '~QSpacerItem()'. Naming it makes this a value class: Python owns
  #  every C++ QSpacerItem behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QSpacerItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSpacerItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSpacerItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK11QSpacerItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSpacerItem::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSpacerItem::minimumSize() const
    address = self.uglySide.call('ritual_ZNK11QSpacerItem11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSpacerItem::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSpacerItem::maximumSize() const
    address = self.uglySide.call('ritual_ZNK11QSpacerItem11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QSpacerItem::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspaceritem.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QSpacerItem::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK11QSpacerItem19expandingDirectionsEv',
    ))

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSpacerItem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#isEmpty
    """
    #  bool QSpacerItem::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QSpacerItem7isEmptyEv')

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QSpacerItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSpacerItem::geometry() const
    address = self.uglySide.call('ritual_ZNK11QSpacerItem8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def sizePolicy(self) -> QSizePolicy:
    """
    Calls Qt's 'QSizePolicy QSpacerItem::sizePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#sizePolicy

    Returns
    -------

    QSizePolicy
      A new cute QSizePolicy around the copy Qt gave back. Python owns it.
    """
    #  QSizePolicy QSpacerItem::sizePolicy() const
    address = self.uglySide.call('ritual_ZNK11QSpacerItem10sizePolicyEv')
    from . import QSizePolicy
    return QSizePolicy._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QSpacerItem::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSpacerItem::setGeometry(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN11QSpacerItem11setGeometryERK5QRect', self._valueOf(a0),
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

  @overload(int, int)
  @overload(int, int, QSizePolicyPolicy)
  @overload(int, int, QSizePolicyPolicy, QSizePolicyPolicy)
  def __init__(
      self,
      w: int,
      h: int,
      hData: QSizePolicy.Policy = QSizePolicyPolicy.Minimum,
      vData: QSizePolicy.Policy = QSizePolicyPolicy.Minimum,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSpacerItem::QSpacerItem(int w, int h,
    QSizePolicy::Policy hData, QSizePolicy::Policy vData)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#QSpacerItem

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    hData : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicyPolicy.Minimum.

    vData : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicyPolicy.Minimum.
    """
    #  QSpacerItem::QSpacerItem(int w, int h, QSizePolicy::Policy hData,
    #      QSizePolicy::Policy vData)
    self._noteCreation(QSpacerItem, lambda: Rituals.call(
        'ritual_ZN11QSpacerItemC1EiiN11QSizePolicy6PolicyES1_',
        w, h, hData.value, vData.value,
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

  @overload(int, int)
  @overload(int, int, QSizePolicyPolicy)
  @overload(int, int, QSizePolicyPolicy, QSizePolicyPolicy)
  def changeSize(
      self,
      w: int,
      h: int,
      hData: QSizePolicy.Policy = QSizePolicyPolicy.Minimum,
      vData: QSizePolicy.Policy = QSizePolicyPolicy.Minimum,
  ) -> None:
    """
    Calls Qt's 'void QSpacerItem::changeSize(int w, int h,
    QSizePolicy::Policy hData, QSizePolicy::Policy vData)'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#changeSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    hData : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicyPolicy.Minimum.

    vData : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicyPolicy.Minimum.
    """
    #  void QSpacerItem::changeSize(int w, int h, QSizePolicy::Policy hData,
    #      QSizePolicy::Policy vData)
    self.uglySide.call(
        'ritual_ZN11QSpacerItem10changeSizeEiiN11QSizePolicy6PolicyES1_',
        w, h, hData.value, vData.value,
    )

  def spacerItem(self) -> Optional[QSpacerItem]:
    """
    Calls Qt's 'QSpacerItem *QSpacerItem::spacerItem()'.

    Qt's own words: https://doc.qt.io/qt-6/qspaceritem.html#spacerItem

    Returns
    -------

    Optional[QSpacerItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpacerItem *QSpacerItem::spacerItem()
    address = self.uglySide.call('ritual_ZN11QSpacerItem10spacerItemEv')
    return QSpacerItem._cuteAt(address)
