//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi_platform.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi_platform.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiGles2NativeHandles::~QRhiGles2NativeHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRhiGles2NativeHandlesD1Ev(QRhiGles2NativeHandles *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
