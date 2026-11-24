//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgfrustum_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgfrustum_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGFrustum::contains(const QSSGBounds3 &box) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSSGFrustum8containsERK11QSSGBounds3(
    const QSSGFrustum *self,
    const QSSGBounds3 *box) {
  return self->contains(*box);
}

//  QSSGFrustum::~QSSGFrustum()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSSGFrustumD1Ev(QSSGFrustum *self) {
  delete self;
}
