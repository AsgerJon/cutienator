"""
LoadHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means LoadHelper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QQmlPrivate, QQmlTypeLoader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlComponentPrivate, QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponentPrivate = WAIT['QQmlComponentPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LoadHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's LoadHelper: a plain Python object standing in front
  of one C++ LoadHelper.

  What exists
  -----------

  Every function of Qt's LoadHelper that has a ritual and that Python can
  call so far, 9 names in all: 'type', 'mode', 'resolveTypeResult',
  'registerCallback', 'unregisterCallback', 'done', 'completed',
  'initializeFromCachedUnit', 'couldFindModule'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 leans on 'lcQmlImport()', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ LoadHelper is created at the first use, not by 'LoadHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LoadHelper.
  - Each name of Qt's LoadHelper that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside LoadHelper, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ResolveTypeResult(CuteNum, scoped=True):
    """
    The enum 'LoadHelper::ResolveTypeResult' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoSuchModule = Kee[int](0)
    ModuleFound = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LoadHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QQmlType:
    """
    Calls Qt's 'QQmlType LoadHelper::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#type

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType LoadHelper::type() const
    address = self.uglySide.call('ritual_ZNK10LoadHelper4typeEv')
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def mode(self) -> QQmlTypeLoader.Mode:
    """
    Calls Qt's 'QQmlTypeLoader::Mode LoadHelper::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#mode

    Returns
    -------

    QQmlTypeLoader.Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlTypeLoader.Mode(number)' gives.
    """
    #  QQmlTypeLoader::Mode LoadHelper::mode() const
    return QQmlTypeLoader.Mode(self.uglySide.call(
        'ritual_ZNK10LoadHelper4modeEv',
    ))

  def resolveTypeResult(self) -> ResolveTypeResult:
    """
    Calls Qt's 'ResolveTypeResult LoadHelper::resolveTypeResult() const'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#resolveTypeResult

    Returns
    -------

    ResolveTypeResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ResolveTypeResult(number)' gives.
    """
    #  ResolveTypeResult LoadHelper::resolveTypeResult() const
    return LoadHelper.ResolveTypeResult(self.uglySide.call(
        'ritual_ZNK10LoadHelper17resolveTypeResultEv',
    ))

  def couldFindModule(self) -> bool:
    """
    Calls Qt's 'bool LoadHelper::couldFindModule() const'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#couldFindModule
    """
    #  bool LoadHelper::couldFindModule() const
    return self.uglySide.call('ritual_ZNK10LoadHelper15couldFindModuleEv')

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
    Qt's 'LoadHelper::LoadHelper(QQmlTypeLoader *loader, QAnyStringView uri,
    QAnyStringView typeName, QQmlTypeLoader::Mode mode)': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'LoadHelper.__init__' has no cute function yet. Qt's "
        "'LoadHelper::LoadHelper(QQmlTypeLoader *loader, QAnyStringView "
        "uri, QAnyStringView typeName, QQmlTypeLoader::Mode mode)': leans "
        "on 'lcQmlImport()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QQmlComponentPrivate)
  @overload(NoneType)
  def registerCallback(
      self,
      callback: Optional[QQmlComponentPrivate],
  ) -> None:
    """
    Calls Qt's 'void LoadHelper::registerCallback(QQmlComponentPrivate
    *callback)'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#registerCallback

    Parameters
    ----------

    callback : Optional[QQmlComponentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LoadHelper::registerCallback(QQmlComponentPrivate *callback)
    self.uglySide.call(
        'ritual_ZN10LoadHelper16registerCallbackEP20QQmlComponentPrivate',
        self._addressOf(callback),
    )

  @overload(QQmlComponentPrivate)
  @overload(NoneType)
  def unregisterCallback(
      self,
      callback: Optional[QQmlComponentPrivate],
  ) -> None:
    """
    Calls Qt's 'void LoadHelper::unregisterCallback(QQmlComponentPrivate
    *callback)'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#unregisterCallback

    Parameters
    ----------

    callback : Optional[QQmlComponentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LoadHelper::unregisterCallback(QQmlComponentPrivate *callback)
    self.uglySide.call(
        'ritual_ZN10LoadHelper18unregisterCallbackEP20QQmlComponentPrivate',
        self._addressOf(callback),
    )

  def done(self) -> None:
    """
    Calls Qt's 'void LoadHelper::done()'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#done
    """
    #  void LoadHelper::done()
    self.uglySide.call('ritual_ZN10LoadHelper4doneEv')

  def completed(self) -> None:
    """
    Calls Qt's 'void LoadHelper::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/loadhelper.html#completed
    """
    #  void LoadHelper::completed()
    self.uglySide.call('ritual_ZN10LoadHelper9completedEv')

  @overload(WAIT['QQmlPrivate.CachedQmlUnit'])
  @overload(NoneType)
  def initializeFromCachedUnit(
      self,
      a0: Optional[QQmlPrivate.CachedQmlUnit],
  ) -> None:
    """
    Calls Qt's 'void LoadHelper::initializeFromCachedUnit(const
    QQmlPrivate::CachedQmlUnit *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/loadhelper.html#initializeFromCachedUnit

    Parameters
    ----------

    a0 : Optional[QQmlPrivate.CachedQmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LoadHelper::initializeFromCachedUnit(const
    #      QQmlPrivate::CachedQmlUnit *a0)
    self.uglySide.call(
        'ritual_ZN10LoadHelper24initializeFromCachedUnitEPKN11QQmlPrivate13'
        'CachedQmlUnitE',
        self._addressOf(a0),
    )
