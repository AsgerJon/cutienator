//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusframe.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QCanBusFrame::QCanBusFrame(FrameType type)
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_ZN12QCanBusFrameC1ENS_9FrameTypeE(
    QCanBusFrame::FrameType type) {
  return new QCanBusFrame(type);
}

//  QCanBusFrame::QCanBusFrame(QCanBusFrame::FrameId identifier, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_ZN12QCanBusFrameC1EjRK10QByteArray(
    QCanBusFrame::FrameId identifier,
    const QByteArray *data) {
  return new QCanBusFrame(identifier, *data);
}

//  bool QCanBusFrame::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame7isValidEv(const QCanBusFrame *self) {
  return self->isValid();
}

//  FrameType QCanBusFrame::frameType() const
extern "C" Q_DECL_EXPORT
QCanBusFrame::FrameType ritual_ZNK12QCanBusFrame9frameTypeEv(
    const QCanBusFrame *self) {
  return self->frameType();
}

//  void QCanBusFrame::setFrameType(FrameType newFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame12setFrameTypeENS_9FrameTypeE(
    QCanBusFrame *self,
    QCanBusFrame::FrameType newFormat) {
  self->setFrameType(newFormat);
}

//  bool QCanBusFrame::hasExtendedFrameFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame22hasExtendedFrameFormatEv(
    const QCanBusFrame *self) {
  return self->hasExtendedFrameFormat();
}

//  void QCanBusFrame::setExtendedFrameFormat(bool isExtended)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame22setExtendedFrameFormatEb(
    QCanBusFrame *self,
    bool isExtended) {
  self->setExtendedFrameFormat(isExtended);
}

//  QCanBusFrame::FrameId QCanBusFrame::frameId() const
extern "C" Q_DECL_EXPORT
QCanBusFrame::FrameId ritual_ZNK12QCanBusFrame7frameIdEv(
    const QCanBusFrame *self) {
  return self->frameId();
}

//  void QCanBusFrame::setFrameId(QCanBusFrame::FrameId newFrameId)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame10setFrameIdEj(
    QCanBusFrame *self,
    QCanBusFrame::FrameId newFrameId) {
  self->setFrameId(newFrameId);
}

//  void QCanBusFrame::setPayload(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame10setPayloadERK10QByteArray(
    QCanBusFrame *self,
    const QByteArray *data) {
  self->setPayload(*data);
}

//  void QCanBusFrame::setTimeStamp(TimeStamp ts)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame12setTimeStampENS_9TimeStampE(
    QCanBusFrame *self,
    const QCanBusFrame::TimeStamp *ts) {
  self->setTimeStamp(*ts);
}

//  QByteArray QCanBusFrame::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QCanBusFrame7payloadEv(const QCanBusFrame *self) {
  return new QByteArray(self->payload());
}

//  TimeStamp QCanBusFrame::timeStamp() const
extern "C" Q_DECL_EXPORT
QCanBusFrame::TimeStamp *ritual_ZNK12QCanBusFrame9timeStampEv(
    const QCanBusFrame *self) {
  return new QCanBusFrame::TimeStamp(self->timeStamp());
}

//  FrameErrors QCanBusFrame::error() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCanBusFrame5errorEv(const QCanBusFrame *self) {
  return static_cast<int>(self->error().toInt());
}

//  void QCanBusFrame::setError(FrameErrors e)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame8setErrorE6QFlagsINS_10FrameErrorEE(
    QCanBusFrame *self,
    int e) {
  self->setError(QFlags<QCanBusFrame::FrameError>::fromInt(e));
}

//  QString QCanBusFrame::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QCanBusFrame8toStringEv(const QCanBusFrame *self) {
  return new QString(self->toString());
}

//  bool QCanBusFrame::hasFlexibleDataRateFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame25hasFlexibleDataRateFormatEv(
    const QCanBusFrame *self) {
  return self->hasFlexibleDataRateFormat();
}

//  void QCanBusFrame::setFlexibleDataRateFormat(bool isFlexibleData)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame25setFlexibleDataRateFormatEb(
    QCanBusFrame *self,
    bool isFlexibleData) {
  self->setFlexibleDataRateFormat(isFlexibleData);
}

//  bool QCanBusFrame::hasBitrateSwitch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame16hasBitrateSwitchEv(const QCanBusFrame *self) {
  return self->hasBitrateSwitch();
}

//  void QCanBusFrame::setBitrateSwitch(bool bitrateSwitch)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame16setBitrateSwitchEb(
    QCanBusFrame *self,
    bool bitrateSwitch) {
  self->setBitrateSwitch(bitrateSwitch);
}

//  bool QCanBusFrame::hasErrorStateIndicator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame22hasErrorStateIndicatorEv(
    const QCanBusFrame *self) {
  return self->hasErrorStateIndicator();
}

//  void QCanBusFrame::setErrorStateIndicator(bool errorStateIndicator)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame22setErrorStateIndicatorEb(
    QCanBusFrame *self,
    bool errorStateIndicator) {
  self->setErrorStateIndicator(errorStateIndicator);
}

//  bool QCanBusFrame::hasLocalEcho() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanBusFrame12hasLocalEchoEv(const QCanBusFrame *self) {
  return self->hasLocalEcho();
}

//  void QCanBusFrame::setLocalEcho(bool localEcho)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame12setLocalEchoEb(
    QCanBusFrame *self,
    bool localEcho) {
  self->setLocalEcho(localEcho);
}

//  QCanBusFrame::~QCanBusFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrameD1Ev(QCanBusFrame *self) {
  delete self;
}

//  QList<QCanBusFrame>::QList()
extern "C" Q_DECL_EXPORT
QList<QCanBusFrame> *ritual_list_make_QCanBusFrame() {
  return new QList<QCanBusFrame>();
}

//  void QList<QCanBusFrame>::append(const QCanBusFrame &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCanBusFrame(
    QList<QCanBusFrame> *self,
    const QCanBusFrame *element) {
  self->append(*element);
}

//  qsizetype QList<QCanBusFrame>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCanBusFrame(const QList<QCanBusFrame> *self) {
  return self->size();
}

//  const QCanBusFrame &QList<QCanBusFrame>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_list_at_QCanBusFrame(
    const QList<QCanBusFrame> *self,
    long long index) {
  return new QCanBusFrame(self->at(index));
}

//  QList<QCanBusFrame>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCanBusFrame(QList<QCanBusFrame> *self) {
  delete self;
}
