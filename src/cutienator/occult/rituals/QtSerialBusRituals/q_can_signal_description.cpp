//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcansignaldescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qcansignaldescription.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QCanSignalDescription::QCanSignalDescription()
extern "C" Q_DECL_EXPORT
QCanSignalDescription *ritual_ZN21QCanSignalDescriptionC1Ev() {
  return new QCanSignalDescription();
}

//  QCanSignalDescription::QCanSignalDescription(const QCanSignalDescription
//      &other)
extern "C" Q_DECL_EXPORT
QCanSignalDescription *ritual_ZN21QCanSignalDescriptionC1ERKS_(
    const QCanSignalDescription *other) {
  return new QCanSignalDescription(*other);
}

//  QCanSignalDescription::~QCanSignalDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescriptionD1Ev(QCanSignalDescription *self) {
  delete self;
}

//  bool QCanSignalDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCanSignalDescription7isValidEv(
    const QCanSignalDescription *self) {
  return self->isValid();
}

//  QString QCanSignalDescription::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCanSignalDescription4nameEv(
    const QCanSignalDescription *self) {
  return new QString(self->name());
}

//  void QCanSignalDescription::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription7setNameERK7QString(
    QCanSignalDescription *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QCanSignalDescription::physicalUnit() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCanSignalDescription12physicalUnitEv(
    const QCanSignalDescription *self) {
  return new QString(self->physicalUnit());
}

//  void QCanSignalDescription::setPhysicalUnit(const QString &unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription15setPhysicalUnitERK7QString(
    QCanSignalDescription *self,
    const QString *unit) {
  self->setPhysicalUnit(*unit);
}

//  QString QCanSignalDescription::receiver() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCanSignalDescription8receiverEv(
    const QCanSignalDescription *self) {
  return new QString(self->receiver());
}

//  void QCanSignalDescription::setReceiver(const QString &receiver)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription11setReceiverERK7QString(
    QCanSignalDescription *self,
    const QString *receiver) {
  self->setReceiver(*receiver);
}

//  QString QCanSignalDescription::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QCanSignalDescription7commentEv(
    const QCanSignalDescription *self) {
  return new QString(self->comment());
}

//  void QCanSignalDescription::setComment(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription10setCommentERK7QString(
    QCanSignalDescription *self,
    const QString *text) {
  self->setComment(*text);
}

//  QtCanBus::DataSource QCanSignalDescription::dataSource() const
extern "C" Q_DECL_EXPORT
QtCanBus::DataSource ritual_ZNK21QCanSignalDescription10dataSourceEv(
    const QCanSignalDescription *self) {
  return self->dataSource();
}

//  void QCanSignalDescription::setDataSource(QtCanBus::DataSource source)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription13setDataSourceEN8QtCanBus10DataSourceE(
    QCanSignalDescription *self,
    QtCanBus::DataSource source) {
  self->setDataSource(source);
}

//  QSysInfo::Endian QCanSignalDescription::dataEndian() const
extern "C" Q_DECL_EXPORT
QSysInfo::Endian ritual_ZNK21QCanSignalDescription10dataEndianEv(
    const QCanSignalDescription *self) {
  return self->dataEndian();
}

//  void QCanSignalDescription::setDataEndian(QSysInfo::Endian endian)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription13setDataEndianEN8QSysInfo6EndianE(
    QCanSignalDescription *self,
    QSysInfo::Endian endian) {
  self->setDataEndian(endian);
}

//  QtCanBus::DataFormat QCanSignalDescription::dataFormat() const
extern "C" Q_DECL_EXPORT
QtCanBus::DataFormat ritual_ZNK21QCanSignalDescription10dataFormatEv(
    const QCanSignalDescription *self) {
  return self->dataFormat();
}

//  void QCanSignalDescription::setDataFormat(QtCanBus::DataFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription13setDataFormatEN8QtCanBus10DataFormatE(
    QCanSignalDescription *self,
    QtCanBus::DataFormat format) {
  self->setDataFormat(format);
}

//  quint16 QCanSignalDescription::startBit() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QCanSignalDescription8startBitEv(
    const QCanSignalDescription *self) {
  return self->startBit();
}

//  void QCanSignalDescription::setStartBit(quint16 bit)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription11setStartBitEt(
    QCanSignalDescription *self,
    quint16 bit) {
  self->setStartBit(bit);
}

//  quint16 QCanSignalDescription::bitLength() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QCanSignalDescription9bitLengthEv(
    const QCanSignalDescription *self) {
  return self->bitLength();
}

//  void QCanSignalDescription::setBitLength(quint16 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription12setBitLengthEt(
    QCanSignalDescription *self,
    quint16 length) {
  self->setBitLength(length);
}

//  double QCanSignalDescription::factor() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK21QCanSignalDescription6factorEv(
    const QCanSignalDescription *self) {
  return self->factor();
}

//  void QCanSignalDescription::setFactor(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription9setFactorEd(
    QCanSignalDescription *self,
    double factor) {
  self->setFactor(factor);
}

//  double QCanSignalDescription::offset() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK21QCanSignalDescription6offsetEv(
    const QCanSignalDescription *self) {
  return self->offset();
}

//  void QCanSignalDescription::setOffset(double offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription9setOffsetEd(
    QCanSignalDescription *self,
    double offset) {
  self->setOffset(offset);
}

//  double QCanSignalDescription::scaling() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK21QCanSignalDescription7scalingEv(
    const QCanSignalDescription *self) {
  return self->scaling();
}

//  void QCanSignalDescription::setScaling(double scaling)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription10setScalingEd(
    QCanSignalDescription *self,
    double scaling) {
  self->setScaling(scaling);
}

//  double QCanSignalDescription::minimum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK21QCanSignalDescription7minimumEv(
    const QCanSignalDescription *self) {
  return self->minimum();
}

//  double QCanSignalDescription::maximum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK21QCanSignalDescription7maximumEv(
    const QCanSignalDescription *self) {
  return self->maximum();
}

//  void QCanSignalDescription::setRange(double minimum, double maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription8setRangeEdd(
    QCanSignalDescription *self,
    double minimum,
    double maximum) {
  self->setRange(minimum, maximum);
}

//  QtCanBus::MultiplexState QCanSignalDescription::multiplexState() const
extern "C" Q_DECL_EXPORT
QtCanBus::MultiplexState ritual_ZNK21QCanSignalDescription14multiplexStateEv(
    const QCanSignalDescription *self) {
  return self->multiplexState();
}

//  void QCanSignalDescription::setMultiplexState(QtCanBus::MultiplexState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription17setMultiplexStateEN8QtCanBus14MultiplexStateE(
    QCanSignalDescription *self,
    QtCanBus::MultiplexState state) {
  self->setMultiplexState(state);
}

//  void QCanSignalDescription::clearMultiplexSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription21clearMultiplexSignalsEv(
    QCanSignalDescription *self) {
  self->clearMultiplexSignals();
}

//  void QCanSignalDescription::addMultiplexSignal(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription18addMultiplexSignalERK7QStringRK8QVariant(
    QCanSignalDescription *self,
    const QString *name,
    const QVariant *value) {
  self->addMultiplexSignal(*name, *value);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QCanSignalDescription &sig)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK21QCanSignalDescription(
    const QDebug *dbg,
    const QCanSignalDescription *sig) {
  return new QDebug(operator<<(*dbg, *sig));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QCanSignalDescription::debugStreaming(QDebug dbg, const
//      QCanSignalDescription &sig)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN21QCanSignalDescription14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QCanSignalDescription *sig) {
  return new QDebug(QCanSignalDescription::debugStreaming(*dbg, *sig));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QCanSignalDescription>::QList()
extern "C" Q_DECL_EXPORT
QList<QCanSignalDescription> *ritual_list_make_QCanSignalDescription() {
  return new QList<QCanSignalDescription>();
}

//  void QList<QCanSignalDescription>::append(const QCanSignalDescription
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCanSignalDescription(
    QList<QCanSignalDescription> *self,
    const QCanSignalDescription *element) {
  self->append(*element);
}

//  qsizetype QList<QCanSignalDescription>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCanSignalDescription(
    const QList<QCanSignalDescription> *self) {
  return self->size();
}

//  const QCanSignalDescription &QList<QCanSignalDescription>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QCanSignalDescription *ritual_list_at_QCanSignalDescription(
    const QList<QCanSignalDescription> *self,
    long long index) {
  return new QCanSignalDescription(self->at(index));
}

//  QList<QCanSignalDescription>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCanSignalDescription(
    QList<QCanSignalDescription> *self) {
  delete self;
}
