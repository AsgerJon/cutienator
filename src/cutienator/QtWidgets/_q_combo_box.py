"""
QComboBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcombobox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QComboBoxInsertPolicy, QComboBoxLabelDrawingMode
from . import QComboBoxSizeAdjustPolicy, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QSize, QVariant
  from ..QtGui import QIcon, QValidator
  from . import QAbstractItemDelegate, QAbstractItemView, QCompleter
  from . import QLineEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemDelegate = WAIT['QAbstractItemDelegate']
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QAbstractItemView = WAIT['QAbstractItemView']
  QCompleter = WAIT['QCompleter']
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QLineEdit = WAIT['QLineEdit']
  QModelIndex = WAIT['QModelIndex']
  QSize = WAIT['QSize']
  QValidator = WAIT['QValidator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBox(QWidget):
  """
  The cute side of Qt's QComboBox: a plain Python object standing in front of
  one C++ QComboBox.

  It is built on the cute 'QWidget', as Qt's QComboBox is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBox that has a ritual and that Python can call
  so far, 67 names in all: 'metaObject', 'tr', 'maxVisibleItems',
  'setMaxVisibleItems', 'count', 'setMaxCount', 'maxCount',
  'duplicatesEnabled', 'setDuplicatesEnabled', 'setFrame', 'hasFrame',
  'findText', 'findData', 'insertPolicy', 'setInsertPolicy',
  'sizeAdjustPolicy', 'setSizeAdjustPolicy', 'minimumContentsLength',
  'setMinimumContentsLength', 'iconSize', 'setIconSize',
  'setPlaceholderText', 'placeholderText', 'isEditable', 'setEditable',
  'setLineEdit', 'lineEdit', 'setValidator', 'validator', 'setCompleter',
  'completer', 'itemDelegate', 'setItemDelegate', 'model', 'setModel',
  'rootModelIndex', 'setRootModelIndex', 'modelColumn', 'setModelColumn',
  'labelDrawingMode', 'setLabelDrawingMode', 'currentIndex', 'currentText',
  'currentData', 'itemText', 'itemIcon', 'itemData', 'addItem', 'insertItem',
  'insertSeparator', 'removeItem', 'setItemText', 'setItemIcon',
  'setItemData', 'view', 'setView', 'sizeHint', 'minimumSizeHint',
  'showPopup', 'hidePopup', 'event', 'inputMethodQuery', 'clear',
  'clearEditText', 'setEditText', 'setCurrentIndex', 'setCurrentText'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QComboBox::~QComboBox()': the destructor: Python never removes a
    C++ QComboBox.

  What has no ritual
  ------------------

  33 of the 105 functions Qt declares: 16 protected; 7 a signal; 4 takes or
  gives a type that cannot be passed yet; 3 private; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QComboBox is created at the first use, not by 'QComboBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBox.
  - Qt tells when it has removed the C++ QComboBox. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QComboBox, and the names Qt has for the
  #  combinations of its flags enums.
  InsertPolicy = QComboBoxInsertPolicy
  LabelDrawingMode = QComboBoxLabelDrawingMode
  SizeAdjustPolicy = QComboBoxSizeAdjustPolicy

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
    Calls Qt's 'QString QComboBox::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#tr

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
    #  QString QComboBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QComboBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QComboBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QComboBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maxVisibleItems(self) -> int:
    """
    Calls Qt's 'int QComboBox::maxVisibleItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#maxVisibleItems
    """
    #  int QComboBox::maxVisibleItems() const
    return self.uglySide.call('ritual_ZNK9QComboBox15maxVisibleItemsEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QComboBox::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#count
    """
    #  int QComboBox::count() const
    return self.uglySide.call('ritual_ZNK9QComboBox5countEv')

  def maxCount(self) -> int:
    """
    Calls Qt's 'int QComboBox::maxCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#maxCount
    """
    #  int QComboBox::maxCount() const
    return self.uglySide.call('ritual_ZNK9QComboBox8maxCountEv')

  def duplicatesEnabled(self) -> bool:
    """
    Calls Qt's 'bool QComboBox::duplicatesEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#duplicatesEnabled
    """
    #  bool QComboBox::duplicatesEnabled() const
    return self.uglySide.call('ritual_ZNK9QComboBox17duplicatesEnabledEv')

  def hasFrame(self) -> bool:
    """
    Calls Qt's 'bool QComboBox::hasFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#hasFrame
    """
    #  bool QComboBox::hasFrame() const
    return self.uglySide.call('ritual_ZNK9QComboBox8hasFrameEv')

  @overload(str, Qt.MatchFlags)
  def findText(self, text: str, flags: Qt.MatchFlags) -> int:
    """
    Calls Qt's 'int QComboBox::findText(const QString &text, Qt::MatchFlags
    flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#findText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    flags : Qt.MatchFlags
      Passed on as its number.
    """
    #  int QComboBox::findText(const QString &text, Qt::MatchFlags flags)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QComboBox8findTextERK7QString6QFlagsIN2Qt9MatchFlagEE',
        text, flags.value,
    )

  @overload(QVariant, int, Qt.MatchFlags)
  def findData(self, data: QVariant, role: int, flags: Qt.MatchFlags) -> int:
    """
    Calls Qt's 'int QComboBox::findData(const QVariant &data, int role,
    Qt::MatchFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#findData

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is.

    flags : Qt.MatchFlags
      Passed on as its number.
    """
    #  int QComboBox::findData(const QVariant &data, int role, Qt::MatchFlags
    #      flags) const
    return self.uglySide.call(
        'ritual_ZNK9QComboBox8findDataERK8QVarianti6QFlagsIN2Qt9MatchFlagEE',
        self._valueOf(data), role, flags.value,
    )

  def insertPolicy(self) -> InsertPolicy:
    """
    Calls Qt's 'InsertPolicy QComboBox::insertPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#insertPolicy

    Returns
    -------

    InsertPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InsertPolicy(number)'
      gives.
    """
    #  InsertPolicy QComboBox::insertPolicy() const
    return QComboBox.InsertPolicy(self.uglySide.call(
        'ritual_ZNK9QComboBox12insertPolicyEv',
    ))

  def sizeAdjustPolicy(self) -> SizeAdjustPolicy:
    """
    Calls Qt's 'SizeAdjustPolicy QComboBox::sizeAdjustPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#sizeAdjustPolicy

    Returns
    -------

    SizeAdjustPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeAdjustPolicy(number)'
      gives.
    """
    #  SizeAdjustPolicy QComboBox::sizeAdjustPolicy() const
    return QComboBox.SizeAdjustPolicy(self.uglySide.call(
        'ritual_ZNK9QComboBox16sizeAdjustPolicyEv',
    ))

  def minimumContentsLength(self) -> int:
    """
    Calls Qt's 'int QComboBox::minimumContentsLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcombobox.html#minimumContentsLength
    """
    #  int QComboBox::minimumContentsLength() const
    return self.uglySide.call(
        'ritual_ZNK9QComboBox21minimumContentsLengthEv',
    )

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QComboBox::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QComboBox::iconSize() const
    address = self.uglySide.call('ritual_ZNK9QComboBox8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QComboBox::placeholderText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QComboBox::placeholderText() const
    return self.uglySide.call('ritual_ZNK9QComboBox15placeholderTextEv')

  def isEditable(self) -> bool:
    """
    Calls Qt's 'bool QComboBox::isEditable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#isEditable
    """
    #  bool QComboBox::isEditable() const
    return self.uglySide.call('ritual_ZNK9QComboBox10isEditableEv')

  def lineEdit(self) -> Optional[QLineEdit]:
    """
    Calls Qt's 'QLineEdit *QComboBox::lineEdit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#lineEdit

    Returns
    -------

    Optional[QLineEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineEdit *QComboBox::lineEdit() const
    address = self.uglySide.call('ritual_ZNK9QComboBox8lineEditEv')
    from . import QLineEdit
    return QLineEdit._cuteAt(address)

  def validator(self) -> Optional[QValidator]:
    """
    Calls Qt's 'const QValidator *QComboBox::validator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#validator

    Returns
    -------

    Optional[QValidator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QValidator *QComboBox::validator() const
    address = self.uglySide.call('ritual_ZNK9QComboBox9validatorEv')
    from ..QtGui import QValidator
    return QValidator._cuteAt(address)

  def completer(self) -> Optional[QCompleter]:
    """
    Calls Qt's 'QCompleter *QComboBox::completer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#completer

    Returns
    -------

    Optional[QCompleter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompleter *QComboBox::completer() const
    address = self.uglySide.call('ritual_ZNK9QComboBox9completerEv')
    from . import QCompleter
    return QCompleter._cuteAt(address)

  def itemDelegate(self) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QComboBox::itemDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#itemDelegate

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QComboBox::itemDelegate() const
    address = self.uglySide.call('ritual_ZNK9QComboBox12itemDelegateEv')
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QComboBox::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QComboBox::model() const
    address = self.uglySide.call('ritual_ZNK9QComboBox5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def rootModelIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QComboBox::rootModelIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#rootModelIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QComboBox::rootModelIndex() const
    address = self.uglySide.call('ritual_ZNK9QComboBox14rootModelIndexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def modelColumn(self) -> int:
    """
    Calls Qt's 'int QComboBox::modelColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#modelColumn
    """
    #  int QComboBox::modelColumn() const
    return self.uglySide.call('ritual_ZNK9QComboBox11modelColumnEv')

  def labelDrawingMode(self) -> LabelDrawingMode:
    """
    Calls Qt's 'LabelDrawingMode QComboBox::labelDrawingMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#labelDrawingMode

    Returns
    -------

    LabelDrawingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelDrawingMode(number)'
      gives.
    """
    #  LabelDrawingMode QComboBox::labelDrawingMode() const
    return QComboBox.LabelDrawingMode(self.uglySide.call(
        'ritual_ZNK9QComboBox16labelDrawingModeEv',
    ))

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QComboBox::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#currentIndex
    """
    #  int QComboBox::currentIndex() const
    return self.uglySide.call('ritual_ZNK9QComboBox12currentIndexEv')

  def currentText(self) -> str:
    """
    Calls Qt's 'QString QComboBox::currentText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#currentText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QComboBox::currentText() const
    return self.uglySide.call('ritual_ZNK9QComboBox11currentTextEv')

  @overload()
  @overload(int)
  def currentData(self, role: int = 256) -> QVariant:
    """
    Calls Qt's 'QVariant QComboBox::currentData(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#currentData

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 256.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QComboBox::currentData(int role) const
    address = self.uglySide.call('ritual_ZNK9QComboBox11currentDataEi', role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def itemText(self, index: int) -> str:
    """
    Calls Qt's 'QString QComboBox::itemText(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#itemText

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QComboBox::itemText(int index) const
    return self.uglySide.call('ritual_ZNK9QComboBox8itemTextEi', index)

  @overload(int)
  def itemIcon(self, index: int) -> QIcon:
    """
    Calls Qt's 'QIcon QComboBox::itemIcon(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#itemIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QComboBox::itemIcon(int index) const
    address = self.uglySide.call('ritual_ZNK9QComboBox8itemIconEi', index)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def itemData(self, index: int, role: int = 256) -> QVariant:
    """
    Calls Qt's 'QVariant QComboBox::itemData(int index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#itemData

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 256.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QComboBox::itemData(int index, int role) const
    address = self.uglySide.call(
        'ritual_ZNK9QComboBox8itemDataEii', index, role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def view(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QComboBox::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#view

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QComboBox::view() const
    address = self.uglySide.call('ritual_ZNK9QComboBox4viewEv')
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QComboBox::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QComboBox::sizeHint() const
    address = self.uglySide.call('ritual_ZNK9QComboBox8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QComboBox::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QComboBox::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK9QComboBox15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, a0: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#inputMethodQuery

    Parameters
    ----------

    a0 : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
    address = self.uglySide.call(
        'ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryE',
        a0.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery
    query, const QVariant &argument) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery query, const
    #      QVariant &argument) const
    address = self.uglySide.call(
        'ritual_ZNK9QComboBox16inputMethodQueryEN2Qt16InputMethodQueryERK8Q'
        'Variant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxVisibleItems(self, maxItems: int) -> None:
    """
    Calls Qt's 'void QComboBox::setMaxVisibleItems(int maxItems)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setMaxVisibleItems

    Parameters
    ----------

    maxItems : int
      Passed on as it is.
    """
    #  void QComboBox::setMaxVisibleItems(int maxItems)
    self.uglySide.call('ritual_ZN9QComboBox18setMaxVisibleItemsEi', maxItems)

  @overload(int)
  def setMaxCount(self, max: int) -> None:
    """
    Calls Qt's 'void QComboBox::setMaxCount(int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setMaxCount

    Parameters
    ----------

    max : int
      Passed on as it is.
    """
    #  void QComboBox::setMaxCount(int max)
    self.uglySide.call('ritual_ZN9QComboBox11setMaxCountEi', max)

  @overload(bool)
  def setDuplicatesEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QComboBox::setDuplicatesEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcombobox.html#setDuplicatesEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QComboBox::setDuplicatesEnabled(bool enable)
    self.uglySide.call('ritual_ZN9QComboBox20setDuplicatesEnabledEb', enable)

  @overload(bool)
  def setFrame(self, a0: bool) -> None:
    """
    Calls Qt's 'void QComboBox::setFrame(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setFrame

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QComboBox::setFrame(bool a0)
    self.uglySide.call('ritual_ZN9QComboBox8setFrameEb', a0)

  @overload(InsertPolicy)
  def setInsertPolicy(self, policy: InsertPolicy) -> None:
    """
    Calls Qt's 'void QComboBox::setInsertPolicy(InsertPolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setInsertPolicy

    Parameters
    ----------

    policy : InsertPolicy
      Passed on as its number.
    """
    #  void QComboBox::setInsertPolicy(InsertPolicy policy)
    self.uglySide.call(
        'ritual_ZN9QComboBox15setInsertPolicyENS_12InsertPolicyE',
        policy.value,
    )

  @overload(SizeAdjustPolicy)
  def setSizeAdjustPolicy(self, policy: SizeAdjustPolicy) -> None:
    """
    Calls Qt's 'void QComboBox::setSizeAdjustPolicy(SizeAdjustPolicy
    policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setSizeAdjustPolicy

    Parameters
    ----------

    policy : SizeAdjustPolicy
      Passed on as its number.
    """
    #  void QComboBox::setSizeAdjustPolicy(SizeAdjustPolicy policy)
    self.uglySide.call(
        'ritual_ZN9QComboBox19setSizeAdjustPolicyENS_16SizeAdjustPolicyE',
        policy.value,
    )

  @overload(int)
  def setMinimumContentsLength(self, characters: int) -> None:
    """
    Calls Qt's 'void QComboBox::setMinimumContentsLength(int characters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcombobox.html#setMinimumContentsLength

    Parameters
    ----------

    characters : int
      Passed on as it is.
    """
    #  void QComboBox::setMinimumContentsLength(int characters)
    self.uglySide.call(
        'ritual_ZN9QComboBox24setMinimumContentsLengthEi', characters,
    )

  @overload(QSize)
  def setIconSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QComboBox::setIconSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setIconSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QComboBox::setIconSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN9QComboBox11setIconSizeERK5QSize', self._valueOf(size),
    )

  @overload(str)
  def setPlaceholderText(self, placeholderText: str) -> None:
    """
    Calls Qt's 'void QComboBox::setPlaceholderText(const QString
    &placeholderText)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setPlaceholderText

    Parameters
    ----------

    placeholderText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QComboBox::setPlaceholderText(const QString &placeholderText)
    self.uglySide.call(
        'ritual_ZN9QComboBox18setPlaceholderTextERK7QString',
        placeholderText,
    )

  @overload(bool)
  def setEditable(self, editable: bool) -> None:
    """
    Calls Qt's 'void QComboBox::setEditable(bool editable)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void QComboBox::setEditable(bool editable)
    self.uglySide.call('ritual_ZN9QComboBox11setEditableEb', editable)

  @overload(QLineEdit)
  @overload(NoneType)
  def setLineEdit(self, edit: Optional[QLineEdit]) -> None:
    """
    Calls Qt's 'void QComboBox::setLineEdit(QLineEdit *edit)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setLineEdit

    Parameters
    ----------

    edit : Optional[QLineEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setLineEdit(QLineEdit *edit)
    self.uglySide.call(
        'ritual_ZN9QComboBox11setLineEditEP9QLineEdit',
        self._addressOf(edit),
    )

  @overload(QValidator)
  @overload(NoneType)
  def setValidator(self, v: Optional[QValidator]) -> None:
    """
    Calls Qt's 'void QComboBox::setValidator(const QValidator *v)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setValidator

    Parameters
    ----------

    v : Optional[QValidator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setValidator(const QValidator *v)
    self.uglySide.call(
        'ritual_ZN9QComboBox12setValidatorEPK10QValidator',
        self._addressOf(v),
    )

  @overload(QCompleter)
  @overload(NoneType)
  def setCompleter(self, c: Optional[QCompleter]) -> None:
    """
    Calls Qt's 'void QComboBox::setCompleter(QCompleter *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setCompleter

    Parameters
    ----------

    c : Optional[QCompleter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setCompleter(QCompleter *c)
    self.uglySide.call(
        'ritual_ZN9QComboBox12setCompleterEP10QCompleter',
        self._addressOf(c),
    )

  @overload(QAbstractItemDelegate)
  @overload(NoneType)
  def setItemDelegate(
      self,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QComboBox::setItemDelegate(QAbstractItemDelegate
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setItemDelegate

    Parameters
    ----------

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setItemDelegate(QAbstractItemDelegate *delegate)
    self.uglySide.call(
        'ritual_ZN9QComboBox15setItemDelegateEP21QAbstractItemDelegate',
        self._addressOf(delegate),
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QComboBox::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN9QComboBox8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QModelIndex)
  def setRootModelIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QComboBox::setRootModelIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setRootModelIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBox::setRootModelIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN9QComboBox17setRootModelIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int)
  def setModelColumn(self, visibleColumn: int) -> None:
    """
    Calls Qt's 'void QComboBox::setModelColumn(int visibleColumn)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setModelColumn

    Parameters
    ----------

    visibleColumn : int
      Passed on as it is.
    """
    #  void QComboBox::setModelColumn(int visibleColumn)
    self.uglySide.call(
        'ritual_ZN9QComboBox14setModelColumnEi', visibleColumn,
    )

  @overload(LabelDrawingMode)
  def setLabelDrawingMode(self, labelDrawing: LabelDrawingMode) -> None:
    """
    Calls Qt's 'void QComboBox::setLabelDrawingMode(LabelDrawingMode
    labelDrawing)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setLabelDrawingMode

    Parameters
    ----------

    labelDrawing : LabelDrawingMode
      Passed on as its number.
    """
    #  void QComboBox::setLabelDrawingMode(LabelDrawingMode labelDrawing)
    self.uglySide.call(
        'ritual_ZN9QComboBox19setLabelDrawingModeENS_16LabelDrawingModeE',
        labelDrawing.value,
    )

  @overload(int, str)
  def setItemText(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QComboBox::setItemText(int index, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setItemText

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QComboBox::setItemText(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN9QComboBox11setItemTextEiRK7QString', index, text,
    )

  @overload(int, QIcon)
  def setItemIcon(self, index: int, icon: QIcon) -> None:
    """
    Calls Qt's 'void QComboBox::setItemIcon(int index, const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setItemIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QComboBox::setItemIcon(int index, const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN9QComboBox11setItemIconEiRK5QIcon',
        index, self._valueOf(icon),
    )

  @overload(int, QVariant)
  @overload(int, QVariant, int)
  def setItemData(
      self,
      index: int,
      value: QVariant,
      role: int = 256,
  ) -> None:
    """
    Calls Qt's 'void QComboBox::setItemData(int index, const QVariant &value,
    int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setItemData

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 256.
    """
    #  void QComboBox::setItemData(int index, const QVariant &value, int
    #      role)
    self.uglySide.call(
        'ritual_ZN9QComboBox11setItemDataEiRK8QVarianti',
        index, self._valueOf(value), role,
    )

  @overload(QAbstractItemView)
  @overload(NoneType)
  def setView(self, itemView: Optional[QAbstractItemView]) -> None:
    """
    Calls Qt's 'void QComboBox::setView(QAbstractItemView *itemView)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setView

    Parameters
    ----------

    itemView : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBox::setView(QAbstractItemView *itemView)
    self.uglySide.call(
        'ritual_ZN9QComboBox7setViewEP17QAbstractItemView',
        self._addressOf(itemView),
    )

  @overload(str)
  def setEditText(self, text: str) -> None:
    """
    Calls Qt's 'void QComboBox::setEditText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setEditText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QComboBox::setEditText(const QString &text)
    self.uglySide.call('ritual_ZN9QComboBox11setEditTextERK7QString', text)

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QComboBox::setCurrentIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QComboBox::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN9QComboBox15setCurrentIndexEi', index)

  @overload(str)
  def setCurrentText(self, text: str) -> None:
    """
    Calls Qt's 'void QComboBox::setCurrentText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#setCurrentText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QComboBox::setCurrentText(const QString &text)
    self.uglySide.call(
        'ritual_ZN9QComboBox14setCurrentTextERK7QString', text,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QComboBox::QComboBox(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#QComboBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QComboBox::QComboBox(QWidget *parent)
    self._noteCreation(QComboBox, lambda: Rituals.call(
        'ritual_ZN9QComboBoxC1EP7QWidget', self._addressOf(parent),
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

  @overload(str)
  @overload(str, QVariant)
  def addItem(self, text: str, userData: Optional[QVariant] = None) -> None:
    """
    Calls Qt's 'void QComboBox::addItem(const QString &text, const QVariant
    &userData)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#addItem

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    userData : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.
    """
    #  void QComboBox::addItem(const QString &text, const QVariant &userData)
    if userData is None:
      from ..QtCore import QVariant
      userData = QVariant()
    self.uglySide.call(
        'ritual_ZN9QComboBox7addItemERK7QStringRK8QVariant',
        text, self._valueOf(userData),
    )

  @overload(QIcon, str)
  @overload(QIcon, str, QVariant)
  def addItem(
      self,
      icon: QIcon,
      text: str,
      userData: Optional[QVariant] = None,
  ) -> None:
    """
    Calls Qt's 'void QComboBox::addItem(const QIcon &icon, const QString
    &text, const QVariant &userData)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#addItem

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    userData : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.
    """
    #  void QComboBox::addItem(const QIcon &icon, const QString &text, const
    #      QVariant &userData)
    if userData is None:
      from ..QtCore import QVariant
      userData = QVariant()
    self.uglySide.call(
        'ritual_ZN9QComboBox7addItemERK5QIconRK7QStringRK8QVariant',
        self._valueOf(icon), text, self._valueOf(userData),
    )

  @overload(int, str)
  @overload(int, str, QVariant)
  def insertItem(
      self,
      index: int,
      text: str,
      userData: Optional[QVariant] = None,
  ) -> None:
    """
    Calls Qt's 'void QComboBox::insertItem(int index, const QString &text,
    const QVariant &userData)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    userData : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.
    """
    #  void QComboBox::insertItem(int index, const QString &text, const
    #      QVariant &userData)
    if userData is None:
      from ..QtCore import QVariant
      userData = QVariant()
    self.uglySide.call(
        'ritual_ZN9QComboBox10insertItemEiRK7QStringRK8QVariant',
        index, text, self._valueOf(userData),
    )

  @overload(int, QIcon, str)
  @overload(int, QIcon, str, QVariant)
  def insertItem(
      self,
      index: int,
      icon: QIcon,
      text: str,
      userData: Optional[QVariant] = None,
  ) -> None:
    """
    Calls Qt's 'void QComboBox::insertItem(int index, const QIcon &icon,
    const QString &text, const QVariant &userData)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    userData : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.
    """
    #  void QComboBox::insertItem(int index, const QIcon &icon, const QString
    #      &text, const QVariant &userData)
    if userData is None:
      from ..QtCore import QVariant
      userData = QVariant()
    self.uglySide.call(
        'ritual_ZN9QComboBox10insertItemEiRK5QIconRK7QStringRK8QVariant',
        index, self._valueOf(icon), text, self._valueOf(userData),
    )

  @overload(int)
  def insertSeparator(self, index: int) -> None:
    """
    Calls Qt's 'void QComboBox::insertSeparator(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#insertSeparator

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QComboBox::insertSeparator(int index)
    self.uglySide.call('ritual_ZN9QComboBox15insertSeparatorEi', index)

  @overload(int)
  def removeItem(self, index: int) -> None:
    """
    Calls Qt's 'void QComboBox::removeItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#removeItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QComboBox::removeItem(int index)
    self.uglySide.call('ritual_ZN9QComboBox10removeItemEi', index)

  def showPopup(self) -> None:
    """
    Calls Qt's 'void QComboBox::showPopup()'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#showPopup
    """
    #  void QComboBox::showPopup()
    self.uglySide.call('ritual_ZN9QComboBox9showPopupEv')

  def hidePopup(self) -> None:
    """
    Calls Qt's 'void QComboBox::hidePopup()'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#hidePopup
    """
    #  void QComboBox::hidePopup()
    self.uglySide.call('ritual_ZN9QComboBox9hidePopupEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QComboBox::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QComboBox::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN9QComboBox5eventEP6QEvent', self._addressOf(event),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QComboBox::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#clear
    """
    #  void QComboBox::clear()
    self.uglySide.call('ritual_ZN9QComboBox5clearEv')

  def clearEditText(self) -> None:
    """
    Calls Qt's 'void QComboBox::clearEditText()'.

    Qt's own words: https://doc.qt.io/qt-6/qcombobox.html#clearEditText
    """
    #  void QComboBox::clearEditText()
    self.uglySide.call('ritual_ZN9QComboBox13clearEditTextEv')
