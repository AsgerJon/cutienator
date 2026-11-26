//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickScreenInfo that Python can take functions over in. Every QQuickScreenInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScreenInfoCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScreenInfoCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScreenInfoCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScreenInfoCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScreenInfoCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScreenInfoCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScreenInfoCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScreenInfo : public QQuickScreenInfo {
public:
  using QQuickScreenInfo::QQuickScreenInfo;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScreenInfoCall0 call = reinterpret_cast<CuteQQuickScreenInfoCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScreenInfoCall1 call = reinterpret_cast<CuteQQuickScreenInfoCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScreenInfoCall2 call = reinterpret_cast<CuteQQuickScreenInfoCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScreenInfoCall3 call = reinterpret_cast<CuteQQuickScreenInfoCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickScreenInfoCall4 call = reinterpret_cast<CuteQQuickScreenInfoCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickScreenInfoCall5 call = reinterpret_cast<CuteQQuickScreenInfoCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickScreenInfoCall6 call = reinterpret_cast<CuteQQuickScreenInfoCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScreenInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickScreenInfo10metaObjectEv(
    const QQuickScreenInfo *self) {
  return self->metaObject();
}

//  void *QQuickScreenInfo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickScreenInfo11qt_metacastEPKc(
    QQuickScreenInfo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickScreenInfo::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickScreenInfo11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickScreenInfo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickScreenInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickScreenInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScreenInfo::tr(s, c, n));
}

//  void QQuickScreenInfo::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo24qt_qmlMarker_uncreatableEv(
    QQuickScreenInfo *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickScreenInfo::QQuickScreenInfo(QObject *parent, QScreen
//      *wrappedScreen)
extern "C" Q_DECL_EXPORT
QQuickScreenInfo *ritual_ZN16QQuickScreenInfoC1EP7QObjectP7QScreen(
    QObject *parent,
    QScreen *wrappedScreen) {
  return new CuteQQuickScreenInfo(parent, wrappedScreen);
}

//  QString QQuickScreenInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickScreenInfo4nameEv(const QQuickScreenInfo *self) {
  return new QString(self->name());
}

//  QString QQuickScreenInfo::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickScreenInfo12manufacturerEv(
    const QQuickScreenInfo *self) {
  return new QString(self->manufacturer());
}

//  QString QQuickScreenInfo::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickScreenInfo5modelEv(const QQuickScreenInfo *self) {
  return new QString(self->model());
}

//  QString QQuickScreenInfo::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickScreenInfo12serialNumberEv(
    const QQuickScreenInfo *self) {
  return new QString(self->serialNumber());
}

//  int QQuickScreenInfo::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo5widthEv(const QQuickScreenInfo *self) {
  return self->width();
}

//  int QQuickScreenInfo::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo6heightEv(const QQuickScreenInfo *self) {
  return self->height();
}

//  int QQuickScreenInfo::desktopAvailableWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo21desktopAvailableWidthEv(
    const QQuickScreenInfo *self) {
  return self->desktopAvailableWidth();
}

//  int QQuickScreenInfo::desktopAvailableHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo22desktopAvailableHeightEv(
    const QQuickScreenInfo *self) {
  return self->desktopAvailableHeight();
}

//  qreal QQuickScreenInfo::logicalPixelDensity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickScreenInfo19logicalPixelDensityEv(
    const QQuickScreenInfo *self) {
  return self->logicalPixelDensity();
}

//  qreal QQuickScreenInfo::pixelDensity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickScreenInfo12pixelDensityEv(
    const QQuickScreenInfo *self) {
  return self->pixelDensity();
}

//  qreal QQuickScreenInfo::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickScreenInfo16devicePixelRatioEv(
    const QQuickScreenInfo *self) {
  return self->devicePixelRatio();
}

//  Qt::ScreenOrientation QQuickScreenInfo::primaryOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK16QQuickScreenInfo18primaryOrientationEv(
    const QQuickScreenInfo *self) {
  return self->primaryOrientation();
}

//  Qt::ScreenOrientation QQuickScreenInfo::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK16QQuickScreenInfo11orientationEv(
    const QQuickScreenInfo *self) {
  return self->orientation();
}

//  int QQuickScreenInfo::virtualX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo8virtualXEv(const QQuickScreenInfo *self) {
  return self->virtualX();
}

//  int QQuickScreenInfo::virtualY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickScreenInfo8virtualYEv(const QQuickScreenInfo *self) {
  return self->virtualY();
}

//  void QQuickScreenInfo::setWrappedScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo16setWrappedScreenEP7QScreen(
    QQuickScreenInfo *self,
    QScreen *screen) {
  self->setWrappedScreen(screen);
}

//  QScreen *QQuickScreenInfo::wrappedScreen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK16QQuickScreenInfo13wrappedScreenEv(
    const QQuickScreenInfo *self) {
  return self->wrappedScreen();
}

//  void QQuickScreenInfo::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo11nameChangedEv(QQuickScreenInfo *self) {
  self->nameChanged();
}

//  void QQuickScreenInfo::manufacturerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo19manufacturerChangedEv(
    QQuickScreenInfo *self) {
  self->manufacturerChanged();
}

//  void QQuickScreenInfo::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo12modelChangedEv(QQuickScreenInfo *self) {
  self->modelChanged();
}

//  void QQuickScreenInfo::serialNumberChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo19serialNumberChangedEv(
    QQuickScreenInfo *self) {
  self->serialNumberChanged();
}

//  void QQuickScreenInfo::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo12widthChangedEv(QQuickScreenInfo *self) {
  self->widthChanged();
}

//  void QQuickScreenInfo::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo13heightChangedEv(QQuickScreenInfo *self) {
  self->heightChanged();
}

//  void QQuickScreenInfo::desktopGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo22desktopGeometryChangedEv(
    QQuickScreenInfo *self) {
  self->desktopGeometryChanged();
}

//  void QQuickScreenInfo::logicalPixelDensityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo26logicalPixelDensityChangedEv(
    QQuickScreenInfo *self) {
  self->logicalPixelDensityChanged();
}

//  void QQuickScreenInfo::pixelDensityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo19pixelDensityChangedEv(
    QQuickScreenInfo *self) {
  self->pixelDensityChanged();
}

//  void QQuickScreenInfo::devicePixelRatioChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo23devicePixelRatioChangedEv(
    QQuickScreenInfo *self) {
  self->devicePixelRatioChanged();
}

//  void QQuickScreenInfo::primaryOrientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo25primaryOrientationChangedEv(
    QQuickScreenInfo *self) {
  self->primaryOrientationChanged();
}

//  void QQuickScreenInfo::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo18orientationChangedEv(
    QQuickScreenInfo *self) {
  self->orientationChanged();
}

//  void QQuickScreenInfo::virtualXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo15virtualXChangedEv(QQuickScreenInfo *self) {
  self->virtualXChanged();
}

//  void QQuickScreenInfo::virtualYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickScreenInfo15virtualYChangedEv(QQuickScreenInfo *self) {
  self->virtualYChanged();
}

//  a Python function taken by a CuteQQuickScreenInfo, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScreenInfo(
    QQuickScreenInfo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScreenInfo *>(self)->take(key, call);
}
