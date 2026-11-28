"""
QAbstractItemDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractitemdelegate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QSize
  from ..QtGui import QHelpEvent, QPainter
  from . import QAbstractItemDelegatePrivate, QAbstractItemView
  from . import QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QAbstractItemView = WAIT['QAbstractItemView']
  QEvent = WAIT['QEvent']
  QHelpEvent = WAIT['QHelpEvent']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemDelegate(QObject):
  """
  The cute side of Qt's QAbstractItemDelegate: a plain Python object standing
  in front of one C++ QAbstractItemDelegate.

  It is built on the cute 'QObject', as Qt's QAbstractItemDelegate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemDelegate that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'paint',
  'sizeHint', 'createEditor', 'destroyEditor', 'setEditorData',
  'setModelData', 'updateEditorGeometry', 'editorEvent', 'handleEditorEvent',
  'helpEvent', 'commitData', 'closeEditor', 'sizeHintChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractItemDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractItemDelegate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractItemDelegate::~QAbstractItemDelegate()': the destructor:
    Python never removes a C++ QAbstractItemDelegate.
  - Qt's 'QList<int> QAbstractItemDelegate::paintingRoles() const': gives a
    type Python has no way to take yet.
  - Qt's 'QAbstractItemDelegate::QAbstractItemDelegate(QObjectPrivate &a0,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QAbstractItemDelegatePrivate *QAbstractItemDelegate::d_func()
    const': takes in Python what 'QAbstractItemDelegatePrivate
    *QAbstractItemDelegate::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractItemDelegate is created at the first use, not by
    'QAbstractItemDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemDelegate.
  - Qt tells when it has removed the C++ QAbstractItemDelegate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractItemDelegate that has no cute function yet,
    'paintingRoles', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QAbstractItemDelegate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class EndEditHint(CuteNum):
    """
    The enum 'QAbstractItemDelegate::EndEditHint' of Qt, with the 5 names Qt
    gives in it.
    """

    NoHint = Kee[int](0)
    EditNextItem = Kee[int](1)
    EditPreviousItem = Kee[int](2)
    SubmitModelCache = Kee[int](3)
    RevertModelCache = Kee[int](4)

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
    Calls Qt's 'QString QAbstractItemDelegate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemdelegate.html#tr

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
    #  QString QAbstractItemDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QAbstractItemDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemDelegate'

  #  A C++ QAbstractItemDelegate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemDelegate'

  #  The functions Qt calls itself that QAbstractItemDelegate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'paintingRoles': (
          'QList<int> QAbstractItemDelegate::paintingRoles() const',
      ),
  }

  #  The functions Qt calls itself that QAbstractItemDelegate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'paint': (
          ('_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionVie'
           'wItemRK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'sizeHint': (
          ('_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK'
           '11QModelIndex',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'createEditor': (
          ('_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOp'
           'tionViewItemRK11QModelIndex',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'destroyEditor': (
          ('_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelI'
           'ndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'setEditorData': (
          ('_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelI'
           'ndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'setModelData': (
          ('_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstract'
           'ItemModelRK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtCore:QAbstractItemModel'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'updateEditorGeometry': (
          ('_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20'
           'QStyleOptionViewItemRK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'editorEvent': (
          ('_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractIte'
           'mModelRK20QStyleOptionViewItemRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
               ('address', 'address', 'QtCore:QAbstractItemModel'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'helpEvent': (
          ('_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractI'
           'temViewRK20QStyleOptionViewItemRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QHelpEvent'),
               ('address', 'address', 'QtWidgets:QAbstractItemView'),
               ('address', 'value', 'QtWidgets:QStyleOptionViewItem'),
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
    Calls Qt's 'const QMetaObject *QAbstractItemDelegate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractItemDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractItemDelegate10metaObjectEv',
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
    Calls Qt's 'QSize QAbstractItemDelegate::sizeHint(const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#sizeHint

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
    #  QSize QAbstractItemDelegate::sizeHint(const QStyleOptionViewItem
    #      &option, const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewIte'
        'mRK11QModelIndex',
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
    Calls Qt's 'QWidget *QAbstractItemDelegate::createEditor(QWidget *parent,
    const QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#createEditor

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
    #  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyl'
        'eOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK2'
          '0QStyleOptionViewItemRK11QModelIndex')
    address = self.uglySide.call(
        ritual,
        self._addressOf(parent), self._valueOf(option), self._valueOf(index),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

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
    Calls Qt's 'void QAbstractItemDelegate::setEditorData(QWidget *editor,
    const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#setEditorData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
    #      QModelIndex &index) const
    ritual = (
        'ritual_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QMod'
        'elIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK'
          '11QModelIndex')
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
    Calls Qt's 'void QAbstractItemDelegate::setModelData(QWidget *editor,
    QAbstractItemModel *model, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#setModelData

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
    #  void QAbstractItemDelegate::setModelData(QWidget *editor,
    #      QAbstractItemModel *model, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstr'
        'actItemModelRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18'
          'QAbstractItemModelRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(editor), self._addressOf(model),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractItemDelegate::QAbstractItemDelegate(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#QAbstractItemDelegate

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractItemDelegate::QAbstractItemDelegate(QObject *parent)
    self._noteCreation(QAbstractItemDelegate, lambda: Rituals.call(
        'ritual_ZN21QAbstractItemDelegateC1EP7QObject',
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
    Calls Qt's 'void QAbstractItemDelegate::paint(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemdelegate.html#paint

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
    #  void QAbstractItemDelegate::paint(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    self.uglySide.call(
        'ritual_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOption'
        'ViewItemRK11QModelIndex',
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(QWidget, QModelIndex)
  @overload(NoneType, QModelIndex)
  def destroyEditor(
      self,
      editor: Optional[QWidget],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemDelegate::destroyEditor(QWidget *editor,
    const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#destroyEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
    #      QModelIndex &index) const
    ritual = (
        'ritual_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QMod'
        'elIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK'
          '11QModelIndex')
    self.uglySide.call(ritual, self._addressOf(editor), self._valueOf(index))

  @overload(QWidget, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def updateEditorGeometry(
      self,
      editor: Optional[QWidget],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemDelegate::updateEditorGeometry(QWidget
    *editor, const QStyleOptionViewItem &option, const QModelIndex &index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#updateEditorGeometry

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
    #  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor,
    #      const QStyleOptionViewItem &option, const QModelIndex &index)
    #      const
    ritual = (
        'ritual_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetR'
        'K20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QW'
          'idgetRK20QStyleOptionViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(editor), self._valueOf(option), self._valueOf(index),
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
    Calls Qt's 'bool QAbstractItemDelegate::editorEvent(QEvent *event,
    QAbstractItemModel *model, const QStyleOptionViewItem &option, const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#editorEvent

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
    #  bool QAbstractItemDelegate::editorEvent(QEvent *event,
    #      QAbstractItemModel *model, const QStyleOptionViewItem &option,
    #      const QModelIndex &index)
    ritual = (
        'ritual_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstract'
        'ItemModelRK20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAb'
          'stractItemModelRK20QStyleOptionViewItemRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(model),
        self._valueOf(option), self._valueOf(index),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def handleEditorEvent(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemDelegate::handleEditorEvent(QObject
    *object, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#handleEditorEvent

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemDelegate::handleEditorEvent(QObject *object, QEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN21QAbstractItemDelegate17handleEditorEventEP7QObjectP6QEv'
        'ent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QHelpEvent, QAbstractItemView, QStyleOptionViewItem, QModelIndex)
  @overload(QHelpEvent, NoneType, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QAbstractItemView, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, NoneType, QStyleOptionViewItem, QModelIndex)
  def helpEvent(
      self,
      event: Optional[QHelpEvent],
      view: Optional[QAbstractItemView],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
    QAbstractItemView *view, const QStyleOptionViewItem &option, const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#helpEvent

    Parameters
    ----------

    event : Optional[QHelpEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    view : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
    #      QAbstractItemView *view, const QStyleOptionViewItem &option, const
    #      QModelIndex &index)
    ritual = (
        'ritual_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstra'
        'ctItemViewRK20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17Q'
          'AbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(view), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(QWidget)
  @overload(NoneType)
  def commitData(self, editor: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractItemDelegate::commitData(QWidget *editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#commitData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemDelegate::commitData(QWidget *editor)
    self.uglySide.call(
        'ritual_ZN21QAbstractItemDelegate10commitDataEP7QWidget',
        self._addressOf(editor),
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, EndEditHint)
  @overload(NoneType, EndEditHint)
  def closeEditor(
      self,
      editor: Optional[QWidget],
      hint: EndEditHint = EndEditHint.NoHint,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemDelegate::closeEditor(QWidget *editor,
    QAbstractItemDelegate::EndEditHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#closeEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : EndEditHint
      Passed on as its number. May be left out, as in Qt: it is then
      EndEditHint.NoHint.
    """
    #  void QAbstractItemDelegate::closeEditor(QWidget *editor,
    #      QAbstractItemDelegate::EndEditHint hint)
    self.uglySide.call(
        'ritual_ZN21QAbstractItemDelegate11closeEditorEP7QWidgetNS_11EndEdi'
        'tHintE',
        self._addressOf(editor), hint.value,
    )

  @overload(QModelIndex)
  def sizeHintChanged(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemDelegate::sizeHintChanged(const QModelIndex
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemdelegate.html#sizeHintChanged

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemDelegate::sizeHintChanged(const QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN21QAbstractItemDelegate15sizeHintChangedERK11QModelIndex',
        self._valueOf(a0),
    )

  def d_func(self) -> Optional[QAbstractItemDelegatePrivate]:
    """
    Calls Qt's 'QAbstractItemDelegatePrivate
    *QAbstractItemDelegate::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemdelegate.html#d_func

    Returns
    -------

    Optional[QAbstractItemDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegatePrivate *QAbstractItemDelegate::d_func()
    address = self.uglySide.call('ritual_ZN21QAbstractItemDelegate6d_funcEv')
    from . import QAbstractItemDelegatePrivate
    return QAbstractItemDelegatePrivate._cuteAt(address)

  @staticmethod
  def paintingRoles(*__, **_) -> Never:
    """
    Qt's 'QList<int> QAbstractItemDelegate::paintingRoles() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractItemDelegate.paintingRoles' has no cute function yet. "
        "Qt's 'QList<int> QAbstractItemDelegate::paintingRoles() const': "
        "gives a type Python has no way to take yet.")
