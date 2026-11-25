//  Written by hand on 2026-11-25 from
//  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what
//  its header writes out. Not written: the constructor, which
//  needs the class's table of virtual functions, 'tr', the
//  slot 'process', the signal 'finished', and
//  'createGenerator', which makes a QQuickItemGenerator of
//  QtQuickVectorImageGenerator, a library the library of this
//  part is not joined to.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuickVectorImageWorker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickVectorImageWorker10metaObjectEv(
    const QQuickVectorImageWorker *self) {
  return self->metaObject();
}

//  QQuickVectorImageWorker::~QQuickVectorImageWorker()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVectorImageWorkerD1Ev(QQuickVectorImageWorker *self) {
  delete self;
}

//  QQuickItemGenerator *QQuickVectorImageWorker::generator() const
extern "C" Q_DECL_EXPORT
QQuickItemGenerator *ritual_ZNK23QQuickVectorImageWorker9generatorEv(
    const QQuickVectorImageWorker *self) {
  return self->generator();
}

//  void QQuickVectorImageWorker::addPluginGenerator(QQuickVectorImagePluginG
//      enerator *pluginGenerator)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVectorImageWorker18addPluginGeneratorEP32QQuickVectorImagePluginGenerator(
    QQuickVectorImageWorker *self,
    QQuickVectorImagePluginGenerator *pluginGenerator) {
  self->addPluginGenerator(pluginGenerator);
}
