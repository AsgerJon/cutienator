"""
QQmlPropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyBinding to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QPropertyBindingPrivate
from . import QQmlPropertyBindingBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject, QUntypedPropertyBinding
  from . import QQmlContext, QQmlPropertyBindingJS, QQmlPropertyData
  from . import QQmlPropertyIndex, QQmlScriptString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlPropertyData = WAIT['QQmlPropertyData']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']
  QQmlScriptString = WAIT['QQmlScriptString']
  QUntypedPropertyBinding = WAIT['QUntypedPropertyBinding']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyBinding(QQmlPropertyBindingBase):
  """
  The cute side of Qt's QQmlPropertyBinding: a plain Python object standing
  in front of one C++ QQmlPropertyBinding.

  It is built on the cute 'QQmlPropertyBindingBase', as Qt's
  QQmlPropertyBinding is built on Qt's QQmlPropertyBindingBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyBinding that has a ritual and that
  Python can call so far, 8 names in all: 'jsExpressionOffsetLength',
  'jsExpression', 'createFromScriptString', 'isUndefined', 'hasDependencies',
  'createBindingLoopErrorDescription', 'makeUntyped', 'bindingErrorCallback'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlPropertyBindingJS *QQmlPropertyBinding::jsExpression()
    const': takes in Python what 'QQmlPropertyBindingJS
    *QQmlPropertyBinding::jsExpression()' takes.
  - Qt's 'QUntypedPropertyBinding QQmlPropertyBinding::create(const
    QQmlPropertyData *pd, QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
    QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QUntypedPropertyBinding QQmlPropertyBinding::create(QMetaType
    propertyType, QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
    QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::createFromCodeString(const QQmlPropertyData
    *property, const QString &str, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16
    lineNumber, QObject *target, QQmlPropertyIndex targetIndex)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::createFromBoundFunction(const QQmlPropertyData *pd,
    QV4::BoundFunction *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
    QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QQmlPropertyBinding::handleUndefinedAssignment(QQmlEnginePrivate *ep,
    void *dataPtr)': names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QQmlPropertyBinding is created at the first use, not by
    'QQmlPropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyBinding.
  - Each name of Qt's QQmlPropertyBinding that has no cute function yet,
    'create', 'createFromBoundFunction', 'createFromCodeString',
    'doEvaluate', 'evaluate', 'handleUndefinedAssignment', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def jsExpressionOffsetLength() -> int:
    """
    Calls Qt's 'std::size_t QQmlPropertyBinding::jsExpressionOffsetLength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#jsExpressionOffsetLength
    """
    #  std::size_t QQmlPropertyBinding::jsExpressionOffsetLength()
    return Rituals.call(
        'ritual_ZN19QQmlPropertyBinding24jsExpressionOffsetLengthEv',
    )

  @staticmethod
  @overload(
      QQmlPropertyData, QQmlScriptString, QObject, QQmlContext, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, QObject, QQmlContext, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, QObject, NoneType, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, QObject, NoneType, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, NoneType, QQmlContext, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, NoneType, QQmlContext, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, NoneType, NoneType, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      QQmlPropertyData, QQmlScriptString, NoneType, NoneType, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, QObject, QQmlContext, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, QObject, QQmlContext, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, QObject, NoneType, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, QObject, NoneType, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, NoneType, QQmlContext, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, NoneType, QQmlContext, NoneType,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, NoneType, NoneType, QObject,
      QQmlPropertyIndex,
  )
  @overload(
      NoneType, QQmlScriptString, NoneType, NoneType, NoneType,
      QQmlPropertyIndex,
  )
  def createFromScriptString(
      property: Optional[QQmlPropertyData],
      script: QQmlScriptString,
      obj: Optional[QObject],
      ctxt: Optional[QQmlContext],
      target: Optional[QObject],
      targetIndex: QQmlPropertyIndex,
  ) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::createFromScriptString(const QQmlPropertyData
    *property, const QQmlScriptString &script, QObject *obj, QQmlContext
    *ctxt, QObject *target, QQmlPropertyIndex targetIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#createFromScriptString

    Parameters
    ----------

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    script : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctxt : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding
    #      QQmlPropertyBinding::createFromScriptString(const QQmlPropertyData
    #      *property, const QQmlScriptString &script, QObject *obj,
    #      QQmlContext *ctxt, QObject *target, QQmlPropertyIndex targetIndex)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyBinding22createFromScriptStringEPK16QQmlPro'
        'pertyDataRK16QQmlScriptStringP7QObjectP11QQmlContextS7_17QQmlPrope'
        'rtyIndex',
        CuteMixin._addressOf(property), CuteMixin._valueOf(script),
        CuteMixin._addressOf(obj, 'QObject'), CuteMixin._addressOf(ctxt),
        CuteMixin._addressOf(target, 'QObject'),
        CuteMixin._valueOf(targetIndex),
    )
    from ..QtCore import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  @staticmethod
  @overload(QUntypedPropertyBinding)
  def isUndefined(binding: QUntypedPropertyBinding) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBinding::isUndefined(const
    QUntypedPropertyBinding &binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#isUndefined

    Parameters
    ----------

    binding : QUntypedPropertyBinding
      Passed on as a value: Qt reads the C++ QUntypedPropertyBinding, which
      stays Python's own.
    """
    #  bool QQmlPropertyBinding::isUndefined(const QUntypedPropertyBinding
    #      &binding)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyBinding11isUndefinedERK23QUntypedPropertyBi'
        'nding',
        CuteMixin._valueOf(binding),
    )

  @staticmethod
  @overload(QPropertyBindingPrivate)
  @overload(NoneType)
  def isUndefined(binding: Optional[QPropertyBindingPrivate]) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBinding::isUndefined(const
    QPropertyBindingPrivate *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#isUndefined

    Parameters
    ----------

    binding : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlPropertyBinding::isUndefined(const QPropertyBindingPrivate
    #      *binding)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyBinding11isUndefinedEPK23QPropertyBindingPr'
        'ivate',
        CuteMixin._addressOf(binding),
    )

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def makeUntyped(
      binding: Optional[QQmlPropertyBinding],
  ) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::makeUntyped(QQmlPropertyBinding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#makeUntyped

    Parameters
    ----------

    binding : Optional[QQmlPropertyBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding
    #      QQmlPropertyBinding::makeUntyped(QQmlPropertyBinding *binding)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyBinding11makeUntypedEPS_',
        CuteMixin._addressOf(binding),
    )
    from ..QtCore import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  @staticmethod
  @overload(QPropertyBindingPrivate)
  @overload(NoneType)
  def bindingErrorCallback(a0: Optional[QPropertyBindingPrivate]) -> None:
    """
    Calls Qt's 'void
    QQmlPropertyBinding::bindingErrorCallback(QPropertyBindingPrivate *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#bindingErrorCallback

    Parameters
    ----------

    a0 : Optional[QPropertyBindingPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyBinding::bindingErrorCallback(QPropertyBindingPrivate
    #      *a0)
    Rituals.call(
        'ritual_ZN19QQmlPropertyBinding20bindingErrorCallbackEP23QPropertyB'
        'indingPrivate',
        CuteMixin._addressOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyBinding'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasDependencies(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBinding::hasDependencies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#hasDependencies
    """
    #  bool QQmlPropertyBinding::hasDependencies() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlPropertyBinding15hasDependenciesEv',
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

  @overload(
      QMetaType, QObject, QQmlPropertyIndex,
      QQmlPropertyBindingBase.HasBoundFunction,
  )
  @overload(
      QMetaType, NoneType, QQmlPropertyIndex,
      QQmlPropertyBindingBase.HasBoundFunction,
  )
  def __init__(
      self,
      metaType: QMetaType,
      target: Optional[QObject],
      targetIndex: QQmlPropertyIndex,
      hasBoundFunction: QQmlPropertyBindingBase.HasBoundFunction,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyBinding::QQmlPropertyBinding(QMetaType metaType, QObject
    *target, QQmlPropertyIndex targetIndex, HasBoundFunction
    hasBoundFunction)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#QQmlPropertyBinding

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    hasBoundFunction : QQmlPropertyBindingBase.HasBoundFunction
      Passed on as its number.
    """
    #  QQmlPropertyBinding::QQmlPropertyBinding(QMetaType metaType, QObject
    #      *target, QQmlPropertyIndex targetIndex, HasBoundFunction
    #      hasBoundFunction)
    self._noteCreation(QQmlPropertyBinding, lambda: Rituals.call(
        'ritual_ZN19QQmlPropertyBindingC1E9QMetaTypeP7QObject17QQmlProperty'
        'IndexN23QQmlPropertyBindingBase16HasBoundFunctionE',
        self._valueOf(metaType), self._addressOf(target, 'QObject'),
        self._valueOf(targetIndex), hasBoundFunction.value,
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

  def jsExpression(self) -> Optional[QQmlPropertyBindingJS]:
    """
    Calls Qt's 'QQmlPropertyBindingJS *QQmlPropertyBinding::jsExpression()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html#jsExpression

    Returns
    -------

    Optional[QQmlPropertyBindingJS]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyBindingJS *QQmlPropertyBinding::jsExpression()
    address = self.uglySide.call(
        'ritual_ZN19QQmlPropertyBinding12jsExpressionEv',
    )
    from . import QQmlPropertyBindingJS
    return QQmlPropertyBindingJS._cuteAt(address)

  def createBindingLoopErrorDescription(self) -> str:
    """
    Calls Qt's 'QString
    QQmlPropertyBinding::createBindingLoopErrorDescription()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybinding.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyBinding::createBindingLoopErrorDescription()
    return self.uglySide.call(
        'ritual_ZN19QQmlPropertyBinding33createBindingLoopErrorDescriptionE'
        'v',
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'QUntypedPropertyBinding QQmlPropertyBinding::create(const
      QQmlPropertyData *pd, QV4::Function *function, QObject *obj, const
      QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
      QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QUntypedPropertyBinding QQmlPropertyBinding::create(QMetaType
      propertyType, QV4::Function *function, QObject *obj, const
      QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
      QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.create' has no cute function yet. Qt's "
        "'QUntypedPropertyBinding QQmlPropertyBinding::create(const "
        "QQmlPropertyData *pd, QV4::Function *function, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext "
        "*scope, QObject *target, QQmlPropertyIndex targetIndex)': takes a "
        "type Python has no way to hand over yet. Qt's "
        "'QUntypedPropertyBinding QQmlPropertyBinding::create(QMetaType "
        "propertyType, QV4::Function *function, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext "
        "*scope, QObject *target, QQmlPropertyIndex targetIndex)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def createFromBoundFunction(*__, **_) -> Never:
    """
    Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::createFromBoundFunction(const QQmlPropertyData *pd,
    QV4::BoundFunction *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
    QObject *target, QQmlPropertyIndex targetIndex)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.createFromBoundFunction' has no cute function "
        "yet. Qt's 'QUntypedPropertyBinding "
        "QQmlPropertyBinding::createFromBoundFunction(const "
        "QQmlPropertyData *pd, QV4::BoundFunction *function, QObject *obj, "
        "const QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext "
        "*scope, QObject *target, QQmlPropertyIndex targetIndex)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def createFromCodeString(*__, **_) -> Never:
    """
    Qt's 'QUntypedPropertyBinding
    QQmlPropertyBinding::createFromCodeString(const QQmlPropertyData
    *property, const QString &str, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16
    lineNumber, QObject *target, QQmlPropertyIndex targetIndex)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.createFromCodeString' has no cute function "
        "yet. Qt's 'QUntypedPropertyBinding "
        "QQmlPropertyBinding::createFromCodeString(const QQmlPropertyData "
        "*property, const QString &str, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16 "
        "lineNumber, QObject *target, QQmlPropertyIndex targetIndex)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def doEvaluate(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyBinding::doEvaluate': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.doEvaluate' has no cute function yet. Qt's "
        "'QQmlPropertyBinding::doEvaluate': a template: a pattern and no "
        "single function.")

  @staticmethod
  def evaluate(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyBinding::evaluate': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.evaluate' has no cute function yet. Qt's "
        "'QQmlPropertyBinding::evaluate': a template: a pattern and no "
        "single function.")

  @staticmethod
  def handleUndefinedAssignment(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlPropertyBinding::handleUndefinedAssignment(QQmlEnginePrivate *ep,
    void *dataPtr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyBinding.handleUndefinedAssignment' has no cute "
        "function yet. Qt's 'void "
        "QQmlPropertyBinding::handleUndefinedAssignment(QQmlEnginePrivate "
        "*ep, void *dataPtr)': names 'void', which has no cute class yet.")
