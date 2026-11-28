"""
QQmlJS::AST::UiPragma binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiPragma to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UiPragma(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiPragma: a plain Python object standing
  in front of one C++ QQmlJS::AST::UiPragma.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiPragma that has a ritual and that
  Python can call so far, 2 names in all: 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiPragma::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiPragma is created at the first use, not by
    'QQmlJS::AST::UiPragma(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiPragma.
  - Each name of Qt's QQmlJS::AST::UiPragma that has no cute function yet,
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
  __qt_class__ = 'QQmlJS::AST::UiPragma'

  #  A C++ QQmlJS::AST::UiPragma Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiPragma'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPragma::firstSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragma.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPragma::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST8UiPragma19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST8UiPragma19firstSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPragma::lastSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragma.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPragma::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST8UiPragma18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST8UiPragma18lastSourceLocationEv'
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

  @overload(WAIT['QQmlJS.MemoryPool'], str)
  @overload(NoneType, str)
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.UiPragmaValueList'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], str, NoneType)
  @overload(NoneType, str, WAIT['QQmlJS.AST.UiPragmaValueList'])
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      name: str,
      values: Optional[QQmlJS.AST.UiPragmaValueList] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiPragma::UiPragma(QStringView name, UiPragmaValueList
    *values)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-uipragma.html#UiPragma

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    values : Optional[QQmlJS.AST.UiPragmaValueList]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlJS::AST::UiPragma::UiPragma(QStringView name, UiPragmaValueList
    #      *values)
    self._noteCreation(UiPragma, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST8UiPragmaC1E11QStringViewPNS0_17UiPragmaValueL'
        'istE',
        self._addressOf(pool), name, self._addressOf(values),
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

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiPragma::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiPragma.accept0' has no cute function yet. Qt's 'void "
        "QQmlJS::AST::UiPragma::accept0(BaseVisitor *visitor)': names "
        "'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
