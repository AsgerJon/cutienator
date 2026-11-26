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

//  QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer &&other)
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferC1EOS_(QOpenGLBuffer *other) {
  return new QOpenGLBuffer(std::move(*other));
}

//  QOpenGLBuffer::~QOpenGLBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBufferD1Ev(QOpenGLBuffer *self) {
  delete self;
}

//  QOpenGLBuffer &QOpenGLBuffer::operator=(const QOpenGLBuffer &other)
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferaSERKS_(
    QOpenGLBuffer *self,
    const QOpenGLBuffer *other) {
  return &(self->operator=(*other));
}

//  QOpenGLBuffer &QOpenGLBuffer::operator=(QOpenGLBuffer &&other)
extern "C" Q_DECL_EXPORT
QOpenGLBuffer *ritual_ZN13QOpenGLBufferaSEOS_(
    QOpenGLBuffer *self,
    QOpenGLBuffer *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QOpenGLBuffer::swap(QOpenGLBuffer &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer4swapERS_(
    QOpenGLBuffer *self,
    QOpenGLBuffer *other) {
  self->swap(*other);
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

//  GLuint QOpenGLBuffer::bufferId() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK13QOpenGLBuffer8bufferIdEv(const QOpenGLBuffer *self) {
  return self->bufferId();
}

//  int QOpenGLBuffer::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QOpenGLBuffer4sizeEv(const QOpenGLBuffer *self) {
  return self->size();
}

//  bool QOpenGLBuffer::read(int offset, void *data, int count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLBuffer4readEiPvi(
    QOpenGLBuffer *self,
    int offset,
    void *data,
    int count) {
  return self->read(offset, data, count);
}

//  void QOpenGLBuffer::write(int offset, const void *data, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer5writeEiPKvi(
    QOpenGLBuffer *self,
    int offset,
    const void *data,
    int count) {
  self->write(offset, data, count);
}

//  void QOpenGLBuffer::allocate(const void *data, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer8allocateEPKvi(
    QOpenGLBuffer *self,
    const void *data,
    int count) {
  self->allocate(data, count);
}

//  void QOpenGLBuffer::allocate(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLBuffer8allocateEi(QOpenGLBuffer *self, int count) {
  self->allocate(count);
}

//  void *QOpenGLBuffer::map(QOpenGLBuffer::Access access)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QOpenGLBuffer3mapENS_6AccessE(
    QOpenGLBuffer *self,
    QOpenGLBuffer::Access access) {
  return self->map(access);
}

//  void *QOpenGLBuffer::mapRange(int offset, int count,
//      QOpenGLBuffer::RangeAccessFlags access)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QOpenGLBuffer8mapRangeEii6QFlagsINS_15RangeAccessFlagEE(
    QOpenGLBuffer *self,
    int offset,
    int count,
    int access) {
  return self->mapRange(
      offset,
      count,
      QFlags<QOpenGLBuffer::RangeAccessFlag>::fromInt(access));
}

//  bool QOpenGLBuffer::unmap()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpenGLBuffer5unmapEv(QOpenGLBuffer *self) {
  return self->unmap();
}

//  QOpenGLBufferPrivate *QOpenGLBuffer::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLBufferPrivate *ritual_ZN13QOpenGLBuffer6d_funcEv(
    QOpenGLBuffer *self) {
  return self->d_func();
}

//  const QOpenGLBufferPrivate *QOpenGLBuffer::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLBufferPrivate *ritual_ZNK13QOpenGLBuffer6d_funcEv(
    const QOpenGLBuffer *self) {
  return self->d_func();
}

#endif  // !defined(QT_NO_OPENGL)
