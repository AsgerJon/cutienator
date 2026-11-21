//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtextstream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>

//  QTextStream::QTextStream()
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1Ev() {
  return new QTextStream();
}

//  QTextStream::QTextStream(QIODevice *device)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1EP9QIODevice(QIODevice *device) {
  return new QTextStream(device);
}

//  QTextStream::QTextStream(QString *string, OpenMode openMode)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1EP7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QString *string,
    int openMode) {
  return new QTextStream(
      string,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  QTextStream::QTextStream(QByteArray *array, OpenMode openMode)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1EP10QByteArray6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QByteArray *array,
    int openMode) {
  return new QTextStream(
      array,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  QTextStream::QTextStream(const QByteArray &array, OpenMode openMode)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1ERK10QByteArray6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    const QByteArray *array,
    int openMode) {
  return new QTextStream(
      *array,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  QTextStream::~QTextStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStreamD1Ev(QTextStream *self) {
  delete self;
}

//  void QTextStream::setEncoding(QStringConverter::Encoding encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream11setEncodingEN16QStringConverter8EncodingE(
    QTextStream *self,
    QStringConverter::Encoding encoding) {
  self->setEncoding(encoding);
}

//  QStringConverter::Encoding QTextStream::encoding() const
extern "C" Q_DECL_EXPORT
QStringConverter::Encoding ritual_ZNK11QTextStream8encodingEv(
    const QTextStream *self) {
  return self->encoding();
}

//  void QTextStream::setAutoDetectUnicode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream20setAutoDetectUnicodeEb(
    QTextStream *self,
    bool enabled) {
  self->setAutoDetectUnicode(enabled);
}

//  bool QTextStream::autoDetectUnicode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextStream17autoDetectUnicodeEv(const QTextStream *self) {
  return self->autoDetectUnicode();
}

//  void QTextStream::setGenerateByteOrderMark(bool generate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream24setGenerateByteOrderMarkEb(
    QTextStream *self,
    bool generate) {
  self->setGenerateByteOrderMark(generate);
}

//  bool QTextStream::generateByteOrderMark() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextStream21generateByteOrderMarkEv(
    const QTextStream *self) {
  return self->generateByteOrderMark();
}

//  void QTextStream::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream9setLocaleERK7QLocale(
    QTextStream *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QTextStream::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK11QTextStream6localeEv(const QTextStream *self) {
  return new QLocale(self->locale());
}

//  void QTextStream::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream9setDeviceEP9QIODevice(
    QTextStream *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QTextStream::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QTextStream6deviceEv(const QTextStream *self) {
  return self->device();
}

//  void QTextStream::setString(QString *string, OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream9setStringEP7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QTextStream *self,
    QString *string,
    int openMode) {
  self->setString(
      string,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  QString *QTextStream::string() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextStream6stringEv(const QTextStream *self) {
  return self->string();
}

//  Status QTextStream::status() const
extern "C" Q_DECL_EXPORT
QTextStream::Status ritual_ZNK11QTextStream6statusEv(
    const QTextStream *self) {
  return self->status();
}

//  void QTextStream::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream9setStatusENS_6StatusE(
    QTextStream *self,
    QTextStream::Status status) {
  self->setStatus(status);
}

//  void QTextStream::resetStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream11resetStatusEv(QTextStream *self) {
  self->resetStatus();
}

//  bool QTextStream::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextStream5atEndEv(const QTextStream *self) {
  return self->atEnd();
}

//  void QTextStream::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream5resetEv(QTextStream *self) {
  self->reset();
}

//  void QTextStream::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream5flushEv(QTextStream *self) {
  self->flush();
}

//  bool QTextStream::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTextStream4seekEx(QTextStream *self, qint64 pos) {
  return self->seek(pos);
}

//  qint64 QTextStream::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QTextStream3posEv(const QTextStream *self) {
  return self->pos();
}

//  void QTextStream::skipWhiteSpace()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream14skipWhiteSpaceEv(QTextStream *self) {
  self->skipWhiteSpace();
}

//  QString QTextStream::readLine(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTextStream8readLineEx(
    QTextStream *self,
    qint64 maxlen) {
  return new QString(self->readLine(maxlen));
}

//  bool QTextStream::readLineInto(QString *line, qint64 maxlen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTextStream12readLineIntoEP7QStringx(
    QTextStream *self,
    QString *line,
    qint64 maxlen) {
  return self->readLineInto(line, maxlen);
}

//  QString QTextStream::readAll()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTextStream7readAllEv(QTextStream *self) {
  return new QString(self->readAll());
}

//  QString QTextStream::read(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTextStream4readEx(QTextStream *self, qint64 maxlen) {
  return new QString(self->read(maxlen));
}

//  void QTextStream::setFieldAlignment(FieldAlignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream17setFieldAlignmentENS_14FieldAlignmentE(
    QTextStream *self,
    QTextStream::FieldAlignment alignment) {
  self->setFieldAlignment(alignment);
}

//  FieldAlignment QTextStream::fieldAlignment() const
extern "C" Q_DECL_EXPORT
QTextStream::FieldAlignment ritual_ZNK11QTextStream14fieldAlignmentEv(
    const QTextStream *self) {
  return self->fieldAlignment();
}

//  void QTextStream::setPadChar(QChar ch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream10setPadCharE5QChar(
    QTextStream *self,
    const QChar *ch) {
  self->setPadChar(*ch);
}

//  QChar QTextStream::padChar() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QTextStream7padCharEv(const QTextStream *self) {
  return new QChar(self->padChar());
}

//  void QTextStream::setFieldWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream13setFieldWidthEi(QTextStream *self, int width) {
  self->setFieldWidth(width);
}

//  int QTextStream::fieldWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextStream10fieldWidthEv(const QTextStream *self) {
  return self->fieldWidth();
}

//  void QTextStream::setNumberFlags(NumberFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream14setNumberFlagsE6QFlagsINS_10NumberFlagEE(
    QTextStream *self,
    int flags) {
  self->setNumberFlags(QFlags<QTextStream::NumberFlag>::fromInt(flags));
}

//  NumberFlags QTextStream::numberFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextStream11numberFlagsEv(const QTextStream *self) {
  return static_cast<int>(self->numberFlags().toInt());
}

//  void QTextStream::setIntegerBase(int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream14setIntegerBaseEi(QTextStream *self, int base) {
  self->setIntegerBase(base);
}

//  int QTextStream::integerBase() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextStream11integerBaseEv(const QTextStream *self) {
  return self->integerBase();
}

//  void QTextStream::setRealNumberNotation(RealNumberNotation notation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream21setRealNumberNotationENS_18RealNumberNotationE(
    QTextStream *self,
    QTextStream::RealNumberNotation notation) {
  self->setRealNumberNotation(notation);
}

//  RealNumberNotation QTextStream::realNumberNotation() const
extern "C" Q_DECL_EXPORT
QTextStream::RealNumberNotation ritual_ZNK11QTextStream18realNumberNotationEv(
    const QTextStream *self) {
  return self->realNumberNotation();
}

//  void QTextStream::setRealNumberPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextStream22setRealNumberPrecisionEi(
    QTextStream *self,
    int precision) {
  self->setRealNumberPrecision(precision);
}

//  int QTextStream::realNumberPrecision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextStream19realNumberPrecisionEv(const QTextStream *self) {
  return self->realNumberPrecision();
}

//  bool QTextStream::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextStreamcvbEv(const QTextStream *self) {
  return self->operator bool();
}
