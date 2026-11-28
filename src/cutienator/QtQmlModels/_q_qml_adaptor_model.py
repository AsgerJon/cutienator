"""
QQmlAdaptorModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlAdaptorModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QByteArray, QTypeRevision
  from ..QtCore import QVariant
  from ..QtQml import QQmlGuardImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlGuardImpl = WAIT['QQmlGuardImpl']
  QTypeRevision = WAIT['QTypeRevision']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAdaptorModel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAdaptorModel: a plain Python object standing in
  front of one C++ QQmlAdaptorModel.

  What exists
  -----------

  Every function of Qt's QQmlAdaptorModel that has a ritual and that Python
  can call so far, 21 names in all: 'model', 'setModel', 'invalidateModel',
  'isValid', 'count', 'rowCount', 'columnCount', 'rowAt', 'columnAt',
  'indexAt', 'useImportVersion', 'adaptsAim', 'aim', 'value',
  'hasProxyObject', 'replaceWatchedRoles', 'modelIndex', 'parentModelIndex',
  'canFetchMore', 'fetchMore', 'objectDestroyedImpl'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAdaptorModel::~QQmlAdaptorModel()': the destructor: Python
    never removes a C++ QQmlAdaptorModel.
  - Qt's 'const QAbstractItemModel *QQmlAdaptorModel::aim() const': takes in
    Python what 'QAbstractItemModel *QQmlAdaptorModel::aim()' takes.
  - Qt's 'QQmlDelegateModelItem *QQmlAdaptorModel::createItem(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, int index)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlAdaptorModel::notify(const QList<QQmlDelegateModelItem *>
    &items, int index, int count, const QList<int> &roles) const': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlAdaptorModel is created at the first use, not by
    'QQmlAdaptorModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAdaptorModel.
  - Each name of Qt's QQmlAdaptorModel that has no cute function yet,
    'createItem', 'notify', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlAdaptorModel, each a class in here as
  #  in C++.

  class Accessors(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlAdaptorModel::Accessors: a plain Python object
    standing in front of one C++ QQmlAdaptorModel::Accessors.

    What exists
    -----------

    No function of Qt's QQmlAdaptorModel::Accessors yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlAdaptorModel::Accessors::~Accessors()': the destructor:
      Python never removes a C++ QQmlAdaptorModel::Accessors.
    - Qt's 'int QQmlAdaptorModel::Accessors::rowCount(const QQmlAdaptorModel
      &a0) const': takes a type Python has no way to hand over yet.
    - Qt's 'int QQmlAdaptorModel::Accessors::columnCount(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
    - Qt's 'void QQmlAdaptorModel::Accessors::cleanup(QQmlAdaptorModel &a0)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'QVariant QQmlAdaptorModel::Accessors::value(const
      QQmlAdaptorModel &a0, int a1, const QString &a2) const': takes a type
      Python has no way to hand over yet.
    - Qt's 'QQmlDelegateModelItem
      *QQmlAdaptorModel::Accessors::createItem(QQmlAdaptorModel &a0, const
      QQmlRefPointer<QQmlDelegateModelItemMetaType> &a1, int a2, int a3, int
      a4)': takes a type Python has no way to hand over yet.
    - Qt's 'bool QQmlAdaptorModel::Accessors::notify(const QQmlAdaptorModel
      &a0, const QList<QQmlDelegateModelItem *> &a1, int a2, int a3, const
      QList<int> &a4) const': takes a type Python has no way to hand over
      yet.
    - Qt's 'void
      QQmlAdaptorModel::Accessors::replaceWatchedRoles(QQmlAdaptorModel &a0,
      const QList<QByteArray> &a1, const QList<QByteArray> &a2) const': takes
      a type Python has no way to hand over yet.
    - Qt's 'QVariant QQmlAdaptorModel::Accessors::parentModelIndex(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
    - Qt's 'QVariant QQmlAdaptorModel::Accessors::modelIndex(const
      QQmlAdaptorModel &a0, int a1) const': takes a type Python has no way to
      hand over yet.
    - Qt's 'bool QQmlAdaptorModel::Accessors::canFetchMore(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
    - Qt's 'void QQmlAdaptorModel::Accessors::fetchMore(QQmlAdaptorModel &a0)
      const': takes a type Python has no way to hand over yet.

    What to expect
    --------------

    - The C++ QQmlAdaptorModel::Accessors is created at the first use, not by
      'QQmlAdaptorModel::Accessors(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlAdaptorModel::Accessors.
    - Each name of Qt's QQmlAdaptorModel::Accessors that has no cute function
      yet, 'canFetchMore', 'cleanup', 'columnCount', 'createItem',
      'fetchMore', 'modelIndex', 'notify', 'parentModelIndex',
      'replaceWatchedRoles', 'rowCount', 'value', holds a function that
      raises 'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlAdaptorModel::Accessors'

    #  The functions Qt calls itself that QQmlAdaptorModel::Accessors is the
    #  first to declare and that cannot be handed to Python yet, each as Qt
    #  declares it. A class of a program that writes one of them anew is
    #  refused, since Qt would never call what it wrote; see
    #  'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'rowCount': (
            'int QQmlAdaptorModel::Accessors::rowCount(const '
            'QQmlAdaptorModel &) const',
        ),
        'columnCount': (
            'int QQmlAdaptorModel::Accessors::columnCount(const '
            'QQmlAdaptorModel &) const',
        ),
        'cleanup': (
            'void QQmlAdaptorModel::Accessors::cleanup(QQmlAdaptorModel &) '
            'const',
        ),
        'value': (
            'QVariant QQmlAdaptorModel::Accessors::value(const '
            'QQmlAdaptorModel &, int, const QString &) const',
        ),
        'createItem': (
            'QQmlDelegateModelItem '
            '*QQmlAdaptorModel::Accessors::createItem(QQmlAdaptorModel &, '
            'const QQmlRefPointer<QQmlDelegateModelItemMetaType> &, int, '
            'int, int)',
        ),
        'notify': (
            'bool QQmlAdaptorModel::Accessors::notify(const '
            'QQmlAdaptorModel &, const QList<QQmlDelegateModelItem *> &, '
            'int, int, const QList<int> &) const',
        ),
        'replaceWatchedRoles': (
            'void '
            'QQmlAdaptorModel::Accessors::replaceWatchedRoles(QQmlAdaptorMo'
            'del &, const QList<QByteArray> &, const QList<QByteArray> &) '
            'const',
        ),
        'parentModelIndex': (
            'QVariant QQmlAdaptorModel::Accessors::parentModelIndex(const '
            'QQmlAdaptorModel &) const',
        ),
        'modelIndex': (
            'QVariant QQmlAdaptorModel::Accessors::modelIndex(const '
            'QQmlAdaptorModel &, int) const',
        ),
        'canFetchMore': (
            'bool QQmlAdaptorModel::Accessors::canFetchMore(const '
            'QQmlAdaptorModel &) const',
        ),
        'fetchMore': (
            'void QQmlAdaptorModel::Accessors::fetchMore(QQmlAdaptorModel '
            '&) const',
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlAdaptorModel::Accessors::Accessors()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmladaptormodel-accessors.html#Accessors
      """
      #  QQmlAdaptorModel::Accessors::Accessors()
      self._noteCreation(QQmlAdaptorModel.Accessors, lambda: Rituals.call(
          'ritual_ZN16QQmlAdaptorModel9AccessorsC1Ev',
      ))

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

    @staticmethod
    def canFetchMore(*__, **_) -> Never:
      """
      Qt's 'bool QQmlAdaptorModel::Accessors::canFetchMore(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.canFetchMore' has no cute function "
          "yet. Qt's 'bool QQmlAdaptorModel::Accessors::canFetchMore(const "
          "QQmlAdaptorModel &a0) const': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def cleanup(*__, **_) -> Never:
      """
      Qt's 'void QQmlAdaptorModel::Accessors::cleanup(QQmlAdaptorModel &a0)
      const': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.cleanup' has no cute function yet. "
          "Qt's 'void QQmlAdaptorModel::Accessors::cleanup(QQmlAdaptorModel "
          "&a0) const': takes a type Python has no way to hand over yet.")

    @staticmethod
    def columnCount(*__, **_) -> Never:
      """
      Qt's 'int QQmlAdaptorModel::Accessors::columnCount(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.columnCount' has no cute function "
          "yet. Qt's 'int QQmlAdaptorModel::Accessors::columnCount(const "
          "QQmlAdaptorModel &a0) const': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def createItem(*__, **_) -> Never:
      """
      Qt's 'QQmlDelegateModelItem
      *QQmlAdaptorModel::Accessors::createItem(QQmlAdaptorModel &a0, const
      QQmlRefPointer<QQmlDelegateModelItemMetaType> &a1, int a2, int a3, int
      a4)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.createItem' has no cute function "
          "yet. Qt's 'QQmlDelegateModelItem "
          "*QQmlAdaptorModel::Accessors::createItem(QQmlAdaptorModel &a0, "
          "const QQmlRefPointer<QQmlDelegateModelItemMetaType> &a1, int a2, "
          "int a3, int a4)': takes a type Python has no way to hand over "
          "yet.")

    @staticmethod
    def fetchMore(*__, **_) -> Never:
      """
      Qt's 'void QQmlAdaptorModel::Accessors::fetchMore(QQmlAdaptorModel &a0)
      const': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.fetchMore' has no cute function yet. "
          "Qt's 'void "
          "QQmlAdaptorModel::Accessors::fetchMore(QQmlAdaptorModel &a0) "
          "const': takes a type Python has no way to hand over yet.")

    @staticmethod
    def modelIndex(*__, **_) -> Never:
      """
      Qt's 'QVariant QQmlAdaptorModel::Accessors::modelIndex(const
      QQmlAdaptorModel &a0, int a1) const': takes a type Python has no way to
      hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.modelIndex' has no cute function "
          "yet. Qt's 'QVariant "
          "QQmlAdaptorModel::Accessors::modelIndex(const QQmlAdaptorModel "
          "&a0, int a1) const': takes a type Python has no way to hand over "
          "yet.")

    @staticmethod
    def notify(*__, **_) -> Never:
      """
      Qt's 'bool QQmlAdaptorModel::Accessors::notify(const QQmlAdaptorModel
      &a0, const QList<QQmlDelegateModelItem *> &a1, int a2, int a3, const
      QList<int> &a4) const': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.notify' has no cute function yet. "
          "Qt's 'bool QQmlAdaptorModel::Accessors::notify(const "
          "QQmlAdaptorModel &a0, const QList<QQmlDelegateModelItem *> &a1, "
          "int a2, int a3, const QList<int> &a4) const': takes a type "
          "Python has no way to hand over yet.")

    @staticmethod
    def parentModelIndex(*__, **_) -> Never:
      """
      Qt's 'QVariant QQmlAdaptorModel::Accessors::parentModelIndex(const
      QQmlAdaptorModel &a0) const': takes a type Python has no way to hand
      over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.parentModelIndex' has no cute "
          "function yet. Qt's 'QVariant "
          "QQmlAdaptorModel::Accessors::parentModelIndex(const "
          "QQmlAdaptorModel &a0) const': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def replaceWatchedRoles(*__, **_) -> Never:
      """
      Qt's 'void
      QQmlAdaptorModel::Accessors::replaceWatchedRoles(QQmlAdaptorModel &a0,
      const QList<QByteArray> &a1, const QList<QByteArray> &a2) const': takes
      a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.replaceWatchedRoles' has no cute "
          "function yet. Qt's 'void "
          "QQmlAdaptorModel::Accessors::replaceWatchedRoles(QQmlAdaptorModel"
          " &a0, const QList<QByteArray> &a1, const QList<QByteArray> &a2) "
          "const': takes a type Python has no way to hand over yet.")

    @staticmethod
    def rowCount(*__, **_) -> Never:
      """
      Qt's 'int QQmlAdaptorModel::Accessors::rowCount(const QQmlAdaptorModel
      &a0) const': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.rowCount' has no cute function yet. "
          "Qt's 'int QQmlAdaptorModel::Accessors::rowCount(const "
          "QQmlAdaptorModel &a0) const': takes a type Python has no way to "
          "hand over yet.")

    @staticmethod
    def value(*__, **_) -> Never:
      """
      Qt's 'QVariant QQmlAdaptorModel::Accessors::value(const
      QQmlAdaptorModel &a0, int a1, const QString &a2) const': takes a type
      Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlAdaptorModel.Accessors.value' has no cute function yet. "
          "Qt's 'QVariant QQmlAdaptorModel::Accessors::value(const "
          "QQmlAdaptorModel &a0, int a1, const QString &a2) const': takes a "
          "type Python has no way to hand over yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlGuardImpl)
  @overload(NoneType)
  def objectDestroyedImpl(a0: Optional[QQmlGuardImpl]) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::objectDestroyedImpl(QQmlGuardImpl
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#objectDestroyedImpl

    Parameters
    ----------

    a0 : Optional[QQmlGuardImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlAdaptorModel::objectDestroyedImpl(QQmlGuardImpl *a0)
    Rituals.call(
        'ritual_ZN16QQmlAdaptorModel19objectDestroyedImplEP13QQmlGuardImpl',
        CuteMixin._addressOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAdaptorModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAdaptorModel::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAdaptorModel::model() const
    address = self.uglySide.call('ritual_ZNK16QQmlAdaptorModel5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlAdaptorModel::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#isValid
    """
    #  bool QQmlAdaptorModel::isValid() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel7isValidEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#count
    """
    #  int QQmlAdaptorModel::count() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel5countEv')

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#rowCount
    """
    #  int QQmlAdaptorModel::rowCount() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#columnCount
    """
    #  int QQmlAdaptorModel::columnCount() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel11columnCountEv')

  @overload(int)
  def rowAt(self, index: int) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::rowAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#rowAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QQmlAdaptorModel::rowAt(int index) const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel5rowAtEi', index)

  @overload(int)
  def columnAt(self, index: int) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::columnAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#columnAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QQmlAdaptorModel::columnAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel8columnAtEi', index,
    )

  @overload(int, int)
  def indexAt(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QQmlAdaptorModel::indexAt(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#indexAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QQmlAdaptorModel::indexAt(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel7indexAtEii', row, column,
    )

  def adaptsAim(self) -> bool:
    """
    Calls Qt's 'bool QQmlAdaptorModel::adaptsAim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#adaptsAim
    """
    #  bool QQmlAdaptorModel::adaptsAim() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel9adaptsAimEv')

  @overload(int, str)
  def value(self, index: int, role: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAdaptorModel::value(int index, const QString
    &role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAdaptorModel::value(int index, const QString &role) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel5valueEiRK7QString', index, role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def hasProxyObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlAdaptorModel::hasProxyObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#hasProxyObject
    """
    #  bool QQmlAdaptorModel::hasProxyObject() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel14hasProxyObjectEv',
    )

  @overload(int)
  def modelIndex(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAdaptorModel::modelIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#modelIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAdaptorModel::modelIndex(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel10modelIndexEi', index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def parentModelIndex(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAdaptorModel::parentModelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#parentModelIndex

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAdaptorModel::parentModelIndex() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlAdaptorModel16parentModelIndexEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def canFetchMore(self) -> bool:
    """
    Calls Qt's 'bool QQmlAdaptorModel::canFetchMore() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#canFetchMore
    """
    #  bool QQmlAdaptorModel::canFetchMore() const
    return self.uglySide.call('ritual_ZNK16QQmlAdaptorModel12canFetchMoreEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, variant: QVariant) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::setModel(const QVariant &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#setModel

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlAdaptorModel::setModel(const QVariant &variant)
    self.uglySide.call(
        'ritual_ZN16QQmlAdaptorModel8setModelERK8QVariant',
        self._valueOf(variant),
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
    Notes what was given, for Qt's 'QQmlAdaptorModel::QQmlAdaptorModel()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#QQmlAdaptorModel
    """
    #  QQmlAdaptorModel::QQmlAdaptorModel()
    self._noteCreation(QQmlAdaptorModel, lambda: Rituals.call(
        'ritual_ZN16QQmlAdaptorModelC1Ev',
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

  def invalidateModel(self) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::invalidateModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#invalidateModel
    """
    #  void QQmlAdaptorModel::invalidateModel()
    self.uglySide.call('ritual_ZN16QQmlAdaptorModel15invalidateModelEv')

  @overload(QTypeRevision)
  def useImportVersion(self, revision: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::useImportVersion(QTypeRevision
    revision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#useImportVersion

    Parameters
    ----------

    revision : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlAdaptorModel::useImportVersion(QTypeRevision revision)
    self.uglySide.call(
        'ritual_ZN16QQmlAdaptorModel16useImportVersionE13QTypeRevision',
        self._valueOf(revision),
    )

  def aim(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQmlAdaptorModel::aim()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#aim

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlAdaptorModel::aim()
    address = self.uglySide.call('ritual_ZN16QQmlAdaptorModel3aimEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @overload(QList[QByteArray], QList[QByteArray])
  def replaceWatchedRoles(
      self,
      oldRoles: QList[QByteArray],
      newRoles: QList[QByteArray],
  ) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::replaceWatchedRoles(const
    QList<QByteArray> &oldRoles, const QList<QByteArray> &newRoles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodel.html#replaceWatchedRoles

    Parameters
    ----------

    oldRoles : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newRoles : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlAdaptorModel::replaceWatchedRoles(const QList<QByteArray>
    #      &oldRoles, const QList<QByteArray> &newRoles)
    self.uglySide.call(
        'ritual_ZN16QQmlAdaptorModel19replaceWatchedRolesERK5QListI10QByteA'
        'rrayES4_',
        self._valueOf(oldRoles), self._valueOf(newRoles),
    )

  def fetchMore(self) -> None:
    """
    Calls Qt's 'void QQmlAdaptorModel::fetchMore()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmladaptormodel.html#fetchMore
    """
    #  void QQmlAdaptorModel::fetchMore()
    self.uglySide.call('ritual_ZN16QQmlAdaptorModel9fetchMoreEv')

  @staticmethod
  def createItem(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModelItem *QQmlAdaptorModel::createItem(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, int index)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModel.createItem' has no cute function yet. Qt's "
        "'QQmlDelegateModelItem *QQmlAdaptorModel::createItem(const "
        "QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, int "
        "index)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def notify(*__, **_) -> Never:
    """
    Qt's 'bool QQmlAdaptorModel::notify(const QList<QQmlDelegateModelItem *>
    &items, int index, int count, const QList<int> &roles) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModel.notify' has no cute function yet. Qt's 'bool "
        "QQmlAdaptorModel::notify(const QList<QQmlDelegateModelItem *> "
        "&items, int index, int count, const QList<int> &roles) const': "
        "takes a type Python has no way to hand over yet.")
