//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qtquicktimelineglobal_p.h>
#include <QtQuickTimeline/QtQuickTimeline>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquickkeyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickKeyframeGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickKeyframeGroup : QQuickKeyframeGroup {
  using QQuickKeyframeGroup::classBegin;
  using QQuickKeyframeGroup::componentComplete;
};

//  A QQuickKeyframeGroup that Python can take functions over in. Every QQuickKeyframeGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickKeyframeGroupCall0)(const void *, int *);
typedef void (*CuteQQuickKeyframeGroupCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeyframeGroupCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickKeyframeGroupCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeGroupCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeGroupCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeGroupCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeGroupCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickKeyframeGroupCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickKeyframeGroup : public QQuickKeyframeGroup {
public:
  using QQuickKeyframeGroup::QQuickKeyframeGroup;
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

  //  void QQuickKeyframeGroup::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickKeyframeGroupCall0 call = reinterpret_cast<CuteQQuickKeyframeGroupCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickKeyframeGroup::classBegin();
  }

  //  void QQuickKeyframeGroup::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickKeyframeGroupCall1 call = reinterpret_cast<CuteQQuickKeyframeGroupCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickKeyframeGroup::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickKeyframeGroupCall2 call = reinterpret_cast<CuteQQuickKeyframeGroupCall2>(taken[2]);
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
      CuteQQuickKeyframeGroupCall3 call = reinterpret_cast<CuteQQuickKeyframeGroupCall3>(taken[3]);
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
      CuteQQuickKeyframeGroupCall4 call = reinterpret_cast<CuteQQuickKeyframeGroupCall4>(taken[4]);
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
      CuteQQuickKeyframeGroupCall5 call = reinterpret_cast<CuteQQuickKeyframeGroupCall5>(taken[5]);
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
      CuteQQuickKeyframeGroupCall6 call = reinterpret_cast<CuteQQuickKeyframeGroupCall6>(taken[6]);
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
      CuteQQuickKeyframeGroupCall7 call = reinterpret_cast<CuteQQuickKeyframeGroupCall7>(taken[7]);
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
      CuteQQuickKeyframeGroupCall8 call = reinterpret_cast<CuteQQuickKeyframeGroupCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickKeyframeGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickKeyframeGroup10metaObjectEv(
    const QQuickKeyframeGroup *self) {
  return self->metaObject();
}

//  QString QQuickKeyframeGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickKeyframeGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickKeyframeGroup::tr(s, c, n));
}

//  QQuickKeyframeGroup::QQuickKeyframeGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickKeyframeGroup *ritual_ZN19QQuickKeyframeGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickKeyframeGroup(parent);
}

//  QObject *QQuickKeyframeGroup::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK19QQuickKeyframeGroup6targetEv(
    const QQuickKeyframeGroup *self) {
  return self->target();
}

//  void QQuickKeyframeGroup::setTargetObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup15setTargetObjectEP7QObject(
    QQuickKeyframeGroup *self,
    QObject *a0) {
  self->setTargetObject(a0);
}

//  QString QQuickKeyframeGroup::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickKeyframeGroup8propertyEv(
    const QQuickKeyframeGroup *self) {
  return new QString(self->property());
}

//  void QQuickKeyframeGroup::setProperty(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup11setPropertyERK7QString(
    QQuickKeyframeGroup *self,
    const QString *a0) {
  self->setProperty(*a0);
}

//  QUrl QQuickKeyframeGroup::keyframeSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickKeyframeGroup14keyframeSourceEv(
    const QQuickKeyframeGroup *self) {
  return new QUrl(self->keyframeSource());
}

//  void QQuickKeyframeGroup::setKeyframeSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup17setKeyframeSourceERK4QUrl(
    QQuickKeyframeGroup *self,
    const QUrl *source) {
  self->setKeyframeSource(*source);
}

//  const QByteArray QQuickKeyframeGroup::keyframeData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QQuickKeyframeGroup12keyframeDataEv(
    const QQuickKeyframeGroup *self) {
  return new QByteArray(self->keyframeData());
}

//  void QQuickKeyframeGroup::setKeyframeData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup15setKeyframeDataERK10QByteArray(
    QQuickKeyframeGroup *self,
    const QByteArray *data) {
  self->setKeyframeData(*data);
}

//  QVariant QQuickKeyframeGroup::evaluate(qreal frame) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickKeyframeGroup8evaluateEd(
    const QQuickKeyframeGroup *self,
    qreal frame) {
  return new QVariant(self->evaluate(frame));
}

//  void QQuickKeyframeGroup::setProperty(qreal frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup11setPropertyEd(
    QQuickKeyframeGroup *self,
    qreal frame) {
  self->setProperty(frame);
}

//  void QQuickKeyframeGroup::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup4initEv(QQuickKeyframeGroup *self) {
  self->init();
}

//  void QQuickKeyframeGroup::resetDefaultValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup17resetDefaultValueEv(
    QQuickKeyframeGroup *self) {
  self->resetDefaultValue();
}

//  void QQuickKeyframeGroup::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup5resetEv(QQuickKeyframeGroup *self) {
  self->reset();
}

//  void QQuickKeyframeGroup::setupKeyframes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup14setupKeyframesEv(
    QQuickKeyframeGroup *self) {
  self->setupKeyframes();
}

//  void QQuickKeyframeGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup10classBeginEv(
    QQuickKeyframeGroup *self) {
  self->classBegin();
}

//  void QQuickKeyframeGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickKeyframeGroup17componentCompleteEv(
    QQuickKeyframeGroup *self) {
  self->componentComplete();
}

//  QQuickKeyframeGroup as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickKeyframeGroup_QQmlParserStatus(
    QQuickKeyframeGroup *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickKeyframeGroup, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickKeyframeGroup(
    QQuickKeyframeGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickKeyframeGroup *>(self)->take(key, call);
}

//  void QQuickKeyframeGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickKeyframeGroup10classBeginEv(
    QQuickKeyframeGroup *self) {
  static_cast<OwnQQuickKeyframeGroup *>(self)->OwnQQuickKeyframeGroup::classBegin();
}

//  void QQuickKeyframeGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickKeyframeGroup17componentCompleteEv(
    QQuickKeyframeGroup *self) {
  static_cast<OwnQQuickKeyframeGroup *>(self)->OwnQQuickKeyframeGroup::componentComplete();
}
