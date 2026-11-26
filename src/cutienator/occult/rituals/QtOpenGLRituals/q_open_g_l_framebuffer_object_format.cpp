//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglframebufferobject.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qopenglframebufferobject.h>

//  QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat()
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormat *ritual_ZN30QOpenGLFramebufferObjectFormatC1Ev() {
  return new QOpenGLFramebufferObjectFormat();
}

//  QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat(const
//      QOpenGLFramebufferObjectFormat &other)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormat *ritual_ZN30QOpenGLFramebufferObjectFormatC1ERKS_(
    const QOpenGLFramebufferObjectFormat *other) {
  return new QOpenGLFramebufferObjectFormat(*other);
}

//  QOpenGLFramebufferObjectFormat
//      &QOpenGLFramebufferObjectFormat::operator=(const
//      QOpenGLFramebufferObjectFormat &other)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormat *ritual_ZN30QOpenGLFramebufferObjectFormataSERKS_(
    QOpenGLFramebufferObjectFormat *self,
    const QOpenGLFramebufferObjectFormat *other) {
  return &(self->operator=(*other));
}

//  QOpenGLFramebufferObjectFormat::~QOpenGLFramebufferObjectFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormatD1Ev(
    QOpenGLFramebufferObjectFormat *self) {
  delete self;
}

//  void QOpenGLFramebufferObjectFormat::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat10setSamplesEi(
    QOpenGLFramebufferObjectFormat *self,
    int samples) {
  self->setSamples(samples);
}

//  int QOpenGLFramebufferObjectFormat::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QOpenGLFramebufferObjectFormat7samplesEv(
    const QOpenGLFramebufferObjectFormat *self) {
  return self->samples();
}

//  void QOpenGLFramebufferObjectFormat::setMipmap(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat9setMipmapEb(
    QOpenGLFramebufferObjectFormat *self,
    bool enabled) {
  self->setMipmap(enabled);
}

//  bool QOpenGLFramebufferObjectFormat::mipmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QOpenGLFramebufferObjectFormat6mipmapEv(
    const QOpenGLFramebufferObjectFormat *self) {
  return self->mipmap();
}

//  void QOpenGLFramebufferObjectFormat::setAttachment(QOpenGLFramebufferObje
//      ct::Attachment attachment)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat13setAttachmentEN24QOpenGLFramebufferObject10AttachmentE(
    QOpenGLFramebufferObjectFormat *self,
    QOpenGLFramebufferObject::Attachment attachment) {
  self->setAttachment(attachment);
}

//  QOpenGLFramebufferObject::Attachment
//      QOpenGLFramebufferObjectFormat::attachment() const
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject::Attachment ritual_ZNK30QOpenGLFramebufferObjectFormat10attachmentEv(
    const QOpenGLFramebufferObjectFormat *self) {
  return self->attachment();
}

//  void QOpenGLFramebufferObjectFormat::setTextureTarget(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat16setTextureTargetEj(
    QOpenGLFramebufferObjectFormat *self,
    GLenum target) {
  self->setTextureTarget(target);
}

//  GLenum QOpenGLFramebufferObjectFormat::textureTarget() const
extern "C" Q_DECL_EXPORT
GLenum ritual_ZNK30QOpenGLFramebufferObjectFormat13textureTargetEv(
    const QOpenGLFramebufferObjectFormat *self) {
  return self->textureTarget();
}

//  void QOpenGLFramebufferObjectFormat::setInternalTextureFormat(GLenum
//      internalTextureFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat24setInternalTextureFormatEj(
    QOpenGLFramebufferObjectFormat *self,
    GLenum internalTextureFormat) {
  self->setInternalTextureFormat(internalTextureFormat);
}

//  GLenum QOpenGLFramebufferObjectFormat::internalTextureFormat() const
extern "C" Q_DECL_EXPORT
GLenum ritual_ZNK30QOpenGLFramebufferObjectFormat21internalTextureFormatEv(
    const QOpenGLFramebufferObjectFormat *self) {
  return self->internalTextureFormat();
}

//  bool QOpenGLFramebufferObjectFormat::operator==(const
//      QOpenGLFramebufferObjectFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QOpenGLFramebufferObjectFormateqERKS_(
    const QOpenGLFramebufferObjectFormat *self,
    const QOpenGLFramebufferObjectFormat *other) {
  return self->operator==(*other);
}

//  bool QOpenGLFramebufferObjectFormat::operator!=(const
//      QOpenGLFramebufferObjectFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QOpenGLFramebufferObjectFormatneERKS_(
    const QOpenGLFramebufferObjectFormat *self,
    const QOpenGLFramebufferObjectFormat *other) {
  return self->operator!=(*other);
}

//  void QOpenGLFramebufferObjectFormat::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLFramebufferObjectFormat6detachEv(
    QOpenGLFramebufferObjectFormat *self) {
  self->detach();
}
