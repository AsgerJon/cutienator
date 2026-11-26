//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcborvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/QUtf8StringView>

//  const char *QtCbor::ByteData::byte() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK6QtCbor8ByteData4byteEv(const QtCbor::ByteData *self) {
  return self->byte();
}

//  char *QtCbor::ByteData::byte()
extern "C" Q_DECL_EXPORT
char *ritual_ZN6QtCbor8ByteData4byteEv(QtCbor::ByteData *self) {
  return self->byte();
}

//  const QChar *QtCbor::ByteData::utf16() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK6QtCbor8ByteData5utf16Ev(
    const QtCbor::ByteData *self) {
  return self->utf16();
}

//  QChar *QtCbor::ByteData::utf16()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN6QtCbor8ByteData5utf16Ev(QtCbor::ByteData *self) {
  return self->utf16();
}

//  QByteArray QtCbor::ByteData::toByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK6QtCbor8ByteData11toByteArrayEv(
    const QtCbor::ByteData *self) {
  return new QByteArray(self->toByteArray());
}

//  QString QtCbor::ByteData::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QtCbor8ByteData8toStringEv(
    const QtCbor::ByteData *self) {
  return new QString(self->toString());
}

//  QString QtCbor::ByteData::toUtf8String() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QtCbor8ByteData12toUtf8StringEv(
    const QtCbor::ByteData *self) {
  return new QString(self->toUtf8String());
}

//  QByteArray QtCbor::ByteData::asByteArrayView() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK6QtCbor8ByteData15asByteArrayViewEv(
    const QtCbor::ByteData *self) {
  return new QByteArray(self->asByteArrayView());
}

//  QLatin1StringView QtCbor::ByteData::asLatin1() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK6QtCbor8ByteData8asLatin1Ev(
    const QtCbor::ByteData *self) {
  return new QLatin1String(self->asLatin1());
}

//  QUtf8StringView QtCbor::ByteData::asUtf8StringView() const
extern "C" Q_DECL_EXPORT
QUtf8StringView *ritual_ZNK6QtCbor8ByteData16asUtf8StringViewEv(
    const QtCbor::ByteData *self) {
  return new QUtf8StringView(self->asUtf8StringView());
}

//  QStringView QtCbor::ByteData::asStringView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QtCbor8ByteData12asStringViewEv(
    const QtCbor::ByteData *self) {
  return new QString(self->asStringView().toString());
}

//  QString QtCbor::ByteData::asQStringRaw() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QtCbor8ByteData12asQStringRawEv(
    const QtCbor::ByteData *self) {
  return new QString(self->asQStringRaw());
}

//  QtCbor::ByteData::~ByteData()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QtCbor8ByteDataD1Ev(QtCbor::ByteData *self) {
  delete self;
}

//  a QUtf8StringView a ritual of QtCbor::ByteData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtCbor_ByteData__QUtf8StringView(QUtf8StringView *self) {
  delete self;
}
