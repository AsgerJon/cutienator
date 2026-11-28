"""
QQmlCompilePass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlCompilePass to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlTypeCompiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlTypeCompiler = WAIT['QQmlTypeCompiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCompilePass(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlCompilePass: a plain Python object standing in
  front of one C++ QQmlCompilePass.

  C++ hands a QQmlCompilePass around as a copy, so every C++ QQmlCompilePass
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlCompilePass that has a ritual and that Python
  can call so far, 3 names in all: 'stringAt', 'recordError', 'resolvedType'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlCompilePass::~QQmlCompilePass()': the destructor: Python
    removes its C++ QQmlCompilePass by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlCompilePass is created at the first use, not by
    'QQmlCompilePass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlCompilePass back gives a copy the ritual made for
    Python, in a new cute QQmlCompilePass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCompilePass'

  #  Qt's '~QQmlCompilePass()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlCompilePass behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlCompilePassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def stringAt(self, idx: int) -> str:
    """
    Calls Qt's 'QString QQmlCompilePass::stringAt(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcompilepass.html#stringAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlCompilePass::stringAt(int idx) const
    return self.uglySide.call('ritual_ZNK15QQmlCompilePass8stringAtEi', idx)

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'QV4::ResolvedTypeReference *QQmlCompilePass::resolvedType(int
    id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcompilepass.html#resolvedType

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.ResolvedTypeReference]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ResolvedTypeReference *QQmlCompilePass::resolvedType(int id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlCompilePass12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

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

  @overload(QQmlTypeCompiler)
  @overload(NoneType)
  def __init__(self, typeCompiler: Optional[QQmlTypeCompiler]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompilepass.html#QQmlCompilePass

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)
    self._noteCreation(QQmlCompilePass, lambda: Rituals.call(
        'ritual_ZN15QQmlCompilePassC1EP16QQmlTypeCompiler',
        self._addressOf(typeCompiler),
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

  @overload(WAIT['QV4.CompiledData.Location'], str)
  def recordError(
      self,
      location: QV4.CompiledData.Location,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlCompilePass::recordError(const
    QV4::CompiledData::Location &location, const QString &description)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcompilepass.html#recordError

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlCompilePass::recordError(const QV4::CompiledData::Location
    #      &location, const QString &description) const
    self.uglySide.call(
        'ritual_ZNK15QQmlCompilePass11recordErrorERKN3QV412CompiledData8Loc'
        'ationERK7QString',
        self._valueOf(location), description,
    )
