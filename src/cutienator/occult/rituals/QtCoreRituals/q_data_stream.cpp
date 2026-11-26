//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatastream.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 1. Kept as it is when the
//  generator runs again. Also added by hand on 2026-11-25, rituals for
//  functions the generator leaves out: 3.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_DATASTREAM)
#include <QtCore/qdatastream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QDataStream::QDataStream()
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamC1Ev() {
  return new QDataStream();
}

//  QDataStream::QDataStream(QIODevice *a0)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamC1EP9QIODevice(QIODevice *a0) {
  return new QDataStream(a0);
}

//  QDataStream::QDataStream(QByteArray *a0, OpenMode flags)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamC1EP10QByteArray6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QByteArray *a0,
    int flags) {
  return new QDataStream(
      a0,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  QDataStream::QDataStream(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamC1ERK10QByteArray(const QByteArray *a0) {
  return new QDataStream(*a0);
}

//  QDataStream::~QDataStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStreamD1Ev(QDataStream *self) {
  delete self;
}

//  QIODevice *QDataStream::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QDataStream6deviceEv(const QDataStream *self) {
  return self->device();
}

//  void QDataStream::setDevice(QIODevice *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream9setDeviceEP9QIODevice(
    QDataStream *self,
    QIODevice *a0) {
  self->setDevice(a0);
}

//  bool QDataStream::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDataStream5atEndEv(const QDataStream *self) {
  return self->atEnd();
}

//  Status QDataStream::status() const
extern "C" Q_DECL_EXPORT
QDataStream::Status ritual_ZNK11QDataStream6statusEv(
    const QDataStream *self) {
  return self->status();
}

//  void QDataStream::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream9setStatusENS_6StatusE(
    QDataStream *self,
    QDataStream::Status status) {
  self->setStatus(status);
}

//  void QDataStream::resetStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream11resetStatusEv(QDataStream *self) {
  self->resetStatus();
}

//  FloatingPointPrecision QDataStream::floatingPointPrecision() const
extern "C" Q_DECL_EXPORT
QDataStream::FloatingPointPrecision ritual_ZNK11QDataStream22floatingPointPrecisionEv(
    const QDataStream *self) {
  return self->floatingPointPrecision();
}

//  void QDataStream::setFloatingPointPrecision(FloatingPointPrecision
//      precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream25setFloatingPointPrecisionENS_22FloatingPointPrecisionE(
    QDataStream *self,
    QDataStream::FloatingPointPrecision precision) {
  self->setFloatingPointPrecision(precision);
}

//  ByteOrder QDataStream::byteOrder() const
extern "C" Q_DECL_EXPORT
QDataStream::ByteOrder ritual_ZNK11QDataStream9byteOrderEv(
    const QDataStream *self) {
  return self->byteOrder();
}

//  void QDataStream::setByteOrder(ByteOrder a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream12setByteOrderENS_9ByteOrderE(
    QDataStream *self,
    QDataStream::ByteOrder a0) {
  self->setByteOrder(a0);
}

//  int QDataStream::version() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDataStream7versionEv(const QDataStream *self) {
  return self->version();
}

//  void QDataStream::setVersion(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream10setVersionEi(QDataStream *self, int a0) {
  self->setVersion(a0);
}

//  QDataStream &QDataStream::operator>>(char &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERc(QDataStream *self, char *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(qint8 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERa(QDataStream *self, qint8 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(quint8 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERh(QDataStream *self, quint8 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(qint16 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERs(QDataStream *self, qint16 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(quint16 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERt(QDataStream *self, quint16 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(qint32 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERi(QDataStream *self, qint32 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(quint32 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERj(QDataStream *self, quint32 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(qint64 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERx(QDataStream *self, qint64 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(quint64 &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERy(QDataStream *self, quint64 *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(std::nullptr_t &ptr)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERDn(
    QDataStream *self,
    std::nullptr_t *ptr) {
  return &(self->operator>>(*ptr));
}

//  QDataStream &QDataStream::operator>>(bool &i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERb(QDataStream *self, bool *i) {
  return &(self->operator>>(*i));
}

//  QDataStream &QDataStream::operator>>(float &f)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERf(QDataStream *self, float *f) {
  return &(self->operator>>(*f));
}

//  QDataStream &QDataStream::operator>>(double &f)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERd(QDataStream *self, double *f) {
  return &(self->operator>>(*f));
}

//  QDataStream &QDataStream::operator>>(char16_t &c)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERDs(QDataStream *self, char16_t *c) {
  return &(self->operator>>(*c));
}

//  QDataStream &QDataStream::operator>>(char32_t &c)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERDi(QDataStream *self, char32_t *c) {
  return &(self->operator>>(*c));
}

//  QDataStream &QDataStream::operator<<(char i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEc(QDataStream *self, char i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(qint8 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEa(QDataStream *self, qint8 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(quint8 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEh(QDataStream *self, quint8 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(qint16 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEs(QDataStream *self, qint16 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(quint16 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEt(QDataStream *self, quint16 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(qint32 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEi(QDataStream *self, qint32 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(quint32 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEj(QDataStream *self, quint32 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(qint64 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEx(QDataStream *self, qint64 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(quint64 i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEy(QDataStream *self, quint64 i) {
  return &(self->operator<<(i));
}

//  QDataStream &QDataStream::operator<<(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEDn(QDataStream *self) {
  return &(self->operator<<(nullptr));
}

//  QDataStream &QDataStream::operator<<(float f)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEf(QDataStream *self, float f) {
  return &(self->operator<<(f));
}

//  QDataStream &QDataStream::operator<<(double f)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEd(QDataStream *self, double f) {
  return &(self->operator<<(f));
}

//  QDataStream &QDataStream::operator<<(const char *str)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEPKc(
    QDataStream *self,
    const char *str) {
  return &(self->operator<<(str));
}

//  QDataStream &QDataStream::operator<<(char16_t c)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEDs(QDataStream *self, char16_t c) {
  return &(self->operator<<(c));
}

//  QDataStream &QDataStream::operator<<(char32_t c)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsEDi(QDataStream *self, char32_t c) {
  return &(self->operator<<(c));
}

//  bool QDataStream::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDataStreamcvbEv(const QDataStream *self) {
  return self->operator bool();
}

//  qint64 QDataStream::readRawData(char *a0, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QDataStream11readRawDataEPcx(
    QDataStream *self,
    char *a0,
    qint64 len) {
  return self->readRawData(a0, len);
}

//  QDataStream &QDataStream::writeBytes(const char *a0, qint64 len)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStream10writeBytesEPKcx(
    QDataStream *self,
    const char *a0,
    qint64 len) {
  return &(self->writeBytes(a0, len));
}

//  qint64 QDataStream::writeRawData(const char *a0, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QDataStream12writeRawDataEPKcx(
    QDataStream *self,
    const char *a0,
    qint64 len) {
  return self->writeRawData(a0, len);
}

//  qint64 QDataStream::skipRawData(qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QDataStream11skipRawDataEx(QDataStream *self, qint64 len) {
  return self->skipRawData(len);
}

//  void QDataStream::startTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream16startTransactionEv(QDataStream *self) {
  self->startTransaction();
}

//  bool QDataStream::commitTransaction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDataStream17commitTransactionEv(QDataStream *self) {
  return self->commitTransaction();
}

//  void QDataStream::rollbackTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream19rollbackTransactionEv(QDataStream *self) {
  self->rollbackTransaction();
}

//  void QDataStream::abortTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDataStream16abortTransactionEv(QDataStream *self) {
  self->abortTransaction();
}

//  bool QDataStream::isDeviceTransactionStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDataStream26isDeviceTransactionStartedEv(
    const QDataStream *self) {
  return self->isDeviceTransactionStarted();
}

//  qint64 QDataStream::readBlock(char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QDataStream9readBlockEPcx(
    QDataStream *self,
    char *data,
    qint64 len) {
  return self->readBlock(data, len);
}

//  qint64 QDataStream::readQSizeType(QDataStream &s)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QDataStream13readQSizeTypeERS_(QDataStream *s) {
  return QDataStream::readQSizeType(*s);
}

//  bool QDataStream::writeQSizeType(QDataStream &s, qint64 value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QDataStream14writeQSizeTypeERS_x(
    QDataStream *s,
    qint64 value) {
  return QDataStream::writeQSizeType(*s, value);
}

//  QDataStream &operator<<(QDataStream &out, const QString &str)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK7QString(
    QDataStream *out,
    const QString *str) {
  return &(operator<<(*out, *str));
}

//  QDataStream &operator>>(QDataStream &in, QString &str)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR7QString(
    QDataStream *in,
    QString *str) {
  return &(operator>>(*in, *str));
}

//  QDataStream &operator<<(QDataStream &out, const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK10QByteArray(
    QDataStream *out,
    const QByteArray *ba) {
  return &(operator<<(*out, *ba));
}

//  QDataStream &operator>>(QDataStream &in, QByteArray &ba)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR10QByteArray(
    QDataStream *in,
    QByteArray *ba) {
  return &(operator>>(*in, *ba));
}

//  template <typename T, std::enable_if_t<std::is_same_v<T, bool>, bool>
//  = true> QDataStream &QDataStream::operator<< <bool, true>(bool i)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamlsIbLb1EEERS_T_(
    QDataStream *self,
    bool i) {
  return &(self->operator<< <bool>(i));
}

//  QDataStream &QDataStream::operator>>(char *&str)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStreamrsERPc(
    QDataStream *self,
    char **str) {
  return &(*self >> *str);
}

#if QT_DEPRECATED_SINCE(6, 11)
//  QDataStream &QDataStream::readBytes(char *&a0, uint &len)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStream9readBytesERPcRj(
    QDataStream *self,
    char **a0,
    uint *len) {
  return &(self->readBytes(*a0, *len));
}
#endif

//  QDataStream &QDataStream::readBytes(char *&a0, qint64 &len)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN11QDataStream9readBytesERPcRx(
    QDataStream *self,
    char **a0,
    qint64 *len) {
  return &(self->readBytes(*a0, *len));
}

#endif  // !defined(QT_NO_DATASTREAM)
