//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformTextureList that Python can take functions over in. Every QPlatformTextureList
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformTextureListCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformTextureListCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformTextureListCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformTextureListCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformTextureListCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformTextureListCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformTextureListCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformTextureList : public QPlatformTextureList {
public:
  using QPlatformTextureList::QPlatformTextureList;
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
      CuteQPlatformTextureListCall0 call = reinterpret_cast<CuteQPlatformTextureListCall0>(taken[0]);
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
      CuteQPlatformTextureListCall1 call = reinterpret_cast<CuteQPlatformTextureListCall1>(taken[1]);
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
      CuteQPlatformTextureListCall2 call = reinterpret_cast<CuteQPlatformTextureListCall2>(taken[2]);
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
      CuteQPlatformTextureListCall3 call = reinterpret_cast<CuteQPlatformTextureListCall3>(taken[3]);
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
      CuteQPlatformTextureListCall4 call = reinterpret_cast<CuteQPlatformTextureListCall4>(taken[4]);
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
      CuteQPlatformTextureListCall5 call = reinterpret_cast<CuteQPlatformTextureListCall5>(taken[5]);
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
      CuteQPlatformTextureListCall6 call = reinterpret_cast<CuteQPlatformTextureListCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformTextureList::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QPlatformTextureList10metaObjectEv(
    const QPlatformTextureList *self) {
  return self->metaObject();
}

//  QString QPlatformTextureList::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QPlatformTextureList2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformTextureList::tr(s, c, n));
}

//  QPlatformTextureList::QPlatformTextureList(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformTextureList *ritual_ZN20QPlatformTextureListC1EP7QObject(
    QObject *parent) {
  return new CuteQPlatformTextureList(parent);
}

//  QPlatformTextureList::~QPlatformTextureList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformTextureListD1Ev(QPlatformTextureList *self) {
  delete self;
}

//  int QPlatformTextureList::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlatformTextureList5countEv(
    const QPlatformTextureList *self) {
  return self->count();
}

//  bool QPlatformTextureList::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformTextureList7isEmptyEv(
    const QPlatformTextureList *self) {
  return self->isEmpty();
}

//  QRhiTexture *QPlatformTextureList::texture(int index) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK20QPlatformTextureList7textureEi(
    const QPlatformTextureList *self,
    int index) {
  return self->texture(index);
}

//  QRhiTexture *QPlatformTextureList::textureExtra(int index) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK20QPlatformTextureList12textureExtraEi(
    const QPlatformTextureList *self,
    int index) {
  return self->textureExtra(index);
}

//  QRect QPlatformTextureList::geometry(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QPlatformTextureList8geometryEi(
    const QPlatformTextureList *self,
    int index) {
  return new QRect(self->geometry(index));
}

//  QRect QPlatformTextureList::clipRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QPlatformTextureList8clipRectEi(
    const QPlatformTextureList *self,
    int index) {
  return new QRect(self->clipRect(index));
}

//  Flags QPlatformTextureList::flags(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlatformTextureList5flagsEi(
    const QPlatformTextureList *self,
    int index) {
  return static_cast<int>(self->flags(index).toInt());
}

//  void QPlatformTextureList::lock(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformTextureList4lockEb(
    QPlatformTextureList *self,
    bool on) {
  self->lock(on);
}

//  bool QPlatformTextureList::isLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformTextureList8isLockedEv(
    const QPlatformTextureList *self) {
  return self->isLocked();
}

//  void QPlatformTextureList::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformTextureList5clearEv(QPlatformTextureList *self) {
  self->clear();
}

//  a Python function taken by a CuteQPlatformTextureList, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformTextureList(
    QPlatformTextureList *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformTextureList *>(self)->take(key, call);
}
