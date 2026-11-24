//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGShaderKeyBoolean::QSSGShaderKeyBoolean(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyBoolean *ritual_ZN20QSSGShaderKeyBooleanC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyBoolean(inName);
}

//  quint32 QSSGShaderKeyBoolean::getMask() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QSSGShaderKeyBoolean7getMaskEv(
    const QSSGShaderKeyBoolean *self) {
  return self->getMask();
}

//  QSSGShaderKeyBoolean::~QSSGShaderKeyBoolean()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGShaderKeyBooleanD1Ev(QSSGShaderKeyBoolean *self) {
  delete self;
}
