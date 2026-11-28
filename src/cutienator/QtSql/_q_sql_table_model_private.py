"""
QSqlTableModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqltablemodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlTableModelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSqlQueryModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QSqlRecord, QSqlTableModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlRecord = WAIT['QSqlRecord']
  QVariant = WAIT['QVariant']


class QSqlTableModelPrivate(QSqlQueryModelPrivate):
  """
  The cute side of Qt's QSqlTableModelPrivate: a plain Python object standing
  in front of one C++ QSqlTableModelPrivate.

  It is built on the cute 'QSqlQueryModelPrivate', as Qt's
  QSqlTableModelPrivate is built on Qt's QSqlQueryModelPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlTableModelPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'q_func', 'clear', 'clearCache',
  'record', 'exec', 'revertCachedRow', 'nameToIndex', 'strippedFieldName',
  'insertCount', 'initRecordAndPrimaryIndex'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlTableModel *QSqlTableModelPrivate::q_func() const': takes
    in Python what 'QSqlTableModel *QSqlTableModelPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QSqlTableModelPrivate is created at the first use, not by
    'QSqlTableModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlTableModelPrivate.
  """

  #  The enums Qt writes inside QSqlTableModelPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Op(CuteNum):
    """
    The enum 'QSqlTableModelPrivate::Op' of Qt, with the 4 names Qt gives in
    it.
    """

    NULL = Kee[int](0)
    Insert = Kee[int](1)
    Update = Kee[int](2)
    Delete = Kee[int](3)

  #  The classes Qt writes inside QSqlTableModelPrivate, each a class in here
  #  as in C++.

  class ModifiedRow(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSqlTableModelPrivate::ModifiedRow: a plain Python
    object standing in front of one C++ QSqlTableModelPrivate::ModifiedRow.

    C++ hands a QSqlTableModelPrivate::ModifiedRow around as a copy, so every
    C++ QSqlTableModelPrivate::ModifiedRow behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QSqlTableModelPrivate::ModifiedRow that has a
    ritual and that Python can call so far, 8 names in all: 'rec',
    'setValue', 'submitted', 'setSubmitted', 'refresh', 'insert', 'revert',
    'primaryValues'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSqlTableModelPrivate::ModifiedRow::ModifiedRow(Op o, const
      QSqlRecord &r)': names the enum 'QSqlTableModelPrivate::Op', whose
      class cannot be named here.
    - Qt's 'Op QSqlTableModelPrivate::ModifiedRow::op() const': gives the
      enum 'QSqlTableModelPrivate::Op', whose class cannot be named here.
    - Qt's 'void QSqlTableModelPrivate::ModifiedRow::setOp(Op o)': names the
      enum 'QSqlTableModelPrivate::Op', whose class cannot be named here.
    - Qt's 'QSqlRecord &QSqlTableModelPrivate::ModifiedRow::recRef()': gives
      a type Python has no way to take yet.
    - Qt's 'void QSqlTableModelPrivate::ModifiedRow::setGenerated(QSqlRecord
      &r, bool g)': takes a type Python has no way to hand over yet.
    - Qt's 'QSqlTableModelPrivate::ModifiedRow::~ModifiedRow()': the
      destructor: Python removes its C++ QSqlTableModelPrivate::ModifiedRow
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSqlTableModelPrivate::ModifiedRow is created at the first use,
      not by 'QSqlTableModelPrivate::ModifiedRow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSqlTableModelPrivate::ModifiedRow back gives a
      copy the ritual made for Python, in a new cute
      QSqlTableModelPrivate::ModifiedRow.
    - Each name of Qt's QSqlTableModelPrivate::ModifiedRow that has no cute
      function yet, '__init__', 'op', 'recRef', 'setGenerated', 'setOp',
      holds a function that raises 'NotImplementedError', and its docstring
      says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QSqlRecord = WAIT['QSqlRecord']
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSqlTableModelPrivate::ModifiedRow'

    #  Qt's '~QSqlTableModelPrivate::ModifiedRow()'. Naming it makes this a
    #  value class: Python owns every C++ QSqlTableModelPrivate::ModifiedRow
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QSqlTableModelPrivate11ModifiedRowD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def rec(self) -> QSqlRecord:
      """
      Calls Qt's 'const QSqlRecord &QSqlTableModelPrivate::ModifiedRow::rec()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#rec

      Returns
      -------

      QSqlRecord
        A new cute QSqlRecord around the copy Qt gave back. Python owns it.
      """
      #  const QSqlRecord &QSqlTableModelPrivate::ModifiedRow::rec() const
      address = self.uglySide.call(
          'ritual_ZNK21QSqlTableModelPrivate11ModifiedRow3recEv',
      )
      from . import QSqlRecord
      return QSqlRecord._cuteOwning(address)

    def submitted(self) -> bool:
      """
      Calls Qt's 'bool QSqlTableModelPrivate::ModifiedRow::submitted()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#submitted
      """
      #  bool QSqlTableModelPrivate::ModifiedRow::submitted() const
      return self.uglySide.call(
          'ritual_ZNK21QSqlTableModelPrivate11ModifiedRow9submittedEv',
      )

    def insert(self) -> bool:
      """
      Calls Qt's 'bool QSqlTableModelPrivate::ModifiedRow::insert() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#insert
      """
      #  bool QSqlTableModelPrivate::ModifiedRow::insert() const
      return self.uglySide.call(
          'ritual_ZNK21QSqlTableModelPrivate11ModifiedRow6insertEv',
      )

    @overload(QSqlRecord)
    def primaryValues(self, pi: QSqlRecord) -> QSqlRecord:
      """
      Calls Qt's 'QSqlRecord
      QSqlTableModelPrivate::ModifiedRow::primaryValues(const QSqlRecord &pi)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html

      Parameters
      ----------

      pi : QSqlRecord
        Passed on as a value: Qt reads the C++ QSqlRecord, which stays
        Python's own.

      Returns
      -------

      QSqlRecord
        A new cute QSqlRecord around the copy Qt gave back. Python owns it.
      """
      #  QSqlRecord QSqlTableModelPrivate::ModifiedRow::primaryValues(const
      #      QSqlRecord &pi) const
      address = self.uglySide.call(
          'ritual_ZNK21QSqlTableModelPrivate11ModifiedRow13primaryValuesERK'
          '10QSqlRecord',
          self._valueOf(pi),
      )
      from . import QSqlRecord
      return QSqlRecord._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int, QVariant)
    def setValue(self, c: int, v: QVariant) -> None:
      """
      Calls Qt's 'void QSqlTableModelPrivate::ModifiedRow::setValue(int c,
      const QVariant &v)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#setValue

      Parameters
      ----------

      c : int
        Passed on as it is.

      v : QVariant
        Passed on as a value: Qt reads the C++ QVariant, which stays Python's
        own.
      """
      #  void QSqlTableModelPrivate::ModifiedRow::setValue(int c, const
      #      QVariant &v)
      self.uglySide.call(
          'ritual_ZN21QSqlTableModelPrivate11ModifiedRow8setValueEiRK8QVari'
          'ant',
          c, self._valueOf(v),
      )

    def setSubmitted(self) -> None:
      """
      Calls Qt's 'void QSqlTableModelPrivate::ModifiedRow::setSubmitted()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html
      """
      #  void QSqlTableModelPrivate::ModifiedRow::setSubmitted()
      self.uglySide.call(
          'ritual_ZN21QSqlTableModelPrivate11ModifiedRow12setSubmittedEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QSqlTableModelPrivate::ModifiedRow::ModifiedRow(Op o, const
      QSqlRecord &r)': names the enum 'QSqlTableModelPrivate::Op', whose
      class cannot be named here.
      """
      raise NotImplementedError(
          "'QSqlTableModelPrivate.ModifiedRow.__init__' has no cute "
          "function yet. Qt's "
          "'QSqlTableModelPrivate::ModifiedRow::ModifiedRow(Op o, const "
          "QSqlRecord &r)': names the enum 'QSqlTableModelPrivate::Op', "
          "whose class cannot be named here.")

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

    @overload(bool, QSqlRecord)
    def refresh(self, exists: bool, newvals: QSqlRecord) -> None:
      """
      Calls Qt's 'void QSqlTableModelPrivate::ModifiedRow::refresh(bool
      exists, const QSqlRecord &newvals)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#refresh

      Parameters
      ----------

      exists : bool
        Passed on as it is.

      newvals : QSqlRecord
        Passed on as a value: Qt reads the C++ QSqlRecord, which stays
        Python's own.
      """
      #  void QSqlTableModelPrivate::ModifiedRow::refresh(bool exists, const
      #      QSqlRecord &newvals)
      self.uglySide.call(
          'ritual_ZN21QSqlTableModelPrivate11ModifiedRow7refreshEbRK10QSqlR'
          'ecord',
          exists, self._valueOf(newvals),
      )

    def revert(self) -> None:
      """
      Calls Qt's 'void QSqlTableModelPrivate::ModifiedRow::revert()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsqltablemodelprivate-modifiedrow.html#revert
      """
      #  void QSqlTableModelPrivate::ModifiedRow::revert()
      self.uglySide.call(
          'ritual_ZN21QSqlTableModelPrivate11ModifiedRow6revertEv',
      )

    @staticmethod
    def op(*__, **_) -> Never:
      """
      Qt's 'Op QSqlTableModelPrivate::ModifiedRow::op() const': gives the
      enum 'QSqlTableModelPrivate::Op', whose class cannot be named here.
      """
      raise NotImplementedError(
          "'QSqlTableModelPrivate.ModifiedRow.op' has no cute function yet. "
          "Qt's 'Op QSqlTableModelPrivate::ModifiedRow::op() const': gives "
          "the enum 'QSqlTableModelPrivate::Op', whose class cannot be "
          "named here.")

    @staticmethod
    def recRef(*__, **_) -> Never:
      """
      Qt's 'QSqlRecord &QSqlTableModelPrivate::ModifiedRow::recRef()': gives
      a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QSqlTableModelPrivate.ModifiedRow.recRef' has no cute function "
          "yet. Qt's 'QSqlRecord "
          "&QSqlTableModelPrivate::ModifiedRow::recRef()': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def setGenerated(*__, **_) -> Never:
      """
      Qt's 'void QSqlTableModelPrivate::ModifiedRow::setGenerated(QSqlRecord
      &r, bool g)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QSqlTableModelPrivate.ModifiedRow.setGenerated' has no cute "
          "function yet. Qt's 'void "
          "QSqlTableModelPrivate::ModifiedRow::setGenerated(QSqlRecord &r, "
          "bool g)': takes a type Python has no way to hand over yet.")

    @staticmethod
    def setOp(*__, **_) -> Never:
      """
      Qt's 'void QSqlTableModelPrivate::ModifiedRow::setOp(Op o)': names the
      enum 'QSqlTableModelPrivate::Op', whose class cannot be named here.
      """
      raise NotImplementedError(
          "'QSqlTableModelPrivate.ModifiedRow.setOp' has no cute function "
          "yet. Qt's 'void QSqlTableModelPrivate::ModifiedRow::setOp(Op "
          "o)': names the enum 'QSqlTableModelPrivate::Op', whose class "
          "cannot be named here.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlTableModelPrivate'

  #  A C++ QSqlTableModelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlTableModelPrivate'

  #  The functions Qt calls itself that QSqlTableModelPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clearCache': (
          ('_ZN21QSqlTableModelPrivate10clearCacheEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'revertCachedRow': (
          ('_ZN21QSqlTableModelPrivate15revertCachedRowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'nameToIndex': (
          ('_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def record(self, values: QList[QVariant]) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlTableModelPrivate::record(const
    QList<QVariant> &values) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodelprivate.html#record

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlTableModelPrivate::record(const QList<QVariant>
    #      &values) const
    address = self.uglySide.call(
        'ritual_ZNK21QSqlTableModelPrivate6recordERK5QListI8QVariantE',
        self._valueOf(values),
    )
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(str)
  def nameToIndex(self, name: str) -> int:
    """
    Calls Qt's 'int QSqlTableModelPrivate::nameToIndex(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#nameToIndex

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QSqlTableModelPrivate::nameToIndex(const QString &name) const
    ritual = 'ritual_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QSqlTableModelPrivate11nameToIndexERK7QString')
    return self.uglySide.call(ritual, name)

  @overload(str)
  def strippedFieldName(self, name: str) -> str:
    """
    Calls Qt's 'QString QSqlTableModelPrivate::strippedFieldName(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#strippedFieldName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlTableModelPrivate::strippedFieldName(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QSqlTableModelPrivate17strippedFieldNameERK7QString',
        name,
    )

  @overload()
  @overload(int)
  def insertCount(self, maxRow: int = -1) -> int:
    """
    Calls Qt's 'int QSqlTableModelPrivate::insertCount(int maxRow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#insertCount

    Parameters
    ----------

    maxRow : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QSqlTableModelPrivate::insertCount(int maxRow) const
    return self.uglySide.call(
        'ritual_ZNK21QSqlTableModelPrivate11insertCountEi', maxRow,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSqlTableModelPrivate::QSqlTableModelPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#QSqlTableModelPrivate
    """
    #  QSqlTableModelPrivate::QSqlTableModelPrivate()
    self._noteCreation(QSqlTableModelPrivate, lambda: Rituals.call(
        'ritual_ZN21QSqlTableModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QSqlTableModel]:
    """
    Calls Qt's 'QSqlTableModel *QSqlTableModelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodelprivate.html#q_func

    Returns
    -------

    Optional[QSqlTableModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlTableModel *QSqlTableModelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QSqlTableModelPrivate6q_funcEv')
    from . import QSqlTableModel
    return QSqlTableModel._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlTableModelPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodelprivate.html#clear
    """
    #  void QSqlTableModelPrivate::clear()
    self.uglySide.call('ritual_ZN21QSqlTableModelPrivate5clearEv')

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QSqlTableModelPrivate::clearCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#clearCache
    """
    #  void QSqlTableModelPrivate::clearCache()
    ritual = 'ritual_ZN21QSqlTableModelPrivate10clearCacheEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSqlTableModelPrivate10clearCacheEv'
    self.uglySide.call(ritual)

  @overload(str, bool, QSqlRecord, QSqlRecord)
  def exec(
      self,
      stmt: str,
      prepStatement: bool,
      rec: QSqlRecord,
      whereValues: QSqlRecord,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlTableModelPrivate::exec(const QString &stmt, bool
    prepStatement, const QSqlRecord &rec, const QSqlRecord &whereValues)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodelprivate.html#exec

    Parameters
    ----------

    stmt : str
      Passed on as it is: a QString is made of it for the call.

    prepStatement : bool
      Passed on as it is.

    rec : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.

    whereValues : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlTableModelPrivate::exec(const QString &stmt, bool
    #      prepStatement, const QSqlRecord &rec, const QSqlRecord
    #      &whereValues)
    return self.uglySide.call(
        'ritual_ZN21QSqlTableModelPrivate4execERK7QStringbRK10QSqlRecordS5_',
        stmt, prepStatement, self._valueOf(rec), self._valueOf(whereValues),
    )

  @overload(int)
  def revertCachedRow(self, row: int) -> None:
    """
    Calls Qt's 'void QSqlTableModelPrivate::revertCachedRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html#revertCachedRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QSqlTableModelPrivate::revertCachedRow(int row)
    ritual = 'ritual_ZN21QSqlTableModelPrivate15revertCachedRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSqlTableModelPrivate15revertCachedRowEi'
    self.uglySide.call(ritual, row)

  def initRecordAndPrimaryIndex(self) -> None:
    """
    Calls Qt's 'void QSqlTableModelPrivate::initRecordAndPrimaryIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodelprivate.html
    """
    #  void QSqlTableModelPrivate::initRecordAndPrimaryIndex()
    self.uglySide.call(
        'ritual_ZN21QSqlTableModelPrivate25initRecordAndPrimaryIndexEv',
    )
