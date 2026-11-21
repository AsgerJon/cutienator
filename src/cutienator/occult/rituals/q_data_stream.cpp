//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatastream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdatastream.h>
#include <QtCore/qbytearray.h>

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

//  bool QDataStream::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDataStreamcvbEv(const QDataStream *self) {
  return self->operator bool();
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
