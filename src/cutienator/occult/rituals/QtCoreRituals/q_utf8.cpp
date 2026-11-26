//  Edited by hand on 2026-11-25: the ritual of 'QChar
//  *QUtf8::convertToUnicode(QChar *, QByteArrayView, State *)' is taken out
//  with its row, as that function is inline and calls the 'char16_t *' one
//  with a state, which Qt declares but its library does not offer (undefined
//  reference when linking). Kept as it is when the generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Also added
//  by hand on 2026-11-25, rituals for functions the generator leaves out: 1.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstringconverter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from src/corelib/text/qstringconverter.cpp, line 807, as _ZN5QUtf816convertToUnicodeE14QByteArrayView
inline QString QUtf8::convertToUnicode(QByteArrayView in)
{
    // UTF-8 to UTF-16 always needs the exact same number of words or less:
    //    UTF-8     UTF-16
    //   1 byte     1 word
    //   2 bytes    1 word
    //   3 bytes    1 word
    //   4 bytes    2 words (one surrogate pair)
    // That is, we'll use the full buffer if the input is US-ASCII (1-byte UTF-8),
    // half the buffer for U+0080-U+07FF text (e.g., Greek, Cyrillic, Arabic) or
    // non-BMP text, and one third of the buffer for U+0800-U+FFFF text (e.g, CJK).
    //
    // The table holds for invalid sequences too: we'll insert one replacement char
    // per invalid byte.
    QString result(in.size(), Qt::Uninitialized);
    QChar *data = const_cast<QChar*>(result.constData()); // we know we're not shared
    const QChar *end = convertToUnicode(data, in);
    result.truncate(end - data);
    return result;
}

//  from src/corelib/text/qstringconverter.cpp, line 1076, as _ZN5QUtf811compareUtf8E14QByteArrayView13QLatin1StringN2Qt15CaseSensitivityE
inline int QUtf8::compareUtf8(QByteArrayView utf8, QLatin1StringView s, Qt::CaseSensitivity cs)
{
    auto src1 = reinterpret_cast<const qchar8_t *>(utf8.data());
    auto end1 = src1 + utf8.size();
    auto src2 = reinterpret_cast<const uchar *>(s.latin1());
    auto end2 = src2 + s.size();

    while (src1 < end1 && src2 < end2) {
        char32_t uc1 = QUtf8Functions::nextUcs4FromUtf8(src1, end1);
        char32_t uc2 = *src2++;
        if (cs == Qt::CaseInsensitive) {
            uc1 = QChar::toCaseFolded(uc1);
            uc2 = QChar::toCaseFolded(uc2);
        }
        if (uc1 != uc2)
            return int(uc1) - int(uc2);
    }

    // the shorter string sorts first
    return (end1 > src1) - (end2 > src2);
}
//  -----------------------------------------------------------------------

//  QChar *QUtf8::convertToUnicode(QChar *buffer, QByteArrayView in)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN5QUtf816convertToUnicodeEP5QChar14QByteArrayView(
    QChar *buffer,
    const QByteArrayView *in) {
  return QUtf8::convertToUnicode(buffer, *in);
}

//  QString QUtf8::convertToUnicode(QByteArrayView in)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QUtf816convertToUnicodeE14QByteArrayView(
    const QByteArrayView *in) {
  return new QString(QUtf8::convertToUnicode(*in));
}

//  QString QUtf8::convertToUnicode(QByteArrayView in,
//      QStringConverter::State *state)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QUtf816convertToUnicodeE14QByteArrayViewPN20QStringConverterBase5StateE(
    const QByteArrayView *in,
    QStringConverter::State *state) {
  return new QString(QUtf8::convertToUnicode(*in, state));
}

//  char *QUtf8::convertFromUnicode(char *dst, QStringView in)
extern "C" Q_DECL_EXPORT
char *ritual_ZN5QUtf818convertFromUnicodeEPc11QStringView(
    char *dst,
    const QString *in) {
  return QUtf8::convertFromUnicode(dst, QStringView(*in));
}

//  QByteArray QUtf8::convertFromUnicode(QStringView in)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QUtf818convertFromUnicodeE11QStringView(
    const QString *in) {
  return new QByteArray(QUtf8::convertFromUnicode(QStringView(*in)));
}

//  QByteArray QUtf8::convertFromUnicode(QStringView in,
//      QStringConverter::State *state)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QUtf818convertFromUnicodeE11QStringViewPN20QStringConverterBase5StateE(
    const QString *in,
    QStringConverter::State *state) {
  return new QByteArray(QUtf8::convertFromUnicode(QStringView(*in), state));
}

//  char *QUtf8::convertFromLatin1(char *out, QLatin1StringView in)
extern "C" Q_DECL_EXPORT
char *ritual_ZN5QUtf817convertFromLatin1EPc13QLatin1String(
    char *out,
    const QLatin1String *in) {
  return QUtf8::convertFromLatin1(out, *in);
}

//  int QUtf8::compareUtf8(QByteArrayView utf8, QLatin1StringView s,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QUtf811compareUtf8E14QByteArrayView13QLatin1StringN2Qt15CaseSensitivityE(
    const QByteArrayView *utf8,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return QUtf8::compareUtf8(*utf8, *s, cs);
}

//  QUtf8::~QUtf8()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QUtf8D1Ev(QUtf8 *self) {
  delete self;
}

//  static char16_t *QUtf8::convertToUnicode(char16_t *dst, QByteArrayView
//      in)
extern "C" Q_DECL_EXPORT
char16_t *ritual_ZN5QUtf816convertToUnicodeEPDs14QByteArrayView(
    char16_t *dst,
    const QByteArrayView *in) {
  return QUtf8::convertToUnicode(dst, *in);
}
