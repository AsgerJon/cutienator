//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglfunctions.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/qopenglfunctions.h>

//  QOpenGLFunctionsPrivate::~QOpenGLFunctionsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLFunctionsPrivateD1Ev(QOpenGLFunctionsPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
