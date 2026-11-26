//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qspritesheet.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qspritesheet.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DExtras/Qt3DExtras>

//  A Qt3DExtras::QSpriteSheet that Python can take functions over in. Every Qt3DExtras::QSpriteSheet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSpriteSheetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QSpriteSheetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSpriteSheetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSpriteSheetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSpriteSheetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSpriteSheetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QSpriteSheetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QSpriteSheet : public Qt3DExtras::QSpriteSheet {
public:
  using Qt3DExtras::QSpriteSheet::QSpriteSheet;
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
      CuteQt3DExtras_QSpriteSheetCall0 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall0>(taken[0]);
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
      CuteQt3DExtras_QSpriteSheetCall1 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall1>(taken[1]);
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
      CuteQt3DExtras_QSpriteSheetCall2 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall2>(taken[2]);
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
      CuteQt3DExtras_QSpriteSheetCall3 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall3>(taken[3]);
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
      CuteQt3DExtras_QSpriteSheetCall4 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall4>(taken[4]);
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
      CuteQt3DExtras_QSpriteSheetCall5 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall5>(taken[5]);
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
      CuteQt3DExtras_QSpriteSheetCall6 call = reinterpret_cast<CuteQt3DExtras_QSpriteSheetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QSpriteSheet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras12QSpriteSheet10metaObjectEv(
    const Qt3DExtras::QSpriteSheet *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QSpriteSheet::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras12QSpriteSheet11qt_metacastEPKc(
    Qt3DExtras::QSpriteSheet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QSpriteSheet::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras12QSpriteSheet11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QSpriteSheet *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QSpriteSheet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras12QSpriteSheet2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QSpriteSheet::tr(s, c, n));
}

//  Qt3DExtras::QSpriteSheet::QSpriteSheet(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheet *ritual_ZN10Qt3DExtras12QSpriteSheetC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QSpriteSheet(parent);
}

//  Qt3DExtras::QSpriteSheet::~QSpriteSheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras12QSpriteSheetD1Ev(
    Qt3DExtras::QSpriteSheet *self) {
  delete self;
}

//  QList<QSpriteSheetItem *> Qt3DExtras::QSpriteSheet::sprites() const
extern "C" Q_DECL_EXPORT
QList<Qt3DExtras::QSpriteSheetItem *> *ritual_ZNK10Qt3DExtras12QSpriteSheet7spritesEv(
    const Qt3DExtras::QSpriteSheet *self) {
  return new QList<Qt3DExtras::QSpriteSheetItem *>(self->sprites());
}

//  QSpriteSheetItem *Qt3DExtras::QSpriteSheet::addSprite(int x, int y, int
//      width, int height)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheetItem *ritual_ZN10Qt3DExtras12QSpriteSheet9addSpriteEiiii(
    Qt3DExtras::QSpriteSheet *self,
    int x,
    int y,
    int width,
    int height) {
  return self->addSprite(x, y, width, height);
}

//  void Qt3DExtras::QSpriteSheet::addSprite(QSpriteSheetItem *sprite)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras12QSpriteSheet9addSpriteEPNS_16QSpriteSheetItemE(
    Qt3DExtras::QSpriteSheet *self,
    Qt3DExtras::QSpriteSheetItem *sprite) {
  self->addSprite(sprite);
}

//  void Qt3DExtras::QSpriteSheet::removeSprite(QSpriteSheetItem *sprite)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras12QSpriteSheet12removeSpriteEPNS_16QSpriteSheetItemE(
    Qt3DExtras::QSpriteSheet *self,
    Qt3DExtras::QSpriteSheetItem *sprite) {
  self->removeSprite(sprite);
}

//  void Qt3DExtras::QSpriteSheet::setSprites(QList<QSpriteSheetItem *>
//      sprites)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras12QSpriteSheet10setSpritesE5QListIPNS_16QSpriteSheetItemEE(
    Qt3DExtras::QSpriteSheet *self,
    const QList<Qt3DExtras::QSpriteSheetItem *> *sprites) {
  self->setSprites(*sprites);
}

//  void Qt3DExtras::QSpriteSheet::spritesChanged(QList<QSpriteSheetItem *>
//      sprites)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras12QSpriteSheet14spritesChangedE5QListIPNS_16QSpriteSheetItemEE(
    Qt3DExtras::QSpriteSheet *self,
    const QList<Qt3DExtras::QSpriteSheetItem *> *sprites) {
  self->spritesChanged(*sprites);
}

//  QSpriteSheetPrivate *Qt3DExtras::QSpriteSheet::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QSpriteSheetPrivate *ritual_ZN10Qt3DExtras12QSpriteSheet6d_funcEv(
    Qt3DExtras::QSpriteSheet *self) {
  return self->d_func();
}

//  const QSpriteSheetPrivate *Qt3DExtras::QSpriteSheet::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QSpriteSheetPrivate *ritual_ZNK10Qt3DExtras12QSpriteSheet6d_funcEv(
    const Qt3DExtras::QSpriteSheet *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QSpriteSheet, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QSpriteSheet(
    Qt3DExtras::QSpriteSheet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QSpriteSheet *>(self)->take(key, call);
}

//  a QList<Qt3DExtras::QSpriteSheetItem *> a ritual of
//      Qt3DExtras::QSpriteSheet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_QSpriteSheet__QList_Qt3DExtras_QSpriteSheetItem(
    QList<Qt3DExtras::QSpriteSheetItem *> *self) {
  delete self;
}
