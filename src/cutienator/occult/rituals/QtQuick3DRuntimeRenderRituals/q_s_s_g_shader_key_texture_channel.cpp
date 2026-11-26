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

//  QSSGShaderKeyTextureChannel::QSSGShaderKeyTextureChannel(const char
//      *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyTextureChannel *ritual_ZN27QSSGShaderKeyTextureChannelC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyTextureChannel(inName);
}

//  TexturChannelBits
//      QSSGShaderKeyTextureChannel::getTextureChannel(QSSGDataView<quint32>
//      inKeySet) const
extern "C" Q_DECL_EXPORT
QSSGShaderKeyTextureChannel::TexturChannelBits ritual_ZNK27QSSGShaderKeyTextureChannel17getTextureChannelE12QSSGDataViewIjE(
    const QSSGShaderKeyTextureChannel *self,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getTextureChannel(*inKeySet);
}

//  void QSSGShaderKeyTextureChannel::setTextureChannel(TexturChannelBits
//      channel, QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyTextureChannel17setTextureChannelENS_17TexturChannelBitsE11QSSGDataRefIjE(
    QSSGShaderKeyTextureChannel *self,
    QSSGShaderKeyTextureChannel::TexturChannelBits channel,
    const QSSGDataRef<quint32> *inKeySet) {
  self->setTextureChannel(channel, *inKeySet);
}

//  void QSSGShaderKeyTextureChannel::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK27QSSGShaderKeyTextureChannel8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyTextureChannel *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyTextureChannel::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyTextureChannel10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyTextureChannel *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyTextureChannel::~QSSGShaderKeyTextureChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGShaderKeyTextureChannelD1Ev(
    QSSGShaderKeyTextureChannel *self) {
  delete self;
}
