"""
QQmlJSMetaParameter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSMetaParameter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlJSMetaParameter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSMetaParameter: a plain Python object standing
  in front of one C++ QQmlJSMetaParameter.

  C++ hands a QQmlJSMetaParameter around as a copy, so every C++
  QQmlJSMetaParameter behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSMetaParameter that has a ritual and that
  Python can call so far, 12 names in all: 'name', 'setName', 'typeName',
  'setTypeName', 'typeQualifier', 'setTypeQualifier', 'isPointer',
  'setIsPointer', 'isList', 'setIsList', '__eq__', '__ne__'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSMetaParameter::QQmlJSMetaParameter(QString name, QString
    typeName, Constness typeQualifier, QWeakPointer<const QQmlJSScope>
    type)': takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaParameter::type()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlJSMetaParameter::setType(QWeakPointer<const QQmlJSScope>
    type)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSMetaParameter::~QQmlJSMetaParameter()': the destructor:
    Python removes its C++ QQmlJSMetaParameter by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlJSMetaParameter is created at the first use, not by
    'QQmlJSMetaParameter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSMetaParameter back gives a copy the ritual made
    for Python, in a new cute QQmlJSMetaParameter.
  - Each name of Qt's QQmlJSMetaParameter that has no cute function yet,
    '__init__', 'setType', 'type', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSMetaParameter, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Constness(CuteNum):
    """
    The enum 'QQmlJSMetaParameter::Constness' of Qt, with the 2 names Qt
    gives in it.
    """

    NonConst = Kee[int](0)
    Const = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSMetaParameter'

  #  Qt's '~QQmlJSMetaParameter()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJSMetaParameter behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlJSMetaParameterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaParameter::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaParameter::name() const
    return self.uglySide.call('ritual_ZNK19QQmlJSMetaParameter4nameEv')

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaParameter::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaParameter::typeName() const
    return self.uglySide.call('ritual_ZNK19QQmlJSMetaParameter8typeNameEv')

  def typeQualifier(self) -> Constness:
    """
    Calls Qt's 'Constness QQmlJSMetaParameter::typeQualifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#typeQualifier

    Returns
    -------

    Constness
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Constness(number)' gives.
    """
    #  Constness QQmlJSMetaParameter::typeQualifier() const
    return QQmlJSMetaParameter.Constness(self.uglySide.call(
        'ritual_ZNK19QQmlJSMetaParameter13typeQualifierEv',
    ))

  def isPointer(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaParameter::isPointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#isPointer
    """
    #  bool QQmlJSMetaParameter::isPointer() const
    return self.uglySide.call('ritual_ZNK19QQmlJSMetaParameter9isPointerEv')

  def isList(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaParameter::isList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#isList
    """
    #  bool QQmlJSMetaParameter::isList() const
    return self.uglySide.call('ritual_ZNK19QQmlJSMetaParameter6isListEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaParameter::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaParameter::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QQmlJSMetaParameter7setNameERK7QString', name,
    )

  @overload(str)
  def setTypeName(self, typeName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaParameter::setTypeName(const QString
    &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#setTypeName

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaParameter::setTypeName(const QString &typeName)
    self.uglySide.call(
        'ritual_ZN19QQmlJSMetaParameter11setTypeNameERK7QString', typeName,
    )

  @overload(Constness)
  def setTypeQualifier(self, typeQualifier: Constness) -> None:
    """
    Calls Qt's 'void QQmlJSMetaParameter::setTypeQualifier(Constness
    typeQualifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#setTypeQualifier

    Parameters
    ----------

    typeQualifier : Constness
      Passed on as its number.
    """
    #  void QQmlJSMetaParameter::setTypeQualifier(Constness typeQualifier)
    self.uglySide.call(
        'ritual_ZN19QQmlJSMetaParameter16setTypeQualifierENS_9ConstnessE',
        typeQualifier.value,
    )

  @overload(bool)
  def setIsPointer(self, isPointer: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaParameter::setIsPointer(bool isPointer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#setIsPointer

    Parameters
    ----------

    isPointer : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaParameter::setIsPointer(bool isPointer)
    self.uglySide.call(
        'ritual_ZN19QQmlJSMetaParameter12setIsPointerEb', isPointer,
    )

  @overload(bool)
  def setIsList(self, isList: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaParameter::setIsList(bool isList)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaparameter.html#setIsList

    Parameters
    ----------

    isList : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaParameter::setIsList(bool isList)
    self.uglySide.call('ritual_ZN19QQmlJSMetaParameter9setIsListEb', isList)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlJSMetaParameter) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlJSMetaParameter &a, const
    QQmlJSMetaParameter &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#operator==

    Parameters
    ----------

    b : QQmlJSMetaParameter
      Passed on as a value: Qt reads the C++ QQmlJSMetaParameter, which stays
      Python's own.
    """
    #  bool operator==(const QQmlJSMetaParameter &a, const
    #      QQmlJSMetaParameter &b)
    return Rituals.call(
        'ritual_ZeqRK19QQmlJSMetaParameterS1_',
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
  def __ne__(self, b: QQmlJSMetaParameter) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlJSMetaParameter &a, const
    QQmlJSMetaParameter &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetaparameter.html#operator!=

    Parameters
    ----------

    b : QQmlJSMetaParameter
      Passed on as a value: Qt reads the C++ QQmlJSMetaParameter, which stays
      Python's own.
    """
    #  bool operator!=(const QQmlJSMetaParameter &a, const
    #      QQmlJSMetaParameter &b)
    return Rituals.call(
        'ritual_ZneRK19QQmlJSMetaParameterS1_',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlJSMetaParameter::QQmlJSMetaParameter(QString name, QString
    typeName, Constness typeQualifier, QWeakPointer<const QQmlJSScope>
    type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaParameter.__init__' has no cute function yet. Qt's "
        "'QQmlJSMetaParameter::QQmlJSMetaParameter(QString name, QString "
        "typeName, Constness typeQualifier, QWeakPointer<const QQmlJSScope> "
        "type)': takes a type Python has no way to hand over yet.")

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
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaParameter::setType(QWeakPointer<const QQmlJSScope>
    type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaParameter.setType' has no cute function yet. Qt's 'void "
        "QQmlJSMetaParameter::setType(QWeakPointer<const QQmlJSScope> "
        "type)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def type(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaParameter::type()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaParameter.type' has no cute function yet. Qt's "
        "'QSharedPointer<const QQmlJSScope> QQmlJSMetaParameter::type() "
        "const': gives a type Python has no way to take yet.")


#  Qt's 'QList<QQmlJSMetaParameter>': the list of QQmlJSMetaParameter, which
#  'QList[QQmlJSMetaParameter]' gives. It is made here, so that there is one
#  as soon as there can be a QQmlJSMetaParameter.
QList.createKind(
    QQmlJSMetaParameter, 'value',
    make='ritual_list_make_QQmlJSMetaParameter',
    add='ritual_list_add_QQmlJSMetaParameter',
    size='ritual_list_size_QQmlJSMetaParameter',
    at='ritual_list_at_QQmlJSMetaParameter',
    drop='ritual_list_drop_QQmlJSMetaParameter',
)
