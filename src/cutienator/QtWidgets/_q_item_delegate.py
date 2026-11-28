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
  from ..QtCore import QRect, QSize, QVariant
  from ..QtGui import QFont, QPainter, QPalette, QPixmap
  from . import QItemEditorFactory, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QItemEditorFactory = WAIT['QItemEditorFactory']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QVariant = WAIT['QVariant']
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
  call so far, 26 names in all: 'metaObject', 'tr', 'hasClipping',
  'setClipping', 'paint', 'sizeHint', 'createEditor', 'setEditorData',
  'setModelData', 'updateEditorGeometry', 'itemEditorFactory',
  'setItemEditorFactory', 'drawDisplay', 'drawDecoration', 'drawFocus',
  'drawCheck', 'drawBackground', 'doLayout', 'rect', 'eventFilter',
  'editorEvent', 'setOptions', 'decoration', 'selectedPixmap', 'doCheck',
  'textRectangle'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QItemDelegate::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QItemDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QItemDelegate::~QItemDelegate()': the destructor: Python never
    removes a C++ QItemDelegate.
  - Qt's 'QItemDelegatePrivate *QItemDelegate::d_func()': gives
    'QItemDelegatePrivate', which has no cute class yet.
  - Qt's 'const QItemDelegatePrivate *QItemDelegate::d_func() const': gives
    'QItemDelegatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

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

  @staticmethod
  @overload(QPixmap, QPalette, bool)
  def selectedPixmap(
      pixmap: QPixmap,
      palette: QPalette,
      enabled: bool,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QItemDelegate::selectedPixmap(const QPixmap &pixmap,
    const QPalette &palette, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#selectedPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    enabled : bool
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QItemDelegate::selectedPixmap(const QPixmap &pixmap, const
    #      QPalette &palette, bool enabled)
    address = Rituals.call(
        'ritual_ZN13QItemDelegate14selectedPixmapERK7QPixmapRK8QPaletteb',
        CuteMixin._valueOf(pixmap), CuteMixin._valueOf(palette), enabled,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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

  #  The functions Qt calls itself that QItemDelegate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawDisplay': (
          ('_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleOptionView'
           'ItemRK5QRectRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'text', ''),
           )),
      ),
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

  @overload(QStyleOptionViewItem, QModelIndex, int)
  def rect(
      self,
      option: QStyleOptionViewItem,
      index: QModelIndex,
      role: int,
  ) -> QRect:
    """
    Calls Qt's 'QRect QItemDelegate::rect(const QStyleOptionViewItem &option,
    const QModelIndex &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#rect

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QItemDelegate::rect(const QStyleOptionViewItem &option, const
    #      QModelIndex &index, int role) const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate4rectERK20QStyleOptionViewItemRK11QModelI'
        'ndexi',
        self._valueOf(option), self._valueOf(index), role,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyleOptionViewItem, QVariant)
  def decoration(
      self,
      option: QStyleOptionViewItem,
      variant: QVariant,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QItemDelegate::decoration(const QStyleOptionViewItem
    &option, const QVariant &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#decoration

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QItemDelegate::decoration(const QStyleOptionViewItem &option,
    #      const QVariant &variant) const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate10decorationERK20QStyleOptionViewItemRK8Q'
        'Variant',
        self._valueOf(option), self._valueOf(variant),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QStyleOptionViewItem, QRect, QVariant)
  def doCheck(
      self,
      option: QStyleOptionViewItem,
      bounding: QRect,
      variant: QVariant,
  ) -> QRect:
    """
    Calls Qt's 'QRect QItemDelegate::doCheck(const QStyleOptionViewItem
    &option, const QRect &bounding, const QVariant &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#doCheck

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    bounding : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QItemDelegate::doCheck(const QStyleOptionViewItem &option, const
    #      QRect &bounding, const QVariant &variant) const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate7doCheckERK20QStyleOptionViewItemRK5QRect'
        'RK8QVariant',
        self._valueOf(option), self._valueOf(bounding),
        self._valueOf(variant),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPainter, QRect, QFont, str)
  @overload(NoneType, QRect, QFont, str)
  def textRectangle(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      font: QFont,
      text: str,
  ) -> QRect:
    """
    Calls Qt's 'QRect QItemDelegate::textRectangle(QPainter *painter, const
    QRect &rect, const QFont &font, const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#textRectangle

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QItemDelegate::textRectangle(QPainter *painter, const QRect
    #      &rect, const QFont &font, const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate13textRectangleEP8QPainterRK5QRectRK5QFon'
        'tRK7QString',
        self._addressOf(painter), self._valueOf(rect), self._valueOf(font),
        text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @overload(QModelIndex, QStyleOptionViewItem)
  def setOptions(
      self,
      index: QModelIndex,
      option: QStyleOptionViewItem,
  ) -> QStyleOptionViewItem:
    """
    Calls Qt's 'QStyleOptionViewItem QItemDelegate::setOptions(const
    QModelIndex &index, const QStyleOptionViewItem &option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#setOptions

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    Returns
    -------

    QStyleOptionViewItem
      A new cute QStyleOptionViewItem around the copy Qt gave back. Python
      owns it.
    """
    #  QStyleOptionViewItem QItemDelegate::setOptions(const QModelIndex
    #      &index, const QStyleOptionViewItem &option) const
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate10setOptionsERK11QModelIndexRK20QStyleOpt'
        'ionViewItem',
        self._valueOf(index), self._valueOf(option),
    )
    from . import QStyleOptionViewItem
    return QStyleOptionViewItem._cuteOwning(address)

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
        'ritual_ZN13QItemDelegateC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QPainter, QStyleOptionViewItem, QRect, str)
  @overload(NoneType, QStyleOptionViewItem, QRect, str)
  def drawDisplay(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      rect: QRect,
      text: str,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::drawDisplay(QPainter *painter, const
    QStyleOptionViewItem &option, const QRect &rect, const QString &text)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#drawDisplay

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

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QItemDelegate::drawDisplay(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QRect &rect, const QString
    #      &text) const
    ritual = (
        'ritual_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleOptionV'
        'iewItemRK5QRectRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleO'
          'ptionViewItemRK5QRectRK7QString')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(option), self._valueOf(rect),
        text,
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
    ritual = (
        'ritual_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyleOpti'
        'onViewItemRK5QRectRK7QPixmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QSty'
          'leOptionViewItemRK5QRectRK7QPixmap')
    self.uglySide.call(
        ritual,
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
    ritual = (
        'ritual_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOptionView'
        'ItemRK5QRect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOpti'
          'onViewItemRK5QRect')
    self.uglySide.call(
        ritual,
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
    ritual = (
        'ritual_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOptionView'
        'ItemRK5QRectN2Qt10CheckStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOpti'
          'onViewItemRK5QRectN2Qt10CheckStateE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(option), self._valueOf(rect),
        state.value,
    )

  @overload(QPainter, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def drawBackground(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::drawBackground(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#drawBackground

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
    #  void QItemDelegate::drawBackground(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate14drawBackgroundEP8QPainterRK20QStyleOpti'
        'onViewItemRK11QModelIndex',
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(QStyleOptionViewItem, QRect, QRect, QRect, bool)
  @overload(QStyleOptionViewItem, QRect, QRect, NoneType, bool)
  @overload(QStyleOptionViewItem, QRect, NoneType, QRect, bool)
  @overload(QStyleOptionViewItem, QRect, NoneType, NoneType, bool)
  @overload(QStyleOptionViewItem, NoneType, QRect, QRect, bool)
  @overload(QStyleOptionViewItem, NoneType, QRect, NoneType, bool)
  @overload(QStyleOptionViewItem, NoneType, NoneType, QRect, bool)
  @overload(QStyleOptionViewItem, NoneType, NoneType, NoneType, bool)
  def doLayout(
      self,
      option: QStyleOptionViewItem,
      checkRect: Optional[QRect],
      iconRect: Optional[QRect],
      textRect: Optional[QRect],
      hint: bool,
  ) -> None:
    """
    Calls Qt's 'void QItemDelegate::doLayout(const QStyleOptionViewItem
    &option, QRect *checkRect, QRect *iconRect, QRect *textRect, bool hint)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemdelegate.html#doLayout

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    checkRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iconRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    textRect : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : bool
      Passed on as it is.
    """
    #  void QItemDelegate::doLayout(const QStyleOptionViewItem &option, QRect
    #      *checkRect, QRect *iconRect, QRect *textRect, bool hint) const
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate8doLayoutERK20QStyleOptionViewItemP5QRect'
        'S4_S4_b',
        self._valueOf(option), self._addressOf(checkRect),
        self._addressOf(iconRect), self._addressOf(textRect), hint,
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
    ritual = 'ritual_ZN13QItemDelegate11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QItemDelegate11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
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
    ritual = (
        'ritual_ZN13QItemDelegate11editorEventEP6QEventP18QAbstractItemMode'
        'lRK20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QItemDelegate11editorEventEP6QEventP18QAbstractIt'
          'emModelRK20QStyleOptionViewItemRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(model),
        self._valueOf(option), self._valueOf(index),
    )
