//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QStringEncoder>

//  QStringEncoder::QStringEncoder(const Interface *i)
extern "C" Q_DECL_EXPORT
QStringEncoder *ritual_ZN14QStringEncoderC1EPKN16QStringConverter9InterfaceE(
    const QStringConverter::Interface *i) {
  return new QStringEncoder(i);
}

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

//  char *QStringEncoder::appendToBuffer(char *out, QStringView in)
extern "C" Q_DECL_EXPORT
char *ritual_ZN14QStringEncoder14appendToBufferEPc11QStringView(
    QStringEncoder *self,
    char *out,
    const QString *in) {
  return self->appendToBuffer(out, QStringView(*in));
}

//  FinalizeResult QStringEncoder::finalize(char *out, qsizetype maxlen)
extern "C" Q_DECL_EXPORT
QStringEncoder::FinalizeResult *ritual_ZN14QStringEncoder8finalizeEPcx(
    QStringEncoder *self,
    char *out,
    qsizetype maxlen) {
  return new QStringEncoder::FinalizeResult(self->finalize(out, maxlen));
}

//  FinalizeResult QStringEncoder::finalize()
extern "C" Q_DECL_EXPORT
QStringEncoder::FinalizeResult *ritual_ZN14QStringEncoder8finalizeEv(
    QStringEncoder *self) {
  return new QStringEncoder::FinalizeResult(self->finalize());
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

//  a QStringEncoder::FinalizeResult a ritual of QStringEncoder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringEncoder__QStringEncoder_FinalizeResult(
    QStringEncoder::FinalizeResult *self) {
  delete self;
}

//  QStringEncoder::DecodedData<const QString &>
//      QStringEncoder::encode(const QString &str)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoder6encodeIvEENS_11DecodedDataIRK7QStringEES4_(
    QStringEncoder *self,
    const QString *str) {
  return new QByteArray(self->encode(*str));
}

//  QStringEncoder::DecodedData<QStringView>
//      QStringEncoder::encode(QStringView in)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoder6encodeE11QStringView(
    QStringEncoder *self,
    const QStringView *in) {
  return new QByteArray(self->encode(*in));
}

//  QStringEncoder::DecodedData<const QString &>
//      QStringEncoder::operator()(const QString &str)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoderclIvEENS_11DecodedDataIRK7QStringEES4_(
    QStringEncoder *self,
    const QString *str) {
  return new QByteArray((*self)(*str));
}

//  QStringEncoder::DecodedData<QStringView>
//      QStringEncoder::operator()(QStringView in)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QStringEncoderclE11QStringView(
    QStringEncoder *self,
    const QStringView *in) {
  return new QByteArray((*self)(*in));
}
