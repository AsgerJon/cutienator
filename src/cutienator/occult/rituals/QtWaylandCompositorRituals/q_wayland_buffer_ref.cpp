//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandbufferref.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>

//  QWaylandBufferRef::QWaylandBufferRef()
extern "C" Q_DECL_EXPORT
QWaylandBufferRef *ritual_ZN17QWaylandBufferRefC1Ev() {
  return new QWaylandBufferRef();
}

//  QWaylandBufferRef::QWaylandBufferRef(const QWaylandBufferRef &ref)
extern "C" Q_DECL_EXPORT
QWaylandBufferRef *ritual_ZN17QWaylandBufferRefC1ERKS_(
    const QWaylandBufferRef *ref) {
  return new QWaylandBufferRef(*ref);
}

//  QWaylandBufferRef::~QWaylandBufferRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandBufferRefD1Ev(QWaylandBufferRef *self) {
  delete self;
}

//  bool QWaylandBufferRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef6isNullEv(const QWaylandBufferRef *self) {
  return self->isNull();
}

//  bool QWaylandBufferRef::hasBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef9hasBufferEv(
    const QWaylandBufferRef *self) {
  return self->hasBuffer();
}

//  bool QWaylandBufferRef::hasContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef10hasContentEv(
    const QWaylandBufferRef *self) {
  return self->hasContent();
}

//  bool QWaylandBufferRef::hasProtectedContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef19hasProtectedContentEv(
    const QWaylandBufferRef *self) {
  return self->hasProtectedContent();
}

//  bool QWaylandBufferRef::isDestroyed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef11isDestroyedEv(
    const QWaylandBufferRef *self) {
  return self->isDestroyed();
}

//  QSize QWaylandBufferRef::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QWaylandBufferRef4sizeEv(const QWaylandBufferRef *self) {
  return new QSize(self->size());
}

//  QWaylandSurface::Origin QWaylandBufferRef::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface::Origin ritual_ZNK17QWaylandBufferRef6originEv(
    const QWaylandBufferRef *self) {
  return self->origin();
}

//  BufferType QWaylandBufferRef::bufferType() const
extern "C" Q_DECL_EXPORT
QWaylandBufferRef::BufferType ritual_ZNK17QWaylandBufferRef10bufferTypeEv(
    const QWaylandBufferRef *self) {
  return self->bufferType();
}

//  BufferFormatEgl QWaylandBufferRef::bufferFormatEgl() const
extern "C" Q_DECL_EXPORT
QWaylandBufferRef::BufferFormatEgl ritual_ZNK17QWaylandBufferRef15bufferFormatEglEv(
    const QWaylandBufferRef *self) {
  return self->bufferFormatEgl();
}

//  bool QWaylandBufferRef::isSharedMemory() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QWaylandBufferRef14isSharedMemoryEv(
    const QWaylandBufferRef *self) {
  return self->isSharedMemory();
}

//  QImage QWaylandBufferRef::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK17QWaylandBufferRef5imageEv(
    const QWaylandBufferRef *self) {
  return new QImage(self->image());
}

#if QT_CONFIG(opengl)
//  QOpenGLTexture *QWaylandBufferRef::toOpenGLTexture(int plane) const
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZNK17QWaylandBufferRef15toOpenGLTextureEi(
    const QWaylandBufferRef *self,
    int plane) {
  return self->toOpenGLTexture(plane);
}
#endif  // QT_CONFIG(opengl)

//  quintptr QWaylandBufferRef::lockNativeBuffer()
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN17QWaylandBufferRef16lockNativeBufferEv(
    QWaylandBufferRef *self) {
  return self->lockNativeBuffer();
}

//  void QWaylandBufferRef::unlockNativeBuffer(quintptr handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWaylandBufferRef18unlockNativeBufferEy(
    QWaylandBufferRef *self,
    quintptr handle) {
  self->unlockNativeBuffer(handle);
}

//  bool operator==(const QWaylandBufferRef &lhs, const QWaylandBufferRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QWaylandBufferRefS1_(
    const QWaylandBufferRef *lhs,
    const QWaylandBufferRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QWaylandBufferRef &lhs, const QWaylandBufferRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QWaylandBufferRefS1_(
    const QWaylandBufferRef *lhs,
    const QWaylandBufferRef *rhs) {
  return operator!=(*lhs, *rhs);
}
