//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/aspectcommanddebugger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/aspectcommanddebugger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  qsizetype Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::size()
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer4sizeEv(
    const Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer *self) {
  return self->size();
}

//  void Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::insert(const
//      QByteArray &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer6insertERK10QByteArray(
    Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer *self,
    const QByteArray *array) {
  self->insert(*array);
}

//  void Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::trim()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer4trimEv(
    Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer *self) {
  self->trim();
}

//  Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::~ReadBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBufferD1Ev(
    Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer *self) {
  delete self;
}
