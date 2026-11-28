"""
QQmlListModelParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlListModelParser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtQml import QQmlCustomParser

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlListModelParser(QQmlCustomParser):
  """
  The cute side of Qt's QQmlListModelParser: a plain Python object standing
  in front of one C++ QQmlListModelParser.

  It is built on the cute 'QQmlCustomParser', as Qt's QQmlListModelParser is
  built on Qt's QQmlCustomParser, and has everything that class has.

  C++ hands a QQmlListModelParser around as a copy, so every C++
  QQmlListModelParser behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlListModelParser that has a ritual and that
  Python can call so far, 1 name in all: 'definesEmptyList'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlListModelParser::verifyBindings(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QList<const QV4::CompiledData::Binding *> &bindings)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlListModelParser::applyBindings(QObject *obj, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QList<const QV4::CompiledData::Binding *> &bindings)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlListModelParser::~QQmlListModelParser()': the destructor:
    Python removes its C++ QQmlListModelParser by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 2 leans on 'ListLayout; 1 leans on
  'QQmlListElement.

  What to expect
  --------------

  - The C++ QQmlListModelParser is created at the first use, not by
    'QQmlListModelParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlListModelParser back gives a copy the ritual made
    for Python, in a new cute QQmlListModelParser.
  - Each name of Qt's QQmlListModelParser that has no cute function yet,
    '__init__', 'applyProperty', 'verifyProperty', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlListModelParser, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PropertyType(CuteNum):
    """
    The enum 'QQmlListModelParser::PropertyType' of Qt, with the 5 names Qt
    gives in it.
    """

    Invalid = Kee[int](0)
    Boolean = Kee[int](1)
    Number = Kee[int](2)
    String = Kee[int](3)
    Script = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def definesEmptyList(s: str) -> bool:
    """
    Calls Qt's 'bool QQmlListModelParser::definesEmptyList(QStringView s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistmodelparser.html#definesEmptyList

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlListModelParser::definesEmptyList(QStringView s)
    return Rituals.call(
        'ritual_ZN19QQmlListModelParser16definesEmptyListE11QStringView', s,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListModelParser'

  #  Qt's '~QQmlListModelParser()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlListModelParser behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlListModelParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QQmlListModelParser::QQmlListModelParser()': leans on
    'ListLayout::getRoleOrCreate(QString const&,
    ListLayout::Role::DataType)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListModelParser.__init__' has no cute function yet. Qt's "
        "'QQmlListModelParser::QQmlListModelParser()': leans on "
        "'ListLayout::getRoleOrCreate(QString const&, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
  def applyProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlListModelParser::applyProperty(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QV4::CompiledData::Binding *binding, ListModel *model, QQmlListModel
    *owner, int outterElementIndex)': leans on
    'ListLayout::getRoleOrCreate(QString const&,
    ListLayout::Role::DataType)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListModelParser.applyProperty' has no cute function yet. Qt's "
        "'bool QQmlListModelParser::applyProperty(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
        "const QV4::CompiledData::Binding *binding, ListModel *model, "
        "QQmlListModel *owner, int outterElementIndex)': leans on "
        "'ListLayout::getRoleOrCreate(QString const&, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def verifyProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlListModelParser::verifyProperty(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QV4::CompiledData::Binding *binding)': leans on
    'QQmlListElement::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListModelParser.verifyProperty' has no cute function yet. "
        "Qt's 'bool QQmlListModelParser::verifyProperty(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit, const QV4::CompiledData::Binding *binding)': "
        "leans on 'QQmlListElement::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
