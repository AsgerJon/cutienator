//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 10. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstringconverter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  uchar QUtf8BaseTraits::peekByte(const char *ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
uchar ritual_ZN15QUtf8BaseTraits8peekByteEPKcx(
    const char *ptr,
    qsizetype n) {
  return QUtf8BaseTraits::peekByte(ptr, n);
}

//  uchar QUtf8BaseTraits::peekByte(const uchar *ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
uchar ritual_ZN15QUtf8BaseTraits8peekByteEPKhx(
    const uchar *ptr,
    qsizetype n) {
  return QUtf8BaseTraits::peekByte(ptr, n);
}

//  uchar QUtf8BaseTraits::peekByte(const qchar8_t *ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
uchar ritual_ZN15QUtf8BaseTraits8peekByteEPK8qchar8_tx(
    const qchar8_t *ptr,
    qsizetype n) {
  return QUtf8BaseTraits::peekByte(ptr, n);
}

//  qptrdiff QUtf8BaseTraits::availableBytes(const char *ptr, const char
//      *end)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN15QUtf8BaseTraits14availableBytesEPKcS1_(
    const char *ptr,
    const char *end) {
  return QUtf8BaseTraits::availableBytes(ptr, end);
}

//  qptrdiff QUtf8BaseTraits::availableBytes(const uchar *ptr, const uchar
//      *end)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN15QUtf8BaseTraits14availableBytesEPKhS1_(
    const uchar *ptr,
    const uchar *end) {
  return QUtf8BaseTraits::availableBytes(ptr, end);
}

//  qptrdiff QUtf8BaseTraits::availableBytes(const qchar8_t *ptr, const
//      qchar8_t *end)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN15QUtf8BaseTraits14availableBytesEPK8qchar8_tS2_(
    const qchar8_t *ptr,
    const qchar8_t *end) {
  return QUtf8BaseTraits::availableBytes(ptr, end);
}

//  char16_t QUtf8BaseTraits::peekUtf16(const char16_t *ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
char16_t ritual_ZN15QUtf8BaseTraits9peekUtf16EPKDsx(
    const char16_t *ptr,
    qsizetype n) {
  return QUtf8BaseTraits::peekUtf16(ptr, n);
}

//  qptrdiff QUtf8BaseTraits::availableUtf16(const char16_t *ptr, const
//      char16_t *end)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN15QUtf8BaseTraits14availableUtf16EPKDsS1_(
    const char16_t *ptr,
    const char16_t *end) {
  return QUtf8BaseTraits::availableUtf16(ptr, end);
}

//  QUtf8BaseTraits::~QUtf8BaseTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraitsD1Ev(QUtf8BaseTraits *self) {
  delete self;
}

//  static void QUtf8BaseTraits::appendByte(uchar *&ptr, uchar b)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits10appendByteERPhh(
    uchar **ptr,
    uchar b) {
  QUtf8BaseTraits::appendByte(*ptr, b);
}

//  static void QUtf8BaseTraits::appendByte(qchar8_t *&ptr, qchar8_t b)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits10appendByteERP8qchar8_tS0_(
    qchar8_t **ptr,
    unsigned char b) {
  QUtf8BaseTraits::appendByte(*ptr, static_cast<qchar8_t>(b));
}

//  static void QUtf8BaseTraits::appendUtf16(char16_t *&ptr, char16_t uc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits11appendUtf16ERPDsDs(
    char16_t **ptr,
    char16_t uc) {
  QUtf8BaseTraits::appendUtf16(*ptr, uc);
}

//  static void QUtf8BaseTraits::appendUcs4(char16_t *&ptr, char32_t uc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits10appendUcs4ERPDsDi(
    char16_t **ptr,
    char32_t uc) {
  QUtf8BaseTraits::appendUcs4(*ptr, uc);
}

//  static void QUtf8BaseTraits::appendUtf16(char32_t *&ptr, char16_t uc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits11appendUtf16ERPDiDs(
    char32_t **ptr,
    char16_t uc) {
  QUtf8BaseTraits::appendUtf16(*ptr, uc);
}

//  static void QUtf8BaseTraits::appendUcs4(char32_t *&ptr, char32_t uc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits10appendUcs4ERPDiDi(
    char32_t **ptr,
    char32_t uc) {
  QUtf8BaseTraits::appendUcs4(*ptr, uc);
}

//  static void QUtf8BaseTraits::advanceByte(const char *&ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits11advanceByteERPKcx(
    const char **ptr,
    qsizetype n) {
  QUtf8BaseTraits::advanceByte(*ptr, n);
}

//  static void QUtf8BaseTraits::advanceByte(const uchar *&ptr, qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits11advanceByteERPKhx(
    const uchar **ptr,
    qsizetype n) {
  QUtf8BaseTraits::advanceByte(*ptr, n);
}

//  static void QUtf8BaseTraits::advanceByte(const qchar8_t *&ptr, qsizetype
//      n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits11advanceByteERPK8qchar8_tx(
    const qchar8_t **ptr,
    qsizetype n) {
  QUtf8BaseTraits::advanceByte(*ptr, n);
}

//  static void QUtf8BaseTraits::advanceUtf16(const char16_t *&ptr, qsizetype
//      n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraits12advanceUtf16ERPKDsx(
    const char16_t **ptr,
    qsizetype n) {
  QUtf8BaseTraits::advanceUtf16(*ptr, n);
}
