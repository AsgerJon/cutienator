//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#include <QtGui/qopenglcontext.h>

//  QNativeInterface::QGLXContext::~QGLXContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface11QGLXContextD1Ev(
    QNativeInterface::QGLXContext *self) {
  delete self;
}

#endif  // QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
