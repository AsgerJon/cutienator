//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QByteArray QOpenGLProgramBinaryCache::ProgramDesc::cacheKey() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QOpenGLProgramBinaryCache11ProgramDesc8cacheKeyEv(
    const QOpenGLProgramBinaryCache::ProgramDesc *self) {
  return new QByteArray(self->cacheKey());
}

//  QOpenGLProgramBinaryCache::ProgramDesc::~ProgramDesc()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLProgramBinaryCache11ProgramDescD1Ev(
    QOpenGLProgramBinaryCache::ProgramDesc *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
