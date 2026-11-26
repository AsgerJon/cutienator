//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/qtext2dmaterial_p_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qblendequation.h>
#include <Qt3DRender/qblendequationarguments.h>
#include <Qt3DRender/qdepthtest.h>
#include <Qt3DRender/qabstracttexture.h>
#include <QtCore/QUrl>
#include <QtGui/QVector3D>
#include <QtGui/QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 135, as _ZN10Qt3DExtras15QText2DMaterialD1Ev
namespace Qt3DExtras {
inline QText2DMaterial::~QText2DMaterial()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 139, as _ZN10Qt3DExtras15QText2DMaterial8setColorERK6QColor
namespace Qt3DExtras {
inline void QText2DMaterial::setColor(const QColor &color)
{
    Q_D(QText2DMaterial);
    d->m_colorParameter->setValue(QVariant::fromValue(color));
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 145, as _ZN10Qt3DExtras15QText2DMaterial23setDistanceFieldTextureEPN10Qt3DRender16QAbstractTextureE
namespace Qt3DExtras {
inline void QText2DMaterial::setDistanceFieldTexture(Qt3DRender::QAbstractTexture *tex)
{
    Q_D(QText2DMaterial);
    d->m_distanceFieldTexture = tex;

    if (tex) {
        d->m_textureParameter->setValue(QVariant::fromValue(tex));
        d->m_textureSizeParameter->setValue(QVariant::fromValue(static_cast<float>(tex->width())));
    } else {
        d->m_textureParameter->setValue(0);
        d->m_textureSizeParameter->setValue(QVariant::fromValue(1.f));
    }
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QText2DMaterial that Python can take functions over in. Every Qt3DExtras::QText2DMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QText2DMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QText2DMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QText2DMaterial : public Qt3DExtras::QText2DMaterial {
public:
  using Qt3DExtras::QText2DMaterial::QText2DMaterial;
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
      CuteQt3DExtras_QText2DMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QText2DMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QText2DMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QText2DMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QText2DMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QText2DMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QText2DMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QText2DMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QText2DMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras15QText2DMaterial10metaObjectEv(
    const Qt3DExtras::QText2DMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QText2DMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras15QText2DMaterial11qt_metacastEPKc(
    Qt3DExtras::QText2DMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QText2DMaterial::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras15QText2DMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QText2DMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DExtras::QText2DMaterial::~QText2DMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QText2DMaterialD1Ev(
    Qt3DExtras::QText2DMaterial *self) {
  delete self;
}

//  void Qt3DExtras::QText2DMaterial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QText2DMaterial8setColorERK6QColor(
    Qt3DExtras::QText2DMaterial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void Qt3DExtras::QText2DMaterial::setDistanceFieldTexture(Qt3DRender::QAb
//      stractTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras15QText2DMaterial23setDistanceFieldTextureEPN10Qt3DRender16QAbstractTextureE(
    Qt3DExtras::QText2DMaterial *self,
    Qt3DRender::QAbstractTexture *tex) {
  self->setDistanceFieldTexture(tex);
}

//  QText2DMaterialPrivate *Qt3DExtras::QText2DMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QText2DMaterialPrivate *ritual_ZN10Qt3DExtras15QText2DMaterial6d_funcEv(
    Qt3DExtras::QText2DMaterial *self) {
  return self->d_func();
}

//  const QText2DMaterialPrivate *Qt3DExtras::QText2DMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QText2DMaterialPrivate *ritual_ZNK10Qt3DExtras15QText2DMaterial6d_funcEv(
    const Qt3DExtras::QText2DMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QText2DMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QText2DMaterial(
    Qt3DExtras::QText2DMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QText2DMaterial *>(self)->take(key, call);
}
