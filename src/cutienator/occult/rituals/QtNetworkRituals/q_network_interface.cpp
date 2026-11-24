//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_NETWORKINTERFACE)
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qlist.h>

//  QNetworkInterface::QNetworkInterface()
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZN17QNetworkInterfaceC1Ev() {
  return new QNetworkInterface();
}

//  QNetworkInterface::QNetworkInterface(const QNetworkInterface &other)
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZN17QNetworkInterfaceC1ERKS_(
    const QNetworkInterface *other) {
  return new QNetworkInterface(*other);
}

//  QNetworkInterface::~QNetworkInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkInterfaceD1Ev(QNetworkInterface *self) {
  delete self;
}

//  bool QNetworkInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QNetworkInterface7isValidEv(const QNetworkInterface *self) {
  return self->isValid();
}

//  int QNetworkInterface::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QNetworkInterface5indexEv(const QNetworkInterface *self) {
  return self->index();
}

//  int QNetworkInterface::maximumTransmissionUnit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QNetworkInterface23maximumTransmissionUnitEv(
    const QNetworkInterface *self) {
  return self->maximumTransmissionUnit();
}

//  QString QNetworkInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QNetworkInterface4nameEv(
    const QNetworkInterface *self) {
  return new QString(self->name());
}

//  QString QNetworkInterface::humanReadableName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QNetworkInterface17humanReadableNameEv(
    const QNetworkInterface *self) {
  return new QString(self->humanReadableName());
}

//  InterfaceFlags QNetworkInterface::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QNetworkInterface5flagsEv(const QNetworkInterface *self) {
  return static_cast<int>(self->flags().toInt());
}

//  InterfaceType QNetworkInterface::type() const
extern "C" Q_DECL_EXPORT
QNetworkInterface::InterfaceType ritual_ZNK17QNetworkInterface4typeEv(
    const QNetworkInterface *self) {
  return self->type();
}

//  QString QNetworkInterface::hardwareAddress() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QNetworkInterface15hardwareAddressEv(
    const QNetworkInterface *self) {
  return new QString(self->hardwareAddress());
}

//  QList<QNetworkAddressEntry> QNetworkInterface::addressEntries() const
extern "C" Q_DECL_EXPORT
QList<QNetworkAddressEntry> *ritual_ZNK17QNetworkInterface14addressEntriesEv(
    const QNetworkInterface *self) {
  return new QList<QNetworkAddressEntry>(self->addressEntries());
}

//  int QNetworkInterface::interfaceIndexFromName(const QString &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QNetworkInterface22interfaceIndexFromNameERK7QString(
    const QString *name) {
  return QNetworkInterface::interfaceIndexFromName(*name);
}

//  QNetworkInterface QNetworkInterface::interfaceFromName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZN17QNetworkInterface17interfaceFromNameERK7QString(
    const QString *name) {
  return new QNetworkInterface(QNetworkInterface::interfaceFromName(*name));
}

//  QNetworkInterface QNetworkInterface::interfaceFromIndex(int index)
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZN17QNetworkInterface18interfaceFromIndexEi(
    int index) {
  return new QNetworkInterface(QNetworkInterface::interfaceFromIndex(index));
}

//  QString QNetworkInterface::interfaceNameFromIndex(int index)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QNetworkInterface22interfaceNameFromIndexEi(int index) {
  return new QString(QNetworkInterface::interfaceNameFromIndex(index));
}

//  QList<QNetworkInterface> QNetworkInterface::allInterfaces()
extern "C" Q_DECL_EXPORT
QList<QNetworkInterface> *ritual_ZN17QNetworkInterface13allInterfacesEv() {
  return new QList<QNetworkInterface>(QNetworkInterface::allInterfaces());
}

//  QList<QHostAddress> QNetworkInterface::allAddresses()
extern "C" Q_DECL_EXPORT
QList<QHostAddress> *ritual_ZN17QNetworkInterface12allAddressesEv() {
  return new QList<QHostAddress>(QNetworkInterface::allAddresses());
}

//  QList<QNetworkInterface>::QList()
extern "C" Q_DECL_EXPORT
QList<QNetworkInterface> *ritual_list_make_QNetworkInterface() {
  return new QList<QNetworkInterface>();
}

//  void QList<QNetworkInterface>::append(const QNetworkInterface &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNetworkInterface(
    QList<QNetworkInterface> *self,
    const QNetworkInterface *element) {
  self->append(*element);
}

//  qsizetype QList<QNetworkInterface>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNetworkInterface(
    const QList<QNetworkInterface> *self) {
  return self->size();
}

//  const QNetworkInterface &QList<QNetworkInterface>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_list_at_QNetworkInterface(
    const QList<QNetworkInterface> *self,
    long long index) {
  return new QNetworkInterface(self->at(index));
}

//  QList<QNetworkInterface>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNetworkInterface(QList<QNetworkInterface> *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKINTERFACE)
