"""
qdesigner_internal::PromotionModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/promotionmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PromotionModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtGui import QStandardItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
  from ..QtGui import QStandardItem
  from . import QDesignerWidgetDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerWidgetDataBaseItemInterface = WAIT['QDesignerWidgetDataBaseItemInterface']
  QModelIndex = WAIT['QModelIndex']
  QStandardItem = WAIT['QStandardItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PromotionModel(QStandardItemModel):
  """
  The cute side of Qt's qdesigner_internal::PromotionModel: a plain Python
  object standing in front of one C++ qdesigner_internal::PromotionModel.

  It is built on the cute 'QStandardItemModel', as Qt's
  qdesigner_internal::PromotionModel is built on Qt's QStandardItemModel, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PromotionModel that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'modelData',
  'includeFileChanged', 'classNameChanged', 'slotItemChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::PromotionModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::PromotionModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 3 leans on 'qdesigner_internal; 2 not a
  gap; 2 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ qdesigner_internal::PromotionModel is created at the first use,
    not by 'qdesigner_internal::PromotionModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::PromotionModel.
  - Qt tells when it has removed the C++ qdesigner_internal::PromotionModel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::PromotionModel that has no cute
    function yet, '__init__', 'indexOfClass', 'initializeHeaders',
    'updateFromWidgetDatabase', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside qdesigner_internal::PromotionModel, each a
  #  class in here as in C++.

  class ModelData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's qdesigner_internal::PromotionModel::ModelData: a
    plain Python object standing in front of one C++
    qdesigner_internal::PromotionModel::ModelData.

    C++ hands a qdesigner_internal::PromotionModel::ModelData around as a
    copy, so every C++ qdesigner_internal::PromotionModel::ModelData behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's qdesigner_internal::PromotionModel::ModelData that
    has a ritual and that Python can call so far, 1 name in all: 'isValid'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'qdesigner_internal::PromotionModel::ModelData::~ModelData()': the
      destructor: Python removes its C++
      qdesigner_internal::PromotionModel::ModelData by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ qdesigner_internal::PromotionModel::ModelData is created at the
      first use, not by 'qdesigner_internal::PromotionModel::ModelData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a qdesigner_internal::PromotionModel::ModelData back
      gives a copy the ritual made for Python, in a new cute
      qdesigner_internal::PromotionModel::ModelData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'qdesigner_internal::PromotionModel::ModelData'

    #  Qt's '~qdesigner_internal::PromotionModel::ModelData()'. Naming it
    #  makes this a value class: Python owns every C++
    #  qdesigner_internal::PromotionModel::ModelData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18qdesigner_internal14PromotionModel9ModelDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool
      qdesigner_internal::PromotionModel::ModelData::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel-modeldata.html
      """
      #  bool qdesigner_internal::PromotionModel::ModelData::isValid() const
      return self.uglySide.call(
          'ritual_ZNK18qdesigner_internal14PromotionModel9ModelData7isValid'
          'Ev',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PromotionModel'

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
    *qdesigner_internal::PromotionModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::PromotionModel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14PromotionModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def modelData(self, index: QModelIndex) -> ModelData:
    """
    Calls Qt's 'ModelData qdesigner_internal::PromotionModel::modelData(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html#modelData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    ModelData
      A new cute qdesigner_internal::PromotionModel::ModelData around the
      copy Qt gave back. Python owns it.
    """
    #  ModelData qdesigner_internal::PromotionModel::modelData(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14PromotionModel9modelDataERK11QMode'
        'lIndex',
        self._valueOf(index),
    )
    return qdesigner_internal.PromotionModel.ModelData._cuteOwning(address)

  @overload(QStandardItem)
  @overload(NoneType)
  def modelData(self, item: Optional[QStandardItem]) -> ModelData:
    """
    Calls Qt's 'ModelData qdesigner_internal::PromotionModel::modelData(const
    QStandardItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html#modelData

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ModelData
      A new cute qdesigner_internal::PromotionModel::ModelData around the
      copy Qt gave back. Python owns it.
    """
    #  ModelData qdesigner_internal::PromotionModel::modelData(const
    #      QStandardItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14PromotionModel9modelDataEPK13QStan'
        'dardItem',
        self._addressOf(item),
    )
    return qdesigner_internal.PromotionModel.ModelData._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::PromotionModel::PromotionModel(
    QDesignerFormEditorInterface *core)': leans on
    'qdesigner_internal::PromotionModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionModel.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::PromotionModel::PromotionModel(QDesignerFormEd"
        "itorInterface *core)': leans on "
        "'qdesigner_internal::PromotionModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QDesignerWidgetDataBaseItemInterface, str)
  @overload(NoneType, str)
  def includeFileChanged(
      self,
      a0: Optional[QDesignerWidgetDataBaseItemInterface],
      includeFile: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionModel::includeFileChanged(
    QDesignerWidgetDataBaseItemInterface *a0, const QString &includeFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html

    Parameters
    ----------

    a0 : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    includeFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionModel::includeFileChanged(
    #      QDesignerWidgetDataBaseItemInterface *a0, const QString
    #      &includeFile)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PromotionModel18includeFileChangedE'
        'P36QDesignerWidgetDataBaseItemInterfaceRK7QString',
        self._addressOf(a0), includeFile,
    )

  @overload(QDesignerWidgetDataBaseItemInterface, str)
  @overload(NoneType, str)
  def classNameChanged(
      self,
      a0: Optional[QDesignerWidgetDataBaseItemInterface],
      newName: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionModel::classNameChanged(
    QDesignerWidgetDataBaseItemInterface *a0, const QString &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html

    Parameters
    ----------

    a0 : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionModel::classNameChanged(
    #      QDesignerWidgetDataBaseItemInterface *a0, const QString &newName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PromotionModel16classNameChangedEP3'
        '6QDesignerWidgetDataBaseItemInterfaceRK7QString',
        self._addressOf(a0), newName,
    )

  @overload(QStandardItem)
  @overload(NoneType)
  def slotItemChanged(self, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionModel::slotItemChanged(QStandardItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotionmodel.html

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PromotionModel::slotItemChanged(QStandardItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PromotionModel15slotItemChangedEP13'
        'QStandardItem',
        self._addressOf(item),
    )

  @staticmethod
  def indexOfClass(*__, **_) -> Never:
    """
    Qt's 'QModelIndex qdesigner_internal::PromotionModel::indexOfClass(const
    QString &className) const': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: unknown type name
    'StandardItemList'; did you mean 'QStandardItem'?.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionModel.indexOfClass' has no cute "
        "function yet. Qt's 'QModelIndex "
        "qdesigner_internal::PromotionModel::indexOfClass(const QString "
        "&className) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: unknown type "
        "name 'StandardItemList'; did you mean 'QStandardItem'?.")

  @staticmethod
  def initializeHeaders(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::PromotionModel::initializeHeaders()':
    leans on 'qdesigner_internal::PromotionModel::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionModel.initializeHeaders' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::PromotionModel::initializeHeaders()': leans on "
        "'qdesigner_internal::PromotionModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateFromWidgetDatabase(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::PromotionModel::updateFromWidgetDatabase()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no member named 'constFirst' in 'QStandardItem'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionModel.updateFromWidgetDatabase' has "
        "no cute function yet. Qt's 'void "
        "qdesigner_internal::PromotionModel::updateFromWidgetDatabase()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no member named 'constFirst' in "
        "'QStandardItem'.")
