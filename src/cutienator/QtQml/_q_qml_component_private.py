"""
QQmlComponentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlComponentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObjectPrivate
from . import QQmlComponent, QQmlTypeLoader, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QUrl, QVariant
  from . import QQmlContext, QQmlEngine, QQmlEnginePrivate, QQmlError
  from . import QQmlNotifyingBlob, QQmlObjectCreator, QQmlPropertyData
  from . import QQmlType, RequiredProperties, RequiredPropertyInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlEnginePrivate = WAIT['QQmlEnginePrivate']
  QQmlNotifyingBlob = WAIT['QQmlNotifyingBlob']
  QQmlObjectCreator = WAIT['QQmlObjectCreator']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']
  RequiredProperties = WAIT['RequiredProperties']
  RequiredPropertyInfo = WAIT['RequiredPropertyInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlComponentPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQmlComponentPrivate: a plain Python object standing
  in front of one C++ QQmlComponentPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlComponentPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. Qt's
  QQmlComponentPrivate is built on Qt's QQmlNotifyingBlob::Callback as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQmlComponentPrivate that has a ritual and that
  Python can call so far, 26 names in all: 'q_func', 'loadUrl', 'loadedType',
  'completeCreate', 'initializeObjectWithInitialProperties',
  'setInitialProperties', 'unsetRequiredPropertyToQQmlError', 'ready',
  'progress', 'hadTopLevelRequiredProperties', 'complete', 'clear', 'get',
  'doBeginCreate', 'setInitialProperty', 'createWithProperties', 'isBound',
  'prepareLoadFromModule', 'completeLoadFromModule', 'setProgress',
  'loadHelperType', 'hasUnsetRequiredProperties', 'requiredProperties',
  'creator', 'engine', 'setData'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlComponent *QQmlComponentPrivate::q_func() const': takes
    in Python what 'QQmlComponent *QQmlComponentPrivate::q_func()' takes.
  - Qt's 'QObject
    *QQmlComponentPrivate::beginCreate(QQmlRefPointer<QQmlContextData> a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlComponentPrivate::incubateObject(QQmlIncubator
    *incubationTask, QQmlComponent *component, QQmlEngine *engine, const
    QQmlRefPointer<QQmlContextData> &context, const
    QQmlRefPointer<QQmlContextData> &forContext)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlComponentPrivate::fromTypeData(const
    QQmlRefPointer<QQmlTypeData> &data)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlComponentPrivate::beginDeferred(QQmlEnginePrivate
    *enginePriv, QObject *object, DeferredState *deferredState)': names
    'QQmlComponentPrivate::DeferredState', which has no cute class yet.
  - Qt's 'void QQmlComponentPrivate::completeDeferred(QQmlEnginePrivate
    *enginePriv, DeferredState *deferredState)': names
    'QQmlComponentPrivate::DeferredState', which has no cute class yet.
  - Qt's 'QQmlProperty
    QQmlComponentPrivate::removePropertyFromRequired(QObject *target, const
    QString &name, RequiredProperties *requiredProperties, QQmlEngine
    *engine, bool *wasInRequiredProperties)': takes a number to change where
    it is.
  - Qt's 'void
    QQmlComponentPrivate::setCreationContext(QQmlRefPointer<QQmlContextData>
    creationContext)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlComponentPrivate::compilationUnit() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QQmlComponentPrivate::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlComponentPrivate is created at the first use, not by
    'QQmlComponentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlComponentPrivate.
  - Each name of Qt's QQmlComponentPrivate that has no cute function yet,
    'beginCreate', 'beginDeferred', 'compilationUnit', 'completeDeferred',
    'fromTypeData', 'incubateObject', 'removePropertyFromRequired',
    'setCompilationUnit', 'setCreationContext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlComponentPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CreateBehavior(CuteNum, scoped=True):
    """
    The enum 'QQmlComponentPrivate::CreateBehavior' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Cpp = Kee[int](0)
    Qml = Kee[int](1)

  #  The classes Qt writes inside QQmlComponentPrivate, each a class in here
  #  as in C++.

  class AnnotatedQmlError(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlComponentPrivate::AnnotatedQmlError: a plain
    Python object standing in front of one C++
    QQmlComponentPrivate::AnnotatedQmlError.

    C++ hands a QQmlComponentPrivate::AnnotatedQmlError around as a copy, so
    every C++ QQmlComponentPrivate::AnnotatedQmlError behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlComponentPrivate::AnnotatedQmlError yet. It can
    be made from Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlComponentPrivate::AnnotatedQmlError::~AnnotatedQmlError()':
      the destructor: Python removes its C++
      QQmlComponentPrivate::AnnotatedQmlError by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlComponentPrivate::AnnotatedQmlError is created at the first
      use, not by 'QQmlComponentPrivate::AnnotatedQmlError(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlComponentPrivate::AnnotatedQmlError back gives
      a copy the ritual made for Python, in a new cute
      QQmlComponentPrivate::AnnotatedQmlError.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlError = WAIT['QQmlError']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlComponentPrivate::AnnotatedQmlError'

    #  Qt's '~QQmlComponentPrivate::AnnotatedQmlError()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlComponentPrivate::AnnotatedQmlError behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorD1Ev')

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
      'QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-annotatedqmlerror.html
      """
      #  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError()
      self._noteCreation(
          QQmlComponentPrivate.AnnotatedQmlError, lambda: Rituals.call(
              'ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1Ev',
          ))

    @overload(QQmlError)
    def __init__(self, error: QQmlError) -> None:
      """
      Notes what was given, for Qt's
      'QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
      error)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-annotatedqmlerror.html

      Parameters
      ----------

      error : QQmlError
        Passed on as a value: Qt reads the C++ QQmlError, which stays
        Python's own.
      """
      #  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
      #      error)
      self._noteCreation(
          QQmlComponentPrivate.AnnotatedQmlError, lambda: Rituals.call(
              'ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1E9QQmlEr'
              'ror',
              self._valueOf(error),
          ))

    @overload(QQmlError, bool)
    def __init__(self, error: QQmlError, transient: bool) -> None:
      """
      Notes what was given, for Qt's
      'QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
      error, bool transient)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-annotatedqmlerror.html

      Parameters
      ----------

      error : QQmlError
        Passed on as a value: Qt reads the C++ QQmlError, which stays
        Python's own.

      transient : bool
        Passed on as it is.
      """
      #  QQmlComponentPrivate::AnnotatedQmlError::AnnotatedQmlError(QQmlError
      #      error, bool transient)
      self._noteCreation(
          QQmlComponentPrivate.AnnotatedQmlError, lambda: Rituals.call(
              'ritual_ZN20QQmlComponentPrivate17AnnotatedQmlErrorC1E9QQmlEr'
              'rorb',
              self._valueOf(error), transient,
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

  class ConstructionState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlComponentPrivate::ConstructionState: a plain
    Python object standing in front of one C++
    QQmlComponentPrivate::ConstructionState.

    What exists
    -----------

    Every function of Qt's QQmlComponentPrivate::ConstructionState that has a
    ritual and that Python can call so far, 13 names in all:
    'ensureRequiredPropertyStorage', 'requiredProperties',
    'addPendingRequiredProperty', 'hasUnsetRequiredProperties',
    'clearRequiredProperties', 'appendErrors', 'appendCreatorErrors',
    'creator', 'clear', 'hasCreator', 'isCompletePending',
    'setCompletePending', 'target'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlComponentPrivate::ConstructionState::ConstructionState(
      ConstructionState &&other)': takes a type Python has no way to hand
      over yet.
    - Qt's 'QQmlComponentPrivate::ConstructionState::~ConstructionState()':
      the destructor: Python never removes a C++
      QQmlComponentPrivate::ConstructionState.
    - Qt's 'QQmlComponentPrivate::ConstructionState
      &QQmlComponentPrivate::ConstructionState::operator=(
      QQmlComponentPrivate::ConstructionState &&other)': assignment: Python
      binds a name and has no operator for it.
    - Qt's 'void
      QQmlComponentPrivate::ConstructionState::swap(ConstructionState
      &other)': takes a type Python has no way to hand over yet.
    - Qt's 'const QQmlObjectCreator
      *QQmlComponentPrivate::ConstructionState::creator() const': takes in
      Python what 'QQmlObjectCreator
      *QQmlComponentPrivate::ConstructionState::creator()' takes.
    - Qt's 'QQmlObjectCreator
      *QQmlComponentPrivate::ConstructionState::initCreator(const
      QQmlRefPointer<QQmlContextData> &parentContext, const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
      QQmlRefPointer<QQmlContextData> &creationContext, const QString
      &inlineComponentName)': takes a type Python has no way to hand over
      yet.

    What has no ritual
    ------------------

    2 of the 22 functions Qt declares: 2 forbidden.

    What to expect
    --------------

    - The C++ QQmlComponentPrivate::ConstructionState is created at the first
      use, not by 'QQmlComponentPrivate::ConstructionState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlComponentPrivate::ConstructionState.
    - Each name of Qt's QQmlComponentPrivate::ConstructionState that has no
      cute function yet, 'initCreator', 'swap', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QObject = WAIT['QObject']
      QQmlError = WAIT['QQmlError']
      QQmlPropertyData = WAIT['QQmlPropertyData']
      RequiredPropertyInfo = WAIT['RequiredPropertyInfo']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlComponentPrivate::ConstructionState'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def requiredProperties(self) -> Optional[RequiredProperties]:
      """
      Calls Qt's 'RequiredProperties
      *QQmlComponentPrivate::ConstructionState::requiredProperties() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Returns
      -------

      Optional[RequiredProperties]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  RequiredProperties
      #      *QQmlComponentPrivate::ConstructionState::requiredProperties()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK20QQmlComponentPrivate17ConstructionState18requiredPro'
          'pertiesEv',
      )
      from . import RequiredProperties
      return RequiredProperties._cuteAt(address)

    def hasUnsetRequiredProperties(self) -> bool:
      """
      Calls Qt's 'bool
      QQmlComponentPrivate::ConstructionState::hasUnsetRequiredProperties()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  bool QQmlComponentPrivate::ConstructionState::
      #      hasUnsetRequiredProperties() const
      return self.uglySide.call(
          'ritual_ZNK20QQmlComponentPrivate17ConstructionState26hasUnsetReq'
          'uiredPropertiesEv',
      )

    def hasCreator(self) -> bool:
      """
      Calls Qt's 'bool QQmlComponentPrivate::ConstructionState::hasCreator()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  bool QQmlComponentPrivate::ConstructionState::hasCreator() const
      return self.uglySide.call(
          'ritual_ZNK20QQmlComponentPrivate17ConstructionState10hasCreatorE'
          'v',
      )

    def isCompletePending(self) -> bool:
      """
      Calls Qt's 'bool
      QQmlComponentPrivate::ConstructionState::isCompletePending() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  bool QQmlComponentPrivate::ConstructionState::isCompletePending()
      #      const
      return self.uglySide.call(
          'ritual_ZNK20QQmlComponentPrivate17ConstructionState17isCompleteP'
          'endingEv',
      )

    def target(self) -> Optional[QObject]:
      """
      Calls Qt's 'QObject *QQmlComponentPrivate::ConstructionState::target()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Returns
      -------

      Optional[QObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QObject *QQmlComponentPrivate::ConstructionState::target() const
      address = self.uglySide.call(
          'ritual_ZNK20QQmlComponentPrivate17ConstructionState6targetEv',
      )
      from ..QtCore import QObject
      return QObject._cuteAt(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(bool)
    def setCompletePending(self, isPending: bool) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::setCompletePending(bool
      isPending)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Parameters
      ----------

      isPending : bool
        Passed on as it is.
      """
      #  void
      #      QQmlComponentPrivate::ConstructionState::setCompletePending(bool
      #      isPending)
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState18setCompleteP'
          'endingEb',
          isPending,
      )

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
      'QQmlComponentPrivate::ConstructionState::ConstructionState()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  QQmlComponentPrivate::ConstructionState::ConstructionState()
      self._noteCreation(
          QQmlComponentPrivate.ConstructionState, lambda: Rituals.call(
              'ritual_ZN20QQmlComponentPrivate17ConstructionStateC1Ev',
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

    @overload(QObject)
    @overload(NoneType)
    def ensureRequiredPropertyStorage(
        self,
        target: Optional[QObject],
    ) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::ensureRequiredPropertyStorage(
      QObject *target)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Parameters
      ----------

      target : Optional[QObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QQmlComponentPrivate::ConstructionState::
      #      ensureRequiredPropertyStorage(QObject *target)
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState29ensureRequir'
          'edPropertyStorageEP7QObject',
          self._addressOf(target, 'QObject'),
      )

    @overload(QObject, QQmlPropertyData, RequiredPropertyInfo)
    @overload(QObject, NoneType, RequiredPropertyInfo)
    @overload(NoneType, QQmlPropertyData, RequiredPropertyInfo)
    @overload(NoneType, NoneType, RequiredPropertyInfo)
    def addPendingRequiredProperty(
        self,
        object: Optional[QObject],
        propData: Optional[QQmlPropertyData],
        info: RequiredPropertyInfo,
    ) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::addPendingRequiredProperty(
      const QObject *object, const QQmlPropertyData *propData, const
      RequiredPropertyInfo &info)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Parameters
      ----------

      object : Optional[QObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      propData : Optional[QQmlPropertyData]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      info : RequiredPropertyInfo
        Passed on as a value: Qt reads the C++ RequiredPropertyInfo, which
        stays Python's own.
      """
      #  void QQmlComponentPrivate::ConstructionState::
      #      addPendingRequiredProperty(const QObject *object, const
      #      QQmlPropertyData *propData, const RequiredPropertyInfo &info)
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState26addPendingRe'
          'quiredPropertyEPK7QObjectPK16QQmlPropertyDataRK20RequiredPropert'
          'yInfo',
          self._addressOf(object, 'QObject'), self._addressOf(propData),
          self._valueOf(info),
      )

    def clearRequiredProperties(self) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::clearRequiredProperties()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  void QQmlComponentPrivate::ConstructionState::
      #      clearRequiredProperties()
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState23clearRequire'
          'dPropertiesEv',
      )

    @overload(QList[QQmlError])
    def appendErrors(self, qmlErrors: QList[QQmlError]) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::appendErrors(const
      QList<QQmlError> &qmlErrors)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Parameters
      ----------

      qmlErrors : QList[QQmlError]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  void QQmlComponentPrivate::ConstructionState::appendErrors(const
      #      QList<QQmlError> &qmlErrors)
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState12appendErrors'
          'ERK5QListI9QQmlErrorE',
          self._valueOf(qmlErrors),
      )

    def appendCreatorErrors(self) -> None:
      """
      Calls Qt's 'void
      QQmlComponentPrivate::ConstructionState::appendCreatorErrors()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  void QQmlComponentPrivate::ConstructionState::appendCreatorErrors()
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState19appendCreato'
          'rErrorsEv',
      )

    def creator(self) -> Optional[QQmlObjectCreator]:
      """
      Calls Qt's 'QQmlObjectCreator
      *QQmlComponentPrivate::ConstructionState::creator()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html

      Returns
      -------

      Optional[QQmlObjectCreator]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QQmlObjectCreator
      #      *QQmlComponentPrivate::ConstructionState::creator()
      address = self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState7creatorEv',
      )
      from . import QQmlObjectCreator
      return QQmlObjectCreator._cuteAt(address)

    def clear(self) -> None:
      """
      Calls Qt's 'void QQmlComponentPrivate::ConstructionState::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlcomponentprivate-constructionstate.html
      """
      #  void QQmlComponentPrivate::ConstructionState::clear()
      self.uglySide.call(
          'ritual_ZN20QQmlComponentPrivate17ConstructionState5clearEv',
      )

    @staticmethod
    def initCreator(*__, **_) -> Never:
      """
      Qt's 'QQmlObjectCreator
      *QQmlComponentPrivate::ConstructionState::initCreator(const
      QQmlRefPointer<QQmlContextData> &parentContext, const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
      QQmlRefPointer<QQmlContextData> &creationContext, const QString
      &inlineComponentName)': takes a type Python has no way to hand over
      yet.
      """
      raise NotImplementedError(
          "'QQmlComponentPrivate.ConstructionState.initCreator' has no cute "
          "function yet. Qt's 'QQmlObjectCreator "
          "*QQmlComponentPrivate::ConstructionState::initCreator(const "
          "QQmlRefPointer<QQmlContextData> &parentContext, const "
          "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
          "const QQmlRefPointer<QQmlContextData> &creationContext, const "
          "QString &inlineComponentName)': takes a type Python has no way "
          "to hand over yet.")

    @staticmethod
    def swap(*__, **_) -> Never:
      """
      Qt's 'void
      QQmlComponentPrivate::ConstructionState::swap(ConstructionState
      &other)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlComponentPrivate.ConstructionState.swap' has no cute "
          "function yet. Qt's 'void "
          "QQmlComponentPrivate::ConstructionState::swap(ConstructionState "
          "&other)': takes a type Python has no way to hand over yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, QObject, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, QObject, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, NoneType, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, QObject, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, QObject, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, NoneType, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, QObject, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, QObject, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, NoneType, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], RequiredProperties, NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, QObject, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, QObject, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, NoneType, QQmlObjectCreator,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], NoneType, NoneType, NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, QObject, QQmlObjectCreator,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, QObject, NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, NoneType, QQmlObjectCreator,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, NoneType, NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      NoneType, QObject, QQmlObjectCreator,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      NoneType, QObject, NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      NoneType, NoneType, QQmlObjectCreator,
  )
  @overload(
      NoneType, WAIT['QV4.QmlContext'], WAIT['QV4.Value'], WAIT['QV4.Value'],
      NoneType, NoneType, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, QObject, QQmlObjectCreator,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, QObject, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, NoneType, QQmlObjectCreator,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'],
      RequiredProperties, NoneType, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType,
      QObject, QQmlObjectCreator,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType,
      QObject, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType,
      NoneType, QQmlObjectCreator,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType,
      NoneType, NoneType,
  )
  def setInitialProperties(
      engine: Optional[QV4.ExecutionEngine],
      qmlContext: Optional[QV4.QmlContext],
      o: QV4.Value,
      v: QV4.Value,
      requiredProperties: Optional[RequiredProperties],
      createdComponent: Optional[QObject],
      creator: Optional[QQmlObjectCreator],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlComponentPrivate::setInitialProperties(QV4::ExecutionEngine *engine,
    QV4::QmlContext *qmlContext, const QV4::Value &o, const QV4::Value &v,
    RequiredProperties *requiredProperties, QObject *createdComponent, const
    QQmlObjectCreator *creator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#setInitialProperties

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qmlContext : Optional[QV4.QmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    requiredProperties : Optional[RequiredProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    createdComponent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    creator : Optional[QQmlObjectCreator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponentPrivate::setInitialProperties(QV4::ExecutionEngine
    #      *engine, QV4::QmlContext *qmlContext, const QV4::Value &o, const
    #      QV4::Value &v, RequiredProperties *requiredProperties, QObject
    #      *createdComponent, const QQmlObjectCreator *creator)
    Rituals.call(
        'ritual_ZN20QQmlComponentPrivate20setInitialPropertiesEPN3QV415Exec'
        'utionEngineEPNS0_10QmlContextERKNS0_5ValueES7_P18RequiredPropertie'
        'sP7QObjectPK17QQmlObjectCreator',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(qmlContext),
        CuteMixin._valueOf(o), CuteMixin._valueOf(v),
        CuteMixin._addressOf(requiredProperties),
        CuteMixin._addressOf(createdComponent, 'QObject'),
        CuteMixin._addressOf(creator),
    )

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def setInitialProperties(
      self,
      object: Optional[QObject],
      properties: QMap[str, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlComponentPrivate::setInitialProperties(QObject
    *object, const QVariantMap &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#setInitialProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QQmlComponentPrivate::setInitialProperties(QObject *object, const
    #      QVariantMap &properties)
    return self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate20setInitialPropertiesEP7QObjectRK4'
        'QMapI7QString8QVariantE',
        self._addressOf(object, 'QObject'), self._valueOf(properties),
    )

  @staticmethod
  @overload(RequiredPropertyInfo)
  def unsetRequiredPropertyToQQmlError(
      unsetRequiredProperty: RequiredPropertyInfo,
  ) -> QQmlError:
    """
    Calls Qt's 'QQmlError
    QQmlComponentPrivate::unsetRequiredPropertyToQQmlError(const
    RequiredPropertyInfo &unsetRequiredProperty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html

    Parameters
    ----------

    unsetRequiredProperty : RequiredPropertyInfo
      Passed on as a value: Qt reads the C++ RequiredPropertyInfo, which
      stays Python's own.

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlComponentPrivate::unsetRequiredPropertyToQQmlError(const
    #      RequiredPropertyInfo &unsetRequiredProperty)
    address = Rituals.call(
        'ritual_ZN20QQmlComponentPrivate32unsetRequiredPropertyToQQmlErrorE'
        'RK20RequiredPropertyInfo',
        CuteMixin._valueOf(unsetRequiredProperty),
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  @staticmethod
  @overload(QQmlEnginePrivate, ConstructionState)
  @overload(QQmlEnginePrivate, NoneType)
  @overload(NoneType, ConstructionState)
  @overload(NoneType, NoneType)
  def complete(
      enginePriv: Optional[QQmlEnginePrivate],
      state: Optional[ConstructionState],
  ) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::complete(QQmlEnginePrivate
    *enginePriv, ConstructionState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#complete

    Parameters
    ----------

    enginePriv : Optional[QQmlEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : Optional[ConstructionState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponentPrivate::complete(QQmlEnginePrivate *enginePriv,
    #      ConstructionState *state)
    Rituals.call(
        'ritual_ZN20QQmlComponentPrivate8completeEP17QQmlEnginePrivatePNS_1'
        '7ConstructionStateE',
        CuteMixin._addressOf(enginePriv), CuteMixin._addressOf(state),
    )

  @staticmethod
  @overload(QQmlComponent)
  @overload(NoneType)
  def get(c: Optional[QQmlComponent]) -> Optional[QQmlComponentPrivate]:
    """
    Calls Qt's 'QQmlComponentPrivate *QQmlComponentPrivate::get(QQmlComponent
    *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#get

    Parameters
    ----------

    c : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlComponentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponentPrivate *QQmlComponentPrivate::get(QQmlComponent *c)
    address = Rituals.call(
        'ritual_ZN20QQmlComponentPrivate3getEP13QQmlComponent',
        CuteMixin._addressOf(c),
    )
    return QQmlComponentPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlComponentPrivate'

  #  The functions Qt calls itself that QQmlComponentPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'incubateObject': (
          'void QQmlComponentPrivate::incubateObject(QQmlIncubator *, '
          'QQmlComponent *, QQmlEngine *, const '
          'QQmlRefPointer<QQmlContextData> &, const '
          'QQmlRefPointer<QQmlContextData> &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def loadedType(self) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlComponentPrivate::loadedType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#loadedType

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlComponentPrivate::loadedType() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate10loadedTypeEv',
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def hadTopLevelRequiredProperties(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponentPrivate::hadTopLevelRequiredProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html
    """
    #  bool QQmlComponentPrivate::hadTopLevelRequiredProperties() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate29hadTopLevelRequiredPropertiesEv',
    )

  def isBound(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponentPrivate::isBound() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#isBound
    """
    #  bool QQmlComponentPrivate::isBound() const
    return self.uglySide.call('ritual_ZNK20QQmlComponentPrivate7isBoundEv')

  def loadHelperType(self) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlComponentPrivate::loadHelperType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#loadHelperType

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlComponentPrivate::loadHelperType() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate14loadHelperTypeEv',
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def hasUnsetRequiredProperties(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponentPrivate::hasUnsetRequiredProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html
    """
    #  bool QQmlComponentPrivate::hasUnsetRequiredProperties() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate26hasUnsetRequiredPropertiesEv',
    )

  def requiredProperties(self) -> Optional[RequiredProperties]:
    """
    Calls Qt's 'RequiredProperties
    *QQmlComponentPrivate::requiredProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#requiredProperties

    Returns
    -------

    Optional[RequiredProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RequiredProperties *QQmlComponentPrivate::requiredProperties() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate18requiredPropertiesEv',
    )
    from . import RequiredProperties
    return RequiredProperties._cuteAt(address)

  def creator(self) -> Optional[QQmlObjectCreator]:
    """
    Calls Qt's 'const QQmlObjectCreator *QQmlComponentPrivate::creator()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#creator

    Returns
    -------

    Optional[QQmlObjectCreator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlObjectCreator *QQmlComponentPrivate::creator() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlComponentPrivate7creatorEv',
    )
    from . import QQmlObjectCreator
    return QQmlObjectCreator._cuteAt(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlComponentPrivate::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlComponentPrivate::engine() const
    address = self.uglySide.call('ritual_ZNK20QQmlComponentPrivate6engineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def setInitialProperty(
      self,
      component: Optional[QObject],
      name: str,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlComponentPrivate::setInitialProperty(QObject
    *component, const QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#setInitialProperty

    Parameters
    ----------

    component : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlComponentPrivate::setInitialProperty(QObject *component,
    #      const QString &name, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate18setInitialPropertyEP7QObjectRK7QS'
        'tringRK8QVariant',
        self._addressOf(component, 'QObject'), name, self._valueOf(value),
    )

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::setProgress(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQmlComponentPrivate::setProgress(qreal progress)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate11setProgressEd', progress,
    )

  @overload(QByteArray, QUrl, QQmlComponent.CompilationMode)
  def setData(
      self,
      data: QByteArray,
      url: QUrl,
      compilationMode: QQmlComponent.CompilationMode,
  ) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::setData(const QByteArray &data,
    const QUrl &url, QQmlComponent::CompilationMode compilationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    compilationMode : QQmlComponent.CompilationMode
      Passed on as its number.
    """
    #  void QQmlComponentPrivate::setData(const QByteArray &data, const QUrl
    #      &url, QQmlComponent::CompilationMode compilationMode)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate7setDataERK10QByteArrayRK4QUrlN13QQ'
        'mlComponent15CompilationModeE',
        self._valueOf(data), self._valueOf(url), compilationMode.value,
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

  def q_func(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlComponentPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#q_func

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlComponentPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQmlComponentPrivate6q_funcEv')
    return QQmlComponent._cuteAt(address)

  @overload(QUrl)
  @overload(QUrl, QQmlComponent.CompilationMode)
  def loadUrl(
      self,
      newUrl: QUrl,
      mode: QQmlComponent.CompilationMode = (
          QQmlComponent.CompilationMode.PreferSynchronous),
  ) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::loadUrl(const QUrl &newUrl,
    QQmlComponent::CompilationMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#loadUrl

    Parameters
    ----------

    newUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    mode : QQmlComponent.CompilationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlComponent.CompilationMode.PreferSynchronous.
    """
    #  void QQmlComponentPrivate::loadUrl(const QUrl &newUrl,
    #      QQmlComponent::CompilationMode mode)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate7loadUrlERK4QUrlN13QQmlComponent15C'
        'ompilationModeE',
        self._valueOf(newUrl), mode.value,
    )

  def completeCreate(self) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::completeCreate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#completeCreate
    """
    #  void QQmlComponentPrivate::completeCreate()
    self.uglySide.call('ritual_ZN20QQmlComponentPrivate14completeCreateEv')

  @overload(
      WAIT['QV4.QmlContext'], WAIT['QV4.Value'], QObject, RequiredProperties,
  )
  @overload(WAIT['QV4.QmlContext'], WAIT['QV4.Value'], QObject, NoneType)
  @overload(
      WAIT['QV4.QmlContext'], WAIT['QV4.Value'], NoneType,
      RequiredProperties,
  )
  @overload(WAIT['QV4.QmlContext'], WAIT['QV4.Value'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.Value'], QObject, RequiredProperties)
  @overload(NoneType, WAIT['QV4.Value'], QObject, NoneType)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, RequiredProperties)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, NoneType)
  def initializeObjectWithInitialProperties(
      self,
      qmlContext: Optional[QV4.QmlContext],
      valuemap: QV4.Value,
      toCreate: Optional[QObject],
      requiredProperties: Optional[RequiredProperties],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlComponentPrivate::initializeObjectWithInitialProperties(QV4::
    QmlContext *qmlContext, const QV4::Value &valuemap, QObject *toCreate,
    RequiredProperties *requiredProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html

    Parameters
    ----------

    qmlContext : Optional[QV4.QmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valuemap : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    toCreate : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requiredProperties : Optional[RequiredProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponentPrivate::initializeObjectWithInitialProperties(QV4::
    #      QmlContext *qmlContext, const QV4::Value &valuemap, QObject
    #      *toCreate, RequiredProperties *requiredProperties)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate37initializeObjectWithInitialProper'
        'tiesEPN3QV410QmlContextERKNS0_5ValueEP7QObjectP18RequiredPropertie'
        's',
        self._addressOf(qmlContext), self._valueOf(valuemap),
        self._addressOf(toCreate, 'QObject'),
        self._addressOf(requiredProperties),
    )

  @overload(QQmlNotifyingBlob)
  @overload(NoneType)
  def ready(self, a0: Optional[QQmlNotifyingBlob]) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::ready(QQmlNotifyingBlob *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#ready

    Parameters
    ----------

    a0 : Optional[QQmlNotifyingBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponentPrivate::ready(QQmlNotifyingBlob *a0)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate5readyEP17QQmlNotifyingBlob',
        self._addressOf(a0),
    )

  @overload(QQmlNotifyingBlob, float)
  @overload(NoneType, float)
  def progress(self, a0: Optional[QQmlNotifyingBlob], a1: float) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::progress(QQmlNotifyingBlob *a0,
    qreal a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#progress

    Parameters
    ----------

    a0 : Optional[QQmlNotifyingBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : float
      Passed on as it is.
    """
    #  void QQmlComponentPrivate::progress(QQmlNotifyingBlob *a0, qreal a1)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate8progressEP17QQmlNotifyingBlobd',
        self._addressOf(a0), a1,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlComponentPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentprivate.html#clear
    """
    #  void QQmlComponentPrivate::clear()
    self.uglySide.call('ritual_ZN20QQmlComponentPrivate5clearEv')

  @overload(QQmlComponent, QQmlContext)
  @overload(QQmlComponent, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def doBeginCreate(
      self,
      q: Optional[QQmlComponent],
      context: Optional[QQmlContext],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponentPrivate::doBeginCreate(QQmlComponent
    *q, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#doBeginCreate

    Parameters
    ----------

    q : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponentPrivate::doBeginCreate(QQmlComponent *q,
    #      QQmlContext *context)
    address = self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate13doBeginCreateEP13QQmlComponentP11'
        'QQmlContext',
        self._addressOf(q), self._addressOf(context),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QObject, QMap[str, QVariant], QQmlContext, CreateBehavior)
  @overload(QObject, QMap[str, QVariant], NoneType, CreateBehavior)
  @overload(NoneType, QMap[str, QVariant], QQmlContext, CreateBehavior)
  @overload(NoneType, QMap[str, QVariant], NoneType, CreateBehavior)
  def createWithProperties(
      self,
      parent: Optional[QObject],
      properties: QMap[str, QVariant],
      context: Optional[QQmlContext],
      behavior: CreateBehavior,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponentPrivate::createWithProperties(QObject
    *parent, const QVariantMap &properties, QQmlContext *context,
    CreateBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#createWithProperties

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    behavior : CreateBehavior
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponentPrivate::createWithProperties(QObject *parent,
    #      const QVariantMap &properties, QQmlContext *context,
    #      CreateBehavior behavior)
    address = self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate20createWithPropertiesEP7QObjectRK4'
        'QMapI7QString8QVariantEP11QQmlContextNS_14CreateBehaviorE',
        self._addressOf(parent, 'QObject'), self._valueOf(properties),
        self._addressOf(context), behavior.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(str, str, QQmlTypeLoader.Mode)
  def prepareLoadFromModule(
      self,
      uri: str,
      typeName: str,
      mode: QQmlTypeLoader.Mode,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlComponentPrivate::prepareLoadFromModule(QAnyStringView uri,
    QAnyStringView typeName, QQmlTypeLoader::Mode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#prepareLoadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QQmlTypeLoader.Mode
      Passed on as its number.
    """
    #  void QQmlComponentPrivate::prepareLoadFromModule(QAnyStringView uri,
    #      QAnyStringView typeName, QQmlTypeLoader::Mode mode)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate21prepareLoadFromModuleE14QAnyStrin'
        'gViewS0_N14QQmlTypeLoader4ModeE',
        uri, typeName, mode.value,
    )

  @overload(str, str)
  def completeLoadFromModule(self, uri: str, typeName: str) -> None:
    """
    Calls Qt's 'void
    QQmlComponentPrivate::completeLoadFromModule(QAnyStringView uri,
    QAnyStringView typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentprivate.html#completeLoadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlComponentPrivate::completeLoadFromModule(QAnyStringView uri,
    #      QAnyStringView typeName)
    self.uglySide.call(
        'ritual_ZN20QQmlComponentPrivate22completeLoadFromModuleE14QAnyStri'
        'ngViewS0_',
        uri, typeName,
    )

  @staticmethod
  def beginCreate(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQmlComponentPrivate::beginCreate(QQmlRefPointer<QQmlContextData> a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.beginCreate' has no cute function yet. Qt's "
        "'QObject "
        "*QQmlComponentPrivate::beginCreate(QQmlRefPointer<QQmlContextData> "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def beginDeferred(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentPrivate::beginDeferred(QQmlEnginePrivate
    *enginePriv, QObject *object, DeferredState *deferredState)': names
    'QQmlComponentPrivate::DeferredState', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.beginDeferred' has no cute function yet. "
        "Qt's 'void QQmlComponentPrivate::beginDeferred(QQmlEnginePrivate "
        "*enginePriv, QObject *object, DeferredState *deferredState)': "
        "names 'QQmlComponentPrivate::DeferredState', which has no cute "
        "class yet.")

  @staticmethod
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlComponentPrivate::compilationUnit() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.compilationUnit' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "QQmlComponentPrivate::compilationUnit() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def completeDeferred(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentPrivate::completeDeferred(QQmlEnginePrivate
    *enginePriv, DeferredState *deferredState)': names
    'QQmlComponentPrivate::DeferredState', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.completeDeferred' has no cute function yet. "
        "Qt's 'void "
        "QQmlComponentPrivate::completeDeferred(QQmlEnginePrivate "
        "*enginePriv, DeferredState *deferredState)': names "
        "'QQmlComponentPrivate::DeferredState', which has no cute class yet."
    )

  @staticmethod
  def fromTypeData(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentPrivate::fromTypeData(const
    QQmlRefPointer<QQmlTypeData> &data)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.fromTypeData' has no cute function yet. Qt's "
        "'void QQmlComponentPrivate::fromTypeData(const "
        "QQmlRefPointer<QQmlTypeData> &data)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def incubateObject(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentPrivate::incubateObject(QQmlIncubator
    *incubationTask, QQmlComponent *component, QQmlEngine *engine, const
    QQmlRefPointer<QQmlContextData> &context, const
    QQmlRefPointer<QQmlContextData> &forContext)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.incubateObject' has no cute function yet. "
        "Qt's 'void QQmlComponentPrivate::incubateObject(QQmlIncubator "
        "*incubationTask, QQmlComponent *component, QQmlEngine *engine, "
        "const QQmlRefPointer<QQmlContextData> &context, const "
        "QQmlRefPointer<QQmlContextData> &forContext)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def removePropertyFromRequired(*__, **_) -> Never:
    """
    Qt's 'QQmlProperty
    QQmlComponentPrivate::removePropertyFromRequired(QObject *target, const
    QString &name, RequiredProperties *requiredProperties, QQmlEngine
    *engine, bool *wasInRequiredProperties)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.removePropertyFromRequired' has no cute "
        "function yet. Qt's 'QQmlProperty "
        "QQmlComponentPrivate::removePropertyFromRequired(QObject *target, "
        "const QString &name, RequiredProperties *requiredProperties, "
        "QQmlEngine *engine, bool *wasInRequiredProperties)': takes a "
        "number to change where it is.")

  @staticmethod
  def setCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentPrivate::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.setCompilationUnit' has no cute function "
        "yet. Qt's 'void QQmlComponentPrivate::setCompilationUnit(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setCreationContext(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlComponentPrivate::setCreationContext(QQmlRefPointer<QQmlContextData>
    creationContext)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentPrivate.setCreationContext' has no cute function "
        "yet. Qt's 'void "
        "QQmlComponentPrivate::setCreationContext(QQmlRefPointer<QQmlContext"
        "Data> creationContext)': takes a type Python has no way to hand "
        "over yet.")
