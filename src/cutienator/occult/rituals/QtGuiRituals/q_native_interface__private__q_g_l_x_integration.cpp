//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QNativeInterface::Private::QGLXIntegration::~QGLXIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QGLXIntegrationD1Ev(
    QNativeInterface::Private::QGLXIntegration *self) {
  delete self;
}

#endif  // QT_CONFIG(xcb_glx_plugin)
#endif  // !defined(QT_NO_OPENGL)
