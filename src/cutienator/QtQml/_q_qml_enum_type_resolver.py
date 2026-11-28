"""
QQmlEnumTypeResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlEnumTypeResolver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQmlCompilePass, QQmlPropertyCache, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlPropertyData, QQmlTypeCompiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlPropertyData = WAIT['QQmlPropertyData']
  QQmlTypeCompiler = WAIT['QQmlTypeCompiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEnumTypeResolver(QQmlCompilePass):
  """
  The cute side of Qt's QQmlEnumTypeResolver: a plain Python object standing
  in front of one C++ QQmlEnumTypeResolver.

  It is built on the cute 'QQmlCompilePass', as Qt's QQmlEnumTypeResolver is
  built on Qt's QQmlCompilePass, and has everything that class has.

  C++ hands a QQmlEnumTypeResolver around as a copy, so every C++
  QQmlEnumTypeResolver behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlEnumTypeResolver that has a ritual and that
  Python can call so far, 4 names in all: 'tr', 'resolveEnumBindings',
  'assignEnumToBinding', 'tryQualifiedEnumAssignment'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding
    *binding, const QString &enumName, int enumValue)': takes in Python what
    'bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding *binding,
    QStringView enumName, int enumValue)' takes.
  - Qt's 'int QQmlEnumTypeResolver::evaluateEnum(const QString &scope,
    QStringView enumName, QStringView enumValue, bool *ok) const': takes a
    number to change where it is.
  - Qt's 'QQmlEnumTypeResolver::~QQmlEnumTypeResolver()': the destructor:
    Python removes its C++ QQmlEnumTypeResolver by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlEnumTypeResolver is created at the first use, not by
    'QQmlEnumTypeResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlEnumTypeResolver back gives a copy the ritual
    made for Python, in a new cute QQmlEnumTypeResolver.
  - Each name of Qt's QQmlEnumTypeResolver that has no cute function yet,
    'evaluateEnum', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlEnumTypeResolver::tr(const char *sourceText,
    const char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlenumtyperesolver.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlEnumTypeResolver::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN20QQmlEnumTypeResolver2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEnumTypeResolver'

  #  Qt's '~QQmlEnumTypeResolver()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlEnumTypeResolver behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlEnumTypeResolverD1Ev'

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

  @overload(QQmlTypeCompiler)
  @overload(NoneType)
  def __init__(self, typeCompiler: Optional[QQmlTypeCompiler]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlEnumTypeResolver::QQmlEnumTypeResolver(QQmlTypeCompiler
    *typeCompiler)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenumtyperesolver.html#QQmlEnumTypeResolver

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlEnumTypeResolver::QQmlEnumTypeResolver(QQmlTypeCompiler
    #      *typeCompiler)
    self._noteCreation(QQmlEnumTypeResolver, lambda: Rituals.call(
        'ritual_ZN20QQmlEnumTypeResolverC1EP16QQmlTypeCompiler',
        self._addressOf(typeCompiler),
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

  def resolveEnumBindings(self) -> bool:
    """
    Calls Qt's 'bool QQmlEnumTypeResolver::resolveEnumBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenumtyperesolver.html#resolveEnumBindings
    """
    #  bool QQmlEnumTypeResolver::resolveEnumBindings()
    return self.uglySide.call(
        'ritual_ZN20QQmlEnumTypeResolver19resolveEnumBindingsEv',
    )

  @overload(WAIT['QmlIR.Binding'], str, int)
  @overload(NoneType, str, int)
  def assignEnumToBinding(
      self,
      binding: Optional[QmlIR.Binding],
      enumName: str,
      enumValue: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding
    *binding, QStringView enumName, int enumValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenumtyperesolver.html#assignEnumToBinding

    Parameters
    ----------

    binding : Optional[QmlIR.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enumName : str
      Passed on as it is: a QString is made of it for the call.

    enumValue : int
      Passed on as it is.
    """
    #  bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding
    #      *binding, QStringView enumName, int enumValue)
    return self.uglySide.call(
        'ritual_ZN20QQmlEnumTypeResolver19assignEnumToBindingEPN5QmlIR7Bind'
        'ingE11QStringViewi',
        self._addressOf(binding), enumName, enumValue,
    )

  @overload(
      WAIT['QmlIR.Object'], QQmlPropertyCache.ConstPtr, QQmlPropertyData,
      WAIT['QmlIR.Binding'],
  )
  @overload(
      WAIT['QmlIR.Object'], QQmlPropertyCache.ConstPtr, QQmlPropertyData,
      NoneType,
  )
  @overload(
      WAIT['QmlIR.Object'], QQmlPropertyCache.ConstPtr, NoneType,
      WAIT['QmlIR.Binding'],
  )
  @overload(
      WAIT['QmlIR.Object'], QQmlPropertyCache.ConstPtr, NoneType, NoneType,
  )
  @overload(
      NoneType, QQmlPropertyCache.ConstPtr, QQmlPropertyData,
      WAIT['QmlIR.Binding'],
  )
  @overload(NoneType, QQmlPropertyCache.ConstPtr, QQmlPropertyData, NoneType)
  @overload(
      NoneType, QQmlPropertyCache.ConstPtr, NoneType, WAIT['QmlIR.Binding'],
  )
  @overload(NoneType, QQmlPropertyCache.ConstPtr, NoneType, NoneType)
  def tryQualifiedEnumAssignment(
      self,
      obj: Optional[QmlIR.Object],
      propertyCache: QQmlPropertyCache.ConstPtr,
      prop: Optional[QQmlPropertyData],
      binding: Optional[QmlIR.Binding],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlEnumTypeResolver::tryQualifiedEnumAssignment(const
    QmlIR::Object *obj, const QQmlPropertyCache::ConstPtr &propertyCache,
    const QQmlPropertyData *prop, QmlIR::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlenumtyperesolver.html

    Parameters
    ----------

    obj : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyCache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.

    prop : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QmlIR.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlEnumTypeResolver::tryQualifiedEnumAssignment(const
    #      QmlIR::Object *obj, const QQmlPropertyCache::ConstPtr
    #      &propertyCache, const QQmlPropertyData *prop, QmlIR::Binding
    #      *binding)
    return self.uglySide.call(
        'ritual_ZN20QQmlEnumTypeResolver26tryQualifiedEnumAssignmentEPKN5Qm'
        'lIR6ObjectERKN17QQmlPropertyCache8ConstPtrEPK16QQmlPropertyDataPNS'
        '0_7BindingE',
        self._addressOf(obj), self._valueOf(propertyCache),
        self._addressOf(prop), self._addressOf(binding),
    )

  @staticmethod
  def evaluateEnum(*__, **_) -> Never:
    """
    Qt's 'int QQmlEnumTypeResolver::evaluateEnum(const QString &scope,
    QStringView enumName, QStringView enumValue, bool *ok) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlEnumTypeResolver.evaluateEnum' has no cute function yet. Qt's "
        "'int QQmlEnumTypeResolver::evaluateEnum(const QString &scope, "
        "QStringView enumName, QStringView enumValue, bool *ok) const': "
        "takes a number to change where it is.")
