//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtextstream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>

//  QTextStreamPrivate *QTextStream::d_func()
extern "C" Q_DECL_EXPORT
QTextStreamPrivate *ritual_ZN11QTextStream6d_funcEv(QTextStream *self) {
  return self->d_func();
}

//  const QTextStreamPrivate *QTextStream::d_func() const
extern "C" Q_DECL_EXPORT
const QTextStreamPrivate *ritual_ZNK11QTextStream6d_funcEv(
    const QTextStream *self) {
  return self->d_func();
}

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

//  QTextStream::QTextStream(FILE *fileHandle, OpenMode openMode)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamC1EP8_IO_FILE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    FILE *fileHandle,
    int openMode) {
  return new QTextStream(
      fileHandle,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
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

//  QTextStream &QTextStream::operator>>(QChar &ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsER5QChar(QTextStream *self, QChar *ch) {
  return &(self->operator>>(*ch));
}

//  QTextStream &QTextStream::operator>>(char &ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERc(QTextStream *self, char *ch) {
  return &(self->operator>>(*ch));
}

//  QTextStream &QTextStream::operator>>(char16_t &ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERDs(QTextStream *self, char16_t *ch) {
  return &(self->operator>>(*ch));
}

//  QTextStream &QTextStream::operator>>(short &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERs(QTextStream *self, short *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(unsigned short &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERt(
    QTextStream *self,
    unsigned short *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(int &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERi(QTextStream *self, int *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(unsigned int &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERj(
    QTextStream *self,
    unsigned int *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(long &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERl(QTextStream *self, long *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(unsigned long &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERm(
    QTextStream *self,
    unsigned long *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(qlonglong &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERx(QTextStream *self, qlonglong *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(qulonglong &i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERy(QTextStream *self, qulonglong *i) {
  return &(self->operator>>(*i));
}

//  QTextStream &QTextStream::operator>>(float &f)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERf(QTextStream *self, float *f) {
  return &(self->operator>>(*f));
}

//  QTextStream &QTextStream::operator>>(double &f)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsERd(QTextStream *self, double *f) {
  return &(self->operator>>(*f));
}

//  QTextStream &QTextStream::operator>>(QString &s)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsER7QString(
    QTextStream *self,
    QString *s) {
  return &(self->operator>>(*s));
}

//  QTextStream &QTextStream::operator>>(QByteArray &array)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsER10QByteArray(
    QTextStream *self,
    QByteArray *array) {
  return &(self->operator>>(*array));
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 12)
//  QTextStream &QTextStream::operator>>(char *c)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamrsEPc(QTextStream *self, char *c) {
  return &(self->operator>>(c));
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 12)

//  QTextStream &QTextStream::operator<<(QChar ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsE5QChar(
    QTextStream *self,
    const QChar *ch) {
  return &(self->operator<<(*ch));
}

//  QTextStream &QTextStream::operator<<(char ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEc(QTextStream *self, char ch) {
  return &(self->operator<<(ch));
}

//  QTextStream &QTextStream::operator<<(char16_t ch)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEDs(QTextStream *self, char16_t ch) {
  return &(self->operator<<(ch));
}

//  QTextStream &QTextStream::operator<<(short i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEs(QTextStream *self, short i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(unsigned short i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEt(
    QTextStream *self,
    unsigned short i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(int i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEi(QTextStream *self, int i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(unsigned int i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEj(QTextStream *self, unsigned int i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(long i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEl(QTextStream *self, long i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(unsigned long i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEm(QTextStream *self, unsigned long i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(qlonglong i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEx(QTextStream *self, qlonglong i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(qulonglong i)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEy(QTextStream *self, qulonglong i) {
  return &(self->operator<<(i));
}

//  QTextStream &QTextStream::operator<<(float f)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEf(QTextStream *self, float f) {
  return &(self->operator<<(f));
}

//  QTextStream &QTextStream::operator<<(double f)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEd(QTextStream *self, double f) {
  return &(self->operator<<(f));
}

//  QTextStream &QTextStream::operator<<(const QString &s)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsERK7QString(
    QTextStream *self,
    const QString *s) {
  return &(self->operator<<(*s));
}

//  QTextStream &QTextStream::operator<<(QStringView s)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsE11QStringView(
    QTextStream *self,
    const QString *s) {
  return &(self->operator<<(QStringView(*s)));
}

//  QTextStream &QTextStream::operator<<(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsE13QLatin1String(
    QTextStream *self,
    const QLatin1String *s) {
  return &(self->operator<<(*s));
}

//  QTextStream &QTextStream::operator<<(const QByteArray &array)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsERK10QByteArray(
    QTextStream *self,
    const QByteArray *array) {
  return &(self->operator<<(*array));
}

//  QTextStream &QTextStream::operator<<(const char *c)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEPKc(QTextStream *self, const char *c) {
  return &(self->operator<<(c));
}

//  QTextStream &QTextStream::operator<<(const void *ptr)
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN11QTextStreamlsEPKv(
    QTextStream *self,
    const void *ptr) {
  return &(self->operator<<(ptr));
}

//  bool QTextStream::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextStreamcvbEv(const QTextStream *self) {
  return self->operator bool();
}
