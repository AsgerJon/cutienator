"""
QQmlPropertyValidator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertyvalidator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyValidator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlPropertyCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QUrl
  from . import QQmlError, QQmlPropertyData, QQmlTypeLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QQmlError = WAIT['QQmlError']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyValidator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyValidator: a plain Python object standing
  in front of one C++ QQmlPropertyValidator.

  C++ hands a QQmlPropertyValidator around as a copy, so every C++
  QQmlPropertyValidator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyValidator that has a ritual and that
  Python can call so far, 9 names in all: 'tr', 'rootPropertyCache',
  'documentSourceUrl', 'typeLoader', 'validateObjectBinding', 'canCoerce',
  'recordError', 'stringAt', 'resolvedType'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyValidator::QQmlPropertyValidator(QQmlTypeLoader
    *typeLoader, const QQmlImports *imports, const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlPropertyValidator::~QQmlPropertyValidator()': the destructor:
    Python removes its C++ QQmlPropertyValidator by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlValueTypeProvider; 1 leans on 'QQmlPropertyValidator.

  What to expect
  --------------

  - The C++ QQmlPropertyValidator is created at the first use, not by
    'QQmlPropertyValidator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyValidator back gives a copy the ritual
    made for Python, in a new cute QQmlPropertyValidator.
  - Each name of Qt's QQmlPropertyValidator that has no cute function yet,
    '__init__', 'validate', 'validateLiteralBinding', 'validateObject', holds
    a function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlPropertyValidator::tr(const char *sourceText,
    const char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#tr

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
    #  QString QQmlPropertyValidator::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN21QQmlPropertyValidator2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyValidator'

  #  Qt's '~QQmlPropertyValidator()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlPropertyValidator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlPropertyValidatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rootPropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlPropertyValidator::rootPropertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#rootPropertyCache

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlPropertyValidator::rootPropertyCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator17rootPropertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  def documentSourceUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlPropertyValidator::documentSourceUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#documentSourceUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlPropertyValidator::documentSourceUrl() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator17documentSourceUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def typeLoader(self) -> Optional[QQmlTypeLoader]:
    """
    Calls Qt's 'QQmlTypeLoader *QQmlPropertyValidator::typeLoader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#typeLoader

    Returns
    -------

    Optional[QQmlTypeLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoader *QQmlPropertyValidator::typeLoader() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator10typeLoaderEv',
    )
    from . import QQmlTypeLoader
    return QQmlTypeLoader._cuteAt(address)

  @overload(QQmlPropertyData, str, WAIT['QV4.CompiledData.Binding'])
  @overload(QQmlPropertyData, str, NoneType)
  @overload(NoneType, str, WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType, str, NoneType)
  def validateObjectBinding(
      self,
      property: Optional[QQmlPropertyData],
      propertyName: str,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> QQmlError:
    """
    Calls Qt's 'QQmlError QQmlPropertyValidator::validateObjectBinding(const
    QQmlPropertyData *property, const QString &propertyName, const
    QV4::CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#validateObjectBinding

    Parameters
    ----------

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlPropertyValidator::validateObjectBinding(const
    #      QQmlPropertyData *property, const QString &propertyName, const
    #      QV4::CompiledData::Binding *binding) const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator21validateObjectBindingEPK16QQmlP'
        'ropertyDataRK7QStringPKN3QV412CompiledData7BindingE',
        self._addressOf(property), propertyName, self._addressOf(binding),
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  @overload(QMetaType, QQmlPropertyCache.ConstPtr)
  def canCoerce(
      self,
      to: QMetaType,
      fromMo: QQmlPropertyCache.ConstPtr,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyValidator::canCoerce(QMetaType to,
    QQmlPropertyCache::ConstPtr fromMo) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#canCoerce

    Parameters
    ----------

    to : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    fromMo : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  bool QQmlPropertyValidator::canCoerce(QMetaType to,
    #      QQmlPropertyCache::ConstPtr fromMo) const
    return self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator9canCoerceE9QMetaTypeN17QQmlPrope'
        'rtyCache8ConstPtrE',
        self._valueOf(to), self._valueOf(fromMo),
    )

  @overload(WAIT['QV4.CompiledData.Location'], str)
  def recordError(
      self,
      location: QV4.CompiledData.Location,
      description: str,
  ) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlPropertyValidator::recordError(const
    QV4::CompiledData::Location &location, const QString &description)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#recordError

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlPropertyValidator::recordError(const
    #      QV4::CompiledData::Location &location, const QString &description)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator11recordErrorERKN3QV412CompiledDa'
        'ta8LocationERK7QString',
        self._valueOf(location), description,
    )
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  @overload(QQmlError)
  def recordError(self, error: QQmlError) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlPropertyValidator::recordError(const
    QQmlError &error) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#recordError

    Parameters
    ----------

    error : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlPropertyValidator::recordError(const QQmlError
    #      &error) const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator11recordErrorERK9QQmlError',
        self._valueOf(error),
    )
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QQmlPropertyValidator::stringAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyValidator::stringAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator8stringAtEi', index,
    )

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'QV4::ResolvedTypeReference
    *QQmlPropertyValidator::resolvedType(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalidator.html#resolvedType

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.ResolvedTypeReference]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ResolvedTypeReference *QQmlPropertyValidator::resolvedType(int
    #      id) const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlPropertyValidator12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

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
    Qt's 'QQmlPropertyValidator::QQmlPropertyValidator(QQmlTypeLoader
    *typeLoader, const QQmlImports *imports, const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyValidator.__init__' has no cute function yet. Qt's "
        "'QQmlPropertyValidator::QQmlPropertyValidator(QQmlTypeLoader "
        "*typeLoader, const QQmlImports *imports, const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet.")

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
  def validate(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlError> QQmlPropertyValidator::validate()': leans on
    'QQmlPropertyValidator::validateObject(int, QV4::CompiledData::Binding
    const*, bool, QQmlPropertyResolver::RevisionCheck) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlPropertyValidator.validate' has no cute function yet. Qt's "
        "'QList<QQmlError> QQmlPropertyValidator::validate()': leans on "
        "'QQmlPropertyValidator::validateObject(int, "
        "QV4::CompiledData::Binding const*, bool, "
        "QQmlPropertyResolver::RevisionCheck) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def validateLiteralBinding(*__, **_) -> Never:
    """
    Qt's 'QQmlError QQmlPropertyValidator::validateLiteralBinding(const
    QQmlPropertyCache::ConstPtr &propertyCache, const QQmlPropertyData
    *property, const QV4::CompiledData::Binding *binding) const': leans on
    'QQmlValueTypeProvider::createValueType(QString const&, QMetaType)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlPropertyValidator.validateLiteralBinding' has no cute "
        "function yet. Qt's 'QQmlError "
        "QQmlPropertyValidator::validateLiteralBinding(const "
        "QQmlPropertyCache::ConstPtr &propertyCache, const QQmlPropertyData "
        "*property, const QV4::CompiledData::Binding *binding) const': "
        "leans on 'QQmlValueTypeProvider::createValueType(QString const&, "
        "QMetaType)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def validateObject(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlError> QQmlPropertyValidator::validateObject(int
    objectIndex, const QV4::CompiledData::Binding *instantiatingBinding, bool
    populatingValueTypeGroupProperty, QQmlPropertyResolver::RevisionCheck
    checkRevision) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'GroupPropertyVector'.
    """
    raise NotImplementedError(
        "'QQmlPropertyValidator.validateObject' has no cute function yet. "
        "Qt's 'QList<QQmlError> QQmlPropertyValidator::validateObject(int "
        "objectIndex, const QV4::CompiledData::Binding "
        "*instantiatingBinding, bool populatingValueTypeGroupProperty, "
        "QQmlPropertyResolver::RevisionCheck checkRevision) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'GroupPropertyVector'.")
