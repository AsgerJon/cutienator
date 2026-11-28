"""
QQmlDirParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlDirParser to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDirParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDirParser: a plain Python object standing in
  front of one C++ QQmlDirParser.

  C++ hands a QQmlDirParser around as a copy, so every C++ QQmlDirParser
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDirParser that has a ritual and that Python can
  call so far, 18 names in all: 'clear', 'parse',
  'disambiguateFileSelectors', 'hasError', 'setError', 'hasTypeNamespace',
  'typeNamespace', 'setTypeNamespace', 'checkNonRelative',
  'designerSupported', 'isStaticModule', 'isSystemModule', 'typeInfos',
  'classNames', 'preferredPath', 'linkTarget', 'reportError',
  'insertComponentOrScript'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QQmlJS::DiagnosticMessage> QQmlDirParser::errors(const
    QString &uri) const': gives a type Python has no way to take yet.
  - Qt's 'QMultiHash<QString, Component> QQmlDirParser::components() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<Import> QQmlDirParser::dependencies() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<Import> QQmlDirParser::imports() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Script> QQmlDirParser::scripts() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Plugin> QQmlDirParser::plugins() const': gives a type Python
    has no way to take yet.
  - Qt's 'QQmlDirParser::~QQmlDirParser()': the destructor: Python removes
    its C++ QQmlDirParser by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 1 not a gap; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QQmlDirParser is created at the first use, not by
    'QQmlDirParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDirParser back gives a copy the ritual made for
    Python, in a new cute QQmlDirParser.
  - Each name of Qt's QQmlDirParser that has no cute function yet,
    'components', 'dependencies', 'errors', 'imports', 'plugins',
    'scanQuotedWord', 'scripts', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlDirParser, each a class in here as in
  #  C++.

  class Component(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDirParser::Component: a plain Python object
    standing in front of one C++ QQmlDirParser::Component.

    C++ hands a QQmlDirParser::Component around as a copy, so every C++
    QQmlDirParser::Component behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlDirParser::Component yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDirParser::Component::~Component()': the destructor: Python
      removes its C++ QQmlDirParser::Component by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlDirParser::Component is created at the first use, not by
      'QQmlDirParser::Component(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlDirParser::Component back gives a copy the
      ritual made for Python, in a new cute QQmlDirParser::Component.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTypeRevision = WAIT['QTypeRevision']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDirParser::Component'

    #  Qt's '~QQmlDirParser::Component()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlDirParser::Component behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlDirParser9ComponentD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Component::Component()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldirparser-component.html#Component
      """
      #  QQmlDirParser::Component::Component()
      self._noteCreation(QQmlDirParser.Component, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser9ComponentC1Ev',
      ))

    @overload(str, str, QTypeRevision)
    def __init__(
        self,
        typeName: str,
        fileName: str,
        version: QTypeRevision,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQmlDirParser::Component::Component(const QString &typeName, const
      QString &fileName, QTypeRevision version)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldirparser-component.html#Component

      Parameters
      ----------

      typeName : str
        Passed on as it is: a QString is made of it for the call.

      fileName : str
        Passed on as it is: a QString is made of it for the call.

      version : QTypeRevision
        Passed on as a value: Qt reads the C++ QTypeRevision, which stays
        Python's own.
      """
      #  QQmlDirParser::Component::Component(const QString &typeName, const
      #      QString &fileName, QTypeRevision version)
      self._noteCreation(QQmlDirParser.Component, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser9ComponentC1ERK7QStringS3_13QTypeRevisio'
          'n',
          typeName, fileName, self._valueOf(version),
      ))

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

  class Import(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDirParser::Import: a plain Python object
    standing in front of one C++ QQmlDirParser::Import.

    C++ hands a QQmlDirParser::Import around as a copy, so every C++
    QQmlDirParser::Import behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlDirParser::Import that has a ritual and that
    Python can call so far, 2 names in all: '__eq__', '__ne__'. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDirParser::Import::~Import()': the destructor: Python removes
      its C++ QQmlDirParser::Import by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlDirParser::Import is created at the first use, not by
      'QQmlDirParser::Import(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlDirParser::Import back gives a copy the ritual
      made for Python, in a new cute QQmlDirParser::Import.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTypeRevision = WAIT['QTypeRevision']

    #  The enums Qt writes inside QQmlDirParser::Import, each a class in here
    #  as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Flag(CuteFlags):
      """
      The flags enum 'QQmlDirParser::Import::Flag' of Qt, with the 4 names Qt
      gives in it. Qt names the type of its combinations
      'QQmlDirParser::Import::Flags'.
      """

      Default = 0x0
      Auto = 0x1
      Optional = 0x2
      OptionalDefault = 0x4

    Flags = Flag

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDirParser::Import'

    #  Qt's '~QQmlDirParser::Import()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlDirParser::Import behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlDirParser6ImportD1Ev'

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

    @overload(THIS)
    def __eq__(self, rhs: QQmlDirParser.Import) -> bool:
      """
      Calls Qt's 'bool operator==(const Import &lhs, const Import &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldirparser-import.html#operator==

      Parameters
      ----------

      rhs : QQmlDirParser.Import
        Passed on as a value: Qt reads the C++ QQmlDirParser::Import, which
        stays Python's own.
      """
      #  bool operator==(const Import &lhs, const Import &rhs)
      return Rituals.call(
          'ritual_ZeqRKN13QQmlDirParser6ImportES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    def __ne__(self, rhs: QQmlDirParser.Import) -> bool:
      """
      Calls Qt's 'bool operator!=(const Import &lhs, const Import &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldirparser-import.html#operator!=

      Parameters
      ----------

      rhs : QQmlDirParser.Import
        Passed on as a value: Qt reads the C++ QQmlDirParser::Import, which
        stays Python's own.
      """
      #  bool operator!=(const Import &lhs, const Import &rhs)
      return Rituals.call(
          'ritual_ZneRKN13QQmlDirParser6ImportES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Import::Import()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-import.html#Import
      """
      #  QQmlDirParser::Import::Import()
      self._noteCreation(QQmlDirParser.Import, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6ImportC1Ev',
      ))

    @overload(str, QTypeRevision, Flags)
    def __init__(
        self,
        module: str,
        version: QTypeRevision,
        flags: Flags,
    ) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Import::Import(QString
      module, QTypeRevision version, Flags flags)', which is called at the
      first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-import.html#Import

      Parameters
      ----------

      module : str
        Passed on as it is: a QString is made of it for the call.

      version : QTypeRevision
        Passed on as a value: Qt reads the C++ QTypeRevision, which stays
        Python's own.

      flags : Flags
        Passed on as its number.
      """
      #  QQmlDirParser::Import::Import(QString module, QTypeRevision version,
      #      Flags flags)
      self._noteCreation(QQmlDirParser.Import, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6ImportC1E7QString13QTypeRevision6QFlags'
          'INS0_4FlagEE',
          module, self._valueOf(version), flags.value,
      ))

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

  class Plugin(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDirParser::Plugin: a plain Python object
    standing in front of one C++ QQmlDirParser::Plugin.

    C++ hands a QQmlDirParser::Plugin around as a copy, so every C++
    QQmlDirParser::Plugin behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlDirParser::Plugin yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDirParser::Plugin::~Plugin()': the destructor: Python removes
      its C++ QQmlDirParser::Plugin by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlDirParser::Plugin is created at the first use, not by
      'QQmlDirParser::Plugin(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlDirParser::Plugin back gives a copy the ritual
      made for Python, in a new cute QQmlDirParser::Plugin.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDirParser::Plugin'

    #  Qt's '~QQmlDirParser::Plugin()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlDirParser::Plugin behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlDirParser6PluginD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Plugin::Plugin()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-plugin.html#Plugin
      """
      #  QQmlDirParser::Plugin::Plugin()
      self._noteCreation(QQmlDirParser.Plugin, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6PluginC1Ev',
      ))

    @overload(str, str, bool)
    def __init__(self, name: str, path: str, optional: bool) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Plugin::Plugin(const
      QString &name, const QString &path, bool optional)', which is called at
      the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-plugin.html#Plugin

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.

      path : str
        Passed on as it is: a QString is made of it for the call.

      optional : bool
        Passed on as it is.
      """
      #  QQmlDirParser::Plugin::Plugin(const QString &name, const QString
      #      &path, bool optional)
      self._noteCreation(QQmlDirParser.Plugin, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6PluginC1ERK7QStringS3_b',
          name, path, optional,
      ))

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

  class Script(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDirParser::Script: a plain Python object
    standing in front of one C++ QQmlDirParser::Script.

    C++ hands a QQmlDirParser::Script around as a copy, so every C++
    QQmlDirParser::Script behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlDirParser::Script yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDirParser::Script::~Script()': the destructor: Python removes
      its C++ QQmlDirParser::Script by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlDirParser::Script is created at the first use, not by
      'QQmlDirParser::Script(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlDirParser::Script back gives a copy the ritual
      made for Python, in a new cute QQmlDirParser::Script.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTypeRevision = WAIT['QTypeRevision']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDirParser::Script'

    #  Qt's '~QQmlDirParser::Script()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlDirParser::Script behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlDirParser6ScriptD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Script::Script()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-script.html#Script
      """
      #  QQmlDirParser::Script::Script()
      self._noteCreation(QQmlDirParser.Script, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6ScriptC1Ev',
      ))

    @overload(str, str, QTypeRevision)
    def __init__(
        self,
        nameSpace: str,
        fileName: str,
        version: QTypeRevision,
    ) -> None:
      """
      Notes what was given, for Qt's 'QQmlDirParser::Script::Script(const
      QString &nameSpace, const QString &fileName, QTypeRevision version)',
      which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmldirparser-script.html#Script

      Parameters
      ----------

      nameSpace : str
        Passed on as it is: a QString is made of it for the call.

      fileName : str
        Passed on as it is: a QString is made of it for the call.

      version : QTypeRevision
        Passed on as a value: Qt reads the C++ QTypeRevision, which stays
        Python's own.
      """
      #  QQmlDirParser::Script::Script(const QString &nameSpace, const
      #      QString &fileName, QTypeRevision version)
      self._noteCreation(QQmlDirParser.Script, lambda: Rituals.call(
          'ritual_ZN13QQmlDirParser6ScriptC1ERK7QStringS3_13QTypeRevision',
          nameSpace, fileName, self._valueOf(version),
      ))

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
  @overload(str, str, str)
  @overload(NoneType, str, str)
  def checkNonRelative(
      item: Optional[str],
      typeName: str,
      fileName: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlDirParser::checkNonRelative(const char *item, const
    QString &typeName, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#checkNonRelative

    Parameters
    ----------

    item : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDirParser::checkNonRelative(const char *item, const QString
    #      &typeName, const QString &fileName)
    Rituals.call(
        'ritual_ZN13QQmlDirParser16checkNonRelativeEPKcRK7QStringS4_',
        CuteMixin._bytesOf(item), typeName, fileName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDirParser'

  #  Qt's '~QQmlDirParser()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlDirParser behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QQmlDirParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#hasError
    """
    #  bool QQmlDirParser::hasError() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser8hasErrorEv')

  def hasTypeNamespace(self) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::hasTypeNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#hasTypeNamespace
    """
    #  bool QQmlDirParser::hasTypeNamespace() const
    return self.uglySide.call(
        'ritual_ZNK13QQmlDirParser16hasTypeNamespaceEv',
    )

  def typeNamespace(self) -> str:
    """
    Calls Qt's 'QString QQmlDirParser::typeNamespace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#typeNamespace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDirParser::typeNamespace() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser13typeNamespaceEv')

  def designerSupported(self) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::designerSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#designerSupported
    """
    #  bool QQmlDirParser::designerSupported() const
    return self.uglySide.call(
        'ritual_ZNK13QQmlDirParser17designerSupportedEv',
    )

  def isStaticModule(self) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::isStaticModule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#isStaticModule
    """
    #  bool QQmlDirParser::isStaticModule() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser14isStaticModuleEv')

  def isSystemModule(self) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::isSystemModule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#isSystemModule
    """
    #  bool QQmlDirParser::isSystemModule() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser14isSystemModuleEv')

  def typeInfos(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDirParser::typeInfos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#typeInfos

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDirParser::typeInfos() const
    address = self.uglySide.call('ritual_ZNK13QQmlDirParser9typeInfosEv')
    return QStringList._cuteOwning(address)

  def classNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDirParser::classNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#classNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDirParser::classNames() const
    address = self.uglySide.call('ritual_ZNK13QQmlDirParser10classNamesEv')
    return QStringList._cuteOwning(address)

  def preferredPath(self) -> str:
    """
    Calls Qt's 'QString QQmlDirParser::preferredPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#preferredPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDirParser::preferredPath() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser13preferredPathEv')

  def linkTarget(self) -> str:
    """
    Calls Qt's 'QString QQmlDirParser::linkTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#linkTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDirParser::linkTarget() const
    return self.uglySide.call('ritual_ZNK13QQmlDirParser10linkTargetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlJS.DiagnosticMessage'])
  def setError(self, a0: QQmlJS.DiagnosticMessage) -> None:
    """
    Calls Qt's 'void QQmlDirParser::setError(const QQmlJS::DiagnosticMessage
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#setError

    Parameters
    ----------

    a0 : QQmlJS.DiagnosticMessage
      Passed on as a value: Qt reads the C++ QQmlJS::DiagnosticMessage, which
      stays Python's own.
    """
    #  void QQmlDirParser::setError(const QQmlJS::DiagnosticMessage &a0)
    self.uglySide.call(
        'ritual_ZN13QQmlDirParser8setErrorERKN6QQmlJS17DiagnosticMessageE',
        self._valueOf(a0),
    )

  @overload(str)
  def setTypeNamespace(self, s: str) -> None:
    """
    Calls Qt's 'void QQmlDirParser::setTypeNamespace(const QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#setTypeNamespace

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDirParser::setTypeNamespace(const QString &s)
    self.uglySide.call(
        'ritual_ZN13QQmlDirParser16setTypeNamespaceERK7QString', s,
    )

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

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlDirParser::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#clear
    """
    #  void QQmlDirParser::clear()
    self.uglySide.call('ritual_ZN13QQmlDirParser5clearEv')

  @overload(str)
  def parse(self, source: str) -> bool:
    """
    Calls Qt's 'bool QQmlDirParser::parse(const QString &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#parse

    Parameters
    ----------

    source : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlDirParser::parse(const QString &source)
    return self.uglySide.call(
        'ritual_ZN13QQmlDirParser5parseERK7QString', source,
    )

  def disambiguateFileSelectors(self) -> None:
    """
    Calls Qt's 'void QQmlDirParser::disambiguateFileSelectors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#disambiguateFileSelectors
    """
    #  void QQmlDirParser::disambiguateFileSelectors()
    self.uglySide.call(
        'ritual_ZN13QQmlDirParser25disambiguateFileSelectorsEv',
    )

  @overload(int, int, str)
  def reportError(self, line: int, column: int, message: str) -> None:
    """
    Calls Qt's 'void QQmlDirParser::reportError(quint16 line, quint16 column,
    const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldirparser.html#reportError

    Parameters
    ----------

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDirParser::reportError(quint16 line, quint16 column, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN13QQmlDirParser11reportErrorEttRK7QString',
        line, column, message,
    )

  @overload(str, str, QTypeRevision)
  def insertComponentOrScript(
      self,
      name: str,
      fileName: str,
      version: QTypeRevision,
  ) -> None:
    """
    Calls Qt's 'void QQmlDirParser::insertComponentOrScript(const QString
    &name, const QString &fileName, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldirparser.html#insertComponentOrScript

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlDirParser::insertComponentOrScript(const QString &name, const
    #      QString &fileName, QTypeRevision version)
    self.uglySide.call(
        'ritual_ZN13QQmlDirParser23insertComponentOrScriptERK7QStringS2_13Q'
        'TypeRevision',
        name, fileName, self._valueOf(version),
    )

  @staticmethod
  def components(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, Component> QQmlDirParser::components() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.components' has no cute function yet. Qt's "
        "'QMultiHash<QString, Component> QQmlDirParser::components() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def dependencies(*__, **_) -> Never:
    """
    Qt's 'QList<Import> QQmlDirParser::dependencies() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.dependencies' has no cute function yet. Qt's "
        "'QList<Import> QQmlDirParser::dependencies() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def errors(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::DiagnosticMessage> QQmlDirParser::errors(const
    QString &uri) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.errors' has no cute function yet. Qt's "
        "'QList<QQmlJS::DiagnosticMessage> QQmlDirParser::errors(const "
        "QString &uri) const': gives a type Python has no way to take yet.")

  @staticmethod
  def imports(*__, **_) -> Never:
    """
    Qt's 'QList<Import> QQmlDirParser::imports() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.imports' has no cute function yet. Qt's "
        "'QList<Import> QQmlDirParser::imports() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QList<Plugin> QQmlDirParser::plugins() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.plugins' has no cute function yet. Qt's "
        "'QList<Plugin> QQmlDirParser::plugins() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def scanQuotedWord(*__, **_) -> Never:
    """
    Qt's 'QString QQmlDirParser::scanQuotedWord(const QChar *&ch, quint16
    lineNumber, quint16 columnNumber)': takes or gives a type that cannot be
    passed yet: const QChar *&.
    """
    raise NotImplementedError(
        "'QQmlDirParser.scanQuotedWord' has no cute function yet. Qt's "
        "'QString QQmlDirParser::scanQuotedWord(const QChar *&ch, quint16 "
        "lineNumber, quint16 columnNumber)': takes or gives a type that "
        "cannot be passed yet: const QChar *&.")

  @staticmethod
  def scripts(*__, **_) -> Never:
    """
    Qt's 'QList<Script> QQmlDirParser::scripts() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDirParser.scripts' has no cute function yet. Qt's "
        "'QList<Script> QQmlDirParser::scripts() const': gives a type "
        "Python has no way to take yet.")
