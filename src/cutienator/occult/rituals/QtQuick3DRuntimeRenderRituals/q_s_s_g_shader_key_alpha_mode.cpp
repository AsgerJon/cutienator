//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>

//  QSSGShaderKeyAlphaMode::QSSGShaderKeyAlphaMode(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyAlphaMode *ritual_ZN22QSSGShaderKeyAlphaModeC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyAlphaMode(inName);
}

//  void QSSGShaderKeyAlphaMode::setAlphaMode(QSSGDataRef<quint32> inKeySet,
//      QSSGRenderDefaultMaterial::MaterialAlphaMode inMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGShaderKeyAlphaMode12setAlphaModeE11QSSGDataRefIjEN25QSSGRenderDefaultMaterial17MaterialAlphaModeE(
    QSSGShaderKeyAlphaMode *self,
    const QSSGDataRef<quint32> *inKeySet,
    QSSGRenderDefaultMaterial::MaterialAlphaMode inMode) {
  self->setAlphaMode(*inKeySet, inMode);
}

//  QSSGRenderDefaultMaterial::MaterialAlphaMode
//      QSSGShaderKeyAlphaMode::getAlphaMode(QSSGDataView<quint32> inKeySet)
//      const
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialAlphaMode ritual_ZNK22QSSGShaderKeyAlphaMode12getAlphaModeE12QSSGDataViewIjE(
    const QSSGShaderKeyAlphaMode *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getAlphaMode(*inKeySet);
}

//  void QSSGShaderKeyAlphaMode::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QSSGShaderKeyAlphaMode8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyAlphaMode *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyAlphaMode::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGShaderKeyAlphaMode10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyAlphaMode *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyAlphaMode::~QSSGShaderKeyAlphaMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSSGShaderKeyAlphaModeD1Ev(QSSGShaderKeyAlphaMode *self) {
  delete self;
}
