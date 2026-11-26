//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcustommaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcustommaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DCustomMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DCustomMaterial : QQuick3DCustomMaterial {
  using QQuick3DCustomMaterial::updateSpatialNode;
  using QQuick3DCustomMaterial::itemChange;
  using QQuick3DCustomMaterial::markAllDirty;
};

//  A QQuick3DCustomMaterial that Python can take functions over in. Every QQuick3DCustomMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DCustomMaterialCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DCustomMaterialCall1)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DCustomMaterialCall2)(const void *, int *);
typedef void (*CuteQQuick3DCustomMaterialCall3)(const void *, int *);
typedef void (*CuteQQuick3DCustomMaterialCall4)(const void *, int *);
typedef void (*CuteQQuick3DCustomMaterialCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DCustomMaterialCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DCustomMaterialCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCustomMaterialCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCustomMaterialCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCustomMaterialCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCustomMaterialCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DCustomMaterialCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DCustomMaterial : public QQuick3DCustomMaterial {
public:
  using QQuick3DCustomMaterial::QQuick3DCustomMaterial;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DCustomMaterial::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall0 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DCustomMaterial::updateSpatialNode(node);
  }

  //  void QQuick3DCustomMaterial::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall1 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall1>(taken[1]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DCustomMaterial::itemChange(a0, a1);
  }

  //  void QQuick3DCustomMaterial::markAllDirty()
  void markAllDirty() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall2 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DCustomMaterial::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall3 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall4 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall5 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall6 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall7 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall8 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall9 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall10 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall11 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DCustomMaterialCall12 call = reinterpret_cast<CuteQQuick3DCustomMaterialCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DCustomMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DCustomMaterial10metaObjectEv(
    const QQuick3DCustomMaterial *self) {
  return self->metaObject();
}

//  void *QQuick3DCustomMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DCustomMaterial11qt_metacastEPKc(
    QQuick3DCustomMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DCustomMaterial::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DCustomMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DCustomMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DCustomMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DCustomMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DCustomMaterial::tr(s, c, n));
}

//  QQuick3DCustomMaterial::QQuick3DCustomMaterial(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial *ritual_ZN22QQuick3DCustomMaterialC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DCustomMaterial(parent);
}

//  QQuick3DCustomMaterial::~QQuick3DCustomMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterialD1Ev(QQuick3DCustomMaterial *self) {
  delete self;
}

//  ShadingMode QQuick3DCustomMaterial::shadingMode() const
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial::ShadingMode ritual_ZNK22QQuick3DCustomMaterial11shadingModeEv(
    const QQuick3DCustomMaterial *self) {
  return self->shadingMode();
}

//  QUrl QQuick3DCustomMaterial::vertexShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuick3DCustomMaterial12vertexShaderEv(
    const QQuick3DCustomMaterial *self) {
  return new QUrl(self->vertexShader());
}

//  QUrl QQuick3DCustomMaterial::fragmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuick3DCustomMaterial14fragmentShaderEv(
    const QQuick3DCustomMaterial *self) {
  return new QUrl(self->fragmentShader());
}

//  QString QQuick3DCustomMaterial::vertexShaderCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuick3DCustomMaterial16vertexShaderCodeEv(
    const QQuick3DCustomMaterial *self) {
  return new QString(self->vertexShaderCode());
}

//  QString QQuick3DCustomMaterial::fragmentShaderCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuick3DCustomMaterial18fragmentShaderCodeEv(
    const QQuick3DCustomMaterial *self) {
  return new QString(self->fragmentShaderCode());
}

//  BlendMode QQuick3DCustomMaterial::srcBlend() const
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial::BlendMode ritual_ZNK22QQuick3DCustomMaterial8srcBlendEv(
    const QQuick3DCustomMaterial *self) {
  return self->srcBlend();
}

//  BlendMode QQuick3DCustomMaterial::dstBlend() const
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial::BlendMode ritual_ZNK22QQuick3DCustomMaterial8dstBlendEv(
    const QQuick3DCustomMaterial *self) {
  return self->dstBlend();
}

//  BlendMode QQuick3DCustomMaterial::srcAlphaBlend() const
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial::BlendMode ritual_ZNK22QQuick3DCustomMaterial13srcAlphaBlendEv(
    const QQuick3DCustomMaterial *self) {
  return self->srcAlphaBlend();
}

//  BlendMode QQuick3DCustomMaterial::dstAlphaBlend() const
extern "C" Q_DECL_EXPORT
QQuick3DCustomMaterial::BlendMode ritual_ZNK22QQuick3DCustomMaterial13dstAlphaBlendEv(
    const QQuick3DCustomMaterial *self) {
  return self->dstAlphaBlend();
}

//  bool QQuick3DCustomMaterial::alwaysDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DCustomMaterial11alwaysDirtyEv(
    const QQuick3DCustomMaterial *self) {
  return self->alwaysDirty();
}

//  float QQuick3DCustomMaterial::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QQuick3DCustomMaterial9lineWidthEv(
    const QQuick3DCustomMaterial *self) {
  return self->lineWidth();
}

//  void QQuick3DCustomMaterial::setShadingMode(QQuick3DCustomMaterial::Shadi
//      ngMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial14setShadingModeENS_11ShadingModeE(
    QQuick3DCustomMaterial *self,
    QQuick3DCustomMaterial::ShadingMode mode) {
  self->setShadingMode(mode);
}

//  void QQuick3DCustomMaterial::setVertexShader(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial15setVertexShaderERK4QUrl(
    QQuick3DCustomMaterial *self,
    const QUrl *url) {
  self->setVertexShader(*url);
}

//  void QQuick3DCustomMaterial::setFragmentShader(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial17setFragmentShaderERK4QUrl(
    QQuick3DCustomMaterial *self,
    const QUrl *url) {
  self->setFragmentShader(*url);
}

//  void QQuick3DCustomMaterial::setVertexShaderCode(const QString &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial19setVertexShaderCodeERK7QString(
    QQuick3DCustomMaterial *self,
    const QString *code) {
  self->setVertexShaderCode(*code);
}

//  void QQuick3DCustomMaterial::setFragmentShaderCode(const QString &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial21setFragmentShaderCodeERK7QString(
    QQuick3DCustomMaterial *self,
    const QString *code) {
  self->setFragmentShaderCode(*code);
}

//  void
//      QQuick3DCustomMaterial::setSrcBlend(QQuick3DCustomMaterial::BlendMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial11setSrcBlendENS_9BlendModeE(
    QQuick3DCustomMaterial *self,
    QQuick3DCustomMaterial::BlendMode mode) {
  self->setSrcBlend(mode);
}

//  void
//      QQuick3DCustomMaterial::setDstBlend(QQuick3DCustomMaterial::BlendMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial11setDstBlendENS_9BlendModeE(
    QQuick3DCustomMaterial *self,
    QQuick3DCustomMaterial::BlendMode mode) {
  self->setDstBlend(mode);
}

//  void QQuick3DCustomMaterial::setSrcAlphaBlend(QQuick3DCustomMaterial::Ble
//      ndMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial16setSrcAlphaBlendENS_9BlendModeE(
    QQuick3DCustomMaterial *self,
    QQuick3DCustomMaterial::BlendMode mode) {
  self->setSrcAlphaBlend(mode);
}

//  void QQuick3DCustomMaterial::setDstAlphaBlend(QQuick3DCustomMaterial::Ble
//      ndMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial16setDstAlphaBlendENS_9BlendModeE(
    QQuick3DCustomMaterial *self,
    QQuick3DCustomMaterial::BlendMode mode) {
  self->setDstAlphaBlend(mode);
}

//  void QQuick3DCustomMaterial::setAlwaysDirty(bool alwaysDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial14setAlwaysDirtyEb(
    QQuick3DCustomMaterial *self,
    bool alwaysDirty) {
  self->setAlwaysDirty(alwaysDirty);
}

//  void QQuick3DCustomMaterial::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial12setLineWidthEf(
    QQuick3DCustomMaterial *self,
    float width) {
  self->setLineWidth(width);
}

//  void QQuick3DCustomMaterial::shadingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial18shadingModeChangedEv(
    QQuick3DCustomMaterial *self) {
  self->shadingModeChanged();
}

//  void QQuick3DCustomMaterial::vertexShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial19vertexShaderChangedEv(
    QQuick3DCustomMaterial *self) {
  self->vertexShaderChanged();
}

//  void QQuick3DCustomMaterial::fragmentShaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial21fragmentShaderChangedEv(
    QQuick3DCustomMaterial *self) {
  self->fragmentShaderChanged();
}

//  void QQuick3DCustomMaterial::vertexShaderCodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial23vertexShaderCodeChangedEv(
    QQuick3DCustomMaterial *self) {
  self->vertexShaderCodeChanged();
}

//  void QQuick3DCustomMaterial::fragmentShaderCodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial25fragmentShaderCodeChangedEv(
    QQuick3DCustomMaterial *self) {
  self->fragmentShaderCodeChanged();
}

//  void QQuick3DCustomMaterial::srcBlendChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial15srcBlendChangedEv(
    QQuick3DCustomMaterial *self) {
  self->srcBlendChanged();
}

//  void QQuick3DCustomMaterial::dstBlendChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial15dstBlendChangedEv(
    QQuick3DCustomMaterial *self) {
  self->dstBlendChanged();
}

//  void QQuick3DCustomMaterial::srcAlphaBlendChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial20srcAlphaBlendChangedEv(
    QQuick3DCustomMaterial *self) {
  self->srcAlphaBlendChanged();
}

//  void QQuick3DCustomMaterial::dstAlphaBlendChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial20dstAlphaBlendChangedEv(
    QQuick3DCustomMaterial *self) {
  self->dstAlphaBlendChanged();
}

//  void QQuick3DCustomMaterial::alwaysDirtyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial18alwaysDirtyChangedEv(
    QQuick3DCustomMaterial *self) {
  self->alwaysDirtyChanged();
}

//  void QQuick3DCustomMaterial::lineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial16lineWidthChangedEv(
    QQuick3DCustomMaterial *self) {
  self->lineWidthChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DCustomMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN22QQuick3DCustomMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCustomMaterial *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DCustomMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DCustomMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DCustomMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial12markAllDirtyEv(
    QQuick3DCustomMaterial *self) {
  self->markAllDirty();
}

//  void QQuick3DCustomMaterial::markDirty(QQuick3DCustomMaterial &that,
//      QQuick3DCustomMaterial::Dirty type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial9markDirtyERS_NS_5DirtyE(
    QQuick3DCustomMaterial *that,
    QQuick3DCustomMaterial::Dirty type) {
  QQuick3DCustomMaterial::markDirty(*that, type);
}

//  void QQuick3DCustomMaterial::onPropertyDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial15onPropertyDirtyEv(
    QQuick3DCustomMaterial *self) {
  self->onPropertyDirty();
}

//  void QQuick3DCustomMaterial::onTextureDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial14onTextureDirtyEv(
    QQuick3DCustomMaterial *self) {
  self->onTextureDirty();
}

//  void QQuick3DCustomMaterial::setDynamicTextureMap(QQuick3DShaderUtilsText
//      ureInput *textureMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DCustomMaterial20setDynamicTextureMapEP31QQuick3DShaderUtilsTextureInput(
    QQuick3DCustomMaterial *self,
    QQuick3DShaderUtilsTextureInput *textureMap) {
  self->setDynamicTextureMap(textureMap);
}

//  a Python function taken by a CuteQQuick3DCustomMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DCustomMaterial(
    QQuick3DCustomMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DCustomMaterial *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DCustomMaterial::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN22QQuick3DCustomMaterial17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DCustomMaterial *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DCustomMaterial *>(self)->OwnQQuick3DCustomMaterial::updateSpatialNode(
      node);
}

//  void QQuick3DCustomMaterial::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DCustomMaterial10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DCustomMaterial *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DCustomMaterial *>(self)->OwnQQuick3DCustomMaterial::itemChange(
      a0,
      *a1);
}

//  void QQuick3DCustomMaterial::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DCustomMaterial12markAllDirtyEv(
    QQuick3DCustomMaterial *self) {
  static_cast<OwnQQuick3DCustomMaterial *>(self)->OwnQQuick3DCustomMaterial::markAllDirty();
}
