//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qextrudedtextmesh.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qextrudedtextmesh.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QExtrudedTextMesh that Python can take functions over in. Every Qt3DExtras::QExtrudedTextMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QExtrudedTextMeshCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QExtrudedTextMeshCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextMeshCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextMeshCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextMeshCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextMeshCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QExtrudedTextMeshCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QExtrudedTextMesh : public Qt3DExtras::QExtrudedTextMesh {
public:
  using Qt3DExtras::QExtrudedTextMesh::QExtrudedTextMesh;
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
      CuteQt3DExtras_QExtrudedTextMeshCall0 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall0>(taken[0]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall1 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall1>(taken[1]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall2 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall2>(taken[2]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall3 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall3>(taken[3]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall4 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall4>(taken[4]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall5 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall5>(taken[5]);
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
      CuteQt3DExtras_QExtrudedTextMeshCall6 call = reinterpret_cast<CuteQt3DExtras_QExtrudedTextMeshCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QExtrudedTextMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras17QExtrudedTextMesh10metaObjectEv(
    const Qt3DExtras::QExtrudedTextMesh *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QExtrudedTextMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras17QExtrudedTextMesh11qt_metacastEPKc(
    Qt3DExtras::QExtrudedTextMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QExtrudedTextMesh::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras17QExtrudedTextMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QExtrudedTextMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QExtrudedTextMesh::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras17QExtrudedTextMesh2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QExtrudedTextMesh::tr(s, c, n));
}

//  Qt3DExtras::QExtrudedTextMesh::QExtrudedTextMesh(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QExtrudedTextMesh *ritual_ZN10Qt3DExtras17QExtrudedTextMeshC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QExtrudedTextMesh(parent);
}

//  Qt3DExtras::QExtrudedTextMesh::~QExtrudedTextMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMeshD1Ev(
    Qt3DExtras::QExtrudedTextMesh *self) {
  delete self;
}

//  QString Qt3DExtras::QExtrudedTextMesh::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DExtras17QExtrudedTextMesh4textEv(
    const Qt3DExtras::QExtrudedTextMesh *self) {
  return new QString(self->text());
}

//  QFont Qt3DExtras::QExtrudedTextMesh::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10Qt3DExtras17QExtrudedTextMesh4fontEv(
    const Qt3DExtras::QExtrudedTextMesh *self) {
  return new QFont(self->font());
}

//  float Qt3DExtras::QExtrudedTextMesh::depth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras17QExtrudedTextMesh5depthEv(
    const Qt3DExtras::QExtrudedTextMesh *self) {
  return self->depth();
}

//  void Qt3DExtras::QExtrudedTextMesh::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh7setTextERK7QString(
    Qt3DExtras::QExtrudedTextMesh *self,
    const QString *text) {
  self->setText(*text);
}

//  void Qt3DExtras::QExtrudedTextMesh::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh7setFontERK5QFont(
    Qt3DExtras::QExtrudedTextMesh *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void Qt3DExtras::QExtrudedTextMesh::setDepth(float depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh8setDepthEf(
    Qt3DExtras::QExtrudedTextMesh *self,
    float depth) {
  self->setDepth(depth);
}

//  void Qt3DExtras::QExtrudedTextMesh::textChanged(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh11textChangedERK7QString(
    Qt3DExtras::QExtrudedTextMesh *self,
    const QString *text) {
  self->textChanged(*text);
}

//  void Qt3DExtras::QExtrudedTextMesh::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh11fontChangedERK5QFont(
    Qt3DExtras::QExtrudedTextMesh *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void Qt3DExtras::QExtrudedTextMesh::depthChanged(float depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras17QExtrudedTextMesh12depthChangedEf(
    Qt3DExtras::QExtrudedTextMesh *self,
    float depth) {
  self->depthChanged(depth);
}

//  a Python function taken by a CuteQt3DExtras_QExtrudedTextMesh, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QExtrudedTextMesh(
    Qt3DExtras::QExtrudedTextMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QExtrudedTextMesh *>(self)->take(key, call);
}
