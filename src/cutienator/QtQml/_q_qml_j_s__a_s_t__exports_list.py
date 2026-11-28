"""
QQmlJS::AST::ExportsList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::ExportsList to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExportsList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::ExportsList: a plain Python object
  standing in front of one C++ QQmlJS::AST::ExportsList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::ExportsList that has a ritual and that
  Python can call so far, 3 names in all: 'finish', 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::ExportsList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::ExportsList is created at the first use, not by
    'QQmlJS::AST::ExportsList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::ExportsList.
  - Each name of Qt's QQmlJS::AST::ExportsList that has no cute function yet,
    'accept0', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::ExportsList'

  #  A C++ QQmlJS::AST::ExportsList Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_ExportsList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ExportsList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportslist.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ExportsList::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST11ExportsList19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST11ExportsList19firstSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::ExportsList::lastSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportslist.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ExportsList::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST11ExportsList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST11ExportsList18lastSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.ExportSpecifier'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.ExportSpecifier'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      exportSpecifier: Optional[QQmlJS.AST.ExportSpecifier],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ExportsList::ExportsList(ExportSpecifier
    *exportSpecifier)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportslist.html#ExportsList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    exportSpecifier : Optional[QQmlJS.AST.ExportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ExportsList::ExportsList(ExportSpecifier
    #      *exportSpecifier)
    self._noteCreation(ExportsList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST11ExportsListC1EPNS0_15ExportSpecifierE',
        self._addressOf(pool), self._addressOf(exportSpecifier),
    ))

  @overload(
      WAIT['QQmlJS.MemoryPool'], THIS, WAIT['QQmlJS.AST.ExportSpecifier'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], THIS, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType,
      WAIT['QQmlJS.AST.ExportSpecifier'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(NoneType, THIS, WAIT['QQmlJS.AST.ExportSpecifier'])
  @overload(NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.ExportSpecifier'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[ExportsList],
      exportSpecifier: Optional[QQmlJS.AST.ExportSpecifier],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ExportsList::ExportsList(ExportsList *previous,
    ExportSpecifier *exportSpecifier)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportslist.html#ExportsList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[ExportsList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    exportSpecifier : Optional[QQmlJS.AST.ExportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ExportsList::ExportsList(ExportsList *previous,
    #      ExportSpecifier *exportSpecifier)
    self._noteCreation(ExportsList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST11ExportsListC1EPS1_PNS0_15ExportSpecifierE',
        self._addressOf(pool), self._addressOf(previous),
        self._addressOf(exportSpecifier),
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

  def finish(self) -> Optional[ExportsList]:
    """
    Calls Qt's 'ExportsList *QQmlJS::AST::ExportsList::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-exportslist.html#finish

    Returns
    -------

    Optional[ExportsList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExportsList *QQmlJS::AST::ExportsList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST11ExportsList6finishEv',
    )
    return ExportsList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::ExportsList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ExportsList.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::ExportsList::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
