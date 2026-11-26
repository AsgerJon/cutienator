//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickgraphicsconfiguration.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickgraphicsconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QQuickGraphicsConfiguration::QQuickGraphicsConfiguration()
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfiguration *ritual_ZN27QQuickGraphicsConfigurationC1Ev() {
  return new QQuickGraphicsConfiguration();
}

//  QQuickGraphicsConfiguration::~QQuickGraphicsConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfigurationD1Ev(
    QQuickGraphicsConfiguration *self) {
  delete self;
}

//  QQuickGraphicsConfiguration::QQuickGraphicsConfiguration(const
//      QQuickGraphicsConfiguration &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfiguration *ritual_ZN27QQuickGraphicsConfigurationC1ERKS_(
    const QQuickGraphicsConfiguration *other) {
  return new QQuickGraphicsConfiguration(*other);
}

//  QQuickGraphicsConfiguration &QQuickGraphicsConfiguration::operator=(const
//      QQuickGraphicsConfiguration &other)
extern "C" Q_DECL_EXPORT
QQuickGraphicsConfiguration *ritual_ZN27QQuickGraphicsConfigurationaSERKS_(
    QQuickGraphicsConfiguration *self,
    const QQuickGraphicsConfiguration *other) {
  return &(self->operator=(*other));
}

//  QByteArrayList QQuickGraphicsConfiguration::preferredInstanceExtensions()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN27QQuickGraphicsConfiguration27preferredInstanceExtensionsEv() {
  return new QList<QByteArray>(
      QQuickGraphicsConfiguration::preferredInstanceExtensions());
}

//  void QQuickGraphicsConfiguration::setDeviceExtensions(const
//      QByteArrayList &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration19setDeviceExtensionsERK5QListI10QByteArrayE(
    QQuickGraphicsConfiguration *self,
    const QList<QByteArray> *extensions) {
  self->setDeviceExtensions(*extensions);
}

//  QByteArrayList QQuickGraphicsConfiguration::deviceExtensions() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK27QQuickGraphicsConfiguration16deviceExtensionsEv(
    const QQuickGraphicsConfiguration *self) {
  return new QList<QByteArray>(self->deviceExtensions());
}

//  void QQuickGraphicsConfiguration::setDepthBufferFor2D(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration19setDepthBufferFor2DEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setDepthBufferFor2D(enable);
}

//  bool QQuickGraphicsConfiguration::isDepthBufferEnabledFor2D() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration25isDepthBufferEnabledFor2DEv(
    const QQuickGraphicsConfiguration *self) {
  return self->isDepthBufferEnabledFor2D();
}

//  void QQuickGraphicsConfiguration::setDebugLayer(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration13setDebugLayerEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setDebugLayer(enable);
}

//  bool QQuickGraphicsConfiguration::isDebugLayerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration19isDebugLayerEnabledEv(
    const QQuickGraphicsConfiguration *self) {
  return self->isDebugLayerEnabled();
}

//  void QQuickGraphicsConfiguration::setDebugMarkers(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration15setDebugMarkersEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setDebugMarkers(enable);
}

//  bool QQuickGraphicsConfiguration::isDebugMarkersEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration21isDebugMarkersEnabledEv(
    const QQuickGraphicsConfiguration *self) {
  return self->isDebugMarkersEnabled();
}

//  void QQuickGraphicsConfiguration::setTimestamps(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration13setTimestampsEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setTimestamps(enable);
}

//  bool QQuickGraphicsConfiguration::timestampsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration17timestampsEnabledEv(
    const QQuickGraphicsConfiguration *self) {
  return self->timestampsEnabled();
}

//  void QQuickGraphicsConfiguration::setPreferSoftwareDevice(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration23setPreferSoftwareDeviceEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setPreferSoftwareDevice(enable);
}

//  bool QQuickGraphicsConfiguration::prefersSoftwareDevice() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration21prefersSoftwareDeviceEv(
    const QQuickGraphicsConfiguration *self) {
  return self->prefersSoftwareDevice();
}

//  void QQuickGraphicsConfiguration::setAutomaticPipelineCache(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration25setAutomaticPipelineCacheEb(
    QQuickGraphicsConfiguration *self,
    bool enable) {
  self->setAutomaticPipelineCache(enable);
}

//  bool QQuickGraphicsConfiguration::isAutomaticPipelineCacheEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickGraphicsConfiguration31isAutomaticPipelineCacheEnabledEv(
    const QQuickGraphicsConfiguration *self) {
  return self->isAutomaticPipelineCacheEnabled();
}

//  void QQuickGraphicsConfiguration::setPipelineCacheSaveFile(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration24setPipelineCacheSaveFileERK7QString(
    QQuickGraphicsConfiguration *self,
    const QString *filename) {
  self->setPipelineCacheSaveFile(*filename);
}

//  QString QQuickGraphicsConfiguration::pipelineCacheSaveFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQuickGraphicsConfiguration21pipelineCacheSaveFileEv(
    const QQuickGraphicsConfiguration *self) {
  return new QString(self->pipelineCacheSaveFile());
}

//  void QQuickGraphicsConfiguration::setPipelineCacheLoadFile(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration24setPipelineCacheLoadFileERK7QString(
    QQuickGraphicsConfiguration *self,
    const QString *filename) {
  self->setPipelineCacheLoadFile(*filename);
}

//  QString QQuickGraphicsConfiguration::pipelineCacheLoadFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQuickGraphicsConfiguration21pipelineCacheLoadFileEv(
    const QQuickGraphicsConfiguration *self) {
  return new QString(self->pipelineCacheLoadFile());
}

//  void QQuickGraphicsConfiguration::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickGraphicsConfiguration6detachEv(
    QQuickGraphicsConfiguration *self) {
  self->detach();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK27QQuickGraphicsConfiguration(
    const QDebug *dbg,
    const QQuickGraphicsConfiguration *config) {
  return new QDebug(operator<<(*dbg, *config));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
