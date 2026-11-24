//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QOpenGLMultiGroupSharedResource::QOpenGLMultiGroupSharedResource()
extern "C" Q_DECL_EXPORT
QOpenGLMultiGroupSharedResource *ritual_ZN31QOpenGLMultiGroupSharedResourceC1Ev() {
  return new QOpenGLMultiGroupSharedResource();
}

//  QOpenGLMultiGroupSharedResource::~QOpenGLMultiGroupSharedResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpenGLMultiGroupSharedResourceD1Ev(
    QOpenGLMultiGroupSharedResource *self) {
  delete self;
}

//  void QOpenGLMultiGroupSharedResource::insert(QOpenGLContext *context,
//      QOpenGLSharedResource *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpenGLMultiGroupSharedResource6insertEP14QOpenGLContextP21QOpenGLSharedResource(
    QOpenGLMultiGroupSharedResource *self,
    QOpenGLContext *context,
    QOpenGLSharedResource *value) {
  self->insert(context, value);
}

//  void QOpenGLMultiGroupSharedResource::cleanup(QOpenGLContextGroup *group,
//      QOpenGLSharedResource *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpenGLMultiGroupSharedResource7cleanupEP19QOpenGLContextGroupP21QOpenGLSharedResource(
    QOpenGLMultiGroupSharedResource *self,
    QOpenGLContextGroup *group,
    QOpenGLSharedResource *value) {
  self->cleanup(group, value);
}

//  QOpenGLSharedResource
//      *QOpenGLMultiGroupSharedResource::value(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLSharedResource *ritual_ZN31QOpenGLMultiGroupSharedResource5valueEP14QOpenGLContext(
    QOpenGLMultiGroupSharedResource *self,
    QOpenGLContext *context) {
  return self->value(context);
}

//  QList<QOpenGLSharedResource *>
//      QOpenGLMultiGroupSharedResource::resources() const
extern "C" Q_DECL_EXPORT
QList<QOpenGLSharedResource *> *ritual_ZNK31QOpenGLMultiGroupSharedResource9resourcesEv(
    const QOpenGLMultiGroupSharedResource *self) {
  return new QList<QOpenGLSharedResource *>(self->resources());
}

#endif  // !defined(QT_NO_OPENGL)
