//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qtexturematerial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qtexturematerial.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtGui/QMatrix3x3>

//  A Qt3DExtras::QTextureMaterial that Python can take functions over in. Every Qt3DExtras::QTextureMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTextureMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTextureMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QTextureMaterial : public Qt3DExtras::QTextureMaterial {
public:
  using Qt3DExtras::QTextureMaterial::QTextureMaterial;
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
      CuteQt3DExtras_QTextureMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QTextureMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QTextureMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QTextureMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QTextureMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QTextureMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QTextureMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QTextureMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras16QTextureMaterial10metaObjectEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QTextureMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras16QTextureMaterial11qt_metacastEPKc(
    Qt3DExtras::QTextureMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QTextureMaterial::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras16QTextureMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QTextureMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QTextureMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras16QTextureMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QTextureMaterial::tr(s, c, n));
}

//  Qt3DExtras::QTextureMaterial::QTextureMaterial(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureMaterial *ritual_ZN10Qt3DExtras16QTextureMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QTextureMaterial(parent);
}

//  Qt3DExtras::QTextureMaterial::~QTextureMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterialD1Ev(
    Qt3DExtras::QTextureMaterial *self) {
  delete self;
}

//  Qt3DRender::QAbstractTexture *Qt3DExtras::QTextureMaterial::texture()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DExtras16QTextureMaterial7textureEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return self->texture();
}

//  QVector2D Qt3DExtras::QTextureMaterial::textureOffset() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK10Qt3DExtras16QTextureMaterial13textureOffsetEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return new QVector2D(self->textureOffset());
}

//  QMatrix3x3 Qt3DExtras::QTextureMaterial::textureTransform() const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK10Qt3DExtras16QTextureMaterial16textureTransformEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return new QMatrix3x3(self->textureTransform());
}

//  bool Qt3DExtras::QTextureMaterial::isAlphaBlendingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras16QTextureMaterial22isAlphaBlendingEnabledEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return self->isAlphaBlendingEnabled();
}

//  void
//      Qt3DExtras::QTextureMaterial::setTexture(Qt3DRender::QAbstractTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial10setTextureEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QTextureMaterial *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->setTexture(texture);
}

//  void Qt3DExtras::QTextureMaterial::setTextureOffset(QVector2D
//      textureOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial16setTextureOffsetE9QVector2D(
    Qt3DExtras::QTextureMaterial *self,
    const QVector2D *textureOffset) {
  self->setTextureOffset(*textureOffset);
}

//  void Qt3DExtras::QTextureMaterial::setTextureTransform(const QMatrix3x3
//      &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial19setTextureTransformERK14QGenericMatrixILi3ELi3EfE(
    Qt3DExtras::QTextureMaterial *self,
    const QMatrix3x3 *matrix) {
  self->setTextureTransform(*matrix);
}

//  void Qt3DExtras::QTextureMaterial::setAlphaBlendingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial23setAlphaBlendingEnabledEb(
    Qt3DExtras::QTextureMaterial *self,
    bool enabled) {
  self->setAlphaBlendingEnabled(enabled);
}

//  void
//      Qt3DExtras::QTextureMaterial::textureChanged(Qt3DRender::QAbstractTex
//      ture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial14textureChangedEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QTextureMaterial *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->textureChanged(texture);
}

//  void Qt3DExtras::QTextureMaterial::textureOffsetChanged(QVector2D
//      textureOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial20textureOffsetChangedE9QVector2D(
    Qt3DExtras::QTextureMaterial *self,
    const QVector2D *textureOffset) {
  self->textureOffsetChanged(*textureOffset);
}

//  void Qt3DExtras::QTextureMaterial::textureTransformChanged(const
//      QMatrix3x3 &textureTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial23textureTransformChangedERK14QGenericMatrixILi3ELi3EfE(
    Qt3DExtras::QTextureMaterial *self,
    const QMatrix3x3 *textureTransform) {
  self->textureTransformChanged(*textureTransform);
}

//  void Qt3DExtras::QTextureMaterial::alphaBlendingEnabledChanged(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QTextureMaterial27alphaBlendingEnabledChangedEb(
    Qt3DExtras::QTextureMaterial *self,
    bool enabled) {
  self->alphaBlendingEnabledChanged(enabled);
}

//  QTextureMaterialPrivate *Qt3DExtras::QTextureMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureMaterialPrivate *ritual_ZN10Qt3DExtras16QTextureMaterial6d_funcEv(
    Qt3DExtras::QTextureMaterial *self) {
  return self->d_func();
}

//  const QTextureMaterialPrivate *Qt3DExtras::QTextureMaterial::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTextureMaterialPrivate *ritual_ZNK10Qt3DExtras16QTextureMaterial6d_funcEv(
    const Qt3DExtras::QTextureMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QTextureMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureMaterial(
    Qt3DExtras::QTextureMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureMaterial *>(self)->take(key, call);
}

//  a QMatrix3x3 a ritual of Qt3DExtras::QTextureMaterial gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_QTextureMaterial__QMatrix3x3(QMatrix3x3 *self) {
  delete self;
}
