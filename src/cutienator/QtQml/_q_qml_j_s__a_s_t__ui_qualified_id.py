"""
QQmlJS::AST::UiQualifiedId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiQualifiedId to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class UiQualifiedId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiQualifiedId: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiQualifiedId.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiQualifiedId that has a ritual and
  that Python can call so far, 5 names in all: 'finish',
  'firstSourceLocation', 'lastSourceLocation', 'lastOwnSourceLocation',
  'toString'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiQualifiedId::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiQualifiedId is created at the first use, not by
    'QQmlJS::AST::UiQualifiedId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiQualifiedId.
  - Each name of Qt's QQmlJS::AST::UiQualifiedId that has no cute function
    yet, 'accept0', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::UiQualifiedId'

  #  A C++ QQmlJS::AST::UiQualifiedId Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiQualifiedId'

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
    QQmlJS::AST::UiQualifiedId::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiQualifiedId::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST13UiQualifiedId19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST13UiQualifiedId19firstSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiQualifiedId::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiQualifiedId::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST13UiQualifiedId18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST13UiQualifiedId18lastSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastOwnSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiQualifiedId::lastOwnSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiQualifiedId::lastOwnSourceLocation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST13UiQualifiedId21lastOwnSourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  @overload()
  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::AST::UiQualifiedId::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::AST::UiQualifiedId::toString() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST13UiQualifiedId8toStringEv',
    )

  @overload(QString)
  @overload(NoneType)
  def toString(self, out: Optional[QString]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::UiQualifiedId::toString(QString *out)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#toString

    Parameters
    ----------

    out : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::UiQualifiedId::toString(QString *out) const
    self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST13UiQualifiedId8toStringEP7QString',
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

  @overload(WAIT['QQmlJS.MemoryPool'], str)
  @overload(NoneType, str)
  def __init__(self, pool: Optional[QQmlJS.MemoryPool], name: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiQualifiedId::UiQualifiedId(QStringView name)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#UiQualifiedId

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiQualifiedId::UiQualifiedId(QStringView name)
    self._noteCreation(UiQualifiedId, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST13UiQualifiedIdC1E11QStringView',
        self._addressOf(pool), name,
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, str)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str)
  @overload(NoneType, THIS, str)
  @overload(NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiQualifiedId],
      name: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiQualifiedId::UiQualifiedId(UiQualifiedId *previous,
    QStringView name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#UiQualifiedId

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiQualifiedId::UiQualifiedId(UiQualifiedId *previous,
    #      QStringView name)
    self._noteCreation(UiQualifiedId, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST13UiQualifiedIdC1EPS1_11QStringView',
        self._addressOf(pool), self._addressOf(previous), name,
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

  def finish(self) -> Optional[UiQualifiedId]:
    """
    Calls Qt's 'UiQualifiedId *QQmlJS::AST::UiQualifiedId::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiqualifiedid.html#finish

    Returns
    -------

    Optional[UiQualifiedId]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  UiQualifiedId *QQmlJS::AST::UiQualifiedId::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST13UiQualifiedId6finishEv',
    )
    return UiQualifiedId._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiQualifiedId::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiQualifiedId.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::UiQualifiedId::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
