//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qshader_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qshader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QShaderPrivate::QShaderPrivate()
extern "C" Q_DECL_EXPORT
QShaderPrivate *ritual_ZN14QShaderPrivateC1Ev() {
  return new QShaderPrivate();
}

//  QShaderPrivate::QShaderPrivate(const QShaderPrivate &other)
extern "C" Q_DECL_EXPORT
QShaderPrivate *ritual_ZN14QShaderPrivateC1ERKS_(
    const QShaderPrivate *other) {
  return new QShaderPrivate(*other);
}

//  QShaderPrivate *QShaderPrivate::get(QShader *s)
extern "C" Q_DECL_EXPORT
QShaderPrivate *ritual_ZN14QShaderPrivate3getEP7QShader(QShader *s) {
  return QShaderPrivate::get(s);
}

//  const QShaderPrivate *QShaderPrivate::get(const QShader *s)
extern "C" Q_DECL_EXPORT
const QShaderPrivate *ritual_ZN14QShaderPrivate3getEPK7QShader(
    const QShader *s) {
  return QShaderPrivate::get(s);
}

//  bool QShaderPrivate::readCount(QDataStream *stream, int *count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QShaderPrivate9readCountEP11QDataStreamPi(
    QDataStream *stream,
    int *count) {
  return QShaderPrivate::readCount(stream, count);
}

//  int QShaderPrivate::qtQsbVersion(QShader::SerializedFormatVersion
//      qtVersion)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QShaderPrivate12qtQsbVersionEN7QShader23SerializedFormatVersionE(
    QShader::SerializedFormatVersion qtVersion) {
  return QShaderPrivate::qtQsbVersion(qtVersion);
}

//  QShaderPrivate::~QShaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QShaderPrivateD1Ev(QShaderPrivate *self) {
  delete self;
}
