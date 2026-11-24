//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
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

//  QOpenGLContextGroup *QOpenGLContextGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpenGLContextGroup *ritual_ZN26QOpenGLContextGroupPrivate6q_funcEv(
    QOpenGLContextGroupPrivate *self) {
  return self->q_func();
}

//  const QOpenGLContextGroup *QOpenGLContextGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLContextGroup *ritual_ZNK26QOpenGLContextGroupPrivate6q_funcEv(
    const QOpenGLContextGroupPrivate *self) {
  return self->q_func();
}

//  QOpenGLContextGroupPrivate::QOpenGLContextGroupPrivate()
extern "C" Q_DECL_EXPORT
QOpenGLContextGroupPrivate *ritual_ZN26QOpenGLContextGroupPrivateC1Ev() {
  return new QOpenGLContextGroupPrivate();
}

//  QOpenGLContextGroupPrivate::~QOpenGLContextGroupPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLContextGroupPrivateD1Ev(
    QOpenGLContextGroupPrivate *self) {
  delete self;
}

//  void QOpenGLContextGroupPrivate::addContext(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLContextGroupPrivate10addContextEP14QOpenGLContext(
    QOpenGLContextGroupPrivate *self,
    QOpenGLContext *ctx) {
  self->addContext(ctx);
}

//  void QOpenGLContextGroupPrivate::removeContext(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLContextGroupPrivate13removeContextEP14QOpenGLContext(
    QOpenGLContextGroupPrivate *self,
    QOpenGLContext *ctx) {
  self->removeContext(ctx);
}

//  void QOpenGLContextGroupPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLContextGroupPrivate7cleanupEv(
    QOpenGLContextGroupPrivate *self) {
  self->cleanup();
}

//  void QOpenGLContextGroupPrivate::deletePendingResources(QOpenGLContext
//      *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLContextGroupPrivate22deletePendingResourcesEP14QOpenGLContext(
    QOpenGLContextGroupPrivate *self,
    QOpenGLContext *ctx) {
  self->deletePendingResources(ctx);
}

#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
