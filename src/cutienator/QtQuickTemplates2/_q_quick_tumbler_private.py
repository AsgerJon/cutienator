"""
QQuickTumblerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTumblerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QQml
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QPalette
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickTumbler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickTumbler = WAIT['QQuickTumbler']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTumblerPrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickTumblerPrivate: a plain Python object standing
  in front of one C++ QQuickTumblerPrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickTumblerPrivate is built on Qt's QQuickControlPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTumblerPrivate that has a ritual and that
  Python can call so far, 29 names in all: 'q_func', 'determineViewType',
  'resetViewData', 'viewContentItemChildItems', 'get', 'defaultPalette',
  '_q_updateItemHeights', '_q_updateItemWidths',
  '_q_onViewCurrentIndexChanged', '_q_onViewCountChanged',
  '_q_onViewOffsetChanged', '_q_onViewContentYChanged',
  'calculateDisplacements', 'disconnectFromView', 'setupViewData',
  'warnAboutIncorrectContentItem', 'syncCurrentIndex',
  'setPendingCurrentIndex', 'propertyChangeReasonToString',
  'setCurrentIndex', 'setCount', 'setWrapBasedOnCount', 'setWrap',
  'effectiveFlickDeceleration', 'beginSetModel', 'endSetModel',
  'itemChildAdded', 'itemChildRemoved', 'itemGeometryChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTumbler *QQuickTumblerPrivate::q_func() const': takes
    in Python what 'QQuickTumbler *QQuickTumblerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickTumblerPrivate is created at the first use, not by
    'QQuickTumblerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTumblerPrivate.
  """

  #  The enums Qt writes inside QQuickTumblerPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ContentItemType(CuteNum):
    """
    The enum 'QQuickTumblerPrivate::ContentItemType' of Qt, with the 4 names
    Qt gives in it.
    """

    NoContentItem = Kee[int](0)
    UnsupportedContentItemType = Kee[int](1)
    PathViewContentItem = Kee[int](2)
    ListViewContentItem = Kee[int](3)

  class PropertyChangeReason(CuteNum):
    """
    The enum 'QQuickTumblerPrivate::PropertyChangeReason' of Qt, with the 2
    names Qt gives in it.
    """

    UserChange = Kee[int](0)
    InternalChange = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTumbler)
  @overload(NoneType)
  def get(
      tumbler: Optional[QQuickTumbler],
  ) -> Optional[QQuickTumblerPrivate]:
    """
    Calls Qt's 'QQuickTumblerPrivate *QQuickTumblerPrivate::get(QQuickTumbler
    *tumbler)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerprivate.html#get

    Parameters
    ----------

    tumbler : Optional[QQuickTumbler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTumblerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumblerPrivate *QQuickTumblerPrivate::get(QQuickTumbler
    #      *tumbler)
    address = Rituals.call(
        'ritual_ZN20QQuickTumblerPrivate3getEP13QQuickTumbler',
        CuteMixin._addressOf(tumbler),
    )
    return QQuickTumblerPrivate._cuteAt(address)

  @staticmethod
  @overload(PropertyChangeReason)
  def propertyChangeReasonToString(
      changeReason: PropertyChangeReason,
  ) -> str:
    """
    Calls Qt's 'QString
    QQuickTumblerPrivate::propertyChangeReasonToString(PropertyChangeReason
    changeReason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html

    Parameters
    ----------

    changeReason : PropertyChangeReason
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTumblerPrivate::propertyChangeReasonToString(
    #      PropertyChangeReason changeReason)
    return Rituals.call(
        'ritual_ZN20QQuickTumblerPrivate28propertyChangeReasonToStringENS_2'
        '0PropertyChangeReasonE',
        changeReason.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTumblerPrivate'

  #  A C++ QQuickTumblerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTumblerPrivate'

  #  The functions Qt calls itself that QQuickTumblerPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemChildAdded': (
          ('_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemChildRemoved': (
          ('_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  def viewContentItemChildItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *>
    QQuickTumblerPrivate::viewContentItemChildItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QQuickTumblerPrivate::viewContentItemChildItems()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTumblerPrivate25viewContentItemChildItemsEv',
    )
    from ..QtQuick import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickTumblerPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickTumblerPrivate::defaultPalette() const
    ritual = 'ritual_ZNK20QQuickTumblerPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickTumblerPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def effectiveFlickDeceleration(self) -> float:
    """
    Calls Qt's 'qreal QQuickTumblerPrivate::effectiveFlickDeceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html
    """
    #  qreal QQuickTumblerPrivate::effectiveFlickDeceleration() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickTumblerPrivate26effectiveFlickDecelerationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPendingCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setPendingCurrentIndex(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#setPendingCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickTumblerPrivate::setPendingCurrentIndex(int index)
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate22setPendingCurrentIndexEi', index,
    )

  @overload(int)
  @overload(int, PropertyChangeReason)
  def setCurrentIndex(
      self,
      newCurrentIndex: int,
      changeReason: PropertyChangeReason = (
          PropertyChangeReason.InternalChange),
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setCurrentIndex(int
    newCurrentIndex, PropertyChangeReason changeReason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#setCurrentIndex

    Parameters
    ----------

    newCurrentIndex : int
      Passed on as it is.

    changeReason : PropertyChangeReason
      Passed on as its number. May be left out, as in Qt: it is then
      PropertyChangeReason.InternalChange.
    """
    #  void QQuickTumblerPrivate::setCurrentIndex(int newCurrentIndex,
    #      PropertyChangeReason changeReason)
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate15setCurrentIndexEiNS_20PropertyCha'
        'ngeReasonE',
        newCurrentIndex, changeReason.value,
    )

  @overload(int)
  def setCount(self, newCount: int) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setCount(int newCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerprivate.html#setCount

    Parameters
    ----------

    newCount : int
      Passed on as it is.
    """
    #  void QQuickTumblerPrivate::setCount(int newCount)
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate8setCountEi', newCount,
    )

  def setWrapBasedOnCount(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setWrapBasedOnCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#setWrapBasedOnCount
    """
    #  void QQuickTumblerPrivate::setWrapBasedOnCount()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate19setWrapBasedOnCountEv',
    )

  @overload(bool, QQml.PropertyUtils.State)
  def setWrap(
      self,
      shouldWrap: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setWrap(bool shouldWrap,
    QQml::PropertyUtils::State propertyState)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerprivate.html#setWrap

    Parameters
    ----------

    shouldWrap : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickTumblerPrivate::setWrap(bool shouldWrap,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate7setWrapEbN4QQml13PropertyUtils5Sta'
        'teE',
        shouldWrap, propertyState.value,
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

  def q_func(self) -> Optional[QQuickTumbler]:
    """
    Calls Qt's 'QQuickTumbler *QQuickTumblerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumblerprivate.html#q_func

    Returns
    -------

    Optional[QQuickTumbler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumbler *QQuickTumblerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickTumblerPrivate6q_funcEv')
    from . import QQuickTumbler
    return QQuickTumbler._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def determineViewType(
      self,
      contentItem: Optional[QQuickItem],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickTumblerPrivate::determineViewType(QQuickItem *contentItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#determineViewType

    Parameters
    ----------

    contentItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTumblerPrivate::determineViewType(QQuickItem
    #      *contentItem)
    address = self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate17determineViewTypeEP10QQuickItem',
        self._addressOf(contentItem),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def resetViewData(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::resetViewData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#resetViewData
    """
    #  void QQuickTumblerPrivate::resetViewData()
    self.uglySide.call('ritual_ZN20QQuickTumblerPrivate13resetViewDataEv')

  def _q_updateItemHeights(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_updateItemHeights()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#_q_updateItemHeights
    """
    #  void QQuickTumblerPrivate::_q_updateItemHeights()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate20_q_updateItemHeightsEv',
    )

  def _q_updateItemWidths(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_updateItemWidths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#_q_updateItemWidths
    """
    #  void QQuickTumblerPrivate::_q_updateItemWidths()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate19_q_updateItemWidthsEv',
    )

  def _q_onViewCurrentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_onViewCurrentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html
    """
    #  void QQuickTumblerPrivate::_q_onViewCurrentIndexChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate28_q_onViewCurrentIndexChangedEv',
    )

  def _q_onViewCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_onViewCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#_q_onViewCountChanged
    """
    #  void QQuickTumblerPrivate::_q_onViewCountChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate21_q_onViewCountChangedEv',
    )

  def _q_onViewOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_onViewOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#_q_onViewOffsetChanged
    """
    #  void QQuickTumblerPrivate::_q_onViewOffsetChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate22_q_onViewOffsetChangedEv',
    )

  def _q_onViewContentYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::_q_onViewContentYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#_q_onViewContentYChanged
    """
    #  void QQuickTumblerPrivate::_q_onViewContentYChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate24_q_onViewContentYChangedEv',
    )

  def calculateDisplacements(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::calculateDisplacements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#calculateDisplacements
    """
    #  void QQuickTumblerPrivate::calculateDisplacements()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate22calculateDisplacementsEv',
    )

  def disconnectFromView(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::disconnectFromView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#disconnectFromView
    """
    #  void QQuickTumblerPrivate::disconnectFromView()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate18disconnectFromViewEv',
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setupViewData(
      self,
      newControlContentItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::setupViewData(QQuickItem
    *newControlContentItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#setupViewData

    Parameters
    ----------

    newControlContentItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerPrivate::setupViewData(QQuickItem
    #      *newControlContentItem)
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate13setupViewDataEP10QQuickItem',
        self._addressOf(newControlContentItem),
    )

  def warnAboutIncorrectContentItem(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::warnAboutIncorrectContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html
    """
    #  void QQuickTumblerPrivate::warnAboutIncorrectContentItem()
    self.uglySide.call(
        'ritual_ZN20QQuickTumblerPrivate29warnAboutIncorrectContentItemEv',
    )

  def syncCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::syncCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#syncCurrentIndex
    """
    #  void QQuickTumblerPrivate::syncCurrentIndex()
    self.uglySide.call('ritual_ZN20QQuickTumblerPrivate16syncCurrentIndexEv')

  def beginSetModel(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::beginSetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#beginSetModel
    """
    #  void QQuickTumblerPrivate::beginSetModel()
    self.uglySide.call('ritual_ZN20QQuickTumblerPrivate13beginSetModelEv')

  def endSetModel(self) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::endSetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#endSetModel
    """
    #  void QQuickTumblerPrivate::endSetModel()
    self.uglySide.call('ritual_ZN20QQuickTumblerPrivate11endSetModelEv')

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildAdded(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::itemChildAdded(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#itemChildAdded

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerPrivate::itemChildAdded(QQuickItem *a0, QQuickItem
    #      *a1)
    ritual = (
        'ritual_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickTumblerPrivate14itemChildAddedEP10QQuickIte'
          'mS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildRemoved(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::itemChildRemoved(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#itemChildRemoved

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumblerPrivate::itemChildRemoved(QQuickItem *a0, QQuickItem
    #      *a1)
    ritual = (
        'ritual_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickTumblerPrivate16itemChildRemovedEP10QQuickI'
          'temS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickTumblerPrivate::itemGeometryChanged(QQuickItem
    *a0, QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumblerprivate.html#itemGeometryChanged

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
    #  void QQuickTumblerPrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN20QQuickTumblerPrivate19itemGeometryChangedEP10QQuickItem'
        '20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickTumblerPrivate19itemGeometryChangedEP10QQui'
          'ckItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )
