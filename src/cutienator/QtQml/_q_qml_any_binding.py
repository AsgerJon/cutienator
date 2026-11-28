"""
QQmlAnyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlAnyBinding to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QUntypedPropertyBinding
  from . import QQmlAbstractBinding, QQmlContext, QQmlProperty
  from . import QQmlPropertyIndex, QQmlScriptString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlProperty = WAIT['QQmlProperty']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAnyBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAnyBinding: a plain Python object standing in
  front of one C++ QQmlAnyBinding.

  C++ hands a QQmlAnyBinding around as a copy, so every C++ QQmlAnyBinding
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlAnyBinding that has a ritual and that Python can
  call so far, 17 names in all: 'ofProperty', 'takeFrom',
  'createFromScriptString', 'removeBindingFrom', 'installOn', 'hasError',
  'isSticky', 'setSticky', '__bool__', 'isAbstractPropertyBinding',
  'isUntypedPropertyBinding', 'asUntypedPropertyBinding',
  'asAbstractBinding', 'refresh', '__eq__', '__ne__', 'clear'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAnyBinding::QQmlAnyBinding(std::nullptr_t a0)': takes in Python
    what 'QQmlAnyBinding::QQmlAnyBinding()' takes.
  - Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromFunction(const
    QQmlProperty &prop, QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromCodeString(const
    QQmlProperty &prop, const QString &code, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16
    lineNumber)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlAnyBinding QQmlAnyBinding::createTranslationBinding(const
    QQmlProperty &prop, const QQmlRefPointer<QV4::ExecutableCompilationUnit>
    &compilationUnit, const QV4::CompiledData::Binding *translationBinding,
    QObject *scopeObject, QQmlRefPointer<QQmlContextData> context)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(std::nullptr_t a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(QQmlAbstractBinding
    *binding)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(const
    QQmlAbstractBinding::Ptr &binding)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(QQmlAbstractBinding::Ptr
    &&binding)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(const
    QUntypedPropertyBinding &untypedBinding)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(QUntypedPropertyBinding
    &&untypedBinding)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'QQmlAnyBinding::QQmlAnyBinding(QQmlAnyBinding &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(QQmlAnyBinding &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QQmlAnyBinding::swap(QQmlAnyBinding &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlAnyBinding &QQmlAnyBinding::operator=(const QQmlAnyBinding
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlAnyBinding::~QQmlAnyBinding()': the destructor: Python removes
    its C++ QQmlAnyBinding by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlAnyBinding is created at the first use, not by
    'QQmlAnyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlAnyBinding back gives a copy the ritual made for
    Python, in a new cute QQmlAnyBinding.
  - Each name of Qt's QQmlAnyBinding that has no cute function yet,
    'createFromCodeString', 'createFromFunction', 'createTranslationBinding',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlAnyBinding, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InterceptorMode(CuteNum):
    """
    The enum 'QQmlAnyBinding::InterceptorMode' of Qt, with the 2 names Qt
    gives in it.
    """

    IgnoreInterceptors = Kee[int](0)
    RespectInterceptors = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlProperty)
  def ofProperty(prop: QQmlProperty) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQmlAnyBinding::ofProperty(const QQmlProperty
    &prop)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#ofProperty

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQmlAnyBinding::ofProperty(const QQmlProperty &prop)
    address = Rituals.call(
        'ritual_ZN14QQmlAnyBinding10ofPropertyERK12QQmlProperty',
        CuteMixin._valueOf(prop),
    )
    return QQmlAnyBinding._cuteOwning(address)

  @staticmethod
  @overload(QObject, QQmlPropertyIndex)
  @overload(NoneType, QQmlPropertyIndex)
  def ofProperty(
      object: Optional[QObject],
      index: QQmlPropertyIndex,
  ) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQmlAnyBinding::ofProperty(QObject *object,
    QQmlPropertyIndex index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#ofProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQmlAnyBinding::ofProperty(QObject *object,
    #      QQmlPropertyIndex index)
    address = Rituals.call(
        'ritual_ZN14QQmlAnyBinding10ofPropertyEP7QObject17QQmlPropertyIndex',
        CuteMixin._addressOf(object, 'QObject'), CuteMixin._valueOf(index),
    )
    return QQmlAnyBinding._cuteOwning(address)

  @staticmethod
  @overload(QQmlProperty)
  def takeFrom(prop: QQmlProperty) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQmlAnyBinding::takeFrom(const QQmlProperty
    &prop)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#takeFrom

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQmlAnyBinding::takeFrom(const QQmlProperty &prop)
    address = Rituals.call(
        'ritual_ZN14QQmlAnyBinding8takeFromERK12QQmlProperty',
        CuteMixin._valueOf(prop),
    )
    return QQmlAnyBinding._cuteOwning(address)

  @staticmethod
  @overload(QQmlProperty, QQmlScriptString, QObject, QQmlContext)
  @overload(QQmlProperty, QQmlScriptString, QObject, NoneType)
  @overload(QQmlProperty, QQmlScriptString, NoneType, QQmlContext)
  @overload(QQmlProperty, QQmlScriptString, NoneType, NoneType)
  def createFromScriptString(
      prop: QQmlProperty,
      script: QQmlScriptString,
      obj: Optional[QObject],
      ctxt: Optional[QQmlContext],
  ) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromScriptString(const
    QQmlProperty &prop, const QQmlScriptString &script, QObject *obj,
    QQmlContext *ctxt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#createFromScriptString

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    script : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctxt : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQmlAnyBinding::createFromScriptString(const
    #      QQmlProperty &prop, const QQmlScriptString &script, QObject *obj,
    #      QQmlContext *ctxt)
    address = Rituals.call(
        'ritual_ZN14QQmlAnyBinding22createFromScriptStringERK12QQmlProperty'
        'RK16QQmlScriptStringP7QObjectP11QQmlContext',
        CuteMixin._valueOf(prop), CuteMixin._valueOf(script),
        CuteMixin._addressOf(obj, 'QObject'), CuteMixin._addressOf(ctxt),
    )
    return QQmlAnyBinding._cuteOwning(address)

  @staticmethod
  @overload(QQmlProperty)
  def removeBindingFrom(prop: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlAnyBinding::removeBindingFrom(const QQmlProperty
    &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#removeBindingFrom

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlAnyBinding::removeBindingFrom(const QQmlProperty &prop)
    Rituals.call(
        'ritual_ZN14QQmlAnyBinding17removeBindingFromERK12QQmlProperty',
        CuteMixin._valueOf(prop),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAnyBinding'

  #  Qt's '~QQmlAnyBinding()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlAnyBinding behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QQmlAnyBindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSticky(self) -> bool:
    """
    Calls Qt's 'bool QQmlAnyBinding::isSticky() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#isSticky
    """
    #  bool QQmlAnyBinding::isSticky() const
    return self.uglySide.call('ritual_ZNK14QQmlAnyBinding8isStickyEv')

  def isAbstractPropertyBinding(self) -> bool:
    """
    Calls Qt's 'bool QQmlAnyBinding::isAbstractPropertyBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#isAbstractPropertyBinding
    """
    #  bool QQmlAnyBinding::isAbstractPropertyBinding() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlAnyBinding25isAbstractPropertyBindingEv',
    )

  def isUntypedPropertyBinding(self) -> bool:
    """
    Calls Qt's 'bool QQmlAnyBinding::isUntypedPropertyBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#isUntypedPropertyBinding
    """
    #  bool QQmlAnyBinding::isUntypedPropertyBinding() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlAnyBinding24isUntypedPropertyBindingEv',
    )

  def asUntypedPropertyBinding(self) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding
    QQmlAnyBinding::asUntypedPropertyBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#asUntypedPropertyBinding

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding QQmlAnyBinding::asUntypedPropertyBinding()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlAnyBinding24asUntypedPropertyBindingEv',
    )
    from ..QtCore import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  def asAbstractBinding(self) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding *QQmlAnyBinding::asAbstractBinding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlanybinding.html#asAbstractBinding

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding *QQmlAnyBinding::asAbstractBinding() const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlAnyBinding17asAbstractBindingEv',
    )
    from . import QQmlAbstractBinding
    return QQmlAbstractBinding._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setSticky(self, sticky: bool = True) -> None:
    """
    Calls Qt's 'void QQmlAnyBinding::setSticky(bool sticky)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#setSticky

    Parameters
    ----------

    sticky : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlAnyBinding::setSticky(bool sticky)
    self.uglySide.call('ritual_ZN14QQmlAnyBinding9setStickyEb', sticky)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QQmlAnyBinding::operator bool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#operator bool
    """
    #  bool QQmlAnyBinding::operator bool() const
    return self.uglySide.call('ritual_ZNK14QQmlAnyBindingcvbEv')

  @overload(THIS)
  def __eq__(self, p2: QQmlAnyBinding) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlAnyBinding &p1, const
    QQmlAnyBinding &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#operator==

    Parameters
    ----------

    p2 : QQmlAnyBinding
      Passed on as a value: Qt reads the C++ QQmlAnyBinding, which stays
      Python's own.
    """
    #  bool operator==(const QQmlAnyBinding &p1, const QQmlAnyBinding &p2)
    return Rituals.call(
        'ritual_ZeqRK14QQmlAnyBindingS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, p2: QQmlAnyBinding) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlAnyBinding &p1, const
    QQmlAnyBinding &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#operator!=

    Parameters
    ----------

    p2 : QQmlAnyBinding
      Passed on as a value: Qt reads the C++ QQmlAnyBinding, which stays
      Python's own.
    """
    #  bool operator!=(const QQmlAnyBinding &p1, const QQmlAnyBinding &p2)
    return Rituals.call(
        'ritual_ZneRK14QQmlAnyBindingS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlAnyBinding::QQmlAnyBinding()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#QQmlAnyBinding
    """
    #  QQmlAnyBinding::QQmlAnyBinding()
    self._noteCreation(QQmlAnyBinding, lambda: Rituals.call(
        'ritual_ZN14QQmlAnyBindingC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQmlAnyBinding) -> None:
    """
    Notes what was given, for Qt's 'QQmlAnyBinding::QQmlAnyBinding(const
    QQmlAnyBinding &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#QQmlAnyBinding

    Parameters
    ----------

    other : QQmlAnyBinding
      Passed on as a value: Qt reads the C++ QQmlAnyBinding, which stays
      Python's own.
    """
    #  QQmlAnyBinding::QQmlAnyBinding(const QQmlAnyBinding &other)
    self._noteCreation(QQmlAnyBinding, lambda: Rituals.call(
        'ritual_ZN14QQmlAnyBindingC1ERKS_', self._valueOf(other),
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

  @overload(QQmlProperty)
  @overload(QQmlProperty, InterceptorMode)
  def installOn(
      self,
      target: QQmlProperty,
      mode: InterceptorMode = InterceptorMode.IgnoreInterceptors,
  ) -> None:
    """
    Calls Qt's 'void QQmlAnyBinding::installOn(const QQmlProperty &target,
    InterceptorMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#installOn

    Parameters
    ----------

    target : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    mode : InterceptorMode
      Passed on as its number. May be left out, as in Qt: it is then
      InterceptorMode.IgnoreInterceptors.
    """
    #  void QQmlAnyBinding::installOn(const QQmlProperty &target,
    #      InterceptorMode mode)
    self.uglySide.call(
        'ritual_ZN14QQmlAnyBinding9installOnERK12QQmlPropertyNS_15Intercept'
        'orModeE',
        self._valueOf(target), mode.value,
    )

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QQmlAnyBinding::hasError()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#hasError
    """
    #  bool QQmlAnyBinding::hasError()
    return self.uglySide.call('ritual_ZN14QQmlAnyBinding8hasErrorEv')

  def refresh(self) -> None:
    """
    Calls Qt's 'void QQmlAnyBinding::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#refresh
    """
    #  void QQmlAnyBinding::refresh()
    self.uglySide.call('ritual_ZN14QQmlAnyBinding7refreshEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlAnyBinding::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlanybinding.html#clear
    """
    #  void QQmlAnyBinding::clear()
    self.uglySide.call('ritual_ZN14QQmlAnyBinding5clearEv')

  @staticmethod
  def createFromCodeString(*__, **_) -> Never:
    """
    Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromCodeString(const
    QQmlProperty &prop, const QString &code, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16
    lineNumber)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAnyBinding.createFromCodeString' has no cute function yet. "
        "Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromCodeString(const "
        "QQmlProperty &prop, const QString &code, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16 "
        "lineNumber)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createFromFunction(*__, **_) -> Never:
    """
    Qt's 'QQmlAnyBinding QQmlAnyBinding::createFromFunction(const
    QQmlProperty &prop, QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAnyBinding.createFromFunction' has no cute function yet. Qt's "
        "'QQmlAnyBinding QQmlAnyBinding::createFromFunction(const "
        "QQmlProperty &prop, QV4::Function *function, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext "
        "*scope)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createTranslationBinding(*__, **_) -> Never:
    """
    Qt's 'QQmlAnyBinding QQmlAnyBinding::createTranslationBinding(const
    QQmlProperty &prop, const QQmlRefPointer<QV4::ExecutableCompilationUnit>
    &compilationUnit, const QV4::CompiledData::Binding *translationBinding,
    QObject *scopeObject, QQmlRefPointer<QQmlContextData> context)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAnyBinding.createTranslationBinding' has no cute function "
        "yet. Qt's 'QQmlAnyBinding "
        "QQmlAnyBinding::createTranslationBinding(const QQmlProperty &prop, "
        "const QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "&compilationUnit, const QV4::CompiledData::Binding "
        "*translationBinding, QObject *scopeObject, "
        "QQmlRefPointer<QQmlContextData> context)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QQmlAnyBinding::swap(QQmlAnyBinding &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAnyBinding.swap' has no cute function yet. Qt's 'void "
        "QQmlAnyBinding::swap(QQmlAnyBinding &other)': takes a type Python "
        "has no way to hand over yet.")
