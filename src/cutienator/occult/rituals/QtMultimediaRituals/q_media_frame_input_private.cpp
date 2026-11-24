//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmediaframeinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmediaframeinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qmediaframeinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/qmediaframeinput.cpp, line 8, as _ZN23QMediaFrameInputPrivate17setCaptureSessionEP20QMediaCaptureSession
inline void QMediaFrameInputPrivate::setCaptureSession(QMediaCaptureSession *session)
{
    if (session == m_captureSession)
        return;

    auto prevSession = std::exchange(m_captureSession, session);
    updateCaptureSessionConnections(prevSession, session);
    updateCanSendMediaFrame();
}

//  from ../qtmultimedia/src/multimedia/qmediaframeinput.cpp, line 18, as _ZN23QMediaFrameInputPrivate23updateCanSendMediaFrameEv
inline void QMediaFrameInputPrivate::updateCanSendMediaFrame()
{
    const bool canSendMediaFrame = m_captureSession && checkIfCanSendMediaFrame();
    if (m_canSendMediaFrame != canSendMediaFrame) {
        m_canSendMediaFrame = canSendMediaFrame;
        if (m_canSendMediaFrame)
            emitReadyToSendMediaFrame();
    }
}

//  from ../qtmultimedia/src/multimedia/qmediaframeinput.cpp, line 28, as _ZN23QMediaFrameInputPrivate24postponeCheckReadyToSendEv
inline void QMediaFrameInputPrivate::postponeCheckReadyToSend()
{
    if (m_canSendMediaFrame && !m_postponeReadyToSendCheckRun) {
        m_postponeReadyToSendCheckRun = true;
        QMetaObject::invokeMethod(
                q_ptr,
                [this]() {
                    m_postponeReadyToSendCheckRun = false;
                    if (m_canSendMediaFrame)
                        emitReadyToSendMediaFrame();
                },
                Qt::QueuedConnection);
    }
}
//  -----------------------------------------------------------------------

//  void QMediaFrameInputPrivate::setCaptureSession(QMediaCaptureSession
//      *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMediaFrameInputPrivate17setCaptureSessionEP20QMediaCaptureSession(
    QMediaFrameInputPrivate *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  QMediaCaptureSession *QMediaFrameInputPrivate::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK23QMediaFrameInputPrivate14captureSessionEv(
    const QMediaFrameInputPrivate *self) {
  return self->captureSession();
}

//  void QMediaFrameInputPrivate::updateCanSendMediaFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMediaFrameInputPrivate23updateCanSendMediaFrameEv(
    QMediaFrameInputPrivate *self) {
  self->updateCanSendMediaFrame();
}

//  void QMediaFrameInputPrivate::postponeCheckReadyToSend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMediaFrameInputPrivate24postponeCheckReadyToSendEv(
    QMediaFrameInputPrivate *self) {
  self->postponeCheckReadyToSend();
}

//  bool QMediaFrameInputPrivate::checkIfCanSendMediaFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QMediaFrameInputPrivate24checkIfCanSendMediaFrameEv(
    const QMediaFrameInputPrivate *self) {
  return self->checkIfCanSendMediaFrame();
}

//  void QMediaFrameInputPrivate::emitReadyToSendMediaFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMediaFrameInputPrivate25emitReadyToSendMediaFrameEv(
    QMediaFrameInputPrivate *self) {
  self->emitReadyToSendMediaFrame();
}

//  void QMediaFrameInputPrivate::updateCaptureSessionConnections(QMediaCaptu
//      reSession *prevSession, QMediaCaptureSession *currentSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMediaFrameInputPrivate31updateCaptureSessionConnectionsEP20QMediaCaptureSessionS1_(
    QMediaFrameInputPrivate *self,
    QMediaCaptureSession *prevSession,
    QMediaCaptureSession *currentSession) {
  self->updateCaptureSessionConnections(prevSession, currentSession);
}
