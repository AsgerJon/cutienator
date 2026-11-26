//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/private/qbatchrenderer_p.h>
#include <QImage>
#include <QPainter>
#include <QHash>
#include <QMap>
#include <QMutexLocker>
#include <QLoggingCategory>
#include <QThread>
#include <QJsonDocument>
#include <QJsonArray>
#include <QtLottie/private/qlottieconstants_p.h>
#include <QtLottie/private/qlottiebase_p.h>
#include <QtLottie/private/qlottieflatlayers_p.h>
#include <QtLottie/private/qlottieroot_p.h>
#include <QtLottie/private/qlottielayer_p.h>
#include <QtLottie/private/qlottieanimation_p.h>
#include <QtLottie/private/qlottierasterrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlottie/src/lottie/renderer/qbatchrenderer.cpp, line 226, as _ZN14QBatchRenderer3runEv
inline void QBatchRenderer::run()
{
    qCDebug(lcLottieQtLottieRenderThread) << "rendering thread" << QThread::currentThread();

    while (!isInterruptionRequested()) {
        QMutexLocker mlocker(&m_mutex);

        for (Entry *e : std::as_const(m_animData))
            prerender(e);

        m_waitCondition.wait(&m_mutex);
    }
}

//  from ../qtlottie/src/lottie/renderer/qbatchrenderer.cpp, line 165, as _ZN14QBatchRenderer8getFrameEP16QLottieAnimationi
inline QLottieRoot *QBatchRenderer::getFrame(QLottieAnimation *animator, int frameNumber)
{
    QMutexLocker mlocker(&m_mutex);

    Entry *entry = m_animData.value(animator, nullptr);
    if (entry)
        return entry->frameCache.value(frameNumber, nullptr);
    else
        return nullptr;
}
//  -----------------------------------------------------------------------

//  A QBatchRenderer that Python can take functions over in. Every QBatchRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBatchRendererCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBatchRendererCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBatchRendererCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBatchRendererCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBatchRendererCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBatchRendererCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBatchRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBatchRendererCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBatchRenderer : public QBatchRenderer {
public:
  using QBatchRenderer::QBatchRenderer;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QBatchRenderer::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBatchRendererCall0 call = reinterpret_cast<CuteQBatchRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QBatchRenderer::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBatchRendererCall1 call = reinterpret_cast<CuteQBatchRendererCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBatchRendererCall2 call = reinterpret_cast<CuteQBatchRendererCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBatchRendererCall3 call = reinterpret_cast<CuteQBatchRendererCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQBatchRendererCall4 call = reinterpret_cast<CuteQBatchRendererCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQBatchRendererCall5 call = reinterpret_cast<CuteQBatchRendererCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQBatchRendererCall6 call = reinterpret_cast<CuteQBatchRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBatchRendererCall7 call = reinterpret_cast<CuteQBatchRendererCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBatchRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QBatchRenderer10metaObjectEv(
    const QBatchRenderer *self) {
  return self->metaObject();
}

//  void *QBatchRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QBatchRenderer11qt_metacastEPKc(
    QBatchRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBatchRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QBatchRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    QBatchRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QBatchRenderer::~QBatchRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRendererD1Ev(QBatchRenderer *self) {
  delete self;
}

//  QLottieRoot *QBatchRenderer::getFrame(QLottieAnimation *animator, int
//      frameNumber)
extern "C" Q_DECL_EXPORT
QLottieRoot *ritual_ZN14QBatchRenderer8getFrameEP16QLottieAnimationi(
    QBatchRenderer *self,
    QLottieAnimation *animator,
    int frameNumber) {
  return self->getFrame(animator, frameNumber);
}

//  void QBatchRenderer::frameReady(QLottieAnimation *animator, int
//      frameNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRenderer10frameReadyEP16QLottieAnimationi(
    QBatchRenderer *self,
    QLottieAnimation *animator,
    int frameNumber) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QBatchRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "frameReady(QLottieAnimation *,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "frameReady(QLottieAnimation *,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&animator)),
      const_cast<void *>(static_cast<const void *>(&frameNumber)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QBatchRenderer::registerAnimator(QLottieAnimation *animator)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRenderer16registerAnimatorEP16QLottieAnimation(
    QBatchRenderer *self,
    QLottieAnimation *animator) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QBatchRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "registerAnimator(QLottieAnimation *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "registerAnimator(QLottieAnimation *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&animator)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QBatchRenderer::deregisterAnimator(QLottieAnimation *animator)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRenderer18deregisterAnimatorEP16QLottieAnimation(
    QBatchRenderer *self,
    QLottieAnimation *animator) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QBatchRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "deregisterAnimator(QLottieAnimation *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "deregisterAnimator(QLottieAnimation *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&animator)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QBatchRenderer::frameRendered(QLottieAnimation *animator, int
//      frameNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRenderer13frameRenderedEP16QLottieAnimationi(
    QBatchRenderer *self,
    QLottieAnimation *animator,
    int frameNumber) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QBatchRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "frameRendered(QLottieAnimation *,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "frameRendered(QLottieAnimation *,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&animator)),
      const_cast<void *>(static_cast<const void *>(&frameNumber)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QBatchRenderer::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBatchRenderer3runEv(QBatchRenderer *self) {
  self->run();
}

//  a Python function taken by a CuteQBatchRenderer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBatchRenderer(
    QBatchRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBatchRenderer *>(self)->take(key, call);
}
