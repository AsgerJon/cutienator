//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dreflectionprobe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dreflectionprobe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DReflectionProbe may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DReflectionProbe : QQuick3DReflectionProbe {
  using QQuick3DReflectionProbe::updateSpatialNode;
  using QQuick3DReflectionProbe::markAllDirty;
  using QQuick3DReflectionProbe::itemChange;
};

//  A QQuick3DReflectionProbe that Python can take functions over in. Every QQuick3DReflectionProbe
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DReflectionProbeCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DReflectionProbeCall1)(const void *, int *);
typedef void (*CuteQQuick3DReflectionProbeCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall5)(const void *, int *);
typedef void (*CuteQQuick3DReflectionProbeCall6)(const void *, int *);
typedef void (*CuteQQuick3DReflectionProbeCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DReflectionProbeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DReflectionProbeCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DReflectionProbeCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DReflectionProbe : public QQuick3DReflectionProbe {
public:
  using QQuick3DReflectionProbe::QQuick3DReflectionProbe;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DReflectionProbe::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall0 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DReflectionProbe::updateSpatialNode(node);
  }

  //  void QQuick3DReflectionProbe::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall1 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DReflectionProbe::markAllDirty();
  }

  //  void QQuick3DReflectionProbe::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall2 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DReflectionProbe::itemChange(a0, a1);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall3 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall4 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall5 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall6 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall7 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall8 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall9 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall10 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall11 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DReflectionProbeCall12 call = reinterpret_cast<CuteQQuick3DReflectionProbeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DReflectionProbe::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DReflectionProbe10metaObjectEv(
    const QQuick3DReflectionProbe *self) {
  return self->metaObject();
}

//  void *QQuick3DReflectionProbe::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DReflectionProbe11qt_metacastEPKc(
    QQuick3DReflectionProbe *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DReflectionProbe::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DReflectionProbe11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DReflectionProbe *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DReflectionProbe::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DReflectionProbe2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DReflectionProbe::tr(s, c, n));
}

//  QQuick3DReflectionProbe::QQuick3DReflectionProbe(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DReflectionProbe *ritual_ZN23QQuick3DReflectionProbeC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DReflectionProbe(parent);
}

//  QQuick3DReflectionProbe::~QQuick3DReflectionProbe()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbeD1Ev(QQuick3DReflectionProbe *self) {
  delete self;
}

//  ReflectionQuality QQuick3DReflectionProbe::quality() const
extern "C" Q_DECL_EXPORT
QQuick3DReflectionProbe::ReflectionQuality ritual_ZNK23QQuick3DReflectionProbe7qualityEv(
    const QQuick3DReflectionProbe *self) {
  return self->quality();
}

//  QColor QQuick3DReflectionProbe::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QQuick3DReflectionProbe10clearColorEv(
    const QQuick3DReflectionProbe *self) {
  return new QColor(self->clearColor());
}

//  ReflectionRefreshMode QQuick3DReflectionProbe::refreshMode() const
extern "C" Q_DECL_EXPORT
QQuick3DReflectionProbe::ReflectionRefreshMode ritual_ZNK23QQuick3DReflectionProbe11refreshModeEv(
    const QQuick3DReflectionProbe *self) {
  return self->refreshMode();
}

//  ReflectionTimeSlicing QQuick3DReflectionProbe::timeSlicing() const
extern "C" Q_DECL_EXPORT
QQuick3DReflectionProbe::ReflectionTimeSlicing ritual_ZNK23QQuick3DReflectionProbe11timeSlicingEv(
    const QQuick3DReflectionProbe *self) {
  return self->timeSlicing();
}

//  bool QQuick3DReflectionProbe::parallaxCorrection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DReflectionProbe18parallaxCorrectionEv(
    const QQuick3DReflectionProbe *self) {
  return self->parallaxCorrection();
}

//  QVector3D QQuick3DReflectionProbe::boxSize() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DReflectionProbe7boxSizeEv(
    const QQuick3DReflectionProbe *self) {
  return new QVector3D(self->boxSize());
}

//  bool QQuick3DReflectionProbe::debugView() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DReflectionProbe9debugViewEv(
    const QQuick3DReflectionProbe *self) {
  return self->debugView();
}

//  QVector3D QQuick3DReflectionProbe::boxOffset() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DReflectionProbe9boxOffsetEv(
    const QQuick3DReflectionProbe *self) {
  return new QVector3D(self->boxOffset());
}

//  void QQuick3DReflectionProbe::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14scheduleUpdateEv(
    QQuick3DReflectionProbe *self) {
  self->scheduleUpdate();
}

//  QQuick3DCubeMapTexture *QQuick3DReflectionProbe::texture() const
extern "C" Q_DECL_EXPORT
QQuick3DCubeMapTexture *ritual_ZNK23QQuick3DReflectionProbe7textureEv(
    const QQuick3DReflectionProbe *self) {
  return self->texture();
}

//  void QQuick3DReflectionProbe::setQuality(ReflectionQuality
//      reflectionQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe10setQualityENS_17ReflectionQualityE(
    QQuick3DReflectionProbe *self,
    QQuick3DReflectionProbe::ReflectionQuality reflectionQuality) {
  self->setQuality(reflectionQuality);
}

//  void QQuick3DReflectionProbe::setClearColor(const QColor &clearColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe13setClearColorERK6QColor(
    QQuick3DReflectionProbe *self,
    const QColor *clearColor) {
  self->setClearColor(*clearColor);
}

//  void QQuick3DReflectionProbe::setRefreshMode(ReflectionRefreshMode
//      newRefreshMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14setRefreshModeENS_21ReflectionRefreshModeE(
    QQuick3DReflectionProbe *self,
    QQuick3DReflectionProbe::ReflectionRefreshMode newRefreshMode) {
  self->setRefreshMode(newRefreshMode);
}

//  void QQuick3DReflectionProbe::setTimeSlicing(ReflectionTimeSlicing
//      newTimeSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14setTimeSlicingENS_21ReflectionTimeSlicingE(
    QQuick3DReflectionProbe *self,
    QQuick3DReflectionProbe::ReflectionTimeSlicing newTimeSlicing) {
  self->setTimeSlicing(newTimeSlicing);
}

//  void QQuick3DReflectionProbe::setParallaxCorrection(bool
//      parallaxCorrection)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe21setParallaxCorrectionEb(
    QQuick3DReflectionProbe *self,
    bool parallaxCorrection) {
  self->setParallaxCorrection(parallaxCorrection);
}

//  void QQuick3DReflectionProbe::setBoxSize(const QVector3D &newBoxSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe10setBoxSizeERK9QVector3D(
    QQuick3DReflectionProbe *self,
    const QVector3D *newBoxSize) {
  self->setBoxSize(*newBoxSize);
}

//  void QQuick3DReflectionProbe::setDebugView(bool debugView)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe12setDebugViewEb(
    QQuick3DReflectionProbe *self,
    bool debugView) {
  self->setDebugView(debugView);
}

//  void QQuick3DReflectionProbe::setBoxOffset(const QVector3D &boxOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe12setBoxOffsetERK9QVector3D(
    QQuick3DReflectionProbe *self,
    const QVector3D *boxOffset) {
  self->setBoxOffset(*boxOffset);
}

//  void QQuick3DReflectionProbe::setTexture(QQuick3DCubeMapTexture
//      *newTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe10setTextureEP22QQuick3DCubeMapTexture(
    QQuick3DReflectionProbe *self,
    QQuick3DCubeMapTexture *newTexture) {
  self->setTexture(newTexture);
}

//  void QQuick3DReflectionProbe::qualityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14qualityChangedEv(
    QQuick3DReflectionProbe *self) {
  self->qualityChanged();
}

//  void QQuick3DReflectionProbe::clearColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe17clearColorChangedEv(
    QQuick3DReflectionProbe *self) {
  self->clearColorChanged();
}

//  void QQuick3DReflectionProbe::refreshModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe18refreshModeChangedEv(
    QQuick3DReflectionProbe *self) {
  self->refreshModeChanged();
}

//  void QQuick3DReflectionProbe::timeSlicingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe18timeSlicingChangedEv(
    QQuick3DReflectionProbe *self) {
  self->timeSlicingChanged();
}

//  void QQuick3DReflectionProbe::parallaxCorrectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe25parallaxCorrectionChangedEv(
    QQuick3DReflectionProbe *self) {
  self->parallaxCorrectionChanged();
}

//  void QQuick3DReflectionProbe::boxSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14boxSizeChangedEv(
    QQuick3DReflectionProbe *self) {
  self->boxSizeChanged();
}

//  void QQuick3DReflectionProbe::debugViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe16debugViewChangedEv(
    QQuick3DReflectionProbe *self) {
  self->debugViewChanged();
}

//  void QQuick3DReflectionProbe::boxOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe16boxOffsetChangedEv(
    QQuick3DReflectionProbe *self) {
  self->boxOffsetChanged();
}

//  void QQuick3DReflectionProbe::textureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe14textureChangedEv(
    QQuick3DReflectionProbe *self) {
  self->textureChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DReflectionProbe::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN23QQuick3DReflectionProbe17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DReflectionProbe *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DReflectionProbe::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe12markAllDirtyEv(
    QQuick3DReflectionProbe *self) {
  self->markAllDirty();
}

//  void QQuick3DReflectionProbe::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DReflectionProbe *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  quint32
//      QQuick3DReflectionProbe::mapToReflectionResolution(ReflectionQuality
//      quality)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN23QQuick3DReflectionProbe25mapToReflectionResolutionENS_17ReflectionQualityE(
    QQuick3DReflectionProbe *self,
    QQuick3DReflectionProbe::ReflectionQuality quality) {
  return self->mapToReflectionResolution(quality);
}

//  void QQuick3DReflectionProbe::findSceneView()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe13findSceneViewEv(
    QQuick3DReflectionProbe *self) {
  self->findSceneView();
}

//  void QQuick3DReflectionProbe::createDebugView()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe15createDebugViewEv(
    QQuick3DReflectionProbe *self) {
  self->createDebugView();
}

//  void QQuick3DReflectionProbe::updateDebugView()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe15updateDebugViewEv(
    QQuick3DReflectionProbe *self) {
  self->updateDebugView();
}

//  void QQuick3DReflectionProbe::updateSceneManager(QQuick3DSceneManager
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DReflectionProbe18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DReflectionProbe *self,
    QQuick3DSceneManager *window) {
  self->updateSceneManager(window);
}

//  a Python function taken by a CuteQQuick3DReflectionProbe, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DReflectionProbe(
    QQuick3DReflectionProbe *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DReflectionProbe *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DReflectionProbe::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN23QQuick3DReflectionProbe17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DReflectionProbe *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DReflectionProbe *>(self)->OwnQQuick3DReflectionProbe::updateSpatialNode(
      node);
}

//  void QQuick3DReflectionProbe::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DReflectionProbe12markAllDirtyEv(
    QQuick3DReflectionProbe *self) {
  static_cast<OwnQQuick3DReflectionProbe *>(self)->OwnQQuick3DReflectionProbe::markAllDirty();
}

//  void QQuick3DReflectionProbe::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DReflectionProbe10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DReflectionProbe *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DReflectionProbe *>(self)->OwnQQuick3DReflectionProbe::itemChange(
      a0,
      *a1);
}
