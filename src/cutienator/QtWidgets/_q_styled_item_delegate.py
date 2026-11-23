"""
QStyledItemDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleditemdelegate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QLocale, QMetaObject
  from ..QtCore import QModelIndex, QSize, QVariant
  from ..QtGui import QPainter
  from . import QItemEditorFactory, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QEvent = WAIT['QEvent']
  QItemEditorFactory = WAIT['QItemEditorFactory']
  QLocale = WAIT['QLocale']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyledItemDelegate(QAbstractItemDelegate):
  """
  The cute side of Qt's QStyledItemDelegate: a plain Python object standing
  in front of one C++ QStyledItemDelegate.

  It is built on the cute 'QAbstractItemDelegate', as Qt's
  QStyledItemDelegate is built on Qt's QAbstractItemDelegate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QStyledItemDelegate that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'paint',
  'sizeHint', 'createEditor', 'setEditorData', 'setModelData',
  'updateEditorGeometry', 'itemEditorFactory', 'setItemEditorFactory',
  'displayText', 'initStyleOption', 'eventFilter', 'editorEvent'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyledItemDelegate::~QStyledItemDelegate()': the destructor:
    Python never removes a C++ QStyledItemDelegate.

  What has no ritual
  ------------------

  8 of the 24 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QStyledItemDelegate is created at the first use, not by
    'QStyledItemDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyledItemDelegate.
  - Qt tells when it has removed the C++ QStyledItemDelegate. Every call on
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
    Calls Qt's 'QString QStyledItemDelegate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleditemdelegate.html#tr

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
    #  QString QStyledItemDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QStyledItemDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyledItemDelegate'

  #  A C++ QStyledItemDelegate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStyledItemDelegate'

  #  The functions Qt calls itself that QStyledItemDelegate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'displayText': (
          ('_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QLocale'),
           )),
      ),
      'initStyleOption': (
          ('_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionViewI'
           'temRK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionViewItem'),
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
    Calls Qt's 'const QMetaObject *QStyledItemDelegate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyledItemDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QStyledItemDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStyleOptionViewItem, QModelIndex)
  def sizeHint(
      self,
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> QSize:
    """
    Calls Qt's 'QSize QStyledItemDelegate::sizeHint(const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint

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
    #  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem
    #      &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate8sizeHintERK20QStyleOptionViewItemR'
        'K11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate8sizeHintERK20QStyleOptionVie'
          'wItemRK11QModelIndex')
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
    Calls Qt's 'QWidget *QStyledItemDelegate::createEditor(QWidget *parent,
    const QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#createEditor

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
    #  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate12createEditorEP7QWidgetRK20QStyleO'
        'ptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate12createEditorEP7QWidgetRK20Q'
          'StyleOptionViewItemRK11QModelIndex')
    address = self.uglySide.call(
        ritual,
        self._addressOf(parent), self._valueOf(option), self._valueOf(index),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def itemEditorFactory(self) -> Optional[QItemEditorFactory]:
    """
    Calls Qt's 'QItemEditorFactory *QStyledItemDelegate::itemEditorFactory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#itemEditorFactory

    Returns
    -------

    Optional[QItemEditorFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemEditorFactory *QStyledItemDelegate::itemEditorFactory() const
    address = self.uglySide.call(
        'ritual_ZNK19QStyledItemDelegate17itemEditorFactoryEv',
    )
    from . import QItemEditorFactory
    return QItemEditorFactory._cuteAt(address)

  @overload(QVariant, QLocale)
  def displayText(self, value: QVariant, locale: QLocale) -> str:
    """
    Calls Qt's 'QString QStyledItemDelegate::displayText(const QVariant
    &value, const QLocale &locale) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#displayText

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyledItemDelegate::displayText(const QVariant &value, const
    #      QLocale &locale) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7Q'
          'Locale')
    return self.uglySide.call(
        ritual, self._valueOf(value), self._valueOf(locale),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, QModelIndex)
  @overload(NoneType, QModelIndex)
  def setEditorData(
      self,
      editor: Optional[QWidget],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QStyledItemDelegate::setEditorData(QWidget *editor,
    const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#setEditorData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QStyledItemDelegate::setEditorData(QWidget *editor, const
    #      QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate13setEditorDataEP7QWidgetRK11QModel'
        'Index')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate13setEditorDataEP7QWidgetRK11'
          'QModelIndex')
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
    Calls Qt's 'void QStyledItemDelegate::setModelData(QWidget *editor,
    QAbstractItemModel *model, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#setModelData

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
    #  void QStyledItemDelegate::setModelData(QWidget *editor,
    #      QAbstractItemModel *model, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate12setModelDataEP7QWidgetP18QAbstrac'
        'tItemModelRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate12setModelDataEP7QWidgetP18QA'
          'bstractItemModelRK11QModelIndex')
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
    Calls Qt's 'void
    QStyledItemDelegate::setItemEditorFactory(QItemEditorFactory *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory

    Parameters
    ----------

    factory : Optional[QItemEditorFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyledItemDelegate::setItemEditorFactory(QItemEditorFactory
    #      *factory)
    self.uglySide.call(
        'ritual_ZN19QStyledItemDelegate20setItemEditorFactoryEP18QItemEdito'
        'rFactory',
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
    Notes what was given, for Qt's
    'QStyledItemDelegate::QStyledItemDelegate(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#QStyledItemDelegate

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStyledItemDelegate::QStyledItemDelegate(QObject *parent)
    self._noteCreation(QStyledItemDelegate, lambda: Rituals.call(
        'ritual_ZN19QStyledItemDelegateC1EP7QObject',
        self._addressOf(parent),
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
    Calls Qt's 'void QStyledItemDelegate::paint(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint

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
    #  void QStyledItemDelegate::paint(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate5paintEP8QPainterRK20QStyleOptionVi'
        'ewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate5paintEP8QPainterRK20QStyleOp'
          'tionViewItemRK11QModelIndex')
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
    Calls Qt's 'void QStyledItemDelegate::updateEditorGeometry(QWidget
    *editor, const QStyleOptionViewItem &option, const QModelIndex &index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#updateEditorGeometry

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
    #  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate20updateEditorGeometryEP7QWidgetRK2'
        '0QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate20updateEditorGeometryEP7QWid'
          'getRK20QStyleOptionViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(editor), self._valueOf(option), self._valueOf(index),
    )

  @overload(QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QModelIndex)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionViewItem],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QStyledItemDelegate::initStyleOption(QStyleOptionViewItem *option, const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QStyledItemDelegate::initStyleOption(QStyleOptionViewItem
    #      *option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOptionVi'
        'ewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QStyledItemDelegate15initStyleOptionEP20QStyleOp'
          'tionViewItemRK11QModelIndex')
    self.uglySide.call(ritual, self._addressOf(option), self._valueOf(index))

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
    Calls Qt's 'bool QStyledItemDelegate::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStyledItemDelegate::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN19QStyledItemDelegate11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QStyledItemDelegate11eventFilterEP7QObjectP6QEven'
          't')
    return self.uglySide.call(
        ritual, self._addressOf(object), self._addressOf(event),
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
    Calls Qt's 'bool QStyledItemDelegate::editorEvent(QEvent *event,
    QAbstractItemModel *model, const QStyleOptionViewItem &option, const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleditemdelegate.html#editorEvent

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
    #  bool QStyledItemDelegate::editorEvent(QEvent *event,
    #      QAbstractItemModel *model, const QStyleOptionViewItem &option,
    #      const QModelIndex &index)
    ritual = (
        'ritual_ZN19QStyledItemDelegate11editorEventEP6QEventP18QAbstractIt'
        'emModelRK20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QStyledItemDelegate11editorEventEP6QEventP18QAbst'
          'ractItemModelRK20QStyleOptionViewItemRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(model),
        self._valueOf(option), self._valueOf(index),
    )
