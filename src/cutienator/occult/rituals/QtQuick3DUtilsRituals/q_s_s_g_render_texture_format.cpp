//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderTextureFormat::QSSGRenderTextureFormat(Format f)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat *ritual_ZN23QSSGRenderTextureFormatC1ENS_6FormatE(
    QSSGRenderTextureFormat::Format f) {
  return new QSSGRenderTextureFormat(f);
}

//  bool QSSGRenderTextureFormat::isCompressedTextureFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderTextureFormat25isCompressedTextureFormatEv(
    const QSSGRenderTextureFormat *self) {
  return self->isCompressedTextureFormat();
}

//  bool QSSGRenderTextureFormat::isUncompressedTextureFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderTextureFormat27isUncompressedTextureFormatEv(
    const QSSGRenderTextureFormat *self) {
  return self->isUncompressedTextureFormat();
}

//  bool QSSGRenderTextureFormat::isDepthTextureFormat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderTextureFormat20isDepthTextureFormatEv(
    const QSSGRenderTextureFormat *self) {
  return self->isDepthTextureFormat();
}

//  const char *QSSGRenderTextureFormat::toString() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK23QSSGRenderTextureFormat8toStringEv(
    const QSSGRenderTextureFormat *self) {
  return self->toString();
}

//  qint32 QSSGRenderTextureFormat::getSizeofFormat() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK23QSSGRenderTextureFormat15getSizeofFormatEv(
    const QSSGRenderTextureFormat *self) {
  return self->getSizeofFormat();
}

//  qint32 QSSGRenderTextureFormat::getNumberOfComponent() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK23QSSGRenderTextureFormat20getNumberOfComponentEv(
    const QSSGRenderTextureFormat *self) {
  return self->getNumberOfComponent();
}

//  bool QSSGRenderTextureFormat::operator==(const QSSGRenderTextureFormat
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderTextureFormateqERKS_(
    const QSSGRenderTextureFormat *self,
    const QSSGRenderTextureFormat *other) {
  return self->operator==(*other);
}

//  bool QSSGRenderTextureFormat::operator!=(const QSSGRenderTextureFormat
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGRenderTextureFormatneERKS_(
    const QSSGRenderTextureFormat *self,
    const QSSGRenderTextureFormat *other) {
  return self->operator!=(*other);
}

//  QSSGRenderTextureFormat::~QSSGRenderTextureFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderTextureFormatD1Ev(QSSGRenderTextureFormat *self) {
  delete self;
}
