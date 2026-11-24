//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanframeprocessor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanframeprocessor.h>
#include <QtCore/qvariant.h>
#include <QtSerialBus/qcanbusframe.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtSerialBus/qcanuniqueiddescription.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QCanFrameProcessor::QCanFrameProcessor()
extern "C" Q_DECL_EXPORT
QCanFrameProcessor *ritual_ZN18QCanFrameProcessorC1Ev() {
  return new QCanFrameProcessor();
}

//  QCanFrameProcessor::~QCanFrameProcessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessorD1Ev(QCanFrameProcessor *self) {
  delete self;
}

//  QCanBusFrame QCanFrameProcessor::prepareFrame(QtCanBus::UniqueId
//      uniqueId, const QVariantMap &signalValues)
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_ZN18QCanFrameProcessor12prepareFrameEN8QtCanBus8UniqueIdERK4QMapI7QString8QVariantE(
    QCanFrameProcessor *self,
    QtCanBus::UniqueId uniqueId,
    const QMap<QString, QVariant> *signalValues) {
  return new QCanBusFrame(self->prepareFrame(uniqueId, *signalValues));
}

//  ParseResult QCanFrameProcessor::parseFrame(const QCanBusFrame &frame)
extern "C" Q_DECL_EXPORT
QCanFrameProcessor::ParseResult *ritual_ZN18QCanFrameProcessor10parseFrameERK12QCanBusFrame(
    QCanFrameProcessor *self,
    const QCanBusFrame *frame) {
  return new QCanFrameProcessor::ParseResult(self->parseFrame(*frame));
}

//  Error QCanFrameProcessor::error() const
extern "C" Q_DECL_EXPORT
QCanFrameProcessor::Error ritual_ZNK18QCanFrameProcessor5errorEv(
    const QCanFrameProcessor *self) {
  return self->error();
}

//  QString QCanFrameProcessor::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCanFrameProcessor11errorStringEv(
    const QCanFrameProcessor *self) {
  return new QString(self->errorString());
}

//  QStringList QCanFrameProcessor::warnings() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QCanFrameProcessor8warningsEv(
    const QCanFrameProcessor *self) {
  return new QList<QString>(self->warnings());
}

//  QList<QCanMessageDescription> QCanFrameProcessor::messageDescriptions()
//      const
extern "C" Q_DECL_EXPORT
QList<QCanMessageDescription> *ritual_ZNK18QCanFrameProcessor19messageDescriptionsEv(
    const QCanFrameProcessor *self) {
  return new QList<QCanMessageDescription>(self->messageDescriptions());
}

//  void QCanFrameProcessor::addMessageDescriptions(const
//      QList<QCanMessageDescription> &descriptions)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessor22addMessageDescriptionsERK5QListI22QCanMessageDescriptionE(
    QCanFrameProcessor *self,
    const QList<QCanMessageDescription> *descriptions) {
  self->addMessageDescriptions(*descriptions);
}

//  void QCanFrameProcessor::setMessageDescriptions(const
//      QList<QCanMessageDescription> &descriptions)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessor22setMessageDescriptionsERK5QListI22QCanMessageDescriptionE(
    QCanFrameProcessor *self,
    const QList<QCanMessageDescription> *descriptions) {
  self->setMessageDescriptions(*descriptions);
}

//  void QCanFrameProcessor::clearMessageDescriptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessor24clearMessageDescriptionsEv(
    QCanFrameProcessor *self) {
  self->clearMessageDescriptions();
}

//  QCanUniqueIdDescription QCanFrameProcessor::uniqueIdDescription() const
extern "C" Q_DECL_EXPORT
QCanUniqueIdDescription *ritual_ZNK18QCanFrameProcessor19uniqueIdDescriptionEv(
    const QCanFrameProcessor *self) {
  return new QCanUniqueIdDescription(self->uniqueIdDescription());
}

//  void QCanFrameProcessor::setUniqueIdDescription(const
//      QCanUniqueIdDescription &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanFrameProcessor22setUniqueIdDescriptionERK23QCanUniqueIdDescription(
    QCanFrameProcessor *self,
    const QCanUniqueIdDescription *description) {
  self->setUniqueIdDescription(*description);
}
