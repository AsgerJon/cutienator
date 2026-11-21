"""
QHeaderView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qheaderview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractItemView, QHeaderViewResizeMode, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QByteArray, QMetaObject, QPoint
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QByteArray = WAIT['QByteArray']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHeaderView(QAbstractItemView):
  """
  The cute side of Qt's QHeaderView: a plain Python object standing in front
  of one C++ QHeaderView.

  It is built on the cute 'QAbstractItemView', as Qt's QHeaderView is built
  on Qt's QAbstractItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHeaderView that has a ritual and that Python can
  call so far, 69 names in all: 'metaObject', 'tr', 'setModel',
  'orientation', 'offset', 'length', 'sizeHint', 'setVisible',
  'sectionSizeHint', 'visualIndexAt', 'logicalIndexAt', 'sectionSize',
  'sectionPosition', 'sectionViewportPosition', 'moveSection',
  'swapSections', 'resizeSection', 'resizeSections', 'isSectionHidden',
  'setSectionHidden', 'hiddenSectionCount', 'hideSection', 'showSection',
  'count', 'visualIndex', 'logicalIndex', 'setSectionsMovable',
  'sectionsMovable', 'setFirstSectionMovable', 'isFirstSectionMovable',
  'setSectionsClickable', 'sectionsClickable', 'setHighlightSections',
  'highlightSections', 'sectionResizeMode', 'setSectionResizeMode',
  'setResizeContentsPrecision', 'resizeContentsPrecision',
  'stretchSectionCount', 'setSortIndicatorShown', 'isSortIndicatorShown',
  'setSortIndicator', 'sortIndicatorSection', 'sortIndicatorOrder',
  'setSortIndicatorClearable', 'isSortIndicatorClearable',
  'stretchLastSection', 'setStretchLastSection', 'cascadingSectionResizes',
  'setCascadingSectionResizes', 'defaultSectionSize',
  'setDefaultSectionSize', 'resetDefaultSectionSize', 'minimumSectionSize',
  'setMinimumSectionSize', 'maximumSectionSize', 'setMaximumSectionSize',
  'defaultAlignment', 'setDefaultAlignment', 'doItemsLayout',
  'sectionsMoved', 'sectionsHidden', 'saveState', 'restoreState', 'reset',
  'setOffset', 'setOffsetToSectionPosition', 'setOffsetToLastSection',
  'headerDataChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHeaderView::~QHeaderView()': the destructor: Python never removes
    a C++ QHeaderView.

  What has no ritual
  ------------------

  53 of the 127 functions Qt declares: 33 protected; 11 a signal; 4 private;
  2 takes or gives a type that cannot be passed yet; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QHeaderView is created at the first use, not by
    'QHeaderView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeaderView.
  - Qt tells when it has removed the C++ QHeaderView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QHeaderView, and the names Qt has for the
  #  combinations of its flags enums.
  ResizeMode = QHeaderViewResizeMode

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
    Calls Qt's 'QString QHeaderView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#tr

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
    #  QString QHeaderView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QHeaderView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHeaderView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHeaderView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHeaderView::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QHeaderView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QHeaderView::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QHeaderView::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK11QHeaderView11orientationEv',
    ))

  def offset(self) -> int:
    """
    Calls Qt's 'int QHeaderView::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#offset
    """
    #  int QHeaderView::offset() const
    return self.uglySide.call('ritual_ZNK11QHeaderView6offsetEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QHeaderView::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#length
    """
    #  int QHeaderView::length() const
    return self.uglySide.call('ritual_ZNK11QHeaderView6lengthEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QHeaderView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QHeaderView::sizeHint() const
    address = self.uglySide.call('ritual_ZNK11QHeaderView8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def sectionSizeHint(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::sectionSizeHint(int logicalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionSizeHint

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::sectionSizeHint(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView15sectionSizeHintEi', logicalIndex,
    )

  @overload(int)
  def visualIndexAt(self, position: int) -> int:
    """
    Calls Qt's 'int QHeaderView::visualIndexAt(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#visualIndexAt

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QHeaderView::visualIndexAt(int position) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView13visualIndexAtEi', position,
    )

  @overload(int)
  def logicalIndexAt(self, position: int) -> int:
    """
    Calls Qt's 'int QHeaderView::logicalIndexAt(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#logicalIndexAt

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  int QHeaderView::logicalIndexAt(int position) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView14logicalIndexAtEi', position,
    )

  @overload(int, int)
  def logicalIndexAt(self, x: int, y: int) -> int:
    """
    Calls Qt's 'int QHeaderView::logicalIndexAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#logicalIndexAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  int QHeaderView::logicalIndexAt(int x, int y) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView14logicalIndexAtEii', x, y,
    )

  @overload(QPoint)
  def logicalIndexAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QHeaderView::logicalIndexAt(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#logicalIndexAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QHeaderView::logicalIndexAt(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView14logicalIndexAtERK6QPoint',
        self._valueOf(pos),
    )

  @overload(int)
  def sectionSize(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::sectionSize(int logicalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionSize

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::sectionSize(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView11sectionSizeEi', logicalIndex,
    )

  @overload(int)
  def sectionPosition(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::sectionPosition(int logicalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionPosition

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::sectionPosition(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView15sectionPositionEi', logicalIndex,
    )

  @overload(int)
  def sectionViewportPosition(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::sectionViewportPosition(int logicalIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#sectionViewportPosition

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::sectionViewportPosition(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView23sectionViewportPositionEi', logicalIndex,
    )

  @overload(int)
  def isSectionHidden(self, logicalIndex: int) -> bool:
    """
    Calls Qt's 'bool QHeaderView::isSectionHidden(int logicalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#isSectionHidden

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  bool QHeaderView::isSectionHidden(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView15isSectionHiddenEi', logicalIndex,
    )

  def hiddenSectionCount(self) -> int:
    """
    Calls Qt's 'int QHeaderView::hiddenSectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#hiddenSectionCount
    """
    #  int QHeaderView::hiddenSectionCount() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView18hiddenSectionCountEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QHeaderView::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#count
    """
    #  int QHeaderView::count() const
    return self.uglySide.call('ritual_ZNK11QHeaderView5countEv')

  @overload(int)
  def visualIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::visualIndex(int logicalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#visualIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::visualIndex(int logicalIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView11visualIndexEi', logicalIndex,
    )

  @overload(int)
  def logicalIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QHeaderView::logicalIndex(int visualIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#logicalIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QHeaderView::logicalIndex(int visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView12logicalIndexEi', visualIndex,
    )

  def sectionsMovable(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::sectionsMovable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionsMovable
    """
    #  bool QHeaderView::sectionsMovable() const
    return self.uglySide.call('ritual_ZNK11QHeaderView15sectionsMovableEv')

  def isFirstSectionMovable(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::isFirstSectionMovable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#isFirstSectionMovable
    """
    #  bool QHeaderView::isFirstSectionMovable() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView21isFirstSectionMovableEv',
    )

  def sectionsClickable(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::sectionsClickable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionsClickable
    """
    #  bool QHeaderView::sectionsClickable() const
    return self.uglySide.call('ritual_ZNK11QHeaderView17sectionsClickableEv')

  def highlightSections(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::highlightSections() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#highlightSections
    """
    #  bool QHeaderView::highlightSections() const
    return self.uglySide.call('ritual_ZNK11QHeaderView17highlightSectionsEv')

  @overload(int)
  def sectionResizeMode(self, logicalIndex: int) -> ResizeMode:
    """
    Calls Qt's 'ResizeMode QHeaderView::sectionResizeMode(int logicalIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionResizeMode

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    Returns
    -------

    ResizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResizeMode(number)'
      gives.
    """
    #  ResizeMode QHeaderView::sectionResizeMode(int logicalIndex) const
    return QHeaderView.ResizeMode(self.uglySide.call(
        'ritual_ZNK11QHeaderView17sectionResizeModeEi', logicalIndex,
    ))

  def resizeContentsPrecision(self) -> int:
    """
    Calls Qt's 'int QHeaderView::resizeContentsPrecision() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#resizeContentsPrecision
    """
    #  int QHeaderView::resizeContentsPrecision() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView23resizeContentsPrecisionEv',
    )

  def stretchSectionCount(self) -> int:
    """
    Calls Qt's 'int QHeaderView::stretchSectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#stretchSectionCount
    """
    #  int QHeaderView::stretchSectionCount() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView19stretchSectionCountEv',
    )

  def isSortIndicatorShown(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::isSortIndicatorShown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#isSortIndicatorShown
    """
    #  bool QHeaderView::isSortIndicatorShown() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView20isSortIndicatorShownEv',
    )

  def sortIndicatorSection(self) -> int:
    """
    Calls Qt's 'int QHeaderView::sortIndicatorSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#sortIndicatorSection
    """
    #  int QHeaderView::sortIndicatorSection() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView20sortIndicatorSectionEv',
    )

  def sortIndicatorOrder(self) -> Qt.SortOrder:
    """
    Calls Qt's 'Qt::SortOrder QHeaderView::sortIndicatorOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#sortIndicatorOrder

    Returns
    -------

    Qt.SortOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.SortOrder(number)'
      gives.
    """
    #  Qt::SortOrder QHeaderView::sortIndicatorOrder() const
    return Qt.SortOrder(self.uglySide.call(
        'ritual_ZNK11QHeaderView18sortIndicatorOrderEv',
    ))

  def isSortIndicatorClearable(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::isSortIndicatorClearable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#isSortIndicatorClearable
    """
    #  bool QHeaderView::isSortIndicatorClearable() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView24isSortIndicatorClearableEv',
    )

  def stretchLastSection(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::stretchLastSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#stretchLastSection
    """
    #  bool QHeaderView::stretchLastSection() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView18stretchLastSectionEv',
    )

  def cascadingSectionResizes(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::cascadingSectionResizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#cascadingSectionResizes
    """
    #  bool QHeaderView::cascadingSectionResizes() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView23cascadingSectionResizesEv',
    )

  def defaultSectionSize(self) -> int:
    """
    Calls Qt's 'int QHeaderView::defaultSectionSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#defaultSectionSize
    """
    #  int QHeaderView::defaultSectionSize() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView18defaultSectionSizeEv',
    )

  def minimumSectionSize(self) -> int:
    """
    Calls Qt's 'int QHeaderView::minimumSectionSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#minimumSectionSize
    """
    #  int QHeaderView::minimumSectionSize() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView18minimumSectionSizeEv',
    )

  def maximumSectionSize(self) -> int:
    """
    Calls Qt's 'int QHeaderView::maximumSectionSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#maximumSectionSize
    """
    #  int QHeaderView::maximumSectionSize() const
    return self.uglySide.call(
        'ritual_ZNK11QHeaderView18maximumSectionSizeEv',
    )

  def defaultAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QHeaderView::defaultAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#defaultAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QHeaderView::defaultAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QHeaderView16defaultAlignmentEv',
    ))

  def sectionsMoved(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::sectionsMoved() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionsMoved
    """
    #  bool QHeaderView::sectionsMoved() const
    return self.uglySide.call('ritual_ZNK11QHeaderView13sectionsMovedEv')

  def sectionsHidden(self) -> bool:
    """
    Calls Qt's 'bool QHeaderView::sectionsHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#sectionsHidden
    """
    #  bool QHeaderView::sectionsHidden() const
    return self.uglySide.call('ritual_ZNK11QHeaderView14sectionsHiddenEv')

  def saveState(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHeaderView::saveState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#saveState

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHeaderView::saveState() const
    address = self.uglySide.call('ritual_ZNK11QHeaderView9saveStateEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QHeaderView::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHeaderView::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN11QHeaderView8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(bool)
  def setVisible(self, v: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setVisible(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#setVisible

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QHeaderView::setVisible(bool v)
    self.uglySide.call('ritual_ZN11QHeaderView10setVisibleEb', v)

  @overload(int, bool)
  def setSectionHidden(self, logicalIndex: int, hide: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setSectionHidden(int logicalIndex, bool
    hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#setSectionHidden

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    hide : bool
      Passed on as it is.
    """
    #  void QHeaderView::setSectionHidden(int logicalIndex, bool hide)
    self.uglySide.call(
        'ritual_ZN11QHeaderView16setSectionHiddenEib', logicalIndex, hide,
    )

  @overload(bool)
  def setSectionsMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setSectionsMovable(bool movable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSectionsMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QHeaderView::setSectionsMovable(bool movable)
    self.uglySide.call(
        'ritual_ZN11QHeaderView18setSectionsMovableEb', movable,
    )

  @overload(bool)
  def setFirstSectionMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setFirstSectionMovable(bool movable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setFirstSectionMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QHeaderView::setFirstSectionMovable(bool movable)
    self.uglySide.call(
        'ritual_ZN11QHeaderView22setFirstSectionMovableEb', movable,
    )

  @overload(bool)
  def setSectionsClickable(self, clickable: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setSectionsClickable(bool clickable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSectionsClickable

    Parameters
    ----------

    clickable : bool
      Passed on as it is.
    """
    #  void QHeaderView::setSectionsClickable(bool clickable)
    self.uglySide.call(
        'ritual_ZN11QHeaderView20setSectionsClickableEb', clickable,
    )

  @overload(bool)
  def setHighlightSections(self, highlight: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setHighlightSections(bool highlight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setHighlightSections

    Parameters
    ----------

    highlight : bool
      Passed on as it is.
    """
    #  void QHeaderView::setHighlightSections(bool highlight)
    self.uglySide.call(
        'ritual_ZN11QHeaderView20setHighlightSectionsEb', highlight,
    )

  @overload(ResizeMode)
  def setSectionResizeMode(self, mode: ResizeMode) -> None:
    """
    Calls Qt's 'void QHeaderView::setSectionResizeMode(ResizeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSectionResizeMode

    Parameters
    ----------

    mode : ResizeMode
      Passed on as its number.
    """
    #  void QHeaderView::setSectionResizeMode(ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN11QHeaderView20setSectionResizeModeENS_10ResizeModeE',
        mode.value,
    )

  @overload(int, ResizeMode)
  def setSectionResizeMode(
      self,
      logicalIndex: int,
      mode: ResizeMode,
  ) -> None:
    """
    Calls Qt's 'void QHeaderView::setSectionResizeMode(int logicalIndex,
    ResizeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSectionResizeMode

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    mode : ResizeMode
      Passed on as its number.
    """
    #  void QHeaderView::setSectionResizeMode(int logicalIndex, ResizeMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN11QHeaderView20setSectionResizeModeEiNS_10ResizeModeE',
        logicalIndex, mode.value,
    )

  @overload(int)
  def setResizeContentsPrecision(self, precision: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setResizeContentsPrecision(int precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setResizeContentsPrecision

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QHeaderView::setResizeContentsPrecision(int precision)
    self.uglySide.call(
        'ritual_ZN11QHeaderView26setResizeContentsPrecisionEi', precision,
    )

  @overload(bool)
  def setSortIndicatorShown(self, show: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setSortIndicatorShown(bool show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSortIndicatorShown

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QHeaderView::setSortIndicatorShown(bool show)
    self.uglySide.call(
        'ritual_ZN11QHeaderView21setSortIndicatorShownEb', show,
    )

  @overload(int, Qt.SortOrder)
  def setSortIndicator(self, logicalIndex: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QHeaderView::setSortIndicator(int logicalIndex,
    Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#setSortIndicator

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QHeaderView::setSortIndicator(int logicalIndex, Qt::SortOrder
    #      order)
    self.uglySide.call(
        'ritual_ZN11QHeaderView16setSortIndicatorEiN2Qt9SortOrderE',
        logicalIndex, order.value,
    )

  @overload(bool)
  def setSortIndicatorClearable(self, clearable: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setSortIndicatorClearable(bool clearable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setSortIndicatorClearable

    Parameters
    ----------

    clearable : bool
      Passed on as it is.
    """
    #  void QHeaderView::setSortIndicatorClearable(bool clearable)
    self.uglySide.call(
        'ritual_ZN11QHeaderView25setSortIndicatorClearableEb', clearable,
    )

  @overload(bool)
  def setStretchLastSection(self, stretch: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setStretchLastSection(bool stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setStretchLastSection

    Parameters
    ----------

    stretch : bool
      Passed on as it is.
    """
    #  void QHeaderView::setStretchLastSection(bool stretch)
    self.uglySide.call(
        'ritual_ZN11QHeaderView21setStretchLastSectionEb', stretch,
    )

  @overload(bool)
  def setCascadingSectionResizes(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHeaderView::setCascadingSectionResizes(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setCascadingSectionResizes

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHeaderView::setCascadingSectionResizes(bool enable)
    self.uglySide.call(
        'ritual_ZN11QHeaderView26setCascadingSectionResizesEb', enable,
    )

  @overload(int)
  def setDefaultSectionSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setDefaultSectionSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setDefaultSectionSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHeaderView::setDefaultSectionSize(int size)
    self.uglySide.call(
        'ritual_ZN11QHeaderView21setDefaultSectionSizeEi', size,
    )

  @overload(int)
  def setMinimumSectionSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setMinimumSectionSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setMinimumSectionSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHeaderView::setMinimumSectionSize(int size)
    self.uglySide.call(
        'ritual_ZN11QHeaderView21setMinimumSectionSizeEi', size,
    )

  @overload(int)
  def setMaximumSectionSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setMaximumSectionSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setMaximumSectionSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHeaderView::setMaximumSectionSize(int size)
    self.uglySide.call(
        'ritual_ZN11QHeaderView21setMaximumSectionSizeEi', size,
    )

  @overload(Qt.Alignment)
  def setDefaultAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QHeaderView::setDefaultAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setDefaultAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QHeaderView::setDefaultAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN11QHeaderView19setDefaultAlignmentE6QFlagsIN2Qt13Alignmen'
        'tFlagEE',
        alignment.value,
    )

  @overload(int)
  def setOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setOffset(int offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#setOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QHeaderView::setOffset(int offset)
    self.uglySide.call('ritual_ZN11QHeaderView9setOffsetEi', offset)

  @overload(int)
  def setOffsetToSectionPosition(self, visualIndex: int) -> None:
    """
    Calls Qt's 'void QHeaderView::setOffsetToSectionPosition(int
    visualIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setOffsetToSectionPosition

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  void QHeaderView::setOffsetToSectionPosition(int visualIndex)
    self.uglySide.call(
        'ritual_ZN11QHeaderView26setOffsetToSectionPositionEi', visualIndex,
    )

  def setOffsetToLastSection(self) -> None:
    """
    Calls Qt's 'void QHeaderView::setOffsetToLastSection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#setOffsetToLastSection
    """
    #  void QHeaderView::setOffsetToLastSection()
    self.uglySide.call('ritual_ZN11QHeaderView22setOffsetToLastSectionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHeaderView::QHeaderView(Qt::Orientation
    orientation, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#QHeaderView

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHeaderView::QHeaderView(Qt::Orientation orientation, QWidget *parent)
    self._noteCreation(QHeaderView, lambda: Rituals.call(
        'ritual_ZN11QHeaderViewC1EN2Qt11OrientationEP7QWidget',
        orientation.value, self._addressOf(parent),
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
  def moveSection(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QHeaderView::moveSection(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#moveSection

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QHeaderView::moveSection(int from, int to)
    self.uglySide.call('ritual_ZN11QHeaderView11moveSectionEii', from_, to)

  @overload(int, int)
  def swapSections(self, first: int, second: int) -> None:
    """
    Calls Qt's 'void QHeaderView::swapSections(int first, int second)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#swapSections

    Parameters
    ----------

    first : int
      Passed on as it is.

    second : int
      Passed on as it is.
    """
    #  void QHeaderView::swapSections(int first, int second)
    self.uglySide.call(
        'ritual_ZN11QHeaderView12swapSectionsEii', first, second,
    )

  @overload(int, int)
  def resizeSection(self, logicalIndex: int, size: int) -> None:
    """
    Calls Qt's 'void QHeaderView::resizeSection(int logicalIndex, int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#resizeSection

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QHeaderView::resizeSection(int logicalIndex, int size)
    self.uglySide.call(
        'ritual_ZN11QHeaderView13resizeSectionEii', logicalIndex, size,
    )

  @overload(ResizeMode)
  def resizeSections(self, mode: ResizeMode) -> None:
    """
    Calls Qt's 'void QHeaderView::resizeSections(QHeaderView::ResizeMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#resizeSections

    Parameters
    ----------

    mode : ResizeMode
      Passed on as its number.
    """
    #  void QHeaderView::resizeSections(QHeaderView::ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN11QHeaderView14resizeSectionsENS_10ResizeModeE',
        mode.value,
    )

  @overload(int)
  def hideSection(self, logicalIndex: int) -> None:
    """
    Calls Qt's 'void QHeaderView::hideSection(int logicalIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#hideSection

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  void QHeaderView::hideSection(int logicalIndex)
    self.uglySide.call('ritual_ZN11QHeaderView11hideSectionEi', logicalIndex)

  @overload(int)
  def showSection(self, logicalIndex: int) -> None:
    """
    Calls Qt's 'void QHeaderView::showSection(int logicalIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#showSection

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  void QHeaderView::showSection(int logicalIndex)
    self.uglySide.call('ritual_ZN11QHeaderView11showSectionEi', logicalIndex)

  def resetDefaultSectionSize(self) -> None:
    """
    Calls Qt's 'void QHeaderView::resetDefaultSectionSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheaderview.html#resetDefaultSectionSize
    """
    #  void QHeaderView::resetDefaultSectionSize()
    self.uglySide.call('ritual_ZN11QHeaderView23resetDefaultSectionSizeEv')

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QHeaderView::doItemsLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#doItemsLayout
    """
    #  void QHeaderView::doItemsLayout()
    self.uglySide.call('ritual_ZN11QHeaderView13doItemsLayoutEv')

  @overload(QByteArray)
  def restoreState(self, state: QByteArray) -> bool:
    """
    Calls Qt's 'bool QHeaderView::restoreState(const QByteArray &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#restoreState

    Parameters
    ----------

    state : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QHeaderView::restoreState(const QByteArray &state)
    return self.uglySide.call(
        'ritual_ZN11QHeaderView12restoreStateERK10QByteArray',
        self._valueOf(state),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QHeaderView::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#reset
    """
    #  void QHeaderView::reset()
    self.uglySide.call('ritual_ZN11QHeaderView5resetEv')

  @overload(Qt.Orientation, int, int)
  def headerDataChanged(
      self,
      orientation: Qt.Orientation,
      logicalFirst: int,
      logicalLast: int,
  ) -> None:
    """
    Calls Qt's 'void QHeaderView::headerDataChanged(Qt::Orientation
    orientation, int logicalFirst, int logicalLast)'.

    Qt's own words: https://doc.qt.io/qt-6/qheaderview.html#headerDataChanged

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    logicalFirst : int
      Passed on as it is.

    logicalLast : int
      Passed on as it is.
    """
    #  void QHeaderView::headerDataChanged(Qt::Orientation orientation, int
    #      logicalFirst, int logicalLast)
    self.uglySide.call(
        'ritual_ZN11QHeaderView17headerDataChangedEN2Qt11OrientationEii',
        orientation.value, logicalFirst, logicalLast,
    )
