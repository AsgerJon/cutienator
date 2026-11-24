//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/extrudedtextgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/extrudedtextgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A ExtrudedTextGeometry that Python can take functions over in. Every ExtrudedTextGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteExtrudedTextGeometryCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteExtrudedTextGeometryCall1)(const void *, int *);
typedef void (*CuteExtrudedTextGeometryCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteExtrudedTextGeometryCall3)(const void *, int *);
typedef void (*CuteExtrudedTextGeometryCall4)(const void *, int *);
typedef void (*CuteExtrudedTextGeometryCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteExtrudedTextGeometryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteExtrudedTextGeometryCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteExtrudedTextGeometryCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteExtrudedTextGeometryCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteExtrudedTextGeometryCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteExtrudedTextGeometryCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteExtrudedTextGeometryCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteExtrudedTextGeometry : public ExtrudedTextGeometry {
public:
  using ExtrudedTextGeometry::ExtrudedTextGeometry;
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
  //      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall0 call = reinterpret_cast<CuteExtrudedTextGeometryCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DGeometry::updateSpatialNode(node);
  }

  //  void QQuick3DGeometry::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall1 call = reinterpret_cast<CuteExtrudedTextGeometryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DGeometry::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall2 call = reinterpret_cast<CuteExtrudedTextGeometryCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall3 call = reinterpret_cast<CuteExtrudedTextGeometryCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall4 call = reinterpret_cast<CuteExtrudedTextGeometryCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteExtrudedTextGeometryCall5 call = reinterpret_cast<CuteExtrudedTextGeometryCall5>(taken[5]);
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
      CuteExtrudedTextGeometryCall6 call = reinterpret_cast<CuteExtrudedTextGeometryCall6>(taken[6]);
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
      CuteExtrudedTextGeometryCall7 call = reinterpret_cast<CuteExtrudedTextGeometryCall7>(taken[7]);
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
      CuteExtrudedTextGeometryCall8 call = reinterpret_cast<CuteExtrudedTextGeometryCall8>(taken[8]);
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
      CuteExtrudedTextGeometryCall9 call = reinterpret_cast<CuteExtrudedTextGeometryCall9>(taken[9]);
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
      CuteExtrudedTextGeometryCall10 call = reinterpret_cast<CuteExtrudedTextGeometryCall10>(taken[10]);
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
      CuteExtrudedTextGeometryCall11 call = reinterpret_cast<CuteExtrudedTextGeometryCall11>(taken[11]);
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
      CuteExtrudedTextGeometryCall12 call = reinterpret_cast<CuteExtrudedTextGeometryCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ExtrudedTextGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20ExtrudedTextGeometry10metaObjectEv(
    const ExtrudedTextGeometry *self) {
  return self->metaObject();
}

//  QString ExtrudedTextGeometry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20ExtrudedTextGeometry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ExtrudedTextGeometry::tr(s, c, n));
}

//  ExtrudedTextGeometry::ExtrudedTextGeometry(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
ExtrudedTextGeometry *ritual_ZN20ExtrudedTextGeometryC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteExtrudedTextGeometry(parent);
}

//  ExtrudedTextGeometry::~ExtrudedTextGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometryD1Ev(ExtrudedTextGeometry *self) {
  delete self;
}

//  QString ExtrudedTextGeometry::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20ExtrudedTextGeometry4textEv(
    const ExtrudedTextGeometry *self) {
  return new QString(self->text());
}

//  void ExtrudedTextGeometry::setText(const QString &newText)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry7setTextERK7QString(
    ExtrudedTextGeometry *self,
    const QString *newText) {
  self->setText(*newText);
}

//  QFont ExtrudedTextGeometry::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK20ExtrudedTextGeometry4fontEv(
    const ExtrudedTextGeometry *self) {
  return new QFont(self->font());
}

//  void ExtrudedTextGeometry::setFont(const QFont &newFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry7setFontERK5QFont(
    ExtrudedTextGeometry *self,
    const QFont *newFont) {
  self->setFont(*newFont);
}

//  float ExtrudedTextGeometry::depth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20ExtrudedTextGeometry5depthEv(
    const ExtrudedTextGeometry *self) {
  return self->depth();
}

//  void ExtrudedTextGeometry::setDepth(float newDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry8setDepthEf(
    ExtrudedTextGeometry *self,
    float newDepth) {
  self->setDepth(newDepth);
}

//  float ExtrudedTextGeometry::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20ExtrudedTextGeometry5scaleEv(
    const ExtrudedTextGeometry *self) {
  return self->scale();
}

//  void ExtrudedTextGeometry::setScale(float newScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry8setScaleEf(
    ExtrudedTextGeometry *self,
    float newScale) {
  self->setScale(newScale);
}

//  bool ExtrudedTextGeometry::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20ExtrudedTextGeometry12asynchronousEv(
    const ExtrudedTextGeometry *self) {
  return self->asynchronous();
}

//  void ExtrudedTextGeometry::setAsynchronous(bool newAsynchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry15setAsynchronousEb(
    ExtrudedTextGeometry *self,
    bool newAsynchronous) {
  self->setAsynchronous(newAsynchronous);
}

//  Status ExtrudedTextGeometry::status() const
extern "C" Q_DECL_EXPORT
ExtrudedTextGeometry::Status ritual_ZNK20ExtrudedTextGeometry6statusEv(
    const ExtrudedTextGeometry *self) {
  return self->status();
}

//  void ExtrudedTextGeometry::doUpdateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry16doUpdateGeometryEv(
    ExtrudedTextGeometry *self) {
  self->doUpdateGeometry();
}

//  void ExtrudedTextGeometry::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry15requestFinishedEv(
    ExtrudedTextGeometry *self) {
  self->requestFinished();
}

//  void ExtrudedTextGeometry::scheduleGeometryUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ExtrudedTextGeometry22scheduleGeometryUpdateEv(
    ExtrudedTextGeometry *self) {
  self->scheduleGeometryUpdate();
}

//  a Python function taken by a CuteExtrudedTextGeometry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ExtrudedTextGeometry(
    ExtrudedTextGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteExtrudedTextGeometry *>(self)->take(key, call);
}
