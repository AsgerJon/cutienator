//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergycharacteristic.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>

//  QLowEnergyCharacteristic::QLowEnergyCharacteristic()
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZN24QLowEnergyCharacteristicC1Ev() {
  return new QLowEnergyCharacteristic();
}

//  QLowEnergyCharacteristic::QLowEnergyCharacteristic(const
//      QLowEnergyCharacteristic &other)
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZN24QLowEnergyCharacteristicC1ERKS_(
    const QLowEnergyCharacteristic *other) {
  return new QLowEnergyCharacteristic(*other);
}

//  QLowEnergyCharacteristic::~QLowEnergyCharacteristic()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyCharacteristicD1Ev(
    QLowEnergyCharacteristic *self) {
  delete self;
}

//  QLowEnergyCharacteristic &QLowEnergyCharacteristic::operator=(const
//      QLowEnergyCharacteristic &other)
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZN24QLowEnergyCharacteristicaSERKS_(
    QLowEnergyCharacteristic *self,
    const QLowEnergyCharacteristic *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QLowEnergyCharacteristic &a, const
//      QLowEnergyCharacteristic &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QLowEnergyCharacteristicS1_(
    const QLowEnergyCharacteristic *a,
    const QLowEnergyCharacteristic *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyCharacteristic &a, const
//      QLowEnergyCharacteristic &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QLowEnergyCharacteristicS1_(
    const QLowEnergyCharacteristic *a,
    const QLowEnergyCharacteristic *b) {
  return operator!=(*a, *b);
}

//  QString QLowEnergyCharacteristic::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QLowEnergyCharacteristic4nameEv(
    const QLowEnergyCharacteristic *self) {
  return new QString(self->name());
}

//  QBluetoothUuid QLowEnergyCharacteristic::uuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK24QLowEnergyCharacteristic4uuidEv(
    const QLowEnergyCharacteristic *self) {
  return new QBluetoothUuid(self->uuid());
}

//  QByteArray QLowEnergyCharacteristic::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QLowEnergyCharacteristic5valueEv(
    const QLowEnergyCharacteristic *self) {
  return new QByteArray(self->value());
}

//  QLowEnergyCharacteristic::PropertyTypes
//      QLowEnergyCharacteristic::properties() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QLowEnergyCharacteristic10propertiesEv(
    const QLowEnergyCharacteristic *self) {
  return static_cast<int>(self->properties().toInt());
}

//  QLowEnergyDescriptor QLowEnergyCharacteristic::descriptor(const
//      QBluetoothUuid &uuid) const
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_ZNK24QLowEnergyCharacteristic10descriptorERK14QBluetoothUuid(
    const QLowEnergyCharacteristic *self,
    const QBluetoothUuid *uuid) {
  return new QLowEnergyDescriptor(self->descriptor(*uuid));
}

//  QList<QLowEnergyDescriptor> QLowEnergyCharacteristic::descriptors() const
extern "C" Q_DECL_EXPORT
QList<QLowEnergyDescriptor> *ritual_ZNK24QLowEnergyCharacteristic11descriptorsEv(
    const QLowEnergyCharacteristic *self) {
  return new QList<QLowEnergyDescriptor>(self->descriptors());
}

//  QLowEnergyDescriptor
//      QLowEnergyCharacteristic::clientCharacteristicConfiguration() const
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_ZNK24QLowEnergyCharacteristic33clientCharacteristicConfigurationEv(
    const QLowEnergyCharacteristic *self) {
  return new QLowEnergyDescriptor(self->clientCharacteristicConfiguration());
}

//  bool QLowEnergyCharacteristic::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLowEnergyCharacteristic7isValidEv(
    const QLowEnergyCharacteristic *self) {
  return self->isValid();
}

//  QLowEnergyHandle QLowEnergyCharacteristic::handle() const
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZNK24QLowEnergyCharacteristic6handleEv(
    const QLowEnergyCharacteristic *self) {
  return self->handle();
}

//  QLowEnergyHandle QLowEnergyCharacteristic::attributeHandle() const
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZNK24QLowEnergyCharacteristic15attributeHandleEv(
    const QLowEnergyCharacteristic *self) {
  return self->attributeHandle();
}

//  QLowEnergyCharacteristic::QLowEnergyCharacteristic(QSharedPointer<QLowEne
//      rgyServicePrivate> p, QLowEnergyHandle handle)
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZN24QLowEnergyCharacteristicC1E14QSharedPointerI24QLowEnergyServicePrivateEt(
    const QSharedPointer<QLowEnergyServicePrivate> *p,
    QLowEnergyHandle handle) {
  return new QLowEnergyCharacteristic(*p, handle);
}

//  bool QLowEnergyCharacteristic::equals(const QLowEnergyCharacteristic &a,
//      const QLowEnergyCharacteristic &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QLowEnergyCharacteristic6equalsERKS_S1_(
    const QLowEnergyCharacteristic *a,
    const QLowEnergyCharacteristic *b) {
  return QLowEnergyCharacteristic::equals(*a, *b);
}

//  QList<QLowEnergyCharacteristic>::QList()
extern "C" Q_DECL_EXPORT
QList<QLowEnergyCharacteristic> *ritual_list_make_QLowEnergyCharacteristic() {
  return new QList<QLowEnergyCharacteristic>();
}

//  void QList<QLowEnergyCharacteristic>::append(const
//      QLowEnergyCharacteristic &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLowEnergyCharacteristic(
    QList<QLowEnergyCharacteristic> *self,
    const QLowEnergyCharacteristic *element) {
  self->append(*element);
}

//  qsizetype QList<QLowEnergyCharacteristic>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLowEnergyCharacteristic(
    const QList<QLowEnergyCharacteristic> *self) {
  return self->size();
}

//  const QLowEnergyCharacteristic
//      &QList<QLowEnergyCharacteristic>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_list_at_QLowEnergyCharacteristic(
    const QList<QLowEnergyCharacteristic> *self,
    long long index) {
  return new QLowEnergyCharacteristic(self->at(index));
}

//  QList<QLowEnergyCharacteristic>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLowEnergyCharacteristic(
    QList<QLowEnergyCharacteristic> *self) {
  delete self;
}
