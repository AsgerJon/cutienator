//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>

//  QStringDecoder::QStringDecoder(Encoding encoding, Flags flags)
extern "C" Q_DECL_EXPORT
QStringDecoder *ritual_ZN14QStringDecoderC1EN16QStringConverter8EncodingE6QFlagsIN20QStringConverterBase4FlagEE(
    QStringConverter::Encoding encoding,
    int flags) {
  return new QStringDecoder(
      encoding,
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QStringDecoder::QStringDecoder()
extern "C" Q_DECL_EXPORT
QStringDecoder *ritual_ZN14QStringDecoderC1Ev() {
  return new QStringDecoder();
}

//  QStringDecoder::QStringDecoder(QAnyStringView name, Flags f)
extern "C" Q_DECL_EXPORT
QStringDecoder *ritual_ZN14QStringDecoderC1E14QAnyStringView6QFlagsIN20QStringConverterBase4FlagEE(
    const QString *name,
    int f) {
  return new QStringDecoder(
      QAnyStringView(*name),
      QFlags<QStringConverterBase::Flag>::fromInt(f));
}

//  qsizetype QStringDecoder::requiredSpace(qsizetype inputLength) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringDecoder13requiredSpaceEx(
    const QStringDecoder *self,
    qsizetype inputLength) {
  return self->requiredSpace(inputLength);
}

//  QChar *QStringDecoder::appendToBuffer(QChar *out, QByteArrayView ba)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN14QStringDecoder14appendToBufferEP5QChar14QByteArrayView(
    QStringDecoder *self,
    QChar *out,
    const QByteArrayView *ba) {
  return self->appendToBuffer(out, *ba);
}

//  QString QStringDecoder::invalidateAndReturnNull()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoder23invalidateAndReturnNullEv(
    QStringDecoder *self) {
  return new QString(self->invalidateAndReturnNull());
}

//  QString QStringDecoder::decodeAsStringImpl(QByteArrayView in)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoder18decodeAsStringImplE14QByteArrayView(
    QStringDecoder *self,
    const QByteArrayView *in) {
  return new QString(self->decodeAsStringImpl(*in));
}

//  QString QStringDecoder::decodeAsString(QByteArrayView in)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoder14decodeAsStringE14QByteArrayView(
    QStringDecoder *self,
    const QByteArrayView *in) {
  return new QString(self->decodeAsString(*in));
}
