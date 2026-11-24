//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergydescriptor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QLowEnergyDescriptor::QLowEnergyDescriptor()
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_ZN20QLowEnergyDescriptorC1Ev() {
  return new QLowEnergyDescriptor();
}

//  QLowEnergyDescriptor::QLowEnergyDescriptor(const QLowEnergyDescriptor
//      &other)
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_ZN20QLowEnergyDescriptorC1ERKS_(
    const QLowEnergyDescriptor *other) {
  return new QLowEnergyDescriptor(*other);
}

//  QLowEnergyDescriptor::~QLowEnergyDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyDescriptorD1Ev(QLowEnergyDescriptor *self) {
  delete self;
}

//  bool operator==(const QLowEnergyDescriptor &a, const QLowEnergyDescriptor
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QLowEnergyDescriptorS1_(
    const QLowEnergyDescriptor *a,
    const QLowEnergyDescriptor *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyDescriptor &a, const QLowEnergyDescriptor
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QLowEnergyDescriptorS1_(
    const QLowEnergyDescriptor *a,
    const QLowEnergyDescriptor *b) {
  return operator!=(*a, *b);
}

//  bool QLowEnergyDescriptor::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QLowEnergyDescriptor7isValidEv(
    const QLowEnergyDescriptor *self) {
  return self->isValid();
}

//  QByteArray QLowEnergyDescriptor::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QLowEnergyDescriptor5valueEv(
    const QLowEnergyDescriptor *self) {
  return new QByteArray(self->value());
}

//  QBluetoothUuid QLowEnergyDescriptor::uuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK20QLowEnergyDescriptor4uuidEv(
    const QLowEnergyDescriptor *self) {
  return new QBluetoothUuid(self->uuid());
}

//  QString QLowEnergyDescriptor::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QLowEnergyDescriptor4nameEv(
    const QLowEnergyDescriptor *self) {
  return new QString(self->name());
}

//  QBluetoothUuid::DescriptorType QLowEnergyDescriptor::type() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid::DescriptorType ritual_ZNK20QLowEnergyDescriptor4typeEv(
    const QLowEnergyDescriptor *self) {
  return self->type();
}

//  QLowEnergyHandle QLowEnergyDescriptor::handle() const
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZNK20QLowEnergyDescriptor6handleEv(
    const QLowEnergyDescriptor *self) {
  return self->handle();
}

//  QLowEnergyHandle QLowEnergyDescriptor::characteristicHandle() const
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZNK20QLowEnergyDescriptor20characteristicHandleEv(
    const QLowEnergyDescriptor *self) {
  return self->characteristicHandle();
}

//  bool QLowEnergyDescriptor::equals(const QLowEnergyDescriptor &a, const
//      QLowEnergyDescriptor &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QLowEnergyDescriptor6equalsERKS_S1_(
    const QLowEnergyDescriptor *a,
    const QLowEnergyDescriptor *b) {
  return QLowEnergyDescriptor::equals(*a, *b);
}

//  QList<QLowEnergyDescriptor>::QList()
extern "C" Q_DECL_EXPORT
QList<QLowEnergyDescriptor> *ritual_list_make_QLowEnergyDescriptor() {
  return new QList<QLowEnergyDescriptor>();
}

//  void QList<QLowEnergyDescriptor>::append(const QLowEnergyDescriptor
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLowEnergyDescriptor(
    QList<QLowEnergyDescriptor> *self,
    const QLowEnergyDescriptor *element) {
  self->append(*element);
}

//  qsizetype QList<QLowEnergyDescriptor>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLowEnergyDescriptor(
    const QList<QLowEnergyDescriptor> *self) {
  return self->size();
}

//  const QLowEnergyDescriptor &QList<QLowEnergyDescriptor>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_list_at_QLowEnergyDescriptor(
    const QList<QLowEnergyDescriptor> *self,
    long long index) {
  return new QLowEnergyDescriptor(self->at(index));
}

//  QList<QLowEnergyDescriptor>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLowEnergyDescriptor(
    QList<QLowEnergyDescriptor> *self) {
  delete self;
}
