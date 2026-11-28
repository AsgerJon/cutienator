"""
QQmlJSUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSUtils to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSMetaProperty, QQmlJSResourceFileMapper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaProperty = WAIT['QQmlJSMetaProperty']
  QQmlJSResourceFileMapper = WAIT['QQmlJSResourceFileMapper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSUtils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSUtils: a plain Python object standing in front
  of one C++ QQmlJSUtils.

  C++ hands a QQmlJSUtils around as a copy, so every C++ QQmlJSUtils behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSUtils that has a ritual and that Python can
  call so far, 5 names in all: 'constRefify',
  'bindablePropertyHasDefaultAccessor', 'resourceFilesFromBuildFolders',
  'qmlSourcePathFromBuildPath', 'qmlBuildPathFromSourcePath'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<QQmlJSMetaProperty>
    QQmlJSUtils::changeHandlerProperty(const QQmlJSScope::ConstPtr &scope,
    QStringView signalName)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::optional<QQmlJSMetaProperty>
    QQmlJSUtils::propertyFromChangedHandler(const QQmlJSScope::ConstPtr
    &scope, QStringView changedHandler)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSUtils::hasCompositeBase(const QQmlJSScope::ConstPtr
    &scope)': takes a type Python has no way to hand over yet.
  - Qt's 'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSTypeResolver
    *typeResolver, const QQmlJSMetaProperty &property, const
    QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor &visitor)':
    takes a type Python has no way to hand over yet.
  - Qt's 'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSScopesById
    &idScopes, const QQmlJSMetaProperty &property, const
    QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor &visitor)':
    takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QQmlJSFixSuggestion> QQmlJSUtils::didYouMean(const
    QString &userInput, QStringList candidates, const QString &filename,
    const QQmlJS::SourceLocation &location)': gives a type Python has no way
    to take yet.
  - Qt's 'std::variant<QString, QQmlJS::DiagnosticMessage>
    QQmlJSUtils::sourceDirectoryPath(const QQmlJSImporter *importer, const
    QString &buildDirectoryPath)': gives a type Python has no way to take
    yet.
  - Qt's 'QStringList QQmlJSUtils::cleanPaths(QStringList &&paths)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QString QQmlJSUtils::getScopeName(const QQmlJSScope::ConstPtr
    &scope, QQmlJSScope::ScopeType type)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QString QQmlJSUtils::fileSelectorFor(const QQmlJSScope::ConstPtr
    &scope1)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSUtils::~QQmlJSUtils()': the destructor: Python removes its
    C++ QQmlJSUtils by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 22 functions Qt declares: 6 a template.

  What to expect
  --------------

  - The C++ QQmlJSUtils is created at the first use, not by
    'QQmlJSUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSUtils back gives a copy the ritual made for
    Python, in a new cute QQmlJSUtils.
  - Each name of Qt's QQmlJSUtils that has no cute function yet,
    'changeHandlerProperty', 'cleanPaths', 'deduplicate', 'didYouMean',
    'escapeString', 'fileSelectorFor', 'getScopeName', 'hasCompositeBase',
    'propertyFromChangedHandler', 'resolveAlias',
    'searchBaseAndExtensionTypes', 'sourceDirectoryPath', 'toLiteral',
    'traverseFollowingMetaObjectHierarchy',
    'traverseFollowingQmlIrObjectStructure', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSUtils, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PropertyAccessor(CuteNum):
    """
    The enum 'QQmlJSUtils::PropertyAccessor' of Qt, with the 2 names Qt gives
    in it.
    """

    PropertyAccessor_Read = Kee[int](0)
    PropertyAccessor_Write = Kee[int](1)

  class ResolvedAliasTarget(CuteNum):
    """
    The enum 'QQmlJSUtils::ResolvedAliasTarget' of Qt, with the 3 names Qt
    gives in it.
    """

    AliasTarget_Invalid = Kee[int](0)
    AliasTarget_Property = Kee[int](1)
    AliasTarget_Object = Kee[int](2)

  #  The classes Qt writes inside QQmlJSUtils, each a class in here as in
  #  C++.

  class AliasResolutionVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSUtils::AliasResolutionVisitor: a plain Python
    object standing in front of one C++ QQmlJSUtils::AliasResolutionVisitor.

    C++ hands a QQmlJSUtils::AliasResolutionVisitor around as a copy, so
    every C++ QQmlJSUtils::AliasResolutionVisitor behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSUtils::AliasResolutionVisitor yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSUtils::AliasResolutionVisitor::~AliasResolutionVisitor()':
      the destructor: Python removes its C++
      QQmlJSUtils::AliasResolutionVisitor by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlJSUtils::AliasResolutionVisitor is created at the first
      use, not by 'QQmlJSUtils::AliasResolutionVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSUtils::AliasResolutionVisitor back gives a
      copy the ritual made for Python, in a new cute
      QQmlJSUtils::AliasResolutionVisitor.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSUtils::AliasResolutionVisitor'

    #  Qt's '~QQmlJSUtils::AliasResolutionVisitor()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlJSUtils::AliasResolutionVisitor
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlJSUtils22AliasResolutionVisitorD1Ev'

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

  class ResolvedAlias(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSUtils::ResolvedAlias: a plain Python object
    standing in front of one C++ QQmlJSUtils::ResolvedAlias.

    C++ hands a QQmlJSUtils::ResolvedAlias around as a copy, so every C++
    QQmlJSUtils::ResolvedAlias behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlJSUtils::ResolvedAlias yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSUtils::ResolvedAlias::~ResolvedAlias()': the destructor:
      Python removes its C++ QQmlJSUtils::ResolvedAlias by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlJSUtils::ResolvedAlias is created at the first use, not by
      'QQmlJSUtils::ResolvedAlias(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSUtils::ResolvedAlias back gives a copy the
      ritual made for Python, in a new cute QQmlJSUtils::ResolvedAlias.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSUtils::ResolvedAlias'

    #  Qt's '~QQmlJSUtils::ResolvedAlias()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSUtils::ResolvedAlias behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlJSUtils13ResolvedAliasD1Ev'

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
  def constRefify(type: str) -> str:
    """
    Calls Qt's 'QString QQmlJSUtils::constRefify(QString type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsutils.html#constRefify

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSUtils::constRefify(QString type)
    return Rituals.call('ritual_ZN11QQmlJSUtils11constRefifyE7QString', type)

  @staticmethod
  @overload(QQmlJSMetaProperty, PropertyAccessor)
  def bindablePropertyHasDefaultAccessor(
      p: QQmlJSMetaProperty,
      accessor: PropertyAccessor,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSUtils::bindablePropertyHasDefaultAccessor(const
    QQmlJSMetaProperty &p, PropertyAccessor accessor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsutils.html

    Parameters
    ----------

    p : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.

    accessor : PropertyAccessor
      Passed on as its number.
    """
    #  bool QQmlJSUtils::bindablePropertyHasDefaultAccessor(const
    #      QQmlJSMetaProperty &p, PropertyAccessor accessor)
    return Rituals.call(
        'ritual_ZN11QQmlJSUtils34bindablePropertyHasDefaultAccessorERK18QQm'
        'lJSMetaPropertyNS_16PropertyAccessorE',
        CuteMixin._valueOf(p), accessor.value,
    )

  @staticmethod
  @overload(QStringList)
  def resourceFilesFromBuildFolders(
      buildFolders: QStringList,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSUtils::resourceFilesFromBuildFolders(const
    QStringList &buildFolders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsutils.html#resourceFilesFromBuildFolders

    Parameters
    ----------

    buildFolders : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSUtils::resourceFilesFromBuildFolders(const
    #      QStringList &buildFolders)
    address = Rituals.call(
        'ritual_ZN11QQmlJSUtils29resourceFilesFromBuildFoldersERK5QListI7QS'
        'tringE',
        CuteMixin._valueOf(buildFolders),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QQmlJSResourceFileMapper, str)
  @overload(NoneType, str)
  def qmlSourcePathFromBuildPath(
      mapper: Optional[QQmlJSResourceFileMapper],
      pathInBuildFolder: str,
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSUtils::qmlSourcePathFromBuildPath(const
    QQmlJSResourceFileMapper *mapper, const QString &pathInBuildFolder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsutils.html#qmlSourcePathFromBuildPath

    Parameters
    ----------

    mapper : Optional[QQmlJSResourceFileMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pathInBuildFolder : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSUtils::qmlSourcePathFromBuildPath(const
    #      QQmlJSResourceFileMapper *mapper, const QString
    #      &pathInBuildFolder)
    return Rituals.call(
        'ritual_ZN11QQmlJSUtils26qmlSourcePathFromBuildPathEPK24QQmlJSResou'
        'rceFileMapperRK7QString',
        CuteMixin._addressOf(mapper), pathInBuildFolder,
    )

  @staticmethod
  @overload(QQmlJSResourceFileMapper, str)
  @overload(NoneType, str)
  def qmlBuildPathFromSourcePath(
      mapper: Optional[QQmlJSResourceFileMapper],
      pathInBuildFolder: str,
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSUtils::qmlBuildPathFromSourcePath(const
    QQmlJSResourceFileMapper *mapper, const QString &pathInBuildFolder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsutils.html#qmlBuildPathFromSourcePath

    Parameters
    ----------

    mapper : Optional[QQmlJSResourceFileMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pathInBuildFolder : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSUtils::qmlBuildPathFromSourcePath(const
    #      QQmlJSResourceFileMapper *mapper, const QString
    #      &pathInBuildFolder)
    return Rituals.call(
        'ritual_ZN11QQmlJSUtils26qmlBuildPathFromSourcePathEPK24QQmlJSResou'
        'rceFileMapperRK7QString',
        CuteMixin._addressOf(mapper), pathInBuildFolder,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSUtils'

  #  Qt's '~QQmlJSUtils()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlJSUtils behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQmlJSUtilsD1Ev'

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
  def changeHandlerProperty(*__, **_) -> Never:
    """
    Qt's 'std::optional<QQmlJSMetaProperty>
    QQmlJSUtils::changeHandlerProperty(const QQmlJSScope::ConstPtr &scope,
    QStringView signalName)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.changeHandlerProperty' has no cute function yet. Qt's "
        "'std::optional<QQmlJSMetaProperty> "
        "QQmlJSUtils::changeHandlerProperty(const QQmlJSScope::ConstPtr "
        "&scope, QStringView signalName)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def cleanPaths(*__, **_) -> Never:
    """
    Qt's 'QStringList QQmlJSUtils::cleanPaths(QStringList &&paths)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.cleanPaths' has no cute function yet. Qt's "
        "'QStringList QQmlJSUtils::cleanPaths(QStringList &&paths)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def deduplicate(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::deduplicate': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.deduplicate' has no cute function yet. Qt's "
        "'QQmlJSUtils::deduplicate': a template: a pattern and no single "
        "function.")

  @staticmethod
  def didYouMean(*__, **_) -> Never:
    """
    Qt's 'std::optional<QQmlJSFixSuggestion> QQmlJSUtils::didYouMean(const
    QString &userInput, QStringList candidates, const QString &filename,
    const QQmlJS::SourceLocation &location)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.didYouMean' has no cute function yet. Qt's "
        "'std::optional<QQmlJSFixSuggestion> QQmlJSUtils::didYouMean(const "
        "QString &userInput, QStringList candidates, const QString "
        "&filename, const QQmlJS::SourceLocation &location)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def escapeString(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::escapeString': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.escapeString' has no cute function yet. Qt's "
        "'QQmlJSUtils::escapeString': a template: a pattern and no single "
        "function.")

  @staticmethod
  def fileSelectorFor(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSUtils::fileSelectorFor(const QQmlJSScope::ConstPtr
    &scope1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.fileSelectorFor' has no cute function yet. Qt's "
        "'QString QQmlJSUtils::fileSelectorFor(const QQmlJSScope::ConstPtr "
        "&scope1)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getScopeName(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSUtils::getScopeName(const QQmlJSScope::ConstPtr
    &scope, QQmlJSScope::ScopeType type)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.getScopeName' has no cute function yet. Qt's 'QString "
        "QQmlJSUtils::getScopeName(const QQmlJSScope::ConstPtr &scope, "
        "QQmlJSScope::ScopeType type)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def hasCompositeBase(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSUtils::hasCompositeBase(const QQmlJSScope::ConstPtr
    &scope)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.hasCompositeBase' has no cute function yet. Qt's "
        "'bool QQmlJSUtils::hasCompositeBase(const QQmlJSScope::ConstPtr "
        "&scope)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def propertyFromChangedHandler(*__, **_) -> Never:
    """
    Qt's 'std::optional<QQmlJSMetaProperty>
    QQmlJSUtils::propertyFromChangedHandler(const QQmlJSScope::ConstPtr
    &scope, QStringView changedHandler)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.propertyFromChangedHandler' has no cute function yet. "
        "Qt's 'std::optional<QQmlJSMetaProperty> "
        "QQmlJSUtils::propertyFromChangedHandler(const "
        "QQmlJSScope::ConstPtr &scope, QStringView changedHandler)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def resolveAlias(*__, **_) -> Never:
    """
    - Qt's 'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSTypeResolver
      *typeResolver, const QQmlJSMetaProperty &property, const
      QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor &visitor)':
      takes a type Python has no way to hand over yet.
    - Qt's 'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSScopesById
      &idScopes, const QQmlJSMetaProperty &property, const
      QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor &visitor)':
      takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.resolveAlias' has no cute function yet. Qt's "
        "'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSTypeResolver "
        "*typeResolver, const QQmlJSMetaProperty &property, const "
        "QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor "
        "&visitor)': takes a type Python has no way to hand over yet. Qt's "
        "'ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSScopesById "
        "&idScopes, const QQmlJSMetaProperty &property, const "
        "QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor "
        "&visitor)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def searchBaseAndExtensionTypes(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::searchBaseAndExtensionTypes': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.searchBaseAndExtensionTypes' has no cute function "
        "yet. Qt's 'QQmlJSUtils::searchBaseAndExtensionTypes': a template: "
        "a pattern and no single function.")

  @staticmethod
  def sourceDirectoryPath(*__, **_) -> Never:
    """
    Qt's 'std::variant<QString, QQmlJS::DiagnosticMessage>
    QQmlJSUtils::sourceDirectoryPath(const QQmlJSImporter *importer, const
    QString &buildDirectoryPath)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.sourceDirectoryPath' has no cute function yet. Qt's "
        "'std::variant<QString, QQmlJS::DiagnosticMessage> "
        "QQmlJSUtils::sourceDirectoryPath(const QQmlJSImporter *importer, "
        "const QString &buildDirectoryPath)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def toLiteral(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::toLiteral': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.toLiteral' has no cute function yet. Qt's "
        "'QQmlJSUtils::toLiteral': a template: a pattern and no single "
        "function.")

  @staticmethod
  def traverseFollowingMetaObjectHierarchy(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::traverseFollowingMetaObjectHierarchy': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.traverseFollowingMetaObjectHierarchy' has no cute "
        "function yet. Qt's "
        "'QQmlJSUtils::traverseFollowingMetaObjectHierarchy': a template: a "
        "pattern and no single function.")

  @staticmethod
  def traverseFollowingQmlIrObjectStructure(*__, **_) -> Never:
    """
    Qt's 'QQmlJSUtils::traverseFollowingQmlIrObjectStructure': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSUtils.traverseFollowingQmlIrObjectStructure' has no cute "
        "function yet. Qt's "
        "'QQmlJSUtils::traverseFollowingQmlIrObjectStructure': a template: "
        "a pattern and no single function.")
