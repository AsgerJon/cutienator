"""
QtProtobufPrivate::QProtobufPropertyOrdering binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufpropertyordering.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QProtobufPropertyOrdering(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtProtobufPrivate::QProtobufPropertyOrdering: a plain
  Python object standing in front of one C++
  QtProtobufPrivate::QProtobufPropertyOrdering.

  C++ hands a QtProtobufPrivate::QProtobufPropertyOrdering around as a copy,
  so every C++ QtProtobufPrivate::QProtobufPropertyOrdering behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtProtobufPrivate::QProtobufPropertyOrdering that
  has a ritual and that Python can call so far, 7 names in all:
  'fieldNumber', 'propertyIndex', 'fieldFlags', 'indexOfFieldNumber',
  'fieldCount', 'char_data', 'uint_dataForIndex'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUtf8StringView
    QtProtobufPrivate::QProtobufPropertyOrdering::messageFullName() const':
    gives a type Python has no way to take yet.
  - Qt's 'QUtf8StringView
    QtProtobufPrivate::QProtobufPropertyOrdering::jsonName(int index) const':
    gives a type Python has no way to take yet.
  - Qt's 'char
    *QtProtobufPrivate::QProtobufPropertyOrdering::char_data(NonConstTag a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const uint
    *QtProtobufPrivate::QProtobufPropertyOrdering::uint_data() const': gives
    'unsigned int', which has no cute class yet.
  - Qt's 'QtProtobufPrivate::QProtobufPropertyOrdering::
    ~QProtobufPropertyOrdering()': the destructor: Python removes its C++
    QtProtobufPrivate::QProtobufPropertyOrdering by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QtProtobufPrivate::QProtobufPropertyOrdering is created at the
    first use, not by 'QtProtobufPrivate::QProtobufPropertyOrdering(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtProtobufPrivate::QProtobufPropertyOrdering back
    gives a copy the ritual made for Python, in a new cute
    QtProtobufPrivate::QProtobufPropertyOrdering.
  - Each name of Qt's QtProtobufPrivate::QProtobufPropertyOrdering that has
    no cute function yet, 'jsonName', 'messageFullName', 'uint_data', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside
  #  QtProtobufPrivate::QProtobufPropertyOrdering, each a class in here as in
  #  C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QtProtobufPrivate::QProtobufPropertyOrdering::Data:
    a plain Python object standing in front of one C++
    QtProtobufPrivate::QProtobufPropertyOrdering::Data.

    C++ hands a QtProtobufPrivate::QProtobufPropertyOrdering::Data around as
    a copy, so every C++ QtProtobufPrivate::QProtobufPropertyOrdering::Data
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QtProtobufPrivate::QProtobufPropertyOrdering::Data
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QtProtobufPrivate::QProtobufPropertyOrdering::Data::~Data()': the
      destructor: Python removes its C++
      QtProtobufPrivate::QProtobufPropertyOrdering::Data by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QtProtobufPrivate::QProtobufPropertyOrdering::Data is created
      at the first use, not by
      'QtProtobufPrivate::QProtobufPropertyOrdering::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QtProtobufPrivate::QProtobufPropertyOrdering::Data
      back gives a copy the ritual made for Python, in a new cute
      QtProtobufPrivate::QProtobufPropertyOrdering::Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QtProtobufPrivate::QProtobufPropertyOrdering::Data'

    #  Qt's '~QtProtobufPrivate::QProtobufPropertyOrdering::Data()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QtProtobufPrivate::QProtobufPropertyOrdering::Data behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QtProtobufPrivate25QProtobufPropertyOrdering4DataD1Ev')

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
  __qt_class__ = 'QtProtobufPrivate::QProtobufPropertyOrdering'

  #  Qt's '~QtProtobufPrivate::QProtobufPropertyOrdering()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtProtobufPrivate::QProtobufPropertyOrdering behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN17QtProtobufPrivate25QProtobufPropertyOrderingD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def fieldNumber(self, index: int) -> int:
    """
    Calls Qt's 'int
    QtProtobufPrivate::QProtobufPropertyOrdering::fieldNumber(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QtProtobufPrivate::QProtobufPropertyOrdering::fieldNumber(int
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering11fieldNum'
        'berEi',
        index,
    )

  @overload(int)
  def propertyIndex(self, index: int) -> int:
    """
    Calls Qt's 'int
    QtProtobufPrivate::QProtobufPropertyOrdering::propertyIndex(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QtProtobufPrivate::QProtobufPropertyOrdering::propertyIndex(int
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering13property'
        'IndexEi',
        index,
    )

  @overload(int)
  def fieldFlags(self, index: int) -> QtProtobufPrivate.FieldFlags:
    """
    Calls Qt's 'FieldFlags
    QtProtobufPrivate::QProtobufPropertyOrdering::fieldFlags(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QtProtobufPrivate.FieldFlags
      The value standing for the combination Qt gave back.
    """
    #  FieldFlags
    #      QtProtobufPrivate::QProtobufPropertyOrdering::fieldFlags(int
    #      index) const
    return QtProtobufPrivate.FieldFlags(self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering10fieldFla'
        'gsEi',
        index,
    ))

  @overload(int)
  def indexOfFieldNumber(self, fieldNumber: int) -> int:
    """
    Calls Qt's 'int
    QtProtobufPrivate::QProtobufPropertyOrdering::indexOfFieldNumber(int
    fieldNumber) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Parameters
    ----------

    fieldNumber : int
      Passed on as it is.
    """
    #  int QtProtobufPrivate::QProtobufPropertyOrdering::indexOfFieldNumber(
    #      int fieldNumber) const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering18indexOfF'
        'ieldNumberEi',
        fieldNumber,
    )

  def fieldCount(self) -> int:
    """
    Calls Qt's 'int
    QtProtobufPrivate::QProtobufPropertyOrdering::fieldCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html
    """
    #  int QtProtobufPrivate::QProtobufPropertyOrdering::fieldCount() const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering10fieldCou'
        'ntEv',
    )

  def char_data(self) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtProtobufPrivate::QProtobufPropertyOrdering::char_data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtProtobufPrivate::QProtobufPropertyOrdering::char_data()
    #      const
    chars = self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9char_data'
        'Ev',
    )
    return None if chars is None else chars.decode()

  @overload(int, int)
  def uint_dataForIndex(self, index: int, offset: int) -> int:
    """
    Calls Qt's 'const uint
    &QtProtobufPrivate::QProtobufPropertyOrdering::uint_dataForIndex(int
    index, uint offset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufpropertyordering.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  const uint
    #      &QtProtobufPrivate::QProtobufPropertyOrdering::uint_dataForIndex(
    #      int index, uint offset) const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering17uint_dat'
        'aForIndexEij',
        index, offset,
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
  def jsonName(*__, **_) -> Never:
    """
    Qt's 'QUtf8StringView
    QtProtobufPrivate::QProtobufPropertyOrdering::jsonName(int index) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufPropertyOrdering.jsonName' has no cute "
        "function yet. Qt's 'QUtf8StringView "
        "QtProtobufPrivate::QProtobufPropertyOrdering::jsonName(int index) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def messageFullName(*__, **_) -> Never:
    """
    Qt's 'QUtf8StringView
    QtProtobufPrivate::QProtobufPropertyOrdering::messageFullName() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufPropertyOrdering.messageFullName' has "
        "no cute function yet. Qt's 'QUtf8StringView "
        "QtProtobufPrivate::QProtobufPropertyOrdering::messageFullName() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def uint_data(*__, **_) -> Never:
    """
    - Qt's 'const uint
      *QtProtobufPrivate::QProtobufPropertyOrdering::uint_data() const':
      gives 'unsigned int', which has no cute class yet.
    - Qt's 'uint
      *QtProtobufPrivate::QProtobufPropertyOrdering::uint_data(NonConstTag
      a0) const': takes or gives a type that cannot be passed yet: uint *.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufPropertyOrdering.uint_data' has no "
        "cute function yet. Qt's 'const uint "
        "*QtProtobufPrivate::QProtobufPropertyOrdering::uint_data() const': "
        "gives 'unsigned int', which has no cute class yet. Qt's 'uint "
        "*QtProtobufPrivate::QProtobufPropertyOrdering::uint_data(NonConstTa"
        "g a0) const': takes or gives a type that cannot be passed yet: "
        "uint *.")
