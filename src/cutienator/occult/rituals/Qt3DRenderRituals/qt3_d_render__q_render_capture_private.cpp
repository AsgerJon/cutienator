//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendercapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qrendercapture.h>
#include <Qt3DRender/private/qrendercapture_p.h>
#include <QtCore/QPointer>
#include <QtCore/QMutexLocker>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 186, as _ZN10Qt3DRender21QRenderCapturePrivateC1Ev
namespace Qt3DRender {
inline QRenderCapturePrivate::QRenderCapturePrivate()
    : QFrameGraphNodePrivate()
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 194, as _ZN10Qt3DRender21QRenderCapturePrivateD1Ev
namespace Qt3DRender {
inline QRenderCapturePrivate::~QRenderCapturePrivate()
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 201, as _ZN10Qt3DRender21QRenderCapturePrivate11createReplyEi
namespace Qt3DRender {
inline QRenderCaptureReply *QRenderCapturePrivate::createReply(int captureId)
{
    QMutexLocker lock(&m_mutex);
    QRenderCaptureReply *reply = new QRenderCaptureReply();
    reply->d_func()->m_captureId = captureId;
    m_waitingReplies.push_back(reply);
    return reply;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 213, as _ZN10Qt3DRender21QRenderCapturePrivate9takeReplyEi
namespace Qt3DRender {
inline QRenderCaptureReply *QRenderCapturePrivate::takeReply(int captureId)
{
    QRenderCaptureReply *reply = nullptr;
    QMutexLocker lock(&m_mutex);
    for (int i = 0; i < m_waitingReplies.size(); ++i) {
        if (m_waitingReplies[i]->d_func()->m_captureId == captureId) {
            reply = m_waitingReplies.takeAt(i);
            break;
        }
    }
    return reply;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 229, as _ZN10Qt3DRender21QRenderCapturePrivate8setImageEPNS_19QRenderCaptureReplyERK6QImage
namespace Qt3DRender {
inline void QRenderCapturePrivate::setImage(QRenderCaptureReply *reply, const QImage &image)
{
    reply->d_func()->m_complete = true;
    reply->d_func()->m_image = image;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/framegraph/qrendercapture.cpp, line 238, as _ZN10Qt3DRender21QRenderCapturePrivate14replyDestroyedEPNS_19QRenderCaptureReplyE
namespace Qt3DRender {
inline void QRenderCapturePrivate::replyDestroyed(QRenderCaptureReply *reply)
{
    QMutexLocker lock(&m_mutex);
    m_waitingReplies.removeAll(reply);
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QRenderCapturePrivate that Python can take functions over in. Every Qt3DRender::QRenderCapturePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderCapturePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QRenderCapturePrivateCall1)(const void *, int *);
class CuteQt3DRender_QRenderCapturePrivate : public Qt3DRender::QRenderCapturePrivate {
public:
  using Qt3DRender::QRenderCapturePrivate::QRenderCapturePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderCapturePrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderCapturePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderCapturePrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderCapturePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QRenderCapturePrivate::QRenderCapturePrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapturePrivate *ritual_ZN10Qt3DRender21QRenderCapturePrivateC1Ev() {
  return new CuteQt3DRender_QRenderCapturePrivate();
}

//  Qt3DRender::QRenderCapturePrivate::~QRenderCapturePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderCapturePrivateD1Ev(
    Qt3DRender::QRenderCapturePrivate *self) {
  delete self;
}

//  QRenderCaptureReply *Qt3DRender::QRenderCapturePrivate::createReply(int
//      captureId)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender21QRenderCapturePrivate11createReplyEi(
    Qt3DRender::QRenderCapturePrivate *self,
    int captureId) {
  return self->createReply(captureId);
}

//  QRenderCaptureReply *Qt3DRender::QRenderCapturePrivate::takeReply(int
//      captureId)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender21QRenderCapturePrivate9takeReplyEi(
    Qt3DRender::QRenderCapturePrivate *self,
    int captureId) {
  return self->takeReply(captureId);
}

//  void Qt3DRender::QRenderCapturePrivate::setImage(QRenderCaptureReply
//      *reply, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderCapturePrivate8setImageEPNS_19QRenderCaptureReplyERK6QImage(
    Qt3DRender::QRenderCapturePrivate *self,
    Qt3DRender::QRenderCaptureReply *reply,
    const QImage *image) {
  self->setImage(reply, *image);
}

//  void
//      Qt3DRender::QRenderCapturePrivate::replyDestroyed(QRenderCaptureReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderCapturePrivate14replyDestroyedEPNS_19QRenderCaptureReplyE(
    Qt3DRender::QRenderCapturePrivate *self,
    Qt3DRender::QRenderCaptureReply *reply) {
  self->replyDestroyed(reply);
}

//  QRenderCapture *Qt3DRender::QRenderCapturePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapture *ritual_ZN10Qt3DRender21QRenderCapturePrivate6q_funcEv(
    Qt3DRender::QRenderCapturePrivate *self) {
  return self->q_func();
}

//  const QRenderCapture *Qt3DRender::QRenderCapturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCapture *ritual_ZNK10Qt3DRender21QRenderCapturePrivate6q_funcEv(
    const Qt3DRender::QRenderCapturePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderCapturePrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderCapturePrivate(
    Qt3DRender::QRenderCapturePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderCapturePrivate *>(self)->take(key, call);
}
