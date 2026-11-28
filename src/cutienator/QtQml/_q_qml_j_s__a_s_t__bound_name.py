"""
QQmlJS::AST::BoundName binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::BoundName to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoundName(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::BoundName: a plain Python object
  standing in front of one C++ QQmlJS::AST::BoundName.

  C++ hands a QQmlJS::AST::BoundName around as a copy, so every C++
  QQmlJS::AST::BoundName behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::BoundName that has a ritual and that
  Python can call so far, 1 name in all: 'isInjected'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::BoundName::~BoundName()': the destructor: Python
    removes its C++ QQmlJS::AST::BoundName by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QQmlJS::AST::BoundName is created at the first use, not by
    'QQmlJS::AST::BoundName(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::AST::BoundName back gives a copy the ritual
    made for Python, in a new cute QQmlJS::AST::BoundName.
  """

  #  The enums Qt writes inside QQmlJS::AST::BoundName, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QQmlJS::AST::BoundName::Type' of Qt, with the 2 names Qt gives
    in it.
    """

    Declared = Kee[int](0)
    Injected = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::BoundName'

  #  Qt's '~QQmlJS::AST::BoundName()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJS::AST::BoundName behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS3AST9BoundNameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInjected(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::BoundName::isInjected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-boundname.html#isInjected
    """
    #  bool QQmlJS::AST::BoundName::isInjected() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST9BoundName10isInjectedEv',
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

  @overload(
      str, WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(str, WAIT['QQmlJS.SourceLocation'], NoneType)
  @overload(
      str, WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.AST.TypeAnnotation'],
      Type,
  )
  @overload(str, WAIT['QQmlJS.SourceLocation'], NoneType, Type)
  def __init__(
      self,
      id: str,
      location: QQmlJS.SourceLocation,
      typeAnnotation: Optional[QQmlJS.AST.TypeAnnotation],
      type: Type = Type.Declared,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::AST::BoundName::BoundName(const
    QString &id, const QQmlJS::SourceLocation &location, TypeAnnotation
    *typeAnnotation, Type type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-boundname.html#BoundName

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    typeAnnotation : Optional[QQmlJS.AST.TypeAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.Declared.
    """
    #  QQmlJS::AST::BoundName::BoundName(const QString &id, const
    #      QQmlJS::SourceLocation &location, TypeAnnotation *typeAnnotation,
    #      Type type)
    self._noteCreation(BoundName, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST9BoundNameC1ERK7QStringRKNS_14SourceLocationEP'
        'NS0_14TypeAnnotationENS1_4TypeE',
        id, self._valueOf(location), self._addressOf(typeAnnotation),
        type.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::AST::BoundName::BoundName()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-boundname.html#BoundName
    """
    #  QQmlJS::AST::BoundName::BoundName()
    self._noteCreation(BoundName, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST9BoundNameC1Ev',
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
