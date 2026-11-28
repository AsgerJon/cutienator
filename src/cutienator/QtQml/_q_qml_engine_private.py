"""
QQmlEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlEnginePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QJSEnginePrivate, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QUrl
  from . import QQmlContext, QQmlEngine, QQmlError, QQmlGadgetPtrWrapper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QQmlContext = WAIT['QQmlContext']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlError = WAIT['QQmlError']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEnginePrivate(QJSEnginePrivate):
  """
  The cute side of Qt's QQmlEnginePrivate: a plain Python object standing in
  front of one C++ QQmlEnginePrivate.

  It is built on the cute 'QJSEnginePrivate', as Qt's QQmlEnginePrivate is
  built on Qt's QJSEnginePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlEnginePrivate that has a ritual and that Python
  can call so far, 15 names in all: 'q_func', 'init',
  '_qt_property_translationLanguage_offset', 'referenceScarceResources',
  'dereferenceScarceResources', 'offlineStorageDatabaseDirectory',
  'sendQuit', 'sendExit', 'warning', 'get', 'designerMode',
  'activateDesignerMode', 'valueTypeInstance', 'compilationUnitFromUrl',
  'cleanupScarceResources'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlEngine *QQmlEnginePrivate::q_func() const': takes in
    Python what 'QQmlEngine *QQmlEnginePrivate::q_func()' takes.
  - Qt's 'QQmlEnginePrivate::~QQmlEnginePrivate()': the destructor: Python
    never removes a C++ QQmlEnginePrivate.
  - Qt's 'QSharedPointer<QQmlImageProviderBase>
    QQmlEnginePrivate::imageProvider(const QString &providerId) const': gives
    a type Python has no way to take yet.
  - Qt's 'void QQmlEnginePrivate::incubate(QQmlIncubator &a0, const
    QQmlRefPointer<QQmlContextData> &a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QQmlEnginePrivate *QQmlEnginePrivate::get(const QQmlEngine
    *e)': takes in Python what 'QQmlEnginePrivate
    *QQmlEnginePrivate::get(QQmlEngine *e)' takes.
  - Qt's 'QQmlEnginePrivate *QQmlEnginePrivate::get(const
    QQmlRefPointer<QQmlContextData> &c)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<QQmlError> QQmlEnginePrivate::qmlErrorFromDiagnostics(const
    QString &fileName, const QList<QQmlJS::DiagnosticMessage>
    &diagnosticMessages)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlEnginePrivate::executeRuntimeFunction(const QUrl &url,
    qsizetype functionIndex, QObject *thisObject, int argc, void **args,
    QMetaType *types)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlEnginePrivate::executeRuntimeFunction(const
    QV4::ExecutableCompilationUnit *unit, qsizetype functionIndex, QObject
    *thisObject, int argc, void **args, QMetaType *types)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlEnginePrivate::createBareContext(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlRefPointer<QQmlContextData> &parentContext, int subComponentIndex)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlEnginePrivate::createComponentRootContext(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlRefPointer<QQmlContextData> &parentContex, int subComponentIndex)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlEnginePrivate::setInternalContext(QObject *This, const
    QQmlRefPointer<QQmlContextData> &context, QQmlContextData::QmlObjectKind
    kind)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 1 a template; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlEnginePrivate is created at the first use, not by
    'QQmlEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlEnginePrivate.
  - Each name of Qt's QQmlEnginePrivate that has no cute function yet,
    'createBareContext', 'createComponentRootContext',
    'executeRuntimeFunction', 'imageProvider', 'incubate',
    'qmlErrorFromDiagnostics', 'setInternalContext', 'singletonInstance',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QQmlEnginePrivate, each a class in here as
  #  in C++.

  class Incubator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlEnginePrivate::Incubator: a plain Python object
    standing in front of one C++ QQmlEnginePrivate::Incubator.

    C++ hands a QQmlEnginePrivate::Incubator around as a copy, so every C++
    QQmlEnginePrivate::Incubator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlEnginePrivate::Incubator yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlEnginePrivate::Incubator::~Incubator()': the destructor:
      Python removes its C++ QQmlEnginePrivate::Incubator by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlEnginePrivate::Incubator is created at the first use, not
      by 'QQmlEnginePrivate::Incubator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlEnginePrivate::Incubator back gives a copy the
      ritual made for Python, in a new cute QQmlEnginePrivate::Incubator.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlEnginePrivate::Incubator'

    #  Qt's '~QQmlEnginePrivate::Incubator()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlEnginePrivate::Incubator behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlEnginePrivate9IncubatorD1Ev'

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
  def _qt_property_translationLanguage_offset() -> int:
    """
    Calls Qt's 'size_t
    QQmlEnginePrivate::_qt_property_translationLanguage_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html
    """
    #  size_t QQmlEnginePrivate::_qt_property_translationLanguage_offset()
    return Rituals.call(
        'ritual_ZN17QQmlEnginePrivate39_qt_property_translationLanguage_off'
        'setEv',
    )

  @staticmethod
  @overload(QQmlEngine)
  @overload(NoneType)
  def get(e: Optional[QQmlEngine]) -> Optional[QQmlEnginePrivate]:
    """
    Calls Qt's 'QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#get

    Parameters
    ----------

    e : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlEngine *e)
    address = Rituals.call(
        'ritual_ZN17QQmlEnginePrivate3getEP10QQmlEngine',
        CuteMixin._addressOf(e),
    )
    return QQmlEnginePrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  def get(p: Optional[QQmlEnginePrivate]) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlEnginePrivate::get(QQmlEnginePrivate *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#get

    Parameters
    ----------

    p : Optional[QQmlEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlEnginePrivate::get(QQmlEnginePrivate *p)
    address = Rituals.call(
        'ritual_ZN17QQmlEnginePrivate3getEPS_', CuteMixin._addressOf(p),
    )
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  def get(e: Optional[QV4.ExecutionEngine]) -> Optional[QQmlEnginePrivate]:
    """
    Calls Qt's 'QQmlEnginePrivate
    *QQmlEnginePrivate::get(QV4::ExecutionEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#get

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEnginePrivate *QQmlEnginePrivate::get(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN17QQmlEnginePrivate3getEPN3QV415ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QQmlEnginePrivate._cuteAt(address)

  @staticmethod
  @overload(QQmlContext)
  def get(c: Optional[QQmlContext]) -> Optional[QQmlEnginePrivate]:
    """
    Calls Qt's 'QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlContext *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#get

    Parameters
    ----------

    c : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEnginePrivate *QQmlEnginePrivate::get(QQmlContext *c)
    address = Rituals.call(
        'ritual_ZN17QQmlEnginePrivate3getEP11QQmlContext',
        CuteMixin._addressOf(c),
    )
    return QQmlEnginePrivate._cuteAt(address)

  @staticmethod
  def designerMode() -> bool:
    """
    Calls Qt's 'bool QQmlEnginePrivate::designerMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#designerMode
    """
    #  bool QQmlEnginePrivate::designerMode()
    return Rituals.call('ritual_ZN17QQmlEnginePrivate12designerModeEv')

  @staticmethod
  def activateDesignerMode() -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::activateDesignerMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#activateDesignerMode
    """
    #  void QQmlEnginePrivate::activateDesignerMode()
    Rituals.call('ritual_ZN17QQmlEnginePrivate20activateDesignerModeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offlineStorageDatabaseDirectory(self) -> str:
    """
    Calls Qt's 'QString QQmlEnginePrivate::offlineStorageDatabaseDirectory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlEnginePrivate::offlineStorageDatabaseDirectory() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlEnginePrivate31offlineStorageDatabaseDirectoryEv',
    )

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

  def q_func(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#q_func

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQmlEnginePrivate6q_funcEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#init
    """
    #  void QQmlEnginePrivate::init()
    self.uglySide.call('ritual_ZN17QQmlEnginePrivate4initEv')

  def referenceScarceResources(self) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::referenceScarceResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#referenceScarceResources
    """
    #  void QQmlEnginePrivate::referenceScarceResources()
    self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate24referenceScarceResourcesEv',
    )

  def dereferenceScarceResources(self) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::dereferenceScarceResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#dereferenceScarceResources
    """
    #  void QQmlEnginePrivate::dereferenceScarceResources()
    self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate26dereferenceScarceResourcesEv',
    )

  def sendQuit(self) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::sendQuit()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#sendQuit
    """
    #  void QQmlEnginePrivate::sendQuit()
    self.uglySide.call('ritual_ZN17QQmlEnginePrivate8sendQuitEv')

  @overload()
  @overload(int)
  def sendExit(self, retCode: int = 0) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::sendExit(int retCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#sendExit

    Parameters
    ----------

    retCode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQmlEnginePrivate::sendExit(int retCode)
    self.uglySide.call('ritual_ZN17QQmlEnginePrivate8sendExitEi', retCode)

  @overload(QQmlError)
  def warning(self, a0: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(const QQmlError &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlEnginePrivate::warning(const QQmlError &a0)
    self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate7warningERK9QQmlError',
        self._valueOf(a0),
    )

  @overload(QList[QQmlError])
  def warning(self, a0: QList[QQmlError]) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(const QList<QQmlError> &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : QList[QQmlError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEnginePrivate::warning(const QList<QQmlError> &a0)
    self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate7warningERK5QListI9QQmlErrorE',
        self._valueOf(a0),
    )

  @staticmethod
  @overload(QQmlEngine, QQmlError)
  @overload(NoneType, QQmlError)
  def warning(a0: Optional[QQmlEngine], a1: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(QQmlEngine *a0, const
    QQmlError &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlEnginePrivate::warning(QQmlEngine *a0, const QQmlError &a1)
    Rituals.call(
        'ritual_ZN17QQmlEnginePrivate7warningEP10QQmlEngineRK9QQmlError',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
    )

  @staticmethod
  @overload(QQmlEngine, QList[QQmlError])
  @overload(NoneType, QList[QQmlError])
  def warning(a0: Optional[QQmlEngine], a1: QList[QQmlError]) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(QQmlEngine *a0, const
    QList<QQmlError> &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QList[QQmlError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEnginePrivate::warning(QQmlEngine *a0, const QList<QQmlError>
    #      &a1)
    Rituals.call(
        'ritual_ZN17QQmlEnginePrivate7warningEP10QQmlEngineRK5QListI9QQmlEr'
        'rorE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
    )

  @staticmethod
  @overload(THIS, QQmlError)
  def warning(a0: Optional[QQmlEnginePrivate], a1: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const
    QQmlError &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : Optional[QQmlEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const QQmlError
    #      &a1)
    Rituals.call(
        'ritual_ZN17QQmlEnginePrivate7warningEPS_RK9QQmlError',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
    )

  @staticmethod
  @overload(THIS, QList[QQmlError])
  def warning(a0: Optional[QQmlEnginePrivate], a1: QList[QQmlError]) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const
    QList<QQmlError> &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengineprivate.html#warning

    Parameters
    ----------

    a0 : Optional[QQmlEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QList[QQmlError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEnginePrivate::warning(QQmlEnginePrivate *a0, const
    #      QList<QQmlError> &a1)
    Rituals.call(
        'ritual_ZN17QQmlEnginePrivate7warningEPS_RK5QListI9QQmlErrorE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
    )

  @overload(QMetaType)
  def valueTypeInstance(
      self,
      type: QMetaType,
  ) -> Optional[QQmlGadgetPtrWrapper]:
    """
    Calls Qt's 'QQmlGadgetPtrWrapper
    *QQmlEnginePrivate::valueTypeInstance(QMetaType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#valueTypeInstance

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QQmlGadgetPtrWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGadgetPtrWrapper *QQmlEnginePrivate::valueTypeInstance(QMetaType
    #      type)
    address = self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate17valueTypeInstanceE9QMetaType',
        self._valueOf(type),
    )
    from . import QQmlGadgetPtrWrapper
    return QQmlGadgetPtrWrapper._cuteAt(address)

  @overload(QUrl)
  def compilationUnitFromUrl(
      self,
      url: QUrl,
  ) -> Optional[QV4.ExecutableCompilationUnit]:
    """
    Calls Qt's 'QV4::ExecutableCompilationUnit
    *QQmlEnginePrivate::compilationUnitFromUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#compilationUnitFromUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QV4.ExecutableCompilationUnit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutableCompilationUnit
    #      *QQmlEnginePrivate::compilationUnitFromUrl(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate22compilationUnitFromUrlERK4QUrl',
        self._valueOf(url),
    )
    return QV4.ExecutableCompilationUnit._cuteAt(address)

  def cleanupScarceResources(self) -> None:
    """
    Calls Qt's 'void QQmlEnginePrivate::cleanupScarceResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengineprivate.html#cleanupScarceResources
    """
    #  void QQmlEnginePrivate::cleanupScarceResources()
    self.uglySide.call(
        'ritual_ZN17QQmlEnginePrivate22cleanupScarceResourcesEv',
    )

  @staticmethod
  def createBareContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlEnginePrivate::createBareContext(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlRefPointer<QQmlContextData> &parentContext, int subComponentIndex)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.createBareContext' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlEnginePrivate::createBareContext(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const "
        "QQmlRefPointer<QQmlContextData> &parentContext, int "
        "subComponentIndex)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def createComponentRootContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlEnginePrivate::createComponentRootContext(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlRefPointer<QQmlContextData> &parentContex, int subComponentIndex)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.createComponentRootContext' has no cute "
        "function yet. Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlEnginePrivate::createComponentRootContext(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const "
        "QQmlRefPointer<QQmlContextData> &parentContex, int "
        "subComponentIndex)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def executeRuntimeFunction(*__, **_) -> Never:
    """
    - Qt's 'void QQmlEnginePrivate::executeRuntimeFunction(const QUrl &url,
      qsizetype functionIndex, QObject *thisObject, int argc, void **args,
      QMetaType *types)': takes a type Python has no way to hand over yet.
    - Qt's 'void QQmlEnginePrivate::executeRuntimeFunction(const
      QV4::ExecutableCompilationUnit *unit, qsizetype functionIndex, QObject
      *thisObject, int argc, void **args, QMetaType *types)': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.executeRuntimeFunction' has no cute function "
        "yet. Qt's 'void QQmlEnginePrivate::executeRuntimeFunction(const "
        "QUrl &url, qsizetype functionIndex, QObject *thisObject, int argc, "
        "void **args, QMetaType *types)': takes a type Python has no way to "
        "hand over yet. Qt's 'void "
        "QQmlEnginePrivate::executeRuntimeFunction(const "
        "QV4::ExecutableCompilationUnit *unit, qsizetype functionIndex, "
        "QObject *thisObject, int argc, void **args, QMetaType *types)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def imageProvider(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QQmlImageProviderBase>
    QQmlEnginePrivate::imageProvider(const QString &providerId) const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.imageProvider' has no cute function yet. Qt's "
        "'QSharedPointer<QQmlImageProviderBase> "
        "QQmlEnginePrivate::imageProvider(const QString &providerId) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def incubate(*__, **_) -> Never:
    """
    Qt's 'void QQmlEnginePrivate::incubate(QQmlIncubator &a0, const
    QQmlRefPointer<QQmlContextData> &a1)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.incubate' has no cute function yet. Qt's 'void "
        "QQmlEnginePrivate::incubate(QQmlIncubator &a0, const "
        "QQmlRefPointer<QQmlContextData> &a1)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def qmlErrorFromDiagnostics(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlError> QQmlEnginePrivate::qmlErrorFromDiagnostics(const
    QString &fileName, const QList<QQmlJS::DiagnosticMessage>
    &diagnosticMessages)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.qmlErrorFromDiagnostics' has no cute function "
        "yet. Qt's 'QList<QQmlError> "
        "QQmlEnginePrivate::qmlErrorFromDiagnostics(const QString "
        "&fileName, const QList<QQmlJS::DiagnosticMessage> "
        "&diagnosticMessages)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setInternalContext(*__, **_) -> Never:
    """
    Qt's 'void QQmlEnginePrivate::setInternalContext(QObject *This, const
    QQmlRefPointer<QQmlContextData> &context, QQmlContextData::QmlObjectKind
    kind)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.setInternalContext' has no cute function yet. "
        "Qt's 'void QQmlEnginePrivate::setInternalContext(QObject *This, "
        "const QQmlRefPointer<QQmlContextData> &context, "
        "QQmlContextData::QmlObjectKind kind)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def singletonInstance(*__, **_) -> Never:
    """
    Qt's 'QQmlEnginePrivate::singletonInstance': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlEnginePrivate.singletonInstance' has no cute function yet. "
        "Qt's 'QQmlEnginePrivate::singletonInstance': a template: a pattern "
        "and no single function.")
