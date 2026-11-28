"""
qdesigner_internal::CETypes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::CETypes to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CETypes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::CETypes: a plain Python object
  standing in front of one C++ qdesigner_internal::CETypes.

  C++ hands a qdesigner_internal::CETypes around as a copy, so every C++
  qdesigner_internal::CETypes behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's qdesigner_internal::CETypes yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::CETypes::~CETypes()': the destructor: Python
    removes its C++ qdesigner_internal::CETypes by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::CETypes is created at the first use, not by
    'qdesigner_internal::CETypes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::CETypes back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::CETypes.
  """

  #  The enums Qt writes inside qdesigner_internal::CETypes, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class LineDir(CuteNum):
    """
    The enum 'qdesigner_internal::CETypes::LineDir' of Qt, with the 4 names
    Qt gives in it.
    """

    UpDir = Kee[int](0)
    DownDir = Kee[int](1)
    RightDir = Kee[int](2)
    LeftDir = Kee[int](3)

  #  The classes Qt writes inside qdesigner_internal::CETypes, each a class
  #  in here as in C++.

  class EndPoint(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's qdesigner_internal::CETypes::EndPoint: a plain
    Python object standing in front of one C++
    qdesigner_internal::CETypes::EndPoint.

    C++ hands a qdesigner_internal::CETypes::EndPoint around as a copy, so
    every C++ qdesigner_internal::CETypes::EndPoint behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's qdesigner_internal::CETypes::EndPoint that has a
    ritual and that Python can call so far, 3 names in all: 'isNull',
    '__eq__', '__ne__'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'qdesigner_internal::CETypes::EndPoint::~EndPoint()': the
      destructor: Python removes its C++
      qdesigner_internal::CETypes::EndPoint by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ qdesigner_internal::CETypes::EndPoint is created at the first
      use, not by 'qdesigner_internal::CETypes::EndPoint(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a qdesigner_internal::CETypes::EndPoint back gives a
      copy the ritual made for Python, in a new cute
      qdesigner_internal::CETypes::EndPoint.
    """

    #  The enums Qt writes inside qdesigner_internal::CETypes::EndPoint, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Type(CuteNum):
      """
      The enum 'qdesigner_internal::CETypes::EndPoint::Type' of Qt, with the
      2 names Qt gives in it.
      """

      Source = Kee[int](0)
      Target = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'qdesigner_internal::CETypes::EndPoint'

    #  Qt's '~qdesigner_internal::CETypes::EndPoint()'. Naming it makes this
    #  a value class: Python owns every C++
    #  qdesigner_internal::CETypes::EndPoint behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN18qdesigner_internal7CETypes8EndPointD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool qdesigner_internal::CETypes::EndPoint::isNull()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-cetypes-endpoint.html#isNull
      """
      #  bool qdesigner_internal::CETypes::EndPoint::isNull() const
      return self.uglySide.call(
          'ritual_ZNK18qdesigner_internal7CETypes8EndPoint6isNullEv',
      )

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
    def __eq__(self, other: CETypes.EndPoint) -> bool:
      """
      Calls Qt's 'bool
      qdesigner_internal::CETypes::EndPoint::operator==(const EndPoint
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-cetypes-endpoint.html

      Parameters
      ----------

      other : CETypes.EndPoint
        Passed on as a value: Qt reads the C++
        qdesigner_internal::CETypes::EndPoint, which stays Python's own.
      """
      #  bool qdesigner_internal::CETypes::EndPoint::operator==(const
      #      EndPoint &other) const
      return self.uglySide.call(
          'ritual_ZNK18qdesigner_internal7CETypes8EndPointeqERKS1_',
          self._valueOf(other),
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
    def __ne__(self, other: CETypes.EndPoint) -> bool:
      """
      Calls Qt's 'bool
      qdesigner_internal::CETypes::EndPoint::operator!=(const EndPoint
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-cetypes-endpoint.html

      Parameters
      ----------

      other : CETypes.EndPoint
        Passed on as a value: Qt reads the C++
        qdesigner_internal::CETypes::EndPoint, which stays Python's own.
      """
      #  bool qdesigner_internal::CETypes::EndPoint::operator!=(const
      #      EndPoint &other) const
      return self.uglySide.call(
          'ritual_ZNK18qdesigner_internal7CETypes8EndPointneERKS1_',
          self._valueOf(other),
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
    @overload(WAIT['qdesigner_internal.Connection'])
    @overload(NoneType)
    @overload(WAIT['qdesigner_internal.Connection'], Type)
    @overload(NoneType, Type)
    def __init__(
        self,
        _con: Optional[qdesigner_internal.Connection] = None,
        _type: Type = Type.Source,
    ) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::CETypes::EndPoint::EndPoint(Connection *_con, Type
      _type)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-cetypes-endpoint.html

      Parameters
      ----------

      _con : Optional[qdesigner_internal.Connection]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      _type : Type
        Passed on as its number. May be left out, as in Qt: it is then
        Type.Source.
      """
      #  qdesigner_internal::CETypes::EndPoint::EndPoint(Connection *_con,
      #      Type _type)
      self._noteCreation(CETypes.EndPoint, lambda: Rituals.call(
          'ritual_ZN18qdesigner_internal7CETypes8EndPointC1EPNS_10Connectio'
          'nENS1_4TypeE',
          self._addressOf(_con), _type.value,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::CETypes'

  #  Qt's '~qdesigner_internal::CETypes()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::CETypes behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal7CETypesD1Ev'

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
