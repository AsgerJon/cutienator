//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  bool QQmlPrivate::RegisterType::has(StructVersion v) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlPrivate12RegisterType3hasENS0_13StructVersionE(
    const QQmlPrivate::RegisterType *self,
    QQmlPrivate::RegisterType::StructVersion v) {
  return self->has(v);
}

//  QQmlPrivate::RegisterType::~RegisterType()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate12RegisterTypeD1Ev(
    QQmlPrivate::RegisterType *self) {
  delete self;
}
