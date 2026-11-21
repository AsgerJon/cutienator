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
from ..QtCore import QObject
from . import QAbstractItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QMetaObject, QModelIndex, QSize
  from ..QtGui import QPainter
  from . import QItemEditorFactory, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QItemEditorFactory = WAIT['QItemEditorFactory']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
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
  call so far, 12 names in all: 'metaObject', 'tr', 'hasClipping',
  'setClipping', 'paint', 'sizeHint', 'createEditor', 'setEditorData',
  'setModelData', 'updateEditorGeometry', 'itemEditorFactory',
  'setItemEditorFactory'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemDelegate::~QItemDelegate()': the destructor: Python never
    removes a C++ QItemDelegate.

  What has no ritual
  ------------------

  22 of the 36 functions Qt declares: 14 protected; 3 private; 2 takes or
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
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QMo'
        'delIndex',
        self._valueOf(option), self._valueOf(index),
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
    address = self.uglySide.call(
        'ritual_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleOptionV'
        'iewItemRK11QModelIndex',
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
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex',
        self._addressOf(editor), self._valueOf(index),
    )

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
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstractItemM'
        'odelRK11QModelIndex',
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
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionViewItem'
        'RK11QModelIndex',
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
    self.uglySide.call(
        'ritual_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyl'
        'eOptionViewItemRK11QModelIndex',
        self._addressOf(editor), self._valueOf(option), self._valueOf(index),
    )
