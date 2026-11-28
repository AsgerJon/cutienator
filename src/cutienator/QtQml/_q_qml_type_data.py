"""
QQmlTypeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypedata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlTypeData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlDataBlob, QQmlNotifyingBlob, QQmlPrivate, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QQmlType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeData(QQmlNotifyingBlob):
  """
  The cute side of Qt's QQmlTypeData: a plain Python object standing in front
  of one C++ QQmlTypeData.

  It is built on the cute 'QQmlNotifyingBlob', as Qt's QQmlTypeData is built
  on Qt's QQmlNotifyingBlob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlTypeData that has a ritual and that Python can
  call so far, 15 names in all: 'tr', 'compilationUnit', 'qmlType',
  'typeClassName', 'backupSourceCode', 'done', 'dataReceived',
  'initializeFromCachedUnit', 'allDependenciesDone', 'stringAt',
  'checkScripts', 'checkDependencies', 'createError',
  'checkCompositeSingletons', 'createQQmlType'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeData::~QQmlTypeData()': the destructor: Python never
    removes a C++ QQmlTypeData.
  - Qt's 'void QQmlTypeData::scriptImported(const
    QQmlRefPointer<QQmlScriptBlob> &blob, const QV4::CompiledData::Location
    &location, const QString &nameSpace, const QString &qualifier)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  14 of the 32 functions Qt declares: 7 leans on 'lcQmlImport()', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 3 leans on 'QQmlThread; 1 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'invalidOverride()', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QQmlTypeData.

  What to expect
  --------------

  - The C++ QQmlTypeData is created at the first use, not by
    'QQmlTypeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeData.
  - Each name of Qt's QQmlTypeData that has no cute function yet, '__init__',
    'buildTypeResolutionCaches', 'compile', 'continueLoadFromIR',
    'createTypeAndPropertyCaches', 'loadFromDiskCache', 'loadFromSource',
    'loadImplicitImport', 'rebuildFromSource', 'resolveType', 'resolveTypes',
    'restoreIR', 'tryLoadFromDiskCache', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlTypeData, each a class in here as in
  #  C++.

  class ScriptReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypeData::ScriptReference: a plain Python
    object standing in front of one C++ QQmlTypeData::ScriptReference.

    C++ hands a QQmlTypeData::ScriptReference around as a copy, so every C++
    QQmlTypeData::ScriptReference behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlTypeData::ScriptReference yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypeData::ScriptReference::~ScriptReference()': the
      destructor: Python removes its C++ QQmlTypeData::ScriptReference by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlTypeData::ScriptReference is created at the first use, not
      by 'QQmlTypeData::ScriptReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypeData::ScriptReference back gives a copy the
      ritual made for Python, in a new cute QQmlTypeData::ScriptReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypeData::ScriptReference'

    #  Qt's '~QQmlTypeData::ScriptReference()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlTypeData::ScriptReference behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQmlTypeData15ScriptReferenceD1Ev'

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

  class TypeReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypeData::TypeReference: a plain Python object
    standing in front of one C++ QQmlTypeData::TypeReference.

    C++ hands a QQmlTypeData::TypeReference around as a copy, so every C++
    QQmlTypeData::TypeReference behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlTypeData::TypeReference that has a ritual and
    that Python can call so far, 1 name in all: 'qualifiedName'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypeData::TypeReference::~TypeReference()': the destructor:
      Python removes its C++ QQmlTypeData::TypeReference by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlTypeData::TypeReference is created at the first use, not by
      'QQmlTypeData::TypeReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypeData::TypeReference back gives a copy the
      ritual made for Python, in a new cute QQmlTypeData::TypeReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypeData::TypeReference'

    #  Qt's '~QQmlTypeData::TypeReference()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlTypeData::TypeReference behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQmlTypeData13TypeReferenceD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def qualifiedName(self) -> str:
      """
      Calls Qt's 'QString QQmlTypeData::TypeReference::qualifiedName()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypedata-typereference.html#qualifiedName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQmlTypeData::TypeReference::qualifiedName() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlTypeData13TypeReference13qualifiedNameEv',
      )

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
    Calls Qt's 'QString QQmlTypeData::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#tr

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
    #  QString QQmlTypeData::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN12QQmlTypeData2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeData'

  #  A C++ QQmlTypeData Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlTypeData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def compilationUnit(self) -> Optional[QV4.CompiledData.CompilationUnit]:
    """
    Calls Qt's 'QV4::CompiledData::CompilationUnit
    *QQmlTypeData::compilationUnit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#compilationUnit

    Returns
    -------

    Optional[QV4.CompiledData.CompilationUnit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QQmlTypeData15compilationUnitEv',
    )
    return QV4.CompiledData.CompilationUnit._cuteAt(address)

  @overload()
  @overload(str)
  def qmlType(self, inlineComponentName: str = '') -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlTypeData::qmlType(const QString
    &inlineComponentName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#qmlType

    Parameters
    ----------

    inlineComponentName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QQmlTypeData7qmlTypeERK7QString', inlineComponentName,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def typeClassName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlTypeData::typeClassName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#typeClassName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlTypeData::typeClassName() const
    address = self.uglySide.call('ritual_ZNK12QQmlTypeData13typeClassNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def backupSourceCode(self) -> QQmlDataBlob.SourceCodeData:
    """
    Calls Qt's 'SourceCodeData QQmlTypeData::backupSourceCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#backupSourceCode

    Returns
    -------

    QQmlDataBlob.SourceCodeData
      A new cute QQmlDataBlob::SourceCodeData around the copy Qt gave back.
      Python owns it.
    """
    #  SourceCodeData QQmlTypeData::backupSourceCode() const
    address = self.uglySide.call(
        'ritual_ZNK12QQmlTypeData16backupSourceCodeEv',
    )
    return QQmlDataBlob.SourceCodeData._cuteOwning(address)

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QQmlTypeData::stringAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeData::stringAt(int index) const
    ritual = 'ritual_ZNK12QQmlTypeData8stringAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQmlTypeData8stringAtEi'
    return self.uglySide.call(ritual, index)

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
    Qt's 'QQmlTypeData::QQmlTypeData(const QUrl &a0, QQmlTypeLoader *a1)':
    leans on 'QQmlTypeData::done()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.__init__' has no cute function yet. Qt's "
        "'QQmlTypeData::QQmlTypeData(const QUrl &a0, QQmlTypeLoader *a1)': "
        "leans on 'QQmlTypeData::done()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def done(self) -> None:
    """
    Calls Qt's 'void QQmlTypeData::done()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#done
    """
    #  void QQmlTypeData::done()
    self.uglySide.call('ritual_ZN12QQmlTypeData4doneEv')

  @overload(QQmlDataBlob.SourceCodeData)
  def dataReceived(self, a0: QQmlDataBlob.SourceCodeData) -> None:
    """
    Calls Qt's 'void QQmlTypeData::dataReceived(const SourceCodeData &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#dataReceived

    Parameters
    ----------

    a0 : QQmlDataBlob.SourceCodeData
      Passed on as a value: Qt reads the C++ QQmlDataBlob::SourceCodeData,
      which stays Python's own.
    """
    #  void QQmlTypeData::dataReceived(const SourceCodeData &a0)
    self.uglySide.call(
        'ritual_ZN12QQmlTypeData12dataReceivedERKN12QQmlDataBlob14SourceCod'
        'eDataE',
        self._valueOf(a0),
    )

  @overload(WAIT['QQmlPrivate.CachedQmlUnit'])
  @overload(NoneType)
  def initializeFromCachedUnit(
      self,
      unit: Optional[QQmlPrivate.CachedQmlUnit],
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeData::initializeFromCachedUnit(const
    QQmlPrivate::CachedQmlUnit *unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypedata.html#initializeFromCachedUnit

    Parameters
    ----------

    unit : Optional[QQmlPrivate.CachedQmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeData::initializeFromCachedUnit(const
    #      QQmlPrivate::CachedQmlUnit *unit)
    self.uglySide.call(
        'ritual_ZN12QQmlTypeData24initializeFromCachedUnitEPKN11QQmlPrivate'
        '13CachedQmlUnitE',
        self._addressOf(unit),
    )

  def allDependenciesDone(self) -> None:
    """
    Calls Qt's 'void QQmlTypeData::allDependenciesDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypedata.html#allDependenciesDone
    """
    #  void QQmlTypeData::allDependenciesDone()
    self.uglySide.call('ritual_ZN12QQmlTypeData19allDependenciesDoneEv')

  def checkScripts(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeData::checkScripts()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#checkScripts
    """
    #  bool QQmlTypeData::checkScripts()
    return self.uglySide.call('ritual_ZN12QQmlTypeData12checkScriptsEv')

  def checkDependencies(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeData::checkDependencies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypedata.html#checkDependencies
    """
    #  bool QQmlTypeData::checkDependencies()
    return self.uglySide.call('ritual_ZN12QQmlTypeData17checkDependenciesEv')

  @overload(TypeReference, str)
  def createError(self, type: TypeReference, message: str) -> None:
    """
    Calls Qt's 'void QQmlTypeData::createError(const TypeReference &type,
    const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#createError

    Parameters
    ----------

    type : TypeReference
      Passed on as a value: Qt reads the C++ QQmlTypeData::TypeReference,
      which stays Python's own.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypeData::createError(const TypeReference &type, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN12QQmlTypeData11createErrorERKNS_13TypeReferenceERK7QStri'
        'ng',
        self._valueOf(type), message,
    )

  @overload(ScriptReference, str)
  def createError(self, script: ScriptReference, message: str) -> None:
    """
    Calls Qt's 'void QQmlTypeData::createError(const ScriptReference &script,
    const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#createError

    Parameters
    ----------

    script : ScriptReference
      Passed on as a value: Qt reads the C++ QQmlTypeData::ScriptReference,
      which stays Python's own.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypeData::createError(const ScriptReference &script, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN12QQmlTypeData11createErrorERKNS_15ScriptReferenceERK7QSt'
        'ring',
        self._valueOf(script), message,
    )

  def checkCompositeSingletons(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeData::checkCompositeSingletons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypedata.html#checkCompositeSingletons
    """
    #  bool QQmlTypeData::checkCompositeSingletons()
    return self.uglySide.call(
        'ritual_ZN12QQmlTypeData24checkCompositeSingletonsEv',
    )

  def createQQmlType(self) -> None:
    """
    Calls Qt's 'void QQmlTypeData::createQQmlType()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypedata.html#createQQmlType
    """
    #  void QQmlTypeData::createQQmlType()
    self.uglySide.call('ritual_ZN12QQmlTypeData14createQQmlTypeEv')

  @staticmethod
  def buildTypeResolutionCaches(*__, **_) -> Never:
    """
    Qt's 'QQmlError
    QQmlTypeData::buildTypeResolutionCaches(QQmlRefPointer<QQmlTypeNameCache>
    *typeNameCache, QV4::CompiledData::ResolvedTypeReferenceMap
    *resolvedTypeCache) const': leans on 'QQmlThread::isThisThread() const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.buildTypeResolutionCaches' has no cute function yet. "
        "Qt's 'QQmlError "
        "QQmlTypeData::buildTypeResolutionCaches(QQmlRefPointer<QQmlTypeName"
        "Cache> *typeNameCache, QV4::CompiledData::ResolvedTypeReferenceMap "
        "*resolvedTypeCache) const': leans on 'QQmlThread::isThisThread() "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def compile(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeData::compile(const QQmlRefPointer<QQmlTypeNameCache>
    &typeNameCache, QV4::CompiledData::ResolvedTypeReferenceMap
    *resolvedTypeCache, const QV4::CompiledData::DependentTypesHasher
    &dependencyHasher)': leans on 'QQmlThread::isThisThread() const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.compile' has no cute function yet. Qt's 'void "
        "QQmlTypeData::compile(const QQmlRefPointer<QQmlTypeNameCache> "
        "&typeNameCache, QV4::CompiledData::ResolvedTypeReferenceMap "
        "*resolvedTypeCache, const QV4::CompiledData::DependentTypesHasher "
        "&dependencyHasher)': leans on 'QQmlThread::isThisThread() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def continueLoadFromIR(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeData::continueLoadFromIR()': leans on 'lcQmlImport()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.continueLoadFromIR' has no cute function yet. Qt's "
        "'void QQmlTypeData::continueLoadFromIR()': leans on "
        "'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def createTypeAndPropertyCaches(*__, **_) -> Never:
    """
    Qt's 'QQmlError QQmlTypeData::createTypeAndPropertyCaches(const
    QQmlRefPointer<QQmlTypeNameCache> &typeNameCache, const
    QV4::CompiledData::ResolvedTypeReferenceMap &resolvedTypeCache)': leans
    on 'invalidOverride()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.createTypeAndPropertyCaches' has no cute function "
        "yet. Qt's 'QQmlError "
        "QQmlTypeData::createTypeAndPropertyCaches(const "
        "QQmlRefPointer<QQmlTypeNameCache> &typeNameCache, const "
        "QV4::CompiledData::ResolvedTypeReferenceMap &resolvedTypeCache)': "
        "leans on 'invalidOverride()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadFromDiskCache(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::loadFromDiskCache(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.loadFromDiskCache' has no cute function yet. Qt's "
        "'bool QQmlTypeData::loadFromDiskCache(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': leans "
        "on 'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadFromSource(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::loadFromSource()': leans on
    'QQmlThread::isThisThread() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.loadFromSource' has no cute function yet. Qt's 'bool "
        "QQmlTypeData::loadFromSource()': leans on "
        "'QQmlThread::isThisThread() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def loadImplicitImport(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::loadImplicitImport()': leans on 'lcQmlImport()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.loadImplicitImport' has no cute function yet. Qt's "
        "'bool QQmlTypeData::loadImplicitImport()': leans on "
        "'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def rebuildFromSource(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::rebuildFromSource()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'setupICs'.
    """
    raise NotImplementedError(
        "'QQmlTypeData.rebuildFromSource' has no cute function yet. Qt's "
        "'bool QQmlTypeData::rebuildFromSource()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'setupICs'.")

  @staticmethod
  def resolveType(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::resolveType(const QString &typeName,
    QTypeRevision &version, TypeReference &ref, int lineNumber, int
    columnNumber, bool reportErrors, QQmlType::RegistrationType
    registrationType, bool *typeRecursionDetected)': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.resolveType' has no cute function yet. Qt's 'bool "
        "QQmlTypeData::resolveType(const QString &typeName, QTypeRevision "
        "&version, TypeReference &ref, int lineNumber, int columnNumber, "
        "bool reportErrors, QQmlType::RegistrationType registrationType, "
        "bool *typeRecursionDetected)': leans on 'lcQmlImport()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resolveTypes(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::resolveTypes()': leans on 'lcQmlImport()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.resolveTypes' has no cute function yet. Qt's 'bool "
        "QQmlTypeData::resolveTypes()': leans on 'lcQmlImport()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def restoreIR(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeData::restoreIR(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.restoreIR' has no cute function yet. Qt's 'void "
        "QQmlTypeData::restoreIR(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': leans "
        "on 'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def tryLoadFromDiskCache(*__, **_) -> Never:
    """
    Qt's 'bool QQmlTypeData::tryLoadFromDiskCache()': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeData.tryLoadFromDiskCache' has no cute function yet. Qt's "
        "'bool QQmlTypeData::tryLoadFromDiskCache()': leans on "
        "'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
