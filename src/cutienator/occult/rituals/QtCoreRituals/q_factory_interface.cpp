//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfactoryinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfactoryinterface.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QFactoryInterface::~QFactoryInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFactoryInterfaceD1Ev(QFactoryInterface *self) {
  delete self;
}

//  QStringList QFactoryInterface::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QFactoryInterface4keysEv(
    const QFactoryInterface *self) {
  return new QList<QString>(self->keys());
}
