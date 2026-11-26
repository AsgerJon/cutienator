//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstringconverter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearray.h>

#if !defined(Q_OS_WIN) || defined(QT_BOOTSTRAPPED)
//  QString QLocal8Bit::convertToUnicode(QByteArrayView in,
//      QStringConverter::State *state)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QLocal8Bit16convertToUnicodeE14QByteArrayViewPN20QStringConverterBase5StateE(
    const QByteArrayView *in,
    QStringConverter::State *state) {
  return new QString(QLocal8Bit::convertToUnicode(*in, state));
}
#endif  // !defined(Q_OS_WIN) || defined(QT_BOOTSTRAPPED)

#if !defined(Q_OS_WIN) || defined(QT_BOOTSTRAPPED)
//  QByteArray QLocal8Bit::convertFromUnicode(QStringView in,
//      QStringConverter::State *state)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QLocal8Bit18convertFromUnicodeE11QStringViewPN20QStringConverterBase5StateE(
    const QString *in,
    QStringConverter::State *state) {
  return new QByteArray(
      QLocal8Bit::convertFromUnicode(
          QStringView(*in),
          state));
}
#endif  // !defined(Q_OS_WIN) || defined(QT_BOOTSTRAPPED)

//  QLocal8Bit::~QLocal8Bit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QLocal8BitD1Ev(QLocal8Bit *self) {
  delete self;
}
