//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(graphicsframecapture)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qgraphicsframecapture_p.h>
#if (defined (Q_OS_WIN) || defined(Q_OS_LINUX)) && QT_CONFIG(library)
#elif QT_CONFIG(metal)
#include <QtGui/private/qgraphicsframecapturemetal_p_p.h>
#else
#include <QtGui/private/qgraphicsframecapture_p_p.h>
#endif
#include <QtCore/qstandardpaths.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qgraphicsframecapture.cpp, line 19, as _ZN28QGraphicsFrameCapturePrivateC1Ev
inline QGraphicsFrameCapturePrivate::QGraphicsFrameCapturePrivate()
    : m_capturePath(QStandardPaths::writableLocation(QStandardPaths::TempLocation) +
                    QStringLiteral("/") + QCoreApplication::applicationName() +
                    QStringLiteral("/captures")),
      m_capturePrefix(QCoreApplication::applicationName())
{

}
//  -----------------------------------------------------------------------

//  A QGraphicsFrameCapturePrivate that Python can take functions over in. Every QGraphicsFrameCapturePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsFrameCapturePrivateCall0)(const void *, QRhi *, int *);
typedef void (*CuteQGraphicsFrameCapturePrivateCall1)(const void *, int *);
typedef void (*CuteQGraphicsFrameCapturePrivateCall2)(const void *, int *);
typedef void (*CuteQGraphicsFrameCapturePrivateCall3)(const void *, const QString *, int *);
typedef void (*CuteQGraphicsFrameCapturePrivateCall4)(const void *, const QString *, int *);
typedef QString * (*CuteQGraphicsFrameCapturePrivateCall5)(const void *, int *);
typedef bool (*CuteQGraphicsFrameCapturePrivateCall6)(const void *, int *);
typedef bool (*CuteQGraphicsFrameCapturePrivateCall7)(const void *, int *);
typedef void (*CuteQGraphicsFrameCapturePrivateCall8)(const void *, int *);
class CuteQGraphicsFrameCapturePrivate : public QGraphicsFrameCapturePrivate {
public:
  using QGraphicsFrameCapturePrivate::QGraphicsFrameCapturePrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate6setRhiEP4QRhi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate17startCaptureFrameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate15endCaptureFrameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate11initializedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QGraphicsFrameCapturePrivate11isCapturingEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QGraphicsFrameCapturePrivate11openCaptureEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsFrameCapturePrivate::setRhi(QRhi *rhi)
  void setRhi(QRhi *rhi) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall0 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall0>(taken[0]);
      call(this, rhi, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsFrameCapturePrivate::startCaptureFrame()
  void startCaptureFrame() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall1 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsFrameCapturePrivate::endCaptureFrame()
  void endCaptureFrame() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall2 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsFrameCapturePrivate::setCapturePath(const QString
  //      &path)
  void setCapturePath(const QString &path) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall3 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall3>(taken[3]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QGraphicsFrameCapturePrivate::setCapturePath(path);
  }

  //  void QGraphicsFrameCapturePrivate::setCapturePrefix(const QString
  //      &prefix)
  void setCapturePrefix(const QString &prefix) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall4 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall4>(taken[4]);
      call(this, &prefix, &handled);
      if (handled) return;
    }
    QGraphicsFrameCapturePrivate::setCapturePrefix(prefix);
  }

  //  QString QGraphicsFrameCapturePrivate::capturedFileName() const
  QString capturedFileName() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall5 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGraphicsFrameCapturePrivate::capturedFileName();
  }

  //  bool QGraphicsFrameCapturePrivate::initialized() const
  bool initialized() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall6 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGraphicsFrameCapturePrivate::isCapturing() const
  bool isCapturing() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall7 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QGraphicsFrameCapturePrivate::openCapture()
  void openCapture() override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsFrameCapturePrivateCall8 call = reinterpret_cast<CuteQGraphicsFrameCapturePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QGraphicsFrameCapturePrivate::QGraphicsFrameCapturePrivate()
extern "C" Q_DECL_EXPORT
QGraphicsFrameCapturePrivate *ritual_ZN28QGraphicsFrameCapturePrivateC1Ev() {
  return new CuteQGraphicsFrameCapturePrivate();
}

//  QGraphicsFrameCapturePrivate::~QGraphicsFrameCapturePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivateD1Ev(
    QGraphicsFrameCapturePrivate *self) {
  delete self;
}

//  void QGraphicsFrameCapturePrivate::setRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate6setRhiEP4QRhi(
    QGraphicsFrameCapturePrivate *self,
    QRhi *rhi) {
  self->setRhi(rhi);
}

//  void QGraphicsFrameCapturePrivate::startCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate17startCaptureFrameEv(
    QGraphicsFrameCapturePrivate *self) {
  self->startCaptureFrame();
}

//  void QGraphicsFrameCapturePrivate::endCaptureFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate15endCaptureFrameEv(
    QGraphicsFrameCapturePrivate *self) {
  self->endCaptureFrame();
}

//  QString QGraphicsFrameCapturePrivate::capturePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QGraphicsFrameCapturePrivate11capturePathEv(
    const QGraphicsFrameCapturePrivate *self) {
  return new QString(self->capturePath());
}

//  void QGraphicsFrameCapturePrivate::setCapturePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString(
    QGraphicsFrameCapturePrivate *self,
    const QString *path) {
  self->setCapturePath(*path);
}

//  QString QGraphicsFrameCapturePrivate::capturePrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QGraphicsFrameCapturePrivate13capturePrefixEv(
    const QGraphicsFrameCapturePrivate *self) {
  return new QString(self->capturePrefix());
}

//  void QGraphicsFrameCapturePrivate::setCapturePrefix(const QString
//      &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QString(
    QGraphicsFrameCapturePrivate *self,
    const QString *prefix) {
  self->setCapturePrefix(*prefix);
}

//  QString QGraphicsFrameCapturePrivate::capturedFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv(
    const QGraphicsFrameCapturePrivate *self) {
  return new QString(self->capturedFileName());
}

//  QStringList QGraphicsFrameCapturePrivate::capturedFilesNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QGraphicsFrameCapturePrivate18capturedFilesNamesEv(
    const QGraphicsFrameCapturePrivate *self) {
  return new QList<QString>(self->capturedFilesNames());
}

//  bool QGraphicsFrameCapturePrivate::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QGraphicsFrameCapturePrivate11initializedEv(
    const QGraphicsFrameCapturePrivate *self) {
  return self->initialized();
}

//  bool QGraphicsFrameCapturePrivate::isCapturing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QGraphicsFrameCapturePrivate11isCapturingEv(
    const QGraphicsFrameCapturePrivate *self) {
  return self->isCapturing();
}

//  void QGraphicsFrameCapturePrivate::openCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGraphicsFrameCapturePrivate11openCaptureEv(
    QGraphicsFrameCapturePrivate *self) {
  self->openCapture();
}

//  a Python function taken by a CuteQGraphicsFrameCapturePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsFrameCapturePrivate(
    QGraphicsFrameCapturePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsFrameCapturePrivate *>(self)->take(key, call);
}

//  void QGraphicsFrameCapturePrivate::setCapturePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString(
    QGraphicsFrameCapturePrivate *self,
    const QString *path) {
  self->QGraphicsFrameCapturePrivate::setCapturePath(*path);
}

//  void QGraphicsFrameCapturePrivate::setCapturePrefix(const QString
//      &prefix)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QString(
    QGraphicsFrameCapturePrivate *self,
    const QString *prefix) {
  self->QGraphicsFrameCapturePrivate::setCapturePrefix(*prefix);
}

//  QString QGraphicsFrameCapturePrivate::capturedFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv(
    const QGraphicsFrameCapturePrivate *self) {
  return new QString(self->QGraphicsFrameCapturePrivate::capturedFileName());
}

#endif  // QT_CONFIG(graphicsframecapture)
