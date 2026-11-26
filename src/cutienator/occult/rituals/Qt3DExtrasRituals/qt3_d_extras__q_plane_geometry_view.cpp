//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qplanegeometryview.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qplanegeometryview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QPlaneGeometryView that Python can take functions over in. Every Qt3DExtras::QPlaneGeometryView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPlaneGeometryViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPlaneGeometryViewCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryViewCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryViewCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryViewCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryViewCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPlaneGeometryViewCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QPlaneGeometryView : public Qt3DExtras::QPlaneGeometryView {
public:
  using Qt3DExtras::QPlaneGeometryView::QPlaneGeometryView;
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
      CuteQt3DExtras_QPlaneGeometryViewCall0 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall0>(taken[0]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall1 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall1>(taken[1]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall2 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall2>(taken[2]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall3 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall3>(taken[3]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall4 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall4>(taken[4]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall5 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall5>(taken[5]);
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
      CuteQt3DExtras_QPlaneGeometryViewCall6 call = reinterpret_cast<CuteQt3DExtras_QPlaneGeometryViewCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QPlaneGeometryView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras18QPlaneGeometryView10metaObjectEv(
    const Qt3DExtras::QPlaneGeometryView *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QPlaneGeometryView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras18QPlaneGeometryView11qt_metacastEPKc(
    Qt3DExtras::QPlaneGeometryView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QPlaneGeometryView::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras18QPlaneGeometryView11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QPlaneGeometryView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QPlaneGeometryView::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras18QPlaneGeometryView2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QPlaneGeometryView::tr(s, c, n));
}

//  Qt3DExtras::QPlaneGeometryView::QPlaneGeometryView(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPlaneGeometryView *ritual_ZN10Qt3DExtras18QPlaneGeometryViewC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QPlaneGeometryView(parent);
}

//  Qt3DExtras::QPlaneGeometryView::~QPlaneGeometryView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryViewD1Ev(
    Qt3DExtras::QPlaneGeometryView *self) {
  delete self;
}

//  float Qt3DExtras::QPlaneGeometryView::width() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras18QPlaneGeometryView5widthEv(
    const Qt3DExtras::QPlaneGeometryView *self) {
  return self->width();
}

//  float Qt3DExtras::QPlaneGeometryView::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras18QPlaneGeometryView6heightEv(
    const Qt3DExtras::QPlaneGeometryView *self) {
  return self->height();
}

//  QSize Qt3DExtras::QPlaneGeometryView::meshResolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras18QPlaneGeometryView14meshResolutionEv(
    const Qt3DExtras::QPlaneGeometryView *self) {
  return new QSize(self->meshResolution());
}

//  bool Qt3DExtras::QPlaneGeometryView::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras18QPlaneGeometryView8mirroredEv(
    const Qt3DExtras::QPlaneGeometryView *self) {
  return self->mirrored();
}

//  void Qt3DExtras::QPlaneGeometryView::setWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView8setWidthEf(
    Qt3DExtras::QPlaneGeometryView *self,
    float width) {
  self->setWidth(width);
}

//  void Qt3DExtras::QPlaneGeometryView::setHeight(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView9setHeightEf(
    Qt3DExtras::QPlaneGeometryView *self,
    float height) {
  self->setHeight(height);
}

//  void Qt3DExtras::QPlaneGeometryView::setMeshResolution(const QSize
//      &resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView17setMeshResolutionERK5QSize(
    Qt3DExtras::QPlaneGeometryView *self,
    const QSize *resolution) {
  self->setMeshResolution(*resolution);
}

//  void Qt3DExtras::QPlaneGeometryView::setMirrored(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView11setMirroredEb(
    Qt3DExtras::QPlaneGeometryView *self,
    bool mirrored) {
  self->setMirrored(mirrored);
}

//  void Qt3DExtras::QPlaneGeometryView::meshResolutionChanged(const QSize
//      &meshResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView21meshResolutionChangedERK5QSize(
    Qt3DExtras::QPlaneGeometryView *self,
    const QSize *meshResolution) {
  self->meshResolutionChanged(*meshResolution);
}

//  void Qt3DExtras::QPlaneGeometryView::widthChanged(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView12widthChangedEf(
    Qt3DExtras::QPlaneGeometryView *self,
    float width) {
  self->widthChanged(width);
}

//  void Qt3DExtras::QPlaneGeometryView::heightChanged(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView13heightChangedEf(
    Qt3DExtras::QPlaneGeometryView *self,
    float height) {
  self->heightChanged(height);
}

//  void Qt3DExtras::QPlaneGeometryView::mirroredChanged(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras18QPlaneGeometryView15mirroredChangedEb(
    Qt3DExtras::QPlaneGeometryView *self,
    bool mirrored) {
  self->mirroredChanged(mirrored);
}

//  a Python function taken by a CuteQt3DExtras_QPlaneGeometryView, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPlaneGeometryView(
    Qt3DExtras::QPlaneGeometryView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPlaneGeometryView *>(self)->take(key, call);
}
