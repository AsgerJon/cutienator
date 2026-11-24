//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QVkCommandBuffer::ComputePassState::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer16ComputePassState5resetEv(
    QVkCommandBuffer::ComputePassState *self) {
  self->reset();
}

//  QVkCommandBuffer::ComputePassState::~ComputePassState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer16ComputePassStateD1Ev(
    QVkCommandBuffer::ComputePassState *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan)
