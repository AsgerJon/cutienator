//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtextureimage.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qtextureimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QTextureImage that Python can take functions over in. Every Qt3DRender::QTextureImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QTextureImageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QTextureImageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTextureImageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTextureImageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTextureImageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTextureImageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTextureImageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QTextureImage : public Qt3DRender::QTextureImage {
public:
  using Qt3DRender::QTextureImage::QTextureImage;
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
      CuteQt3DRender_QTextureImageCall0 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall0>(taken[0]);
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
      CuteQt3DRender_QTextureImageCall1 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall1>(taken[1]);
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
      CuteQt3DRender_QTextureImageCall2 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall2>(taken[2]);
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
      CuteQt3DRender_QTextureImageCall3 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall3>(taken[3]);
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
      CuteQt3DRender_QTextureImageCall4 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall4>(taken[4]);
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
      CuteQt3DRender_QTextureImageCall5 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall5>(taken[5]);
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
      CuteQt3DRender_QTextureImageCall6 call = reinterpret_cast<CuteQt3DRender_QTextureImageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QTextureImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QTextureImage10metaObjectEv(
    const Qt3DRender::QTextureImage *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QTextureImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender13QTextureImage11qt_metacastEPKc(
    Qt3DRender::QTextureImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QTextureImage::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender13QTextureImage11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QTextureImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QTextureImage::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QTextureImage2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QTextureImage::tr(s, c, n));
}

//  Qt3DRender::QTextureImage::QTextureImage(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImage *ritual_ZN10Qt3DRender13QTextureImageC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QTextureImage(parent);
}

//  Qt3DRender::QTextureImage::~QTextureImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImageD1Ev(
    Qt3DRender::QTextureImage *self) {
  delete self;
}

//  QUrl Qt3DRender::QTextureImage::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender13QTextureImage6sourceEv(
    const Qt3DRender::QTextureImage *self) {
  return new QUrl(self->source());
}

//  Status Qt3DRender::QTextureImage::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImage::Status ritual_ZNK10Qt3DRender13QTextureImage6statusEv(
    const Qt3DRender::QTextureImage *self) {
  return self->status();
}

//  bool Qt3DRender::QTextureImage::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QTextureImage10isMirroredEv(
    const Qt3DRender::QTextureImage *self) {
  return self->isMirrored();
}

//  void Qt3DRender::QTextureImage::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage9setSourceERK4QUrl(
    Qt3DRender::QTextureImage *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void Qt3DRender::QTextureImage::setMirrored(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage11setMirroredEb(
    Qt3DRender::QTextureImage *self,
    bool mirrored) {
  self->setMirrored(mirrored);
}

//  void Qt3DRender::QTextureImage::sourceChanged(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage13sourceChangedERK4QUrl(
    Qt3DRender::QTextureImage *self,
    const QUrl *source) {
  self->sourceChanged(*source);
}

//  void Qt3DRender::QTextureImage::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage13statusChangedENS0_6StatusE(
    Qt3DRender::QTextureImage *self,
    Qt3DRender::QTextureImage::Status status) {
  self->statusChanged(status);
}

//  void Qt3DRender::QTextureImage::mirroredChanged(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage15mirroredChangedEb(
    Qt3DRender::QTextureImage *self,
    bool mirrored) {
  self->mirroredChanged(mirrored);
}

//  void Qt3DRender::QTextureImage::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QTextureImage9setStatusENS0_6StatusE(
    Qt3DRender::QTextureImage *self,
    Qt3DRender::QTextureImage::Status status) {
  self->setStatus(status);
}

//  QTextureImageDataGeneratorPtr Qt3DRender::QTextureImage::dataGenerator()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataGeneratorPtr *ritual_ZNK10Qt3DRender13QTextureImage13dataGeneratorEv(
    const Qt3DRender::QTextureImage *self) {
  return new Qt3DRender::QTextureImageDataGeneratorPtr(
      self->dataGenerator());
}

//  QTextureImagePrivate *Qt3DRender::QTextureImage::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImagePrivate *ritual_ZN10Qt3DRender13QTextureImage6d_funcEv(
    Qt3DRender::QTextureImage *self) {
  return self->d_func();
}

//  const QTextureImagePrivate *Qt3DRender::QTextureImage::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureImagePrivate *ritual_ZNK10Qt3DRender13QTextureImage6d_funcEv(
    const Qt3DRender::QTextureImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QTextureImage, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTextureImage(
    Qt3DRender::QTextureImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTextureImage *>(self)->take(key, call);
}

//  a Qt3DRender::QTextureImageDataGeneratorPtr a ritual of
//      Qt3DRender::QTextureImage gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QTextureImage__Qt3DRender_QTextureImageDataGeneratorPtr(
    Qt3DRender::QTextureImageDataGeneratorPtr *self) {
  delete self;
}
