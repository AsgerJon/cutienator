//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the rituals of
//  toggleMakeCurrentTracker and cleanMakeCurrentTracker are taken
//  out, as they use static members (makeCurrentTracker and its
//  mutex) that Qt's library does not offer (undefined reference).
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qopenglcontext.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLContext *QOpenGLContextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN21QOpenGLContextPrivate6q_funcEv(
    QOpenGLContextPrivate *self) {
  return self->q_func();
}

//  const QOpenGLContext *QOpenGLContextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLContext *ritual_ZNK21QOpenGLContextPrivate6q_funcEv(
    const QOpenGLContextPrivate *self) {
  return self->q_func();
}

//  QOpenGLContextPrivate::QOpenGLContextPrivate()
extern "C" Q_DECL_EXPORT
QOpenGLContextPrivate *ritual_ZN21QOpenGLContextPrivateC1Ev() {
  return new QOpenGLContextPrivate();
}

//  QOpenGLContextPrivate::~QOpenGLContextPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLContextPrivateD1Ev(QOpenGLContextPrivate *self) {
  delete self;
}

//  void QOpenGLContextPrivate::adopt(QPlatformOpenGLContext *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLContextPrivate5adoptEP22QPlatformOpenGLContext(
    QOpenGLContextPrivate *self,
    QPlatformOpenGLContext *a0) {
  self->adopt(a0);
}

//  QOpenGLContext *QOpenGLContextPrivate::setCurrentContext(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN21QOpenGLContextPrivate17setCurrentContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLContextPrivate::setCurrentContext(context);
}

//  int QOpenGLContextPrivate::maxTextureSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN21QOpenGLContextPrivate14maxTextureSizeEv(
    QOpenGLContextPrivate *self) {
  return self->maxTextureSize();
}

//  QOpenGLContextPrivate *QOpenGLContextPrivate::get(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLContextPrivate *ritual_ZN21QOpenGLContextPrivate3getEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLContextPrivate::get(context);
}

//  void QOpenGLContextPrivate::_q_screenDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLContextPrivate18_q_screenDestroyedEP7QObject(
    QOpenGLContextPrivate *self,
    QObject *object) {
  self->_q_screenDestroyed(object);
}

#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
