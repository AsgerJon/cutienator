//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/qserialportinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialPort/qserialportinfo.h>
#include <QtCore/qstring.h>
#include <QtSerialPort/QtSerialPort>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialPort/6.12.0/QtSerialPort/private/qserialportinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSerialPortInfoPrivate *QSerialPortInfo::d_func()
extern "C" Q_DECL_EXPORT
QSerialPortInfoPrivate *ritual_ZN15QSerialPortInfo6d_funcEv(
    QSerialPortInfo *self) {
  return self->d_func();
}

//  const QSerialPortInfoPrivate *QSerialPortInfo::d_func() const
extern "C" Q_DECL_EXPORT
const QSerialPortInfoPrivate *ritual_ZNK15QSerialPortInfo6d_funcEv(
    const QSerialPortInfo *self) {
  return self->d_func();
}

//  QSerialPortInfo::QSerialPortInfo()
extern "C" Q_DECL_EXPORT
QSerialPortInfo *ritual_ZN15QSerialPortInfoC1Ev() {
  return new QSerialPortInfo();
}

//  QSerialPortInfo::QSerialPortInfo(const QString &name)
extern "C" Q_DECL_EXPORT
QSerialPortInfo *ritual_ZN15QSerialPortInfoC1ERK7QString(
    const QString *name) {
  return new QSerialPortInfo(*name);
}

//  QSerialPortInfo::QSerialPortInfo(const QSerialPortInfo &other)
extern "C" Q_DECL_EXPORT
QSerialPortInfo *ritual_ZN15QSerialPortInfoC1ERKS_(
    const QSerialPortInfo *other) {
  return new QSerialPortInfo(*other);
}

//  QSerialPortInfo::~QSerialPortInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSerialPortInfoD1Ev(QSerialPortInfo *self) {
  delete self;
}

//  QString QSerialPortInfo::portName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSerialPortInfo8portNameEv(
    const QSerialPortInfo *self) {
  return new QString(self->portName());
}

//  QString QSerialPortInfo::systemLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSerialPortInfo14systemLocationEv(
    const QSerialPortInfo *self) {
  return new QString(self->systemLocation());
}

//  QString QSerialPortInfo::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSerialPortInfo11descriptionEv(
    const QSerialPortInfo *self) {
  return new QString(self->description());
}

//  QString QSerialPortInfo::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSerialPortInfo12manufacturerEv(
    const QSerialPortInfo *self) {
  return new QString(self->manufacturer());
}

//  QString QSerialPortInfo::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSerialPortInfo12serialNumberEv(
    const QSerialPortInfo *self) {
  return new QString(self->serialNumber());
}

//  quint16 QSerialPortInfo::vendorIdentifier() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QSerialPortInfo16vendorIdentifierEv(
    const QSerialPortInfo *self) {
  return self->vendorIdentifier();
}

//  quint16 QSerialPortInfo::productIdentifier() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QSerialPortInfo17productIdentifierEv(
    const QSerialPortInfo *self) {
  return self->productIdentifier();
}

//  bool QSerialPortInfo::hasVendorIdentifier() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSerialPortInfo19hasVendorIdentifierEv(
    const QSerialPortInfo *self) {
  return self->hasVendorIdentifier();
}

//  bool QSerialPortInfo::hasProductIdentifier() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSerialPortInfo20hasProductIdentifierEv(
    const QSerialPortInfo *self) {
  return self->hasProductIdentifier();
}

//  bool QSerialPortInfo::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSerialPortInfo6isNullEv(const QSerialPortInfo *self) {
  return self->isNull();
}

//  QList<QSerialPortInfo> QSerialPortInfo::availablePorts()
extern "C" Q_DECL_EXPORT
QList<QSerialPortInfo> *ritual_ZN15QSerialPortInfo14availablePortsEv() {
  return new QList<QSerialPortInfo>(QSerialPortInfo::availablePorts());
}

//  QSerialPortInfo::QSerialPortInfo(const QSerialPortInfoPrivate &dd)
extern "C" Q_DECL_EXPORT
QSerialPortInfo *ritual_ZN15QSerialPortInfoC1ERK22QSerialPortInfoPrivate(
    const QSerialPortInfoPrivate *dd) {
  return new QSerialPortInfo(*dd);
}

//  QList<QSerialPortInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QSerialPortInfo> *ritual_list_make_QSerialPortInfo() {
  return new QList<QSerialPortInfo>();
}

//  void QList<QSerialPortInfo>::append(const QSerialPortInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSerialPortInfo(
    QList<QSerialPortInfo> *self,
    const QSerialPortInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QSerialPortInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSerialPortInfo(
    const QList<QSerialPortInfo> *self) {
  return self->size();
}

//  const QSerialPortInfo &QList<QSerialPortInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSerialPortInfo *ritual_list_at_QSerialPortInfo(
    const QList<QSerialPortInfo> *self,
    long long index) {
  return new QSerialPortInfo(self->at(index));
}

//  QList<QSerialPortInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSerialPortInfo(QList<QSerialPortInfo> *self) {
  delete self;
}
