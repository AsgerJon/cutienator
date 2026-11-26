//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qphongalphamaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qphongalphamaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QPhongAlphaMaterial that Python can take functions over in. Every Qt3DExtras::QPhongAlphaMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPhongAlphaMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPhongAlphaMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QPhongAlphaMaterial : public Qt3DExtras::QPhongAlphaMaterial {
public:
  using Qt3DExtras::QPhongAlphaMaterial::QPhongAlphaMaterial;
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
      CuteQt3DExtras_QPhongAlphaMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QPhongAlphaMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QPhongAlphaMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial10metaObjectEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QPhongAlphaMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras19QPhongAlphaMaterial11qt_metacastEPKc(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QPhongAlphaMaterial::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras19QPhongAlphaMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QPhongAlphaMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QPhongAlphaMaterial::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras19QPhongAlphaMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QPhongAlphaMaterial::tr(s, c, n));
}

//  Qt3DExtras::QPhongAlphaMaterial::QPhongAlphaMaterial(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongAlphaMaterial *ritual_ZN10Qt3DExtras19QPhongAlphaMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QPhongAlphaMaterial(parent);
}

//  Qt3DExtras::QPhongAlphaMaterial::~QPhongAlphaMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterialD1Ev(
    Qt3DExtras::QPhongAlphaMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QPhongAlphaMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial7ambientEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return new QColor(self->ambient());
}

//  QColor Qt3DExtras::QPhongAlphaMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial7diffuseEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return new QColor(self->diffuse());
}

//  QColor Qt3DExtras::QPhongAlphaMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial8specularEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return new QColor(self->specular());
}

//  float Qt3DExtras::QPhongAlphaMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial9shininessEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->shininess();
}

//  float Qt3DExtras::QPhongAlphaMaterial::alpha() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial5alphaEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->alpha();
}

//  Qt3DRender::QBlendEquationArguments::Blending
//      Qt3DExtras::QPhongAlphaMaterial::sourceRgbArg() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial12sourceRgbArgEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->sourceRgbArg();
}

//  Qt3DRender::QBlendEquationArguments::Blending
//      Qt3DExtras::QPhongAlphaMaterial::destinationRgbArg() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial17destinationRgbArgEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->destinationRgbArg();
}

//  Qt3DRender::QBlendEquationArguments::Blending
//      Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArg() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial14sourceAlphaArgEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->sourceAlphaArg();
}

//  Qt3DRender::QBlendEquationArguments::Blending
//      Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArg() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial19destinationAlphaArgEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->destinationAlphaArg();
}

//  Qt3DRender::QBlendEquation::BlendFunction
//      Qt3DExtras::QPhongAlphaMaterial::blendFunctionArg() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquation::BlendFunction ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial16blendFunctionArgEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->blendFunctionArg();
}

//  void Qt3DExtras::QPhongAlphaMaterial::setAmbient(const QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial10setAmbientERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setDiffuse(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial10setDiffuseERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *diffuse) {
  self->setDiffuse(*diffuse);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setSpecular(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial11setSpecularERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial12setShininessEf(
    Qt3DExtras::QPhongAlphaMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setAlpha(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial8setAlphaEf(
    Qt3DExtras::QPhongAlphaMaterial *self,
    float alpha) {
  self->setAlpha(alpha);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setSourceRgbArg(Qt3DRender::QBlendE
//      quationArguments::Blending sourceRgbArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial15setSourceRgbArgEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgbArg) {
  self->setSourceRgbArg(sourceRgbArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setDestinationRgbArg(Qt3DRender::QB
//      lendEquationArguments::Blending destinationRgbArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial20setDestinationRgbArgEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgbArg) {
  self->setDestinationRgbArg(destinationRgbArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setSourceAlphaArg(Qt3DRender::QBlen
//      dEquationArguments::Blending sourceAlphaArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial17setSourceAlphaArgEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceAlphaArg) {
  self->setSourceAlphaArg(sourceAlphaArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setDestinationAlphaArg(Qt3DRender::
//      QBlendEquationArguments::Blending destinationAlphaArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial22setDestinationAlphaArgEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationAlphaArg) {
  self->setDestinationAlphaArg(destinationAlphaArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::setBlendFunctionArg(Qt3DRender::QBl
//      endEquation::BlendFunction blendFunctionArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial19setBlendFunctionArgEN10Qt3DRender14QBlendEquation13BlendFunctionE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquation::BlendFunction blendFunctionArg) {
  self->setBlendFunctionArg(blendFunctionArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::ambientChanged(const QColor
//      &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QPhongAlphaMaterial::diffuseChanged(const QColor
//      &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial14diffuseChangedERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *diffuse) {
  self->diffuseChanged(*diffuse);
}

//  void Qt3DExtras::QPhongAlphaMaterial::specularChanged(const QColor
//      &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial15specularChangedERK6QColor(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QPhongAlphaMaterial::shininessChanged(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial16shininessChangedEf(
    Qt3DExtras::QPhongAlphaMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  void Qt3DExtras::QPhongAlphaMaterial::alphaChanged(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial12alphaChangedEf(
    Qt3DExtras::QPhongAlphaMaterial *self,
    float alpha) {
  self->alphaChanged(alpha);
}

//  void Qt3DExtras::QPhongAlphaMaterial::sourceRgbArgChanged(Qt3DRender::QBl
//      endEquationArguments::Blending sourceRgbArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial19sourceRgbArgChangedEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgbArg) {
  self->sourceRgbArgChanged(sourceRgbArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::destinationRgbArgChanged(Qt3DRender
//      ::QBlendEquationArguments::Blending destinationRgbArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial24destinationRgbArgChangedEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgbArg) {
  self->destinationRgbArgChanged(destinationRgbArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::sourceAlphaArgChanged(Qt3DRender::Q
//      BlendEquationArguments::Blending sourceAlphaArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial21sourceAlphaArgChangedEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceAlphaArg) {
  self->sourceAlphaArgChanged(sourceAlphaArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::destinationAlphaArgChanged(Qt3DRend
//      er::QBlendEquationArguments::Blending destinationAlphaArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial26destinationAlphaArgChangedEN10Qt3DRender23QBlendEquationArguments8BlendingE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationAlphaArg) {
  self->destinationAlphaArgChanged(destinationAlphaArg);
}

//  void Qt3DExtras::QPhongAlphaMaterial::blendFunctionArgChanged(Qt3DRender:
//      :QBlendEquation::BlendFunction blendFunctionArg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras19QPhongAlphaMaterial23blendFunctionArgChangedEN10Qt3DRender14QBlendEquation13BlendFunctionE(
    Qt3DExtras::QPhongAlphaMaterial *self,
    Qt3DRender::QBlendEquation::BlendFunction blendFunctionArg) {
  self->blendFunctionArgChanged(blendFunctionArg);
}

//  QPhongAlphaMaterialPrivate *Qt3DExtras::QPhongAlphaMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongAlphaMaterialPrivate *ritual_ZN10Qt3DExtras19QPhongAlphaMaterial6d_funcEv(
    Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->d_func();
}

//  const QPhongAlphaMaterialPrivate
//      *Qt3DExtras::QPhongAlphaMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPhongAlphaMaterialPrivate *ritual_ZNK10Qt3DExtras19QPhongAlphaMaterial6d_funcEv(
    const Qt3DExtras::QPhongAlphaMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QPhongAlphaMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPhongAlphaMaterial(
    Qt3DExtras::QPhongAlphaMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPhongAlphaMaterial *>(self)->take(key, call);
}
