//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaobject.h>

//  QMetaClassInfo::QMetaClassInfo()
extern "C" Q_DECL_EXPORT
QMetaClassInfo *ritual_ZN14QMetaClassInfoC1Ev() {
  return new QMetaClassInfo();
}

//  const char *QMetaClassInfo::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK14QMetaClassInfo4nameEv(const QMetaClassInfo *self) {
  return self->name();
}

//  const char *QMetaClassInfo::value() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK14QMetaClassInfo5valueEv(const QMetaClassInfo *self) {
  return self->value();
}

//  const QMetaObject *QMetaClassInfo::enclosingMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QMetaClassInfo19enclosingMetaObjectEv(
    const QMetaClassInfo *self) {
  return self->enclosingMetaObject();
}

//  QMetaClassInfo::~QMetaClassInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMetaClassInfoD1Ev(QMetaClassInfo *self) {
  delete self;
}
