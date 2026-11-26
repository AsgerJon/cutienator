//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/6.12.0/QtTextToSpeech/private/qtexttospeech_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtTextToSpeech/qtexttospeech.h>
#include <QtTextToSpeech/QtTextToSpeech>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTextToSpeech/6.12.0/QtTextToSpeech/private/qtexttospeech_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QMultiHash>
#include <QtCore/QString>
#include <QtCore/QCborMap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtTextToSpeech/qtexttospeech.h>
#include <QtTextToSpeech/private/qtexttospeech_p.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtMultimedia/qaudiobuffer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtspeech/src/tts/qtexttospeech.cpp, line 24, as _ZN20QTextToSpeechPrivateC1EP13QTextToSpeech
inline QTextToSpeechPrivate::QTextToSpeechPrivate(QTextToSpeech *speech)
    : q_ptr(speech)
{
    qRegisterMetaType<QTextToSpeech::State>();
    qRegisterMetaType<QTextToSpeech::ErrorReason>();
}

//  from ../qtspeech/src/tts/qtexttospeech.cpp, line 31, as _ZN20QTextToSpeechPrivateD1Ev
inline QTextToSpeechPrivate::~QTextToSpeechPrivate()
{
}

//  from ../qtspeech/src/tts/qtexttospeech.cpp, line 155, as _ZN20QTextToSpeechPrivate11updateStateEN13QTextToSpeech5StateE
inline void QTextToSpeechPrivate::updateState(QTextToSpeech::State newState)
{
    Q_Q(QTextToSpeech);
    if (m_state == newState)
        return;

    if (newState == QTextToSpeech::Ready) {
        // If we have more text to process, start the next request immediately,
        // and ignore the transition to Ready (don't emit the signals).
        if (!m_pendingUtterances.isEmpty()) {
            const QString nextText = m_pendingUtterances.first();
            // QTextToSpeech::pause prepends an empty entry to request a pause
            if (nextText.isEmpty()) {
                m_state = QTextToSpeech::Paused;
                m_pendingUtterances.dequeue();
            } else {
                const auto nextFunction = [this]{
                    switch (m_state) {
                    case QTextToSpeech::Synthesizing:
                        return &QTextToSpeechEngine::synthesize;
                    case QTextToSpeech::Speaking:
                    case QTextToSpeech::Paused:
                        return &QTextToSpeechEngine::say;
                    default:
                        break;
                    }
                    return decltype(&QTextToSpeechEngine::synthesize)(nullptr);
                }();
                if (nextFunction) {
                    const auto oldState = m_state;
                    emit q->aboutToSynthesize(m_currentUtterance);
                    // connected slot could have called pause or stop, in which
                    // case the state changed or the pendingTexts got reset.
                    if (m_state == oldState && !m_pendingUtterances.isEmpty()) {
                        m_pendingUtterances.dequeue();
                        ++m_currentUtterance;
                        (m_engine.get()->*nextFunction)(nextText);
                        return;
                    } else if (m_state == QTextToSpeech::Paused) {
                        // In case of pause(), empty strings got inserted.
                        // We are already idle, so remove them again.
                        while (!m_pendingUtterances.isEmpty() && m_pendingUtterances.first().isEmpty())
                            m_pendingUtterances.dequeue();
                        return;
                    }
                    // in case of stop(), disconnect and update the state
                    disconnectSynthesizeFunctor();
                }
            }
        } else {
            // If we are done synthesizing and the functor-overload was used,
            // clear the temporary connection.
            disconnectSynthesizeFunctor();
        }
    }
    m_state = newState;
    emit q->stateChanged(newState);
}

//  from ../qtspeech/src/tts/qtexttospeech.cpp, line 214, as _ZN20QTextToSpeechPrivate27disconnectSynthesizeFunctorEv
inline void QTextToSpeechPrivate::disconnectSynthesizeFunctor()
{
    if (m_slotObject) {
        m_slotObject->destroyIfLastRef();
        m_slotObject = nullptr;
        m_engine->disconnect(m_synthesizeConnection);
    }
}
//  -----------------------------------------------------------------------

//  QTextToSpeech *QTextToSpeechPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextToSpeech *ritual_ZN20QTextToSpeechPrivate6q_funcEv(
    QTextToSpeechPrivate *self) {
  return self->q_func();
}

//  const QTextToSpeech *QTextToSpeechPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextToSpeech *ritual_ZNK20QTextToSpeechPrivate6q_funcEv(
    const QTextToSpeechPrivate *self) {
  return self->q_func();
}

//  QTextToSpeechPrivate::QTextToSpeechPrivate(QTextToSpeech *speech)
extern "C" Q_DECL_EXPORT
QTextToSpeechPrivate *ritual_ZN20QTextToSpeechPrivateC1EP13QTextToSpeech(
    QTextToSpeech *speech) {
  return new QTextToSpeechPrivate(speech);
}

//  QTextToSpeechPrivate::~QTextToSpeechPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextToSpeechPrivateD1Ev(QTextToSpeechPrivate *self) {
  delete self;
}

//  void QTextToSpeechPrivate::updateState(QTextToSpeech::State newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextToSpeechPrivate11updateStateEN13QTextToSpeech5StateE(
    QTextToSpeechPrivate *self,
    QTextToSpeech::State newState) {
  self->updateState(newState);
}

//  void QTextToSpeechPrivate::disconnectSynthesizeFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextToSpeechPrivate27disconnectSynthesizeFunctorEv(
    QTextToSpeechPrivate *self) {
  self->disconnectSynthesizeFunctor();
}

//  a QMultiHash<QString, QCborMap> a ritual of QTextToSpeechPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextToSpeechPrivate__QMultiHash_QString_QCborMap(
    QMultiHash<QString, QCborMap> *self) {
  delete self;
}
