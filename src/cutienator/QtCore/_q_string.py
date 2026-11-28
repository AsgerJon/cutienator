"""
QString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QArrayData, QChar, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QByteArrayView, QLatin1String, QRegularExpression
  from . import QRegularExpressionMatch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QLatin1String = WAIT['QLatin1String']
  QRegularExpression = WAIT['QRegularExpression']
  QRegularExpressionMatch = WAIT['QRegularExpressionMatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QString(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QString: a plain Python object standing in front of
  one C++ QString.

  C++ hands a QString around as a copy, so every C++ QString behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QString that has a ritual and that Python can call
  so far, 89 names in all: 'maxSize', 'size', 'count', 'length', 'isEmpty',
  'resize', 'resizeForOverwrite', 'truncate', 'chop', 'capacity', 'reserve',
  'squeeze', 'unicode', 'data', 'constData', 'detach', 'isDetached',
  'isSharedWith', 'clear', 'at', '__getitem__', 'front', 'back', 'arg_impl',
  'indexOf', 'lastIndexOf', 'contains', 'section', 'left', 'right', 'mid',
  'first', 'last', 'sliced', 'chopped', 'startsWith', 'endsWith', 'isUpper',
  'isLower', 'leftJustified', 'rightJustified', 'toLower', 'toUpper',
  'toCaseFolded', 'trimmed', 'simplified', 'toHtmlEscaped', '__iadd__',
  'split', 'normalized', 'repeated', 'nullTerminated', 'toLatin1', 'toUtf8',
  'toLocal8Bit', 'fromLatin1', 'fromUtf8', 'fromLocal8Bit', 'fromRawData',
  'compare', 'localeAwareCompare', 'number', 'begin', 'cbegin', 'constBegin',
  'end', 'cend', 'constEnd', 'push_back', 'push_front', 'shrink_to_fit',
  'erase', 'max_size', 'isNull', 'isRightToLeft', 'isValidUtf16',
  'reallocData', 'reallocGrowData', 'compare_helper',
  'localeAwareCompare_helper', 'toLower_helper', 'toUpper_helper',
  'toCaseFolded_helper', 'trimmed_helper', 'simplified_helper',
  'toLatin1_helper', 'toUtf8_helper', 'toLocal8Bit_helper', 'verify'. It can
  be made from Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString::QString(QChar c)': takes in Python what
    'QString::QString(const QChar *unicode, qsizetype size)' takes.
  - Qt's 'QString::QString(const QString &a0)': takes in Python what
    'QString::QString(QStringView sv)' takes.
  - Qt's 'QString::~QString()': the destructor: Python removes its C++
    QString by it, and has no other use for it.
  - Qt's 'QString &QString::operator=(QChar c)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QString &QString::operator=(const QString &a0)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QString &QString::operator=(QLatin1StringView latin1)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QString::QString(QString &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QString &QString::operator=(QString &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'void QString::swap(QString &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QString &QString::fill(QChar c, qsizetype size)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::slice(qsizetype pos)': gives a type Python has no
    way to take yet.
  - Qt's 'QString &QString::slice(qsizetype pos, qsizetype n)': gives a type
    Python has no way to take yet.
  - Qt's 'const QChar *QString::data() const': takes in Python what 'QChar
    *QString::data()' takes.
  - Qt's 'QChar &QString::operator[](qsizetype i)': gives a type Python has
    no way to take yet.
  - Qt's 'QChar &QString::front()': gives a type Python has no way to take
    yet.
  - Qt's 'QChar &QString::back()': gives a type Python has no way to take
    yet.
  - Qt's 'QString QString::arg_impl(qulonglong a, int fieldwidth, int base,
    QChar fillChar) const': takes in Python what 'QString
    QString::arg_impl(qlonglong a, int fieldwidth, int base, QChar fillChar)
    const' takes.
  - Qt's 'QString QString::arg_impl(double a, int fieldWidth, char format,
    int precision, QChar fillChar) const': takes a single letter as C has it.
  - Qt's 'QString QString::vasprintf(const char *format, __va_list_tag *ap)':
    names '__va_list_tag', which has no cute class yet.
  - Qt's 'qsizetype QString::indexOf(QStringView s, qsizetype from,
    Qt::CaseSensitivity cs) const': takes in Python what 'qsizetype
    QString::indexOf(const QString &s, qsizetype from, Qt::CaseSensitivity
    cs) const' takes.
  - Qt's 'qsizetype QString::lastIndexOf(QStringView s, Qt::CaseSensitivity
    cs) const': takes in Python what 'qsizetype QString::lastIndexOf(const
    QString &s, Qt::CaseSensitivity cs) const' takes.
  - Qt's 'qsizetype QString::lastIndexOf(QStringView s, qsizetype from,
    Qt::CaseSensitivity cs) const': takes in Python what 'qsizetype
    QString::lastIndexOf(const QString &s, qsizetype from,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'bool QString::contains(QStringView s, Qt::CaseSensitivity cs)
    const': takes in Python what 'bool QString::contains(const QString &s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'qsizetype QString::count(QStringView s, Qt::CaseSensitivity cs)
    const': takes in Python what 'qsizetype QString::count(const QString &s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'bool QString::startsWith(QStringView s, Qt::CaseSensitivity cs)
    const': takes in Python what 'bool QString::startsWith(const QString &s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'bool QString::endsWith(QStringView s, Qt::CaseSensitivity cs)
    const': takes in Python what 'bool QString::endsWith(const QString &s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'QString &QString::insert(qsizetype i, QChar c)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, const QChar *uc, qsizetype
    len)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, const QString &s)': gives a
    type Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, QStringView v)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, QLatin1StringView s)': gives
    a type Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, QUtf8StringView s)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QString &QString::append(QChar c)': gives a type Python has no way
    to take yet.
  - Qt's 'QString &QString::append(const QChar *uc, qsizetype len)': gives a
    type Python has no way to take yet.
  - Qt's 'QString &QString::append(const QString &s)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::append(QStringView v)': gives a type Python has
    no way to take yet.
  - Qt's 'QString &QString::append(QLatin1StringView s)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::append(QUtf8StringView s)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString &QString::prepend(QChar c)': gives a type Python has no way
    to take yet.
  - Qt's 'QString &QString::prepend(const QChar *uc, qsizetype len)': gives a
    type Python has no way to take yet.
  - Qt's 'QString &QString::prepend(const QString &s)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::prepend(QStringView v)': gives a type Python has
    no way to take yet.
  - Qt's 'QString &QString::prepend(QLatin1StringView s)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::prepend(QUtf8StringView s)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString &QString::assign(QAnyStringView s)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::assign(qsizetype n, QChar c)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::operator+=(QStringView v)': takes in Python what
    'QString &QString::operator+=(const QString &s)' takes.
  - Qt's 'QString &QString::operator+=(QUtf8StringView s)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QString &QString::remove(qsizetype i, qsizetype len)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::remove(QChar c, Qt::CaseSensitivity cs)': gives a
    type Python has no way to take yet.
  - Qt's 'QString &QString::remove(QLatin1StringView s, Qt::CaseSensitivity
    cs)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::remove(const QString &s, Qt::CaseSensitivity
    cs)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::removeAt(qsizetype pos)': gives a type Python has
    no way to take yet.
  - Qt's 'QString &QString::removeFirst()': gives a type Python has no way to
    take yet.
  - Qt's 'QString &QString::removeLast()': gives a type Python has no way to
    take yet.
  - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, QChar
    after)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, const QChar
    *s, qsizetype slen)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, const QString
    &after)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(QChar before, QChar after,
    Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(const QChar *before, qsizetype blen,
    const QChar *after, qsizetype alen, Qt::CaseSensitivity cs)': gives a
    type Python has no way to take yet.
  - Qt's 'QString &QString::replace(QLatin1StringView before,
    QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::replace(QLatin1StringView before, const QString
    &after, Qt::CaseSensitivity cs)': gives a type Python has no way to take
    yet.
  - Qt's 'QString &QString::replace(const QString &before, QLatin1StringView
    after, Qt::CaseSensitivity cs)': gives a type Python has no way to take
    yet.
  - Qt's 'QString &QString::replace(const QString &before, const QString
    &after, Qt::CaseSensitivity cs)': gives a type Python has no way to take
    yet.
  - Qt's 'QString &QString::replace(QChar c, const QString &after,
    Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(QChar c, QLatin1StringView after,
    Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::replace(const QRegularExpression &re, const
    QString &after)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::remove(const QRegularExpression &re)': gives a
    type Python has no way to take yet.
  - Qt's 'const ushort *QString::utf16() const': gives 'unsigned short',
    which has no cute class yet.
  - Qt's 'QString &QString::nullTerminate()': gives a type Python has no way
    to take yet.
  - Qt's 'QList<uint> QString::toUcs4() const': gives a type Python has no
    way to take yet.
  - Qt's 'QString QString::fromUtf16(const char16_t *a0, qsizetype size)':
    names 'char16_t', which has no cute class yet.
  - Qt's 'QString QString::fromUcs4(const char32_t *a0, qsizetype size)':
    names 'char32_t', which has no cute class yet.
  - Qt's 'QString QString::fromRawData(const char16_t *unicode, qsizetype
    size)': names 'char16_t', which has no cute class yet.
  - Qt's 'QString QString::fromUtf16(const ushort *str, qsizetype size)':
    names 'ushort', which has no cute class yet.
  - Qt's 'QString QString::fromUcs4(const uint *str, qsizetype size)': names
    'uint', which has no cute class yet.
  - Qt's 'qsizetype QString::toWCharArray(wchar_t *array) const': names
    'wchar_t', which has no cute class yet.
  - Qt's 'QString QString::fromWCharArray(const wchar_t *string, qsizetype
    size)': names 'wchar_t', which has no cute class yet.
  - Qt's 'QString &QString::setRawData(const QChar *unicode, qsizetype
    size)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::setUnicode(const QChar *unicode, qsizetype
    size)': gives a type Python has no way to take yet.
  - Qt's 'QString &QString::setUtf16(const char16_t *utf16, qsizetype size)':
    names 'char16_t', which has no cute class yet.
  - Qt's 'int QString::compare(QStringView s, Qt::CaseSensitivity cs) const':
    takes in Python what 'int QString::compare(const QString &s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'int QString::compare(const QString &s1, QStringView s2,
    Qt::CaseSensitivity cs)': takes in Python what 'int
    QString::compare(const QString &s1, const QString &s2,
    Qt::CaseSensitivity cs)' takes.
  - Qt's 'int QString::compare(QStringView s1, const QString &s2,
    Qt::CaseSensitivity cs)': takes in Python what 'int
    QString::compare(const QString &s1, const QString &s2,
    Qt::CaseSensitivity cs)' takes.
  - Qt's 'int QString::localeAwareCompare(QStringView s) const': takes in
    Python what 'int QString::localeAwareCompare(const QString &s) const'
    takes.
  - Qt's 'int QString::localeAwareCompare(QStringView s1, QStringView s2)':
    takes in Python what 'int QString::localeAwareCompare(const QString &s1,
    const QString &s2)' takes.
  - Qt's 'short QString::toShort(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'ushort QString::toUShort(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'int QString::toInt(bool *ok, int base) const': takes a number to
    change where it is.
  - Qt's 'uint QString::toUInt(bool *ok, int base) const': takes a number to
    change where it is.
  - Qt's 'long QString::toLong(bool *ok, int base) const': takes a number to
    change where it is.
  - Qt's 'ulong QString::toULong(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'qlonglong QString::toLongLong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qulonglong QString::toULongLong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'float QString::toFloat(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'double QString::toDouble(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'QString &QString::setNum(short a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(ushort a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(int a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(uint a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(long a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(ulong a0, int base)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::setNum(qlonglong a0, int base)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::setNum(qulonglong a0, int base)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::setNum(float a0, char format, int precision)':
    takes a single letter as C has it.
  - Qt's 'QString &QString::setNum(double a0, char format, int precision)':
    takes a single letter as C has it.
  - Qt's 'QString QString::number(uint a0, int base)': takes in Python what
    'QString QString::number(int a0, int base)' takes.
  - Qt's 'QString QString::number(long a0, int base)': takes in Python what
    'QString QString::number(int a0, int base)' takes.
  - Qt's 'QString QString::number(ulong a0, int base)': takes in Python what
    'QString QString::number(int a0, int base)' takes.
  - Qt's 'QString QString::number(qlonglong a0, int base)': takes in Python
    what 'QString QString::number(int a0, int base)' takes.
  - Qt's 'QString QString::number(qulonglong a0, int base)': takes in Python
    what 'QString QString::number(int a0, int base)' takes.
  - Qt's 'QString QString::number(double a0, char format, int precision)':
    takes a single letter as C has it.
  - Qt's 'bool operator==(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const QLatin1StringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QLatin1StringView &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator!=(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator<(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator>(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator<=(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator>=(const QString &lhs, const std::nullptr_t &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator==(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator!=(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator<(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator>(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator<=(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator>=(const std::nullptr_t &lhs, const QString &rhs)': an
    operator Python has no name for.
  - Qt's 'bool operator==(const QString &lhs, const char16_t *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const char16_t *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const char16_t *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const char16_t *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const char16_t *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const char16_t *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const char16_t *const &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const char16_t *const &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const char16_t *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const char16_t *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const char16_t *const &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const char16_t *const &lhs, const QString &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const QChar &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator==(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator!=(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator<(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator>(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator<=(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'bool operator>=(const QChar &lhs, const QString &rhs)': an operator
    between other classes, written inside this one.
  - Qt's 'QString::QString(const char *ch)': takes in Python what
    'QString::QString(const QChar *unicode, qsizetype size)' takes.
  - Qt's 'QString &QString::operator=(const char *ch)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QString &QString::operator=(const QByteArray &a)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QString &QString::prepend(const char *s)': gives a type Python has
    no way to take yet.
  - Qt's 'QString &QString::prepend(const QByteArray &s)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::append(const char *s)': gives a type Python has
    no way to take yet.
  - Qt's 'QString &QString::append(const QByteArray &s)': gives a type Python
    has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, const char *s)': gives a type
    Python has no way to take yet.
  - Qt's 'QString &QString::insert(qsizetype i, const QByteArray &s)': gives
    a type Python has no way to take yet.
  - Qt's 'bool operator==(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const QByteArrayView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QByteArrayView &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QByteArray &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QString &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const char *const &lhs, const QString &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'const_iterator QString::begin() const': takes in Python what
    'iterator QString::begin()' takes.
  - Qt's 'const_iterator QString::end() const': takes in Python what
    'iterator QString::end()' takes.
  - Qt's 'reverse_iterator QString::rbegin()': gives a type Python has no way
    to take yet.
  - Qt's 'reverse_iterator QString::rend()': gives a type Python has no way
    to take yet.
  - Qt's 'const_reverse_iterator QString::rbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QString::rend() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_reverse_iterator QString::crbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QString::crend() const': gives a type Python
    has no way to take yet.
  - Qt's 'QString QString::fromStdString(const std::string &s)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::string QString::toStdString() const': gives a type Python has
    no way to take yet.
  - Qt's 'QString QString::fromStdWString(const std::wstring &s)': takes a
    type Python has no way to hand over yet.
  - Qt's 'std::wstring QString::toStdWString() const': gives a type Python
    has no way to take yet.
  - Qt's 'QString QString::fromStdU16String(const std::u16string &s)': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::u16string QString::toStdU16String() const': gives a type
    Python has no way to take yet.
  - Qt's 'QString QString::fromStdU32String(const std::u32string &s)': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::u32string QString::toStdU32String() const': gives a type
    Python has no way to take yet.
  - Qt's 'std::u16string_view QString::operator basic_string_view() const':
    an operator Python has no name for.
  - Qt's 'QString::QString(DataPointer &&dd)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QString &QString::assign_helper(const char32_t *data, qsizetype
    len)': names 'char32_t', which has no cute class yet.
  - Qt's 'QString QString::sliced_helper(QString &str, qsizetype pos,
    qsizetype n)': takes a type Python has no way to hand over yet.
  - Qt's 'QString QString::toLower_helper(QString &str)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString QString::toUpper_helper(QString &str)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString QString::toCaseFolded_helper(QString &str)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QString QString::trimmed_helper(QString &str)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString QString::simplified_helper(QString &str)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QByteArray QString::toLatin1_helper_inplace(QString &a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'qsizetype QString::toUcs4_helper(const char16_t *uc, qsizetype
    length, char32_t *out)': names 'char16_t', which has no cute class yet.
  - Qt's 'qlonglong QString::toIntegral_helper(QStringView string, bool *ok,
    int base)': takes a number to change where it is.
  - Qt's 'qulonglong QString::toIntegral_helper(QStringView string, bool *ok,
    uint base)': takes a number to change where it is.
  - Qt's 'DataPointer &QString::data_ptr()': gives a type Python has no way
    to take yet.
  - Qt's 'const DataPointer &QString::data_ptr() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  36 of the 417 functions Qt declares: 18 a template; 17 not a gap; 1 takes
  any number of arguments.

  What to expect
  --------------

  - The C++ QString is created at the first use, not by 'QString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QString back gives a copy the ritual made for Python,
    in a new cute QString.
  - Each name of Qt's QString that has no cute function yet, 'append', 'arg',
    'asprintf', 'assign', 'assign_helper', 'assign_helper_char8', 'crbegin',
    'crend', 'data_ptr', 'fill', 'fromStdString', 'fromStdU16String',
    'fromStdU32String', 'fromStdWString', 'fromUcs4', 'fromUtf16',
    'fromWCharArray', 'insert', 'nullTerminate', 'prepend', 'rbegin',
    'remove', 'removeAt', 'removeFirst', 'removeIf', 'removeIf_helper',
    'removeLast', 'rend', 'replace', 'setNum', 'setRawData', 'setUnicode',
    'setUtf16', 'slice', 'sliced_helper', 'swap', 'toDouble', 'toFloat',
    'toInt', 'toIntegral_helper', 'toLatin1_helper_inplace', 'toLong',
    'toLongLong', 'toShort', 'toStdString', 'toStdU16String',
    'toStdU32String', 'toStdWString', 'toUInt', 'toULong', 'toULongLong',
    'toUShort', 'toUcs4', 'toUcs4_helper', 'toWCharArray', 'tokenize',
    'utf16', 'vasprintf', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QString, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class NormalizationForm(CuteNum):
    """
    The enum 'QString::NormalizationForm' of Qt, with the 4 names Qt gives in
    it.
    """

    NormalizationForm_D = Kee[int](0)
    NormalizationForm_C = Kee[int](1)
    NormalizationForm_KD = Kee[int](2)
    NormalizationForm_KC = Kee[int](3)

  class SectionFlag(CuteFlags):
    """
    The flags enum 'QString::SectionFlag' of Qt, with the 5 names Qt gives in
    it. Qt names the type of its combinations 'QString::SectionFlags'.
    """

    SectionDefault = 0x0
    SectionSkipEmpty = 0x1
    SectionIncludeLeadingSep = 0x2
    SectionIncludeTrailingSep = 0x4
    SectionCaseInsensitiveSeps = 0x8

  SectionFlags = SectionFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxSize() -> int:
    """
    Calls Qt's 'qsizetype QString::maxSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#maxSize
    """
    #  qsizetype QString::maxSize()
    return Rituals.call('ritual_ZN7QString7maxSizeEv')

  @staticmethod
  @overload(QByteArrayView)
  def fromLatin1(ba: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QString::fromLatin1(QByteArrayView ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromLatin1

    Parameters
    ----------

    ba : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromLatin1(QByteArrayView ba)
    return Rituals.call(
        'ritual_ZN7QString10fromLatin1E14QByteArrayView',
        CuteMixin._valueOf(ba),
    )

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def fromLatin1(str: Optional[str], size: int) -> str:
    """
    Calls Qt's 'QString QString::fromLatin1(const char *str, qsizetype
    size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromLatin1

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromLatin1(const char *str, qsizetype size)
    return Rituals.call(
        'ritual_ZN7QString10fromLatin1EPKcx', CuteMixin._bytesOf(str), size,
    )

  @staticmethod
  @overload(QByteArrayView)
  def fromUtf8(utf8: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QString::fromUtf8(QByteArrayView utf8)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromUtf8

    Parameters
    ----------

    utf8 : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromUtf8(QByteArrayView utf8)
    return Rituals.call(
        'ritual_ZN7QString8fromUtf8E14QByteArrayView',
        CuteMixin._valueOf(utf8),
    )

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def fromUtf8(utf8: Optional[str], size: int) -> str:
    """
    Calls Qt's 'QString QString::fromUtf8(const char *utf8, qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromUtf8

    Parameters
    ----------

    utf8 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromUtf8(const char *utf8, qsizetype size)
    return Rituals.call(
        'ritual_ZN7QString8fromUtf8EPKcx', CuteMixin._bytesOf(utf8), size,
    )

  @staticmethod
  @overload(QByteArrayView)
  def fromLocal8Bit(ba: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QString::fromLocal8Bit(QByteArrayView ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromLocal8Bit

    Parameters
    ----------

    ba : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromLocal8Bit(QByteArrayView ba)
    return Rituals.call(
        'ritual_ZN7QString13fromLocal8BitE14QByteArrayView',
        CuteMixin._valueOf(ba),
    )

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def fromLocal8Bit(str: Optional[str], size: int) -> str:
    """
    Calls Qt's 'QString QString::fromLocal8Bit(const char *str, qsizetype
    size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromLocal8Bit

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromLocal8Bit(const char *str, qsizetype size)
    return Rituals.call(
        'ritual_ZN7QString13fromLocal8BitEPKcx',
        CuteMixin._bytesOf(str), size,
    )

  @staticmethod
  @overload(QChar, int)
  @overload(NoneType, int)
  def fromRawData(a0: Optional[QChar], size: int) -> str:
    """
    Calls Qt's 'QString QString::fromRawData(const QChar *a0, qsizetype
    size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#fromRawData

    Parameters
    ----------

    a0 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::fromRawData(const QChar *a0, qsizetype size)
    return Rituals.call(
        'ritual_ZN7QString11fromRawDataEPK5QCharx',
        CuteMixin._addressOf(a0), size,
    )

  @staticmethod
  @overload(int)
  @overload(int, int)
  def number(a0: int, base: int = 10) -> str:
    """
    Calls Qt's 'QString QString::number(int a0, int base)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#number

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    base : int
      Passed on as it is. May be left out, as in Qt: it is then 10.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::number(int a0, int base)
    return Rituals.call('ritual_ZN7QString6numberEii', a0, base)

  @staticmethod
  @overload(QChar, int, QChar, int)
  @overload(QChar, int, NoneType, int)
  @overload(NoneType, int, QChar, int)
  @overload(NoneType, int, NoneType, int)
  @overload(QChar, int, QChar, int, Qt.CaseSensitivity)
  @overload(QChar, int, NoneType, int, Qt.CaseSensitivity)
  @overload(NoneType, int, QChar, int, Qt.CaseSensitivity)
  @overload(NoneType, int, NoneType, int, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      data2: Optional[QChar],
      length2: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare_helper(const QChar *data1, qsizetype
    length1, const QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    data2 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length2 : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare_helper(const QChar *data1, qsizetype length1,
    #      const QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN7QString14compare_helperEPK5QCharxS2_xN2Qt15CaseSensitivi'
        'tyE',
        CuteMixin._addressOf(data1), length1, CuteMixin._addressOf(data2),
        length2, cs.value,
    )

  @staticmethod
  @overload(QChar, int, str, int)
  @overload(NoneType, int, str, int)
  @overload(QChar, int, str, int, Qt.CaseSensitivity)
  @overload(NoneType, int, str, int, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      data2: Optional[str],
      length2: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare_helper(const QChar *data1, qsizetype
    length1, const char *data2, qsizetype length2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    data2 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length2 : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare_helper(const QChar *data1, qsizetype length1,
    #      const char *data2, qsizetype length2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN7QString14compare_helperEPK5QCharxPKcxN2Qt15CaseSensitivi'
        'tyE',
        CuteMixin._addressOf(data1), length1, CuteMixin._bytesOf(data2),
        length2, cs.value,
    )

  @staticmethod
  @overload(QChar, int, QChar, int)
  @overload(QChar, int, NoneType, int)
  @overload(NoneType, int, QChar, int)
  @overload(NoneType, int, NoneType, int)
  def localeAwareCompare_helper(
      data1: Optional[QChar],
      length1: int,
      data2: Optional[QChar],
      length2: int,
  ) -> int:
    """
    Calls Qt's 'int QString::localeAwareCompare_helper(const QChar *data1,
    qsizetype length1, const QChar *data2, qsizetype length2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstring.html#localeAwareCompare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    data2 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length2 : int
      Passed on as it is.
    """
    #  int QString::localeAwareCompare_helper(const QChar *data1, qsizetype
    #      length1, const QChar *data2, qsizetype length2)
    return Rituals.call(
        'ritual_ZN7QString25localeAwareCompare_helperEPK5QCharxS2_x',
        CuteMixin._addressOf(data1), length1, CuteMixin._addressOf(data2),
        length2,
    )

  @staticmethod
  @overload(str)
  def toLower_helper(str: str) -> str:
    """
    Calls Qt's 'QString QString::toLower_helper(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLower_helper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toLower_helper(const QString &str)
    return Rituals.call('ritual_ZN7QString14toLower_helperERKS_', str)

  @staticmethod
  @overload(str)
  def toUpper_helper(str: str) -> str:
    """
    Calls Qt's 'QString QString::toUpper_helper(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toUpper_helper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toUpper_helper(const QString &str)
    return Rituals.call('ritual_ZN7QString14toUpper_helperERKS_', str)

  @staticmethod
  @overload(str)
  def toCaseFolded_helper(str: str) -> str:
    """
    Calls Qt's 'QString QString::toCaseFolded_helper(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toCaseFolded_helper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toCaseFolded_helper(const QString &str)
    return Rituals.call('ritual_ZN7QString19toCaseFolded_helperERKS_', str)

  @staticmethod
  @overload(str)
  def trimmed_helper(str: str) -> str:
    """
    Calls Qt's 'QString QString::trimmed_helper(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#trimmed_helper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::trimmed_helper(const QString &str)
    return Rituals.call('ritual_ZN7QString14trimmed_helperERKS_', str)

  @staticmethod
  @overload(str)
  def simplified_helper(str: str) -> str:
    """
    Calls Qt's 'QString QString::simplified_helper(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#simplified_helper

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::simplified_helper(const QString &str)
    return Rituals.call('ritual_ZN7QString17simplified_helperERKS_', str)

  @staticmethod
  @overload(str)
  def toLatin1_helper(a0: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toLatin1_helper(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLatin1_helper

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toLatin1_helper(const QString &a0)
    address = Rituals.call('ritual_ZN7QString15toLatin1_helperERKS_', a0)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str)
  def toUtf8_helper(a0: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toUtf8_helper(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toUtf8_helper

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toUtf8_helper(const QString &a0)
    address = Rituals.call('ritual_ZN7QString13toUtf8_helperERKS_', a0)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QChar, int)
  @overload(NoneType, int)
  def toLocal8Bit_helper(data: Optional[QChar], size: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toLocal8Bit_helper(const QChar *data,
    qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLocal8Bit_helper

    Parameters
    ----------

    data : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toLocal8Bit_helper(const QChar *data, qsizetype
    #      size)
    address = Rituals.call(
        'ritual_ZN7QString18toLocal8Bit_helperEPK5QCharx',
        CuteMixin._addressOf(data), size,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QString'

  #  Qt's '~QString()'. Naming it makes this a value class: Python owns every
  #  C++ QString behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QStringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QString::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#size
    """
    #  qsizetype QString::size() const
    return self.uglySide.call('ritual_ZNK7QString4sizeEv')

  @overload()
  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QString::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#count
    """
    #  qsizetype QString::count() const
    return self.uglySide.call('ritual_ZNK7QString5countEv')

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def count(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::count(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#count

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::count(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString5countE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def count(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::count(const QString &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#count

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::count(const QString &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString5countERKS_N2Qt15CaseSensitivityE', s, cs.value,
    )

  @overload(QRegularExpression)
  def count(self, re: QRegularExpression) -> int:
    """
    Calls Qt's 'qsizetype QString::count(const QRegularExpression &re)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#count

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  qsizetype QString::count(const QRegularExpression &re) const
    return self.uglySide.call(
        'ritual_ZNK7QString5countERK18QRegularExpression', self._valueOf(re),
    )

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QString::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#length
    """
    #  qsizetype QString::length() const
    return self.uglySide.call('ritual_ZNK7QString6lengthEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QString::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isEmpty
    """
    #  bool QString::isEmpty() const
    return self.uglySide.call('ritual_ZNK7QString7isEmptyEv')

  def capacity(self) -> int:
    """
    Calls Qt's 'qsizetype QString::capacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#capacity
    """
    #  qsizetype QString::capacity() const
    return self.uglySide.call('ritual_ZNK7QString8capacityEv')

  def unicode(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QString::unicode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#unicode

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QString::unicode() const
    address = self.uglySide.call('ritual_ZNK7QString7unicodeEv')
    return QChar._cuteAt(address)

  def constData(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QString::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#constData

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QString::constData() const
    address = self.uglySide.call('ritual_ZNK7QString9constDataEv')
    return QChar._cuteAt(address)

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QString::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isDetached
    """
    #  bool QString::isDetached() const
    return self.uglySide.call('ritual_ZNK7QString10isDetachedEv')

  @overload(str)
  def isSharedWith(self, other: str) -> bool:
    """
    Calls Qt's 'bool QString::isSharedWith(const QString &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isSharedWith

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QString::isSharedWith(const QString &other) const
    return self.uglySide.call('ritual_ZNK7QString12isSharedWithERKS_', other)

  @overload(int)
  def at(self, i: int) -> QChar:
    """
    Calls Qt's 'const QChar QString::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  const QChar QString::at(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK7QString2atEx', i)
    return QChar._cuteOwning(address)

  def front(self) -> QChar:
    """
    Calls Qt's 'QChar QString::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#front

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QString::front() const
    address = self.uglySide.call('ritual_ZNK7QString5frontEv')
    return QChar._cuteOwning(address)

  def back(self) -> QChar:
    """
    Calls Qt's 'QChar QString::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#back

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QString::back() const
    address = self.uglySide.call('ritual_ZNK7QString4backEv')
    return QChar._cuteOwning(address)

  @overload(int, int, int, QChar)
  def arg_impl(
      self,
      a: int,
      fieldwidth: int,
      base: int,
      fillChar: QChar,
  ) -> str:
    """
    Calls Qt's 'QString QString::arg_impl(qlonglong a, int fieldwidth, int
    base, QChar fillChar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#arg_impl

    Parameters
    ----------

    a : int
      Passed on as it is.

    fieldwidth : int
      Passed on as it is.

    base : int
      Passed on as it is.

    fillChar : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::arg_impl(qlonglong a, int fieldwidth, int base, QChar
    #      fillChar) const
    return self.uglySide.call(
        'ritual_ZNK7QString8arg_implExii5QChar',
        a, fieldwidth, base, self._valueOf(fillChar),
    )

  @overload(str, int, QChar)
  def arg_impl(self, a: str, fieldWidth: int, fillChar: QChar) -> str:
    """
    Calls Qt's 'QString QString::arg_impl(QAnyStringView a, int fieldWidth,
    QChar fillChar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#arg_impl

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    fieldWidth : int
      Passed on as it is.

    fillChar : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::arg_impl(QAnyStringView a, int fieldWidth, QChar
    #      fillChar) const
    return self.uglySide.call(
        'ritual_ZNK7QString8arg_implE14QAnyStringViewi5QChar',
        a, fieldWidth, self._valueOf(fillChar),
    )

  @overload(QChar)
  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      c: QChar,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::indexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#indexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::indexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString7indexOfE5QCharxN2Qt15CaseSensitivityE',
        self._valueOf(c), from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      s: QLatin1String,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::indexOf(QLatin1StringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#indexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::indexOf(QLatin1StringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString7indexOfE13QLatin1StringxN2Qt15CaseSensitivityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      s: str,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::indexOf(const QString &s, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#indexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::indexOf(const QString &s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString7indexOfERKS_xN2Qt15CaseSensitivityE',
        s, from_, cs.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, QRegularExpressionMatch)
  @overload(QRegularExpression, int, NoneType)
  def indexOf(
      self,
      re: QRegularExpression,
      from_: int = 0,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::indexOf(const QRegularExpression &re,
    qsizetype from, QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#indexOf

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qsizetype QString::indexOf(const QRegularExpression &re, qsizetype
    #      from, QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK7QString7indexOfERK18QRegularExpressionxP23QRegularExpre'
        'ssionMatch',
        self._valueOf(re), from_, self._addressOf(rmatch),
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(QChar c, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      c: QChar,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfE5QCharxN2Qt15CaseSensitivityE',
        self._valueOf(c), from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(QLatin1StringView s,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfE13QLatin1StringN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(s), cs.value,
    )

  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(QLatin1StringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(QLatin1StringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfE13QLatin1StringxN2Qt15CaseSensitiv'
        'ityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(const QString &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(const QString &s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfERKS_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: str,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(const QString &s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QString::lastIndexOf(const QString &s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfERKS_xN2Qt15CaseSensitivityE',
        s, from_, cs.value,
    )

  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, QRegularExpressionMatch)
  @overload(QRegularExpression, int, NoneType)
  def lastIndexOf(
      self,
      re: QRegularExpression,
      from_: int,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> int:
    """
    Calls Qt's 'qsizetype QString::lastIndexOf(const QRegularExpression &re,
    qsizetype from, QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#lastIndexOf

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    from_ : int
      Passed on as it is.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qsizetype QString::lastIndexOf(const QRegularExpression &re, qsizetype
    #      from, QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK7QString11lastIndexOfERK18QRegularExpressionxP23QRegular'
        'ExpressionMatch',
        self._valueOf(re), from_, self._addressOf(rmatch),
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def contains(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::contains(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#contains

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::contains(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString8containsE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def contains(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::contains(const QString &s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#contains

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::contains(const QString &s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString8containsERKS_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def contains(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::contains(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#contains

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::contains(QLatin1StringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString8containsE13QLatin1StringN2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, QRegularExpressionMatch)
  @overload(QRegularExpression, NoneType)
  def contains(
      self,
      re: QRegularExpression,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QString::contains(const QRegularExpression &re,
    QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#contains

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QString::contains(const QRegularExpression &re,
    #      QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK7QString8containsERK18QRegularExpressionP23QRegularExpre'
        'ssionMatch',
        self._valueOf(re), self._addressOf(rmatch),
    )

  @overload(QChar, int)
  @overload(QChar, int, int)
  @overload(QChar, int, int, SectionFlags)
  def section(
      self,
      sep: QChar,
      start: int,
      end: int = -1,
      flags: SectionFlags = SectionFlags.SectionDefault,
  ) -> str:
    """
    Calls Qt's 'QString QString::section(QChar sep, qsizetype start,
    qsizetype end, SectionFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#section

    Parameters
    ----------

    sep : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    flags : SectionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SectionFlags.SectionDefault.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::section(QChar sep, qsizetype start, qsizetype end,
    #      SectionFlags flags) const
    return self.uglySide.call(
        'ritual_ZNK7QString7sectionE5QCharxx6QFlagsINS_11SectionFlagEE',
        self._valueOf(sep), start, end, flags.value,
    )

  @overload(str, int)
  @overload(str, int, int)
  @overload(str, int, int, SectionFlags)
  def section(
      self,
      in_sep: str,
      start: int,
      end: int = -1,
      flags: SectionFlags = SectionFlags.SectionDefault,
  ) -> str:
    """
    Calls Qt's 'QString QString::section(const QString &in_sep, qsizetype
    start, qsizetype end, SectionFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#section

    Parameters
    ----------

    in_sep : str
      Passed on as it is: a QString is made of it for the call.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    flags : SectionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SectionFlags.SectionDefault.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::section(const QString &in_sep, qsizetype start,
    #      qsizetype end, SectionFlags flags) const
    return self.uglySide.call(
        'ritual_ZNK7QString7sectionERKS_xx6QFlagsINS_11SectionFlagEE',
        in_sep, start, end, flags.value,
    )

  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, int)
  @overload(QRegularExpression, int, int, SectionFlags)
  def section(
      self,
      re: QRegularExpression,
      start: int,
      end: int = -1,
      flags: SectionFlags = SectionFlags.SectionDefault,
  ) -> str:
    """
    Calls Qt's 'QString QString::section(const QRegularExpression &re,
    qsizetype start, qsizetype end, SectionFlags flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#section

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    flags : SectionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SectionFlags.SectionDefault.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::section(const QRegularExpression &re, qsizetype
    #      start, qsizetype end, SectionFlags flags) const
    return self.uglySide.call(
        'ritual_ZNK7QString7sectionERK18QRegularExpressionxx6QFlagsINS_11Se'
        'ctionFlagEE',
        self._valueOf(re), start, end, flags.value,
    )

  @overload(int)
  def left(self, n: int) -> str:
    """
    Calls Qt's 'QString QString::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::left(qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString4leftEx', n)

  @overload(int)
  def right(self, n: int) -> str:
    """
    Calls Qt's 'QString QString::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::right(qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString5rightEx', n)

  @overload(int)
  @overload(int, int)
  def mid(self, position: int, n: int = -1) -> str:
    """
    Calls Qt's 'QString QString::mid(qsizetype position, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#mid

    Parameters
    ----------

    position : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::mid(qsizetype position, qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString3midExx', position, n)

  @overload(int)
  def first(self, n: int) -> str:
    """
    Calls Qt's 'QString QString::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::first(qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString5firstEx', n)

  @overload(int)
  def last(self, n: int) -> str:
    """
    Calls Qt's 'QString QString::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::last(qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString4lastEx', n)

  @overload(int)
  def sliced(self, pos: int) -> str:
    """
    Calls Qt's 'QString QString::sliced(qsizetype pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::sliced(qsizetype pos) const
    return self.uglySide.call('ritual_ZNKR7QString6slicedEx', pos)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> str:
    """
    Calls Qt's 'QString QString::sliced(qsizetype pos, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::sliced(qsizetype pos, qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString6slicedExx', pos, n)

  @overload(int)
  def chopped(self, n: int) -> str:
    """
    Calls Qt's 'QString QString::chopped(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#chopped

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::chopped(qsizetype n) const
    return self.uglySide.call('ritual_ZNKR7QString7choppedEx', n)

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::startsWith(const QString &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#startsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::startsWith(const QString &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString10startsWithERKS_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::startsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#startsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::startsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString10startsWithE13QLatin1StringN2Qt15CaseSensitivit'
        'yE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def startsWith(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::startsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::startsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString10startsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def endsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::endsWith(const QString &s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#endsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::endsWith(const QString &s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString8endsWithERKS_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def endsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::endsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#endsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::endsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString8endsWithE13QLatin1StringN2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def endsWith(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QString::endsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QString::endsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString8endsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  def isUpper(self) -> bool:
    """
    Calls Qt's 'bool QString::isUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isUpper
    """
    #  bool QString::isUpper() const
    return self.uglySide.call('ritual_ZNK7QString7isUpperEv')

  def isLower(self) -> bool:
    """
    Calls Qt's 'bool QString::isLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isLower
    """
    #  bool QString::isLower() const
    return self.uglySide.call('ritual_ZNK7QString7isLowerEv')

  @overload(int, QChar)
  @overload(int, QChar, bool)
  def leftJustified(
      self,
      width: int,
      fill: QChar,
      trunc: bool = False,
  ) -> str:
    """
    Calls Qt's 'QString QString::leftJustified(qsizetype width, QChar fill,
    bool trunc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#leftJustified

    Parameters
    ----------

    width : int
      Passed on as it is.

    fill : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    trunc : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::leftJustified(qsizetype width, QChar fill, bool
    #      trunc) const
    return self.uglySide.call(
        'ritual_ZNK7QString13leftJustifiedEx5QCharb',
        width, self._valueOf(fill), trunc,
    )

  @overload(int, QChar)
  @overload(int, QChar, bool)
  def rightJustified(
      self,
      width: int,
      fill: QChar,
      trunc: bool = False,
  ) -> str:
    """
    Calls Qt's 'QString QString::rightJustified(qsizetype width, QChar fill,
    bool trunc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#rightJustified

    Parameters
    ----------

    width : int
      Passed on as it is.

    fill : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    trunc : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::rightJustified(qsizetype width, QChar fill, bool
    #      trunc) const
    return self.uglySide.call(
        'ritual_ZNK7QString14rightJustifiedEx5QCharb',
        width, self._valueOf(fill), trunc,
    )

  def toLower(self) -> str:
    """
    Calls Qt's 'QString QString::toLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLower

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toLower() const
    return self.uglySide.call('ritual_ZNKR7QString7toLowerEv')

  def toUpper(self) -> str:
    """
    Calls Qt's 'QString QString::toUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toUpper

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toUpper() const
    return self.uglySide.call('ritual_ZNKR7QString7toUpperEv')

  def toCaseFolded(self) -> str:
    """
    Calls Qt's 'QString QString::toCaseFolded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toCaseFolded

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toCaseFolded() const
    return self.uglySide.call('ritual_ZNKR7QString12toCaseFoldedEv')

  def trimmed(self) -> str:
    """
    Calls Qt's 'QString QString::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#trimmed

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::trimmed() const
    return self.uglySide.call('ritual_ZNKR7QString7trimmedEv')

  def simplified(self) -> str:
    """
    Calls Qt's 'QString QString::simplified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#simplified

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::simplified() const
    return self.uglySide.call('ritual_ZNKR7QString10simplifiedEv')

  def toHtmlEscaped(self) -> str:
    """
    Calls Qt's 'QString QString::toHtmlEscaped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toHtmlEscaped

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::toHtmlEscaped() const
    return self.uglySide.call('ritual_ZNK7QString13toHtmlEscapedEv')

  @overload(str)
  @overload(str, Qt.SplitBehavior)
  @overload(str, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: str,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QString::split(const QString &sep,
    Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#split

    Parameters
    ----------

    sep : str
      Passed on as it is: a QString is made of it for the call.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QString::split(const QString &sep, Qt::SplitBehavior
    #      behavior, Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK7QString5splitERKS_6QFlagsIN2Qt18SplitBehaviorFlagsEENS3'
        '_15CaseSensitivityE',
        sep, behavior.value, cs.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QChar)
  @overload(QChar, Qt.SplitBehavior)
  @overload(QChar, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: QChar,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QString::split(QChar sep, Qt::SplitBehavior
    behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#split

    Parameters
    ----------

    sep : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QString::split(QChar sep, Qt::SplitBehavior behavior,
    #      Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK7QString5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFlagsEEN'
        'S2_15CaseSensitivityE',
        self._valueOf(sep), behavior.value, cs.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QRegularExpression)
  @overload(QRegularExpression, Qt.SplitBehavior)
  def split(
      self,
      sep: QRegularExpression,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QString::split(const QRegularExpression &sep,
    Qt::SplitBehavior behavior) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#split

    Parameters
    ----------

    sep : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QString::split(const QRegularExpression &sep,
    #      Qt::SplitBehavior behavior) const
    address = self.uglySide.call(
        'ritual_ZNK7QString5splitERK18QRegularExpression6QFlagsIN2Qt18Split'
        'BehaviorFlagsEE',
        self._valueOf(sep), behavior.value,
    )
    return QStringList._cuteOwning(address)

  @overload(NormalizationForm)
  @overload(NormalizationForm, QChar.UnicodeVersion)
  def normalized(
      self,
      mode: NormalizationForm,
      version: QChar.UnicodeVersion = (
          QChar.UnicodeVersion.Unicode_Unassigned),
  ) -> str:
    """
    Calls Qt's 'QString QString::normalized(NormalizationForm mode,
    QChar::UnicodeVersion version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#normalized

    Parameters
    ----------

    mode : NormalizationForm
      Passed on as its number.

    version : QChar.UnicodeVersion
      Passed on as its number. May be left out, as in Qt: it is then
      QChar.UnicodeVersion.Unicode_Unassigned.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::normalized(NormalizationForm mode,
    #      QChar::UnicodeVersion version) const
    return self.uglySide.call(
        'ritual_ZNK7QString10normalizedENS_17NormalizationFormEN5QChar14Uni'
        'codeVersionE',
        mode.value, version.value,
    )

  @overload(int)
  def repeated(self, times: int) -> str:
    """
    Calls Qt's 'QString QString::repeated(qsizetype times) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#repeated

    Parameters
    ----------

    times : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::repeated(qsizetype times) const
    return self.uglySide.call('ritual_ZNK7QString8repeatedEx', times)

  def nullTerminated(self) -> str:
    """
    Calls Qt's 'QString QString::nullTerminated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#nullTerminated

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QString::nullTerminated() const
    return self.uglySide.call('ritual_ZNKR7QString14nullTerminatedEv')

  def toLatin1(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLatin1

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toLatin1() const
    address = self.uglySide.call('ritual_ZNKR7QString8toLatin1Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toUtf8(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toUtf8

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toUtf8() const
    address = self.uglySide.call('ritual_ZNKR7QString6toUtf8Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toLocal8Bit(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QString::toLocal8Bit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#toLocal8Bit

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QString::toLocal8Bit() const
    address = self.uglySide.call('ritual_ZNKR7QString11toLocal8BitEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def compare(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(const QString &s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(const QString &s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString7compareERKS_N2Qt15CaseSensitivityE', s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def compare(
      self,
      other: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(QLatin1StringView other,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    other : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(QLatin1StringView other, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK7QString7compareE13QLatin1StringN2Qt15CaseSensitivityE',
        self._valueOf(other), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def compare(
      self,
      ch: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(QChar ch, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(QChar ch, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK7QString7compareE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(ch), cs.value,
    )

  @staticmethod
  @overload(str, str)
  @overload(str, str, Qt.CaseSensitivity)
  def compare(
      s1: str,
      s2: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(const QString &s1, const QString &s2,
    Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(const QString &s1, const QString &s2,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN7QString7compareERKS_S1_N2Qt15CaseSensitivityE',
        s1, s2, cs.value,
    )

  @staticmethod
  @overload(str, QLatin1String)
  @overload(str, QLatin1String, Qt.CaseSensitivity)
  def compare(
      s1: str,
      s2: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(const QString &s1, QLatin1StringView s2,
    Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(const QString &s1, QLatin1StringView s2,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN7QString7compareERKS_13QLatin1StringN2Qt15CaseSensitivity'
        'E',
        s1, CuteMixin._valueOf(s2), cs.value,
    )

  @staticmethod
  @overload(QLatin1String, str)
  @overload(QLatin1String, str, Qt.CaseSensitivity)
  def compare(
      s1: QLatin1String,
      s2: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QString::compare(QLatin1StringView s1, const QString &s2,
    Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#compare

    Parameters
    ----------

    s1 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    s2 : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QString::compare(QLatin1StringView s1, const QString &s2,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN7QString7compareE13QLatin1StringRKS_N2Qt15CaseSensitivity'
        'E',
        CuteMixin._valueOf(s1), s2, cs.value,
    )

  @overload(str)
  def localeAwareCompare(self, s: str) -> int:
    """
    Calls Qt's 'int QString::localeAwareCompare(const QString &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#localeAwareCompare

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QString::localeAwareCompare(const QString &s) const
    return self.uglySide.call(
        'ritual_ZNK7QString18localeAwareCompareERKS_', s,
    )

  @staticmethod
  @overload(str, str)
  def localeAwareCompare(s1: str, s2: str) -> int:
    """
    Calls Qt's 'int QString::localeAwareCompare(const QString &s1, const
    QString &s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#localeAwareCompare

    Parameters
    ----------

    s1 : str
      Passed on as it is: a QString is made of it for the call.

    s2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QString::localeAwareCompare(const QString &s1, const QString &s2)
    return Rituals.call(
        'ritual_ZN7QString18localeAwareCompareERKS_S1_', s1, s2,
    )

  def cbegin(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QString::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#cbegin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QString::cbegin() const
    address = self.uglySide.call('ritual_ZNK7QString6cbeginEv')
    return QChar._cuteAt(address)

  def constBegin(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QString::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#constBegin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QString::constBegin() const
    address = self.uglySide.call('ritual_ZNK7QString10constBeginEv')
    return QChar._cuteAt(address)

  def cend(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QString::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#cend

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QString::cend() const
    address = self.uglySide.call('ritual_ZNK7QString4cendEv')
    return QChar._cuteAt(address)

  def constEnd(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QString::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#constEnd

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QString::constEnd() const
    address = self.uglySide.call('ritual_ZNK7QString8constEndEv')
    return QChar._cuteAt(address)

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QString::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#max_size
    """
    #  qsizetype QString::max_size() const
    return self.uglySide.call('ritual_ZNK7QString8max_sizeEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QString::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isNull
    """
    #  bool QString::isNull() const
    return self.uglySide.call('ritual_ZNK7QString6isNullEv')

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QString::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isRightToLeft
    """
    #  bool QString::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK7QString13isRightToLeftEv')

  def isValidUtf16(self) -> bool:
    """
    Calls Qt's 'bool QString::isValidUtf16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#isValidUtf16
    """
    #  bool QString::isValidUtf16() const
    return self.uglySide.call('ritual_ZNK7QString12isValidUtf16Ev')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, i: int) -> QChar:
    """
    Calls Qt's 'const QChar QString::operator[](qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  const QChar QString::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK7QStringixEx', i)
    return QChar._cuteOwning(address)

  @overload(QChar)
  def __iadd__(self, c: QChar) -> QString:
    """
    Calls Qt's 'QString &QString::operator+=(QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator+=

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  QString &QString::operator+=(QChar c)
    self.uglySide.call('ritual_ZN7QStringpLE5QChar', self._valueOf(c))
    return self

  @overload(str)
  def __iadd__(self, s: str) -> QString:
    """
    Calls Qt's 'QString &QString::operator+=(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator+=

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QString &QString::operator+=(const QString &s)
    self.uglySide.call('ritual_ZN7QStringpLERKS_', s)
    return self

  @overload(QLatin1String)
  def __iadd__(self, s: QLatin1String) -> QString:
    """
    Calls Qt's 'QString &QString::operator+=(QLatin1StringView s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator+=

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QString &QString::operator+=(QLatin1StringView s)
    self.uglySide.call(
        'ritual_ZN7QStringpLE13QLatin1String', self._valueOf(s),
    )
    return self

  @overload(NoneType)
  def __iadd__(self, s: Optional[str]) -> QString:
    """
    Calls Qt's 'QString &QString::operator+=(const char *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator+=

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QString &QString::operator+=(const char *s)
    self.uglySide.call('ritual_ZN7QStringpLEPKc', self._bytesOf(s))
    return self

  @overload(QByteArray)
  def __iadd__(self, s: QByteArray) -> QString:
    """
    Calls Qt's 'QString &QString::operator+=(const QByteArray &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#operator+=

    Parameters
    ----------

    s : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QString &QString::operator+=(const QByteArray &s)
    self.uglySide.call(
        'ritual_ZN7QStringpLERK10QByteArray', self._valueOf(s),
    )
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QString::QString()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString
    """
    #  QString::QString()
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1Ev',
    ))

  @overload(QChar)
  @overload(NoneType)
  @overload(QChar, int)
  @overload(NoneType, int)
  def __init__(self, unicode: Optional[QChar], size: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(const QChar *unicode,
    qsizetype size)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    unicode : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QString::QString(const QChar *unicode, qsizetype size)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1EPK5QCharx', self._addressOf(unicode), size,
    ))

  @overload(int, QChar)
  def __init__(self, size: int, c: QChar) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(qsizetype size, QChar
    c)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    size : int
      Passed on as it is.

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  QString::QString(qsizetype size, QChar c)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1Ex5QChar', size, self._valueOf(c),
    ))

  @overload(QLatin1String)
  def __init__(self, latin1: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(QLatin1StringView
    latin1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    latin1 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QString::QString(QLatin1StringView latin1)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1E13QLatin1String', self._valueOf(latin1),
    ))

  @overload(str)
  def __init__(self, sv: str) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(QStringView sv)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    sv : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QString::QString(QStringView sv)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1E11QStringView', sv,
    ))

  @overload(QByteArray)
  def __init__(self, a: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(const QByteArray &a)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QString::QString(const QByteArray &a)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1ERK10QByteArray', self._valueOf(a),
    ))

  @overload(int, Qt.Initialization)
  def __init__(self, size: int, a1: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QString::QString(qsizetype size,
    Qt::Initialization a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#QString

    Parameters
    ----------

    size : int
      Passed on as it is.

    a1 : Qt.Initialization
      Passed on as its number.
    """
    #  QString::QString(qsizetype size, Qt::Initialization a1)
    self._noteCreation(QString, lambda: Rituals.call(
        'ritual_ZN7QStringC1ExN2Qt14InitializationE', size, a1.value,
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

  @overload(int)
  def resize(self, size: int) -> None:
    """
    Calls Qt's 'void QString::resize(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#resize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QString::resize(qsizetype size)
    self.uglySide.call('ritual_ZN7QString6resizeEx', size)

  @overload(int, QChar)
  def resize(self, size: int, fillChar: QChar) -> None:
    """
    Calls Qt's 'void QString::resize(qsizetype size, QChar fillChar)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#resize

    Parameters
    ----------

    size : int
      Passed on as it is.

    fillChar : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QString::resize(qsizetype size, QChar fillChar)
    self.uglySide.call(
        'ritual_ZN7QString6resizeEx5QChar', size, self._valueOf(fillChar),
    )

  @overload(int)
  def resizeForOverwrite(self, size: int) -> None:
    """
    Calls Qt's 'void QString::resizeForOverwrite(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#resizeForOverwrite

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QString::resizeForOverwrite(qsizetype size)
    self.uglySide.call('ritual_ZN7QString18resizeForOverwriteEx', size)

  @overload(int)
  def truncate(self, pos: int) -> None:
    """
    Calls Qt's 'void QString::truncate(qsizetype pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#truncate

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QString::truncate(qsizetype pos)
    self.uglySide.call('ritual_ZN7QString8truncateEx', pos)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QString::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QString::chop(qsizetype n)
    self.uglySide.call('ritual_ZN7QString4chopEx', n)

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QString::reserve(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QString::reserve(qsizetype size)
    self.uglySide.call('ritual_ZN7QString7reserveEx', size)

  def squeeze(self) -> None:
    """
    Calls Qt's 'void QString::squeeze()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#squeeze
    """
    #  void QString::squeeze()
    self.uglySide.call('ritual_ZN7QString7squeezeEv')

  def data(self) -> Optional[QChar]:
    """
    Calls Qt's 'QChar *QString::data()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#data

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChar *QString::data()
    address = self.uglySide.call('ritual_ZN7QString4dataEv')
    return QChar._cuteAt(address)

  def detach(self) -> None:
    """
    Calls Qt's 'void QString::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#detach
    """
    #  void QString::detach()
    self.uglySide.call('ritual_ZN7QString6detachEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QString::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#clear
    """
    #  void QString::clear()
    self.uglySide.call('ritual_ZN7QString5clearEv')

  def begin(self) -> Optional[QChar]:
    """
    Calls Qt's 'iterator QString::begin()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#begin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  iterator QString::begin()
    address = self.uglySide.call('ritual_ZN7QString5beginEv')
    return QChar._cuteAt(address)

  def end(self) -> Optional[QChar]:
    """
    Calls Qt's 'iterator QString::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#end

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  iterator QString::end()
    address = self.uglySide.call('ritual_ZN7QString3endEv')
    return QChar._cuteAt(address)

  @overload(QChar)
  def push_back(self, c: QChar) -> None:
    """
    Calls Qt's 'void QString::push_back(QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#push_back

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QString::push_back(QChar c)
    self.uglySide.call(
        'ritual_ZN7QString9push_backE5QChar', self._valueOf(c),
    )

  @overload(str)
  def push_back(self, s: str) -> None:
    """
    Calls Qt's 'void QString::push_back(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#push_back

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QString::push_back(const QString &s)
    self.uglySide.call('ritual_ZN7QString9push_backERKS_', s)

  @overload(QChar)
  def push_front(self, c: QChar) -> None:
    """
    Calls Qt's 'void QString::push_front(QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#push_front

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QString::push_front(QChar c)
    self.uglySide.call(
        'ritual_ZN7QString10push_frontE5QChar', self._valueOf(c),
    )

  @overload(str)
  def push_front(self, s: str) -> None:
    """
    Calls Qt's 'void QString::push_front(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#push_front

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QString::push_front(const QString &s)
    self.uglySide.call('ritual_ZN7QString10push_frontERKS_', s)

  def shrink_to_fit(self) -> None:
    """
    Calls Qt's 'void QString::shrink_to_fit()'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#shrink_to_fit
    """
    #  void QString::shrink_to_fit()
    self.uglySide.call('ritual_ZN7QString13shrink_to_fitEv')

  @overload(QChar, QChar)
  @overload(QChar, NoneType)
  @overload(NoneType, QChar)
  @overload(NoneType, NoneType)
  def erase(
      self,
      first: Optional[QChar],
      last: Optional[QChar],
  ) -> Optional[QChar]:
    """
    Calls Qt's 'iterator QString::erase(const_iterator first, const_iterator
    last)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#erase

    Parameters
    ----------

    first : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    last : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  iterator QString::erase(const_iterator first, const_iterator last)
    address = self.uglySide.call(
        'ritual_ZN7QString5eraseEPK5QCharS2_',
        self._addressOf(first), self._addressOf(last),
    )
    return QChar._cuteAt(address)

  @overload(QChar)
  @overload(NoneType)
  def erase(self, it: Optional[QChar]) -> Optional[QChar]:
    """
    Calls Qt's 'iterator QString::erase(const_iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#erase

    Parameters
    ----------

    it : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  iterator QString::erase(const_iterator it)
    address = self.uglySide.call(
        'ritual_ZN7QString5eraseEPK5QChar', self._addressOf(it),
    )
    return QChar._cuteAt(address)

  @overload(int, QArrayData.AllocationOption)
  def reallocData(
      self,
      alloc: int,
      option: QArrayData.AllocationOption,
  ) -> None:
    """
    Calls Qt's 'void QString::reallocData(qsizetype alloc,
    QArrayData::AllocationOption option)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#reallocData

    Parameters
    ----------

    alloc : int
      Passed on as it is.

    option : QArrayData.AllocationOption
      Passed on as its number.
    """
    #  void QString::reallocData(qsizetype alloc,
    #      QArrayData::AllocationOption option)
    self.uglySide.call(
        'ritual_ZN7QString11reallocDataExN10QArrayData16AllocationOptionE',
        alloc, option.value,
    )

  @overload(int)
  def reallocGrowData(self, n: int) -> None:
    """
    Calls Qt's 'void QString::reallocGrowData(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#reallocGrowData

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QString::reallocGrowData(qsizetype n)
    self.uglySide.call('ritual_ZN7QString15reallocGrowDataEx', n)

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QString::verify(qsizetype pos, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstring.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QString::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK7QString6verifyExx', pos, n)

  @staticmethod
  def append(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::append(QChar c)': gives a type Python has no
      way to take yet.
    - Qt's 'QString &QString::append(const QChar *uc, qsizetype len)': gives
      a type Python has no way to take yet.
    - Qt's 'QString &QString::append(const QString &s)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::append(QStringView v)': gives a type Python has
      no way to take yet.
    - Qt's 'QString &QString::append(QLatin1StringView s)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::append(QUtf8StringView s)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QString &QString::append(const char *s)': gives a type Python has
      no way to take yet.
    - Qt's 'QString &QString::append(const QByteArray &s)': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.append' has no cute function yet. Qt's 'QString "
        "&QString::append(QChar c)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::append(const QChar *uc, qsizetype "
        "len)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::append(const QString &s)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::append(QStringView v)': "
        "gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::append(QLatin1StringView s)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::append(QUtf8StringView "
        "s)': takes a type Python has no way to hand over yet. Qt's "
        "'QString &QString::append(const char *s)': gives a type Python has "
        "no way to take yet. Qt's 'QString &QString::append(const "
        "QByteArray &s)': gives a type Python has no way to take yet.")

  @staticmethod
  def arg(*__, **_) -> Never:
    """Qt's 'QString::arg': a template: a pattern and no single function."""
    raise NotImplementedError(
        "'QString.arg' has no cute function yet. Qt's 'QString::arg': a "
        "template: a pattern and no single function.")

  @staticmethod
  def asprintf(*__, **_) -> Never:
    """
    Qt's 'QString QString::asprintf(const char *format)': takes any number of
    arguments.
    """
    raise NotImplementedError(
        "'QString.asprintf' has no cute function yet. Qt's 'QString "
        "QString::asprintf(const char *format)': takes any number of "
        "arguments.")

  @staticmethod
  def assign(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::assign(QAnyStringView s)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::assign(qsizetype n, QChar c)': gives a type
      Python has no way to take yet.
    - Qt's 'QString::assign': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QString.assign' has no cute function yet. Qt's 'QString "
        "&QString::assign(QAnyStringView s)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::assign(qsizetype n, QChar "
        "c)': gives a type Python has no way to take yet. Qt's "
        "'QString::assign': a template: a pattern and no single function.")

  @staticmethod
  def assign_helper(*__, **_) -> Never:
    """
    Qt's 'QString &QString::assign_helper(const char32_t *data, qsizetype
    len)': names 'char32_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.assign_helper' has no cute function yet. Qt's 'QString "
        "&QString::assign_helper(const char32_t *data, qsizetype len)': "
        "names 'char32_t', which has no cute class yet.")

  @staticmethod
  def assign_helper_char8(*__, **_) -> Never:
    """
    Qt's 'QString::assign_helper_char8': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QString.assign_helper_char8' has no cute function yet. Qt's "
        "'QString::assign_helper_char8': a template: a pattern and no "
        "single function.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QString::crbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QString::crbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QString::crend() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QString::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def data_ptr(*__, **_) -> Never:
    """
    - Qt's 'DataPointer &QString::data_ptr()': gives a type Python has no way
      to take yet.
    - Qt's 'const DataPointer &QString::data_ptr() const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.data_ptr' has no cute function yet. Qt's 'DataPointer "
        "&QString::data_ptr()': gives a type Python has no way to take yet. "
        "Qt's 'const DataPointer &QString::data_ptr() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def fill(*__, **_) -> Never:
    """
    Qt's 'QString &QString::fill(QChar c, qsizetype size)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.fill' has no cute function yet. Qt's 'QString "
        "&QString::fill(QChar c, qsizetype size)': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def fromStdString(*__, **_) -> Never:
    """
    Qt's 'QString QString::fromStdString(const std::string &s)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.fromStdString' has no cute function yet. Qt's 'QString "
        "QString::fromStdString(const std::string &s)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def fromStdU16String(*__, **_) -> Never:
    """
    Qt's 'QString QString::fromStdU16String(const std::u16string &s)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.fromStdU16String' has no cute function yet. Qt's 'QString "
        "QString::fromStdU16String(const std::u16string &s)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fromStdU32String(*__, **_) -> Never:
    """
    Qt's 'QString QString::fromStdU32String(const std::u32string &s)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.fromStdU32String' has no cute function yet. Qt's 'QString "
        "QString::fromStdU32String(const std::u32string &s)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fromStdWString(*__, **_) -> Never:
    """
    Qt's 'QString QString::fromStdWString(const std::wstring &s)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.fromStdWString' has no cute function yet. Qt's 'QString "
        "QString::fromStdWString(const std::wstring &s)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fromUcs4(*__, **_) -> Never:
    """
    - Qt's 'QString QString::fromUcs4(const char32_t *a0, qsizetype size)':
      names 'char32_t', which has no cute class yet.
    - Qt's 'QString QString::fromUcs4(const uint *str, qsizetype size)':
      names 'uint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.fromUcs4' has no cute function yet. Qt's 'QString "
        "QString::fromUcs4(const char32_t *a0, qsizetype size)': names "
        "'char32_t', which has no cute class yet. Qt's 'QString "
        "QString::fromUcs4(const uint *str, qsizetype size)': names 'uint', "
        "which has no cute class yet.")

  @staticmethod
  def fromUtf16(*__, **_) -> Never:
    """
    - Qt's 'QString QString::fromUtf16(const char16_t *a0, qsizetype size)':
      names 'char16_t', which has no cute class yet.
    - Qt's 'QString QString::fromUtf16(const ushort *str, qsizetype size)':
      names 'ushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.fromUtf16' has no cute function yet. Qt's 'QString "
        "QString::fromUtf16(const char16_t *a0, qsizetype size)': names "
        "'char16_t', which has no cute class yet. Qt's 'QString "
        "QString::fromUtf16(const ushort *str, qsizetype size)': names "
        "'ushort', which has no cute class yet.")

  @staticmethod
  def fromWCharArray(*__, **_) -> Never:
    """
    Qt's 'QString QString::fromWCharArray(const wchar_t *string, qsizetype
    size)': names 'wchar_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.fromWCharArray' has no cute function yet. Qt's 'QString "
        "QString::fromWCharArray(const wchar_t *string, qsizetype size)': "
        "names 'wchar_t', which has no cute class yet.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::insert(qsizetype i, QChar c)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, const QChar *uc, qsizetype
      len)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, const QString &s)': gives a
      type Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, QStringView v)': gives a
      type Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, QLatin1StringView s)':
      gives a type Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, QUtf8StringView s)': takes
      a type Python has no way to hand over yet.
    - Qt's 'QString &QString::insert(qsizetype i, const char *s)': gives a
      type Python has no way to take yet.
    - Qt's 'QString &QString::insert(qsizetype i, const QByteArray &s)':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.insert' has no cute function yet. Qt's 'QString "
        "&QString::insert(qsizetype i, QChar c)': gives a type Python has "
        "no way to take yet. Qt's 'QString &QString::insert(qsizetype i, "
        "const QChar *uc, qsizetype len)': gives a type Python has no way "
        "to take yet. Qt's 'QString &QString::insert(qsizetype i, const "
        "QString &s)': gives a type Python has no way to take yet. Qt's "
        "'QString &QString::insert(qsizetype i, QStringView v)': gives a "
        "type Python has no way to take yet. Qt's 'QString "
        "&QString::insert(qsizetype i, QLatin1StringView s)': gives a type "
        "Python has no way to take yet. Qt's 'QString "
        "&QString::insert(qsizetype i, QUtf8StringView s)': takes a type "
        "Python has no way to hand over yet. Qt's 'QString "
        "&QString::insert(qsizetype i, const char *s)': gives a type Python "
        "has no way to take yet. Qt's 'QString &QString::insert(qsizetype "
        "i, const QByteArray &s)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def nullTerminate(*__, **_) -> Never:
    """
    Qt's 'QString &QString::nullTerminate()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QString.nullTerminate' has no cute function yet. Qt's 'QString "
        "&QString::nullTerminate()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def prepend(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::prepend(QChar c)': gives a type Python has no
      way to take yet.
    - Qt's 'QString &QString::prepend(const QChar *uc, qsizetype len)': gives
      a type Python has no way to take yet.
    - Qt's 'QString &QString::prepend(const QString &s)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::prepend(QStringView v)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::prepend(QLatin1StringView s)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::prepend(QUtf8StringView s)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QString &QString::prepend(const char *s)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::prepend(const QByteArray &s)': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.prepend' has no cute function yet. Qt's 'QString "
        "&QString::prepend(QChar c)': gives a type Python has no way to "
        "take yet. Qt's 'QString &QString::prepend(const QChar *uc, "
        "qsizetype len)': gives a type Python has no way to take yet. Qt's "
        "'QString &QString::prepend(const QString &s)': gives a type Python "
        "has no way to take yet. Qt's 'QString "
        "&QString::prepend(QStringView v)': gives a type Python has no way "
        "to take yet. Qt's 'QString &QString::prepend(QLatin1StringView "
        "s)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::prepend(QUtf8StringView s)': takes a type Python has no "
        "way to hand over yet. Qt's 'QString &QString::prepend(const char "
        "*s)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::prepend(const QByteArray &s)': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    - Qt's 'reverse_iterator QString::rbegin()': gives a type Python has no
      way to take yet.
    - Qt's 'const_reverse_iterator QString::rbegin() const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.rbegin' has no cute function yet. Qt's 'reverse_iterator "
        "QString::rbegin()': gives a type Python has no way to take yet. "
        "Qt's 'const_reverse_iterator QString::rbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::remove(qsizetype i, qsizetype len)': gives a
      type Python has no way to take yet.
    - Qt's 'QString &QString::remove(QChar c, Qt::CaseSensitivity cs)': gives
      a type Python has no way to take yet.
    - Qt's 'QString &QString::remove(QLatin1StringView s, Qt::CaseSensitivity
      cs)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::remove(const QString &s, Qt::CaseSensitivity
      cs)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::remove(const QRegularExpression &re)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.remove' has no cute function yet. Qt's 'QString "
        "&QString::remove(qsizetype i, qsizetype len)': gives a type Python "
        "has no way to take yet. Qt's 'QString &QString::remove(QChar c, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::remove(QLatin1StringView s, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::remove(const QString &s, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::remove(const QRegularExpression "
        "&re)': gives a type Python has no way to take yet.")

  @staticmethod
  def removeAt(*__, **_) -> Never:
    """
    Qt's 'QString &QString::removeAt(qsizetype pos)': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QString.removeAt' has no cute function yet. Qt's 'QString "
        "&QString::removeAt(qsizetype pos)': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def removeFirst(*__, **_) -> Never:
    """
    Qt's 'QString &QString::removeFirst()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QString.removeFirst' has no cute function yet. Qt's 'QString "
        "&QString::removeFirst()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def removeIf(*__, **_) -> Never:
    """
    Qt's 'QString::removeIf': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QString.removeIf' has no cute function yet. Qt's "
        "'QString::removeIf': a template: a pattern and no single function.")

  @staticmethod
  def removeIf_helper(*__, **_) -> Never:
    """
    Qt's 'QString::removeIf_helper': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QString.removeIf_helper' has no cute function yet. Qt's "
        "'QString::removeIf_helper': a template: a pattern and no single "
        "function.")

  @staticmethod
  def removeLast(*__, **_) -> Never:
    """
    Qt's 'QString &QString::removeLast()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QString.removeLast' has no cute function yet. Qt's 'QString "
        "&QString::removeLast()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    - Qt's 'reverse_iterator QString::rend()': gives a type Python has no way
      to take yet.
    - Qt's 'const_reverse_iterator QString::rend() const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.rend' has no cute function yet. Qt's 'reverse_iterator "
        "QString::rend()': gives a type Python has no way to take yet. Qt's "
        "'const_reverse_iterator QString::rend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def replace(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, QChar
      after)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, const QChar
      *s, qsizetype slen)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(qsizetype i, qsizetype len, const
      QString &after)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(QChar before, QChar after,
      Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(const QChar *before, qsizetype blen,
      const QChar *after, qsizetype alen, Qt::CaseSensitivity cs)': gives a
      type Python has no way to take yet.
    - Qt's 'QString &QString::replace(QLatin1StringView before,
      QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::replace(QLatin1StringView before, const QString
      &after, Qt::CaseSensitivity cs)': gives a type Python has no way to
      take yet.
    - Qt's 'QString &QString::replace(const QString &before,
      QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::replace(const QString &before, const QString
      &after, Qt::CaseSensitivity cs)': gives a type Python has no way to
      take yet.
    - Qt's 'QString &QString::replace(QChar c, const QString &after,
      Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(QChar c, QLatin1StringView after,
      Qt::CaseSensitivity cs)': gives a type Python has no way to take yet.
    - Qt's 'QString &QString::replace(const QRegularExpression &re, const
      QString &after)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.replace' has no cute function yet. Qt's 'QString "
        "&QString::replace(qsizetype i, qsizetype len, QChar after)': gives "
        "a type Python has no way to take yet. Qt's 'QString "
        "&QString::replace(qsizetype i, qsizetype len, const QChar *s, "
        "qsizetype slen)': gives a type Python has no way to take yet. Qt's "
        "'QString &QString::replace(qsizetype i, qsizetype len, const "
        "QString &after)': gives a type Python has no way to take yet. Qt's "
        "'QString &QString::replace(QChar before, QChar after, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::replace(const QChar *before, "
        "qsizetype blen, const QChar *after, qsizetype alen, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::replace(QLatin1StringView before, "
        "QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type "
        "Python has no way to take yet. Qt's 'QString "
        "&QString::replace(QLatin1StringView before, const QString &after, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::replace(const QString &before, "
        "QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type "
        "Python has no way to take yet. Qt's 'QString "
        "&QString::replace(const QString &before, const QString &after, "
        "Qt::CaseSensitivity cs)': gives a type Python has no way to take "
        "yet. Qt's 'QString &QString::replace(QChar c, const QString "
        "&after, Qt::CaseSensitivity cs)': gives a type Python has no way "
        "to take yet. Qt's 'QString &QString::replace(QChar c, "
        "QLatin1StringView after, Qt::CaseSensitivity cs)': gives a type "
        "Python has no way to take yet. Qt's 'QString "
        "&QString::replace(const QRegularExpression &re, const QString "
        "&after)': gives a type Python has no way to take yet.")

  @staticmethod
  def setNum(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::setNum(short a0, int base)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::setNum(ushort a0, int base)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::setNum(int a0, int base)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::setNum(uint a0, int base)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::setNum(long a0, int base)': gives a type Python
      has no way to take yet.
    - Qt's 'QString &QString::setNum(ulong a0, int base)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::setNum(qlonglong a0, int base)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::setNum(qulonglong a0, int base)': gives a type
      Python has no way to take yet.
    - Qt's 'QString &QString::setNum(float a0, char format, int precision)':
      takes a single letter as C has it.
    - Qt's 'QString &QString::setNum(double a0, char format, int precision)':
      takes a single letter as C has it.
    """
    raise NotImplementedError(
        "'QString.setNum' has no cute function yet. Qt's 'QString "
        "&QString::setNum(short a0, int base)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::setNum(ushort a0, int "
        "base)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::setNum(int a0, int base)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::setNum(uint a0, int "
        "base)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::setNum(long a0, int base)': gives a type Python has no "
        "way to take yet. Qt's 'QString &QString::setNum(ulong a0, int "
        "base)': gives a type Python has no way to take yet. Qt's 'QString "
        "&QString::setNum(qlonglong a0, int base)': gives a type Python has "
        "no way to take yet. Qt's 'QString &QString::setNum(qulonglong a0, "
        "int base)': gives a type Python has no way to take yet. Qt's "
        "'QString &QString::setNum(float a0, char format, int precision)': "
        "takes a single letter as C has it. Qt's 'QString "
        "&QString::setNum(double a0, char format, int precision)': takes a "
        "single letter as C has it.")

  @staticmethod
  def setRawData(*__, **_) -> Never:
    """
    Qt's 'QString &QString::setRawData(const QChar *unicode, qsizetype
    size)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.setRawData' has no cute function yet. Qt's 'QString "
        "&QString::setRawData(const QChar *unicode, qsizetype size)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setUnicode(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::setUnicode(const QChar *unicode, qsizetype
      size)': gives a type Python has no way to take yet.
    - Qt's 'QString::setUnicode': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QString.setUnicode' has no cute function yet. Qt's 'QString "
        "&QString::setUnicode(const QChar *unicode, qsizetype size)': gives "
        "a type Python has no way to take yet. Qt's 'QString::setUnicode': "
        "a template: a pattern and no single function.")

  @staticmethod
  def setUtf16(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::setUtf16(const char16_t *utf16, qsizetype
      size)': names 'char16_t', which has no cute class yet.
    - Qt's 'QString::setUtf16': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QString.setUtf16' has no cute function yet. Qt's 'QString "
        "&QString::setUtf16(const char16_t *utf16, qsizetype size)': names "
        "'char16_t', which has no cute class yet. Qt's 'QString::setUtf16': "
        "a template: a pattern and no single function.")

  @staticmethod
  def slice(*__, **_) -> Never:
    """
    - Qt's 'QString &QString::slice(qsizetype pos)': gives a type Python has
      no way to take yet.
    - Qt's 'QString &QString::slice(qsizetype pos, qsizetype n)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.slice' has no cute function yet. Qt's 'QString "
        "&QString::slice(qsizetype pos)': gives a type Python has no way to "
        "take yet. Qt's 'QString &QString::slice(qsizetype pos, qsizetype "
        "n)': gives a type Python has no way to take yet.")

  @staticmethod
  def sliced_helper(*__, **_) -> Never:
    """
    Qt's 'QString QString::sliced_helper(QString &str, qsizetype pos,
    qsizetype n)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.sliced_helper' has no cute function yet. Qt's 'QString "
        "QString::sliced_helper(QString &str, qsizetype pos, qsizetype n)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QString::swap(QString &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QString.swap' has no cute function yet. Qt's 'void "
        "QString::swap(QString &other)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def toDouble(*__, **_) -> Never:
    """
    Qt's 'double QString::toDouble(bool *ok) const': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QString.toDouble' has no cute function yet. Qt's 'double "
        "QString::toDouble(bool *ok) const': takes a number to change where "
        "it is.")

  @staticmethod
  def toFloat(*__, **_) -> Never:
    """
    Qt's 'float QString::toFloat(bool *ok) const': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QString.toFloat' has no cute function yet. Qt's 'float "
        "QString::toFloat(bool *ok) const': takes a number to change where "
        "it is.")

  @staticmethod
  def toInt(*__, **_) -> Never:
    """
    Qt's 'int QString::toInt(bool *ok, int base) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QString.toInt' has no cute function yet. Qt's 'int "
        "QString::toInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toIntegral_helper(*__, **_) -> Never:
    """
    - Qt's 'qlonglong QString::toIntegral_helper(QStringView string, bool
      *ok, int base)': takes a number to change where it is.
    - Qt's 'qulonglong QString::toIntegral_helper(QStringView string, bool
      *ok, uint base)': takes a number to change where it is.
    - Qt's 'QString::toIntegral_helper': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QString.toIntegral_helper' has no cute function yet. Qt's "
        "'qlonglong QString::toIntegral_helper(QStringView string, bool "
        "*ok, int base)': takes a number to change where it is. Qt's "
        "'qulonglong QString::toIntegral_helper(QStringView string, bool "
        "*ok, uint base)': takes a number to change where it is. Qt's "
        "'QString::toIntegral_helper': a template: a pattern and no single "
        "function.")

  @staticmethod
  def toLatin1_helper_inplace(*__, **_) -> Never:
    """
    Qt's 'QByteArray QString::toLatin1_helper_inplace(QString &a0)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QString.toLatin1_helper_inplace' has no cute function yet. Qt's "
        "'QByteArray QString::toLatin1_helper_inplace(QString &a0)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def toLong(*__, **_) -> Never:
    """
    Qt's 'long QString::toLong(bool *ok, int base) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QString.toLong' has no cute function yet. Qt's 'long "
        "QString::toLong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toLongLong(*__, **_) -> Never:
    """
    Qt's 'qlonglong QString::toLongLong(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QString.toLongLong' has no cute function yet. Qt's 'qlonglong "
        "QString::toLongLong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toShort(*__, **_) -> Never:
    """
    Qt's 'short QString::toShort(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QString.toShort' has no cute function yet. Qt's 'short "
        "QString::toShort(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toStdString(*__, **_) -> Never:
    """
    Qt's 'std::string QString::toStdString() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QString.toStdString' has no cute function yet. Qt's 'std::string "
        "QString::toStdString() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def toStdU16String(*__, **_) -> Never:
    """
    Qt's 'std::u16string QString::toStdU16String() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.toStdU16String' has no cute function yet. Qt's "
        "'std::u16string QString::toStdU16String() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toStdU32String(*__, **_) -> Never:
    """
    Qt's 'std::u32string QString::toStdU32String() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.toStdU32String' has no cute function yet. Qt's "
        "'std::u32string QString::toStdU32String() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toStdWString(*__, **_) -> Never:
    """
    Qt's 'std::wstring QString::toStdWString() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QString.toStdWString' has no cute function yet. Qt's "
        "'std::wstring QString::toStdWString() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def toUInt(*__, **_) -> Never:
    """
    Qt's 'uint QString::toUInt(bool *ok, int base) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QString.toUInt' has no cute function yet. Qt's 'uint "
        "QString::toUInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULong(*__, **_) -> Never:
    """
    Qt's 'ulong QString::toULong(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QString.toULong' has no cute function yet. Qt's 'ulong "
        "QString::toULong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULongLong(*__, **_) -> Never:
    """
    Qt's 'qulonglong QString::toULongLong(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QString.toULongLong' has no cute function yet. Qt's 'qulonglong "
        "QString::toULongLong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUShort(*__, **_) -> Never:
    """
    Qt's 'ushort QString::toUShort(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QString.toUShort' has no cute function yet. Qt's 'ushort "
        "QString::toUShort(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUcs4(*__, **_) -> Never:
    """
    Qt's 'QList<uint> QString::toUcs4() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QString.toUcs4' has no cute function yet. Qt's 'QList<uint> "
        "QString::toUcs4() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def toUcs4_helper(*__, **_) -> Never:
    """
    Qt's 'qsizetype QString::toUcs4_helper(const char16_t *uc, qsizetype
    length, char32_t *out)': names 'char16_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.toUcs4_helper' has no cute function yet. Qt's 'qsizetype "
        "QString::toUcs4_helper(const char16_t *uc, qsizetype length, "
        "char32_t *out)': names 'char16_t', which has no cute class yet.")

  @staticmethod
  def toWCharArray(*__, **_) -> Never:
    """
    Qt's 'qsizetype QString::toWCharArray(wchar_t *array) const': names
    'wchar_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.toWCharArray' has no cute function yet. Qt's 'qsizetype "
        "QString::toWCharArray(wchar_t *array) const': names 'wchar_t', "
        "which has no cute class yet.")

  @staticmethod
  def tokenize(*__, **_) -> Never:
    """
    Qt's 'QString::tokenize': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QString.tokenize' has no cute function yet. Qt's "
        "'QString::tokenize': a template: a pattern and no single function.")

  @staticmethod
  def utf16(*__, **_) -> Never:
    """
    Qt's 'const ushort *QString::utf16() const': gives 'unsigned short',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.utf16' has no cute function yet. Qt's 'const ushort "
        "*QString::utf16() const': gives 'unsigned short', which has no "
        "cute class yet.")

  @staticmethod
  def vasprintf(*__, **_) -> Never:
    """
    Qt's 'QString QString::vasprintf(const char *format, __va_list_tag *ap)':
    names '__va_list_tag', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QString.vasprintf' has no cute function yet. Qt's 'QString "
        "QString::vasprintf(const char *format, __va_list_tag *ap)': names "
        "'__va_list_tag', which has no cute class yet.")
