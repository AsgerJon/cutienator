//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, which Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11CommandBuffer::~QD3D11CommandBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QD3D11CommandBufferD1Ev(QD3D11CommandBuffer *self) {
  delete self;
}

//  void QD3D11CommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QD3D11CommandBuffer7destroyEv(QD3D11CommandBuffer *self) {
  self->destroy();
}

//  const uchar *QD3D11CommandBuffer::retainData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZN19QD3D11CommandBuffer10retainDataERK10QByteArray(
    QD3D11CommandBuffer *self,
    const QByteArray *data) {
  return self->retainData(*data);
}

//  const uchar *QD3D11CommandBuffer::retainBufferData(const QRhiBufferData
//      &data)
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZN19QD3D11CommandBuffer16retainBufferDataERK14QRhiBufferData(
    QD3D11CommandBuffer *self,
    const QRhiBufferData *data) {
  return self->retainBufferData(*data);
}

//  const uchar *QD3D11CommandBuffer::retainImage(const QImage &image)
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZN19QD3D11CommandBuffer11retainImageERK6QImage(
    QD3D11CommandBuffer *self,
    const QImage *image) {
  return self->retainImage(*image);
}

//  int QD3D11CommandBuffer::retainResourceBatches(const
//      QD3D11ShaderResourceBindings::ResourceBatches &resourceBatches)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QD3D11CommandBuffer21retainResourceBatchesERKN28QD3D11ShaderResourceBindings15ResourceBatchesE(
    QD3D11CommandBuffer *self,
    const QD3D11ShaderResourceBindings::ResourceBatches *resourceBatches) {
  return self->retainResourceBatches(*resourceBatches);
}

//  void QD3D11CommandBuffer::resetCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QD3D11CommandBuffer13resetCommandsEv(
    QD3D11CommandBuffer *self) {
  self->resetCommands();
}

//  void QD3D11CommandBuffer::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QD3D11CommandBuffer10resetStateEv(
    QD3D11CommandBuffer *self) {
  self->resetState();
}

//  void QD3D11CommandBuffer::resetCachedState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QD3D11CommandBuffer16resetCachedStateEv(
    QD3D11CommandBuffer *self) {
  self->resetCachedState();
}

#endif  // defined(Q_OS_WIN)
