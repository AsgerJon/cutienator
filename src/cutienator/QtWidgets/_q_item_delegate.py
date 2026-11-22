"""
QItemDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qitemdelegate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QAbstractItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QRect, QSize
  from ..QtGui import QPainter, QPixmap
  from . import QItemEditorFactory, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QEvent = WAIT['QEvent']
  QItemEditorFactory = WAIT['QItemEditorFactory']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemDelegate(QAbstractItemDelegate):
  """
  The cute side of Qt's QItemDelegate: a plain Python object standing in
  front of one C++ QItemDelegate.

  It is built on the cute 'QAbstractItemDelegate', as Qt's QItemDelegate is
  built on Qt's QAbstractItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemDelegate that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'hasClipping',
  'setClipping', 'paint', 'sizeHint', 'createEditor', 'setEditorData',
  'setModelData', 'updateEditorGeometry', 'itemEditorFactory',
  'setItemEditorFactory', 'drawDecoration', 'drawFocus', 'drawCheck',
  'eventFilter', 'editorEvent'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemDelegate::~QItemDelegate()': the destructor: Python never
    removes a C++ QItemDelegate.

  What has no ritual
  ------------------

  17 of the 36 functions Qt declares: 9 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QItemDelegate is created at the first use, not by
    'QItemDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemDelegate.
  - Qt tells when it has removed the C++ QItemDelegate. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QItemDelegate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#tr

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
    #  QString QItemDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QItemDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemDelegate'

  #  A C++ QItemDelegate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemDelegate'

  #  The functions Qt calls itself that QItemDelegate is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'drawDisplay': (
          'void QItemDelegate::drawDisplay(QPainter *, const '
          'QStyleOptionViewItem &, const QRect &, const QString &) const',
      ),
  }

  #  The functions Qt calls itself that QItemDelegate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawDecoration': (
          ('_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyleOptionV'
           'iewItemRK5QRectRK7QPixmap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'drawFocus': (
          ('_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOptionViewIte'
           'mRK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'drawCheck': (
          ('_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOptionViewIte'
           'mRK5QRectN2Qt10CheckStateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'enum', 'QtCore:Qt.CheckState'),
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
    Calls Qt's 'const QMetaObject *QItemDelegate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemDelegate::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QItemDelegate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasClipping(self) -> bool:
    """
    Calls Qt's 'bool QItemDelegate::hasClipping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#hasClipping
    """
    #  bool QItemDelegate::hasClipping() const
    return self.uglySide.call('ritual_ZNK13QItemDelegate11hasClippingEv')

  @overload(QStyleOptionViewItem, QModelIndex)
  def sizeHint(
      self,
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> QSize:
    """
    Calls Qt's 'QSize QItemDelegate::sizeHint(const QStyleOptionViewItem
    &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#sizeHint

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QItemDelegate::sizeHint(const QStyleOptionViewItem &option,
    #      const QModelIndex &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QMo'
        'delIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemR'
          'K11QModelIndex')
    address = self.uglySide.call(
        ritual, self._valueOf(option), self._valueOf(index),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QWidget, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def createEditor(
      self,
      parent: Optional[QWidget],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QItemDelegate::createEditor(QWidget *parent, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#createEditor

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QItemDelegate::createEditor(QWidget *parent, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleOptionV'
        'iewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleO'
          'ptionViewItemRK11QModelIndex')
    address = self.uglySide.call(
        ritual,
        self._addressOf(parent), self._valueOf(option), self._valueOf(index),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def itemEditorFactory(self) -> Optional[QItemEditorFactory]:
    """
    Calls Qt's 'QItemEditorFactory *QItemDelegate::itemEditorFactory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemdelegate.html#itemEditorFactory

    Returns
    -------

    Optional[QItemEditorFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemEditorFactory *QItemDelegate::itemEditorFactory() const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate17itemEditorFactoryEv',
    )
    from . import QItemEditorFactory
    return QItemEditorFactory._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setClipping(self, clip: bool) -> None:
    """
    Calls Qt's 'void QItemDelegate::setClipping(bool clip)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#setClipping

    Parameters
    ----------

    clip : bool
      Passed on as it is.
    """
    #  void QItemDelegate::setClipping(bool clip)
    self.uglySide.call('ritual_ZN13QItemDelegate11setClippingEb', clip)

  @overload(QWidget, QModelIndex)
  @overload(NoneType, QModelIndex)
  def setEditorData(
      self,
      editor: Optional[QWidget],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::setEditorData(QWidget *editor, const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#setEditorData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QItemDelegate::setEditorData(QWidget *editor, const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModel'
          'Index')
    self.uglySide.call(ritual, self._addressOf(editor), self._valueOf(index))

  @overload(QWidget, QAbstractItemModel, QModelIndex)
  @overload(QWidget, NoneType, QModelIndex)
  @overload(NoneType, QAbstractItemModel, QModelIndex)
  @overload(NoneType, NoneType, QModelIndex)
  def setModelData(
      self,
      editor: Optional[QWidget],
      model: Optional[QAbstractItemModel],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::setModelData(QWidget *editor,
    QAbstractItemModel *model, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#setModelData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QItemDelegate::setModelData(QWidget *editor, QAbstractItemModel
    #      *model, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstractItemM'
        'odelRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstrac'
          'tItemModelRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(editor), self._addressOf(model),
        self._valueOf(index),
    )

  @overload(QItemEditorFactory)
  @overload(NoneType)
  def setItemEditorFactory(
      self,
      factory: Optional[QItemEditorFactory],
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::setItemEditorFactory(QItemEditorFactory
    *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemdelegate.html#setItemEditorFactory

    Parameters
    ----------

    factory : Optional[QItemEditorFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemDelegate::setItemEditorFactory(QItemEditorFactory *factory)
    self.uglySide.call(
        'ritual_ZN13QItemDelegate20setItemEditorFactoryEP18QItemEditorFacto'
        'ry',
        self._addressOf(factory),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QItemDelegate::QItemDelegate(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#QItemDelegate

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemDelegate::QItemDelegate(QObject *parent)
    self._noteCreation(QItemDelegate, lambda: Rituals.call(
        'ritual_ZN13QItemDelegateC1EP7QObject', self._addressOf(parent),
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

  @overload(QPainter, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def paint(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::paint(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QItemDelegate::paint(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionViewItem'
        'RK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionVi'
          'ewItemRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(QWidget, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def updateEditorGeometry(
      self,
      editor: Optional[QWidget],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::updateEditorGeometry(QWidget *editor,
    const QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemdelegate.html#updateEditorGeometry

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QItemDelegate::updateEditorGeometry(QWidget *editor, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyl'
        'eOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK2'
          '0QStyleOptionViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(editor), self._valueOf(option), self._valueOf(index),
    )

  @overload(QPainter, QStyleOptionViewItem, QRect, QPixmap)
  @overload(NoneType, QStyleOptionViewItem, QRect, QPixmap)
  def drawDecoration(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      rect: QRect,
      pixmap: QPixmap,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::drawDecoration(QPainter *painter, const
    QStyleOptionViewItem &option, const QRect &rect, const QPixmap &pixmap)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#drawDecoration

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QItemDelegate::drawDecoration(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QRect &rect, const QPixmap
    #      &pixmap) const
    self.uglySide.call(
        'ritual_own_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyle'
        'OptionViewItemRK5QRectRK7QPixmap',
        self._addressOf(painter), self._valueOf(option), self._valueOf(rect),
        self._valueOf(pixmap),
    )

  @overload(QPainter, QStyleOptionViewItem, QRect)
  @overload(NoneType, QStyleOptionViewItem, QRect)
  def drawFocus(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      rect: QRect,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::drawFocus(QPainter *painter, const
    QStyleOptionViewItem &option, const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#drawFocus

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QItemDelegate::drawFocus(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QRect &rect) const
    self.uglySide.call(
        'ritual_own_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOption'
        'ViewItemRK5QRect',
        self._addressOf(painter), self._valueOf(option), self._valueOf(rect),
    )

  @overload(QPainter, QStyleOptionViewItem, QRect, Qt.CheckState)
  @overload(NoneType, QStyleOptionViewItem, QRect, Qt.CheckState)
  def drawCheck(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      rect: QRect,
      state: Qt.CheckState,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::drawCheck(QPainter *painter, const
    QStyleOptionViewItem &option, const QRect &rect, Qt::CheckState state)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#drawCheck

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QItemDelegate::drawCheck(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QRect &rect, Qt::CheckState
    #      state) const
    self.uglySide.call(
        'ritual_own_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOption'
        'ViewItemRK5QRectN2Qt10CheckStateE',
        self._addressOf(painter), self._valueOf(option), self._valueOf(rect),
        state.value,
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QItemDelegate::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QItemDelegate::eventFilter(QObject *object, QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN13QItemDelegate11eventFilterEP7QObjectP6QEvent',
        self._addressOf(object), self._addressOf(event),
    )

  @overload(QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex)
  @overload(QEvent, NoneType, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QAbstractItemModel, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, NoneType, QStyleOptionViewItem, QModelIndex)
  def editorEvent(
      self,
      event: Optional[QEvent],
      model: Optional[QAbstractItemModel],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QItemDelegate::editorEvent(QEvent *event,
    QAbstractItemModel *model, const QStyleOptionViewItem &option, const
    QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#editorEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
    #      *model, const QStyleOptionViewItem &option, const QModelIndex
    #      &index)
    return self.uglySide.call(
        'ritual_own_ZN13QItemDelegate11editorEventEP6QEventP18QAbstractItem'
        'ModelRK20QStyleOptionViewItemRK11QModelIndex',
        self._addressOf(event), self._addressOf(model),
        self._valueOf(option), self._valueOf(index),
    )
