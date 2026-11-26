//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRender::QSSGRender()
extern "C" Q_DECL_EXPORT
QSSGRender *ritual_ZN10QSSGRenderC1Ev() {
  return new QSSGRender();
}

//  QSSGRender::QSSGRender(const QSSGRender &a0)
extern "C" Q_DECL_EXPORT
QSSGRender *ritual_ZN10QSSGRenderC1ERKS_(const QSSGRender *a0) {
  return new QSSGRender(*a0);
}

//  void QSSGRender::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QSSGRender8addDebugER6QDebug(
    const QSSGRender *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGRender::~QSSGRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSSGRenderD1Ev(QSSGRender *self) {
  delete self;
}
