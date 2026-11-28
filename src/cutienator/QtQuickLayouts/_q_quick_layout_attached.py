"""
QQuickLayoutAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickLayoutAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF, QMetaObject, QSizeF
  from ..QtQuick import QQuickItem, QQuickItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLayoutAttached(QObject):
  """
  The cute side of Qt's QQuickLayoutAttached: a plain Python object standing
  in front of one C++ QQuickLayoutAttached.

  It is built on the cute 'QObject', as Qt's QQuickLayoutAttached is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLayoutAttached that has a ritual and that
  Python can call so far, 98 names in all: 'metaObject', 'tr',
  'minimumWidth', 'setMinimumWidth', 'isMinimumWidthSet', 'minimumHeight',
  'setMinimumHeight', 'isMinimumHeightSet', 'preferredWidth',
  'setPreferredWidth', 'isPreferredWidthSet', 'preferredHeight',
  'setPreferredHeight', 'isPreferredHeightSet', 'maximumWidth',
  'setMaximumWidth', 'isMaximumWidthSet', 'maximumHeight',
  'setMaximumHeight', 'isMaximumHeightSet', 'setMinimumImplicitSize',
  'setMaximumImplicitSize', 'fillWidth', 'setFillWidth', 'isFillWidthSet',
  'fillHeight', 'setFillHeight', 'isFillHeightSet', 'useDefaultSizePolicy',
  'setUseDefaultSizePolicy', 'row', 'setRow', 'isRowSet', 'column',
  'setColumn', 'isColumnSet', 'rowSpan', 'setRowSpan', 'columnSpan',
  'setColumnSpan', 'alignment', 'setAlignment', 'isAlignmentSet',
  'horizontalStretchFactor', 'setHorizontalStretchFactor',
  'isHorizontalStretchFactorSet', 'verticalStretchFactor',
  'setVerticalStretchFactor', 'isVerticalStretchFactorSet', 'margins',
  'setMargins', 'isMarginsSet', 'leftMargin', 'setLeftMargin',
  'resetLeftMargin', 'isLeftMarginSet', 'topMargin', 'setTopMargin',
  'resetTopMargin', 'isTopMarginSet', 'rightMargin', 'setRightMargin',
  'resetRightMargin', 'isRightMarginSet', 'bottomMargin', 'setBottomMargin',
  'resetBottomMargin', 'isBottomMarginSet', 'qMargins', 'effectiveQMargins',
  'setChangesNotificationEnabled', 'sizeHint', 'isExtentExplicitlySet',
  'itemForSizePolicy', 'minimumWidthChanged', 'minimumHeightChanged',
  'preferredWidthChanged', 'preferredHeightChanged', 'maximumWidthChanged',
  'maximumHeightChanged', 'fillWidthChanged', 'fillHeightChanged',
  'useDefaultSizePolicyChanged', 'leftMarginChanged', 'topMarginChanged',
  'rightMarginChanged', 'bottomMarginChanged', 'marginsChanged',
  'rowChanged', 'columnChanged', 'rowSpanChanged', 'columnSpanChanged',
  'alignmentChanged', 'horizontalStretchFactorChanged',
  'verticalStretchFactorChanged', 'invalidateItem', 'parentLayout', 'item'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLayoutAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickLayoutAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 103 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickLayoutAttached is created at the first use, not by
    'QQuickLayoutAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLayoutAttached.
  - Qt tells when it has removed the C++ QQuickLayoutAttached. Every call on
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
    Calls Qt's 'QString QQuickLayoutAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#tr

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
    #  QString QQuickLayoutAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickLayoutAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLayoutAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLayoutAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLayoutAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimumWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::minimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#minimumWidth
    """
    #  qreal QQuickLayoutAttached::minimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached12minimumWidthEv',
    )

  def isMinimumWidthSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isMinimumWidthSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isMinimumWidthSet
    """
    #  bool QQuickLayoutAttached::isMinimumWidthSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached17isMinimumWidthSetEv',
    )

  def minimumHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::minimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#minimumHeight
    """
    #  qreal QQuickLayoutAttached::minimumHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached13minimumHeightEv',
    )

  def isMinimumHeightSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isMinimumHeightSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isMinimumHeightSet
    """
    #  bool QQuickLayoutAttached::isMinimumHeightSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached18isMinimumHeightSetEv',
    )

  def preferredWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::preferredWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#preferredWidth
    """
    #  qreal QQuickLayoutAttached::preferredWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached14preferredWidthEv',
    )

  def isPreferredWidthSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isPreferredWidthSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isPreferredWidthSet
    """
    #  bool QQuickLayoutAttached::isPreferredWidthSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached19isPreferredWidthSetEv',
    )

  def preferredHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::preferredHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#preferredHeight
    """
    #  qreal QQuickLayoutAttached::preferredHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached15preferredHeightEv',
    )

  def isPreferredHeightSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isPreferredHeightSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isPreferredHeightSet
    """
    #  bool QQuickLayoutAttached::isPreferredHeightSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached20isPreferredHeightSetEv',
    )

  def maximumWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::maximumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#maximumWidth
    """
    #  qreal QQuickLayoutAttached::maximumWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached12maximumWidthEv',
    )

  def isMaximumWidthSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isMaximumWidthSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isMaximumWidthSet
    """
    #  bool QQuickLayoutAttached::isMaximumWidthSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached17isMaximumWidthSetEv',
    )

  def maximumHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::maximumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#maximumHeight
    """
    #  qreal QQuickLayoutAttached::maximumHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached13maximumHeightEv',
    )

  def isMaximumHeightSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isMaximumHeightSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isMaximumHeightSet
    """
    #  bool QQuickLayoutAttached::isMaximumHeightSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached18isMaximumHeightSetEv',
    )

  def fillWidth(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::fillWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#fillWidth
    """
    #  bool QQuickLayoutAttached::fillWidth() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached9fillWidthEv')

  def isFillWidthSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isFillWidthSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isFillWidthSet
    """
    #  bool QQuickLayoutAttached::isFillWidthSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached14isFillWidthSetEv',
    )

  def fillHeight(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::fillHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#fillHeight
    """
    #  bool QQuickLayoutAttached::fillHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached10fillHeightEv',
    )

  def isFillHeightSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isFillHeightSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isFillHeightSet
    """
    #  bool QQuickLayoutAttached::isFillHeightSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached15isFillHeightSetEv',
    )

  def useDefaultSizePolicy(self) -> QQuickLayout.SizePolicy:
    """
    Calls Qt's 'QQuickLayout::SizePolicy
    QQuickLayoutAttached::useDefaultSizePolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#useDefaultSizePolicy

    Returns
    -------

    QQuickLayout.SizePolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickLayout.SizePolicy(number)' gives.
    """
    #  QQuickLayout::SizePolicy QQuickLayoutAttached::useDefaultSizePolicy()
    #      const
    return QQuickLayout.SizePolicy(self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached20useDefaultSizePolicyEv',
    ))

  def row(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#row
    """
    #  int QQuickLayoutAttached::row() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached3rowEv')

  def isRowSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isRowSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#isRowSet
    """
    #  bool QQuickLayoutAttached::isRowSet() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached8isRowSetEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#column
    """
    #  int QQuickLayoutAttached::column() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached6columnEv')

  def isColumnSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isColumnSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isColumnSet
    """
    #  bool QQuickLayoutAttached::isColumnSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached11isColumnSetEv',
    )

  def rowSpan(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::rowSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#rowSpan
    """
    #  int QQuickLayoutAttached::rowSpan() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached7rowSpanEv')

  def columnSpan(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::columnSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#columnSpan
    """
    #  int QQuickLayoutAttached::columnSpan() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached10columnSpanEv',
    )

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQuickLayoutAttached::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQuickLayoutAttached::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached9alignmentEv',
    ))

  def isAlignmentSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isAlignmentSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isAlignmentSet
    """
    #  bool QQuickLayoutAttached::isAlignmentSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached14isAlignmentSetEv',
    )

  def horizontalStretchFactor(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::horizontalStretchFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#horizontalStretchFactor
    """
    #  int QQuickLayoutAttached::horizontalStretchFactor() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached23horizontalStretchFactorEv',
    )

  def isHorizontalStretchFactorSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isHorizontalStretchFactorSet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html
    """
    #  bool QQuickLayoutAttached::isHorizontalStretchFactorSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached28isHorizontalStretchFactorSetEv',
    )

  def verticalStretchFactor(self) -> int:
    """
    Calls Qt's 'int QQuickLayoutAttached::verticalStretchFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#verticalStretchFactor
    """
    #  int QQuickLayoutAttached::verticalStretchFactor() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached21verticalStretchFactorEv',
    )

  def isVerticalStretchFactorSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isVerticalStretchFactorSet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html
    """
    #  bool QQuickLayoutAttached::isVerticalStretchFactorSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached26isVerticalStretchFactorSetEv',
    )

  def margins(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#margins
    """
    #  qreal QQuickLayoutAttached::margins() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached7marginsEv')

  def isMarginsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isMarginsSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isMarginsSet
    """
    #  bool QQuickLayoutAttached::isMarginsSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached12isMarginsSetEv',
    )

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::leftMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#leftMargin
    """
    #  qreal QQuickLayoutAttached::leftMargin() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached10leftMarginEv',
    )

  def isLeftMarginSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isLeftMarginSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isLeftMarginSet
    """
    #  bool QQuickLayoutAttached::isLeftMarginSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached15isLeftMarginSetEv',
    )

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::topMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#topMargin
    """
    #  qreal QQuickLayoutAttached::topMargin() const
    return self.uglySide.call('ritual_ZNK20QQuickLayoutAttached9topMarginEv')

  def isTopMarginSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isTopMarginSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isTopMarginSet
    """
    #  bool QQuickLayoutAttached::isTopMarginSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached14isTopMarginSetEv',
    )

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::rightMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#rightMargin
    """
    #  qreal QQuickLayoutAttached::rightMargin() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached11rightMarginEv',
    )

  def isRightMarginSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isRightMarginSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isRightMarginSet
    """
    #  bool QQuickLayoutAttached::isRightMarginSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached16isRightMarginSetEv',
    )

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::bottomMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#bottomMargin
    """
    #  qreal QQuickLayoutAttached::bottomMargin() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached12bottomMarginEv',
    )

  def isBottomMarginSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::isBottomMarginSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isBottomMarginSet
    """
    #  bool QQuickLayoutAttached::isBottomMarginSet() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached17isBottomMarginSetEv',
    )

  def qMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickLayoutAttached::qMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#qMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickLayoutAttached::qMargins() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached8qMarginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def effectiveQMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickLayoutAttached::effectiveQMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#effectiveQMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickLayoutAttached::effectiveQMargins() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached17effectiveQMarginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  @overload(Qt.SizeHint, Qt.Orientation)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      orientation: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutAttached::sizeHint(Qt::SizeHint which,
    Qt::Orientation orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QQuickLayoutAttached::sizeHint(Qt::SizeHint which,
    #      Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached8sizeHintEN2Qt8SizeHintENS0_11Orie'
        'ntationE',
        which.value, orientation.value,
    )

  @overload(Qt.Orientation, Qt.SizeHint)
  def isExtentExplicitlySet(
      self,
      o: Qt.Orientation,
      whichSize: Qt.SizeHint,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickLayoutAttached::isExtentExplicitlySet(Qt::Orientation o,
    Qt::SizeHint whichSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#isExtentExplicitlySet

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.

    whichSize : Qt.SizeHint
      Passed on as its number.
    """
    #  bool QQuickLayoutAttached::isExtentExplicitlySet(Qt::Orientation o,
    #      Qt::SizeHint whichSize) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached21isExtentExplicitlySetEN2Qt11Orie'
        'ntationENS0_8SizeHintE',
        o.value, whichSize.value,
    )

  @overload(bool)
  def itemForSizePolicy(
      self,
      isFillSet: bool,
  ) -> Optional[QQuickItemPrivate]:
    """
    Calls Qt's 'QQuickItemPrivate
    *QQuickLayoutAttached::itemForSizePolicy(bool isFillSet) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#itemForSizePolicy

    Parameters
    ----------

    isFillSet : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemPrivate *QQuickLayoutAttached::itemForSizePolicy(bool
    #      isFillSet) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached17itemForSizePolicyEb', isFillSet,
    )
    from ..QtQuick import QQuickItemPrivate
    return QQuickItemPrivate._cuteAt(address)

  def parentLayout(self) -> Optional[QQuickLayout]:
    """
    Calls Qt's 'QQuickLayout *QQuickLayoutAttached::parentLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#parentLayout

    Returns
    -------

    Optional[QQuickLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLayout *QQuickLayoutAttached::parentLayout() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickLayoutAttached12parentLayoutEv',
    )
    return QQuickLayout._cuteAt(address)

  def item(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickLayoutAttached::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#item

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickLayoutAttached::item() const
    address = self.uglySide.call('ritual_ZNK20QQuickLayoutAttached4itemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMinimumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMinimumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMinimumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setMinimumWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached15setMinimumWidthEd', width,
    )

  @overload(float)
  def setMinimumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMinimumHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMinimumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setMinimumHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached16setMinimumHeightEd', height,
    )

  @overload(float)
  def setPreferredWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setPreferredWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setPreferredWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setPreferredWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached17setPreferredWidthEd', width,
    )

  @overload(float)
  def setPreferredHeight(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setPreferredHeight(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setPreferredHeight

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setPreferredHeight(qreal width)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached18setPreferredHeightEd', width,
    )

  @overload(float)
  def setMaximumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMaximumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMaximumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setMaximumWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached15setMaximumWidthEd', width,
    )

  @overload(float)
  def setMaximumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMaximumHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMaximumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setMaximumHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached16setMaximumHeightEd', height,
    )

  @overload(QSizeF)
  def setMinimumImplicitSize(self, sz: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMinimumImplicitSize(const
    QSizeF &sz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMinimumImplicitSize

    Parameters
    ----------

    sz : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickLayoutAttached::setMinimumImplicitSize(const QSizeF &sz)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached22setMinimumImplicitSizeERK6QSizeF',
        self._valueOf(sz),
    )

  @overload(QSizeF)
  def setMaximumImplicitSize(self, sz: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMaximumImplicitSize(const
    QSizeF &sz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMaximumImplicitSize

    Parameters
    ----------

    sz : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickLayoutAttached::setMaximumImplicitSize(const QSizeF &sz)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached22setMaximumImplicitSizeERK6QSizeF',
        self._valueOf(sz),
    )

  @overload(bool)
  def setFillWidth(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setFillWidth(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setFillWidth

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setFillWidth(bool fill)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached12setFillWidthEb', fill,
    )

  @overload(bool)
  def setFillHeight(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setFillHeight(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setFillHeight

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setFillHeight(bool fill)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached13setFillHeightEb', fill,
    )

  @overload(QQuickLayout.SizePolicy)
  def setUseDefaultSizePolicy(
      self,
      sizePolicy: QQuickLayout.SizePolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutAttached::setUseDefaultSizePolicy(QQuickLayout::SizePolicy
    sizePolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setUseDefaultSizePolicy

    Parameters
    ----------

    sizePolicy : QQuickLayout.SizePolicy
      Passed on as its number.
    """
    #  void QQuickLayoutAttached::setUseDefaultSizePolicy(QQuickLayout::
    #      SizePolicy sizePolicy)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached23setUseDefaultSizePolicyEN12QQuick'
        'Layout10SizePolicyE',
        sizePolicy.value,
    )

  @overload(int)
  def setRow(self, row: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutattached.html#setRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setRow(int row)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached6setRowEi', row)

  @overload(int)
  def setColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setColumn(int column)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached9setColumnEi', column)

  @overload(int)
  def setRowSpan(self, span: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setRowSpan(int span)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setRowSpan

    Parameters
    ----------

    span : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setRowSpan(int span)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached10setRowSpanEi', span)

  @overload(int)
  def setColumnSpan(self, span: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setColumnSpan(int span)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setColumnSpan

    Parameters
    ----------

    span : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setColumnSpan(int span)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached13setColumnSpanEi', span,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, align: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setAlignment(Qt::Alignment
    align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setAlignment

    Parameters
    ----------

    align : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickLayoutAttached::setAlignment(Qt::Alignment align)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached12setAlignmentE6QFlagsIN2Qt13Alignm'
        'entFlagEE',
        align.value,
    )

  @overload(int)
  def setHorizontalStretchFactor(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setHorizontalStretchFactor(int
    stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setHorizontalStretchFactor(int
    #      stretchFactor)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached26setHorizontalStretchFactorEi',
        stretchFactor,
    )

  @overload(int)
  def setVerticalStretchFactor(self, stretchFactor: int) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setVerticalStretchFactor(int
    stretchFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setVerticalStretchFactor

    Parameters
    ----------

    stretchFactor : int
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setVerticalStretchFactor(int stretchFactor)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached24setVerticalStretchFactorEi',
        stretchFactor,
    )

  @overload(float)
  def setMargins(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setMargins(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setMargins

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setMargins(qreal m)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached10setMarginsEd', m)

  @overload(float)
  def setLeftMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setLeftMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setLeftMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setLeftMargin(qreal m)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached13setLeftMarginEd', m)

  @overload(float)
  def setTopMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setTopMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setTopMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setTopMargin(qreal m)
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached12setTopMarginEd', m)

  @overload(float)
  def setRightMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setRightMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setRightMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setRightMargin(qreal m)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached14setRightMarginEd', m,
    )

  @overload(float)
  def setBottomMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::setBottomMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#setBottomMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickLayoutAttached::setBottomMargin(qreal m)
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached15setBottomMarginEd', m,
    )

  @overload(bool)
  def setChangesNotificationEnabled(self, enabled: bool) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutAttached::setChangesNotificationEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  bool QQuickLayoutAttached::setChangesNotificationEnabled(bool enabled)
    return self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached29setChangesNotificationEnabledEb',
        enabled,
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
    'QQuickLayoutAttached::QQuickLayoutAttached(QObject *object)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#QQuickLayoutAttached

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickLayoutAttached::QQuickLayoutAttached(QObject *object)
    self._noteCreation(QQuickLayoutAttached, lambda: Rituals.call(
        'ritual_ZN20QQuickLayoutAttachedC1EP7QObject',
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

  def resetLeftMargin(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::resetLeftMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#resetLeftMargin
    """
    #  void QQuickLayoutAttached::resetLeftMargin()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached15resetLeftMarginEv')

  def resetTopMargin(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::resetTopMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#resetTopMargin
    """
    #  void QQuickLayoutAttached::resetTopMargin()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached14resetTopMarginEv')

  def resetRightMargin(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::resetRightMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#resetRightMargin
    """
    #  void QQuickLayoutAttached::resetRightMargin()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached16resetRightMarginEv')

  def resetBottomMargin(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::resetBottomMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#resetBottomMargin
    """
    #  void QQuickLayoutAttached::resetBottomMargin()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached17resetBottomMarginEv',
    )

  def minimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::minimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#minimumWidthChanged
    """
    #  void QQuickLayoutAttached::minimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached19minimumWidthChangedEv',
    )

  def minimumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::minimumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#minimumHeightChanged
    """
    #  void QQuickLayoutAttached::minimumHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached20minimumHeightChangedEv',
    )

  def preferredWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::preferredWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#preferredWidthChanged
    """
    #  void QQuickLayoutAttached::preferredWidthChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached21preferredWidthChangedEv',
    )

  def preferredHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::preferredHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#preferredHeightChanged
    """
    #  void QQuickLayoutAttached::preferredHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached22preferredHeightChangedEv',
    )

  def maximumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::maximumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#maximumWidthChanged
    """
    #  void QQuickLayoutAttached::maximumWidthChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached19maximumWidthChangedEv',
    )

  def maximumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::maximumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#maximumHeightChanged
    """
    #  void QQuickLayoutAttached::maximumHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached20maximumHeightChangedEv',
    )

  def fillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::fillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#fillWidthChanged
    """
    #  void QQuickLayoutAttached::fillWidthChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached16fillWidthChangedEv')

  def fillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::fillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#fillHeightChanged
    """
    #  void QQuickLayoutAttached::fillHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached17fillHeightChangedEv',
    )

  def useDefaultSizePolicyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::useDefaultSizePolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html
    """
    #  void QQuickLayoutAttached::useDefaultSizePolicyChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached27useDefaultSizePolicyChangedEv',
    )

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::leftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#leftMarginChanged
    """
    #  void QQuickLayoutAttached::leftMarginChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached17leftMarginChangedEv',
    )

  def topMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::topMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#topMarginChanged
    """
    #  void QQuickLayoutAttached::topMarginChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached16topMarginChangedEv')

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#rightMarginChanged
    """
    #  void QQuickLayoutAttached::rightMarginChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached18rightMarginChangedEv',
    )

  def bottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::bottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#bottomMarginChanged
    """
    #  void QQuickLayoutAttached::bottomMarginChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached19bottomMarginChangedEv',
    )

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::marginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#marginsChanged
    """
    #  void QQuickLayoutAttached::marginsChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached14marginsChangedEv')

  def rowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::rowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#rowChanged
    """
    #  void QQuickLayoutAttached::rowChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached10rowChangedEv')

  def columnChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::columnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#columnChanged
    """
    #  void QQuickLayoutAttached::columnChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached13columnChangedEv')

  def rowSpanChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::rowSpanChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#rowSpanChanged
    """
    #  void QQuickLayoutAttached::rowSpanChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached14rowSpanChangedEv')

  def columnSpanChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::columnSpanChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#columnSpanChanged
    """
    #  void QQuickLayoutAttached::columnSpanChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached17columnSpanChangedEv',
    )

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#alignmentChanged
    """
    #  void QQuickLayoutAttached::alignmentChanged()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached16alignmentChangedEv')

  def horizontalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::horizontalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html
    """
    #  void QQuickLayoutAttached::horizontalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached30horizontalStretchFactorChangedEv',
    )

  def verticalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::verticalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html
    """
    #  void QQuickLayoutAttached::verticalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickLayoutAttached28verticalStretchFactorChangedEv',
    )

  def invalidateItem(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutAttached::invalidateItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutattached.html#invalidateItem
    """
    #  void QQuickLayoutAttached::invalidateItem()
    self.uglySide.call('ritual_ZN20QQuickLayoutAttached14invalidateItemEv')
