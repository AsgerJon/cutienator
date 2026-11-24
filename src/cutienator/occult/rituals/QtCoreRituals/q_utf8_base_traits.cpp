//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes
//  made here are lost.
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

//  qptrdiff QUtf8BaseTraits::availableBytes(const char *ptr, const char
//      *end)
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZN15QUtf8BaseTraits14availableBytesEPKcS1_(
    const char *ptr,
    const char *end) {
  return QUtf8BaseTraits::availableBytes(ptr, end);
}

//  QUtf8BaseTraits::~QUtf8BaseTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QUtf8BaseTraitsD1Ev(QUtf8BaseTraits *self) {
  delete self;
}
