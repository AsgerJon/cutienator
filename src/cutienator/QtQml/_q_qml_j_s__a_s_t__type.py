"""
QQmlJS::AST::Type binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::Type to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Type(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::Type: a plain Python object standing in
  front of one C++ QQmlJS::AST::Type.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::Type that has a ritual and that Python
  can call so far, 3 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'toString'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::Type::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::Type is created at the first use, not by
    'QQmlJS::AST::Type(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::Type.
  - Each name of Qt's QQmlJS::AST::Type that has no cute function yet,
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
  __qt_class__ = 'QQmlJS::AST::Type'

  #  A C++ QQmlJS::AST::Type Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_Type'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::Type::firstSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-type.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::Type::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST4Type19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST4Type19firstSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::Type::lastSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-type.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::Type::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST4Type18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST4Type18lastSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  @overload()
  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::AST::Type::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-type.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::AST::Type::toString() const
    return self.uglySide.call('ritual_ZNK6QQmlJS3AST4Type8toStringEv')

  @overload(QString)
  @overload(NoneType)
  def toString(self, out: Optional[QString]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Type::toString(QString *out) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-type.html#toString

    Parameters
    ----------

    out : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Type::toString(QString *out) const
    self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST4Type8toStringEP7QString',
        self._addressOf(out),
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.UiQualifiedId'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'], THIS,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'], NoneType,
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, THIS)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.UiQualifiedId'], THIS)
  @overload(NoneType, WAIT['QQmlJS.AST.UiQualifiedId'], NoneType)
  @overload(NoneType, NoneType, THIS)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      typeId: Optional[QQmlJS.AST.UiQualifiedId],
      typeArgument: Optional[Type] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::AST::Type::Type(UiQualifiedId
    *typeId, Type *typeArgument)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-type.html#Type

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeId : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeArgument : Optional[Type]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlJS::AST::Type::Type(UiQualifiedId *typeId, Type *typeArgument)
    self._noteCreation(Type, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST4TypeC1EPNS0_13UiQualifiedIdEPS1_',
        self._addressOf(pool), self._addressOf(typeId),
        self._addressOf(typeArgument),
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
    Qt's 'void QQmlJS::AST::Type::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.Type.accept0' has no cute function yet. Qt's 'void "
        "QQmlJS::AST::Type::accept0(BaseVisitor *visitor)': names "
        "'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
