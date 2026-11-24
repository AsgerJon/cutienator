//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglbuffer.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglbuffer.h>

//  QOpenGLBuffer::QOpenGLBuffer()
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferC1Ev() {
  return new QOpenGLBuffer();
}

//  QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer::Type type)
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferC1ENS_4TypeE(
    QOpenGLBuffer::Type type) {
  return new QOpenGLBuffer(type);
}

//  QOpenGLBuffer::QOpenGLBuffer(const QOpenGLBuffer &other)
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferC1ERKS_(const QOpenGLBuffer *other) {
  return new QOpenGLBuffer(*other);
}

//  QOpenGLBuffer::~QOpenGLBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBufferD1Ev(QOpenGLBuffer *self) {
  delete self;
}

//  QOpenGLBuffer::Type QOpenGLBuffer::type() const
extern "C" Q_DECL_EXPORT
QOpenGLBuffer::Type ritual_ZNK13QOpenGLBuffer4typeEv(
    const QOpenGLBuffer *self) {
  return self->type();
}

//  QOpenGLBuffer::UsagePattern QOpenGLBuffer::usagePattern() const
extern "C" Q_DECL_EXPORT
QOpenGLBuffer::UsagePattern ritual_ZNK13QOpenGLBuffer12usagePatternEv(
    const QOpenGLBuffer *self) {
  return self->usagePattern();
}

//  void QOpenGLBuffer::setUsagePattern(QOpenGLBuffer::UsagePattern value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer15setUsagePatternENS_12UsagePatternE(
    QOpenGLBuffer *self,
    QOpenGLBuffer::UsagePattern value) {
  self->setUsagePattern(value);
}

//  bool QOpenGLBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLBuffer6createEv(QOpenGLBuffer *self) {
  return self->create();
}

//  bool QOpenGLBuffer::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpenGLBuffer9isCreatedEv(const QOpenGLBuffer *self) {
  return self->isCreated();
}

//  void QOpenGLBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer7destroyEv(QOpenGLBuffer *self) {
  self->destroy();
}

//  bool QOpenGLBuffer::bind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLBuffer4bindEv(QOpenGLBuffer *self) {
  return self->bind();
}

//  void QOpenGLBuffer::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer7releaseEv(QOpenGLBuffer *self) {
  self->release();
}

//  void QOpenGLBuffer::release(QOpenGLBuffer::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer7releaseENS_4TypeE(QOpenGLBuffer::Type type) {
  QOpenGLBuffer::release(type);
}

//  int QOpenGLBuffer::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QOpenGLBuffer4sizeEv(const QOpenGLBuffer *self) {
  return self->size();
}

//  void QOpenGLBuffer::allocate(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer8allocateEi(QOpenGLBuffer *self, int count) {
  self->allocate(count);
}

//  bool QOpenGLBuffer::unmap()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLBuffer5unmapEv(QOpenGLBuffer *self) {
  return self->unmap();
}

#endif  // !defined(QT_NO_OPENGL)
