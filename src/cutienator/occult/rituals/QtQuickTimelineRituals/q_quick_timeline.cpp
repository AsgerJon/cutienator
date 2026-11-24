//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimeline_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qtquicktimelineglobal_p.h>
#include <QtQuickTimeline/QtQuickTimeline>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimeline_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimelineanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickTimeline may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTimeline : QQuickTimeline {
  using QQuickTimeline::classBegin;
  using QQuickTimeline::componentComplete;
};

//  A QQuickTimeline that Python can take functions over in. Every QQuickTimeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTimelineCall0)(const void *, int *);
typedef void (*CuteQQuickTimelineCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTimelineCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTimelineCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimelineCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimelineCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimelineCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimelineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimelineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTimeline : public QQuickTimeline {
public:
  using QQuickTimeline::QQuickTimeline;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickTimeline::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTimelineCall0 call = reinterpret_cast<CuteQQuickTimelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTimeline::classBegin();
  }

  //  void QQuickTimeline::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTimelineCall1 call = reinterpret_cast<CuteQQuickTimelineCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTimeline::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTimelineCall2 call = reinterpret_cast<CuteQQuickTimelineCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTimelineCall3 call = reinterpret_cast<CuteQQuickTimelineCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTimelineCall4 call = reinterpret_cast<CuteQQuickTimelineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTimelineCall5 call = reinterpret_cast<CuteQQuickTimelineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTimelineCall6 call = reinterpret_cast<CuteQQuickTimelineCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTimelineCall7 call = reinterpret_cast<CuteQQuickTimelineCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTimelineCall8 call = reinterpret_cast<CuteQQuickTimelineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTimeline::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTimeline10metaObjectEv(
    const QQuickTimeline *self) {
  return self->metaObject();
}

//  QString QQuickTimeline::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTimeline2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTimeline::tr(s, c, n));
}

//  QQuickTimeline::QQuickTimeline(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTimeline *ritual_ZN14QQuickTimelineC1EP7QObject(QObject *parent) {
  return new CuteQQuickTimeline(parent);
}

//  bool QQuickTimeline::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTimeline7enabledEv(const QQuickTimeline *self) {
  return self->enabled();
}

//  void QQuickTimeline::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline10setEnabledEb(
    QQuickTimeline *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  qreal QQuickTimeline::startFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTimeline10startFrameEv(const QQuickTimeline *self) {
  return self->startFrame();
}

//  void QQuickTimeline::setStartFrame(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline13setStartFrameEd(
    QQuickTimeline *self,
    qreal a0) {
  self->setStartFrame(a0);
}

//  qreal QQuickTimeline::endFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTimeline8endFrameEv(const QQuickTimeline *self) {
  return self->endFrame();
}

//  void QQuickTimeline::setEndFrame(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline11setEndFrameEd(
    QQuickTimeline *self,
    qreal a0) {
  self->setEndFrame(a0);
}

//  qreal QQuickTimeline::currentFrame() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTimeline12currentFrameEv(
    const QQuickTimeline *self) {
  return self->currentFrame();
}

//  void QQuickTimeline::setCurrentFrame(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline15setCurrentFrameEd(
    QQuickTimeline *self,
    qreal a0) {
  self->setCurrentFrame(a0);
}

//  void QQuickTimeline::reevaluate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline10reevaluateEv(QQuickTimeline *self) {
  self->reevaluate();
}

//  void QQuickTimeline::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline4initEv(QQuickTimeline *self) {
  self->init();
}

//  void QQuickTimeline::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline5resetEv(QQuickTimeline *self) {
  self->reset();
}

//  QList<QQuickTimelineAnimation *> QQuickTimeline::getAnimations() const
extern "C" Q_DECL_EXPORT
QList<QQuickTimelineAnimation *> *ritual_ZNK14QQuickTimeline13getAnimationsEv(
    const QQuickTimeline *self) {
  return new QList<QQuickTimelineAnimation *>(self->getAnimations());
}

//  void QQuickTimeline::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline10classBeginEv(QQuickTimeline *self) {
  self->classBegin();
}

//  void QQuickTimeline::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeline17componentCompleteEv(QQuickTimeline *self) {
  self->componentComplete();
}

//  QQuickTimeline as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickTimeline_QQmlParserStatus(
    QQuickTimeline *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickTimeline, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTimeline(
    QQuickTimeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTimeline *>(self)->take(key, call);
}

//  void QQuickTimeline::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTimeline10classBeginEv(QQuickTimeline *self) {
  static_cast<OwnQQuickTimeline *>(self)->OwnQQuickTimeline::classBegin();
}

//  void QQuickTimeline::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTimeline17componentCompleteEv(
    QQuickTimeline *self) {
  static_cast<OwnQQuickTimeline *>(self)->OwnQQuickTimeline::componentComplete();
}
