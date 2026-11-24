//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGShaderKeyTextureChannel::QSSGShaderKeyTextureChannel(const char
//      *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyTextureChannel *ritual_ZN27QSSGShaderKeyTextureChannelC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyTextureChannel(inName);
}

//  QSSGShaderKeyTextureChannel::~QSSGShaderKeyTextureChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyTextureChannelD1Ev(
    QSSGShaderKeyTextureChannel *self) {
  delete self;
}
