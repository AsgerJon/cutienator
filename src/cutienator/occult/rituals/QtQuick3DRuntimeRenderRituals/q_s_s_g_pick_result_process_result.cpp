//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpickresult_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpickresult_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderpickresult.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
//      QSSGRenderPickResult &inSrc)
extern "C" Q_DECL_EXPORT
QSSGPickResultProcessResult *ritual_ZN27QSSGPickResultProcessResultC1ERK20QSSGRenderPickResult(
    const QSSGRenderPickResult *inSrc) {
  return new QSSGPickResultProcessResult(*inSrc);
}

//  QSSGPickResultProcessResult::QSSGPickResultProcessResult(const
//      QSSGRenderPickResult &inSrc, bool consumed)
extern "C" Q_DECL_EXPORT
QSSGPickResultProcessResult *ritual_ZN27QSSGPickResultProcessResultC1ERK20QSSGRenderPickResultb(
    const QSSGRenderPickResult *inSrc,
    bool consumed) {
  return new QSSGPickResultProcessResult(*inSrc, consumed);
}

//  QSSGPickResultProcessResult::QSSGPickResultProcessResult()
extern "C" Q_DECL_EXPORT
QSSGPickResultProcessResult *ritual_ZN27QSSGPickResultProcessResultC1Ev() {
  return new QSSGPickResultProcessResult();
}

//  QSSGPickResultProcessResult::~QSSGPickResultProcessResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGPickResultProcessResultD1Ev(
    QSSGPickResultProcessResult *self) {
  delete self;
}
