//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Utils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>

//  bool operator==(const QSSGRuntimeObjectNameKey &lhs, const
//      QSSGRuntimeObjectNameKey &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QSSGRuntimeObjectNameKeyS1_(
    const QSSGRuntimeObjectNameKey *lhs,
    const QSSGRuntimeObjectNameKey *rhs) {
  return operator==(*lhs, *rhs);
}

//  QSSGRuntimeObjectNameKey::~QSSGRuntimeObjectNameKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRuntimeObjectNameKeyD1Ev(
    QSSGRuntimeObjectNameKey *self) {
  delete self;
}
