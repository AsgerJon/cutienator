"""
QLocaleData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QLocaleData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from . import QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLocaleId


class QLocaleData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLocaleData: a plain Python object standing in front
  of one C++ QLocaleData.

  C++ hands a QLocaleData around as a copy, so every C++ QLocaleData behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLocaleData that has a ritual and that Python can
  call so far, 40 names in all: 'validateChars', 'id', 'groupSizes',
  'startListPattern', 'midListPattern', 'endListPattern', 'pairListPattern',
  'listDelimit', 'decimalSeparator', 'groupDelim', 'percent', 'zero',
  'minus', 'plus', 'exponential', 'quoteStart', 'quoteEnd',
  'quoteStartAlternate', 'quoteEndAlternate', 'longDateFormat',
  'shortDateFormat', 'longTimeFormat', 'shortTimeFormat',
  'longDayNamesStandalone', 'longDayNames', 'shortDayNamesStandalone',
  'shortDayNames', 'narrowDayNamesStandalone', 'narrowDayNames',
  'anteMeridiem', 'postMeridiem', 'byteCount', 'byteAmountSI',
  'byteAmountIEC', 'currencySymbol', 'currencyDisplayName', 'currencyFormat',
  'currencyFormatNegative', 'endonymLanguage', 'endonymTerritory'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float QLocaleData::convertDoubleToFloat(double d, bool *ok)': takes
    a number to change where it is.
  - Qt's 'QSimpleParsedNumber<qint64>
    QLocaleData::bytearrayToLongLong(QByteArrayView num, int base)': gives a
    type Python has no way to take yet.
  - Qt's 'QLocaleData::~QLocaleData()': the destructor: Python removes its
    C++ QLocaleData by it, and has no other use for it.

  What has no ritual
  ------------------

  26 of the 69 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 leans on
  'QLocaleData; 3 leans on 'qulltoa(unsigned long long, int, QStringView)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 2 leans on 'qstrntoull(char const*, long long, int)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken; 1 leans on 'qt_asciiToDouble(char const*, long long,
  StrayCharacterMode)', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QLocaleData is created at the first use, not by
    'QLocaleData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLocaleData back gives a copy the ritual made for
    Python, in a new cute QLocaleData.
  - Each name of Qt's QLocaleData that has no cute function yet,
    'allLocaleDataRows', 'applyIntegerFormatting', 'bytearrayToLongLong',
    'bytearrayToUnsLongLong', 'c', 'convertDoubleToFloat',
    'dataForLocaleIndex', 'decimalForm', 'decimalPoint', 'digitSequence',
    'doubleToString', 'exponentForm', 'exponentSeparator', 'findLocaleIndex',
    'groupSeparator', 'listSeparator', 'longLongToString', 'negativeSign',
    'numberToCLocale', 'percentSign', 'positiveSign', 'signPrefix',
    'stringToDouble', 'stringToLongLong', 'stringToUnsLongLong',
    'unsLongLongToString', 'zeroDigit', 'zeroUcs', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLocaleData, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DoubleForm(CuteNum):
    """
    The enum 'QLocaleData::DoubleForm' of Qt, with the 4 names Qt gives in
    it.
    """

    DFExponent = Kee[int](0)
    DFDecimal = Kee[int](1)
    DFSignificantDigits = Kee[int](2)
    _DFMax = Kee[int](2)

  class Flags(CuteNum):
    """
    The enum 'QLocaleData::Flags' of Qt, with the 12 names Qt gives in it.
    """

    NoFlags = Kee[int](0)
    AddTrailingZeroes = Kee[int](1)
    ZeroPadded = Kee[int](2)
    LeftAdjusted = Kee[int](4)
    BlankBeforePositive = Kee[int](8)
    AlwaysShowSign = Kee[int](16)
    GroupDigits = Kee[int](32)
    CapitalEorX = Kee[int](64)
    ShowBase = Kee[int](128)
    UppercaseBase = Kee[int](256)
    ZeroPadExponent = Kee[int](512)
    ForcePoint = Kee[int](1024)

  class NumberMode(CuteNum):
    """
    The enum 'QLocaleData::NumberMode' of Qt, with the 3 names Qt gives in
    it.
    """

    IntegerMode = Kee[int](0)
    DoubleStandardMode = Kee[int](1)
    DoubleScientificMode = Kee[int](2)

  #  The classes Qt writes inside QLocaleData, each a class in here as in
  #  C++.

  class DataRange(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLocaleData::DataRange: a plain Python object
    standing in front of one C++ QLocaleData::DataRange.

    C++ hands a QLocaleData::DataRange around as a copy, so every C++
    QLocaleData::DataRange behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QLocaleData::DataRange that has a ritual and that
    Python can call so far, 1 name in all: 'stringSize'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QString QLocaleData::DataRange::getData(const char16_t *table)
      const': names 'char16_t', which has no cute class yet.
    - Qt's 'QStringView QLocaleData::DataRange::viewData(const char16_t
      *table) const': names 'char16_t', which has no cute class yet.
    - Qt's 'QString QLocaleData::DataRange::getListEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
    - Qt's 'QStringView QLocaleData::DataRange::viewListEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
    - Qt's 'char32_t QLocaleData::DataRange::ucsFirst(const char16_t *table)
      const': names 'char16_t', which has no cute class yet.
    - Qt's 'const QChar *QLocaleData::DataRange::stringStart(const char16_t
      *table) const': names 'char16_t', which has no cute class yet.
    - Qt's 'DataRange QLocaleData::DataRange::listEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
    - Qt's 'QLocaleData::DataRange::~DataRange()': the destructor: Python
      removes its C++ QLocaleData::DataRange by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QLocaleData::DataRange is created at the first use, not by
      'QLocaleData::DataRange(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLocaleData::DataRange back gives a copy the ritual
      made for Python, in a new cute QLocaleData::DataRange.
    - Each name of Qt's QLocaleData::DataRange that has no cute function yet,
      'getData', 'getListEntry', 'listEntry', 'stringStart', 'ucsFirst',
      'viewData', 'viewListEntry', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLocaleData::DataRange'

    #  Qt's '~QLocaleData::DataRange()'. Naming it makes this a value class:
    #  Python owns every C++ QLocaleData::DataRange behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QLocaleData9DataRangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def stringSize(self) -> int:
      """
      Calls Qt's 'qsizetype QLocaleData::DataRange::stringSize() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-datarange.html#stringSize
      """
      #  qsizetype QLocaleData::DataRange::stringSize() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData9DataRange10stringSizeEv',
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

    @staticmethod
    def getData(*__, **_) -> Never:
      """
      Qt's 'QString QLocaleData::DataRange::getData(const char16_t *table)
      const': names 'char16_t', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.getData' has no cute function yet. Qt's "
          "'QString QLocaleData::DataRange::getData(const char16_t *table) "
          "const': names 'char16_t', which has no cute class yet.")

    @staticmethod
    def getListEntry(*__, **_) -> Never:
      """
      Qt's 'QString QLocaleData::DataRange::getListEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.getListEntry' has no cute function yet. "
          "Qt's 'QString QLocaleData::DataRange::getListEntry(const "
          "char16_t *table, qsizetype index) const': names 'char16_t', "
          "which has no cute class yet.")

    @staticmethod
    def listEntry(*__, **_) -> Never:
      """
      Qt's 'DataRange QLocaleData::DataRange::listEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.listEntry' has no cute function yet. Qt's "
          "'DataRange QLocaleData::DataRange::listEntry(const char16_t "
          "*table, qsizetype index) const': names 'char16_t', which has no "
          "cute class yet.")

    @staticmethod
    def stringStart(*__, **_) -> Never:
      """
      Qt's 'const QChar *QLocaleData::DataRange::stringStart(const char16_t
      *table) const': names 'char16_t', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.stringStart' has no cute function yet. "
          "Qt's 'const QChar *QLocaleData::DataRange::stringStart(const "
          "char16_t *table) const': names 'char16_t', which has no cute "
          "class yet.")

    @staticmethod
    def ucsFirst(*__, **_) -> Never:
      """
      Qt's 'char32_t QLocaleData::DataRange::ucsFirst(const char16_t *table)
      const': names 'char16_t', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.ucsFirst' has no cute function yet. Qt's "
          "'char32_t QLocaleData::DataRange::ucsFirst(const char16_t "
          "*table) const': names 'char16_t', which has no cute class yet.")

    @staticmethod
    def viewData(*__, **_) -> Never:
      """
      Qt's 'QStringView QLocaleData::DataRange::viewData(const char16_t
      *table) const': names 'char16_t', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.viewData' has no cute function yet. Qt's "
          "'QStringView QLocaleData::DataRange::viewData(const char16_t "
          "*table) const': names 'char16_t', which has no cute class yet.")

    @staticmethod
    def viewListEntry(*__, **_) -> Never:
      """
      Qt's 'QStringView QLocaleData::DataRange::viewListEntry(const char16_t
      *table, qsizetype index) const': names 'char16_t', which has no cute
      class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DataRange.viewListEntry' has no cute function yet. "
          "Qt's 'QStringView QLocaleData::DataRange::viewListEntry(const "
          "char16_t *table, qsizetype index) const': names 'char16_t', "
          "which has no cute class yet.")

  class DigitSequence(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLocaleData::DigitSequence: a plain Python object
    standing in front of one C++ QLocaleData::DigitSequence.

    C++ hands a QLocaleData::DigitSequence around as a copy, so every C++
    QLocaleData::DigitSequence behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QLocaleData::DigitSequence that has a ritual and
    that Python can call so far, 8 names in all: 'endIndex', 'size',
    'isEmpty', 'hasSign', 'first', 'last', 'sliced', 'used'. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLocaleData::DigitSequence::DigitSequence(DigitSequence &&a0)':
      takes a type Python has no way to hand over yet.
    - Qt's 'DigitSequence &QLocaleData::DigitSequence::operator=(const
      DigitSequence &a0)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'DigitSequence
      &QLocaleData::DigitSequence::operator=(DigitSequence &&a0)':
      assignment: Python binds a name and has no operator for it.
    - Qt's 'QLocaleData::DigitSequence::~DigitSequence()': the destructor:
      Python removes its C++ QLocaleData::DigitSequence by it, and has no
      other use for it.
    - Qt's 'void QLocaleData::DigitSequence::transcribeTo(CharBuff *buff)
      const': names 'QLocaleData::CharBuff', which has no cute class yet.
    - Qt's 'QLocaleData::DigitSequence::DigitSequence(QByteArray &&digs,
      QList<qsizetype> &&bounds, char sgn)': takes a type Python has no way
      to hand over yet.

    What has no ritual
    ------------------

    1 of the 18 functions Qt declares: 1 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ QLocaleData::DigitSequence is created at the first use, not by
      'QLocaleData::DigitSequence(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLocaleData::DigitSequence back gives a copy the
      ritual made for Python, in a new cute QLocaleData::DigitSequence.
    - Each name of Qt's QLocaleData::DigitSequence that has no cute function
      yet, 'transcribeTo', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The enums Qt writes inside QLocaleData::DigitSequence, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Option(CuteFlags, scoped=True):
      """
      The flags enum 'QLocaleData::DigitSequence::Option' of Qt, with the 2
      names Qt gives in it. Qt names the type of its combinations
      'QLocaleData::DigitSequence::Options'. C++ keeps these names inside the
      enum, so the class that holds the enum does not have them.
      """

      Default = 0x0
      AllowSign = 0x1

    Options = Option

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLocaleData::DigitSequence'

    #  Qt's '~QLocaleData::DigitSequence()'. Naming it makes this a value
    #  class: Python owns every C++ QLocaleData::DigitSequence behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QLocaleData13DigitSequenceD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def endIndex(self) -> int:
      """
      Calls Qt's 'qsizetype QLocaleData::DigitSequence::endIndex() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#endIndex
      """
      #  qsizetype QLocaleData::DigitSequence::endIndex() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence8endIndexEv',
      )

    def size(self) -> int:
      """
      Calls Qt's 'qsizetype QLocaleData::DigitSequence::size() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#size
      """
      #  qsizetype QLocaleData::DigitSequence::size() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence4sizeEv',
      )

    def isEmpty(self) -> bool:
      """
      Calls Qt's 'bool QLocaleData::DigitSequence::isEmpty() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#isEmpty
      """
      #  bool QLocaleData::DigitSequence::isEmpty() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence7isEmptyEv',
      )

    def hasSign(self) -> bool:
      """
      Calls Qt's 'bool QLocaleData::DigitSequence::hasSign() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#hasSign
      """
      #  bool QLocaleData::DigitSequence::hasSign() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence7hasSignEv',
      )

    @overload(int)
    def first(self, count: int) -> QLocaleData.DigitSequence:
      """
      Calls Qt's 'DigitSequence QLocaleData::DigitSequence::first(qsizetype
      count) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#first

      Parameters
      ----------

      count : int
        Passed on as it is.

      Returns
      -------

      QLocaleData.DigitSequence
        A new cute QLocaleData::DigitSequence around the copy Qt gave back.
        Python owns it.
      """
      #  DigitSequence QLocaleData::DigitSequence::first(qsizetype count)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence5firstEx', count,
      )
      return QLocaleData.DigitSequence._cuteOwning(address)

    @overload(int)
    def last(self, count: int) -> QLocaleData.DigitSequence:
      """
      Calls Qt's 'DigitSequence QLocaleData::DigitSequence::last(qsizetype
      count) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#last

      Parameters
      ----------

      count : int
        Passed on as it is.

      Returns
      -------

      QLocaleData.DigitSequence
        A new cute QLocaleData::DigitSequence around the copy Qt gave back.
        Python owns it.
      """
      #  DigitSequence QLocaleData::DigitSequence::last(qsizetype count)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence4lastEx', count,
      )
      return QLocaleData.DigitSequence._cuteOwning(address)

    @overload(int)
    def sliced(self, from_: int) -> QLocaleData.DigitSequence:
      """
      Calls Qt's 'DigitSequence QLocaleData::DigitSequence::sliced(qsizetype
      from) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#sliced

      Parameters
      ----------

      from_ : int
        Passed on as it is.

      Returns
      -------

      QLocaleData.DigitSequence
        A new cute QLocaleData::DigitSequence around the copy Qt gave back.
        Python owns it.
      """
      #  DigitSequence QLocaleData::DigitSequence::sliced(qsizetype from)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence6slicedEx', from_,
      )
      return QLocaleData.DigitSequence._cuteOwning(address)

    @overload(int, int)
    def sliced(self, from_: int, count: int) -> QLocaleData.DigitSequence:
      """
      Calls Qt's 'DigitSequence QLocaleData::DigitSequence::sliced(qsizetype
      from, qsizetype count) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#sliced

      Parameters
      ----------

      from_ : int
        Passed on as it is.

      count : int
        Passed on as it is.

      Returns
      -------

      QLocaleData.DigitSequence
        A new cute QLocaleData::DigitSequence around the copy Qt gave back.
        Python owns it.
      """
      #  DigitSequence QLocaleData::DigitSequence::sliced(qsizetype from,
      #      qsizetype count) const
      address = self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence6slicedExx', from_, count,
      )
      return QLocaleData.DigitSequence._cuteOwning(address)

    @overload(str, int)
    def used(self, text: str, from_: int) -> str:
      """
      Calls Qt's 'QStringView QLocaleData::DigitSequence::used(const
      QStringView text, qsizetype from) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#used

      Parameters
      ----------

      text : str
        Passed on as it is: a QString is made of it for the call.

      from_ : int
        Passed on as it is.

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QStringView QLocaleData::DigitSequence::used(const QStringView text,
      #      qsizetype from) const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence4usedE11QStringViewx',
          text, from_,
      )

    @overload(str)
    def used(self, text: str) -> str:
      """
      Calls Qt's 'QStringView QLocaleData::DigitSequence::used(const
      QStringView text) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#used

      Parameters
      ----------

      text : str
        Passed on as it is: a QString is made of it for the call.

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QStringView QLocaleData::DigitSequence::used(const QStringView text)
      #      const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData13DigitSequence4usedE11QStringView', text,
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

    @overload(THIS)
    def __init__(self, a0: QLocaleData.DigitSequence) -> None:
      """
      Notes what was given, for Qt's
      'QLocaleData::DigitSequence::DigitSequence(const DigitSequence &a0)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-digitsequence.html#DigitSequence

      Parameters
      ----------

      a0 : QLocaleData.DigitSequence
        Passed on as a value: Qt reads the C++ QLocaleData::DigitSequence,
        which stays Python's own.
      """
      #  QLocaleData::DigitSequence::DigitSequence(const DigitSequence &a0)
      self._noteCreation(QLocaleData.DigitSequence, lambda: Rituals.call(
          'ritual_ZN11QLocaleData13DigitSequenceC1ERKS0_', self._valueOf(a0),
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

    @staticmethod
    def transcribeTo(*__, **_) -> Never:
      """
      Qt's 'void QLocaleData::DigitSequence::transcribeTo(CharBuff *buff)
      const': names 'QLocaleData::CharBuff', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QLocaleData.DigitSequence.transcribeTo' has no cute function "
          "yet. Qt's 'void "
          "QLocaleData::DigitSequence::transcribeTo(CharBuff *buff) const': "
          "names 'QLocaleData::CharBuff', which has no cute class yet.")

  class GroupSizes(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLocaleData::GroupSizes: a plain Python object
    standing in front of one C++ QLocaleData::GroupSizes.

    C++ hands a QLocaleData::GroupSizes around as a copy, so every C++
    QLocaleData::GroupSizes behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QLocaleData::GroupSizes that has a ritual and that
    Python can call so far, 1 name in all: 'isValid'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLocaleData::GroupSizes::~GroupSizes()': the destructor: Python
      removes its C++ QLocaleData::GroupSizes by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QLocaleData::GroupSizes is created at the first use, not by
      'QLocaleData::GroupSizes(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLocaleData::GroupSizes back gives a copy the
      ritual made for Python, in a new cute QLocaleData::GroupSizes.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLocaleData::GroupSizes'

    #  Qt's '~QLocaleData::GroupSizes()'. Naming it makes this a value class:
    #  Python owns every C++ QLocaleData::GroupSizes behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QLocaleData10GroupSizesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QLocaleData::GroupSizes::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-groupsizes.html#isValid
      """
      #  bool QLocaleData::GroupSizes::isValid() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData10GroupSizes7isValidEv',
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

  class NumericData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLocaleData::NumericData: a plain Python object
    standing in front of one C++ QLocaleData::NumericData.

    C++ hands a QLocaleData::NumericData around as a copy, so every C++
    QLocaleData::NumericData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QLocaleData::NumericData that has a ritual and
    that Python can call so far, 4 names in all: 'setZero', 'zeroWidth',
    'digitValue', 'fractionalIsGroup'. None can be made from Python: one
    comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const GroupSizes &QLocaleData::NumericData::groupSizes() const':
      gives 'QLocaleData::GroupSizes', which stands beside this class inside
      'QLocaleData' and cannot be named from here.
    - Qt's 'bool QLocaleData::NumericData::isValid(NumberMode mode) const':
      names the enum 'QLocaleData::NumberMode', whose class cannot be named
      here.
    - Qt's 'QLocaleData::NumericData::~NumericData()': the destructor: Python
      removes its C++ QLocaleData::NumericData by it, and has no other use
      for it.

    What has no ritual
    ------------------

    1 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ QLocaleData::NumericData is created at the first use, not by
      'QLocaleData::NumericData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLocaleData::NumericData back gives a copy the
      ritual made for Python, in a new cute QLocaleData::NumericData.
    - Each name of Qt's QLocaleData::NumericData that has no cute function
      yet, '__init__', 'groupSizes', 'isValid', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLocaleData::NumericData'

    #  Qt's '~QLocaleData::NumericData()'. Naming it makes this a value
    #  class: Python owns every C++ QLocaleData::NumericData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QLocaleData11NumericDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def zeroWidth(self) -> int:
      """
      Calls Qt's 'qsizetype QLocaleData::NumericData::zeroWidth() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-numericdata.html#zeroWidth
      """
      #  qsizetype QLocaleData::NumericData::zeroWidth() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData11NumericData9zeroWidthEv',
      )

    @overload(int)
    def digitValue(self, digit: int) -> int:
      """
      Calls Qt's 'qint8 QLocaleData::NumericData::digitValue(char32_t digit)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-numericdata.html#digitValue

      Parameters
      ----------

      digit : int
        Passed on as it is.
      """
      #  qint8 QLocaleData::NumericData::digitValue(char32_t digit) const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData11NumericData10digitValueEDi', digit,
      )

    def fractionalIsGroup(self) -> bool:
      """
      Calls Qt's 'bool QLocaleData::NumericData::fractionalIsGroup() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-numericdata.html#fractionalIsGroup
      """
      #  bool QLocaleData::NumericData::fractionalIsGroup() const
      return self.uglySide.call(
          'ritual_ZNK11QLocaleData11NumericData17fractionalIsGroupEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def setZero(self, zero: str) -> None:
      """
      Calls Qt's 'void QLocaleData::NumericData::setZero(QStringView zero)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlocaledata-numericdata.html#setZero

      Parameters
      ----------

      zero : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QLocaleData::NumericData::setZero(QStringView zero)
      self.uglySide.call(
          'ritual_ZN11QLocaleData11NumericData7setZeroE11QStringView', zero,
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
      Qt's 'QLocaleData::NumericData::NumericData(const QLocaleData *data,
      QLocaleData::NumberMode mode)': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'single_character_data'.
      """
      raise NotImplementedError(
          "'QLocaleData.NumericData.__init__' has no cute function yet. "
          "Qt's 'QLocaleData::NumericData::NumericData(const QLocaleData "
          "*data, QLocaleData::NumberMode mode)': Qt's library has no name "
          "for it, and its code in Qt's source does not compile apart from "
          "its file: use of undeclared identifier 'single_character_data'.")

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

    @staticmethod
    def groupSizes(*__, **_) -> Never:
      """
      Qt's 'const GroupSizes &QLocaleData::NumericData::groupSizes() const':
      gives 'QLocaleData::GroupSizes', which stands beside this class inside
      'QLocaleData' and cannot be named from here.
      """
      raise NotImplementedError(
          "'QLocaleData.NumericData.groupSizes' has no cute function yet. "
          "Qt's 'const GroupSizes &QLocaleData::NumericData::groupSizes() "
          "const': gives 'QLocaleData::GroupSizes', which stands beside "
          "this class inside 'QLocaleData' and cannot be named from here.")

    @staticmethod
    def isValid(*__, **_) -> Never:
      """
      Qt's 'bool QLocaleData::NumericData::isValid(NumberMode mode) const':
      names the enum 'QLocaleData::NumberMode', whose class cannot be named
      here.
      """
      raise NotImplementedError(
          "'QLocaleData.NumericData.isValid' has no cute function yet. Qt's "
          "'bool QLocaleData::NumericData::isValid(NumberMode mode) const': "
          "names the enum 'QLocaleData::NumberMode', whose class cannot be "
          "named here.")

  class ParsingResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLocaleData::ParsingResult: a plain Python object
    standing in front of one C++ QLocaleData::ParsingResult.

    C++ hands a QLocaleData::ParsingResult around as a copy, so every C++
    QLocaleData::ParsingResult behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QLocaleData::ParsingResult yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLocaleData::ParsingResult::~ParsingResult()': the destructor:
      Python removes its C++ QLocaleData::ParsingResult by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QLocaleData::ParsingResult is created at the first use, not by
      'QLocaleData::ParsingResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLocaleData::ParsingResult back gives a copy the
      ritual made for Python, in a new cute QLocaleData::ParsingResult.
    """

    #  The enums Qt writes inside QLocaleData::ParsingResult, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class State(CuteNum):
      """
      The enum 'QLocaleData::ParsingResult::State' of Qt, with the 3 names Qt
      gives in it.
      """

      Invalid = Kee[int](0)
      Intermediate = Kee[int](1)
      Acceptable = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLocaleData::ParsingResult'

    #  Qt's '~QLocaleData::ParsingResult()'. Naming it makes this a value
    #  class: Python owns every C++ QLocaleData::ParsingResult behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QLocaleData13ParsingResultD1Ev'

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
  __qt_class__ = 'QLocaleData'

  #  Qt's '~QLocaleData()'. Naming it makes this a value class: Python owns
  #  every C++ QLocaleData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLocaleDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, NumberMode)
  @overload(str, NumberMode, int)
  @overload(str, NumberMode, int, QLocale.NumberOptions)
  def validateChars(
      self,
      str: str,
      numMode: NumberMode,
      decDigits: int = -1,
      number_options: QLocale.NumberOptions = (
          QLocale.NumberOptions.DefaultNumberOptions),
  ) -> ParsingResult:
    """
    Calls Qt's 'ParsingResult QLocaleData::validateChars(QStringView str,
    NumberMode numMode, int decDigits, QLocale::NumberOptions number_options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#validateChars

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    numMode : NumberMode
      Passed on as its number.

    decDigits : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    number_options : QLocale.NumberOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QLocale.NumberOptions.DefaultNumberOptions.

    Returns
    -------

    ParsingResult
      A new cute QLocaleData::ParsingResult around the copy Qt gave back.
      Python owns it.
    """
    #  ParsingResult QLocaleData::validateChars(QStringView str, NumberMode
    #      numMode, int decDigits, QLocale::NumberOptions number_options)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData13validateCharsE11QStringViewNS_10NumberMod'
        'eEi6QFlagsIN7QLocale12NumberOptionEE',
        str, numMode.value, decDigits, number_options.value,
    )
    return QLocaleData.ParsingResult._cuteOwning(address)

  def id(self) -> QLocaleId:
    """
    Calls Qt's 'QLocaleId QLocaleData::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#id

    Returns
    -------

    QLocaleId
      A new cute QLocaleId around the copy Qt gave back. Python owns it.
    """
    #  QLocaleId QLocaleData::id() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData2idEv')
    from . import QLocaleId
    return QLocaleId._cuteOwning(address)

  def groupSizes(self) -> GroupSizes:
    """
    Calls Qt's 'GroupSizes QLocaleData::groupSizes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#groupSizes

    Returns
    -------

    GroupSizes
      A new cute QLocaleData::GroupSizes around the copy Qt gave back. Python
      owns it.
    """
    #  GroupSizes QLocaleData::groupSizes() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData10groupSizesEv')
    return QLocaleData.GroupSizes._cuteOwning(address)

  def startListPattern(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::startListPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#startListPattern

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::startListPattern() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData16startListPatternEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def midListPattern(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::midListPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#midListPattern

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::midListPattern() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14midListPatternEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def endListPattern(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::endListPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#endListPattern

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::endListPattern() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14endListPatternEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def pairListPattern(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::pairListPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#pairListPattern

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::pairListPattern() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData15pairListPatternEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def listDelimit(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::listDelimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#listDelimit

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::listDelimit() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData11listDelimitEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def decimalSeparator(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::decimalSeparator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#decimalSeparator

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::decimalSeparator() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData16decimalSeparatorEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def groupDelim(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::groupDelim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#groupDelim

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::groupDelim() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData10groupDelimEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def percent(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::percent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#percent

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::percent() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData7percentEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def zero(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::zero() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#zero

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::zero() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData4zeroEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def minus(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::minus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#minus

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::minus() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData5minusEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def plus(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::plus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#plus

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::plus() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData4plusEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def exponential(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::exponential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#exponential

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::exponential() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData11exponentialEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def quoteStart(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::quoteStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#quoteStart

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::quoteStart() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData10quoteStartEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def quoteEnd(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::quoteEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#quoteEnd

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::quoteEnd() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData8quoteEndEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def quoteStartAlternate(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::quoteStartAlternate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#quoteStartAlternate

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::quoteStartAlternate() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData19quoteStartAlternateEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def quoteEndAlternate(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::quoteEndAlternate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#quoteEndAlternate

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::quoteEndAlternate() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData17quoteEndAlternateEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def longDateFormat(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::longDateFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#longDateFormat

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::longDateFormat() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14longDateFormatEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def shortDateFormat(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::shortDateFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#shortDateFormat

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::shortDateFormat() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData15shortDateFormatEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def longTimeFormat(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::longTimeFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#longTimeFormat

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::longTimeFormat() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14longTimeFormatEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def shortTimeFormat(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::shortTimeFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#shortTimeFormat

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::shortTimeFormat() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData15shortTimeFormatEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def longDayNamesStandalone(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::longDayNamesStandalone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#longDayNamesStandalone

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::longDayNamesStandalone() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData22longDayNamesStandaloneEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def longDayNames(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::longDayNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#longDayNames

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::longDayNames() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData12longDayNamesEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def shortDayNamesStandalone(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::shortDayNamesStandalone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#shortDayNamesStandalone

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::shortDayNamesStandalone() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData23shortDayNamesStandaloneEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def shortDayNames(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::shortDayNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#shortDayNames

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::shortDayNames() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData13shortDayNamesEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def narrowDayNamesStandalone(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::narrowDayNamesStandalone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#narrowDayNamesStandalone

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::narrowDayNamesStandalone() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData24narrowDayNamesStandaloneEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def narrowDayNames(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::narrowDayNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#narrowDayNames

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::narrowDayNames() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14narrowDayNamesEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def anteMeridiem(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::anteMeridiem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#anteMeridiem

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::anteMeridiem() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData12anteMeridiemEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def postMeridiem(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::postMeridiem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#postMeridiem

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::postMeridiem() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData12postMeridiemEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def byteCount(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::byteCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#byteCount

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::byteCount() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData9byteCountEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def byteAmountSI(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::byteAmountSI() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#byteAmountSI

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::byteAmountSI() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData12byteAmountSIEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def byteAmountIEC(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::byteAmountIEC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#byteAmountIEC

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::byteAmountIEC() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData13byteAmountIECEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def currencySymbol(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::currencySymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#currencySymbol

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::currencySymbol() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14currencySymbolEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def currencyDisplayName(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::currencyDisplayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#currencyDisplayName

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::currencyDisplayName() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData19currencyDisplayNameEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def currencyFormat(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::currencyFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#currencyFormat

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::currencyFormat() const
    address = self.uglySide.call('ritual_ZNK11QLocaleData14currencyFormatEv')
    return QLocaleData.DataRange._cuteOwning(address)

  def currencyFormatNegative(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::currencyFormatNegative() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocaledata.html#currencyFormatNegative

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::currencyFormatNegative() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData22currencyFormatNegativeEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def endonymLanguage(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::endonymLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#endonymLanguage

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::endonymLanguage() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData15endonymLanguageEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

  def endonymTerritory(self) -> DataRange:
    """
    Calls Qt's 'DataRange QLocaleData::endonymTerritory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocaledata.html#endonymTerritory

    Returns
    -------

    DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  DataRange QLocaleData::endonymTerritory() const
    address = self.uglySide.call(
        'ritual_ZNK11QLocaleData16endonymTerritoryEv',
    )
    return QLocaleData.DataRange._cuteOwning(address)

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
  def allLocaleDataRows(*__, **_) -> Never:
    """
    Qt's 'bool QLocaleData::allLocaleDataRows(bool (*)(qsizetype, const
    QLocaleData &) check)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'locale_data'.
    """
    raise NotImplementedError(
        "'QLocaleData.allLocaleDataRows' has no cute function yet. Qt's "
        "'bool QLocaleData::allLocaleDataRows(bool (*)(qsizetype, const "
        "QLocaleData &) check)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'locale_data'.")

  @staticmethod
  def applyIntegerFormatting(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::applyIntegerFormatting(QString &&numStr, bool
    negative, int precision, int base, int width, unsigned int flags) const':
    leans on 'QLocaleData::negativeSign() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.applyIntegerFormatting' has no cute function yet. "
        "Qt's 'QString QLocaleData::applyIntegerFormatting(QString "
        "&&numStr, bool negative, int precision, int base, int width, "
        "unsigned int flags) const': leans on 'QLocaleData::negativeSign() "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def bytearrayToLongLong(*__, **_) -> Never:
    """
    Qt's 'QSimpleParsedNumber<qint64>
    QLocaleData::bytearrayToLongLong(QByteArrayView num, int base)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLocaleData.bytearrayToLongLong' has no cute function yet. Qt's "
        "'QSimpleParsedNumber<qint64> "
        "QLocaleData::bytearrayToLongLong(QByteArrayView num, int base)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bytearrayToUnsLongLong(*__, **_) -> Never:
    """
    Qt's 'QSimpleParsedNumber<quint64>
    QLocaleData::bytearrayToUnsLongLong(QByteArrayView num, int base)': leans
    on 'qstrntoull(char const*, long long, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.bytearrayToUnsLongLong' has no cute function yet. "
        "Qt's 'QSimpleParsedNumber<quint64> "
        "QLocaleData::bytearrayToUnsLongLong(QByteArrayView num, int "
        "base)': leans on 'qstrntoull(char const*, long long, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def c(*__, **_) -> Never:
    """
    Qt's 'const QLocaleData *QLocaleData::c()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'locale_index'.
    """
    raise NotImplementedError(
        "'QLocaleData.c' has no cute function yet. Qt's 'const QLocaleData "
        "*QLocaleData::c()': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'locale_index'.")

  @staticmethod
  def convertDoubleToFloat(*__, **_) -> Never:
    """
    Qt's 'float QLocaleData::convertDoubleToFloat(double d, bool *ok)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QLocaleData.convertDoubleToFloat' has no cute function yet. Qt's "
        "'float QLocaleData::convertDoubleToFloat(double d, bool *ok)': "
        "takes a number to change where it is.")

  @staticmethod
  def dataForLocaleIndex(*__, **_) -> Never:
    """
    Qt's 'const QLocaleData *QLocaleData::dataForLocaleIndex(qsizetype
    index)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'locale_data_size'.
    """
    raise NotImplementedError(
        "'QLocaleData.dataForLocaleIndex' has no cute function yet. Qt's "
        "'const QLocaleData *QLocaleData::dataForLocaleIndex(qsizetype "
        "index)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'locale_data_size'.")

  @staticmethod
  def decimalForm(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::decimalForm(QString &&digits, int decpt, int
    precision, PrecisionMode pm, bool mustMarkDecimal, bool groupDigits)
    const': leans on 'QLocaleData::decimalPoint() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLocaleData.decimalForm' has no cute function yet. Qt's 'QString "
        "QLocaleData::decimalForm(QString &&digits, int decpt, int "
        "precision, PrecisionMode pm, bool mustMarkDecimal, bool "
        "groupDigits) const': leans on 'QLocaleData::decimalPoint() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def decimalPoint(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::decimalPoint() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'localeString'.
    """
    raise NotImplementedError(
        "'QLocaleData.decimalPoint' has no cute function yet. Qt's 'QString "
        "QLocaleData::decimalPoint() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'localeString'.")

  @staticmethod
  def digitSequence(*__, **_) -> Never:
    """
    Qt's 'DigitSequence QLocaleData::digitSequence(QStringView text,
    DigitSequence::Options flags, qsizetype from) const': leans on
    'QLocaleData::NumericData::NumericData(QLocaleData const*,
    QLocaleData::NumberMode)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.digitSequence' has no cute function yet. Qt's "
        "'DigitSequence QLocaleData::digitSequence(QStringView text, "
        "DigitSequence::Options flags, qsizetype from) const': leans on "
        "'QLocaleData::NumericData::NumericData(QLocaleData const*, "
        "QLocaleData::NumberMode)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def doubleToString(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::doubleToString(double d, int precision,
    DoubleForm form, int width, unsigned int flags) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'isAsciiDigit'; did you mean
    'QtMiscUtils::isAsciiDigit'?.
    """
    raise NotImplementedError(
        "'QLocaleData.doubleToString' has no cute function yet. Qt's "
        "'QString QLocaleData::doubleToString(double d, int precision, "
        "DoubleForm form, int width, unsigned int flags) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isAsciiDigit'; did you mean 'QtMiscUtils::isAsciiDigit'?.")

  @staticmethod
  def exponentForm(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::exponentForm(QString &&digits, int decpt, int
    precision, PrecisionMode pm, bool mustMarkDecimal, int minExponentDigits)
    const': leans on 'qulltoa(unsigned long long, int, QStringView)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.exponentForm' has no cute function yet. Qt's 'QString "
        "QLocaleData::exponentForm(QString &&digits, int decpt, int "
        "precision, PrecisionMode pm, bool mustMarkDecimal, int "
        "minExponentDigits) const': leans on 'qulltoa(unsigned long long, "
        "int, QStringView)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def exponentSeparator(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::exponentSeparator() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'single_character_data'.
    """
    raise NotImplementedError(
        "'QLocaleData.exponentSeparator' has no cute function yet. Qt's "
        "'QString QLocaleData::exponentSeparator() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'single_character_data'.")

  @staticmethod
  def findLocaleIndex(*__, **_) -> Never:
    """
    Qt's 'qsizetype QLocaleData::findLocaleIndex(QLocaleId localeId)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'findLocaleIndexById';
    did you mean 'findLocaleIndex'?.
    """
    raise NotImplementedError(
        "'QLocaleData.findLocaleIndex' has no cute function yet. Qt's "
        "'qsizetype QLocaleData::findLocaleIndex(QLocaleId localeId)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'findLocaleIndexById'; did you mean 'findLocaleIndex'?.")

  @staticmethod
  def groupSeparator(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::groupSeparator() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'localeString'.
    """
    raise NotImplementedError(
        "'QLocaleData.groupSeparator' has no cute function yet. Qt's "
        "'QString QLocaleData::groupSeparator() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'localeString'.")

  @staticmethod
  def listSeparator(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::listSeparator() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'single_character_data'.
    """
    raise NotImplementedError(
        "'QLocaleData.listSeparator' has no cute function yet. Qt's "
        "'QString QLocaleData::listSeparator() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'single_character_data'.")

  @staticmethod
  def longLongToString(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::longLongToString(qint64 l, int precision, int
    base, int width, unsigned int flags) const': leans on 'qulltoa(unsigned
    long long, int, QStringView)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.longLongToString' has no cute function yet. Qt's "
        "'QString QLocaleData::longLongToString(qint64 l, int precision, "
        "int base, int width, unsigned int flags) const': leans on "
        "'qulltoa(unsigned long long, int, QStringView)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def negativeSign(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::negativeSign() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'localeString'.
    """
    raise NotImplementedError(
        "'QLocaleData.negativeSign' has no cute function yet. Qt's 'QString "
        "QLocaleData::negativeSign() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'localeString'.")

  @staticmethod
  def numberToCLocale(*__, **_) -> Never:
    """
    Qt's 'bool QLocaleData::numberToCLocale(QStringView s,
    QLocale::NumberOptions number_options, NumberMode mode, CharBuff *result)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'isAsciiDigit'; did you mean 'QtMiscUtils::isAsciiDigit'?.
    """
    raise NotImplementedError(
        "'QLocaleData.numberToCLocale' has no cute function yet. Qt's 'bool "
        "QLocaleData::numberToCLocale(QStringView s, QLocale::NumberOptions "
        "number_options, NumberMode mode, CharBuff *result) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isAsciiDigit'; did you mean 'QtMiscUtils::isAsciiDigit'?.")

  @staticmethod
  def percentSign(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::percentSign() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'single_character_data'.
    """
    raise NotImplementedError(
        "'QLocaleData.percentSign' has no cute function yet. Qt's 'QString "
        "QLocaleData::percentSign() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'single_character_data'.")

  @staticmethod
  def positiveSign(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::positiveSign() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'localeString'.
    """
    raise NotImplementedError(
        "'QLocaleData.positiveSign' has no cute function yet. Qt's 'QString "
        "QLocaleData::positiveSign() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'localeString'.")

  @staticmethod
  def signPrefix(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::signPrefix(bool negative, unsigned int flags)
    const': leans on 'QLocaleData::negativeSign() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLocaleData.signPrefix' has no cute function yet. Qt's 'QString "
        "QLocaleData::signPrefix(bool negative, unsigned int flags) const': "
        "leans on 'QLocaleData::negativeSign() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def stringToDouble(*__, **_) -> Never:
    """
    Qt's 'double QLocaleData::stringToDouble(QStringView str, bool *ok,
    QLocale::NumberOptions options) const': leans on 'qt_asciiToDouble(char
    const*, long long, StrayCharacterMode)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.stringToDouble' has no cute function yet. Qt's "
        "'double QLocaleData::stringToDouble(QStringView str, bool *ok, "
        "QLocale::NumberOptions options) const': leans on "
        "'qt_asciiToDouble(char const*, long long, StrayCharacterMode)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def stringToLongLong(*__, **_) -> Never:
    """
    Qt's 'QSimpleParsedNumber<qint64>
    QLocaleData::stringToLongLong(QStringView str, int base,
    QLocale::NumberOptions options) const': leans on
    'QLocaleData::numberToCLocale(QStringView, QFlags<QLocale::NumberOption>,
    QLocaleData::NumberMode, QVarLengthArray<char, 256ll>*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.stringToLongLong' has no cute function yet. Qt's "
        "'QSimpleParsedNumber<qint64> "
        "QLocaleData::stringToLongLong(QStringView str, int base, "
        "QLocale::NumberOptions options) const': leans on "
        "'QLocaleData::numberToCLocale(QStringView, "
        "QFlags<QLocale::NumberOption>, QLocaleData::NumberMode, "
        "QVarLengthArray<char, 256ll>*) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def stringToUnsLongLong(*__, **_) -> Never:
    """
    Qt's 'QSimpleParsedNumber<quint64>
    QLocaleData::stringToUnsLongLong(QStringView str, int base,
    QLocale::NumberOptions options) const': leans on 'qstrntoull(char const*,
    long long, int)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.stringToUnsLongLong' has no cute function yet. Qt's "
        "'QSimpleParsedNumber<quint64> "
        "QLocaleData::stringToUnsLongLong(QStringView str, int base, "
        "QLocale::NumberOptions options) const': leans on 'qstrntoull(char "
        "const*, long long, int)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def unsLongLongToString(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::unsLongLongToString(quint64 l, int precision,
    int base, int width, unsigned int flags) const': leans on
    'qulltoa(unsigned long long, int, QStringView)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocaleData.unsLongLongToString' has no cute function yet. Qt's "
        "'QString QLocaleData::unsLongLongToString(quint64 l, int "
        "precision, int base, int width, unsigned int flags) const': leans "
        "on 'qulltoa(unsigned long long, int, QStringView)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def zeroDigit(*__, **_) -> Never:
    """
    Qt's 'QString QLocaleData::zeroDigit() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'localeString'.
    """
    raise NotImplementedError(
        "'QLocaleData.zeroDigit' has no cute function yet. Qt's 'QString "
        "QLocaleData::zeroDigit() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'localeString'.")

  @staticmethod
  def zeroUcs(*__, **_) -> Never:
    """
    Qt's 'char32_t QLocaleData::zeroUcs() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'systemLocaleData'.
    """
    raise NotImplementedError(
        "'QLocaleData.zeroUcs' has no cute function yet. Qt's 'char32_t "
        "QLocaleData::zeroUcs() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'systemLocaleData'.")
