//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 1. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstringconverter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringlist.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/private/qunicodetables_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/qstringmatcher.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/qcollator.h>
#include <QtCore/qttypetraits.h>
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/private/qfunctions_p.h>
#include <limits.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <wchar.h>
#include <QtCore/qlatin1stringmatcher.h>
#include <QtCore/private/qstringiterator_p.h>
#include <QtCore/private/qstringalgorithms_p.h>
#include <algorithm>
#include <functional>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#include <QtCore/qstringconverter.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/private/qstringiterator_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/qcontainertools_impl.h>
#include <QtCore/qbytearraylist.h>
#if QT_CONFIG(icu)
#include <unicode/ucnv.h>
#include <unicode/ucnv_cb.h>
#include <unicode/ucnv_err.h>
#include <unicode/ustring.h>
#elif QT_CONFIG(winsdkicu)
#include <icu.h>
#include <QtCore/private/qfunctions_win_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtCore/qt_windows.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qvarlengtharray.h>
#include <QtCore/private/wcharhelpers_win_p.h>
#include <QtCore/q20iterator.h>
#endif
#endif
#include <array>
#if __has_include(<bit>) && __cplusplus > 201703L
#include <bit>
#endif
#include <string>
#include <QtCore/q20utility.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/q26numeric.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/text/qstring.cpp, line 920, as local:qstring.cpp:qt_from_latin1
Q_CORE_EXPORT void qt_from_latin1(char16_t *dst, const char *str, size_t size) noexcept;

//  from src/corelib/text/qstring.cpp, line 5652, as _ZN7QLatin116convertToUnicodeEPDs13QLatin1String
inline char16_t *QLatin1::convertToUnicode(char16_t *out, QLatin1StringView in) noexcept
{
    const qsizetype len = in.size();
    qt_from_latin1(out, in.data(), len);
    return std::next(out, len);
}

//  from src/corelib/text/qstringconverter.cpp, line 1906, as _ZN7QLatin118convertFromUnicodeEPc11QStringViewPN20QStringConverterBase5StateE
inline char *QLatin1::convertFromUnicode(char *out, QStringView in, QStringConverter::State *state) noexcept
{
    Q_ASSERT(state);
    if (state->flags & QStringConverter::Flag::Stateless) // temporary
        state = nullptr;

    const char replacement = (state && state->flags & QStringConverter::Flag::ConvertInvalidToNull) ? 0 : '?';
    qsizetype invalid = 0;
    for (qsizetype i = 0; i < in.size(); ++i) {
        if (in[i] > QChar(0xff)) {
            *out = replacement;
            ++invalid;
        } else {
            *out = (char)in[i].cell();
        }
        ++out;
    }
    if (state)
        state->invalidChars += invalid;
    return out;
}
//  -----------------------------------------------------------------------

//  char *QLatin1::convertFromUnicode(char *out, QStringView in,
//      QStringConverter::State *state)
extern "C" Q_DECL_EXPORT
char *ritual_ZN7QLatin118convertFromUnicodeEPc11QStringViewPN20QStringConverterBase5StateE(
    char *out,
    const QString *in,
    QStringConverter::State *state) {
  return QLatin1::convertFromUnicode(out, QStringView(*in), state);
}

//  char *QLatin1::convertFromUnicode(char *out, QStringView in)
extern "C" Q_DECL_EXPORT
char *ritual_ZN7QLatin118convertFromUnicodeEPc11QStringView(
    char *out,
    const QString *in) {
  return QLatin1::convertFromUnicode(out, QStringView(*in));
}

//  QLatin1::~QLatin1()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLatin1D1Ev(QLatin1 *self) {
  delete self;
}

//  static char16_t *QLatin1::convertToUnicode(char16_t *dst,
//      QLatin1StringView in)
extern "C" Q_DECL_EXPORT
char16_t *ritual_ZN7QLatin116convertToUnicodeEPDs13QLatin1String(
    char16_t *dst,
    const QLatin1StringView *in) {
  return QLatin1::convertToUnicode(dst, *in);
}
