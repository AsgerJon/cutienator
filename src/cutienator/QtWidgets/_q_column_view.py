"""
QColumnView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcolumnview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QItemSelectionModel
from . import QAbstractItemView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QItemSelection, QMetaObject
  from ..QtCore import QModelIndex, QPoint, QRect, QSize
  from ..QtGui import QRegion, QResizeEvent
  from . import QColumnViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColumnView(QAbstractItemView):
  """
  The cute side of Qt's QColumnView: a plain Python object standing in front
  of one C++ QColumnView.

  It is built on the cute 'QAbstractItemView', as Qt's QColumnView is built
  on Qt's QAbstractItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QColumnView that has a ritual and that Python can
  call so far, 29 names in all: 'metaObject', 'tr', 'updatePreviewWidget',
  'indexAt', 'scrollTo', 'sizeHint', 'visualRect', 'setModel',
  'setSelectionModel', 'setRootIndex', 'selectAll', 'setResizeGripsVisible',
  'resizeGripsVisible', 'setPreviewColumnVisible', 'isPreviewColumnVisible',
  'previewWidget', 'setPreviewWidget', 'isIndexHidden', 'resizeEvent',
  'setSelection', 'visualRegionForSelection', 'horizontalOffset',
  'verticalOffset', 'rowsInserted', 'currentChanged', 'scrollContentsBy',
  'createColumn', 'initializeColumn', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QColumnView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QColumnView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QColumnView::~QColumnView()': the destructor: Python never removes
    a C++ QColumnView.
  - Qt's 'void QColumnView::setColumnWidths(const QList<int> &list)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<int> QColumnView::columnWidths() const': gives a type Python
    has no way to take yet.
  - Qt's 'QColumnView::QColumnView(QColumnViewPrivate &dd, QWidget *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QModelIndex QColumnView::moveCursor(CursorAction cursorAction,
    Qt::KeyboardModifiers modifiers)': names the enum
    'QAbstractItemView::CursorAction', whose class cannot be named here.
  - Qt's 'const QColumnViewPrivate *QColumnView::d_func() const': takes in
    Python what 'QColumnViewPrivate *QColumnView::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QColumnView is created at the first use, not by
    'QColumnView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColumnView.
  - Qt tells when it has removed the C++ QColumnView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QColumnView that has no cute function yet,
    'columnWidths', 'setColumnWidths', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QColumnView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#tr

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
    #  QString QColumnView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QColumnView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColumnView'

  #  A C++ QColumnView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QColumnView'

  #  The functions Qt calls itself that QColumnView is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'createColumn': (
          ('_ZN11QColumnView12createColumnERK11QModelIndex',
           ('address', 'address', 'QtWidgets:QAbstractItemView'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QColumnView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QColumnView::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QColumnView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPoint)
  def indexAt(self, point: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QColumnView::indexAt(const QPoint &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#indexAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QColumnView::indexAt(const QPoint &point) const
    ritual = 'ritual_ZNK11QColumnView7indexAtERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView7indexAtERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(point))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QColumnView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QColumnView::sizeHint() const
    ritual = 'ritual_ZNK11QColumnView8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QColumnView::visualRect(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#visualRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QColumnView::visualRect(const QModelIndex &index) const
    ritual = 'ritual_ZNK11QColumnView10visualRectERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView10visualRectERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def resizeGripsVisible(self) -> bool:
    """
    Calls Qt's 'bool QColumnView::resizeGripsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#resizeGripsVisible
    """
    #  bool QColumnView::resizeGripsVisible() const
    return self.uglySide.call(
        'ritual_ZNK11QColumnView18resizeGripsVisibleEv',
    )

  def isPreviewColumnVisible(self) -> bool:
    """
    Calls Qt's 'bool QColumnView::isPreviewColumnVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#isPreviewColumnVisible
    """
    #  bool QColumnView::isPreviewColumnVisible() const
    return self.uglySide.call(
        'ritual_ZNK11QColumnView22isPreviewColumnVisibleEv',
    )

  def previewWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QColumnView::previewWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#previewWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QColumnView::previewWidget() const
    address = self.uglySide.call('ritual_ZNK11QColumnView13previewWidgetEv')
    return QWidget._cuteAt(address)

  @overload(QModelIndex)
  def isIndexHidden(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QColumnView::isIndexHidden(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#isIndexHidden

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QColumnView::isIndexHidden(const QModelIndex &index) const
    ritual = 'ritual_ZNK11QColumnView13isIndexHiddenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView13isIndexHiddenERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(QItemSelection)
  def visualRegionForSelection(self, selection: QItemSelection) -> QRegion:
    """
    Calls Qt's 'QRegion QColumnView::visualRegionForSelection(const
    QItemSelection &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#visualRegionForSelection

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QColumnView::visualRegionForSelection(const QItemSelection
    #      &selection) const
    ritual = (
        'ritual_ZNK11QColumnView24visualRegionForSelectionERK14QItemSelecti'
        'on')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QColumnView24visualRegionForSelectionERK14QItemS'
          'election')
    address = self.uglySide.call(ritual, self._valueOf(selection))
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QColumnView::horizontalOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#horizontalOffset
    """
    #  int QColumnView::horizontalOffset() const
    ritual = 'ritual_ZNK11QColumnView16horizontalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView16horizontalOffsetEv'
    return self.uglySide.call(ritual)

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QColumnView::verticalOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#verticalOffset
    """
    #  int QColumnView::verticalOffset() const
    ritual = 'ritual_ZNK11QColumnView14verticalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QColumnView14verticalOffsetEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QColumnView::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnView::setModel(QAbstractItemModel *model)
    ritual = 'ritual_ZN11QColumnView8setModelEP18QAbstractItemModel'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView8setModelEP18QAbstractItemModel'
    self.uglySide.call(ritual, self._addressOf(model))

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QColumnView::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnView::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    ritual = (
        'ritual_ZN11QColumnView17setSelectionModelEP19QItemSelectionModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QColumnView17setSelectionModelEP19QItemSelectionM'
          'odel')
    self.uglySide.call(ritual, self._addressOf(selectionModel))

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QColumnView::setRootIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QColumnView::setRootIndex(const QModelIndex &index)
    ritual = 'ritual_ZN11QColumnView12setRootIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView12setRootIndexERK11QModelIndex'
    self.uglySide.call(ritual, self._valueOf(index))

  @overload(bool)
  def setResizeGripsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QColumnView::setResizeGripsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#setResizeGripsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QColumnView::setResizeGripsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN11QColumnView21setResizeGripsVisibleEb', visible,
    )

  @overload(bool)
  def setPreviewColumnVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QColumnView::setPreviewColumnVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#setPreviewColumnVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QColumnView::setPreviewColumnVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN11QColumnView23setPreviewColumnVisibleEb', visible,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setPreviewWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QColumnView::setPreviewWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#setPreviewWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnView::setPreviewWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QColumnView16setPreviewWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QRect, QItemSelectionModel.SelectionFlags)
  def setSelection(
      self,
      rect: QRect,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QColumnView::setSelection(const QRect &rect,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#setSelection

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QColumnView::setSelection(const QRect &rect,
    #      QItemSelectionModel::SelectionFlags command)
    ritual = (
        'ritual_ZN11QColumnView12setSelectionERK5QRect6QFlagsIN19QItemSelec'
        'tionModel13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QColumnView12setSelectionERK5QRect6QFlagsIN19QIte'
          'mSelectionModel13SelectionFlagEE')
    self.uglySide.call(ritual, self._valueOf(rect), command.value)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QColumnView::QColumnView(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#QColumnView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QColumnView::QColumnView(QWidget *parent)
    self._noteCreation(QColumnView, lambda: Rituals.call(
        'ritual_ZN11QColumnViewC1EP7QWidget', self._addressOf(parent),
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

  @overload(QModelIndex)
  def updatePreviewWidget(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QColumnView::updatePreviewWidget(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnview.html#updatePreviewWidget

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QColumnView::updatePreviewWidget(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN11QColumnView19updatePreviewWidgetERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  @overload(QModelIndex, QAbstractItemView.ScrollHint)
  def scrollTo(
      self,
      index: QModelIndex,
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QColumnView::scrollTo(const QModelIndex &index,
    ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#scrollTo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QColumnView::scrollTo(const QModelIndex &index, ScrollHint hint)
    ritual = (
        'ritual_ZN11QColumnView8scrollToERK11QModelIndexN17QAbstractItemVie'
        'w10ScrollHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QColumnView8scrollToERK11QModelIndexN17QAbstractI'
          'temView10ScrollHintE')
    self.uglySide.call(ritual, self._valueOf(index), hint.value)

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QColumnView::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#selectAll
    """
    #  void QColumnView::selectAll()
    ritual = 'ritual_ZN11QColumnView9selectAllEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView9selectAllEv'
    self.uglySide.call(ritual)

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QColumnView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnView::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN11QColumnView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QModelIndex, int, int)
  def rowsInserted(self, parent: QModelIndex, start: int, end: int) -> None:
    """
    Calls Qt's 'void QColumnView::rowsInserted(const QModelIndex &parent, int
    start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#rowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QColumnView::rowsInserted(const QModelIndex &parent, int start,
    #      int end)
    ritual = 'ritual_ZN11QColumnView12rowsInsertedERK11QModelIndexii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView12rowsInsertedERK11QModelIndexii'
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, QModelIndex)
  def currentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QColumnView::currentChanged(const QModelIndex &current,
    const QModelIndex &previous)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#currentChanged

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QColumnView::currentChanged(const QModelIndex &current, const
    #      QModelIndex &previous)
    ritual = 'ritual_ZN11QColumnView14currentChangedERK11QModelIndexS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QColumnView14currentChangedERK11QModelIndexS2_')
    self.uglySide.call(
        ritual, self._valueOf(current), self._valueOf(previous),
    )

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QColumnView::scrollContentsBy(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QColumnView::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN11QColumnView16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

  @overload(QModelIndex)
  def createColumn(
      self,
      rootIndex: QModelIndex,
  ) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QColumnView::createColumn(const
    QModelIndex &rootIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#createColumn

    Parameters
    ----------

    rootIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QColumnView::createColumn(const QModelIndex
    #      &rootIndex)
    ritual = 'ritual_ZN11QColumnView12createColumnERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QColumnView12createColumnERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(rootIndex))
    return QAbstractItemView._cuteAt(address)

  @overload(QAbstractItemView)
  @overload(NoneType)
  def initializeColumn(self, column: Optional[QAbstractItemView]) -> None:
    """
    Calls Qt's 'void QColumnView::initializeColumn(QAbstractItemView *column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#initializeColumn

    Parameters
    ----------

    column : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnView::initializeColumn(QAbstractItemView *column) const
    self.uglySide.call(
        'ritual_ZNK11QColumnView16initializeColumnEP17QAbstractItemView',
        self._addressOf(column),
    )

  def d_func(self) -> Optional[QColumnViewPrivate]:
    """
    Calls Qt's 'QColumnViewPrivate *QColumnView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnview.html#d_func

    Returns
    -------

    Optional[QColumnViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColumnViewPrivate *QColumnView::d_func()
    address = self.uglySide.call('ritual_ZN11QColumnView6d_funcEv')
    from . import QColumnViewPrivate
    return QColumnViewPrivate._cuteAt(address)

  @staticmethod
  def columnWidths(*__, **_) -> Never:
    """
    Qt's 'QList<int> QColumnView::columnWidths() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QColumnView.columnWidths' has no cute function yet. Qt's "
        "'QList<int> QColumnView::columnWidths() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setColumnWidths(*__, **_) -> Never:
    """
    Qt's 'void QColumnView::setColumnWidths(const QList<int> &list)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColumnView.setColumnWidths' has no cute function yet. Qt's 'void "
        "QColumnView::setColumnWidths(const QList<int> &list)': takes a "
        "type Python has no way to hand over yet.")
