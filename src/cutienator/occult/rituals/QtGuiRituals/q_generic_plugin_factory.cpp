//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qgenericpluginfactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qgenericpluginfactory.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QGenericPluginFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QGenericPluginFactory4keysEv() {
  return new QList<QString>(QGenericPluginFactory::keys());
}

//  QObject *QGenericPluginFactory::create(const QString &a0, const QString
//      &a1)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN21QGenericPluginFactory6createERK7QStringS2_(
    const QString *a0,
    const QString *a1) {
  return QGenericPluginFactory::create(*a0, *a1);
}

//  QGenericPluginFactory::~QGenericPluginFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGenericPluginFactoryD1Ev(QGenericPluginFactory *self) {
  delete self;
}
