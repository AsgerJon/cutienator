//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengltextureblitter.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qopengltextureblitter.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/QMatrix3x3>
#include <QtCore/QRectF>
#include <QtCore/QSize>

//  QOpenGLTextureBlitter::QOpenGLTextureBlitter()
extern "C" Q_DECL_EXPORT
QOpenGLTextureBlitter *ritual_ZN21QOpenGLTextureBlitterC1Ev() {
  return new QOpenGLTextureBlitter();
}

//  QOpenGLTextureBlitter::~QOpenGLTextureBlitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitterD1Ev(QOpenGLTextureBlitter *self) {
  delete self;
}

//  bool QOpenGLTextureBlitter::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QOpenGLTextureBlitter6createEv(QOpenGLTextureBlitter *self) {
  return self->create();
}

//  bool QOpenGLTextureBlitter::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTextureBlitter9isCreatedEv(
    const QOpenGLTextureBlitter *self) {
  return self->isCreated();
}

//  void QOpenGLTextureBlitter::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter7destroyEv(
    QOpenGLTextureBlitter *self) {
  self->destroy();
}

//  bool QOpenGLTextureBlitter::supportsExternalOESTarget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTextureBlitter25supportsExternalOESTargetEv(
    const QOpenGLTextureBlitter *self) {
  return self->supportsExternalOESTarget();
}

//  bool QOpenGLTextureBlitter::supportsRectangleTarget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGLTextureBlitter23supportsRectangleTargetEv(
    const QOpenGLTextureBlitter *self) {
  return self->supportsRectangleTarget();
}

//  void QOpenGLTextureBlitter::bind(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter4bindEj(
    QOpenGLTextureBlitter *self,
    GLenum target) {
  self->bind(target);
}

//  void QOpenGLTextureBlitter::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter7releaseEv(
    QOpenGLTextureBlitter *self) {
  self->release();
}

//  void QOpenGLTextureBlitter::setRedBlueSwizzle(bool swizzle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter17setRedBlueSwizzleEb(
    QOpenGLTextureBlitter *self,
    bool swizzle) {
  self->setRedBlueSwizzle(swizzle);
}

//  void QOpenGLTextureBlitter::setOpacity(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter10setOpacityEf(
    QOpenGLTextureBlitter *self,
    float opacity) {
  self->setOpacity(opacity);
}

//  void QOpenGLTextureBlitter::blit(GLuint texture, const QMatrix4x4
//      &targetTransform, Origin sourceOrigin)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter4blitEjRK10QMatrix4x4NS_6OriginE(
    QOpenGLTextureBlitter *self,
    GLuint texture,
    const QMatrix4x4 *targetTransform,
    QOpenGLTextureBlitter::Origin sourceOrigin) {
  self->blit(texture, *targetTransform, sourceOrigin);
}

//  void QOpenGLTextureBlitter::blit(GLuint texture, const QMatrix4x4
//      &targetTransform, const QMatrix3x3 &sourceTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLTextureBlitter4blitEjRK10QMatrix4x4RK14QGenericMatrixILi3ELi3EfE(
    QOpenGLTextureBlitter *self,
    GLuint texture,
    const QMatrix4x4 *targetTransform,
    const QMatrix3x3 *sourceTransform) {
  self->blit(texture, *targetTransform, *sourceTransform);
}

//  QMatrix4x4 QOpenGLTextureBlitter::targetTransform(const QRectF &target,
//      const QRect &viewport)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QOpenGLTextureBlitter15targetTransformERK6QRectFRK5QRect(
    const QRectF *target,
    const QRect *viewport) {
  return new QMatrix4x4(
      QOpenGLTextureBlitter::targetTransform(
          *target,
          *viewport));
}

//  QMatrix3x3 QOpenGLTextureBlitter::sourceTransform(const QRectF
//      &subTexture, const QSize &textureSize, Origin origin)
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZN21QOpenGLTextureBlitter15sourceTransformERK6QRectFRK5QSizeNS_6OriginE(
    const QRectF *subTexture,
    const QSize *textureSize,
    QOpenGLTextureBlitter::Origin origin) {
  return new QMatrix3x3(
      QOpenGLTextureBlitter::sourceTransform(
          *subTexture,
          *textureSize,
          origin));
}

//  QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLTextureBlitterPrivate *ritual_ZN21QOpenGLTextureBlitter6d_funcEv(
    QOpenGLTextureBlitter *self) {
  return self->d_func();
}

//  const QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLTextureBlitterPrivate *ritual_ZNK21QOpenGLTextureBlitter6d_funcEv(
    const QOpenGLTextureBlitter *self) {
  return self->d_func();
}

//  a QMatrix3x3 a ritual of QOpenGLTextureBlitter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLTextureBlitter__QMatrix3x3(QMatrix3x3 *self) {
  delete self;
}
