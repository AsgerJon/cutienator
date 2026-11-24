//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGBindBuffer::QSSGBindBuffer(const QByteArray &inBufName)
extern "C" Q_DECL_EXPORT
QSSGBindBuffer *ritual_ZN14QSSGBindBufferC1ERK10QByteArray(
    const QByteArray *inBufName) {
  return new QSSGBindBuffer(*inBufName);
}

//  QSSGBindBuffer::QSSGBindBuffer(const QSSGBindBuffer &command)
extern "C" Q_DECL_EXPORT
QSSGBindBuffer *ritual_ZN14QSSGBindBufferC1ERKS_(
    const QSSGBindBuffer *command) {
  return new QSSGBindBuffer(*command);
}

//  QSSGBindBuffer::~QSSGBindBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGBindBufferD1Ev(QSSGBindBuffer *self) {
  delete self;
}
