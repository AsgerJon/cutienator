//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qtextcodec.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#if QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#include <QtCore5Compat/qtextcodec.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QTextDecoder::QTextDecoder(const QTextCodec *codec)
extern "C" Q_DECL_EXPORT
QTextDecoder *ritual_ZN12QTextDecoderC1EPK10QTextCodec(
    const QTextCodec *codec) {
  return new QTextDecoder(codec);
}

//  QTextDecoder::QTextDecoder(const QTextCodec *codec,
//      QTextCodec::ConversionFlags flags)
extern "C" Q_DECL_EXPORT
QTextDecoder *ritual_ZN12QTextDecoderC1EPK10QTextCodec6QFlagsIN20QStringConverterBase4FlagEE(
    const QTextCodec *codec,
    int flags) {
  return new QTextDecoder(
      codec,
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QTextDecoder::~QTextDecoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextDecoderD1Ev(QTextDecoder *self) {
  delete self;
}

//  QString QTextDecoder::toUnicode(const char *chars, int len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTextDecoder9toUnicodeEPKci(
    QTextDecoder *self,
    const char *chars,
    int len) {
  return new QString(self->toUnicode(chars, len));
}

//  QString QTextDecoder::toUnicode(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTextDecoder9toUnicodeERK10QByteArray(
    QTextDecoder *self,
    const QByteArray *ba) {
  return new QString(self->toUnicode(*ba));
}

//  void QTextDecoder::toUnicode(QString *target, const char *chars, int len)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextDecoder9toUnicodeEP7QStringPKci(
    QTextDecoder *self,
    QString *target,
    const char *chars,
    int len) {
  self->toUnicode(target, chars, len);
}

//  bool QTextDecoder::hasFailure() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextDecoder10hasFailureEv(const QTextDecoder *self) {
  return self->hasFailure();
}

//  bool QTextDecoder::needsMoreData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextDecoder13needsMoreDataEv(const QTextDecoder *self) {
  return self->needsMoreData();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec)
