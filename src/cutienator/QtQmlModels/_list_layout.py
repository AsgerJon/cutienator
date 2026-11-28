"""
ListLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ListLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ListLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ListLayout: a plain Python object standing in front
  of one C++ ListLayout.

  C++ hands a ListLayout around as a copy, so every C++ ListLayout behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ListLayout that has a ritual and that Python can
  call so far, 3 names in all: 'getExistingRole', 'roleCount', 'sync'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ListLayout::~ListLayout()': the destructor: Python removes its C++
    ListLayout by it, and has no other use for it.
  - Qt's 'const Role &ListLayout::getRoleOrCreate(QV4::String *key,
    Role::DataType type)': names the enum 'ListLayout::Role::DataType', whose
    class cannot be named here.
  - Qt's 'const Role &ListLayout::createRole(const QString &key,
    Role::DataType type)': names the enum 'ListLayout::Role::DataType', whose
    class cannot be named here.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'ListLayout.

  What to expect
  --------------

  - The C++ ListLayout is created at the first use, not by 'ListLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ListLayout back gives a copy the ritual made for
    Python, in a new cute ListLayout.
  - Each name of Qt's ListLayout that has no cute function yet, 'createRole',
    'getRoleOrCreate', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside ListLayout, each a class in here as in C++.

  class Role(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's ListLayout::Role: a plain Python object standing in
    front of one C++ ListLayout::Role.

    C++ hands a ListLayout::Role around as a copy, so every C++
    ListLayout::Role behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's ListLayout::Role yet. It can be made from Python, in
    2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'ListLayout::Role::~Role()': the destructor: Python removes its
      C++ ListLayout::Role by it, and has no other use for it.

    What to expect
    --------------

    - The C++ ListLayout::Role is created at the first use, not by
      'ListLayout::Role(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a ListLayout::Role back gives a copy the ritual made
      for Python, in a new cute ListLayout::Role.
    """

    #  The enums Qt writes inside ListLayout::Role, each a class in here as
    #  in C++, and the names Qt has for the combinations of its flags enums.

    class DataType(CuteNum):
      """
      The enum 'ListLayout::Role::DataType' of Qt, with the 11 names Qt gives
      in it.
      """

      Invalid = Kee[int](-1)
      String = Kee[int](0)
      Number = Kee[int](1)
      Bool = Kee[int](2)
      List = Kee[int](3)
      QObject = Kee[int](4)
      VariantMap = Kee[int](5)
      DateTime = Kee[int](6)
      Url = Kee[int](7)
      Function = Kee[int](8)
      MaxDataType = Kee[int](9)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'ListLayout::Role'

    #  Qt's '~ListLayout::Role()'. Naming it makes this a value class: Python
    #  owns every C++ ListLayout::Role behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN10ListLayout4RoleD1Ev'

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
      Notes what was given, for Qt's 'ListLayout::Role::Role()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/listlayout-role.html#Role
      """
      #  ListLayout::Role::Role()
      self._noteCreation(ListLayout.Role, lambda: Rituals.call(
          'ritual_ZN10ListLayout4RoleC1Ev',
      ))

    @overload(THIS)
    @overload(NoneType)
    def __init__(self, other: Optional[ListLayout.Role]) -> None:
      """
      Notes what was given, for Qt's 'ListLayout::Role::Role(const Role
      *other)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/listlayout-role.html#Role

      Parameters
      ----------

      other : Optional[ListLayout.Role]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  ListLayout::Role::Role(const Role *other)
      self._noteCreation(ListLayout.Role, lambda: Rituals.call(
          'ritual_ZN10ListLayout4RoleC1EPKS0_', self._addressOf(other),
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

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def sync(src: Optional[ListLayout], target: Optional[ListLayout]) -> None:
    """
    Calls Qt's 'void ListLayout::sync(ListLayout *src, ListLayout *target)'.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#sync

    Parameters
    ----------

    src : Optional[ListLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[ListLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ListLayout::sync(ListLayout *src, ListLayout *target)
    Rituals.call(
        'ritual_ZN10ListLayout4syncEPS_S0_',
        CuteMixin._addressOf(src), CuteMixin._addressOf(target),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ListLayout'

  #  Qt's '~ListLayout()'. Naming it makes this a value class: Python owns
  #  every C++ ListLayout behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10ListLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def getExistingRole(self, index: int) -> Role:
    """
    Calls Qt's 'const Role &ListLayout::getExistingRole(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#getExistingRole

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Role
      A new cute ListLayout::Role around the copy Qt gave back. Python owns
      it.
    """
    #  const Role &ListLayout::getExistingRole(int index) const
    address = self.uglySide.call(
        'ritual_ZNK10ListLayout15getExistingRoleEi', index,
    )
    return ListLayout.Role._cuteOwning(address)

  @overload(str)
  def getExistingRole(self, key: str) -> Optional[Role]:
    """
    Calls Qt's 'const Role *ListLayout::getExistingRole(const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#getExistingRole

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Role]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Role *ListLayout::getExistingRole(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK10ListLayout15getExistingRoleERK7QString', key,
    )
    return ListLayout.Role._cuteAt(address)

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def getExistingRole(self, key: Optional[QV4.String]) -> Optional[Role]:
    """
    Calls Qt's 'const Role *ListLayout::getExistingRole(QV4::String *key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#getExistingRole

    Parameters
    ----------

    key : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Role]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Role *ListLayout::getExistingRole(QV4::String *key) const
    address = self.uglySide.call(
        'ritual_ZNK10ListLayout15getExistingRoleEPN3QV46StringE',
        self._addressOf(key),
    )
    return ListLayout.Role._cuteAt(address)

  def roleCount(self) -> int:
    """
    Calls Qt's 'int ListLayout::roleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#roleCount
    """
    #  int ListLayout::roleCount() const
    return self.uglySide.call('ritual_ZNK10ListLayout9roleCountEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'ListLayout::ListLayout()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#ListLayout
    """
    #  ListLayout::ListLayout()
    self._noteCreation(ListLayout, lambda: Rituals.call(
        'ritual_ZN10ListLayoutC1Ev',
    ))

  @overload(THIS)
  @overload(NoneType)
  def __init__(self, other: Optional[ListLayout]) -> None:
    """
    Notes what was given, for Qt's 'ListLayout::ListLayout(const ListLayout
    *other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/listlayout.html#ListLayout

    Parameters
    ----------

    other : Optional[ListLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ListLayout::ListLayout(const ListLayout *other)
    self._noteCreation(ListLayout, lambda: Rituals.call(
        'ritual_ZN10ListLayoutC1EPKS_', self._addressOf(other),
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
  def createRole(*__, **_) -> Never:
    """
    Qt's 'const Role &ListLayout::createRole(const QString &key,
    Role::DataType type)': names the enum 'ListLayout::Role::DataType', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'ListLayout.createRole' has no cute function yet. Qt's 'const Role "
        "&ListLayout::createRole(const QString &key, Role::DataType type)': "
        "names the enum 'ListLayout::Role::DataType', whose class cannot be "
        "named here.")

  @staticmethod
  def getRoleOrCreate(*__, **_) -> Never:
    """
    - Qt's 'const Role &ListLayout::getRoleOrCreate(QV4::String *key,
      Role::DataType type)': names the enum 'ListLayout::Role::DataType',
      whose class cannot be named here.
    - Qt's 'const Role &ListLayout::getRoleOrCreate(const QString &key,
      Role::DataType type)': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'roleTypeName'.
    - Qt's 'const Role *ListLayout::getRoleOrCreate(const QString &key, const
      QVariant &data)': leans on 'ListLayout::getRoleOrCreate(QString const&,
      ListLayout::Role::DataType)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListLayout.getRoleOrCreate' has no cute function yet. Qt's 'const "
        "Role &ListLayout::getRoleOrCreate(QV4::String *key, Role::DataType "
        "type)': names the enum 'ListLayout::Role::DataType', whose class "
        "cannot be named here. Qt's 'const Role "
        "&ListLayout::getRoleOrCreate(const QString &key, Role::DataType "
        "type)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'roleTypeName'. Qt's 'const Role "
        "*ListLayout::getRoleOrCreate(const QString &key, const QVariant "
        "&data)': leans on 'ListLayout::getRoleOrCreate(QString const&, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
