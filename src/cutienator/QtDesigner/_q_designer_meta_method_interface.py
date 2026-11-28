"""
QDesignerMetaMethodInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMetaMethodInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDesignerMetaMethodInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMetaMethodInterface: a plain Python object
  standing in front of one C++ QDesignerMetaMethodInterface.

  What exists
  -----------

  Every function of Qt's QDesignerMetaMethodInterface that has a ritual and
  that Python can call so far, 8 names in all: 'access', 'methodType',
  'parameterNames', 'parameterTypes', 'signature', 'normalizedSignature',
  'tag', 'typeName'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerMetaMethodInterface::~QDesignerMetaMethodInterface()': the
    destructor: Python never removes a C++ QDesignerMetaMethodInterface.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerMetaMethodInterface is created at the first use, not by
    'QDesignerMetaMethodInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaMethodInterface.
  - Each name of Qt's QDesignerMetaMethodInterface that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDesignerMetaMethodInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Access(CuteNum):
    """
    The enum 'QDesignerMetaMethodInterface::Access' of Qt, with the 3 names
    Qt gives in it.
    """

    Private = Kee[int](0)
    Protected = Kee[int](1)
    Public = Kee[int](2)

  class MethodType(CuteNum):
    """
    The enum 'QDesignerMetaMethodInterface::MethodType' of Qt, with the 4
    names Qt gives in it.
    """

    Method = Kee[int](0)
    Signal = Kee[int](1)
    Slot = Kee[int](2)
    Constructor = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaMethodInterface'

  #  A C++ QDesignerMetaMethodInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaMethodInterface'

  #  The functions Qt calls itself that QDesignerMetaMethodInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parameterNames': (
          'QStringList QDesignerMetaMethodInterface::parameterNames() const',
      ),
      'parameterTypes': (
          'QStringList QDesignerMetaMethodInterface::parameterTypes() const',
      ),
  }

  #  The functions Qt calls itself that QDesignerMetaMethodInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'access': (
          ('_ZNK28QDesignerMetaMethodInterface6accessEv',
           ('int', 'enum', 'QtDesigner:QDesignerMetaMethodInterface.Access'),
           ()),
      ),
      'methodType': (
          ('_ZNK28QDesignerMetaMethodInterface10methodTypeEv',
           ('int', 'enum',
            'QtDesigner:QDesignerMetaMethodInterface.MethodType'),
           ()),
      ),
      'signature': (
          ('_ZNK28QDesignerMetaMethodInterface9signatureEv',
           ('address', 'text', ''),
           ()),
      ),
      'normalizedSignature': (
          ('_ZNK28QDesignerMetaMethodInterface19normalizedSignatureEv',
           ('address', 'text', ''),
           ()),
      ),
      'tag': (
          ('_ZNK28QDesignerMetaMethodInterface3tagEv',
           ('address', 'text', ''),
           ()),
      ),
      'typeName': (
          ('_ZNK28QDesignerMetaMethodInterface8typeNameEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def access(self) -> Access:
    """
    Calls Qt's 'Access QDesignerMetaMethodInterface::access() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#access

    Returns
    -------

    Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Access(number)' gives.
    """
    #  Access QDesignerMetaMethodInterface::access() const
    return QDesignerMetaMethodInterface.Access(self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface6accessEv',
    ))

  def methodType(self) -> MethodType:
    """
    Calls Qt's 'MethodType QDesignerMetaMethodInterface::methodType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#methodType

    Returns
    -------

    MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MethodType(number)'
      gives.
    """
    #  MethodType QDesignerMetaMethodInterface::methodType() const
    return QDesignerMetaMethodInterface.MethodType(self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface10methodTypeEv',
    ))

  def parameterNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerMetaMethodInterface::parameterNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#parameterNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerMetaMethodInterface::parameterNames() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface14parameterNamesEv',
    )
    return QStringList._cuteOwning(address)

  def parameterTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerMetaMethodInterface::parameterTypes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#parameterTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerMetaMethodInterface::parameterTypes() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface14parameterTypesEv',
    )
    return QStringList._cuteOwning(address)

  def signature(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaMethodInterface::signature() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#signature

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaMethodInterface::signature() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface9signatureEv',
    )

  def normalizedSignature(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaMethodInterface::normalizedSignature()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaMethodInterface::normalizedSignature() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface19normalizedSignatureEv',
    )

  def tag(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaMethodInterface::tag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#tag

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaMethodInterface::tag() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface3tagEv',
    )

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaMethodInterface::typeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetamethodinterface.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaMethodInterface::typeName() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaMethodInterface8typeNameEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDesignerMetaMethodInterface::QDesignerMetaMethodInterface()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerMetaMethodInterface.__init__' has no cute function yet. "
        "Qt's "
        "'QDesignerMetaMethodInterface::QDesignerMetaMethodInterface()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
