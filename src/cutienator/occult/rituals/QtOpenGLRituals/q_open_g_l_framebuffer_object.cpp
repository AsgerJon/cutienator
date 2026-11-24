//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglframebufferobject.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qopenglframebufferobject.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  QOpenGLFramebufferObjectPrivate *QOpenGLFramebufferObject::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectPrivate *ritual_ZN24QOpenGLFramebufferObject6d_funcEv(
    QOpenGLFramebufferObject *self) {
  return self->d_func();
}

//  const QOpenGLFramebufferObjectPrivate *QOpenGLFramebufferObject::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QOpenGLFramebufferObjectPrivate *ritual_ZNK24QOpenGLFramebufferObject6d_funcEv(
    const QOpenGLFramebufferObject *self) {
  return self->d_func();
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
//      GLenum target)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizej(
    const QSize *size,
    GLenum target) {
  return new QOpenGLFramebufferObject(*size, target);
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int height,
//      GLenum target)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1Eiij(
    int width,
    int height,
    GLenum target) {
  return new QOpenGLFramebufferObject(width, height, target);
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
//      Attachment attachment, GLenum target, GLenum internalFormat)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizeNS_10AttachmentEjj(
    const QSize *size,
    QOpenGLFramebufferObject::Attachment attachment,
    GLenum target,
    GLenum internalFormat) {
  return new QOpenGLFramebufferObject(
      *size,
      attachment,
      target,
      internalFormat);
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int height,
//      Attachment attachment, GLenum target, GLenum internalFormat)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1EiiNS_10AttachmentEjj(
    int width,
    int height,
    QOpenGLFramebufferObject::Attachment attachment,
    GLenum target,
    GLenum internalFormat) {
  return new QOpenGLFramebufferObject(
      width,
      height,
      attachment,
      target,
      internalFormat);
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
//      const QOpenGLFramebufferObjectFormat &format)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizeRK30QOpenGLFramebufferObjectFormat(
    const QSize *size,
    const QOpenGLFramebufferObjectFormat *format) {
  return new QOpenGLFramebufferObject(*size, *format);
}

//  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int height,
//      const QOpenGLFramebufferObjectFormat &format)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN24QOpenGLFramebufferObjectC1EiiRK30QOpenGLFramebufferObjectFormat(
    int width,
    int height,
    const QOpenGLFramebufferObjectFormat *format) {
  return new QOpenGLFramebufferObject(width, height, *format);
}

//  QOpenGLFramebufferObject::~QOpenGLFramebufferObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObjectD1Ev(
    QOpenGLFramebufferObject *self) {
  delete self;
}

//  void QOpenGLFramebufferObject::addColorAttachment(const QSize &size,
//      GLenum internalFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject18addColorAttachmentERK5QSizej(
    QOpenGLFramebufferObject *self,
    const QSize *size,
    GLenum internalFormat) {
  self->addColorAttachment(*size, internalFormat);
}

//  void QOpenGLFramebufferObject::addColorAttachment(int width, int height,
//      GLenum internalFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject18addColorAttachmentEiij(
    QOpenGLFramebufferObject *self,
    int width,
    int height,
    GLenum internalFormat) {
  self->addColorAttachment(width, height, internalFormat);
}

//  QOpenGLFramebufferObjectFormat QOpenGLFramebufferObject::format() const
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObjectFormat *ritual_ZNK24QOpenGLFramebufferObject6formatEv(
    const QOpenGLFramebufferObject *self) {
  return new QOpenGLFramebufferObjectFormat(self->format());
}

//  bool QOpenGLFramebufferObject::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QOpenGLFramebufferObject7isValidEv(
    const QOpenGLFramebufferObject *self) {
  return self->isValid();
}

//  bool QOpenGLFramebufferObject::isBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QOpenGLFramebufferObject7isBoundEv(
    const QOpenGLFramebufferObject *self) {
  return self->isBound();
}

//  bool QOpenGLFramebufferObject::bind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLFramebufferObject4bindEv(
    QOpenGLFramebufferObject *self) {
  return self->bind();
}

//  bool QOpenGLFramebufferObject::release()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLFramebufferObject7releaseEv(
    QOpenGLFramebufferObject *self) {
  return self->release();
}

//  int QOpenGLFramebufferObject::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLFramebufferObject5widthEv(
    const QOpenGLFramebufferObject *self) {
  return self->width();
}

//  int QOpenGLFramebufferObject::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLFramebufferObject6heightEv(
    const QOpenGLFramebufferObject *self) {
  return self->height();
}

//  QSize QOpenGLFramebufferObject::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QOpenGLFramebufferObject4sizeEv(
    const QOpenGLFramebufferObject *self) {
  return new QSize(self->size());
}

//  QList<QSize> QOpenGLFramebufferObject::sizes() const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK24QOpenGLFramebufferObject5sizesEv(
    const QOpenGLFramebufferObject *self) {
  return new QList<QSize>(self->sizes());
}

//  QImage QOpenGLFramebufferObject::toImage(bool flipped) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK24QOpenGLFramebufferObject7toImageEb(
    const QOpenGLFramebufferObject *self,
    bool flipped) {
  return new QImage(self->toImage(flipped));
}

//  QImage QOpenGLFramebufferObject::toImage(bool flipped, int
//      colorAttachmentIndex) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK24QOpenGLFramebufferObject7toImageEbi(
    const QOpenGLFramebufferObject *self,
    bool flipped,
    int colorAttachmentIndex) {
  return new QImage(self->toImage(flipped, colorAttachmentIndex));
}

//  Attachment QOpenGLFramebufferObject::attachment() const
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject::Attachment ritual_ZNK24QOpenGLFramebufferObject10attachmentEv(
    const QOpenGLFramebufferObject *self) {
  return self->attachment();
}

//  void QOpenGLFramebufferObject::setAttachment(Attachment attachment)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject13setAttachmentENS_10AttachmentE(
    QOpenGLFramebufferObject *self,
    QOpenGLFramebufferObject::Attachment attachment) {
  self->setAttachment(attachment);
}

//  bool QOpenGLFramebufferObject::bindDefault()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLFramebufferObject11bindDefaultEv() {
  return QOpenGLFramebufferObject::bindDefault();
}

//  bool QOpenGLFramebufferObject::hasOpenGLFramebufferObjects()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLFramebufferObject27hasOpenGLFramebufferObjectsEv() {
  return QOpenGLFramebufferObject::hasOpenGLFramebufferObjects();
}

//  bool QOpenGLFramebufferObject::hasOpenGLFramebufferBlit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLFramebufferObject24hasOpenGLFramebufferBlitEv() {
  return QOpenGLFramebufferObject::hasOpenGLFramebufferBlit();
}

//  void QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
//      *target, const QRect &targetRect, QOpenGLFramebufferObject *source,
//      const QRect &sourceRect, GLbitfield buffers, GLenum filter, int
//      readColorAttachmentIndex, int drawColorAttachmentIndex,
//      FramebufferRestorePolicy restorePolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0_S3_jjiiNS_24FramebufferRestorePolicyE(
    QOpenGLFramebufferObject *target,
    const QRect *targetRect,
    QOpenGLFramebufferObject *source,
    const QRect *sourceRect,
    GLbitfield buffers,
    GLenum filter,
    int readColorAttachmentIndex,
    int drawColorAttachmentIndex,
    QOpenGLFramebufferObject::FramebufferRestorePolicy restorePolicy) {
  QOpenGLFramebufferObject::blitFramebuffer(
      target,
      *targetRect,
      source,
      *sourceRect,
      buffers,
      filter,
      readColorAttachmentIndex,
      drawColorAttachmentIndex,
      restorePolicy);
}

//  void QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
//      *target, const QRect &targetRect, QOpenGLFramebufferObject *source,
//      const QRect &sourceRect, GLbitfield buffers, GLenum filter, int
//      readColorAttachmentIndex, int drawColorAttachmentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0_S3_jjii(
    QOpenGLFramebufferObject *target,
    const QRect *targetRect,
    QOpenGLFramebufferObject *source,
    const QRect *sourceRect,
    GLbitfield buffers,
    GLenum filter,
    int readColorAttachmentIndex,
    int drawColorAttachmentIndex) {
  QOpenGLFramebufferObject::blitFramebuffer(
      target,
      *targetRect,
      source,
      *sourceRect,
      buffers,
      filter,
      readColorAttachmentIndex,
      drawColorAttachmentIndex);
}

//  void QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
//      *target, const QRect &targetRect, QOpenGLFramebufferObject *source,
//      const QRect &sourceRect, GLbitfield buffers, GLenum filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0_S3_jj(
    QOpenGLFramebufferObject *target,
    const QRect *targetRect,
    QOpenGLFramebufferObject *source,
    const QRect *sourceRect,
    GLbitfield buffers,
    GLenum filter) {
  QOpenGLFramebufferObject::blitFramebuffer(
      target,
      *targetRect,
      source,
      *sourceRect,
      buffers,
      filter);
}

//  void QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
//      *target, QOpenGLFramebufferObject *source, GLbitfield buffers, GLenum
//      filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_S0_jj(
    QOpenGLFramebufferObject *target,
    QOpenGLFramebufferObject *source,
    GLbitfield buffers,
    GLenum filter) {
  QOpenGLFramebufferObject::blitFramebuffer(target, source, buffers, filter);
}
