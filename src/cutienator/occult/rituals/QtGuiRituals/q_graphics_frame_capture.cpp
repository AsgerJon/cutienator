//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(graphicsframecapture)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QGraphicsFrameCapture::QGraphicsFrameCapture()
extern "C" Q_DECL_EXPORT
QGraphicsFrameCapture *ritual_ZN21QGraphicsFrameCaptureC1Ev() {
  return new QGraphicsFrameCapture();
}

//  QGraphicsFrameCapture::~QGraphicsFrameCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCaptureD1Ev(QGraphicsFrameCapture *self) {
  delete self;
}

//  void QGraphicsFrameCapture::setRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCapture6setRhiEP4QRhi(
    QGraphicsFrameCapture *self,
    QRhi *rhi) {
  self->setRhi(rhi);
}

//  void QGraphicsFrameCapture::startCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCapture17startCaptureFrameEv(
    QGraphicsFrameCapture *self) {
  self->startCaptureFrame();
}

//  void QGraphicsFrameCapture::endCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCapture15endCaptureFrameEv(
    QGraphicsFrameCapture *self) {
  self->endCaptureFrame();
}

//  QString QGraphicsFrameCapture::capturePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QGraphicsFrameCapture11capturePathEv(
    const QGraphicsFrameCapture *self) {
  return new QString(self->capturePath());
}

//  void QGraphicsFrameCapture::setCapturePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCapture14setCapturePathERK7QString(
    QGraphicsFrameCapture *self,
    const QString *path) {
  self->setCapturePath(*path);
}

//  QString QGraphicsFrameCapture::capturePrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QGraphicsFrameCapture13capturePrefixEv(
    const QGraphicsFrameCapture *self) {
  return new QString(self->capturePrefix());
}

//  void QGraphicsFrameCapture::setCapturePrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsFrameCapture16setCapturePrefixERK7QString(
    QGraphicsFrameCapture *self,
    const QString *prefix) {
  self->setCapturePrefix(*prefix);
}

//  QString QGraphicsFrameCapture::capturedFileName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGraphicsFrameCapture16capturedFileNameEv(
    QGraphicsFrameCapture *self) {
  return new QString(self->capturedFileName());
}

//  QStringList QGraphicsFrameCapture::capturedFilesNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QGraphicsFrameCapture18capturedFilesNamesEv(
    QGraphicsFrameCapture *self) {
  return new QList<QString>(self->capturedFilesNames());
}

//  bool QGraphicsFrameCapture::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGraphicsFrameCapture8isLoadedEv(
    const QGraphicsFrameCapture *self) {
  return self->isLoaded();
}

//  bool QGraphicsFrameCapture::isCapturing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGraphicsFrameCapture11isCapturingEv(
    const QGraphicsFrameCapture *self) {
  return self->isCapturing();
}

//  void QGraphicsFrameCapture::openCapture() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QGraphicsFrameCapture11openCaptureEv(
    const QGraphicsFrameCapture *self) {
  self->openCapture();
}

#endif  // QT_CONFIG(graphicsframecapture)
