//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendertexturedata_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendertexturedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderTextureData::QSSGRenderTextureData()
extern "C" Q_DECL_EXPORT
QSSGRenderTextureData *ritual_ZN21QSSGRenderTextureDataC1Ev() {
  return new QSSGRenderTextureData();
}

//  QSSGRenderTextureData::~QSSGRenderTextureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureDataD1Ev(QSSGRenderTextureData *self) {
  delete self;
}

//  const QByteArray &QSSGRenderTextureData::textureData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QSSGRenderTextureData11textureDataEv(
    const QSSGRenderTextureData *self) {
  return new QByteArray(self->textureData());
}

//  void QSSGRenderTextureData::setTextureData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureData14setTextureDataERK10QByteArray(
    QSSGRenderTextureData *self,
    const QByteArray *data) {
  self->setTextureData(*data);
}

//  QSize QSSGRenderTextureData::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QSSGRenderTextureData4sizeEv(
    const QSSGRenderTextureData *self) {
  return new QSize(self->size());
}

//  void QSSGRenderTextureData::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureData7setSizeERK5QSize(
    QSSGRenderTextureData *self,
    const QSize *size) {
  self->setSize(*size);
}

//  int QSSGRenderTextureData::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSSGRenderTextureData5depthEv(
    const QSSGRenderTextureData *self) {
  return self->depth();
}

//  void QSSGRenderTextureData::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureData8setDepthEi(
    QSSGRenderTextureData *self,
    int depth) {
  self->setDepth(depth);
}

//  QSSGRenderTextureFormat QSSGRenderTextureData::format() const
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat *ritual_ZNK21QSSGRenderTextureData6formatEv(
    const QSSGRenderTextureData *self) {
  return new QSSGRenderTextureFormat(self->format());
}

//  void QSSGRenderTextureData::setFormat(QSSGRenderTextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureData9setFormatE23QSSGRenderTextureFormat(
    QSSGRenderTextureData *self,
    const QSSGRenderTextureFormat *format) {
  self->setFormat(*format);
}

//  bool QSSGRenderTextureData::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGRenderTextureData15hasTransparencyEv(
    const QSSGRenderTextureData *self) {
  return self->hasTransparency();
}

//  void QSSGRenderTextureData::setHasTransparency(bool hasTransparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderTextureData18setHasTransparencyEb(
    QSSGRenderTextureData *self,
    bool hasTransparency) {
  self->setHasTransparency(hasTransparency);
}

//  quint32 QSSGRenderTextureData::version() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK21QSSGRenderTextureData7versionEv(
    const QSSGRenderTextureData *self) {
  return self->version();
}

//  QSSGRenderTextureData::QSSGRenderTextureData(QSSGRenderGraphObject::Type
//      inType)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureData *ritual_ZN21QSSGRenderTextureDataC1EN21QSSGRenderGraphObject4TypeE(
    QSSGRenderGraphObject::Type inType) {
  return new QSSGRenderTextureData(inType);
}
