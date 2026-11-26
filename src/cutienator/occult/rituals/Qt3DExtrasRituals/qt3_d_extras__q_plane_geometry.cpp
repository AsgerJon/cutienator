//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qplanegeometry.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qplanegeometry.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QPlaneGeometry that Python can take functions over in. Every Qt3DExtras::QPlaneGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPlaneGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPlaneGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QPlaneGeometry : public Qt3DExtras::QPlaneGeometry {
public:
  using Qt3DExtras::QPlaneGeometry::QPlaneGeometry;
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
      CuteQt3DExtras_QPlaneGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QPlaneGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QPlaneGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QPlaneGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QPlaneGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QPlaneGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QPlaneGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QPlaneGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras14QPlaneGeometry10metaObjectEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QPlaneGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras14QPlaneGeometry11qt_metacastEPKc(
    Qt3DExtras::QPlaneGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QPlaneGeometry::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras14QPlaneGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QPlaneGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QPlaneGeometry::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras14QPlaneGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QPlaneGeometry::tr(s, c, n));
}

//  Qt3DExtras::QPlaneGeometry::QPlaneGeometry(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometry *ritual_ZN10Qt3DExtras14QPlaneGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QPlaneGeometry(parent);
}

//  Qt3DExtras::QPlaneGeometry::~QPlaneGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometryD1Ev(
    Qt3DExtras::QPlaneGeometry *self) {
  delete self;
}

//  void Qt3DExtras::QPlaneGeometry::updateVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry14updateVerticesEv(
    Qt3DExtras::QPlaneGeometry *self) {
  self->updateVertices();
}

//  void Qt3DExtras::QPlaneGeometry::updateIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry13updateIndicesEv(
    Qt3DExtras::QPlaneGeometry *self) {
  self->updateIndices();
}

//  QSize Qt3DExtras::QPlaneGeometry::resolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras14QPlaneGeometry10resolutionEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return new QSize(self->resolution());
}

//  float Qt3DExtras::QPlaneGeometry::width() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QPlaneGeometry5widthEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->width();
}

//  float Qt3DExtras::QPlaneGeometry::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QPlaneGeometry6heightEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->height();
}

//  bool Qt3DExtras::QPlaneGeometry::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras14QPlaneGeometry8mirroredEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->mirrored();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::positionAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QPlaneGeometry17positionAttributeEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::normalAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QPlaneGeometry15normalAttributeEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::texCoordAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QPlaneGeometry17texCoordAttributeEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->texCoordAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::tangentAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QPlaneGeometry16tangentAttributeEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->tangentAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QPlaneGeometry::indexAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras14QPlaneGeometry14indexAttributeEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->indexAttribute();
}

//  void Qt3DExtras::QPlaneGeometry::setResolution(const QSize &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry13setResolutionERK5QSize(
    Qt3DExtras::QPlaneGeometry *self,
    const QSize *resolution) {
  self->setResolution(*resolution);
}

//  void Qt3DExtras::QPlaneGeometry::setWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry8setWidthEf(
    Qt3DExtras::QPlaneGeometry *self,
    float width) {
  self->setWidth(width);
}

//  void Qt3DExtras::QPlaneGeometry::setHeight(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry9setHeightEf(
    Qt3DExtras::QPlaneGeometry *self,
    float height) {
  self->setHeight(height);
}

//  void Qt3DExtras::QPlaneGeometry::setMirrored(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry11setMirroredEb(
    Qt3DExtras::QPlaneGeometry *self,
    bool mirrored) {
  self->setMirrored(mirrored);
}

//  void Qt3DExtras::QPlaneGeometry::resolutionChanged(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry17resolutionChangedERK5QSize(
    Qt3DExtras::QPlaneGeometry *self,
    const QSize *resolution) {
  self->resolutionChanged(*resolution);
}

//  void Qt3DExtras::QPlaneGeometry::widthChanged(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry12widthChangedEf(
    Qt3DExtras::QPlaneGeometry *self,
    float width) {
  self->widthChanged(width);
}

//  void Qt3DExtras::QPlaneGeometry::heightChanged(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry13heightChangedEf(
    Qt3DExtras::QPlaneGeometry *self,
    float height) {
  self->heightChanged(height);
}

//  void Qt3DExtras::QPlaneGeometry::mirroredChanged(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPlaneGeometry15mirroredChangedEb(
    Qt3DExtras::QPlaneGeometry *self,
    bool mirrored) {
  self->mirroredChanged(mirrored);
}

//  Qt3DExtras::QPlaneGeometry::QPlaneGeometry(QPlaneGeometryPrivate &dd,
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometry *ritual_ZN10Qt3DExtras14QPlaneGeometryC1ERNS_21QPlaneGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QPlaneGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QPlaneGeometry(*dd, parent);
}

//  QPlaneGeometryPrivate *Qt3DExtras::QPlaneGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometryPrivate *ritual_ZN10Qt3DExtras14QPlaneGeometry6d_funcEv(
    Qt3DExtras::QPlaneGeometry *self) {
  return self->d_func();
}

//  const QPlaneGeometryPrivate *Qt3DExtras::QPlaneGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPlaneGeometryPrivate *ritual_ZNK10Qt3DExtras14QPlaneGeometry6d_funcEv(
    const Qt3DExtras::QPlaneGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QPlaneGeometry, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPlaneGeometry(
    Qt3DExtras::QPlaneGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPlaneGeometry *>(self)->take(key, call);
}
