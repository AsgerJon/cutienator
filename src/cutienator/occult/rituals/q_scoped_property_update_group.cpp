//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>

//  QScopedPropertyUpdateGroup::QScopedPropertyUpdateGroup()
extern "C" Q_DECL_EXPORT
QScopedPropertyUpdateGroup *ritual_ZN26QScopedPropertyUpdateGroupC1Ev() {
  return new QScopedPropertyUpdateGroup();
}

//  QScopedPropertyUpdateGroup::~QScopedPropertyUpdateGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QScopedPropertyUpdateGroupD1Ev(
    QScopedPropertyUpdateGroup *self) {
  delete self;
}
