//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#include <QtCore/qobjectdefs.h>

//  QGenericArgument::QGenericArgument(const char *aName, const void *aData)
extern "C" Q_DECL_EXPORT
QGenericArgument *ritual_ZN16QGenericArgumentC1EPKcPKv(
    const char *aName,
    const void *aData) {
  return new QGenericArgument(aName, aData);
}

//  void *QGenericArgument::data() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK16QGenericArgument4dataEv(const QGenericArgument *self) {
  return self->data();
}

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

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
