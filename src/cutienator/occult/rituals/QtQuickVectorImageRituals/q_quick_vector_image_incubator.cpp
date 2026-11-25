//  Written by hand on 2026-11-25 from
//  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Not written: the signal 'statusUpdated'.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimageincubator_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QQuickVectorImageIncubator may call these functions of
//  it. This one is, and makes them free for the rituals to call.
struct OwnQQuickVectorImageIncubator : QQuickVectorImageIncubator {
  using QQuickVectorImageIncubator::statusChanged;
};

//  A QQuickVectorImageIncubator that Python can take functions over in. Every
//  QQuickVectorImageIncubator Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQQuickVectorImageIncubatorCall0)(const void *, int, int *);
typedef void (*CuteQQuickVectorImageIncubatorCall1)(const void *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVectorImageIncubatorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVectorImageIncubatorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVectorImageIncubatorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVectorImageIncubatorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVectorImageIncubatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVectorImageIncubatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVectorImageIncubatorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickVectorImageIncubator : public QQuickVectorImageIncubator {
public:
  using QQuickVectorImageIncubator::QQuickVectorImageIncubator;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QQmlIncubator13statusChangedENS_6StatusE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QQmlIncubator15setInitialStateEP7QObject")) {
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

  //  void QQuickVectorImageIncubator::statusChanged(Status status)
  void statusChanged(QQmlIncubator::Status status) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickVectorImageIncubatorCall0 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall0>(taken[0]);
      call(this, static_cast<int>(status), &handled);
      if (handled) return;
    }
    QQuickVectorImageIncubator::statusChanged(status);
  }

  //  void QQmlIncubator::setInitialState(QObject *object)
  void setInitialState(QObject *object) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickVectorImageIncubatorCall1 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall1>(taken[1]);
      call(this, object, &handled);
      if (handled) return;
    }
    QQmlIncubator::setInitialState(object);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickVectorImageIncubatorCall2 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall2>(taken[2]);
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
      CuteQQuickVectorImageIncubatorCall3 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall3>(taken[3]);
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
      CuteQQuickVectorImageIncubatorCall4 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall4>(taken[4]);
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
      CuteQQuickVectorImageIncubatorCall5 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall5>(taken[5]);
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
      CuteQQuickVectorImageIncubatorCall6 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall6>(taken[6]);
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
      CuteQQuickVectorImageIncubatorCall7 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall7>(taken[7]);
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
      CuteQQuickVectorImageIncubatorCall8 call = reinterpret_cast<CuteQQuickVectorImageIncubatorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickVectorImageIncubator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickVectorImageIncubator10metaObjectEv(
    const QQuickVectorImageIncubator *self) {
  return self->metaObject();
}

//  QString QQuickVectorImageIncubator::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickVectorImageIncubator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickVectorImageIncubator::tr(s, c, n));
}

//  QQuickVectorImageIncubator::QQuickVectorImageIncubator(IncubationMode
//      incubationMode, QQmlContext *context, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickVectorImageIncubator *ritual_ZN26QQuickVectorImageIncubatorC1EN13QQmlIncubator14IncubationModeEP11QQmlContextP7QObject(
    QQmlIncubator::IncubationMode incubationMode,
    QQmlContext *context,
    QObject *parent) {
  return new CuteQQuickVectorImageIncubator(incubationMode, context, parent);
}

//  QQuickVectorImageIncubator::~QQuickVectorImageIncubator()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickVectorImageIncubatorD1Ev(
    QQuickVectorImageIncubator *self) {
  delete self;
}

//  void QQuickVectorImageIncubator::start(const QString &fileName,
//      QQuickVectorImageGenerator::GeneratorFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickVectorImageIncubator5startERK7QString6QFlagsIN26QQuickVectorImageGenerator13GeneratorFlagEE(
    QQuickVectorImageIncubator *self,
    const QString *fileName,
    int flags) {
  self->start(
      *fileName,
      QFlags<QQuickVectorImageGenerator::GeneratorFlag>::fromInt(flags));
}

//  QQmlIncubator::Status QQuickVectorImageIncubator::status() const
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZNK26QQuickVectorImageIncubator6statusEv(
    const QQuickVectorImageIncubator *self) {
  return self->status();
}

//  void QQuickVectorImageIncubator::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickVectorImageIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuickVectorImageIncubator *self,
    QQmlIncubator::Status status) {
  static_cast<OwnQQuickVectorImageIncubator *>(self)->statusChanged(status);
}

//  void QQuickVectorImageIncubator::generatorFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickVectorImageIncubator17generatorFinishedEv(
    QQuickVectorImageIncubator *self) {
  self->generatorFinished();
}

//  void QQuickVectorImageIncubator::componentUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickVectorImageIncubator16componentUpdatedEv(
    QQuickVectorImageIncubator *self) {
  self->componentUpdated();
}

//  a Python function taken by a CuteQQuickVectorImageIncubator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickVectorImageIncubator(
    QQuickVectorImageIncubator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickVectorImageIncubator *>(self)->take(key, call);
}

//  void QQuickVectorImageIncubator::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickVectorImageIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuickVectorImageIncubator *self,
    QQmlIncubator::Status status) {
  static_cast<OwnQQuickVectorImageIncubator *>(self)->OwnQQuickVectorImageIncubator::statusChanged(status);
}
