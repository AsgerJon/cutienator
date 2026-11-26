//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderablesFilterCommand::QSSGRenderablesFilterCommand()
extern "C" Q_DECL_EXPORT
QSSGRenderablesFilterCommand *ritual_ZN28QSSGRenderablesFilterCommandC1Ev() {
  return new QSSGRenderablesFilterCommand();
}

//  void QSSGRenderablesFilterCommand::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QSSGRenderablesFilterCommand8addDebugER6QDebug(
    const QSSGRenderablesFilterCommand *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGRenderablesFilterCommand::~QSSGRenderablesFilterCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderablesFilterCommandD1Ev(
    QSSGRenderablesFilterCommand *self) {
  delete self;
}
