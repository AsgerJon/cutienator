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
#include <QtCore/qstring.h>

//  QOpenGLProgramBinaryCache::QOpenGLProgramBinaryCache()
extern "C" Q_DECL_EXPORT
QOpenGLProgramBinaryCache *ritual_ZN25QOpenGLProgramBinaryCacheC1Ev() {
  return new QOpenGLProgramBinaryCache();
}

//  bool QOpenGLProgramBinaryCache::load(const QByteArray &cacheKey, uint
//      programId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QOpenGLProgramBinaryCache4loadERK10QByteArrayj(
    QOpenGLProgramBinaryCache *self,
    const QByteArray *cacheKey,
    uint programId) {
  return self->load(*cacheKey, programId);
}

//  void QOpenGLProgramBinaryCache::save(const QByteArray &cacheKey, uint
//      programId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLProgramBinaryCache4saveERK10QByteArrayj(
    QOpenGLProgramBinaryCache *self,
    const QByteArray *cacheKey,
    uint programId) {
  self->save(*cacheKey, programId);
}

//  QString QOpenGLProgramBinaryCache::cacheFileName(const QByteArray
//      &cacheKey) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpenGLProgramBinaryCache13cacheFileNameERK10QByteArray(
    const QOpenGLProgramBinaryCache *self,
    const QByteArray *cacheKey) {
  return new QString(self->cacheFileName(*cacheKey));
}

//  bool QOpenGLProgramBinaryCache::verifyHeader(const QByteArray &buf) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpenGLProgramBinaryCache12verifyHeaderERK10QByteArray(
    const QOpenGLProgramBinaryCache *self,
    const QByteArray *buf) {
  return self->verifyHeader(*buf);
}

#endif  // QT_CONFIG(opengl)
