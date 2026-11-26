//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGBindShader::QSSGBindShader(const QByteArray &inShaderPathKey)
extern "C" Q_DECL_EXPORT
QSSGBindShader *ritual_ZN14QSSGBindShaderC1ERK10QByteArray(
    const QByteArray *inShaderPathKey) {
  return new QSSGBindShader(*inShaderPathKey);
}

//  QSSGBindShader::QSSGBindShader()
extern "C" Q_DECL_EXPORT
QSSGBindShader *ritual_ZN14QSSGBindShaderC1Ev() {
  return new QSSGBindShader();
}

//  QSSGBindShader::QSSGBindShader(const QSSGBindShader &command)
extern "C" Q_DECL_EXPORT
QSSGBindShader *ritual_ZN14QSSGBindShaderC1ERKS_(
    const QSSGBindShader *command) {
  return new QSSGBindShader(*command);
}

//  void QSSGBindShader::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QSSGBindShader8addDebugER6QDebug(
    const QSSGBindShader *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGBindShader::~QSSGBindShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGBindShaderD1Ev(QSSGBindShader *self) {
  delete self;
}
