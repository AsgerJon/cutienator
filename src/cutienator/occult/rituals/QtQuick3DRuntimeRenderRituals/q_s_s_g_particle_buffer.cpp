//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>

//  void QSSGParticleBuffer::resize(int particleCount, int particleSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGParticleBuffer6resizeEii(
    QSSGParticleBuffer *self,
    int particleCount,
    int particleSize) {
  self->resize(particleCount, particleSize);
}

//  void QSSGParticleBuffer::resizeLine(int particleCount, int segmentCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGParticleBuffer10resizeLineEii(
    QSSGParticleBuffer *self,
    int particleCount,
    int segmentCount) {
  self->resizeLine(particleCount, segmentCount);
}

//  void QSSGParticleBuffer::setBounds(const QSSGBounds3 &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGParticleBuffer9setBoundsERK11QSSGBounds3(
    QSSGParticleBuffer *self,
    const QSSGBounds3 *bounds) {
  self->setBounds(*bounds);
}

//  char *QSSGParticleBuffer::pointer()
extern "C" Q_DECL_EXPORT
char *ritual_ZN18QSSGParticleBuffer7pointerEv(QSSGParticleBuffer *self) {
  return self->pointer();
}

//  const char *QSSGParticleBuffer::pointer() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK18QSSGParticleBuffer7pointerEv(
    const QSSGParticleBuffer *self) {
  return self->pointer();
}

//  int QSSGParticleBuffer::particlesPerSlice() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer17particlesPerSliceEv(
    const QSSGParticleBuffer *self) {
  return self->particlesPerSlice();
}

//  int QSSGParticleBuffer::sliceStride() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer11sliceStrideEv(
    const QSSGParticleBuffer *self) {
  return self->sliceStride();
}

//  int QSSGParticleBuffer::particleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer13particleCountEv(
    const QSSGParticleBuffer *self) {
  return self->particleCount();
}

//  int QSSGParticleBuffer::sliceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer10sliceCountEv(
    const QSSGParticleBuffer *self) {
  return self->sliceCount();
}

//  QSize QSSGParticleBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QSSGParticleBuffer4sizeEv(
    const QSSGParticleBuffer *self) {
  return new QSize(self->size());
}

//  QByteArray QSSGParticleBuffer::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QSSGParticleBuffer4dataEv(
    const QSSGParticleBuffer *self) {
  return new QByteArray(self->data());
}

//  QSSGBounds3 QSSGParticleBuffer::bounds() const
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZNK18QSSGParticleBuffer6boundsEv(
    const QSSGParticleBuffer *self) {
  return new QSSGBounds3(self->bounds());
}

//  int QSSGParticleBuffer::bufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer10bufferSizeEv(
    const QSSGParticleBuffer *self) {
  return self->bufferSize();
}

//  int QSSGParticleBuffer::serial() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer6serialEv(const QSSGParticleBuffer *self) {
  return self->serial();
}

//  int QSSGParticleBuffer::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSSGParticleBuffer8segmentsEv(
    const QSSGParticleBuffer *self) {
  return self->segments();
}

//  QSSGParticleBuffer::~QSSGParticleBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGParticleBufferD1Ev(QSSGParticleBuffer *self) {
  delete self;
}
