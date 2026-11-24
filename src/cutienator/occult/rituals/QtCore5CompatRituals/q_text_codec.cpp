//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qtextcodec.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#if QT_CONFIG(textcodec)
#include <QtCore5Compat/qtextcodec.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qchar.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTextCodec that Python can take functions over in. Every QTextCodec
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textcodec)
typedef const QByteArray * (*CuteQTextCodecCall0)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
typedef int (*CuteQTextCodecCall1)(const void *, int *);
#endif  // QT_CONFIG(textcodec)
class CuteQTextCodec : public QTextCodec {
public:
  using QTextCodec::QTextCodec;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec4nameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
    if (!std::strcmp(key, "_ZNK10QTextCodec7mibEnumEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textcodec)
    return false;
  }

#if QT_CONFIG(textcodec)
  //  QByteArray QTextCodec::name() const
  QByteArray name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextCodecCall0 call = reinterpret_cast<CuteQTextCodecCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(textcodec)

#if QT_CONFIG(textcodec)
  //  int QTextCodec::mibEnum() const
  int mibEnum() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextCodecCall1 call = reinterpret_cast<CuteQTextCodecCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(textcodec)
};

//  QTextCodec *QTextCodec::codecForName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec12codecForNameERK10QByteArray(
    const QByteArray *name) {
  return QTextCodec::codecForName(*name);
}

//  QTextCodec *QTextCodec::codecForName(const char *name)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec12codecForNameEPKc(const char *name) {
  return QTextCodec::codecForName(name);
}

//  QTextCodec *QTextCodec::codecForMib(int mib)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec11codecForMibEi(int mib) {
  return QTextCodec::codecForMib(mib);
}

//  QList<QByteArray> QTextCodec::availableCodecs()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN10QTextCodec15availableCodecsEv() {
  return new QList<QByteArray>(QTextCodec::availableCodecs());
}

//  QTextCodec *QTextCodec::codecForLocale()
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec14codecForLocaleEv() {
  return QTextCodec::codecForLocale();
}

//  void QTextCodec::setCodecForLocale(QTextCodec *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextCodec17setCodecForLocaleEPS_(QTextCodec *c) {
  QTextCodec::setCodecForLocale(c);
}

//  QTextCodec *QTextCodec::codecForTr()
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec10codecForTrEv() {
  return QTextCodec::codecForTr();
}

//  QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec12codecForHtmlERK10QByteArray(
    const QByteArray *ba) {
  return QTextCodec::codecForHtml(*ba);
}

//  QTextCodec *QTextCodec::codecForHtml(const QByteArray &ba, QTextCodec
//      *defaultCodec)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec12codecForHtmlERK10QByteArrayPS_(
    const QByteArray *ba,
    QTextCodec *defaultCodec) {
  return QTextCodec::codecForHtml(*ba, defaultCodec);
}

//  QTextCodec *QTextCodec::codecForUtfText(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec15codecForUtfTextERK10QByteArray(
    const QByteArray *ba) {
  return QTextCodec::codecForUtfText(*ba);
}

//  QTextCodec *QTextCodec::codecForUtfText(const QByteArray &ba, QTextCodec
//      *defaultCodec)
extern "C" Q_DECL_EXPORT
QTextCodec *ritual_ZN10QTextCodec15codecForUtfTextERK10QByteArrayPS_(
    const QByteArray *ba,
    QTextCodec *defaultCodec) {
  return QTextCodec::codecForUtfText(*ba, defaultCodec);
}

//  bool QTextCodec::canEncode(QChar a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextCodec9canEncodeE5QChar(
    const QTextCodec *self,
    const QChar *a0) {
  return self->canEncode(*a0);
}

//  bool QTextCodec::canEncode(const QString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextCodec9canEncodeERK7QString(
    const QTextCodec *self,
    const QString *a0) {
  return self->canEncode(*a0);
}

//  bool QTextCodec::canEncode(QStringView a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTextCodec9canEncodeE11QStringView(
    const QTextCodec *self,
    const QString *a0) {
  return self->canEncode(QStringView(*a0));
}

//  QString QTextCodec::toUnicode(const QByteArray &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTextCodec9toUnicodeERK10QByteArray(
    const QTextCodec *self,
    const QByteArray *a0) {
  return new QString(self->toUnicode(*a0));
}

//  QString QTextCodec::toUnicode(const char *chars) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTextCodec9toUnicodeEPKc(
    const QTextCodec *self,
    const char *chars) {
  return new QString(self->toUnicode(chars));
}

//  QByteArray QTextCodec::fromUnicode(const QString &uc) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QTextCodec11fromUnicodeERK7QString(
    const QTextCodec *self,
    const QString *uc) {
  return new QByteArray(self->fromUnicode(*uc));
}

//  QByteArray QTextCodec::fromUnicode(QStringView uc) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QTextCodec11fromUnicodeE11QStringView(
    const QTextCodec *self,
    const QString *uc) {
  return new QByteArray(self->fromUnicode(QStringView(*uc)));
}

//  QTextDecoder *QTextCodec::makeDecoder(ConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QTextDecoder *ritual_ZNK10QTextCodec11makeDecoderE6QFlagsIN20QStringConverterBase4FlagEE(
    const QTextCodec *self,
    int flags) {
  return self->makeDecoder(
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QTextEncoder *QTextCodec::makeEncoder(ConversionFlags flags) const
extern "C" Q_DECL_EXPORT
QTextEncoder *ritual_ZNK10QTextCodec11makeEncoderE6QFlagsIN20QStringConverterBase4FlagEE(
    const QTextCodec *self,
    int flags) {
  return self->makeEncoder(
      QFlags<QStringConverterBase::Flag>::fromInt(flags));
}

//  QByteArray QTextCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QTextCodec4nameEv(const QTextCodec *self) {
  return new QByteArray(self->name());
}

//  QList<QByteArray> QTextCodec::aliases() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK10QTextCodec7aliasesEv(const QTextCodec *self) {
  return new QList<QByteArray>(self->aliases());
}

//  int QTextCodec::mibEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextCodec7mibEnumEv(const QTextCodec *self) {
  return self->mibEnum();
}

//  QTextCodec::~QTextCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextCodecD1Ev(QTextCodec *self) {
  delete self;
}

//  a Python function taken by a CuteQTextCodec, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextCodec(QTextCodec *self, const char *key, void *call) {
  return static_cast<CuteQTextCodec *>(self)->take(key, call);
}

#endif  // QT_CONFIG(textcodec)
