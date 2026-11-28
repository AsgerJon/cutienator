"""
QLibraryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlibrary_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QLibraryPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QLibrary

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLibraryPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLibraryPrivate: a plain Python object standing in
  front of one C++ QLibraryPrivate.

  What exists
  -----------

  Every function of Qt's QLibraryPrivate that has a ritual and that Python
  can call so far, 4 names in all: 'loadHints', 'prefix_sys', 'get',
  'mergeLoadHints'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLibraryPrivate::~QLibraryPrivate()': the destructor: Python never
    removes a C++ QLibraryPrivate.

  What has no ritual
  ------------------

  14 of the 20 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 cannot be
  called and cannot be called through the meta-object and cannot be copied; 2
  leans on 'qt_lcDebugPlugins()', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken; 2 leans on
  'QLibraryPrivate.

  What to expect
  --------------

  - The C++ QLibraryPrivate is created at the first use, not by
    'QLibraryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLibraryPrivate.
  - Each name of Qt's QLibraryPrivate that has no cute function yet,
    'findOrCreate', 'isPlugin', 'load', 'loadPlugin', 'load_sys',
    'pluginInstance', 'release', 'resolve', 'resolve_sys', 'setLoadHints',
    'suffixes_sys', 'unload', 'unload_sys', 'updatePluginState', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLibraryPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class UnloadFlag(CuteNum):
    """
    The enum 'QLibraryPrivate::UnloadFlag' of Qt, with the 2 names Qt gives
    in it.
    """

    UnloadSys = Kee[int](0)
    NoUnloadSys = Kee[int](1)

  #  The classes Qt writes inside QLibraryPrivate, each a class in here as in
  #  C++.

  class Deleter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLibraryPrivate::Deleter: a plain Python object
    standing in front of one C++ QLibraryPrivate::Deleter.

    C++ hands a QLibraryPrivate::Deleter around as a copy, so every C++
    QLibraryPrivate::Deleter behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QLibraryPrivate::Deleter yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLibraryPrivate::Deleter::~Deleter()': the destructor: Python
      removes its C++ QLibraryPrivate::Deleter by it, and has no other use
      for it.

    What has no ritual
    ------------------

    1 of the 2 functions Qt declares: 1 leans on 'QLibraryPrivate.

    What to expect
    --------------

    - The C++ QLibraryPrivate::Deleter is created at the first use, not by
      'QLibraryPrivate::Deleter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLibraryPrivate::Deleter back gives a copy the
      ritual made for Python, in a new cute QLibraryPrivate::Deleter.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLibraryPrivate::Deleter'

    #  Qt's '~QLibraryPrivate::Deleter()'. Naming it makes this a value
    #  class: Python owns every C++ QLibraryPrivate::Deleter behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QLibraryPrivate7DeleterD1Ev'

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
  def prefix_sys() -> str:
    """
    Calls Qt's 'QStringView QLibraryPrivate::prefix_sys()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryprivate.html#prefix_sys

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QLibraryPrivate::prefix_sys()
    return Rituals.call('ritual_ZN15QLibraryPrivate10prefix_sysEv')

  @staticmethod
  @overload(QLibrary)
  @overload(NoneType)
  def get(lib: Optional[QLibrary]) -> Optional[QLibraryPrivate]:
    """
    Calls Qt's 'QLibraryPrivate *QLibraryPrivate::get(QLibrary *lib)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryprivate.html#get

    Parameters
    ----------

    lib : Optional[QLibrary]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLibraryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLibraryPrivate *QLibraryPrivate::get(QLibrary *lib)
    address = Rituals.call(
        'ritual_ZN15QLibraryPrivate3getEP8QLibrary',
        CuteMixin._addressOf(lib),
    )
    return QLibraryPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLibraryPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def loadHints(self) -> QLibrary.LoadHints:
    """
    Calls Qt's 'QLibrary::LoadHints QLibraryPrivate::loadHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryprivate.html#loadHints

    Returns
    -------

    QLibrary.LoadHints
      The value standing for the combination Qt gave back.
    """
    #  QLibrary::LoadHints QLibraryPrivate::loadHints() const
    return QLibrary.LoadHints(self.uglySide.call(
        'ritual_ZNK15QLibraryPrivate9loadHintsEv',
    ))

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

  @overload(str, str, QLibrary.LoadHints)
  def __init__(
      self,
      canonicalFileName: str,
      version: str,
      loadHints: QLibrary.LoadHints,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLibraryPrivate::QLibraryPrivate(const
    QString &canonicalFileName, const QString &version, QLibrary::LoadHints
    loadHints)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryprivate.html#QLibraryPrivate

    Parameters
    ----------

    canonicalFileName : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.

    loadHints : QLibrary.LoadHints
      Passed on as its number.
    """
    #  QLibraryPrivate::QLibraryPrivate(const QString &canonicalFileName,
    #      const QString &version, QLibrary::LoadHints loadHints)
    self._noteCreation(QLibraryPrivate, lambda: Rituals.call(
        'ritual_ZN15QLibraryPrivateC1ERK7QStringS2_6QFlagsIN8QLibrary8LoadH'
        'intEE',
        canonicalFileName, version, loadHints.value,
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

  @overload(QLibrary.LoadHints)
  def mergeLoadHints(self, loadHints: QLibrary.LoadHints) -> None:
    """
    Calls Qt's 'void QLibraryPrivate::mergeLoadHints(QLibrary::LoadHints
    loadHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryprivate.html#mergeLoadHints

    Parameters
    ----------

    loadHints : QLibrary.LoadHints
      Passed on as its number.
    """
    #  void QLibraryPrivate::mergeLoadHints(QLibrary::LoadHints loadHints)
    self.uglySide.call(
        'ritual_ZN15QLibraryPrivate14mergeLoadHintsE6QFlagsIN8QLibrary8Load'
        'HintEE',
        loadHints.value,
    )

  @staticmethod
  def findOrCreate(*__, **_) -> Never:
    """
    Qt's 'QLibraryPrivate *QLibraryPrivate::findOrCreate(const QString
    &fileName, const QString &version, QLibrary::LoadHints loadHints)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: incomplete type 'QLibraryStore' named in nested name
    specifier.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.findOrCreate' has no cute function yet. Qt's "
        "'QLibraryPrivate *QLibraryPrivate::findOrCreate(const QString "
        "&fileName, const QString &version, QLibrary::LoadHints "
        "loadHints)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: incomplete type "
        "'QLibraryStore' named in nested name specifier.")

  @staticmethod
  def isPlugin(*__, **_) -> Never:
    """
    Qt's 'bool QLibraryPrivate::isPlugin()': leans on
    'QLibraryPrivate::updatePluginState()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.isPlugin' has no cute function yet. Qt's 'bool "
        "QLibraryPrivate::isPlugin()': leans on "
        "'QLibraryPrivate::updatePluginState()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'bool QLibraryPrivate::load()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QLibraryPrivate_load_entry'.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.load' has no cute function yet. Qt's 'bool "
        "QLibraryPrivate::load()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QLibraryPrivate_load_entry'.")

  @staticmethod
  def loadPlugin(*__, **_) -> Never:
    """
    Qt's 'QtPluginInstanceFunction QLibraryPrivate::loadPlugin()': leans on
    'qt_lcDebugPlugins()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.loadPlugin' has no cute function yet. Qt's "
        "'QtPluginInstanceFunction QLibraryPrivate::loadPlugin()': leans on "
        "'qt_lcDebugPlugins()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def load_sys(*__, **_) -> Never:
    """
    Qt's 'bool QLibraryPrivate::load_sys()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.load_sys' has no cute function yet. Qt's 'bool "
        "QLibraryPrivate::load_sys()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def pluginInstance(*__, **_) -> Never:
    """
    Qt's 'QObject *QLibraryPrivate::pluginInstance()': leans on
    'qt_lcDebugPlugins()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.pluginInstance' has no cute function yet. Qt's "
        "'QObject *QLibraryPrivate::pluginInstance()': leans on "
        "'qt_lcDebugPlugins()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'void QLibraryPrivate::release()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    incomplete type 'QLibraryStore' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.release' has no cute function yet. Qt's 'void "
        "QLibraryPrivate::release()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "incomplete type 'QLibraryStore' named in nested name specifier.")

  @staticmethod
  def resolve(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer QLibraryPrivate::resolve(const char *a0)': leans
    on 'QLibraryPrivate::resolve_sys(char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.resolve' has no cute function yet. Qt's "
        "'QFunctionPointer QLibraryPrivate::resolve(const char *a0)': leans "
        "on 'QLibraryPrivate::resolve_sys(char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def resolve_sys(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer QLibraryPrivate::resolve_sys(const char *a0)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.resolve_sys' has no cute function yet. Qt's "
        "'QFunctionPointer QLibraryPrivate::resolve_sys(const char *a0)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setLoadHints(*__, **_) -> Never:
    """
    Qt's 'void QLibraryPrivate::setLoadHints(QLibrary::LoadHints lh)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qt_library_mutex'.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.setLoadHints' has no cute function yet. Qt's "
        "'void QLibraryPrivate::setLoadHints(QLibrary::LoadHints lh)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_library_mutex'.")

  @staticmethod
  def suffixes_sys(*__, **_) -> Never:
    """
    Qt's 'QStringList QLibraryPrivate::suffixes_sys(const QString
    &fullVersion)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.suffixes_sys' has no cute function yet. Qt's "
        "'QStringList QLibraryPrivate::suffixes_sys(const QString "
        "&fullVersion)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def unload(*__, **_) -> Never:
    """
    Qt's 'bool QLibraryPrivate::unload(UnloadFlag flag)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'lcDebugLibrary'.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.unload' has no cute function yet. Qt's 'bool "
        "QLibraryPrivate::unload(UnloadFlag flag)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'lcDebugLibrary'.")

  @staticmethod
  def unload_sys(*__, **_) -> Never:
    """
    Qt's 'bool QLibraryPrivate::unload_sys()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.unload_sys' has no cute function yet. Qt's 'bool "
        "QLibraryPrivate::unload_sys()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def updatePluginState(*__, **_) -> Never:
    """
    Qt's 'void QLibraryPrivate::updatePluginState()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'findPatternUnloaded'.
    """
    raise NotImplementedError(
        "'QLibraryPrivate.updatePluginState' has no cute function yet. Qt's "
        "'void QLibraryPrivate::updatePluginState()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'findPatternUnloaded'.")
