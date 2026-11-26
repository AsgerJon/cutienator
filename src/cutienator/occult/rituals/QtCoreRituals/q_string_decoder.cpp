//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringconverter.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again. Also added by hand on 2026-11-25, rituals for
//  functions the generator leaves out: 1.
#include <QtCore/qstringconverter.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/QStringDecoder>
#include <QtCore/QByteArrayView>
#include <QtCore/qbytearray.h>

//  QStringDecoder::QStringDecoder(const Interface *i)
extern "C" Q_DECL_EXPORT
QStringDecoder *ritual_ZN14QStringDecoderC1EPKN16QStringConverter9InterfaceE(
    const QStringConverter::Interface *i) {
  return new QStringDecoder(i);
}

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

//  FinalizeResultQChar QStringDecoder::finalize(QChar *out, qsizetype
//      maxlen)
extern "C" Q_DECL_EXPORT
QStringDecoder::FinalizeResultQChar *ritual_ZN14QStringDecoder8finalizeEP5QCharx(
    QStringDecoder *self,
    QChar *out,
    qsizetype maxlen) {
  return new QStringDecoder::FinalizeResultQChar(
      self->finalize(
          out,
          maxlen));
}

//  FinalizeResult QStringDecoder::finalize(char16_t *out, qsizetype maxlen)
extern "C" Q_DECL_EXPORT
QStringDecoder::FinalizeResult *ritual_ZN14QStringDecoder8finalizeEPDsx(
    QStringDecoder *self,
    char16_t *out,
    qsizetype maxlen) {
  return new QStringDecoder::FinalizeResult(self->finalize(out, maxlen));
}

//  FinalizeResult QStringDecoder::finalize()
extern "C" Q_DECL_EXPORT
QStringDecoder::FinalizeResult *ritual_ZN14QStringDecoder8finalizeEv(
    QStringDecoder *self) {
  return new QStringDecoder::FinalizeResult(self->finalize());
}

//  QStringDecoder QStringDecoder::decoderForHtml(QByteArrayView data)
extern "C" Q_DECL_EXPORT
QStringDecoder *ritual_ZN14QStringDecoder14decoderForHtmlE14QByteArrayView(
    const QByteArrayView *data) {
  return new QStringDecoder(QStringDecoder::decoderForHtml(*data));
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

//  a QStringDecoder::FinalizeResultQChar a ritual of QStringDecoder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringDecoder__QStringDecoder_FinalizeResultQChar(
    QStringDecoder::FinalizeResultQChar *self) {
  delete self;
}

//  a QStringDecoder::FinalizeResult a ritual of QStringDecoder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringDecoder__QStringDecoder_FinalizeResult(
    QStringDecoder::FinalizeResult *self) {
  delete self;
}

//  a QStringDecoder a ritual of QStringDecoder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringDecoder__QStringDecoder(QStringDecoder *self) {
  delete self;
}

//  QStringDecoder::EncodedData<const QByteArray &>
//      QStringDecoder::decode(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoder6decodeIvEENS_11EncodedDataIRK10QByteArrayEES4_(
    QStringDecoder *self,
    const QByteArray *ba) {
  return new QString(self->decode(*ba));
}

//  QStringDecoder::EncodedData<QByteArrayView>
//      QStringDecoder::decode(QByteArrayView ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoder6decodeE14QByteArrayView(
    QStringDecoder *self,
    const QByteArrayView *ba) {
  return new QString(self->decode(*ba));
}

//  QStringDecoder::EncodedData<const QByteArray &>
//      QStringDecoder::operator()(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoderclIvEENS_11EncodedDataIRK10QByteArrayEES4_(
    QStringDecoder *self,
    const QByteArray *ba) {
  return new QString((*self)(*ba));
}

//  QStringDecoder::EncodedData<QByteArrayView>
//      QStringDecoder::operator()(QByteArrayView ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStringDecoderclE14QByteArrayView(
    QStringDecoder *self,
    const QByteArrayView *ba) {
  return new QString((*self)(*ba));
}

//  char16_t *QStringDecoder::appendToBuffer(char16_t *out, QByteArrayView
//      ba)
extern "C" Q_DECL_EXPORT
char16_t *ritual_ZN14QStringDecoder14appendToBufferEPDs14QByteArrayView(
    QStringDecoder *self,
    char16_t *out,
    const QByteArrayView *ba) {
  return self->appendToBuffer(out, *ba);
}
