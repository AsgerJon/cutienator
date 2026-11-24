//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusfactory.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qcanbusdeviceinfo.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCanBusFactory that Python can take functions over in. Every QCanBusFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanBusFactoryCall0)(const void *, const QString *, QString *, int *);
class CuteQCanBusFactory : public QCanBusFactory {
public:
  using QCanBusFactory::QCanBusFactory;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QCanBusFactory12createDeviceERK7QStringPS0_")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QCanBusDevice *QCanBusFactory::createDevice(const QString
  //      &interfaceName, QString *errorMessage) const
  QCanBusDevice *createDevice(
      const QString &interfaceName,
      QString *errorMessage) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanBusFactoryCall0 call = reinterpret_cast<CuteQCanBusFactoryCall0>(taken[0]);
      void * given = call(this, &interfaceName, errorMessage, &handled);
      if (handled) return static_cast<QCanBusDevice *>(given);
    }
    return {};
  }
};

//  QCanBusDevice *QCanBusFactory::createDevice(const QString &interfaceName,
//      QString *errorMessage) const
extern "C" Q_DECL_EXPORT
QCanBusDevice *ritual_ZNK14QCanBusFactory12createDeviceERK7QStringPS0_(
    const QCanBusFactory *self,
    const QString *interfaceName,
    QString *errorMessage) {
  return self->createDevice(*interfaceName, errorMessage);
}

//  QList<QCanBusDeviceInfo> QCanBusFactory::availableDevices(QString
//      *errorMessage) const
extern "C" Q_DECL_EXPORT
QList<QCanBusDeviceInfo> *ritual_ZNK14QCanBusFactory16availableDevicesEP7QString(
    const QCanBusFactory *self,
    QString *errorMessage) {
  return new QList<QCanBusDeviceInfo>(self->availableDevices(errorMessage));
}

//  QCanBusFactory::~QCanBusFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanBusFactoryD1Ev(QCanBusFactory *self) {
  delete self;
}

//  a Python function taken by a CuteQCanBusFactory, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanBusFactory(
    QCanBusFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanBusFactory *>(self)->take(key, call);
}
