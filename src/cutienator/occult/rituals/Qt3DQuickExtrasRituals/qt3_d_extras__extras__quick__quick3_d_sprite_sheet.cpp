//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dspritesheet_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/qt3dquickextras_global_p.h>
#include <Qt3DQuickExtras/Qt3DQuickExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dspritesheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DExtras/Qt3DExtras>

//  A Qt3DExtras::Extras::Quick::Quick3DSpriteSheet that Python can take functions over in. Every Qt3DExtras::Extras::Quick::Quick3DSpriteSheet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheet : public Qt3DExtras::Extras::Quick::Quick3DSpriteSheet {
public:
  using Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::Quick3DSpriteSheet;
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall0 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall0>(taken[0]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall1 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall1>(taken[1]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall2 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall2>(taken[2]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall3 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall3>(taken[3]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall4 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall4>(taken[4]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall5 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall5>(taken[5]);
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
      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall6 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet10metaObjectEv(
    const Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet11qt_metacastEPKc(
    Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::tr(
          s,
          c,
          n));
}

//  Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::Quick3DSpriteSheet(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheetC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheet(parent);
}

//  Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::~Quick3DSpriteSheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheetD1Ev(
    Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self) {
  delete self;
}

//  QQmlListProperty<Qt3DExtras::QSpriteSheetItem>
//      Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::sprites()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DExtras::QSpriteSheetItem> *ritual_ZN10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet7spritesEv(
    Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self) {
  return new QQmlListProperty<Qt3DExtras::QSpriteSheetItem>(self->sprites());
}

//  QSpriteSheet
//      *Qt3DExtras::Extras::Quick::Quick3DSpriteSheet::parentSpriteSheet()
//      const
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheet *ritual_ZNK10Qt3DExtras6Extras5Quick18Quick3DSpriteSheet17parentSpriteSheetEv(
    const Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self) {
  return self->parentSpriteSheet();
}

//  a Python function taken by a
//      CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheet, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_Extras_Quick_Quick3DSpriteSheet(
    Qt3DExtras::Extras::Quick::Quick3DSpriteSheet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_Extras_Quick_Quick3DSpriteSheet *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DExtras::QSpriteSheetItem> a ritual of
//      Qt3DExtras::Extras::Quick::Quick3DSpriteSheet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_Extras_Quick_Quick3DSpriteSheet__QQmlListProperty_Qt3DExtras_QSpriteSheetItem(
    QQmlListProperty<Qt3DExtras::QSpriteSheetItem> *self) {
  delete self;
}
