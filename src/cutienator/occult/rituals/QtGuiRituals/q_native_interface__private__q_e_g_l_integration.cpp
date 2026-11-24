//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QNativeInterface::Private::QEGLIntegration::~QEGLIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QEGLIntegrationD1Ev(
    QNativeInterface::Private::QEGLIntegration *self) {
  delete self;
}

#endif  // QT_CONFIG(egl)
#endif  // !defined(QT_NO_OPENGL)
