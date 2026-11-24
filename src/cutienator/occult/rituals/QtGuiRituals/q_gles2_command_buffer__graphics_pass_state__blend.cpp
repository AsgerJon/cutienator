//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGles2CommandBuffer::GraphicsPassState::Blend::~Blend()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBuffer17GraphicsPassState5BlendD1Ev(
    QGles2CommandBuffer::GraphicsPassState::Blend *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
