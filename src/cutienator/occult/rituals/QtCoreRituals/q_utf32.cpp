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

//  QString QUtf32::convertToUnicode(QByteArrayView a0,
//      QStringConverter::State *a1, DataEndianness a2)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QUtf3216convertToUnicodeE14QByteArrayViewPN20QStringConverterBase5StateE14DataEndianness(
    const QByteArrayView *a0,
    QStringConverter::State *a1,
    DataEndianness a2) {
  return new QString(QUtf32::convertToUnicode(*a0, a1, a2));
}

//  QByteArray QUtf32::convertFromUnicode(QStringView a0,
//      QStringConverter::State *a1, DataEndianness a2)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QUtf3218convertFromUnicodeE11QStringViewPN20QStringConverterBase5StateE14DataEndianness(
    const QString *a0,
    QStringConverter::State *a1,
    DataEndianness a2) {
  return new QByteArray(
      QUtf32::convertFromUnicode(
          QStringView(*a0),
          a1,
          a2));
}

//  QUtf32::~QUtf32()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QUtf32D1Ev(QUtf32 *self) {
  delete self;
}
