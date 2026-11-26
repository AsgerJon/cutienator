//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbus.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbus.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qcanbusdeviceinfo.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QCanBus::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QCanBus10metaObjectEv(const QCanBus *self) {
  return self->metaObject();
}

//  void *QCanBus::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QCanBus11qt_metacastEPKc(QCanBus *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCanBus::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QCanBus11qt_metacallEN11QMetaObject4CallEiPPv(
    QCanBus *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCanBus::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QCanBus2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QCanBus::tr(s, c, n));
}

//  QCanBus *QCanBus::instance()
extern "C" Q_DECL_EXPORT
QCanBus *ritual_ZN7QCanBus8instanceEv() {
  return QCanBus::instance();
}

//  QStringList QCanBus::plugins() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QCanBus7pluginsEv(const QCanBus *self) {
  return new QList<QString>(self->plugins());
}

//  QList<QCanBusDeviceInfo> QCanBus::availableDevices(const QString &plugin,
//      QString *errorMessage) const
extern "C" Q_DECL_EXPORT
QList<QCanBusDeviceInfo> *ritual_ZNK7QCanBus16availableDevicesERK7QStringPS0_(
    const QCanBus *self,
    const QString *plugin,
    QString *errorMessage) {
  return new QList<QCanBusDeviceInfo>(
      self->availableDevices(
          *plugin,
          errorMessage));
}

//  QList<QCanBusDeviceInfo> QCanBus::availableDevices(QString *errorMessage)
//      const
extern "C" Q_DECL_EXPORT
QList<QCanBusDeviceInfo> *ritual_ZNK7QCanBus16availableDevicesEP7QString(
    const QCanBus *self,
    QString *errorMessage) {
  return new QList<QCanBusDeviceInfo>(self->availableDevices(errorMessage));
}

//  QCanBusDevice *QCanBus::createDevice(const QString &plugin, const QString
//      &interfaceName, QString *errorMessage) const
extern "C" Q_DECL_EXPORT
QCanBusDevice *ritual_ZNK7QCanBus12createDeviceERK7QStringS2_PS0_(
    const QCanBus *self,
    const QString *plugin,
    const QString *interfaceName,
    QString *errorMessage) {
  return self->createDevice(*plugin, *interfaceName, errorMessage);
}

//  QCanBus::QCanBus(QObject *parent)
extern "C" Q_DECL_EXPORT
QCanBus *ritual_ZN7QCanBusC1EP7QObject(QObject *parent) {
  return new QCanBus(parent);
}
