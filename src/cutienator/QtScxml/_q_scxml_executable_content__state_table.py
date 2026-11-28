"""
QScxmlExecutableContent::StateTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::StateTable to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class StateTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlExecutableContent::StateTable: a plain Python
  object standing in front of one C++ QScxmlExecutableContent::StateTable.

  C++ hands a QScxmlExecutableContent::StateTable around as a copy, so every
  C++ QScxmlExecutableContent::StateTable behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::StateTable that has a
  ritual and that Python can call so far, 3 names in all: 'state',
  'transition', 'array'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlExecutableContent::StateTable::~StateTable()': the
    destructor: Python removes its C++ QScxmlExecutableContent::StateTable by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::StateTable is created at the first use,
    not by 'QScxmlExecutableContent::StateTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::StateTable back gives a copy
    the ritual made for Python, in a new cute
    QScxmlExecutableContent::StateTable.
  """

  #  The classes Qt writes inside QScxmlExecutableContent::StateTable, each a
  #  class in here as in C++.

  class Array(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlExecutableContent::StateTable::Array: a plain
    Python object standing in front of one C++
    QScxmlExecutableContent::StateTable::Array.

    C++ hands a QScxmlExecutableContent::StateTable::Array around as a copy,
    so every C++ QScxmlExecutableContent::StateTable::Array behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QScxmlExecutableContent::StateTable::Array that
    has a ritual and that Python can call so far, 5 names in all: 'size',
    'isValid', '__getitem__', 'begin', 'end'. None can be made from Python:
    one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlExecutableContent::StateTable::Array::Array(const int
      *start)': names 'int', which has no cute class yet.
    - Qt's 'QScxmlExecutableContent::StateTable::Array::~Array()': the
      destructor: Python removes its C++
      QScxmlExecutableContent::StateTable::Array by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QScxmlExecutableContent::StateTable::Array is created at the
      first use, not by 'QScxmlExecutableContent::StateTable::Array(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlExecutableContent::StateTable::Array back
      gives a copy the ritual made for Python, in a new cute
      QScxmlExecutableContent::StateTable::Array.
    - Each name of Qt's QScxmlExecutableContent::StateTable::Array that has
      no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The classes Qt writes inside
    #  QScxmlExecutableContent::StateTable::Array, each a class in here as in
    #  C++.

    class const_iterator(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QScxmlExecutableContent::StateTable::Array::const_iterator: a plain
      Python object standing in front of one C++
      QScxmlExecutableContent::StateTable::Array::const_iterator.

      C++ hands a QScxmlExecutableContent::StateTable::Array::const_iterator
      around as a copy, so every C++
      QScxmlExecutableContent::StateTable::Array::const_iterator behind a
      cute one is Python's own: it is removed, by the ritual named in
      '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      Every function of Qt's
      QScxmlExecutableContent::StateTable::Array::const_iterator that has a
      ritual and that Python can call so far, 2 names in all: '__eq__',
      '__ne__'. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's 'QScxmlExecutableContent::StateTable::Array::const_iterator::
        const_iterator(const Array &a, int pos)': names a class it is written
        two deep inside.
      - Qt's 'const_iterator
        &QScxmlExecutableContent::StateTable::Array::const_iterator::
        operator++()': an operator Python has no name for.
      - Qt's 'int
        QScxmlExecutableContent::StateTable::Array::const_iterator::
        operator*() const': an operator Python has no name for.
      - Qt's 'QScxmlExecutableContent::StateTable::Array::const_iterator::
        ~const_iterator()': the destructor: Python removes its C++
        QScxmlExecutableContent::StateTable::Array::const_iterator by it, and
        has no other use for it.

      What to expect
      --------------

      - The C++ QScxmlExecutableContent::StateTable::Array::const_iterator is
        created at the first use, not by
        'QScxmlExecutableContent::StateTable::Array::const_iterator(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a
        QScxmlExecutableContent::StateTable::Array::const_iterator back gives
        a copy the ritual made for Python, in a new cute
        QScxmlExecutableContent::StateTable::Array::const_iterator.
      - Each name of Qt's
        QScxmlExecutableContent::StateTable::Array::const_iterator that has
        no cute function yet, '__init__', holds a function that raises
        'NotImplementedError', and its docstring says why.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QScxmlExecutableContent::StateTable::Array::const_iterator'

      #  Qt's
      #  '~QScxmlExecutableContent::StateTable::Array::const_iterator()'.
      #  Naming it makes this a value class: Python owns every C++
      #  QScxmlExecutableContent::StateTable::Array::const_iterator behind a
      #  cute one, and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_iteratorD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      @overload(THIS)
      def __eq__(self, other: StateTable.Array.const_iterator) -> bool:
        """
        Calls Qt's 'bool
        QScxmlExecutableContent::StateTable::Array::const_iterator::
        operator==(const const_iterator &other) const'.

        Qt's own words:
        https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array-const_iterator.html

        Parameters
        ----------

        other : StateTable.Array.const_iterator
          Passed on as a value: Qt reads the C++
          QScxmlExecutableContent::StateTable::Array::const_iterator, which
          stays Python's own.
        """
        #  bool QScxmlExecutableContent::StateTable::Array::const_iterator::
        #      operator==(const const_iterator &other) const
        return self.uglySide.call(
            'ritual_ZNK23QScxmlExecutableContent10StateTable5Array14const_i'
            'teratoreqERKS2_',
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
      def __ne__(self, other: StateTable.Array.const_iterator) -> bool:
        """
        Calls Qt's 'bool
        QScxmlExecutableContent::StateTable::Array::const_iterator::
        operator!=(const StateTable::Array::const_iterator &other)'.

        Qt's own words:
        https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array-const_iterator.html

        Parameters
        ----------

        other : StateTable.Array.const_iterator
          Passed on as a value: Qt reads the C++
          QScxmlExecutableContent::StateTable::Array::const_iterator, which
          stays Python's own.
        """
        #  bool QScxmlExecutableContent::StateTable::Array::const_iterator::
        #      operator!=(const StateTable::Array::const_iterator &other)
        return self.uglySide.call(
            'ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_it'
            'eratorneERKS2_',
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

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      @staticmethod
      def __init__(*__, **_) -> Never:
        """
        Qt's 'QScxmlExecutableContent::StateTable::Array::const_iterator::
        const_iterator(const Array &a, int pos)': names a class it is written
        two deep inside.
        """
        raise NotImplementedError(
            "'QScxmlExecutableContent.StateTable.Array.const_iterator.__init"
            "__' has no cute function yet. Qt's "
            "'QScxmlExecutableContent::StateTable::Array::const_iterator::co"
            "nst_iterator(const Array &a, int pos)': names a class it is "
            "written two deep inside.")

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlExecutableContent::StateTable::Array'

    #  Qt's '~QScxmlExecutableContent::StateTable::Array()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QScxmlExecutableContent::StateTable::Array behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QScxmlExecutableContent10StateTable5ArrayD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def size(self) -> int:
      """
      Calls Qt's 'int QScxmlExecutableContent::StateTable::Array::size()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array.html
      """
      #  int QScxmlExecutableContent::StateTable::Array::size() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5Array4sizeEv',
      )

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QScxmlExecutableContent::StateTable::Array::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array.html
      """
      #  bool QScxmlExecutableContent::StateTable::Array::isValid() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5Array7isValidEv',
      )

    def begin(self) -> const_iterator:
      """
      Calls Qt's 'const_iterator
      QScxmlExecutableContent::StateTable::Array::begin() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array.html

      Returns
      -------

      const_iterator
        A new cute QScxmlExecutableContent::StateTable::Array::const_iterator
        around the copy Qt gave back. Python owns it.
      """
      #  const_iterator QScxmlExecutableContent::StateTable::Array::begin()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5Array5beginEv',
      )
      return QScxmlExecutableContent.StateTable.Array.const_iterator._cuteOwning(address)

    def end(self) -> const_iterator:
      """
      Calls Qt's 'const_iterator
      QScxmlExecutableContent::StateTable::Array::end() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array.html

      Returns
      -------

      const_iterator
        A new cute QScxmlExecutableContent::StateTable::Array::const_iterator
        around the copy Qt gave back. Python owns it.
      """
      #  const_iterator QScxmlExecutableContent::StateTable::Array::end()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5Array3endEv',
      )
      return QScxmlExecutableContent.StateTable.Array.const_iterator._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def __getitem__(self, idx: int) -> int:
      """
      Calls Qt's 'int
      QScxmlExecutableContent::StateTable::Array::operator[](int idx) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-array.html

      Parameters
      ----------

      idx : int
        Passed on as it is.
      """
      #  int QScxmlExecutableContent::StateTable::Array::operator[](int idx)
      #      const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5ArrayixEi', idx,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QScxmlExecutableContent::StateTable::Array::Array(const int
      *start)': names 'int', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QScxmlExecutableContent.StateTable.Array.__init__' has no cute "
          "function yet. Qt's "
          "'QScxmlExecutableContent::StateTable::Array::Array(const int "
          "*start)': names 'int', which has no cute class yet.")

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

  class State(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlExecutableContent::StateTable::State: a plain
    Python object standing in front of one C++
    QScxmlExecutableContent::StateTable::State.

    C++ hands a QScxmlExecutableContent::StateTable::State around as a copy,
    so every C++ QScxmlExecutableContent::StateTable::State behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QScxmlExecutableContent::StateTable::State that
    has a ritual and that Python can call so far, 5 names in all: 'isAtomic',
    'isCompound', 'parentIsScxmlElement', 'isHistoryState', 'isParallel'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlExecutableContent::StateTable::State::~State()': the
      destructor: Python removes its C++
      QScxmlExecutableContent::StateTable::State by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QScxmlExecutableContent::StateTable::State is created at the
      first use, not by 'QScxmlExecutableContent::StateTable::State(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlExecutableContent::StateTable::State back
      gives a copy the ritual made for Python, in a new cute
      QScxmlExecutableContent::StateTable::State.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlExecutableContent::StateTable::State'

    #  Qt's '~QScxmlExecutableContent::StateTable::State()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QScxmlExecutableContent::StateTable::State behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QScxmlExecutableContent10StateTable5StateD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isAtomic(self) -> bool:
      """
      Calls Qt's 'bool QScxmlExecutableContent::StateTable::State::isAtomic()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  bool QScxmlExecutableContent::StateTable::State::isAtomic() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5State8isAtomicEv',
      )

    def isCompound(self) -> bool:
      """
      Calls Qt's 'bool
      QScxmlExecutableContent::StateTable::State::isCompound() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  bool QScxmlExecutableContent::StateTable::State::isCompound() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5State10isCompoun'
          'dEv',
      )

    def parentIsScxmlElement(self) -> bool:
      """
      Calls Qt's 'bool
      QScxmlExecutableContent::StateTable::State::parentIsScxmlElement()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  bool QScxmlExecutableContent::StateTable::State::
      #      parentIsScxmlElement() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5State20parentIsS'
          'cxmlElementEv',
      )

    def isHistoryState(self) -> bool:
      """
      Calls Qt's 'bool
      QScxmlExecutableContent::StateTable::State::isHistoryState() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  bool QScxmlExecutableContent::StateTable::State::isHistoryState()
      #      const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5State14isHistory'
          'StateEv',
      )

    def isParallel(self) -> bool:
      """
      Calls Qt's 'bool
      QScxmlExecutableContent::StateTable::State::isParallel() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  bool QScxmlExecutableContent::StateTable::State::isParallel() const
      return self.uglySide.call(
          'ritual_ZNK23QScxmlExecutableContent10StateTable5State10isParalle'
          'lEv',
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QScxmlExecutableContent::StateTable::State::State()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-state.html
      """
      #  QScxmlExecutableContent::StateTable::State::State()
      self._noteCreation(StateTable.State, lambda: Rituals.call(
          'ritual_ZN23QScxmlExecutableContent10StateTable5StateC1Ev',
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

  class Transition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlExecutableContent::StateTable::Transition: a
    plain Python object standing in front of one C++
    QScxmlExecutableContent::StateTable::Transition.

    C++ hands a QScxmlExecutableContent::StateTable::Transition around as a
    copy, so every C++ QScxmlExecutableContent::StateTable::Transition behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QScxmlExecutableContent::StateTable::Transition yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlExecutableContent::StateTable::Transition::~Transition()':
      the destructor: Python removes its C++
      QScxmlExecutableContent::StateTable::Transition by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QScxmlExecutableContent::StateTable::Transition is created at
      the first use, not by
      'QScxmlExecutableContent::StateTable::Transition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlExecutableContent::StateTable::Transition
      back gives a copy the ritual made for Python, in a new cute
      QScxmlExecutableContent::StateTable::Transition.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlExecutableContent::StateTable::Transition'

    #  Qt's '~QScxmlExecutableContent::StateTable::Transition()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QScxmlExecutableContent::StateTable::Transition behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QScxmlExecutableContent10StateTable10TransitionD1Ev')

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
      Notes what was given, for Qt's
      'QScxmlExecutableContent::StateTable::Transition::Transition()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable-transition.html
      """
      #  QScxmlExecutableContent::StateTable::Transition::Transition()
      self._noteCreation(StateTable.Transition, lambda: Rituals.call(
          'ritual_ZN23QScxmlExecutableContent10StateTable10TransitionC1Ev',
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
  __qt_class__ = 'QScxmlExecutableContent::StateTable'

  #  Qt's '~QScxmlExecutableContent::StateTable()'. Naming it makes this a
  #  value class: Python owns every C++ QScxmlExecutableContent::StateTable
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent10StateTableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def state(self, idx: int) -> State:
    """
    Calls Qt's 'const State &QScxmlExecutableContent::StateTable::state(int
    idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable.html#state

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    State
      A new cute QScxmlExecutableContent::StateTable::State around the copy
      Qt gave back. Python owns it.
    """
    #  const State &QScxmlExecutableContent::StateTable::state(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent10StateTable5stateEi', idx,
    )
    return QScxmlExecutableContent.StateTable.State._cuteOwning(address)

  @overload(int)
  def transition(self, idx: int) -> Transition:
    """
    Calls Qt's 'const Transition
    &QScxmlExecutableContent::StateTable::transition(int idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable.html#transition

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Transition
      A new cute QScxmlExecutableContent::StateTable::Transition around the
      copy Qt gave back. Python owns it.
    """
    #  const Transition &QScxmlExecutableContent::StateTable::transition(int
    #      idx) const
    address = self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent10StateTable10transitionEi', idx,
    )
    return QScxmlExecutableContent.StateTable.Transition._cuteOwning(address)

  @overload(int)
  def array(self, idx: int) -> Array:
    """
    Calls Qt's 'const Array QScxmlExecutableContent::StateTable::array(int
    idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable.html#array

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Array
      A new cute QScxmlExecutableContent::StateTable::Array around the copy
      Qt gave back. Python owns it.
    """
    #  const Array QScxmlExecutableContent::StateTable::array(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent10StateTable5arrayEi', idx,
    )
    return QScxmlExecutableContent.StateTable.Array._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QScxmlExecutableContent::StateTable::StateTable()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-statetable.html#StateTable
    """
    #  QScxmlExecutableContent::StateTable::StateTable()
    self._noteCreation(StateTable, lambda: Rituals.call(
        'ritual_ZN23QScxmlExecutableContent10StateTableC1Ev',
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
