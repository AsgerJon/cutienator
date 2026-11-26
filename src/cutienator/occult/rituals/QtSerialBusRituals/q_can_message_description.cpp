//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanmessagedescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qcansignaldescription.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QCanMessageDescription::QCanMessageDescription()
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN22QCanMessageDescriptionC1Ev() {
  return new QCanMessageDescription();
}

//  QCanMessageDescription::QCanMessageDescription(const
//      QCanMessageDescription &other)
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN22QCanMessageDescriptionC1ERKS_(
    const QCanMessageDescription *other) {
  return new QCanMessageDescription(*other);
}

//  QCanMessageDescription::QCanMessageDescription(QCanMessageDescription
//      &&other)
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN22QCanMessageDescriptionC1EOS_(
    QCanMessageDescription *other) {
  return new QCanMessageDescription(std::move(*other));
}

//  QCanMessageDescription::~QCanMessageDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescriptionD1Ev(QCanMessageDescription *self) {
  delete self;
}

//  QCanMessageDescription &QCanMessageDescription::operator=(const
//      QCanMessageDescription &other)
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN22QCanMessageDescriptionaSERKS_(
    QCanMessageDescription *self,
    const QCanMessageDescription *other) {
  return &(self->operator=(*other));
}

//  QCanMessageDescription
//      &QCanMessageDescription::operator=(QCanMessageDescription &&other)
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_ZN22QCanMessageDescriptionaSEOS_(
    QCanMessageDescription *self,
    QCanMessageDescription *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCanMessageDescription::swap(QCanMessageDescription &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription4swapERS_(
    QCanMessageDescription *self,
    QCanMessageDescription *other) {
  self->swap(*other);
}

//  bool QCanMessageDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QCanMessageDescription7isValidEv(
    const QCanMessageDescription *self) {
  return self->isValid();
}

//  QtCanBus::UniqueId QCanMessageDescription::uniqueId() const
extern "C" Q_DECL_EXPORT
QtCanBus::UniqueId ritual_ZNK22QCanMessageDescription8uniqueIdEv(
    const QCanMessageDescription *self) {
  return self->uniqueId();
}

//  void QCanMessageDescription::setUniqueId(QtCanBus::UniqueId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription11setUniqueIdEN8QtCanBus8UniqueIdE(
    QCanMessageDescription *self,
    QtCanBus::UniqueId id) {
  self->setUniqueId(id);
}

//  QString QCanMessageDescription::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QCanMessageDescription4nameEv(
    const QCanMessageDescription *self) {
  return new QString(self->name());
}

//  void QCanMessageDescription::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription7setNameERK7QString(
    QCanMessageDescription *self,
    const QString *name) {
  self->setName(*name);
}

//  quint8 QCanMessageDescription::size() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK22QCanMessageDescription4sizeEv(
    const QCanMessageDescription *self) {
  return self->size();
}

//  void QCanMessageDescription::setSize(quint8 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription7setSizeEh(
    QCanMessageDescription *self,
    quint8 size) {
  self->setSize(size);
}

//  QString QCanMessageDescription::transmitter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QCanMessageDescription11transmitterEv(
    const QCanMessageDescription *self) {
  return new QString(self->transmitter());
}

//  void QCanMessageDescription::setTransmitter(const QString &transmitter)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription14setTransmitterERK7QString(
    QCanMessageDescription *self,
    const QString *transmitter) {
  self->setTransmitter(*transmitter);
}

//  QString QCanMessageDescription::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QCanMessageDescription7commentEv(
    const QCanMessageDescription *self) {
  return new QString(self->comment());
}

//  void QCanMessageDescription::setComment(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription10setCommentERK7QString(
    QCanMessageDescription *self,
    const QString *text) {
  self->setComment(*text);
}

//  QList<QCanSignalDescription> QCanMessageDescription::signalDescriptions()
//      const
extern "C" Q_DECL_EXPORT
QList<QCanSignalDescription> *ritual_ZNK22QCanMessageDescription18signalDescriptionsEv(
    const QCanMessageDescription *self) {
  return new QList<QCanSignalDescription>(self->signalDescriptions());
}

//  QCanSignalDescription
//      QCanMessageDescription::signalDescriptionForName(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QCanSignalDescription *ritual_ZNK22QCanMessageDescription24signalDescriptionForNameERK7QString(
    const QCanMessageDescription *self,
    const QString *name) {
  return new QCanSignalDescription(self->signalDescriptionForName(*name));
}

//  void QCanMessageDescription::clearSignalDescriptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription23clearSignalDescriptionsEv(
    QCanMessageDescription *self) {
  self->clearSignalDescriptions();
}

//  void QCanMessageDescription::addSignalDescription(const
//      QCanSignalDescription &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription20addSignalDescriptionERK21QCanSignalDescription(
    QCanMessageDescription *self,
    const QCanSignalDescription *description) {
  self->addSignalDescription(*description);
}

//  void QCanMessageDescription::setSignalDescriptions(const
//      QList<QCanSignalDescription> &descriptions)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanMessageDescription21setSignalDescriptionsERK5QListI21QCanSignalDescriptionE(
    QCanMessageDescription *self,
    const QList<QCanSignalDescription> *descriptions) {
  self->setSignalDescriptions(*descriptions);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QCanMessageDescription &msg)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK22QCanMessageDescription(
    const QDebug *dbg,
    const QCanMessageDescription *msg) {
  return new QDebug(operator<<(*dbg, *msg));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QCanMessageDescription::debugStreaming(QDebug dbg, const
//      QCanMessageDescription &msg)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN22QCanMessageDescription14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QCanMessageDescription *msg) {
  return new QDebug(QCanMessageDescription::debugStreaming(*dbg, *msg));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QCanMessageDescription>::QList()
extern "C" Q_DECL_EXPORT
QList<QCanMessageDescription> *ritual_list_make_QCanMessageDescription() {
  return new QList<QCanMessageDescription>();
}

//  void QList<QCanMessageDescription>::append(const QCanMessageDescription
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCanMessageDescription(
    QList<QCanMessageDescription> *self,
    const QCanMessageDescription *element) {
  self->append(*element);
}

//  qsizetype QList<QCanMessageDescription>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCanMessageDescription(
    const QList<QCanMessageDescription> *self) {
  return self->size();
}

//  const QCanMessageDescription &QList<QCanMessageDescription>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QCanMessageDescription *ritual_list_at_QCanMessageDescription(
    const QList<QCanMessageDescription> *self,
    long long index) {
  return new QCanMessageDescription(self->at(index));
}

//  QList<QCanMessageDescription>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCanMessageDescription(
    QList<QCanMessageDescription> *self) {
  delete self;
}
