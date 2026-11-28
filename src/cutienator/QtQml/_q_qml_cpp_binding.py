"""
QQmlCppBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcppbinding_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlCppBinding to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QUntypedPropertyBinding
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCppBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlCppBinding: a plain Python object standing in
  front of one C++ QQmlCppBinding.

  C++ hands a QQmlCppBinding around as a copy, so every C++ QQmlCppBinding
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlCppBinding that has a ritual and that Python can
  call so far, 2 names in all: 'createBindingForBindable',
  'createBindingForNonBindable'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedPropertyBinding
    QQmlCppBinding::createTranslationBindingForBindable(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, QObject
    *bindingTarget, int metaPropertyIndex, const QQmlTranslation
    &translationData, const QString &propertyName)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlCppBinding::createTranslationBindingForNonBindable(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlSourceLocation &location, const QQmlTranslation &translationData,
    QObject *thisObject, QObject *bindingTarget, int metaPropertyIndex, const
    QString &propertyName, int valueTypePropertyIndex)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQmlCppBinding::~QQmlCppBinding()': the destructor: Python removes
    its C++ QQmlCppBinding by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlCppBinding is created at the first use, not by
    'QQmlCppBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlCppBinding back gives a copy the ritual made for
    Python, in a new cute QQmlCppBinding.
  - Each name of Qt's QQmlCppBinding that has no cute function yet,
    'createTranslationBindingForBindable',
    'createTranslationBindingForNonBindable', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], QObject, int, QObject, int, int,
      str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], QObject, int, NoneType, int,
      int, str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], NoneType, int, QObject, int,
      int, str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], NoneType, int, NoneType, int,
      int, str,
  )
  @overload(NoneType, QObject, int, QObject, int, int, str)
  @overload(NoneType, QObject, int, NoneType, int, int, str)
  @overload(NoneType, NoneType, int, QObject, int, int, str)
  @overload(NoneType, NoneType, int, NoneType, int, int, str)
  def createBindingForBindable(
      unit: Optional[QV4.ExecutableCompilationUnit],
      thisObject: Optional[QObject],
      functionIndex: int,
      bindingTarget: Optional[QObject],
      metaPropertyIndex: int,
      valueTypePropertyIndex: int,
      propertyName: str,
  ) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding
    QQmlCppBinding::createBindingForBindable(const
    QV4::ExecutableCompilationUnit *unit, QObject *thisObject, qsizetype
    functionIndex, QObject *bindingTarget, int metaPropertyIndex, int
    valueTypePropertyIndex, const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcppbinding.html#createBindingForBindable

    Parameters
    ----------

    unit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    functionIndex : int
      Passed on as it is.

    bindingTarget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaPropertyIndex : int
      Passed on as it is.

    valueTypePropertyIndex : int
      Passed on as it is.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding QQmlCppBinding::createBindingForBindable(const
    #      QV4::ExecutableCompilationUnit *unit, QObject *thisObject,
    #      qsizetype functionIndex, QObject *bindingTarget, int
    #      metaPropertyIndex, int valueTypePropertyIndex, const QString
    #      &propertyName)
    address = Rituals.call(
        'ritual_ZN14QQmlCppBinding24createBindingForBindableEPKN3QV425Execu'
        'tableCompilationUnitEP7QObjectxS5_iiRK7QString',
        CuteMixin._addressOf(unit), CuteMixin._addressOf(thisObject,
        'QObject'), functionIndex, CuteMixin._addressOf(bindingTarget,
        'QObject'), metaPropertyIndex, valueTypePropertyIndex, propertyName,
    )
    from ..QtCore import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  @staticmethod
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], QObject, int, QObject, int, int,
      str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], QObject, int, NoneType, int,
      int, str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], NoneType, int, QObject, int,
      int, str,
  )
  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], NoneType, int, NoneType, int,
      int, str,
  )
  @overload(NoneType, QObject, int, QObject, int, int, str)
  @overload(NoneType, QObject, int, NoneType, int, int, str)
  @overload(NoneType, NoneType, int, QObject, int, int, str)
  @overload(NoneType, NoneType, int, NoneType, int, int, str)
  def createBindingForNonBindable(
      unit: Optional[QV4.ExecutableCompilationUnit],
      thisObject: Optional[QObject],
      functionIndex: int,
      bindingTarget: Optional[QObject],
      metaPropertyIndex: int,
      valueTypePropertyIndex: int,
      propertyName: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlCppBinding::createBindingForNonBindable(const
    QV4::ExecutableCompilationUnit *unit, QObject *thisObject, qsizetype
    functionIndex, QObject *bindingTarget, int metaPropertyIndex, int
    valueTypePropertyIndex, const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcppbinding.html#createBindingForNonBindable

    Parameters
    ----------

    unit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    functionIndex : int
      Passed on as it is.

    bindingTarget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaPropertyIndex : int
      Passed on as it is.

    valueTypePropertyIndex : int
      Passed on as it is.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlCppBinding::createBindingForNonBindable(const
    #      QV4::ExecutableCompilationUnit *unit, QObject *thisObject,
    #      qsizetype functionIndex, QObject *bindingTarget, int
    #      metaPropertyIndex, int valueTypePropertyIndex, const QString
    #      &propertyName)
    Rituals.call(
        'ritual_ZN14QQmlCppBinding27createBindingForNonBindableEPKN3QV425Ex'
        'ecutableCompilationUnitEP7QObjectxS5_iiRK7QString',
        CuteMixin._addressOf(unit), CuteMixin._addressOf(thisObject,
        'QObject'), functionIndex, CuteMixin._addressOf(bindingTarget,
        'QObject'), metaPropertyIndex, valueTypePropertyIndex, propertyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCppBinding'

  #  Qt's '~QQmlCppBinding()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlCppBinding behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QQmlCppBindingD1Ev'

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
  def createTranslationBindingForBindable(*__, **_) -> Never:
    """
    Qt's 'QUntypedPropertyBinding
    QQmlCppBinding::createTranslationBindingForBindable(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, QObject
    *bindingTarget, int metaPropertyIndex, const QQmlTranslation
    &translationData, const QString &propertyName)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlCppBinding.createTranslationBindingForBindable' has no cute "
        "function yet. Qt's 'QUntypedPropertyBinding "
        "QQmlCppBinding::createTranslationBindingForBindable(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, QObject "
        "*bindingTarget, int metaPropertyIndex, const QQmlTranslation "
        "&translationData, const QString &propertyName)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def createTranslationBindingForNonBindable(*__, **_) -> Never:
    """
    Qt's 'void QQmlCppBinding::createTranslationBindingForNonBindable(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlSourceLocation &location, const QQmlTranslation &translationData,
    QObject *thisObject, QObject *bindingTarget, int metaPropertyIndex, const
    QString &propertyName, int valueTypePropertyIndex)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlCppBinding.createTranslationBindingForNonBindable' has no "
        "cute function yet. Qt's 'void "
        "QQmlCppBinding::createTranslationBindingForNonBindable(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const "
        "QQmlSourceLocation &location, const QQmlTranslation "
        "&translationData, QObject *thisObject, QObject *bindingTarget, int "
        "metaPropertyIndex, const QString &propertyName, int "
        "valueTypePropertyIndex)': takes a type Python has no way to hand "
        "over yet.")
