"""
QQmlSA::Method binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Method(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::Method: a plain Python object standing in
  front of one C++ QQmlSA::Method.

  C++ hands a QQmlSA::Method around as a copy, so every C++ QQmlSA::Method
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::Method that has a ritual and that Python can
  call so far, 6 names in all: 'd_func', 'methodName', 'sourceLocation',
  'methodType', '__eq__', '__ne__'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const MethodPrivate *QQmlSA::Method::d_func() const': takes in
    Python what 'MethodPrivate *QQmlSA::Method::d_func()' takes.
  - Qt's 'QQmlSA::Method::Method(Method &&a0)': takes a type Python has no
    way to hand over yet.
  - Qt's 'Method &QQmlSA::Method::operator=(const Method &a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'Method &QQmlSA::Method::operator=(Method &&a0)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QQmlSA::Method::~Method()': the destructor: Python removes its C++
    QQmlSA::Method by it, and has no other use for it.
  - Qt's 'bool QQmlSA::Method::operatorEqualsImpl(const Method &a0, const
    Method &a1)': an operator Python has no name for.

  What to expect
  --------------

  - The C++ QQmlSA::Method is created at the first use, not by
    'QQmlSA::Method(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::Method back gives a copy the ritual made for
    Python, in a new cute QQmlSA::Method.
  """

  #  The classes Qt writes inside QQmlSA::Method, each a class in here as in
  #  C++.

  class Methods(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlSA::Method::Methods: a plain Python object
    standing in front of one C++ QQmlSA::Method::Methods.

    C++ hands a QQmlSA::Method::Methods around as a copy, so every C++
    QQmlSA::Method::Methods behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlSA::Method::Methods that has a ritual and that
    Python can call so far, 1 name in all: 'd_func'. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const MethodsPrivate *QQmlSA::Method::Methods::d_func() const':
      takes in Python what 'MethodsPrivate
      *QQmlSA::Method::Methods::d_func()' takes.
    - Qt's 'QQmlSA::Method::Methods::~Methods()': the destructor: Python
      removes its C++ QQmlSA::Method::Methods by it, and has no other use for
      it.
    - Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::begin() const': gives a type Python has no way
      to take yet.
    - Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::end() const': gives a type Python has no way
      to take yet.
    - Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::constBegin() const': gives a type Python has
      no way to take yet.
    - Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::constEnd() const': gives a type Python has no
      way to take yet.

    What to expect
    --------------

    - The C++ QQmlSA::Method::Methods is created at the first use, not by
      'QQmlSA::Method::Methods(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlSA::Method::Methods back gives a copy the
      ritual made for Python, in a new cute QQmlSA::Method::Methods.
    - Each name of Qt's QQmlSA::Method::Methods that has no cute function
      yet, 'begin', 'constBegin', 'constEnd', 'end', holds a function that
      raises 'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlSA::Method::Methods'

    #  Qt's '~QQmlSA::Method::Methods()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlSA::Method::Methods behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN6QQmlSA6Method7MethodsD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlSA::Method::Methods::Methods()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-method-methods.html#Methods
      """
      #  QQmlSA::Method::Methods::Methods()
      self._noteCreation(Method.Methods, lambda: Rituals.call(
          'ritual_ZN6QQmlSA6Method7MethodsC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: Method.Methods) -> None:
      """
      Notes what was given, for Qt's 'QQmlSA::Method::Methods::Methods(const
      Methods &a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-method-methods.html#Methods

      Parameters
      ----------

      a0 : Method.Methods
        Passed on as a value: Qt reads the C++ QQmlSA::Method::Methods, which
        stays Python's own.
      """
      #  QQmlSA::Method::Methods::Methods(const Methods &a0)
      self._noteCreation(Method.Methods, lambda: Rituals.call(
          'ritual_ZN6QQmlSA6Method7MethodsC1ERKS1_', self._valueOf(a0),
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

    def d_func(self) -> Optional[QQmlSA.MethodsPrivate]:
      """
      Calls Qt's 'MethodsPrivate *QQmlSA::Method::Methods::d_func()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-method-methods.html#d_func

      Returns
      -------

      Optional[QQmlSA.MethodsPrivate]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  MethodsPrivate *QQmlSA::Method::Methods::d_func()
      address = self.uglySide.call(
          'ritual_ZN6QQmlSA6Method7Methods6d_funcEv',
      )
      return QQmlSA.MethodsPrivate._cuteAt(address)

    @staticmethod
    def begin(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::begin() const': gives a type Python has no way
      to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Method.Methods.begin' has no cute function yet. Qt's "
          "'QMultiHash<QString, Method>::const_iterator "
          "QQmlSA::Method::Methods::begin() const': gives a type Python has "
          "no way to take yet.")

    @staticmethod
    def constBegin(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::constBegin() const': gives a type Python has
      no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Method.Methods.constBegin' has no cute function yet. "
          "Qt's 'QMultiHash<QString, Method>::const_iterator "
          "QQmlSA::Method::Methods::constBegin() const': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def constEnd(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::constEnd() const': gives a type Python has no
      way to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Method.Methods.constEnd' has no cute function yet. Qt's "
          "'QMultiHash<QString, Method>::const_iterator "
          "QQmlSA::Method::Methods::constEnd() const': gives a type Python "
          "has no way to take yet.")

    @staticmethod
    def end(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Method>::const_iterator
      QQmlSA::Method::Methods::end() const': gives a type Python has no way
      to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Method.Methods.end' has no cute function yet. Qt's "
          "'QMultiHash<QString, Method>::const_iterator "
          "QQmlSA::Method::Methods::end() const': gives a type Python has "
          "no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::Method'

  #  Qt's '~QQmlSA::Method()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSA::Method behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA6MethodD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def methodName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Method::methodName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#methodName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Method::methodName() const
    return self.uglySide.call('ritual_ZNK6QQmlSA6Method10methodNameEv')

  def sourceLocation(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation QQmlSA::Method::sourceLocation()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#sourceLocation

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::Method::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA6Method14sourceLocationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def methodType(self) -> QQmlSA.MethodType:
    """
    Calls Qt's 'MethodType QQmlSA::Method::methodType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#methodType

    Returns
    -------

    QQmlSA.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.MethodType(number)' gives.
    """
    #  MethodType QQmlSA::Method::methodType() const
    return QQmlSA.MethodType(self.uglySide.call(
        'ritual_ZNK6QQmlSA6Method10methodTypeEv',
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

  @overload(THIS)
  def __eq__(self, rhs: Method) -> bool:
    """
    Calls Qt's 'bool operator==(const Method &lhs, const Method &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#operator==

    Parameters
    ----------

    rhs : Method
      Passed on as a value: Qt reads the C++ QQmlSA::Method, which stays
      Python's own.
    """
    #  bool operator==(const Method &lhs, const Method &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_6MethodES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: Method) -> bool:
    """
    Calls Qt's 'bool operator!=(const Method &lhs, const Method &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#operator!=

    Parameters
    ----------

    rhs : Method
      Passed on as a value: Qt reads the C++ QQmlSA::Method, which stays
      Python's own.
    """
    #  bool operator!=(const Method &lhs, const Method &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_6MethodES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Method::Method()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#Method
    """
    #  QQmlSA::Method::Method()
    self._noteCreation(Method, lambda: Rituals.call(
        'ritual_ZN6QQmlSA6MethodC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: Method) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Method::Method(const Method
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#Method

    Parameters
    ----------

    a0 : Method
      Passed on as a value: Qt reads the C++ QQmlSA::Method, which stays
      Python's own.
    """
    #  QQmlSA::Method::Method(const Method &a0)
    self._noteCreation(Method, lambda: Rituals.call(
        'ritual_ZN6QQmlSA6MethodC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlSA.MethodPrivate]:
    """
    Calls Qt's 'MethodPrivate *QQmlSA::Method::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-method.html#d_func

    Returns
    -------

    Optional[QQmlSA.MethodPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MethodPrivate *QQmlSA::Method::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA6Method6d_funcEv')
    return QQmlSA.MethodPrivate._cuteAt(address)
