//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopengl_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopengl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/QSet>
#include <QtCore/QString>
#include <QtCore/QVersionNumber>
#include <QtCore/QJsonDocument>

//  QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const QString
//      &osName, const QVersionNumber &kernelVersion, const QString
//      &osVersion, const QJsonDocument &doc)
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZN13QOpenGLConfig11gpuFeaturesERKNS_3GpuERK7QStringRK14QVersionNumberS5_RK13QJsonDocument(
    const QOpenGLConfig::Gpu *gpu,
    const QString *osName,
    const QVersionNumber *kernelVersion,
    const QString *osVersion,
    const QJsonDocument *doc) {
  return new QSet<QString>(
      QOpenGLConfig::gpuFeatures(
          *gpu,
          *osName,
          *kernelVersion,
          *osVersion,
          *doc));
}

//  QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const QString
//      &osName, const QVersionNumber &kernelVersion, const QString
//      &osVersion, const QString &fileName)
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZN13QOpenGLConfig11gpuFeaturesERKNS_3GpuERK7QStringRK14QVersionNumberS5_S5_(
    const QOpenGLConfig::Gpu *gpu,
    const QString *osName,
    const QVersionNumber *kernelVersion,
    const QString *osVersion,
    const QString *fileName) {
  return new QSet<QString>(
      QOpenGLConfig::gpuFeatures(
          *gpu,
          *osName,
          *kernelVersion,
          *osVersion,
          *fileName));
}

//  QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const
//      QJsonDocument &doc)
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZN13QOpenGLConfig11gpuFeaturesERKNS_3GpuERK13QJsonDocument(
    const QOpenGLConfig::Gpu *gpu,
    const QJsonDocument *doc) {
  return new QSet<QString>(QOpenGLConfig::gpuFeatures(*gpu, *doc));
}

//  QSet<QString> QOpenGLConfig::gpuFeatures(const Gpu &gpu, const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZN13QOpenGLConfig11gpuFeaturesERKNS_3GpuERK7QString(
    const QOpenGLConfig::Gpu *gpu,
    const QString *fileName) {
  return new QSet<QString>(QOpenGLConfig::gpuFeatures(*gpu, *fileName));
}

//  QOpenGLConfig::~QOpenGLConfig()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpenGLConfigD1Ev(QOpenGLConfig *self) {
  delete self;
}

//  a QSet<QString> a ritual of QOpenGLConfig gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLConfig__QSet_QString(QSet<QString> *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
