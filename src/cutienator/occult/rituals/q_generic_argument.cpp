//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  const char *QGenericArgument::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QGenericArgument4nameEv(
    const QGenericArgument *self) {
  return self->name();
}

//  QGenericArgument::~QGenericArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGenericArgumentD1Ev(QGenericArgument *self) {
  delete self;
}
