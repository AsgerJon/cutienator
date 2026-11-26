//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  QSSGSceneDesc::PropertyCall::~PropertyCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc12PropertyCallD1Ev(
    QSSGSceneDesc::PropertyCall *self) {
  delete self;
}

//  bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const char *a1,
//      const void *a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSSGSceneDesc12PropertyCall3setER14QQuick3DObjectPKcPKv(
    QSSGSceneDesc::PropertyCall *self,
    QQuick3DObject *a0,
    const char *a1,
    const void *a2) {
  return self->set(*a0, a1, a2);
}

//  bool QSSGSceneDesc::PropertyCall::set(QQuick3DObject &a0, const char *a1,
//      const QVariant &a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSSGSceneDesc12PropertyCall3setER14QQuick3DObjectPKcRK8QVariant(
    QSSGSceneDesc::PropertyCall *self,
    QQuick3DObject *a0,
    const char *a1,
    const QVariant *a2) {
  return self->set(*a0, a1, *a2);
}

//  bool QSSGSceneDesc::PropertyCall::get(const QQuick3DObject &a0, const
//      void **a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSSGSceneDesc12PropertyCall3getERK14QQuick3DObjectPPKv(
    const QSSGSceneDesc::PropertyCall *self,
    const QQuick3DObject *a0,
    const void **a1) {
  return self->get(*a0, a1);
}
