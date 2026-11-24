//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>

//  QSize QtWayland::SharedMemoryBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QtWayland18SharedMemoryBuffer4sizeEv(
    const QtWayland::SharedMemoryBuffer *self) {
  return new QSize(self->QtWayland::SharedMemoryBuffer::size());
}

//  QWaylandSurface::Origin QtWayland::SharedMemoryBuffer::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface::Origin ritual_own_ZNK9QtWayland18SharedMemoryBuffer6originEv(
    const QtWayland::SharedMemoryBuffer *self) {
  return self->QtWayland::SharedMemoryBuffer::origin();
}

//  QImage QtWayland::SharedMemoryBuffer::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK9QtWayland18SharedMemoryBuffer5imageEv(
    const QtWayland::SharedMemoryBuffer *self) {
  return new QImage(self->QtWayland::SharedMemoryBuffer::image());
}

#if QT_CONFIG(opengl)
//  QOpenGLTexture *QtWayland::SharedMemoryBuffer::toOpenGlTexture(int plane)
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_own_ZN9QtWayland18SharedMemoryBuffer15toOpenGlTextureEi(
    QtWayland::SharedMemoryBuffer *self,
    int plane) {
  return self->QtWayland::SharedMemoryBuffer::toOpenGlTexture(plane);
}
#endif  // QT_CONFIG(opengl)
