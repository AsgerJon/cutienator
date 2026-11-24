//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLProgramBinarySupportCheck::QOpenGLProgramBinarySupportCheck(QOpenG
//      LContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLProgramBinarySupportCheck *ritual_ZN32QOpenGLProgramBinarySupportCheckC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLProgramBinarySupportCheck(context);
}

//  void QOpenGLProgramBinarySupportCheck::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLProgramBinarySupportCheck18invalidateResourceEv(
    QOpenGLProgramBinarySupportCheck *self) {
  self->invalidateResource();
}

//  void QOpenGLProgramBinarySupportCheck::freeResource(QOpenGLContext *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLProgramBinarySupportCheck12freeResourceEP14QOpenGLContext(
    QOpenGLProgramBinarySupportCheck *self,
    QOpenGLContext *a0) {
  self->freeResource(a0);
}

//  bool QOpenGLProgramBinarySupportCheck::isSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QOpenGLProgramBinarySupportCheck11isSupportedEv(
    const QOpenGLProgramBinarySupportCheck *self) {
  return self->isSupported();
}

//  void QOpenGLProgramBinarySupportCheck::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QOpenGLProgramBinarySupportCheck18invalidateResourceEv(
    QOpenGLProgramBinarySupportCheck *self) {
  self->QOpenGLProgramBinarySupportCheck::invalidateResource();
}

//  void QOpenGLProgramBinarySupportCheck::freeResource(QOpenGLContext *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QOpenGLProgramBinarySupportCheck12freeResourceEP14QOpenGLContext(
    QOpenGLProgramBinarySupportCheck *self,
    QOpenGLContext *a0) {
  self->QOpenGLProgramBinarySupportCheck::freeResource(a0);
}
