//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qtextcodec.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#if QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#include <QtCore5Compat/qtextcodec.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringview.h>

//  QTextEncoder::QTextEncoder(const QTextCodec *codec)
extern "C" Q_DECL_EXPORT
QTextEncoder *ritual_ZN12QTextEncoderC1EPK10QTextCodec(
    const QTextCodec *codec) {
  return new QTextEncoder(codec);
}

//  QTextEncoder::QTextEncoder(const QTextCodec *codec,
//      QTextCodec::ConversionFlags flags)
extern "C" Q_DECL_EXPORT
QTextEncoder *ritual_ZN12QTextEncoderC1EPK10QTextCodec6QFlagsIN20QStringConverterBase4FlagEE(
    const QTextCodec *codec,
    int flags) {
  return new QTextEncoder(
      codec,
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QTextEncoder::~QTextEncoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextEncoderD1Ev(QTextEncoder *self) {
  delete self;
}

//  QByteArray QTextEncoder::fromUnicode(const QString &str)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QTextEncoder11fromUnicodeERK7QString(
    QTextEncoder *self,
    const QString *str) {
  return new QByteArray(self->fromUnicode(*str));
}

//  QByteArray QTextEncoder::fromUnicode(QStringView str)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QTextEncoder11fromUnicodeE11QStringView(
    QTextEncoder *self,
    const QString *str) {
  return new QByteArray(self->fromUnicode(QStringView(*str)));
}

//  QByteArray QTextEncoder::fromUnicode(const QChar *uc, int len)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN12QTextEncoder11fromUnicodeEPK5QChari(
    QTextEncoder *self,
    const QChar *uc,
    int len) {
  return new QByteArray(self->fromUnicode(uc, len));
}

//  bool QTextEncoder::hasFailure() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextEncoder10hasFailureEv(const QTextEncoder *self) {
  return self->hasFailure();
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(textcodec)
