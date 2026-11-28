"""
QQuickGridLayoutBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickGridLayoutBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickLayout
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QQuickGridLayoutBasePrivate
  from ..QtGui import QGridLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGridLayoutItem = WAIT['QGridLayoutItem']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridLayoutBase(QQuickLayout):
  """
  The cute side of Qt's QQuickGridLayoutBase: a plain Python object standing
  in front of one C++ QQuickGridLayoutBase.

  It is built on the cute 'QQuickLayout', as Qt's QQuickGridLayoutBase is
  built on Qt's QQuickLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGridLayoutBase that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr',
  'componentComplete', 'invalidate', 'orientation', 'setOrientation',
  'sizeHint', 'layoutDirection', 'setLayoutDirection',
  'effectiveLayoutDirection', 'setAlignment', 'setStretchFactor',
  'itemDestroyed', 'itemVisibilityChanged', 'updateLayoutItems', 'itemAt',
  'itemCount', 'rearrange', 'insertLayoutItems', 'layoutDirectionChanged',
  'removeGridItem', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGridLayoutBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGridLayoutBase::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGridLayoutBase::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's
    'QQuickGridLayoutBase::QQuickGridLayoutBase(QQuickGridLayoutBasePrivate
    &dd, Qt::Orientation orientation, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQuickGridLayoutBase::~QQuickGridLayoutBase()': the destructor:
    Python never removes a C++ QQuickGridLayoutBase.
  - Qt's 'const QQuickGridLayoutBasePrivate *QQuickGridLayoutBase::d_func()
    const': takes in Python what 'QQuickGridLayoutBasePrivate
    *QQuickGridLayoutBase::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGridLayoutBase is created at the first use, not by
    'QQuickGridLayoutBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGridLayoutBase.
  - Qt tells when it has removed the C++ QQuickGridLayoutBase. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickGridLayoutBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutbase.html#tr

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
    #  QString QQuickGridLayoutBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickGridLayoutBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridLayoutBase'

  #  A C++ QQuickGridLayoutBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGridLayoutBase'

  #  The functions Qt calls itself that QQuickGridLayoutBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insertLayoutItems': (
          ('_ZN20QQuickGridLayoutBase17insertLayoutItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGridLayoutBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGridLayoutBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickGridLayoutBase::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickGridLayoutBase::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutBase11orientationEv',
    ))

  @overload(Qt.SizeHint)
  def sizeHint(self, whichSizeHint: Qt.SizeHint) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGridLayoutBase::sizeHint(Qt::SizeHint
    whichSizeHint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutbase.html#sizeHint

    Parameters
    ----------

    whichSizeHint : Qt.SizeHint
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickGridLayoutBase::sizeHint(Qt::SizeHint whichSizeHint)
    #      const
    ritual = 'ritual_ZNK20QQuickGridLayoutBase8sizeHintEN2Qt8SizeHintE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickGridLayoutBase8sizeHintEN2Qt8SizeHintE'
    address = self.uglySide.call(ritual, whichSizeHint.value)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickGridLayoutBase::layoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickGridLayoutBase::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutBase15layoutDirectionEv',
    ))

  def effectiveLayoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QQuickGridLayoutBase::effectiveLayoutDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#effectiveLayoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickGridLayoutBase::effectiveLayoutDirection()
    #      const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutBase24effectiveLayoutDirectionEv',
    ))

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickGridLayoutBase::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutbase.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickGridLayoutBase::itemAt(int index) const
    ritual = 'ritual_ZNK20QQuickGridLayoutBase6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickGridLayoutBase6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QQuickItem._cuteAt(address)

  def itemCount(self) -> int:
    """
    Calls Qt's 'int QQuickGridLayoutBase::itemCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#itemCount
    """
    #  int QQuickGridLayoutBase::itemCount() const
    ritual = 'ritual_ZNK20QQuickGridLayoutBase9itemCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickGridLayoutBase9itemCountEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickGridLayoutBase::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN20QQuickGridLayoutBase14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, dir: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QQuickGridLayoutBase::setLayoutDirection(Qt::LayoutDirection dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#setLayoutDirection

    Parameters
    ----------

    dir : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickGridLayoutBase::setLayoutDirection(Qt::LayoutDirection dir)
    self.uglySide.call(
        'ritual_ZN20QQuickGridLayoutBase18setLayoutDirectionEN2Qt15LayoutDi'
        'rectionE',
        dir.value,
    )

  @overload(QQuickItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      item: Optional[QQuickItem],
      align: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::setAlignment(QQuickItem *item,
    Qt::Alignment align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#setAlignment

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    align : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickGridLayoutBase::setAlignment(QQuickItem *item,
    #      Qt::Alignment align)
    ritual = (
        'ritual_ZN20QQuickGridLayoutBase12setAlignmentEP10QQuickItem6QFlags'
        'IN2Qt13AlignmentFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGridLayoutBase12setAlignmentEP10QQuickItem6'
          'QFlagsIN2Qt13AlignmentFlagEE')
    self.uglySide.call(ritual, self._addressOf(item), align.value)

  @overload(QQuickItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      item: Optional[QQuickItem],
      stretchFactor: int,
      orient: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::setStretchFactor(QQuickItem *item,
    int stretchFactor, Qt::Orientation orient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#setStretchFactor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretchFactor : int
      Passed on as it is.

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickGridLayoutBase::setStretchFactor(QQuickItem *item, int
    #      stretchFactor, Qt::Orientation orient)
    ritual = (
        'ritual_ZN20QQuickGridLayoutBase16setStretchFactorEP10QQuickItemiN2'
        'Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGridLayoutBase16setStretchFactorEP10QQuickI'
          'temiN2Qt11OrientationE')
    self.uglySide.call(
        ritual, self._addressOf(item), stretchFactor, orient.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGridLayoutBase::QQuickGridLayoutBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#QQuickGridLayoutBase
    """
    #  QQuickGridLayoutBase::QQuickGridLayoutBase()
    self._noteCreation(QQuickGridLayoutBase, lambda: Rituals.call(
        'ritual_ZN20QQuickGridLayoutBaseC1Ev',
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#componentComplete
    """
    #  void QQuickGridLayoutBase::componentComplete()
    ritual = 'ritual_ZN20QQuickGridLayoutBase17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGridLayoutBase17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def invalidate(self, childItem: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::invalidate(QQuickItem
    *childItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#invalidate

    Parameters
    ----------

    childItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickGridLayoutBase::invalidate(QQuickItem *childItem)
    ritual = 'ritual_ZN20QQuickGridLayoutBase10invalidateEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGridLayoutBase10invalidateEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(childItem))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridLayoutBase::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN20QQuickGridLayoutBase13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGridLayoutBase13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::itemVisibilityChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#itemVisibilityChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridLayoutBase::itemVisibilityChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickGridLayoutBase21itemVisibilityChangedEP10QQuickIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGridLayoutBase21itemVisibilityChangedEP10QQ'
          'uickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def updateLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::updateLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#updateLayoutItems
    """
    #  void QQuickGridLayoutBase::updateLayoutItems()
    ritual = 'ritual_ZN20QQuickGridLayoutBase17updateLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGridLayoutBase17updateLayoutItemsEv'
    self.uglySide.call(ritual)

  @overload(QSizeF)
  def rearrange(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::rearrange(const QSizeF &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#rearrange

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGridLayoutBase::rearrange(const QSizeF &size)
    ritual = 'ritual_ZN20QQuickGridLayoutBase9rearrangeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGridLayoutBase9rearrangeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(size))

  def insertLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::insertLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#insertLayoutItems
    """
    #  void QQuickGridLayoutBase::insertLayoutItems()
    ritual = 'ritual_ZN20QQuickGridLayoutBase17insertLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGridLayoutBase17insertLayoutItemsEv'
    self.uglySide.call(ritual)

  def layoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::layoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#layoutDirectionChanged
    """
    #  void QQuickGridLayoutBase::layoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickGridLayoutBase22layoutDirectionChangedEv',
    )

  @overload(QGridLayoutItem)
  @overload(NoneType)
  def removeGridItem(self, gridItem: Optional[QGridLayoutItem]) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutBase::removeGridItem(QGridLayoutItem
    *gridItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutbase.html#removeGridItem

    Parameters
    ----------

    gridItem : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridLayoutBase::removeGridItem(QGridLayoutItem *gridItem)
    self.uglySide.call(
        'ritual_ZN20QQuickGridLayoutBase14removeGridItemEP15QGridLayoutItem',
        self._addressOf(gridItem),
    )

  def d_func(self) -> Optional[QQuickGridLayoutBasePrivate]:
    """
    Calls Qt's 'QQuickGridLayoutBasePrivate *QQuickGridLayoutBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutbase.html#d_func

    Returns
    -------

    Optional[QQuickGridLayoutBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGridLayoutBasePrivate *QQuickGridLayoutBase::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickGridLayoutBase6d_funcEv')
    from . import QQuickGridLayoutBasePrivate
    return QQuickGridLayoutBasePrivate._cuteAt(address)
