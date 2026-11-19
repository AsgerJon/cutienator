//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qiodevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qiodevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QIODevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QIODevice10metaObjectEv(
    const QIODevice *self) {
  return self->metaObject();
}

//  QString QIODevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QIODevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIODevice::tr(s, c, n));
}

//  QIODevice::~QIODevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODeviceD1Ev(QIODevice *self) {
  delete self;
}

//  QIODeviceBase::OpenMode QIODevice::openMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice8openModeEv(const QIODevice *self) {
  return static_cast<int>(self->openMode().toInt());
}

//  void QIODevice::setTextModeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice18setTextModeEnabledEb(
    QIODevice *self,
    bool enabled) {
  self->setTextModeEnabled(enabled);
}

//  bool QIODevice::isTextModeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice17isTextModeEnabledEv(const QIODevice *self) {
  return self->isTextModeEnabled();
}

//  bool QIODevice::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice6isOpenEv(const QIODevice *self) {
  return self->isOpen();
}

//  bool QIODevice::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice10isReadableEv(const QIODevice *self) {
  return self->isReadable();
}

//  bool QIODevice::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice10isWritableEv(const QIODevice *self) {
  return self->isWritable();
}

//  bool QIODevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice12isSequentialEv(const QIODevice *self) {
  return self->isSequential();
}

//  int QIODevice::readChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice16readChannelCountEv(const QIODevice *self) {
  return self->readChannelCount();
}

//  int QIODevice::writeChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice17writeChannelCountEv(const QIODevice *self) {
  return self->writeChannelCount();
}

//  int QIODevice::currentReadChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice18currentReadChannelEv(const QIODevice *self) {
  return self->currentReadChannel();
}

//  void QIODevice::setCurrentReadChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice21setCurrentReadChannelEi(
    QIODevice *self,
    int channel) {
  self->setCurrentReadChannel(channel);
}

//  int QIODevice::currentWriteChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice19currentWriteChannelEv(const QIODevice *self) {
  return self->currentWriteChannel();
}

//  void QIODevice::setCurrentWriteChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice22setCurrentWriteChannelEi(
    QIODevice *self,
    int channel) {
  self->setCurrentWriteChannel(channel);
}

//  bool QIODevice::open(QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIODevice *self,
    int mode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QIODevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice5closeEv(QIODevice *self) {
  self->close();
}

//  qint64 QIODevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice3posEv(const QIODevice *self) {
  return self->pos();
}

//  qint64 QIODevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice4sizeEv(const QIODevice *self) {
  return self->size();
}

//  bool QIODevice::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice4seekEx(QIODevice *self, qint64 pos) {
  return self->seek(pos);
}

//  bool QIODevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice5atEndEv(const QIODevice *self) {
  return self->atEnd();
}

//  bool QIODevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice5resetEv(QIODevice *self) {
  return self->reset();
}

//  qint64 QIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice14bytesAvailableEv(const QIODevice *self) {
  return self->bytesAvailable();
}

//  qint64 QIODevice::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice12bytesToWriteEv(const QIODevice *self) {
  return self->bytesToWrite();
}

//  QByteArray QIODevice::read(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice4readEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->read(maxlen));
}

//  QByteArray QIODevice::readAll()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice7readAllEv(QIODevice *self) {
  return new QByteArray(self->readAll());
}

//  QByteArray QIODevice::readLine(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice8readLineEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->readLine(maxlen));
}

//  bool QIODevice::readLineInto(QByteArray *result, qint64 maxlen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice12readLineIntoEP10QByteArrayx(
    QIODevice *self,
    QByteArray *result,
    qint64 maxlen) {
  return self->readLineInto(result, maxlen);
}

//  bool QIODevice::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice11canReadLineEv(const QIODevice *self) {
  return self->canReadLine();
}

//  void QIODevice::startTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice16startTransactionEv(QIODevice *self) {
  self->startTransaction();
}

//  void QIODevice::commitTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice17commitTransactionEv(QIODevice *self) {
  self->commitTransaction();
}

//  void QIODevice::rollbackTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice19rollbackTransactionEv(QIODevice *self) {
  self->rollbackTransaction();
}

//  bool QIODevice::isTransactionStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice20isTransactionStartedEv(const QIODevice *self) {
  return self->isTransactionStarted();
}

//  qint64 QIODevice::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeEPKcx(
    QIODevice *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

//  qint64 QIODevice::write(const char *data)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeEPKc(QIODevice *self, const char *data) {
  return self->write(data);
}

//  qint64 QIODevice::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeERK10QByteArray(
    QIODevice *self,
    const QByteArray *data) {
  return self->write(*data);
}

//  QByteArray QIODevice::peek(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice4peekEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->peek(maxlen));
}

//  qint64 QIODevice::skip(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice4skipEx(QIODevice *self, qint64 maxSize) {
  return self->skip(maxSize);
}

//  bool QIODevice::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice16waitForReadyReadEi(QIODevice *self, int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QIODevice::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice19waitForBytesWrittenEi(QIODevice *self, int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  void QIODevice::ungetChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice9ungetCharEc(QIODevice *self, char c) {
  self->ungetChar(c);
}

//  bool QIODevice::putChar(char c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice7putCharEc(QIODevice *self, char c) {
  return self->putChar(c);
}

//  QString QIODevice::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QIODevice11errorStringEv(const QIODevice *self) {
  return new QString(self->errorString());
}
