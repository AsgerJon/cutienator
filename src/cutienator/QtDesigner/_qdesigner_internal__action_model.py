"""
qdesigner_internal::ActionModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QStringList
from ..QtGui import QStandardItemModel
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex
  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import QDesignerFormEditorInterface, QDesignerPropertySheetExtension
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerPropertySheetExtension = WAIT['QDesignerPropertySheetExtension']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionModel(QStandardItemModel):
  """
  The cute side of Qt's qdesigner_internal::ActionModel: a plain Python
  object standing in front of one C++ qdesigner_internal::ActionModel.

  It is built on the cute 'QStandardItemModel', as Qt's
  qdesigner_internal::ActionModel is built on Qt's QStandardItemModel, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionModel that has a ritual
  and that Python can call so far, 17 names in all: 'metaObject', 'tr',
  'initialize', 'clearActions', 'addAction', 'remove', 'update',
  'findAction', 'actionName', 'actionAt', 'indexOf', 'mimeData', 'mimeTypes',
  'dropMimeData', 'associatedWidgets', 'actionShortCut',
  'resourceImageDropped'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ActionModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ActionModel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    qdesigner_internal::ActionModel::setItems(QDesignerFormEditorInterface
    *core, QAction *a, const QIcon &defaultIcon, QStandardItemList &sl)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionModel is created at the first use, not
    by 'qdesigner_internal::ActionModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ActionModel.
  - Qt tells when it has removed the C++ qdesigner_internal::ActionModel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ActionModel that has no cute
    function yet, 'setItems', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::ActionModel, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Columns(CuteNum):
    """
    The enum 'qdesigner_internal::ActionModel::Columns' of Qt, with the 8
    names Qt gives in it.
    """

    NameColumn = Kee[int](0)
    UsedColumn = Kee[int](1)
    TextColumn = Kee[int](2)
    ShortCutColumn = Kee[int](3)
    CheckedColumn = Kee[int](4)
    ToolTipColumn = Kee[int](5)
    MenuRoleColumn = Kee[int](6)
    NumColumns = Kee[int](7)

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
    Calls Qt's 'QString qdesigner_internal::ActionModel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#tr

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
    #  QString qdesigner_internal::ActionModel::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal11ActionModel2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QAction)
  @overload(NoneType)
  def associatedWidgets(action: Optional[QAction]) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::ActionModel::associatedWidgets(const QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::ActionModel::associatedWidgets(const
    #      QAction *action)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal11ActionModel17associatedWidgetsEPK7Q'
        'Action',
        CuteMixin._addressOf(action),
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  @staticmethod
  @overload(QDesignerFormEditorInterface, QAction)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def actionShortCut(
      core: Optional[QDesignerFormEditorInterface],
      action: Optional[QAction],
  ) -> qdesigner_internal.PropertySheetKeySequenceValue:
    """
    Calls Qt's 'PropertySheetKeySequenceValue
    qdesigner_internal::ActionModel::actionShortCut(
    QDesignerFormEditorInterface *core, QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#actionShortCut

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    qdesigner_internal.PropertySheetKeySequenceValue
      A new cute qdesigner_internal::PropertySheetKeySequenceValue around the
      copy Qt gave back. Python owns it.
    """
    #  PropertySheetKeySequenceValue
    #      qdesigner_internal::ActionModel::actionShortCut(
    #      QDesignerFormEditorInterface *core, QAction *action)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal11ActionModel14actionShortCutEP28QDes'
        'ignerFormEditorInterfaceP7QAction',
        CuteMixin._addressOf(core), CuteMixin._addressOf(action),
    )
    return qdesigner_internal.PropertySheetKeySequenceValue._cuteOwning(address)

  @staticmethod
  @overload(QDesignerPropertySheetExtension)
  @overload(NoneType)
  def actionShortCut(
      ps: Optional[QDesignerPropertySheetExtension],
  ) -> qdesigner_internal.PropertySheetKeySequenceValue:
    """
    Calls Qt's 'PropertySheetKeySequenceValue
    qdesigner_internal::ActionModel::actionShortCut(const
    QDesignerPropertySheetExtension *ps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#actionShortCut

    Parameters
    ----------

    ps : Optional[QDesignerPropertySheetExtension]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    qdesigner_internal.PropertySheetKeySequenceValue
      A new cute qdesigner_internal::PropertySheetKeySequenceValue around the
      copy Qt gave back. Python owns it.
    """
    #  PropertySheetKeySequenceValue
    #      qdesigner_internal::ActionModel::actionShortCut(const
    #      QDesignerPropertySheetExtension *ps)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal11ActionModel14actionShortCutEPK31QDe'
        'signerPropertySheetExtension',
        CuteMixin._addressOf(ps, 'QDesignerPropertySheetExtension'),
    )
    return qdesigner_internal.PropertySheetKeySequenceValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::ActionModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ActionModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def findAction(self, a0: Optional[QAction]) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ActionModel::findAction(QAction *a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#findAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::ActionModel::findAction(QAction *a0) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel10findActionEP7QAction',
        self._addressOf(a0),
    )

  @overload(int)
  def actionName(self, row: int) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::ActionModel::actionName(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#actionName

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::ActionModel::actionName(int row) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel10actionNameEi', row,
    )

  @overload(QModelIndex)
  def actionAt(self, index: QModelIndex) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *qdesigner_internal::ActionModel::actionAt(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#actionAt

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ActionModel::actionAt(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel8actionAtERK11QModelInd'
        'ex',
        self._valueOf(index),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def indexOf(self, a: Optional[QAction]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex qdesigner_internal::ActionModel::indexOf(QAction
    *a) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#indexOf

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex qdesigner_internal::ActionModel::indexOf(QAction *a) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel7indexOfEP7QAction',
        self._addressOf(a),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *qdesigner_internal::ActionModel::mimeData(const
    QModelIndexList &indexes) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#mimeData

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *qdesigner_internal::ActionModel::mimeData(const
    #      QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel8mimeDataERK5QListI11QM'
        'odelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList qdesigner_internal::ActionModel::mimeTypes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::ActionModel::mimeTypes() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11ActionModel9mimeTypesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'qdesigner_internal::ActionModel::ActionModel(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#ActionModel

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::ActionModel::ActionModel(QWidget *parent)
    self._noteCreation(ActionModel, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal11ActionModelC1EP7QWidget',
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def initialize(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionModel::initialize(QDesignerFormEditorInterface
    *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#initialize

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionModel::initialize(
    #      QDesignerFormEditorInterface *core)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel10initializeEP28QDesigne'
        'rFormEditorInterface',
        self._addressOf(core),
    )

  def clearActions(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionModel::clearActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#clearActions
    """
    #  void qdesigner_internal::ActionModel::clearActions()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel12clearActionsEv',
    )

  @overload(QAction)
  @overload(NoneType)
  def addAction(self, a: Optional[QAction]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    qdesigner_internal::ActionModel::addAction(QAction *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#addAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex qdesigner_internal::ActionModel::addAction(QAction *a)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel9addActionEP7QAction',
        self._addressOf(a),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def remove(self, row: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionModel::remove(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#remove

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionModel::remove(int row)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel6removeEi', row,
    )

  @overload(int)
  def update(self, row: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionModel::update(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#update

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionModel::update(int row)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel6updateEi', row,
    )

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def dropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ActionModel::dropMimeData(const
    QMimeData *data, Qt::DropAction action, int row, int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html#dropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool qdesigner_internal::ActionModel::dropMimeData(const QMimeData
    #      *data, Qt::DropAction action, int row, int column, const
    #      QModelIndex &parent)
    ritual = (
        'ritual_ZN18qdesigner_internal11ActionModel12dropMimeDataEPK9QMimeD'
        'ataN2Qt10DropActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal11ActionModel12dropMimeDataEPK9'
          'QMimeDataN2Qt10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(str, QAction)
  @overload(str, NoneType)
  def resourceImageDropped(
      self,
      path: str,
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionModel::resourceImageDropped(const QString
    &path, QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionmodel.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionModel::resourceImageDropped(const
    #      QString &path, QAction *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11ActionModel20resourceImageDroppedER'
        'K7QStringP7QAction',
        path, self._addressOf(action),
    )

  @staticmethod
  def setItems(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::ActionModel::setItems(QDesignerFormEditorInterface
    *core, QAction *a, const QIcon &defaultIcon, QStandardItemList &sl)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionModel.setItems' has no cute function "
        "yet. Qt's 'void "
        "qdesigner_internal::ActionModel::setItems(QDesignerFormEditorInterf"
        "ace *core, QAction *a, const QIcon &defaultIcon, QStandardItemList "
        "&sl)': takes a type Python has no way to hand over yet.")
