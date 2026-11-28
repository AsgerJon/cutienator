"""
QQmlJSMetaProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSMetaProperty to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList
from ..QtQml import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QQmlJSAnnotation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSAnnotation = WAIT['QQmlJSAnnotation']


class QQmlJSMetaProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSMetaProperty: a plain Python object standing in
  front of one C++ QQmlJSMetaProperty.

  C++ hands a QQmlJSMetaProperty around as a copy, so every C++
  QQmlJSMetaProperty behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSMetaProperty that has a ritual and that Python
  can call so far, 49 names in all: 'setPropertyName', 'propertyName',
  'setTypeName', 'typeName', 'setRead', 'read', 'setWrite', 'write',
  'setReset', 'reset', 'setBindable', 'bindable', 'setNotify', 'notify',
  'setPrivateClass', 'privateClass', 'isPrivate', 'setSourceLocation',
  'sourceLocation', 'setAnnotations', 'annotations', 'setIsList', 'isList',
  'setIsWritable', 'isWritable', 'setIsPointer', 'isPointer',
  'setIsTypeConstant', 'isTypeConstant', 'setAliasExpression',
  'aliasExpression', 'isAlias', 'setAliasTargetName', 'aliasTargetName',
  'setIsFinal', 'isFinal', 'setIsOverride', 'isOverride', 'setIsVirtual',
  'isVirtual', 'setIsPropertyConstant', 'isPropertyConstant', 'setRevision',
  'revision', 'setIndex', 'index', 'isValid', '__eq__', '__ne__'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJSMetaProperty::setType(const QDeferredSharedPointer<const
    QQmlJSScope> &type)': takes a type Python has no way to hand over yet.
  - Qt's 'QDeferredSharedPointer<const QQmlJSScope>
    QQmlJSMetaProperty::type() const': gives a type Python has no way to take
    yet.
  - Qt's 'void QQmlJSMetaProperty::setAliasTargetScope(const
    QSharedPointer<const QQmlJSScope> &scope)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaProperty::aliasTargetScope() const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlJSMetaProperty::~QQmlJSMetaProperty()': the destructor: Python
    removes its C++ QQmlJSMetaProperty by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSMetaProperty is created at the first use, not by
    'QQmlJSMetaProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSMetaProperty back gives a copy the ritual made
    for Python, in a new cute QQmlJSMetaProperty.
  - Each name of Qt's QQmlJSMetaProperty that has no cute function yet,
    'aliasTargetScope', 'setAliasTargetScope', 'setType', 'type', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSMetaProperty'

  #  Qt's '~QQmlJSMetaProperty()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSMetaProperty behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlJSMetaPropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::propertyName() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty12propertyNameEv',
    )

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::typeName() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty8typeNameEv')

  def read(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::read() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#read

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::read() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty4readEv')

  def write(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::write() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#write

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::write() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty5writeEv')

  def reset(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::reset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#reset

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::reset() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty5resetEv')

  def bindable(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::bindable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#bindable

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::bindable() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty8bindableEv')

  def notify(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::notify() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#notify

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::notify() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty6notifyEv')

  def privateClass(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::privateClass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#privateClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::privateClass() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty12privateClassEv',
    )

  def isPrivate(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isPrivate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isPrivate
    """
    #  bool QQmlJSMetaProperty::isPrivate() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty9isPrivateEv')

  def sourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSMetaProperty::sourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#sourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSMetaProperty::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty14sourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def annotations(self) -> QList[QQmlJSAnnotation]:
    """
    Calls Qt's 'const QList<QQmlJSAnnotation>
    &QQmlJSMetaProperty::annotations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#annotations

    Returns
    -------

    QList[QQmlJSAnnotation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QQmlJSAnnotation> &QQmlJSMetaProperty::annotations() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty11annotationsEv',
    )
    from . import QQmlJSAnnotation
    return QList[QQmlJSAnnotation]._cuteOwning(address)

  def isList(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isList
    """
    #  bool QQmlJSMetaProperty::isList() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty6isListEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isWritable
    """
    #  bool QQmlJSMetaProperty::isWritable() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty10isWritableEv')

  def isPointer(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isPointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isPointer
    """
    #  bool QQmlJSMetaProperty::isPointer() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty9isPointerEv')

  def isTypeConstant(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isTypeConstant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isTypeConstant
    """
    #  bool QQmlJSMetaProperty::isTypeConstant() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty14isTypeConstantEv',
    )

  def aliasExpression(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::aliasExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#aliasExpression

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::aliasExpression() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty15aliasExpressionEv',
    )

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isAlias
    """
    #  bool QQmlJSMetaProperty::isAlias() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty7isAliasEv')

  def aliasTargetName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaProperty::aliasTargetName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#aliasTargetName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaProperty::aliasTargetName() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty15aliasTargetNameEv',
    )

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isFinal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isFinal
    """
    #  bool QQmlJSMetaProperty::isFinal() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty7isFinalEv')

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isOverride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isOverride
    """
    #  bool QQmlJSMetaProperty::isOverride() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty10isOverrideEv')

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isVirtual() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isVirtual
    """
    #  bool QQmlJSMetaProperty::isVirtual() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty9isVirtualEv')

  def isPropertyConstant(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isPropertyConstant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isPropertyConstant
    """
    #  bool QQmlJSMetaProperty::isPropertyConstant() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSMetaProperty18isPropertyConstantEv',
    )

  def revision(self) -> int:
    """
    Calls Qt's 'int QQmlJSMetaProperty::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#revision
    """
    #  int QQmlJSMetaProperty::revision() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty8revisionEv')

  def index(self) -> int:
    """
    Calls Qt's 'int QQmlJSMetaProperty::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#index
    """
    #  int QQmlJSMetaProperty::index() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty5indexEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaProperty::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#isValid
    """
    #  bool QQmlJSMetaProperty::isValid() const
    return self.uglySide.call('ritual_ZNK18QQmlJSMetaProperty7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPropertyName(self, propertyName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setPropertyName(const QString
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setPropertyName

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setPropertyName(const QString &propertyName)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty15setPropertyNameERK7QString',
        propertyName,
    )

  @overload(str)
  def setTypeName(self, typeName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setTypeName(const QString
    &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setTypeName

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setTypeName(const QString &typeName)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty11setTypeNameERK7QString', typeName,
    )

  @overload(str)
  def setRead(self, read: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setRead(const QString &read)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setRead

    Parameters
    ----------

    read : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setRead(const QString &read)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty7setReadERK7QString', read,
    )

  @overload(str)
  def setWrite(self, write: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setWrite(const QString &write)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setWrite

    Parameters
    ----------

    write : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setWrite(const QString &write)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty8setWriteERK7QString', write,
    )

  @overload(str)
  def setReset(self, reset: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setReset(const QString &reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setReset

    Parameters
    ----------

    reset : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setReset(const QString &reset)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty8setResetERK7QString', reset,
    )

  @overload(str)
  def setBindable(self, bindable: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setBindable(const QString
    &bindable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setBindable

    Parameters
    ----------

    bindable : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setBindable(const QString &bindable)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty11setBindableERK7QString', bindable,
    )

  @overload(str)
  def setNotify(self, notify: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setNotify(const QString &notify)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setNotify

    Parameters
    ----------

    notify : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setNotify(const QString &notify)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty9setNotifyERK7QString', notify,
    )

  @overload(str)
  def setPrivateClass(self, privateClass: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setPrivateClass(const QString
    &privateClass)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setPrivateClass

    Parameters
    ----------

    privateClass : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setPrivateClass(const QString &privateClass)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty15setPrivateClassERK7QString',
        privateClass,
    )

  @overload(WAIT['QQmlJS.SourceLocation'])
  def setSourceLocation(
      self,
      newSourceLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setSourceLocation(const
    QQmlJS::SourceLocation &newSourceLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setSourceLocation

    Parameters
    ----------

    newSourceLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSMetaProperty::setSourceLocation(const
    #      QQmlJS::SourceLocation &newSourceLocation)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty17setSourceLocationERKN6QQmlJS14Sourc'
        'eLocationE',
        self._valueOf(newSourceLocation),
    )

  @overload(QList[QQmlJSAnnotation])
  def setAnnotations(self, annotation: QList[QQmlJSAnnotation]) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setAnnotations(const
    QList<QQmlJSAnnotation> &annotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setAnnotations

    Parameters
    ----------

    annotation : QList[QQmlJSAnnotation]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSMetaProperty::setAnnotations(const QList<QQmlJSAnnotation>
    #      &annotation)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty14setAnnotationsERK5QListI16QQmlJSAnn'
        'otationE',
        self._valueOf(annotation),
    )

  @overload(bool)
  def setIsList(self, isList: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsList(bool isList)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsList

    Parameters
    ----------

    isList : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsList(bool isList)
    self.uglySide.call('ritual_ZN18QQmlJSMetaProperty9setIsListEb', isList)

  @overload(bool)
  def setIsWritable(self, isWritable: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsWritable(bool isWritable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsWritable

    Parameters
    ----------

    isWritable : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsWritable(bool isWritable)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty13setIsWritableEb', isWritable,
    )

  @overload(bool)
  def setIsPointer(self, isPointer: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsPointer(bool isPointer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsPointer

    Parameters
    ----------

    isPointer : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsPointer(bool isPointer)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty12setIsPointerEb', isPointer,
    )

  @overload(bool)
  def setIsTypeConstant(self, isTypeConstant: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsTypeConstant(bool
    isTypeConstant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsTypeConstant

    Parameters
    ----------

    isTypeConstant : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsTypeConstant(bool isTypeConstant)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty17setIsTypeConstantEb', isTypeConstant,
    )

  @overload(str)
  def setAliasExpression(self, aliasString: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setAliasExpression(const QString
    &aliasString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setAliasExpression

    Parameters
    ----------

    aliasString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setAliasExpression(const QString
    #      &aliasString)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty18setAliasExpressionERK7QString',
        aliasString,
    )

  @overload(str)
  def setAliasTargetName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setAliasTargetName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setAliasTargetName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaProperty::setAliasTargetName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty18setAliasTargetNameERK7QString', name,
    )

  @overload(bool)
  def setIsFinal(self, isFinal: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsFinal(bool isFinal)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsFinal

    Parameters
    ----------

    isFinal : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsFinal(bool isFinal)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty10setIsFinalEb', isFinal,
    )

  @overload(bool)
  def setIsOverride(self, isOverride: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsOverride(bool isOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsOverride

    Parameters
    ----------

    isOverride : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsOverride(bool isOverride)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty13setIsOverrideEb', isOverride,
    )

  @overload(bool)
  def setIsVirtual(self, isVirtual: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsVirtual(bool isVirtual)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsVirtual

    Parameters
    ----------

    isVirtual : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsVirtual(bool isVirtual)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty12setIsVirtualEb', isVirtual,
    )

  @overload(bool)
  def setIsPropertyConstant(self, isPropertyConstant: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIsPropertyConstant(bool
    isPropertyConstant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIsPropertyConstant

    Parameters
    ----------

    isPropertyConstant : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIsPropertyConstant(bool
    #      isPropertyConstant)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty21setIsPropertyConstantEb',
        isPropertyConstant,
    )

  @overload(int)
  def setRevision(self, revision: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setRevision(int revision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setRevision

    Parameters
    ----------

    revision : int
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setRevision(int revision)
    self.uglySide.call(
        'ritual_ZN18QQmlJSMetaProperty11setRevisionEi', revision,
    )

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaProperty::setIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSMetaProperty::setIndex(int index)
    self.uglySide.call('ritual_ZN18QQmlJSMetaProperty8setIndexEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlJSMetaProperty) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlJSMetaProperty &a, const
    QQmlJSMetaProperty &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#operator==

    Parameters
    ----------

    b : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.
    """
    #  bool operator==(const QQmlJSMetaProperty &a, const QQmlJSMetaProperty
    #      &b)
    return Rituals.call(
        'ritual_ZeqRK18QQmlJSMetaPropertyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QQmlJSMetaProperty) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlJSMetaProperty &a, const
    QQmlJSMetaProperty &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaproperty.html#operator!=

    Parameters
    ----------

    b : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.
    """
    #  bool operator!=(const QQmlJSMetaProperty &a, const QQmlJSMetaProperty
    #      &b)
    return Rituals.call(
        'ritual_ZneRK18QQmlJSMetaPropertyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    Notes what was given, for Qt's
    'QQmlJSMetaProperty::QQmlJSMetaProperty()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaproperty.html#QQmlJSMetaProperty
    """
    #  QQmlJSMetaProperty::QQmlJSMetaProperty()
    self._noteCreation(QQmlJSMetaProperty, lambda: Rituals.call(
        'ritual_ZN18QQmlJSMetaPropertyC1Ev',
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

  @staticmethod
  def aliasTargetScope(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaProperty::aliasTargetScope() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaProperty.aliasTargetScope' has no cute function yet. "
        "Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaProperty::aliasTargetScope() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setAliasTargetScope(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaProperty::setAliasTargetScope(const
    QSharedPointer<const QQmlJSScope> &scope)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaProperty.setAliasTargetScope' has no cute function yet. "
        "Qt's 'void QQmlJSMetaProperty::setAliasTargetScope(const "
        "QSharedPointer<const QQmlJSScope> &scope)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaProperty::setType(const QDeferredSharedPointer<const
    QQmlJSScope> &type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaProperty.setType' has no cute function yet. Qt's 'void "
        "QQmlJSMetaProperty::setType(const QDeferredSharedPointer<const "
        "QQmlJSScope> &type)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def type(*__, **_) -> Never:
    """
    Qt's 'QDeferredSharedPointer<const QQmlJSScope>
    QQmlJSMetaProperty::type() const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaProperty.type' has no cute function yet. Qt's "
        "'QDeferredSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaProperty::type() const': gives a type Python has no way "
        "to take yet.")


#  Qt's 'QHash<QString, QQmlJSMetaProperty>': the QHash from text to
#  QQmlJSMetaProperty, which 'QHash[str, QQmlJSMetaProperty]' gives. It is
#  completed here, in the file of the class of its values.
QHash.createKind(
    str, QQmlJSMetaProperty, 'value',
    make='ritual_map_make_QHash_QString_QQmlJSMetaProperty',
    put='ritual_map_put_QHash_QString_QQmlJSMetaProperty',
    size='ritual_map_size_QHash_QString_QQmlJSMetaProperty',
    key='ritual_map_key_QHash_QString_QQmlJSMetaProperty',
    value='ritual_map_value_QHash_QString_QQmlJSMetaProperty',
    has='ritual_map_has_QHash_QString_QQmlJSMetaProperty',
    get='ritual_map_get_QHash_QString_QQmlJSMetaProperty',
    drop='ritual_map_drop_QHash_QString_QQmlJSMetaProperty',
)
