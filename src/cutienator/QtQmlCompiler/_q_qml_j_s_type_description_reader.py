"""
QQmlJSTypeDescriptionReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstypedescriptionreader_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSTypeDescriptionReader to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtQml import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
  from . import QQmlJSMetaEnum, QQmlJSMetaMethod
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaEnum = WAIT['QQmlJSMetaEnum']
  QQmlJSMetaMethod = WAIT['QQmlJSMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSTypeDescriptionReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSTypeDescriptionReader: a plain Python object
  standing in front of one C++ QQmlJSTypeDescriptionReader.

  What exists
  -----------

  Every function of Qt's QQmlJSTypeDescriptionReader that has a ritual and
  that Python can call so far, 18 names in all: 'tr', 'errorMessage',
  'warningMessage', 'readDocument', 'readModule', 'readDependencies',
  'readComponent', 'readParameter', 'readStringBinding', 'readBoolBinding',
  'readNumericBinding', 'readNumericVersionBinding', 'readIntBinding',
  'readStringList', 'readEnumValues', 'addError', 'addWarning', 'getArray'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QQmlJSTypeDescriptionReader::operator()(QList<QQmlJSExportedScope>
    *objects, QStringList *dependencies)': names
    'QList<QQmlJSExportedScope>', which has no cute class yet.
  - Qt's 'void QQmlJSTypeDescriptionReader::readSignalOrMethod(QQmlJS::AST::
    UiObjectDefinition *ast, bool isMethod, const QQmlJSScope::Ptr &scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QQmlJSTypeDescriptionReader::readProperty(QQmlJS::AST::UiObjectDefinition
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QQmlJSTypeDescriptionReader::readEnum(QQmlJS::AST::UiObjectDefinition
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<QQmlJSScope::Export>
    QQmlJSTypeDescriptionReader::readExports(QQmlJS::AST::UiScriptBinding
    *ast)': gives a type Python has no way to take yet.
  - Qt's 'void
    QQmlJSTypeDescriptionReader::readAliases(QQmlJS::AST::UiScriptBinding
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QQmlJSTypeDescriptionReader::readInterfaces(QQmlJS::AST::UiScriptBinding
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    QQmlJSTypeDescriptionReader::checkMetaObjectRevisions(QQmlJS::AST::
    UiScriptBinding *ast, QList<QQmlJSScope::Export> *exports)': names
    'QList<QQmlJSScope::Export>', which has no cute class yet.
  - Qt's 'void QQmlJSTypeDescriptionReader::readDeferredNames(QQmlJS::AST::
    UiScriptBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlJSTypeDescriptionReader::readImmediateNames(QQmlJS::AST::
    UiScriptBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlJSTypeDescriptionReader is created at the first use, not by
    'QQmlJSTypeDescriptionReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSTypeDescriptionReader.
  - Each name of Qt's QQmlJSTypeDescriptionReader that has no cute function
    yet, 'checkMetaObjectRevisions', 'readAliases', 'readDeferredNames',
    'readEnum', 'readExports', 'readImmediateNames', 'readInterfaces',
    'readProperty', 'readSignalOrMethod', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlJSTypeDescriptionReader::tr(const char
    *sourceText, const char *disambiguation, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#tr

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
    #  QString QQmlJSTypeDescriptionReader::tr(const char *sourceText, const
    #      char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSTypeDescriptionReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QQmlJSTypeDescriptionReader::errorMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSTypeDescriptionReader::errorMessage() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlJSTypeDescriptionReader12errorMessageEv',
    )

  def warningMessage(self) -> str:
    """
    Calls Qt's 'QString QQmlJSTypeDescriptionReader::warningMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#warningMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSTypeDescriptionReader::warningMessage() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlJSTypeDescriptionReader14warningMessageEv',
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

  @overload(str, str)
  def __init__(self, fileName: str, data: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSTypeDescriptionReader::QQmlJSTypeDescriptionReader(QString
    fileName, QString data)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJSTypeDescriptionReader::QQmlJSTypeDescriptionReader(QString
    #      fileName, QString data)
    self._noteCreation(QQmlJSTypeDescriptionReader, lambda: Rituals.call(
        'ritual_ZN27QQmlJSTypeDescriptionReaderC1E7QStringS0_',
        fileName, data,
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

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  @overload(NoneType)
  def readDocument(self, ast: Optional[QQmlJS.AST.UiProgram]) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypeDescriptionReader::readDocument(QQmlJS::AST::UiProgram *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readDocument

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readDocument(QQmlJS::AST::UiProgram
    #      *ast)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader12readDocumentEPN6QQmlJS3AST'
        '9UiProgramE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  @overload(NoneType)
  def readModule(self, ast: Optional[QQmlJS.AST.UiObjectDefinition]) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypeDescriptionReader::readModule(QQmlJS::AST::UiObjectDefinition
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readModule

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readModule(QQmlJS::AST::
    #      UiObjectDefinition *ast)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader10readModuleEPN6QQmlJS3AST18'
        'UiObjectDefinitionE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readDependencies(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypeDescriptionReader::readDependencies(QQmlJS::AST::
    UiScriptBinding *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readDependencies

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readDependencies(QQmlJS::AST::
    #      UiScriptBinding *ast)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader16readDependenciesEPN6QQmlJS'
        '3AST15UiScriptBindingE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  @overload(NoneType)
  def readComponent(
      self,
      ast: Optional[QQmlJS.AST.UiObjectDefinition],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypeDescriptionReader::readComponent(QQmlJS::AST::
    UiObjectDefinition *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readComponent

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readComponent(QQmlJS::AST::
    #      UiObjectDefinition *ast)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader13readComponentEPN6QQmlJS3AS'
        'T18UiObjectDefinitionE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'], QQmlJSMetaMethod)
  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'], NoneType)
  @overload(NoneType, QQmlJSMetaMethod)
  @overload(NoneType, NoneType)
  def readParameter(
      self,
      ast: Optional[QQmlJS.AST.UiObjectDefinition],
      metaMethod: Optional[QQmlJSMetaMethod],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypeDescriptionReader::readParameter(QQmlJS::AST::
    UiObjectDefinition *ast, QQmlJSMetaMethod *metaMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readParameter

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaMethod : Optional[QQmlJSMetaMethod]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readParameter(QQmlJS::AST::
    #      UiObjectDefinition *ast, QQmlJSMetaMethod *metaMethod)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader13readParameterEPN6QQmlJS3AS'
        'T18UiObjectDefinitionEP16QQmlJSMetaMethod',
        self._addressOf(ast), self._addressOf(metaMethod),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readStringBinding(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> str:
    """
    Calls Qt's 'QString
    QQmlJSTypeDescriptionReader::readStringBinding(QQmlJS::AST::
    UiScriptBinding *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readStringBinding

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSTypeDescriptionReader::readStringBinding(QQmlJS::AST::
    #      UiScriptBinding *ast)
    return self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader17readStringBindingEPN6QQmlJ'
        'S3AST15UiScriptBindingE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readBoolBinding(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypeDescriptionReader::readBoolBinding(QQmlJS::AST::UiScriptBinding
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readBoolBinding

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSTypeDescriptionReader::readBoolBinding(QQmlJS::AST::
    #      UiScriptBinding *ast)
    return self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader15readBoolBindingEPN6QQmlJS3'
        'AST15UiScriptBindingE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readNumericBinding(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> float:
    """
    Calls Qt's 'double
    QQmlJSTypeDescriptionReader::readNumericBinding(QQmlJS::AST::
    UiScriptBinding *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QQmlJSTypeDescriptionReader::readNumericBinding(QQmlJS::AST::
    #      UiScriptBinding *ast)
    return self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader18readNumericBindingEPN6QQml'
        'JS3AST15UiScriptBindingE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readNumericVersionBinding(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision
    QQmlJSTypeDescriptionReader::readNumericVersionBinding(QQmlJS::AST::
    UiScriptBinding *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision
    #      QQmlJSTypeDescriptionReader::readNumericVersionBinding(QQmlJS::
    #      AST::UiScriptBinding *ast)
    address = self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader25readNumericVersionBindingE'
        'PN6QQmlJS3AST15UiScriptBindingE',
        self._addressOf(ast),
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readIntBinding(self, ast: Optional[QQmlJS.AST.UiScriptBinding]) -> int:
    """
    Calls Qt's 'int
    QQmlJSTypeDescriptionReader::readIntBinding(QQmlJS::AST::UiScriptBinding
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readIntBinding

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlJSTypeDescriptionReader::readIntBinding(QQmlJS::AST::
    #      UiScriptBinding *ast)
    return self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader14readIntBindingEPN6QQmlJS3A'
        'ST15UiScriptBindingE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def readStringList(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQmlJSTypeDescriptionReader::readStringList(QQmlJS::AST::UiScriptBinding
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readStringList

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSTypeDescriptionReader::readStringList(QQmlJS::AST::
    #      UiScriptBinding *ast)
    address = self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader14readStringListEPN6QQmlJS3A'
        'ST15UiScriptBindingE',
        self._addressOf(ast),
    )
    return QStringList._cuteOwning(address)

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'], QQmlJSMetaEnum)
  @overload(WAIT['QQmlJS.AST.UiScriptBinding'], NoneType)
  @overload(NoneType, QQmlJSMetaEnum)
  @overload(NoneType, NoneType)
  def readEnumValues(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
      metaEnum: Optional[QQmlJSMetaEnum],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypeDescriptionReader::readEnumValues(QQmlJS::AST::UiScriptBinding
    *ast, QQmlJSMetaEnum *metaEnum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#readEnumValues

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaEnum : Optional[QQmlJSMetaEnum]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSTypeDescriptionReader::readEnumValues(QQmlJS::AST::
    #      UiScriptBinding *ast, QQmlJSMetaEnum *metaEnum)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader14readEnumValuesEPN6QQmlJS3A'
        'ST15UiScriptBindingEP14QQmlJSMetaEnum',
        self._addressOf(ast), self._addressOf(metaEnum),
    )

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def addError(self, loc: QQmlJS.SourceLocation, message: str) -> None:
    """
    Calls Qt's 'void QQmlJSTypeDescriptionReader::addError(const
    QQmlJS::SourceLocation &loc, const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#addError

    Parameters
    ----------

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSTypeDescriptionReader::addError(const
    #      QQmlJS::SourceLocation &loc, const QString &message)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader8addErrorERKN6QQmlJS14Source'
        'LocationERK7QString',
        self._valueOf(loc), message,
    )

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def addWarning(self, loc: QQmlJS.SourceLocation, message: str) -> None:
    """
    Calls Qt's 'void QQmlJSTypeDescriptionReader::addWarning(const
    QQmlJS::SourceLocation &loc, const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#addWarning

    Parameters
    ----------

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSTypeDescriptionReader::addWarning(const
    #      QQmlJS::SourceLocation &loc, const QString &message)
    self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader10addWarningERKN6QQmlJS14Sou'
        'rceLocationERK7QString',
        self._valueOf(loc), message,
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def getArray(
      self,
      ast: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> Optional[QQmlJS.AST.ArrayPattern]:
    """
    Calls Qt's 'QQmlJS::AST::ArrayPattern
    *QQmlJSTypeDescriptionReader::getArray(QQmlJS::AST::UiScriptBinding
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypedescriptionreader.html#getArray

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlJS.AST.ArrayPattern]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJS::AST::ArrayPattern
    #      *QQmlJSTypeDescriptionReader::getArray(QQmlJS::AST::
    #      UiScriptBinding *ast)
    address = self.uglySide.call(
        'ritual_ZN27QQmlJSTypeDescriptionReader8getArrayEPN6QQmlJS3AST15UiS'
        'criptBindingE',
        self._addressOf(ast),
    )
    return QQmlJS.AST.ArrayPattern._cuteAt(address)

  @staticmethod
  def checkMetaObjectRevisions(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSTypeDescriptionReader::checkMetaObjectRevisions(QQmlJS::AST::
    UiScriptBinding *ast, QList<QQmlJSScope::Export> *exports)': names
    'QList<QQmlJSScope::Export>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.checkMetaObjectRevisions' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::checkMetaObjectRevisions(QQmlJS::AST::"
        "UiScriptBinding *ast, QList<QQmlJSScope::Export> *exports)': names "
        "'QList<QQmlJSScope::Export>', which has no cute class yet.")

  @staticmethod
  def readAliases(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSTypeDescriptionReader::readAliases(QQmlJS::AST::UiScriptBinding
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readAliases' has no cute function "
        "yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readAliases(QQmlJS::AST::UiScriptBindi"
        "ng *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def readDeferredNames(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypeDescriptionReader::readDeferredNames(QQmlJS::AST::
    UiScriptBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readDeferredNames' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readDeferredNames(QQmlJS::AST::UiScrip"
        "tBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def readEnum(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSTypeDescriptionReader::readEnum(QQmlJS::AST::UiObjectDefinition
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readEnum' has no cute function yet. "
        "Qt's 'void "
        "QQmlJSTypeDescriptionReader::readEnum(QQmlJS::AST::UiObjectDefiniti"
        "on *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def readExports(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJSScope::Export>
    QQmlJSTypeDescriptionReader::readExports(QQmlJS::AST::UiScriptBinding
    *ast)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readExports' has no cute function "
        "yet. Qt's 'QList<QQmlJSScope::Export> "
        "QQmlJSTypeDescriptionReader::readExports(QQmlJS::AST::UiScriptBindi"
        "ng *ast)': gives a type Python has no way to take yet.")

  @staticmethod
  def readImmediateNames(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypeDescriptionReader::readImmediateNames(QQmlJS::AST::
    UiScriptBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readImmediateNames' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readImmediateNames(QQmlJS::AST::UiScri"
        "ptBinding *ast, const QQmlJSScope::Ptr &scope)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def readInterfaces(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSTypeDescriptionReader::readInterfaces(QQmlJS::AST::UiScriptBinding
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readInterfaces' has no cute function "
        "yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readInterfaces(QQmlJS::AST::UiScriptBi"
        "nding *ast, const QQmlJSScope::Ptr &scope)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def readProperty(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSTypeDescriptionReader::readProperty(QQmlJS::AST::UiObjectDefinition
    *ast, const QQmlJSScope::Ptr &scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readProperty' has no cute function "
        "yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readProperty(QQmlJS::AST::UiObjectDefi"
        "nition *ast, const QQmlJSScope::Ptr &scope)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def readSignalOrMethod(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypeDescriptionReader::readSignalOrMethod(QQmlJS::AST::
    UiObjectDefinition *ast, bool isMethod, const QQmlJSScope::Ptr &scope)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeDescriptionReader.readSignalOrMethod' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSTypeDescriptionReader::readSignalOrMethod(QQmlJS::AST::UiObje"
        "ctDefinition *ast, bool isMethod, const QQmlJSScope::Ptr &scope)': "
        "takes a type Python has no way to hand over yet.")
