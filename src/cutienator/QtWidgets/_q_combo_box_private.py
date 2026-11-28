"""
QComboBoxPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboBoxPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QStyle, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPoint, QRect
  from ..QtGui import QIcon
  from . import QComboBox, QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBoxPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QComboBoxPrivate: a plain Python object standing in
  front of one C++ QComboBoxPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QComboBoxPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBoxPrivate that has a ritual and that Python
  can call so far, 32 names in all: 'q_func', 'init',
  'updateLineEditGeometry', 'matchFlags', 'editingFinished', 'returnPressed',
  'itemSelected', 'emitActivated', 'emitHighlighted',
  'emitCurrentIndexChanged', 'modelDestroyed', 'updateMicroFocus',
  'completerActivated', 'resetButton', 'updateIndexBeforeChange',
  'updateArrow', 'updateHoverControl', 'trySetValidIndex', 'popupGeometry',
  'newHoverControl', 'computeWidthHint', 'itemText', 'itemIcon', 'itemRole',
  'updateLayoutDirection', 'setCurrentIndex', 'initViewItemOption',
  'updateViewContainerPaletteAndOpacity', 'updateFocusPolicy', 'doHidePopup',
  'updateCurrentText', 'disconnectModel'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QComboBox *QComboBoxPrivate::q_func() const': takes in Python
    what 'QComboBox *QComboBoxPrivate::q_func()' takes.
  - Qt's 'QComboBoxPrivate::~QComboBoxPrivate()': the destructor: Python
    never removes a C++ QComboBoxPrivate.
  - Qt's 'QSize QComboBoxPrivate::recomputeSizeHint(QSize &sh) const': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  13 of the 49 functions Qt declares: 11 leans on 'QComboBoxDelegate; 2
  cannot be called and cannot be called through the meta-object and cannot be
  copied.

  What to expect
  --------------

  - The C++ QComboBoxPrivate is created at the first use, not by
    'QComboBoxPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBoxPrivate.
  - Each name of Qt's QComboBoxPrivate that has no cute function yet,
    'adjustComboBoxSize', 'complete', 'connectModel', 'contains',
    'dataChanged', 'keyboardSearchString', 'modelChanged', 'modelReset',
    'recomputeSizeHint', 'rowsInserted', 'rowsRemoved',
    'showPopupFromMouseEvent', 'updateDelegate', 'viewContainer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QComboBoxPrivate'

  #  A C++ QComboBoxPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboBoxPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def matchFlags(self) -> Qt.MatchFlags:
    """
    Calls Qt's 'Qt::MatchFlags QComboBoxPrivate::matchFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#matchFlags

    Returns
    -------

    Qt.MatchFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MatchFlags QComboBoxPrivate::matchFlags() const
    return Qt.MatchFlags(self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate10matchFlagsEv',
    ))

  @overload(QPoint)
  def popupGeometry(self, globalPos: QPoint) -> QRect:
    """
    Calls Qt's 'QRect QComboBoxPrivate::popupGeometry(const QPoint
    &globalPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#popupGeometry

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QComboBoxPrivate::popupGeometry(const QPoint &globalPos) const
    address = self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate13popupGeometryERK6QPoint',
        self._valueOf(globalPos),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def computeWidthHint(self) -> int:
    """
    Calls Qt's 'int QComboBoxPrivate::computeWidthHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#computeWidthHint
    """
    #  int QComboBoxPrivate::computeWidthHint() const
    return self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate16computeWidthHintEv',
    )

  @overload(QModelIndex)
  def itemText(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QComboBoxPrivate::itemText(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#itemText

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QComboBoxPrivate::itemText(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate8itemTextERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def itemIcon(self, index: QModelIndex) -> QIcon:
    """
    Calls Qt's 'QIcon QComboBoxPrivate::itemIcon(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#itemIcon

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QComboBoxPrivate::itemIcon(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate8itemIconERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def itemRole(self) -> int:
    """
    Calls Qt's 'int QComboBoxPrivate::itemRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#itemRole
    """
    #  int QComboBoxPrivate::itemRole() const
    return self.uglySide.call('ritual_ZNK16QComboBoxPrivate8itemRoleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def setCurrentIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::setCurrentIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#setCurrentIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::setCurrentIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate15setCurrentIndexERK11QModelIndex',
        self._valueOf(index),
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
    Notes what was given, for Qt's 'QComboBoxPrivate::QComboBoxPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#QComboBoxPrivate
    """
    #  QComboBoxPrivate::QComboBoxPrivate()
    self._noteCreation(QComboBoxPrivate, lambda: Rituals.call(
        'ritual_ZN16QComboBoxPrivateC1Ev',
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

  def q_func(self) -> Optional[QComboBox]:
    """
    Calls Qt's 'QComboBox *QComboBoxPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#q_func

    Returns
    -------

    Optional[QComboBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComboBox *QComboBoxPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QComboBoxPrivate6q_funcEv')
    from . import QComboBox
    return QComboBox._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#init
    """
    #  void QComboBoxPrivate::init()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate4initEv')

  def updateLineEditGeometry(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateLineEditGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateLineEditGeometry
    """
    #  void QComboBoxPrivate::updateLineEditGeometry()
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate22updateLineEditGeometryEv',
    )

  def editingFinished(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::editingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#editingFinished
    """
    #  void QComboBoxPrivate::editingFinished()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate15editingFinishedEv')

  def returnPressed(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::returnPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#returnPressed
    """
    #  void QComboBoxPrivate::returnPressed()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate13returnPressedEv')

  @overload(QModelIndex)
  def itemSelected(self, item: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::itemSelected(const QModelIndex
    &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#itemSelected

    Parameters
    ----------

    item : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::itemSelected(const QModelIndex &item)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate12itemSelectedERK11QModelIndex',
        self._valueOf(item),
    )

  @overload(QModelIndex)
  def emitActivated(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::emitActivated(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#emitActivated

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::emitActivated(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate13emitActivatedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def emitHighlighted(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::emitHighlighted(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#emitHighlighted

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::emitHighlighted(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate15emitHighlightedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def emitCurrentIndexChanged(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::emitCurrentIndexChanged(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#emitCurrentIndexChanged

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::emitCurrentIndexChanged(const QModelIndex
    #      &index)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate23emitCurrentIndexChangedERK11QModelInd'
        'ex',
        self._valueOf(index),
    )

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#modelDestroyed
    """
    #  void QComboBoxPrivate::modelDestroyed()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate14modelDestroyedEv')

  def updateMicroFocus(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateMicroFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateMicroFocus
    """
    #  void QComboBoxPrivate::updateMicroFocus()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate16updateMicroFocusEv')

  @overload(QModelIndex)
  def completerActivated(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::completerActivated(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#completerActivated

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxPrivate::completerActivated(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate18completerActivatedERK11QModelIndex',
        self._valueOf(index),
    )

  def resetButton(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::resetButton()'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#resetButton
    """
    #  void QComboBoxPrivate::resetButton()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate11resetButtonEv')

  def updateIndexBeforeChange(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateIndexBeforeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateIndexBeforeChange
    """
    #  void QComboBoxPrivate::updateIndexBeforeChange()
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate23updateIndexBeforeChangeEv',
    )

  @overload(QStyle.StateFlag)
  def updateArrow(self, state: QStyle.StateFlag) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateArrow(QStyle::StateFlag state)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#updateArrow

    Parameters
    ----------

    state : QStyle.StateFlag
      Passed on as its number.
    """
    #  void QComboBoxPrivate::updateArrow(QStyle::StateFlag state)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate11updateArrowEN6QStyle9StateFlagE',
        state.value,
    )

  @overload(QPoint)
  def updateHoverControl(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QComboBoxPrivate::updateHoverControl(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QComboBoxPrivate::updateHoverControl(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate18updateHoverControlERK6QPoint',
        self._valueOf(pos),
    )

  def trySetValidIndex(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::trySetValidIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#trySetValidIndex
    """
    #  void QComboBoxPrivate::trySetValidIndex()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate16trySetValidIndexEv')

  @overload(QPoint)
  def newHoverControl(self, pos: QPoint) -> QStyle.SubControl:
    """
    Calls Qt's 'QStyle::SubControl QComboBoxPrivate::newHoverControl(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#newHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  QStyle::SubControl QComboBoxPrivate::newHoverControl(const QPoint
    #      &pos)
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate15newHoverControlERK6QPoint',
        self._valueOf(pos),
    ))

  def updateLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateLayoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateLayoutDirection
    """
    #  void QComboBoxPrivate::updateLayoutDirection()
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate21updateLayoutDirectionEv',
    )

  @overload(QStyleOptionViewItem)
  @overload(NoneType)
  def initViewItemOption(
      self,
      option: Optional[QStyleOptionViewItem],
  ) -> None:
    """
    Calls Qt's 'void
    QComboBoxPrivate::initViewItemOption(QStyleOptionViewItem *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#initViewItemOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivate::initViewItemOption(QStyleOptionViewItem
    #      *option) const
    self.uglySide.call(
        'ritual_ZNK16QComboBoxPrivate18initViewItemOptionEP20QStyleOptionVi'
        'ewItem',
        self._addressOf(option),
    )

  def updateViewContainerPaletteAndOpacity(self) -> None:
    """
    Calls Qt's 'void
    QComboBoxPrivate::updateViewContainerPaletteAndOpacity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html
    """
    #  void QComboBoxPrivate::updateViewContainerPaletteAndOpacity()
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate36updateViewContainerPaletteAndOpacityE'
        'v',
    )

  def updateFocusPolicy(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateFocusPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateFocusPolicy
    """
    #  void QComboBoxPrivate::updateFocusPolicy()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate17updateFocusPolicyEv')

  def doHidePopup(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::doHidePopup()'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxprivate.html#doHidePopup
    """
    #  void QComboBoxPrivate::doHidePopup()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate11doHidePopupEv')

  @overload(str)
  def updateCurrentText(self, text: str) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::updateCurrentText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#updateCurrentText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QComboBoxPrivate::updateCurrentText(const QString &text)
    self.uglySide.call(
        'ritual_ZN16QComboBoxPrivate17updateCurrentTextERK7QString', text,
    )

  def disconnectModel(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivate::disconnectModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivate.html#disconnectModel
    """
    #  void QComboBoxPrivate::disconnectModel()
    self.uglySide.call('ritual_ZN16QComboBoxPrivate15disconnectModelEv')

  @staticmethod
  def adjustComboBoxSize(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::adjustComboBoxSize()': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.adjustComboBoxSize' has no cute function yet. "
        "Qt's 'void QComboBoxPrivate::adjustComboBoxSize()': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def complete(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::complete()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.complete' has no cute function yet. Qt's 'void "
        "QComboBoxPrivate::complete()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def connectModel(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::connectModel()': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.connectModel' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::connectModel()': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def contains(*__, **_) -> Never:
    """
    Qt's 'bool QComboBoxPrivate::contains(const QString &text, int role)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.contains' has no cute function yet. Qt's 'bool "
        "QComboBoxPrivate::contains(const QString &text, int role)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight)': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.dataChanged' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::dataChanged(const QModelIndex &topLeft, "
        "const QModelIndex &bottomRight)': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def keyboardSearchString(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::keyboardSearchString(const QString &text)':
    leans on 'QComboBoxDelegate::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.keyboardSearchString' has no cute function yet. "
        "Qt's 'void QComboBoxPrivate::keyboardSearchString(const QString "
        "&text)': leans on 'QComboBoxDelegate::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def modelChanged(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::modelChanged()': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.modelChanged' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::modelChanged()': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def modelReset(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::modelReset()': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.modelReset' has no cute function yet. Qt's 'void "
        "QComboBoxPrivate::modelReset()': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def recomputeSizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QComboBoxPrivate::recomputeSizeHint(QSize &sh) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.recomputeSizeHint' has no cute function yet. "
        "Qt's 'QSize QComboBoxPrivate::recomputeSizeHint(QSize &sh) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def rowsInserted(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::rowsInserted(const QModelIndex &parent, int
    start, int end)': leans on 'QComboBoxDelegate::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.rowsInserted' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::rowsInserted(const QModelIndex &parent, "
        "int start, int end)': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def rowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::rowsRemoved(const QModelIndex &parent, int
    start, int end)': leans on 'QComboBoxDelegate::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.rowsRemoved' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::rowsRemoved(const QModelIndex &parent, int "
        "start, int end)': leans on 'QComboBoxDelegate::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def showPopupFromMouseEvent(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::showPopupFromMouseEvent(QMouseEvent *e)':
    leans on 'QComboBoxDelegate::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.showPopupFromMouseEvent' has no cute function "
        "yet. Qt's 'void "
        "QComboBoxPrivate::showPopupFromMouseEvent(QMouseEvent *e)': leans "
        "on 'QComboBoxDelegate::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateDelegate(*__, **_) -> Never:
    """
    Qt's 'void QComboBoxPrivate::updateDelegate(bool force)': leans on
    'QComboBoxDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.updateDelegate' has no cute function yet. Qt's "
        "'void QComboBoxPrivate::updateDelegate(bool force)': leans on "
        "'QComboBoxDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def viewContainer(*__, **_) -> Never:
    """
    Qt's 'QComboBoxPrivateContainer *QComboBoxPrivate::viewContainer()':
    leans on 'QComboBoxDelegate::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivate.viewContainer' has no cute function yet. Qt's "
        "'QComboBoxPrivateContainer *QComboBoxPrivate::viewContainer()': "
        "leans on 'QComboBoxDelegate::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
