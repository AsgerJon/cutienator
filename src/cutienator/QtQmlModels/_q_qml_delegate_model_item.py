"""
QQmlDelegateModelItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDynamicMetaObjectData, QMetaObject
  from ..QtCore import QPersistentModelIndex, QVariant
  from ..QtQml import QQmlComponent
  from . import QQDMIncubationTask, QQmlDelegateModelAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDynamicMetaObjectData = WAIT['QDynamicMetaObjectData']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QQDMIncubationTask = WAIT['QQDMIncubationTask']
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelItem(QObject):
  """
  The cute side of Qt's QQmlDelegateModelItem: a plain Python object standing
  in front of one C++ QQmlDelegateModelItem.

  It is built on the cute 'QObject', as Qt's QQmlDelegateModelItem is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelItem that has a ritual and that
  Python can call so far, 52 names in all: 'metaObject', 'tr',
  'referenceObjectWeak', 'releaseObjectWeak', 'clearObjectWeakReferences',
  'isObjectReferenced', 'childContextObjectDestroyed', 'isScriptReferenced',
  'dispose', 'modelObject', 'destroyObject', 'destroyObjectLater',
  'dataForObject', 'modelRow', 'modelColumn', 'modelIndex',
  'hasValidModelIndex', 'setModelIndex', 'setPersistentModelIndex',
  'persistentModelIndex', 'usesStructuredModelData', 'get', 'setValue',
  'get_model', 'get_groups', 'set_groups', 'get_member', 'set_member',
  'get_index', 'attached', 'disableStructuredModelData',
  'exchangeMetaObject', 'incubationTask', 'clearIncubationTask',
  'setIncubationTask', 'objectStrongRef', 'objectWeakRef', 'scriptRef',
  'object', 'setObject', 'delegate', 'setDelegate', 'groups', 'setGroups',
  'addGroups', 'removeGroups', 'clearGroups', 'modelIndexChanged',
  'rowChanged', 'columnChanged', 'referenceSript', 'releaseScript'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateModelItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlDelegateModelItem::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDelegateModelItem::QQmlDelegateModelItem(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
    QQmlAdaptorModel::Accessors *accessor, int modelIndex, int row, int
    column)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlDelegateModelItem::~QQmlDelegateModelItem()': the destructor:
    Python never removes a C++ QQmlDelegateModelItem.
  - Qt's 'int QQmlDelegateModelItem::groupIndex(Compositor::Group group)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlDelegateModelItem::resolveIndex(const QQmlAdaptorModel
    &a0, int a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlDelegateModelItem::initProxy()': gives a type Python has no way to
    take yet.
  - Qt's 'const QQmlRefPointer<QQmlContextData>
    &QQmlDelegateModelItem::contextData() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QQmlDelegateModelItem::setContextData(const
    QQmlRefPointer<QQmlContextData> &contextData)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QQmlRefPointer<QQmlDelegateModelItemMetaType>
    &QQmlDelegateModelItem::metaType() const': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  3 of the 65 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlDelegateModelItem is created at the first use, not by
    'QQmlDelegateModelItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelItem.
  - Qt tells when it has removed the C++ QQmlDelegateModelItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDelegateModelItem that has no cute function yet,
    '__init__', 'contextData', 'groupIndex', 'initProxy', 'metaType',
    'resolveIndex', 'setContextData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlDelegateModelItem, each a class in here
  #  as in C++.

  class ObjectReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDelegateModelItem::ObjectReference: a plain
    Python object standing in front of one C++
    QQmlDelegateModelItem::ObjectReference.

    What exists
    -----------

    No function of Qt's QQmlDelegateModelItem::ObjectReference yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDelegateModelItem::ObjectReference::~ObjectReference()': the
      destructor: Python never removes a C++
      QQmlDelegateModelItem::ObjectReference.

    What has no ritual
    ------------------

    4 of the 6 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QQmlDelegateModelItem::ObjectReference is created at the first
      use, not by 'QQmlDelegateModelItem::ObjectReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlDelegateModelItem::ObjectReference.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDelegateModelItem::ObjectReference'

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

    @overload(QQmlDelegateModelItem)
    @overload(NoneType)
    def __init__(self, item: Optional[QQmlDelegateModelItem]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlDelegateModelItem::ObjectReference::ObjectReference(
      QQmlDelegateModelItem *item)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldelegatemodelitem-objectreference.html

      Parameters
      ----------

      item : Optional[QQmlDelegateModelItem]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlDelegateModelItem::ObjectReference::ObjectReference(
      #      QQmlDelegateModelItem *item)
      self._noteCreation(
          QQmlDelegateModelItem.ObjectReference, lambda: Rituals.call(
              'ritual_ZN21QQmlDelegateModelItem15ObjectReferenceC1EPS_',
              self._addressOf(item),
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

  class ObjectSpanReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDelegateModelItem::ObjectSpanReference: a plain
    Python object standing in front of one C++
    QQmlDelegateModelItem::ObjectSpanReference.

    What exists
    -----------

    No function of Qt's QQmlDelegateModelItem::ObjectSpanReference yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDelegateModelItem::ObjectSpanReference::ObjectSpanReference(
      QSpan<QQmlDelegateModelItem *const> span)': takes a type Python has no
      way to hand over yet.
    - Qt's
      'QQmlDelegateModelItem::ObjectSpanReference::~ObjectSpanReference()':
      the destructor: Python never removes a C++
      QQmlDelegateModelItem::ObjectSpanReference.

    What has no ritual
    ------------------

    4 of the 6 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QQmlDelegateModelItem::ObjectSpanReference is created at the
      first use, not by 'QQmlDelegateModelItem::ObjectSpanReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QQmlDelegateModelItem::ObjectSpanReference.
    - Each name of Qt's QQmlDelegateModelItem::ObjectSpanReference that has
      no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDelegateModelItem::ObjectSpanReference'

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQmlDelegateModelItem::ObjectSpanReference::ObjectSpanReference(
      QSpan<QQmlDelegateModelItem *const> span)': takes a type Python has no
      way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlDelegateModelItem.ObjectSpanReference.__init__' has no cute "
          "function yet. Qt's "
          "'QQmlDelegateModelItem::ObjectSpanReference::ObjectSpanReference("
          "QSpan<QQmlDelegateModelItem *const> span)': takes a type Python "
          "has no way to hand over yet.")

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

  class ScriptReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDelegateModelItem::ScriptReference: a plain
    Python object standing in front of one C++
    QQmlDelegateModelItem::ScriptReference.

    What exists
    -----------

    Every function of Qt's QQmlDelegateModelItem::ScriptReference that has a
    ritual and that Python can call so far, 1 name in all: 'data'. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDelegateModelItem::ScriptReference::~ScriptReference()': the
      destructor: Python never removes a C++
      QQmlDelegateModelItem::ScriptReference.

    What has no ritual
    ------------------

    4 of the 7 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QQmlDelegateModelItem::ScriptReference is created at the first
      use, not by 'QQmlDelegateModelItem::ScriptReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlDelegateModelItem::ScriptReference.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlDelegateModelItem = WAIT['QQmlDelegateModelItem']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDelegateModelItem::ScriptReference'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def data(self) -> Optional[QQmlDelegateModelItem]:
      """
      Calls Qt's 'QQmlDelegateModelItem
      *QQmlDelegateModelItem::ScriptReference::data() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldelegatemodelitem-scriptreference.html#data

      Returns
      -------

      Optional[QQmlDelegateModelItem]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QQmlDelegateModelItem
      #      *QQmlDelegateModelItem::ScriptReference::data() const
      address = self.uglySide.call(
          'ritual_ZNK21QQmlDelegateModelItem15ScriptReference4dataEv',
      )
      return QQmlDelegateModelItem._cuteAt(address)

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

    @overload(QQmlDelegateModelItem)
    @overload(NoneType)
    def __init__(self, item: Optional[QQmlDelegateModelItem]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlDelegateModelItem::ScriptReference::ScriptReference(
      QQmlDelegateModelItem *item)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldelegatemodelitem-scriptreference.html

      Parameters
      ----------

      item : Optional[QQmlDelegateModelItem]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlDelegateModelItem::ScriptReference::ScriptReference(
      #      QQmlDelegateModelItem *item)
      self._noteCreation(
          QQmlDelegateModelItem.ScriptReference, lambda: Rituals.call(
              'ritual_ZN21QQmlDelegateModelItem15ScriptReferenceC1EPS_',
              self._addressOf(item),
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
    Calls Qt's 'QString QQmlDelegateModelItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#tr

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
    #  QString QQmlDelegateModelItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def dataForObject(
      object: Optional[QObject],
  ) -> Optional[QQmlDelegateModelItem]:
    """
    Calls Qt's 'QQmlDelegateModelItem
    *QQmlDelegateModelItem::dataForObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#dataForObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlDelegateModelItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelItem *QQmlDelegateModelItem::dataForObject(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem13dataForObjectEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQmlDelegateModelItem._cuteAt(address)

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def get_model(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlDelegateModelItem::get_model(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#get_model

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlDelegateModelItem::get_model(const
    #      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
    #      QV4::Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem9get_modelEPKN3QV414FunctionObject'
        'EPKNS0_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def get_groups(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlDelegateModelItem::get_groups(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#get_groups

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlDelegateModelItem::get_groups(const
    #      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
    #      QV4::Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem10get_groupsEPKN3QV414FunctionObje'
        'ctEPKNS0_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def set_groups(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlDelegateModelItem::set_groups(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#set_groups

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlDelegateModelItem::set_groups(const
    #      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
    #      QV4::Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem10set_groupsEPKN3QV414FunctionObje'
        'ctEPKNS0_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(THIS, int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def get_member(
      thisItem: Optional[QQmlDelegateModelItem],
      flag: int,
      a2: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QQmlDelegateModelItem::get_member(QQmlDelegateModelItem *thisItem, uint
    flag, const QV4::Value &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#get_member

    Parameters
    ----------

    thisItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flag : int
      Passed on as it is.

    a2 : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::ReturnedValue
    #      QQmlDelegateModelItem::get_member(QQmlDelegateModelItem *thisItem,
    #      uint flag, const QV4::Value &a2)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem10get_memberEPS_jRKN3QV45ValueE',
        CuteMixin._addressOf(thisItem), flag, CuteMixin._valueOf(a2),
    )

  @staticmethod
  @overload(THIS, int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def set_member(
      thisItem: Optional[QQmlDelegateModelItem],
      flag: int,
      arg: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QQmlDelegateModelItem::set_member(QQmlDelegateModelItem *thisItem, uint
    flag, const QV4::Value &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#set_member

    Parameters
    ----------

    thisItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flag : int
      Passed on as it is.

    arg : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::ReturnedValue
    #      QQmlDelegateModelItem::set_member(QQmlDelegateModelItem *thisItem,
    #      uint flag, const QV4::Value &arg)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem10set_memberEPS_jRKN3QV45ValueE',
        CuteMixin._addressOf(thisItem), flag, CuteMixin._valueOf(arg),
    )

  @staticmethod
  @overload(THIS, int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def get_index(
      thisItem: Optional[QQmlDelegateModelItem],
      flag: int,
      arg: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QQmlDelegateModelItem::get_index(QQmlDelegateModelItem *thisItem, uint
    flag, const QV4::Value &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#get_index

    Parameters
    ----------

    thisItem : Optional[QQmlDelegateModelItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flag : int
      Passed on as it is.

    arg : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  QV4::ReturnedValue
    #      QQmlDelegateModelItem::get_index(QQmlDelegateModelItem *thisItem,
    #      uint flag, const QV4::Value &arg)
    return Rituals.call(
        'ritual_ZN21QQmlDelegateModelItem9get_indexEPS_jRKN3QV45ValueE',
        CuteMixin._addressOf(thisItem), flag, CuteMixin._valueOf(arg),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelItem'

  #  A C++ QQmlDelegateModelItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelItem'

  #  The functions Qt calls itself that QQmlDelegateModelItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'resolveIndex': (
          'bool QQmlDelegateModelItem::resolveIndex(const QQmlAdaptorModel '
          '&, int)',
      ),
      'initProxy': (
          'QQmlRefPointer<QQmlContextData> '
          'QQmlDelegateModelItem::initProxy()',
      ),
  }

  #  The functions Qt calls itself that QQmlDelegateModelItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setModelIndex': (
          ('_ZN21QQmlDelegateModelItem13setModelIndexEiiib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'get': (
          ('_ZN21QQmlDelegateModelItem3getEv',
           ('unsigned long long', 'number', ''),
           ()),
      ),
      'setValue': (
          ('_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
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
    Calls Qt's 'const QMetaObject *QQmlDelegateModelItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateModelItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isObjectReferenced(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::isObjectReferenced() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#isObjectReferenced
    """
    #  bool QQmlDelegateModelItem::isObjectReferenced() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem18isObjectReferencedEv',
    )

  def isScriptReferenced(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::isScriptReferenced() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#isScriptReferenced
    """
    #  bool QQmlDelegateModelItem::isScriptReferenced() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem18isScriptReferencedEv',
    )

  def modelRow(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItem::modelRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#modelRow
    """
    #  int QQmlDelegateModelItem::modelRow() const
    return self.uglySide.call('ritual_ZNK21QQmlDelegateModelItem8modelRowEv')

  def modelColumn(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItem::modelColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#modelColumn
    """
    #  int QQmlDelegateModelItem::modelColumn() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem11modelColumnEv',
    )

  def modelIndex(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItem::modelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#modelIndex
    """
    #  int QQmlDelegateModelItem::modelIndex() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem10modelIndexEv',
    )

  def hasValidModelIndex(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::hasValidModelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#hasValidModelIndex
    """
    #  bool QQmlDelegateModelItem::hasValidModelIndex() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem18hasValidModelIndexEv',
    )

  def persistentModelIndex(self) -> QPersistentModelIndex:
    """
    Calls Qt's 'QPersistentModelIndex
    QQmlDelegateModelItem::persistentModelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#persistentModelIndex

    Returns
    -------

    QPersistentModelIndex
      A new cute QPersistentModelIndex around the copy Qt gave back. Python
      owns it.
    """
    #  QPersistentModelIndex QQmlDelegateModelItem::persistentModelIndex()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem20persistentModelIndexEv',
    )
    from ..QtCore import QPersistentModelIndex
    return QPersistentModelIndex._cuteOwning(address)

  def usesStructuredModelData(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::usesStructuredModelData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#usesStructuredModelData
    """
    #  bool QQmlDelegateModelItem::usesStructuredModelData() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem23usesStructuredModelDataEv',
    )

  def attached(self) -> Optional[QQmlDelegateModelAttached]:
    """
    Calls Qt's 'QQmlDelegateModelAttached *QQmlDelegateModelItem::attached()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#attached

    Returns
    -------

    Optional[QQmlDelegateModelAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelAttached *QQmlDelegateModelItem::attached() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem8attachedEv',
    )
    from . import QQmlDelegateModelAttached
    return QQmlDelegateModelAttached._cuteAt(address)

  def incubationTask(self) -> Optional[QQDMIncubationTask]:
    """
    Calls Qt's 'QQDMIncubationTask *QQmlDelegateModelItem::incubationTask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#incubationTask

    Returns
    -------

    Optional[QQDMIncubationTask]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQDMIncubationTask *QQmlDelegateModelItem::incubationTask() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem14incubationTaskEv',
    )
    from . import QQDMIncubationTask
    return QQDMIncubationTask._cuteAt(address)

  def objectStrongRef(self) -> int:
    """
    Calls Qt's 'quint16 QQmlDelegateModelItem::objectStrongRef() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#objectStrongRef
    """
    #  quint16 QQmlDelegateModelItem::objectStrongRef() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem15objectStrongRefEv',
    )

  def objectWeakRef(self) -> int:
    """
    Calls Qt's 'quint16 QQmlDelegateModelItem::objectWeakRef() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#objectWeakRef
    """
    #  quint16 QQmlDelegateModelItem::objectWeakRef() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem13objectWeakRefEv',
    )

  def scriptRef(self) -> int:
    """
    Calls Qt's 'quint16 QQmlDelegateModelItem::scriptRef() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#scriptRef
    """
    #  quint16 QQmlDelegateModelItem::scriptRef() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem9scriptRefEv',
    )

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDelegateModelItem::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDelegateModelItem::object() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem6objectEv',
    )
    return QObject._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlDelegateModelItem::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlDelegateModelItem::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlDelegateModelItem8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def groups(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItem::groups() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#groups
    """
    #  int QQmlDelegateModelItem::groups() const
    return self.uglySide.call('ritual_ZNK21QQmlDelegateModelItem6groupsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  @overload(int, int, int, bool)
  def setModelIndex(
      self,
      idx: int,
      newRow: int,
      newColumn: int,
      alwaysEmit: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setModelIndex(int idx, int
    newRow, int newColumn, bool alwaysEmit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setModelIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.

    newRow : int
      Passed on as it is.

    newColumn : int
      Passed on as it is.

    alwaysEmit : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQmlDelegateModelItem::setModelIndex(int idx, int newRow, int
    #      newColumn, bool alwaysEmit)
    ritual = 'ritual_ZN21QQmlDelegateModelItem13setModelIndexEiiib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQmlDelegateModelItem13setModelIndexEiiib'
    self.uglySide.call(ritual, idx, newRow, newColumn, alwaysEmit)

  @overload(QPersistentModelIndex)
  def setPersistentModelIndex(self, index: QPersistentModelIndex) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setPersistentModelIndex(const
    QPersistentModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setPersistentModelIndex

    Parameters
    ----------

    index : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  void QQmlDelegateModelItem::setPersistentModelIndex(const
    #      QPersistentModelIndex &index)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem23setPersistentModelIndexERK21QPer'
        'sistentModelIndex',
        self._valueOf(index),
    )

  @overload(str, QVariant)
  def setValue(self, role: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setValue(const QString &role,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setValue

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlDelegateModelItem::setValue(const QString &role, const
    #      QVariant &value)
    ritual = (
        'ritual_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQmlDelegateModelItem8setValueERK7QStringRK8QVari'
          'ant')
    self.uglySide.call(ritual, role, self._valueOf(value))

  @overload(QQDMIncubationTask)
  @overload(NoneType)
  def setIncubationTask(
      self,
      incubationTask: Optional[QQDMIncubationTask],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelItem::setIncubationTask(QQDMIncubationTask
    *incubationTask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setIncubationTask

    Parameters
    ----------

    incubationTask : Optional[QQDMIncubationTask]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelItem::setIncubationTask(QQDMIncubationTask
    #      *incubationTask)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem17setIncubationTaskEP18QQDMIncubat'
        'ionTask',
        self._addressOf(incubationTask),
    )

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelItem::setObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem9setObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelItem::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(int)
  def setGroups(self, groups: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::setGroups(int groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#setGroups

    Parameters
    ----------

    groups : int
      Passed on as it is.
    """
    #  void QQmlDelegateModelItem::setGroups(int groups)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem9setGroupsEi', groups,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlDelegateModelItem::QQmlDelegateModelItem(const
    QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
    QQmlAdaptorModel::Accessors *accessor, int modelIndex, int row, int
    column)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.__init__' has no cute function yet. Qt's "
        "'QQmlDelegateModelItem::QQmlDelegateModelItem(const "
        "QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, "
        "QQmlAdaptorModel::Accessors *accessor, int modelIndex, int row, "
        "int column)': takes a type Python has no way to hand over yet.")

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

  def referenceObjectWeak(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDelegateModelItem::referenceObjectWeak()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#referenceObjectWeak

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDelegateModelItem::referenceObjectWeak()
    address = self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem19referenceObjectWeakEv',
    )
    return QObject._cuteAt(address)

  def releaseObjectWeak(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::releaseObjectWeak()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#releaseObjectWeak
    """
    #  bool QQmlDelegateModelItem::releaseObjectWeak()
    return self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem17releaseObjectWeakEv',
    )

  def clearObjectWeakReferences(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::clearObjectWeakReferences()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html
    """
    #  void QQmlDelegateModelItem::clearObjectWeakReferences()
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem25clearObjectWeakReferencesEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def childContextObjectDestroyed(
      self,
      childContextObject: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelItem::childContextObjectDestroyed(QObject
    *childContextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html

    Parameters
    ----------

    childContextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelItem::childContextObjectDestroyed(QObject
    #      *childContextObject)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem27childContextObjectDestroyedEP7QO'
        'bject',
        self._addressOf(childContextObject, 'QObject'),
    )

  def dispose(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::dispose()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#dispose
    """
    #  void QQmlDelegateModelItem::dispose()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem7disposeEv')

  def modelObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDelegateModelItem::modelObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#modelObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDelegateModelItem::modelObject()
    address = self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem11modelObjectEv',
    )
    return QObject._cuteAt(address)

  def destroyObject(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::destroyObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#destroyObject
    """
    #  void QQmlDelegateModelItem::destroyObject()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem13destroyObjectEv')

  def destroyObjectLater(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::destroyObjectLater()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#destroyObjectLater
    """
    #  void QQmlDelegateModelItem::destroyObjectLater()
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem18destroyObjectLaterEv',
    )

  def get(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlDelegateModelItem::get()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#get
    """
    #  QV4::ReturnedValue QQmlDelegateModelItem::get()
    ritual = 'ritual_ZN21QQmlDelegateModelItem3getEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQmlDelegateModelItem3getEv'
    return self.uglySide.call(ritual)

  def disableStructuredModelData(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::disableStructuredModelData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html
    """
    #  void QQmlDelegateModelItem::disableStructuredModelData()
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem26disableStructuredModelDataEv',
    )

  @overload(QDynamicMetaObjectData)
  @overload(NoneType)
  def exchangeMetaObject(
      self,
      metaObject: Optional[QDynamicMetaObjectData],
  ) -> Optional[QDynamicMetaObjectData]:
    """
    Calls Qt's 'QDynamicMetaObjectData
    *QQmlDelegateModelItem::exchangeMetaObject(QDynamicMetaObjectData
    *metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#exchangeMetaObject

    Parameters
    ----------

    metaObject : Optional[QDynamicMetaObjectData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDynamicMetaObjectData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDynamicMetaObjectData
    #      *QQmlDelegateModelItem::exchangeMetaObject(QDynamicMetaObjectData
    #      *metaObject)
    address = self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem18exchangeMetaObjectEP22QDynamicMe'
        'taObjectData',
        self._addressOf(metaObject, 'QDynamicMetaObjectData'),
    )
    from ..QtCore import QDynamicMetaObjectData
    return QDynamicMetaObjectData._cuteAt(address)

  def clearIncubationTask(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::clearIncubationTask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#clearIncubationTask
    """
    #  void QQmlDelegateModelItem::clearIncubationTask()
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem19clearIncubationTaskEv',
    )

  @overload(int)
  def addGroups(self, groups: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::addGroups(int groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#addGroups

    Parameters
    ----------

    groups : int
      Passed on as it is.
    """
    #  void QQmlDelegateModelItem::addGroups(int groups)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem9addGroupsEi', groups,
    )

  @overload(int)
  def removeGroups(self, groups: int) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::removeGroups(int groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#removeGroups

    Parameters
    ----------

    groups : int
      Passed on as it is.
    """
    #  void QQmlDelegateModelItem::removeGroups(int groups)
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem12removeGroupsEi', groups,
    )

  def clearGroups(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::clearGroups()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#clearGroups
    """
    #  void QQmlDelegateModelItem::clearGroups()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem11clearGroupsEv')

  def modelIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::modelIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#modelIndexChanged
    """
    #  void QQmlDelegateModelItem::modelIndexChanged()
    self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem17modelIndexChangedEv',
    )

  def rowChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::rowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#rowChanged
    """
    #  void QQmlDelegateModelItem::rowChanged()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem10rowChangedEv')

  def columnChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::columnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#columnChanged
    """
    #  void QQmlDelegateModelItem::columnChanged()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem13columnChangedEv')

  def referenceSript(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItem::referenceSript()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#referenceSript
    """
    #  void QQmlDelegateModelItem::referenceSript()
    self.uglySide.call('ritual_ZN21QQmlDelegateModelItem14referenceSriptEv')

  def releaseScript(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelItem::releaseScript()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitem.html#releaseScript
    """
    #  bool QQmlDelegateModelItem::releaseScript()
    return self.uglySide.call(
        'ritual_ZN21QQmlDelegateModelItem13releaseScriptEv',
    )

  @staticmethod
  def contextData(*__, **_) -> Never:
    """
    Qt's 'const QQmlRefPointer<QQmlContextData>
    &QQmlDelegateModelItem::contextData() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.contextData' has no cute function yet. Qt's "
        "'const QQmlRefPointer<QQmlContextData> "
        "&QQmlDelegateModelItem::contextData() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def groupIndex(*__, **_) -> Never:
    """
    Qt's 'int QQmlDelegateModelItem::groupIndex(Compositor::Group group)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.groupIndex' has no cute function yet. Qt's "
        "'int QQmlDelegateModelItem::groupIndex(Compositor::Group group)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def initProxy(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlDelegateModelItem::initProxy()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.initProxy' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QQmlDelegateModelItem::initProxy()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def metaType(*__, **_) -> Never:
    """
    Qt's 'const QQmlRefPointer<QQmlDelegateModelItemMetaType>
    &QQmlDelegateModelItem::metaType() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.metaType' has no cute function yet. Qt's "
        "'const QQmlRefPointer<QQmlDelegateModelItemMetaType> "
        "&QQmlDelegateModelItem::metaType() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def resolveIndex(*__, **_) -> Never:
    """
    Qt's 'bool QQmlDelegateModelItem::resolveIndex(const QQmlAdaptorModel
    &a0, int a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.resolveIndex' has no cute function yet. "
        "Qt's 'bool QQmlDelegateModelItem::resolveIndex(const "
        "QQmlAdaptorModel &a0, int a1)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setContextData(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelItem::setContextData(const
    QQmlRefPointer<QQmlContextData> &contextData)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelItem.setContextData' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelItem::setContextData(const "
        "QQmlRefPointer<QQmlContextData> &contextData)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QQmlDelegateModelItem *>': the list of QQmlDelegateModelItem,
#  which 'QList[QQmlDelegateModelItem]' gives. It is made here, so that there
#  is one as soon as there can be a QQmlDelegateModelItem.
QList.createKind(
    QQmlDelegateModelItem, 'address',
    make='ritual_list_make_QQmlDelegateModelItem_ptr',
    add='ritual_list_add_QQmlDelegateModelItem_ptr',
    size='ritual_list_size_QQmlDelegateModelItem_ptr',
    at='ritual_list_at_QQmlDelegateModelItem_ptr',
    drop='ritual_list_drop_QQmlDelegateModelItem_ptr',
)
