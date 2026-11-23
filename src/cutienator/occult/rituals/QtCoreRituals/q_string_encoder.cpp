//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringview.h>

//  QStringEncoder::QStringEncoder()
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1Ev() {
  return new QStringEncoder();
}

//  QStringEncoder::QStringEncoder(Encoding encoding, Flags flags)
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1EN16QStringConverter8EncodingE6QFlagsIN20QStringConverterBase4FlagEE(
    QStringConverter::Encoding encoding,
    int flags) {
  return new QStringEncoder(
      encoding,
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QStringEncoder::QStringEncoder(QAnyStringView name, Flags flags)
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1E14QAnyStringView6QFlagsIN20QStringConverterBase4FlagEE(
    const QString *name,
    int flags) {
  return new QStringEncoder(
      QAnyStringView(*name),
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  qsizetype QStringEncoder::requiredSpace(qsizetype inputLength) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringEncoder13requiredSpaceEx(
    const QStringEncoder *self,
    qsizetype inputLength) {
  return self->requiredSpace(inputLength);
}

//  QByteArray QStringEncoder::invalidateAndReturnNull()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoder23invalidateAndReturnNullEv(
    QStringEncoder *self) {
  return new QByteArray(self->invalidateAndReturnNull());
}

//  QByteArray QStringEncoder::encodeAsByteArrayImpl(QStringView in)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoder21encodeAsByteArrayImplE11QStringView(
    QStringEncoder *self,
    const QString *in) {
  return new QByteArray(self->encodeAsByteArrayImpl(QStringView(*in)));
}

//  QByteArray QStringEncoder::encodeAsByteArray(QStringView in)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoder17encodeAsByteArrayE11QStringView(
    QStringEncoder *self,
    const QString *in) {
  return new QByteArray(self->encodeAsByteArray(QStringView(*in)));
}
