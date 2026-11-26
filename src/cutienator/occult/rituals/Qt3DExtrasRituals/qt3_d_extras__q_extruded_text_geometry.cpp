//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qextrudedtextgeometry.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DExtras/qextrudedtextgeometry.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QExtrudedTextGeometry that Python can take functions over in. Every Qt3DExtras::QExtrudedTextGeometry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QExtrudedTextGeometryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QExtrudedTextGeometryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextGeometryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QExtrudedTextGeometry : public Qt3DExtras::QExtrudedTextGeometry {
public:
  using Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry;
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
      CuteQt3DExtras_QExtrudedTextGeometryCall0 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall0>(taken[0]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall1 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall1>(taken[1]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall2 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall2>(taken[2]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall3 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall3>(taken[3]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall4 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall4>(taken[4]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall5 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall5>(taken[5]);
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
      CuteQt3DExtras_QExtrudedTextGeometryCall6 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextGeometryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QExtrudedTextGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry10metaObjectEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QExtrudedTextGeometry::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11qt_metacastEPKc(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QExtrudedTextGeometry::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QExtrudedTextGeometry *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QExtrudedTextGeometry::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras21QExtrudedTextGeometry2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QExtrudedTextGeometry::tr(s, c, n));
}

//  Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QExtrudedTextGeometry *ritual_ZN10Qt3DExtras21QExtrudedTextGeometryC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QExtrudedTextGeometry(parent);
}

//  Qt3DExtras::QExtrudedTextGeometry::~QExtrudedTextGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometryD1Ev(
    Qt3DExtras::QExtrudedTextGeometry *self) {
  delete self;
}

//  Qt3DCore::QAttribute
//      *Qt3DExtras::QExtrudedTextGeometry::positionAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry17positionAttributeEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->positionAttribute();
}

//  Qt3DCore::QAttribute
//      *Qt3DExtras::QExtrudedTextGeometry::normalAttribute() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry15normalAttributeEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->normalAttribute();
}

//  Qt3DCore::QAttribute *Qt3DExtras::QExtrudedTextGeometry::indexAttribute()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry14indexAttributeEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->indexAttribute();
}

//  QString Qt3DExtras::QExtrudedTextGeometry::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry4textEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return new QString(self->text());
}

//  QFont Qt3DExtras::QExtrudedTextGeometry::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry4fontEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return new QFont(self->font());
}

//  float Qt3DExtras::QExtrudedTextGeometry::extrusionLength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry15extrusionLengthEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->extrusionLength();
}

//  void Qt3DExtras::QExtrudedTextGeometry::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry7setTextERK7QString(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const QString *text) {
  self->setText(*text);
}

//  void Qt3DExtras::QExtrudedTextGeometry::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry7setFontERK5QFont(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void Qt3DExtras::QExtrudedTextGeometry::setDepth(float extrusionLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry8setDepthEf(
    Qt3DExtras::QExtrudedTextGeometry *self,
    float extrusionLength) {
  self->setDepth(extrusionLength);
}

//  void Qt3DExtras::QExtrudedTextGeometry::textChanged(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11textChangedERK7QString(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const QString *text) {
  self->textChanged(*text);
}

//  void Qt3DExtras::QExtrudedTextGeometry::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11fontChangedERK5QFont(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void Qt3DExtras::QExtrudedTextGeometry::depthChanged(float
//      extrusionLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QExtrudedTextGeometry12depthChangedEf(
    Qt3DExtras::QExtrudedTextGeometry *self,
    float extrusionLength) {
  self->depthChanged(extrusionLength);
}

//  Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry(QExtrudedTextGeo
//      metryPrivate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QExtrudedTextGeometry *ritual_ZN10Qt3DExtras21QExtrudedTextGeometryC1ERNS_28QExtrudedTextGeometryPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QExtrudedTextGeometryPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QExtrudedTextGeometry(*dd, parent);
}

//  QExtrudedTextGeometryPrivate *Qt3DExtras::QExtrudedTextGeometry::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QExtrudedTextGeometryPrivate *ritual_ZN10Qt3DExtras21QExtrudedTextGeometry6d_funcEv(
    Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->d_func();
}

//  const QExtrudedTextGeometryPrivate
//      *Qt3DExtras::QExtrudedTextGeometry::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QExtrudedTextGeometryPrivate *ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry6d_funcEv(
    const Qt3DExtras::QExtrudedTextGeometry *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QExtrudedTextGeometry, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QExtrudedTextGeometry(
    Qt3DExtras::QExtrudedTextGeometry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QExtrudedTextGeometry *>(self)->take(key, call);
}
