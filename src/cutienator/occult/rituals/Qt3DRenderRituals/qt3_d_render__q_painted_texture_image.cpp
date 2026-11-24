//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qpaintedtextureimage.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qpaintedtextureimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QPaintedTextureImage that Python can take functions over in. Every Qt3DRender::QPaintedTextureImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QPaintedTextureImageCall0)(const void *, QPainter *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPaintedTextureImageCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPaintedTextureImageCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPaintedTextureImageCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPaintedTextureImageCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPaintedTextureImageCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPaintedTextureImageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPaintedTextureImageCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QPaintedTextureImage : public Qt3DRender::QPaintedTextureImage {
public:
  using Qt3DRender::QPaintedTextureImage::QPaintedTextureImage;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender20QPaintedTextureImage5paintEP8QPainter")) {
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

  //  void Qt3DRender::QPaintedTextureImage::paint(QPainter *painter)
  void paint(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QPaintedTextureImageCall0 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QPaintedTextureImageCall1 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QPaintedTextureImageCall2 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall2>(taken[2]);
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
      CuteQt3DRender_QPaintedTextureImageCall3 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall3>(taken[3]);
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
      CuteQt3DRender_QPaintedTextureImageCall4 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall4>(taken[4]);
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
      CuteQt3DRender_QPaintedTextureImageCall5 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall5>(taken[5]);
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
      CuteQt3DRender_QPaintedTextureImageCall6 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall6>(taken[6]);
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
      CuteQt3DRender_QPaintedTextureImageCall7 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QPaintedTextureImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender20QPaintedTextureImage10metaObjectEv(
    const Qt3DRender::QPaintedTextureImage *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QPaintedTextureImage::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender20QPaintedTextureImage2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QPaintedTextureImage::tr(s, c, n));
}

//  void Qt3DRender::QPaintedTextureImage::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QPaintedTextureImage5paintEP8QPainter(
    Qt3DRender::QPaintedTextureImage *self,
    QPainter *painter) {
  self->paint(painter);
}

//  QPaintedTextureImagePrivate *Qt3DRender::QPaintedTextureImage::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPaintedTextureImagePrivate *ritual_ZN10Qt3DRender20QPaintedTextureImage6d_funcEv(
    Qt3DRender::QPaintedTextureImage *self) {
  return self->d_func();
}

//  const QPaintedTextureImagePrivate
//      *Qt3DRender::QPaintedTextureImage::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPaintedTextureImagePrivate *ritual_ZNK10Qt3DRender20QPaintedTextureImage6d_funcEv(
    const Qt3DRender::QPaintedTextureImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QPaintedTextureImage, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPaintedTextureImage(
    Qt3DRender::QPaintedTextureImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPaintedTextureImage *>(self)->take(key, call);
}
