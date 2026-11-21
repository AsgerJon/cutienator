//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstylefactory.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstylefactory.h>
#include <QtCore/qstring.h>

//  QStyle *QStyleFactory::create(const QString &a0)
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN13QStyleFactory6createERK7QString(const QString *a0) {
  return QStyleFactory::create(*a0);
}

//  QStyleFactory::~QStyleFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStyleFactoryD1Ev(QStyleFactory *self) {
  delete self;
}
