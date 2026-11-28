"""
QQmlPropertyCacheCreatorBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyCacheCreatorBase to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import OverrideSemantics, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyCacheCreatorBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyCacheCreatorBase: a plain Python object
  standing in front of one C++ QQmlPropertyCacheCreatorBase.

  C++ hands a QQmlPropertyCacheCreatorBase around as a copy, so every C++
  QQmlPropertyCacheCreatorBase behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyCacheCreatorBase that has a ritual and
  that Python can call so far, 4 names in all: 'tr',
  'propertyTypeForMetaType', 'canCreateClassNameTypeByUrl', 'explain'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<QMetaType>
    QQmlPropertyCacheCreatorBase::metaTypeForPropertyType(QV4::
    CompiledData::CommonType type)': gives a type Python has no way to take
    yet.
  - Qt's 'std::optional<QMetaType>
    QQmlPropertyCacheCreatorBase::listTypeForPropertyType(QV4::
    CompiledData::CommonType type)': gives a type Python has no way to take
    yet.
  - Qt's 'QQmlPropertyCacheCreatorBase::~QQmlPropertyCacheCreatorBase()': the
    destructor: Python removes its C++ QQmlPropertyCacheCreatorBase by it,
    and has no other use for it.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlPropertyCacheCreatorBase is created at the first use, not by
    'QQmlPropertyCacheCreatorBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyCacheCreatorBase back gives a copy the
    ritual made for Python, in a new cute QQmlPropertyCacheCreatorBase.
  - Each name of Qt's QQmlPropertyCacheCreatorBase that has no cute function
    yet, 'createClassNameForInlineComponent', 'createClassNameTypeByUrl',
    'listTypeForPropertyType', 'metaTypeForPropertyType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlPropertyCacheCreatorBase, each a class
  #  in here as in C++.

  class IncrementalResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlPropertyCacheCreatorBase::IncrementalResult: a
    plain Python object standing in front of one C++
    QQmlPropertyCacheCreatorBase::IncrementalResult.

    C++ hands a QQmlPropertyCacheCreatorBase::IncrementalResult around as a
    copy, so every C++ QQmlPropertyCacheCreatorBase::IncrementalResult behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlPropertyCacheCreatorBase::IncrementalResult yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlPropertyCacheCreatorBase::IncrementalResult::~IncrementalResult(
      )': the destructor: Python removes its C++
      QQmlPropertyCacheCreatorBase::IncrementalResult by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQmlPropertyCacheCreatorBase::IncrementalResult is created at
      the first use, not by
      'QQmlPropertyCacheCreatorBase::IncrementalResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlPropertyCacheCreatorBase::IncrementalResult
      back gives a copy the ritual made for Python, in a new cute
      QQmlPropertyCacheCreatorBase::IncrementalResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlPropertyCacheCreatorBase::IncrementalResult'

    #  Qt's '~QQmlPropertyCacheCreatorBase::IncrementalResult()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQmlPropertyCacheCreatorBase::IncrementalResult behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QQmlPropertyCacheCreatorBase17IncrementalResultD1Ev')

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
    Calls Qt's 'QString QQmlPropertyCacheCreatorBase::tr(const char
    *sourceText, const char *disambiguation, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachecreatorbase.html#tr

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
    #  QString QQmlPropertyCacheCreatorBase::tr(const char *sourceText, const
    #      char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN28QQmlPropertyCacheCreatorBase2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  @overload(QMetaType)
  def propertyTypeForMetaType(
      metaType: QMetaType,
  ) -> QV4.CompiledData.CommonType:
    """
    Calls Qt's 'QV4::CompiledData::CommonType
    QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(QMetaType
    metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachecreatorbase.html

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QV4.CompiledData.CommonType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QV4.CompiledData.CommonType(number)' gives.
    """
    #  QV4::CompiledData::CommonType
    #      QQmlPropertyCacheCreatorBase::propertyTypeForMetaType(QMetaType
    #      metaType)
    return QV4.CompiledData.CommonType(Rituals.call(
        'ritual_ZN28QQmlPropertyCacheCreatorBase23propertyTypeForMetaTypeE9'
        'QMetaType',
        CuteMixin._valueOf(metaType),
    ))

  @staticmethod
  @overload(QUrl)
  def canCreateClassNameTypeByUrl(url: QUrl) -> bool:
    """
    Calls Qt's 'bool
    QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachecreatorbase.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(const
    #      QUrl &url)
    return Rituals.call(
        'ritual_ZN28QQmlPropertyCacheCreatorBase27canCreateClassNameTypeByU'
        'rlERK4QUrl',
        CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(OverrideSemantics.Status)
  def explain(reason: OverrideSemantics.Status) -> str:
    """
    Calls Qt's 'QString
    QQmlPropertyCacheCreatorBase::explain(OverrideSemantics::Status reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachecreatorbase.html#explain

    Parameters
    ----------

    reason : OverrideSemantics.Status
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QQmlPropertyCacheCreatorBase::explain(OverrideSemantics::Status
    #      reason)
    return Rituals.call(
        'ritual_ZN28QQmlPropertyCacheCreatorBase7explainEN17OverrideSemanti'
        'cs6StatusE',
        reason.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyCacheCreatorBase'

  #  Qt's '~QQmlPropertyCacheCreatorBase()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlPropertyCacheCreatorBase behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QQmlPropertyCacheCreatorBaseD1Ev'

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
  def createClassNameForInlineComponent(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    QQmlPropertyCacheCreatorBase::createClassNameForInlineComponent(const
    QUrl &url)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'processUrlForClassName'.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheCreatorBase.createClassNameForInlineComponent' "
        "has no cute function yet. Qt's 'QByteArray "
        "QQmlPropertyCacheCreatorBase::createClassNameForInlineComponent(con"
        "st QUrl &url)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'processUrlForClassName'.")

  @staticmethod
  def createClassNameTypeByUrl(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    QQmlPropertyCacheCreatorBase::createClassNameTypeByUrl(const QUrl &url)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'processUrlForClassName'.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheCreatorBase.createClassNameTypeByUrl' has no "
        "cute function yet. Qt's 'QByteArray "
        "QQmlPropertyCacheCreatorBase::createClassNameTypeByUrl(const QUrl "
        "&url)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'processUrlForClassName'.")

  @staticmethod
  def listTypeForPropertyType(*__, **_) -> Never:
    """
    Qt's 'std::optional<QMetaType>
    QQmlPropertyCacheCreatorBase::listTypeForPropertyType(QV4::
    CompiledData::CommonType type)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheCreatorBase.listTypeForPropertyType' has no cute "
        "function yet. Qt's 'std::optional<QMetaType> "
        "QQmlPropertyCacheCreatorBase::listTypeForPropertyType(QV4::Compiled"
        "Data::CommonType type)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def metaTypeForPropertyType(*__, **_) -> Never:
    """
    Qt's 'std::optional<QMetaType>
    QQmlPropertyCacheCreatorBase::metaTypeForPropertyType(QV4::
    CompiledData::CommonType type)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheCreatorBase.metaTypeForPropertyType' has no cute "
        "function yet. Qt's 'std::optional<QMetaType> "
        "QQmlPropertyCacheCreatorBase::metaTypeForPropertyType(QV4::Compiled"
        "Data::CommonType type)': gives a type Python has no way to take "
        "yet.")
