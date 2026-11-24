//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DRandomInstancing that Python can take functions over in. Every QQuick3DRandomInstancing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DRandomInstancingCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DRandomInstancingCall1)(const void *, int *);
typedef void (*CuteQQuick3DRandomInstancingCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DRandomInstancingCall3)(const void *, int *);
typedef void (*CuteQQuick3DRandomInstancingCall4)(const void *, int *);
typedef void (*CuteQQuick3DRandomInstancingCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRandomInstancingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DRandomInstancingCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRandomInstancingCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRandomInstancingCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRandomInstancingCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRandomInstancingCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DRandomInstancingCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DRandomInstancing : public QQuick3DRandomInstancing {
public:
  using QQuick3DRandomInstancing::QQuick3DRandomInstancing;
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
  //      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall0 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstancing::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall1 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall2 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall3 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall4 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DRandomInstancingCall5 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall5>(taken[5]);
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
      CuteQQuick3DRandomInstancingCall6 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall6>(taken[6]);
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
      CuteQQuick3DRandomInstancingCall7 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall7>(taken[7]);
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
      CuteQQuick3DRandomInstancingCall8 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall8>(taken[8]);
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
      CuteQQuick3DRandomInstancingCall9 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall9>(taken[9]);
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
      CuteQQuick3DRandomInstancingCall10 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall10>(taken[10]);
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
      CuteQQuick3DRandomInstancingCall11 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall11>(taken[11]);
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
      CuteQQuick3DRandomInstancingCall12 call = reinterpret_cast<CuteQQuick3DRandomInstancingCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DRandomInstancing::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DRandomInstancing10metaObjectEv(
    const QQuick3DRandomInstancing *self) {
  return self->metaObject();
}

//  QString QQuick3DRandomInstancing::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DRandomInstancing2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRandomInstancing::tr(s, c, n));
}

//  QQuick3DRandomInstancing::QQuick3DRandomInstancing(QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRandomInstancing *ritual_ZN24QQuick3DRandomInstancingC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DRandomInstancing(parent);
}

//  QQuick3DRandomInstancing::~QQuick3DRandomInstancing()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancingD1Ev(
    QQuick3DRandomInstancing *self) {
  delete self;
}

//  QByteArray QQuick3DRandomInstancing::getInstanceBuffer(int
//      *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QQuick3DRandomInstancing17getInstanceBufferEPi(
    QQuick3DRandomInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

//  int QQuick3DRandomInstancing::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuick3DRandomInstancing13instanceCountEv(
    const QQuick3DRandomInstancing *self) {
  return self->instanceCount();
}

//  int QQuick3DRandomInstancing::randomSeed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuick3DRandomInstancing10randomSeedEv(
    const QQuick3DRandomInstancing *self) {
  return self->randomSeed();
}

//  QQuick3DInstanceRange *QQuick3DRandomInstancing::position() const
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZNK24QQuick3DRandomInstancing8positionEv(
    const QQuick3DRandomInstancing *self) {
  return self->position();
}

//  QQuick3DInstanceRange *QQuick3DRandomInstancing::scale() const
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZNK24QQuick3DRandomInstancing5scaleEv(
    const QQuick3DRandomInstancing *self) {
  return self->scale();
}

//  QQuick3DInstanceRange *QQuick3DRandomInstancing::rotation() const
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZNK24QQuick3DRandomInstancing8rotationEv(
    const QQuick3DRandomInstancing *self) {
  return self->rotation();
}

//  QQuick3DInstanceRange *QQuick3DRandomInstancing::color() const
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZNK24QQuick3DRandomInstancing5colorEv(
    const QQuick3DRandomInstancing *self) {
  return self->color();
}

//  QQuick3DInstanceRange *QQuick3DRandomInstancing::customData() const
extern "C" Q_DECL_EXPORT
QQuick3DInstanceRange *ritual_ZNK24QQuick3DRandomInstancing10customDataEv(
    const QQuick3DRandomInstancing *self) {
  return self->customData();
}

//  ColorModel QQuick3DRandomInstancing::colorModel() const
extern "C" Q_DECL_EXPORT
QQuick3DRandomInstancing::ColorModel ritual_ZNK24QQuick3DRandomInstancing10colorModelEv(
    const QQuick3DRandomInstancing *self) {
  return self->colorModel();
}

//  QVector3D QQuick3DRandomInstancing::gridSpacing() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK24QQuick3DRandomInstancing11gridSpacingEv(
    const QQuick3DRandomInstancing *self) {
  return new QVector3D(self->gridSpacing());
}

//  void QQuick3DRandomInstancing::setGridSpacing(const QVector3D
//      &newGridSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing14setGridSpacingERK9QVector3D(
    QQuick3DRandomInstancing *self,
    const QVector3D *newGridSpacing) {
  self->setGridSpacing(*newGridSpacing);
}

//  void QQuick3DRandomInstancing::setInstanceCount(int instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing16setInstanceCountEi(
    QQuick3DRandomInstancing *self,
    int instanceCount) {
  self->setInstanceCount(instanceCount);
}

//  void QQuick3DRandomInstancing::setRandomSeed(int randomSeed)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing13setRandomSeedEi(
    QQuick3DRandomInstancing *self,
    int randomSeed) {
  self->setRandomSeed(randomSeed);
}

//  void QQuick3DRandomInstancing::setPosition(QQuick3DInstanceRange
//      *position)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing11setPositionEP21QQuick3DInstanceRange(
    QQuick3DRandomInstancing *self,
    QQuick3DInstanceRange *position) {
  self->setPosition(position);
}

//  void QQuick3DRandomInstancing::setScale(QQuick3DInstanceRange *scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing8setScaleEP21QQuick3DInstanceRange(
    QQuick3DRandomInstancing *self,
    QQuick3DInstanceRange *scale) {
  self->setScale(scale);
}

//  void QQuick3DRandomInstancing::setRotation(QQuick3DInstanceRange
//      *rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing11setRotationEP21QQuick3DInstanceRange(
    QQuick3DRandomInstancing *self,
    QQuick3DInstanceRange *rotation) {
  self->setRotation(rotation);
}

//  void QQuick3DRandomInstancing::setColor(QQuick3DInstanceRange *color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing8setColorEP21QQuick3DInstanceRange(
    QQuick3DRandomInstancing *self,
    QQuick3DInstanceRange *color) {
  self->setColor(color);
}

//  void QQuick3DRandomInstancing::setCustomData(QQuick3DInstanceRange
//      *customData)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing13setCustomDataEP21QQuick3DInstanceRange(
    QQuick3DRandomInstancing *self,
    QQuick3DInstanceRange *customData) {
  self->setCustomData(customData);
}

//  void QQuick3DRandomInstancing::setColorModel(ColorModel colorModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing13setColorModelENS_10ColorModelE(
    QQuick3DRandomInstancing *self,
    QQuick3DRandomInstancing::ColorModel colorModel) {
  self->setColorModel(colorModel);
}

//  void QQuick3DRandomInstancing::handleChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing12handleChangeEv(
    QQuick3DRandomInstancing *self) {
  self->handleChange();
}

//  void QQuick3DRandomInstancing::generateInstanceTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DRandomInstancing21generateInstanceTableEv(
    QQuick3DRandomInstancing *self) {
  self->generateInstanceTable();
}

//  a Python function taken by a CuteQQuick3DRandomInstancing, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DRandomInstancing(
    QQuick3DRandomInstancing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DRandomInstancing *>(self)->take(key, call);
}
