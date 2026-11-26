//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/qsvgrenderer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSvg/qtsvgglobal.h>
#if !defined(QT_NO_SVGRENDERER)
#include <QtSvg/qsvgrenderer.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSvgRenderer that Python can take functions over in. Every QSvgRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSvgRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSvgRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSvgRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSvgRenderer : public QSvgRenderer {
public:
  using QSvgRenderer::QSvgRenderer;
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
      CuteQSvgRendererCall0 call = reinterpret_cast<CuteQSvgRendererCall0>(taken[0]);
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
      CuteQSvgRendererCall1 call = reinterpret_cast<CuteQSvgRendererCall1>(taken[1]);
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
      CuteQSvgRendererCall2 call = reinterpret_cast<CuteQSvgRendererCall2>(taken[2]);
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
      CuteQSvgRendererCall3 call = reinterpret_cast<CuteQSvgRendererCall3>(taken[3]);
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
      CuteQSvgRendererCall4 call = reinterpret_cast<CuteQSvgRendererCall4>(taken[4]);
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
      CuteQSvgRendererCall5 call = reinterpret_cast<CuteQSvgRendererCall5>(taken[5]);
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
      CuteQSvgRendererCall6 call = reinterpret_cast<CuteQSvgRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSvgRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QSvgRenderer10metaObjectEv(
    const QSvgRenderer *self) {
  return self->metaObject();
}

//  void *QSvgRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QSvgRenderer11qt_metacastEPKc(
    QSvgRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSvgRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QSvgRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSvgRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSvgRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QSvgRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSvgRenderer::tr(s, c, n));
}

//  QSvgRenderer::QSvgRenderer(QObject *parent)
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZN12QSvgRendererC1EP7QObject(QObject *parent) {
  return new CuteQSvgRenderer(parent);
}

//  QSvgRenderer::QSvgRenderer(const QString &filename, QObject *parent)
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZN12QSvgRendererC1ERK7QStringP7QObject(
    const QString *filename,
    QObject *parent) {
  return new CuteQSvgRenderer(*filename, parent);
}

//  QSvgRenderer::QSvgRenderer(const QByteArray &contents, QObject *parent)
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZN12QSvgRendererC1ERK10QByteArrayP7QObject(
    const QByteArray *contents,
    QObject *parent) {
  return new CuteQSvgRenderer(*contents, parent);
}

//  QSvgRenderer::QSvgRenderer(QXmlStreamReader *contents, QObject *parent)
extern "C" Q_DECL_EXPORT
QSvgRenderer *ritual_ZN12QSvgRendererC1EP16QXmlStreamReaderP7QObject(
    QXmlStreamReader *contents,
    QObject *parent) {
  return new CuteQSvgRenderer(contents, parent);
}

//  QSvgRenderer::~QSvgRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRendererD1Ev(QSvgRenderer *self) {
  delete self;
}

//  bool QSvgRenderer::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgRenderer7isValidEv(const QSvgRenderer *self) {
  return self->isValid();
}

//  QSize QSvgRenderer::defaultSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QSvgRenderer11defaultSizeEv(const QSvgRenderer *self) {
  return new QSize(self->defaultSize());
}

//  QRect QSvgRenderer::viewBox() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QSvgRenderer7viewBoxEv(const QSvgRenderer *self) {
  return new QRect(self->viewBox());
}

//  QRectF QSvgRenderer::viewBoxF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSvgRenderer8viewBoxFEv(const QSvgRenderer *self) {
  return new QRectF(self->viewBoxF());
}

//  void QSvgRenderer::setViewBox(const QRect &viewbox)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer10setViewBoxERK5QRect(
    QSvgRenderer *self,
    const QRect *viewbox) {
  self->setViewBox(*viewbox);
}

//  void QSvgRenderer::setViewBox(const QRectF &viewbox)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer10setViewBoxERK6QRectF(
    QSvgRenderer *self,
    const QRectF *viewbox) {
  self->setViewBox(*viewbox);
}

//  Qt::AspectRatioMode QSvgRenderer::aspectRatioMode() const
extern "C" Q_DECL_EXPORT
Qt::AspectRatioMode ritual_ZNK12QSvgRenderer15aspectRatioModeEv(
    const QSvgRenderer *self) {
  return self->aspectRatioMode();
}

//  void QSvgRenderer::setAspectRatioMode(Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QSvgRenderer *self,
    Qt::AspectRatioMode mode) {
  self->setAspectRatioMode(mode);
}

//  QtSvg::Options QSvgRenderer::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgRenderer7optionsEv(const QSvgRenderer *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QSvgRenderer::setOptions(QtSvg::Options flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer10setOptionsE6QFlagsIN5QtSvg6OptionEE(
    QSvgRenderer *self,
    int flags) {
  self->setOptions(QFlags<QtSvg::Option>::fromInt(flags));
}

//  bool QSvgRenderer::animated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgRenderer8animatedEv(const QSvgRenderer *self) {
  return self->animated();
}

//  int QSvgRenderer::framesPerSecond() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgRenderer15framesPerSecondEv(const QSvgRenderer *self) {
  return self->framesPerSecond();
}

//  void QSvgRenderer::setFramesPerSecond(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer18setFramesPerSecondEi(
    QSvgRenderer *self,
    int num) {
  self->setFramesPerSecond(num);
}

//  int QSvgRenderer::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgRenderer12currentFrameEv(const QSvgRenderer *self) {
  return self->currentFrame();
}

//  void QSvgRenderer::setCurrentFrame(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer15setCurrentFrameEi(QSvgRenderer *self, int a0) {
  self->setCurrentFrame(a0);
}

//  int QSvgRenderer::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgRenderer17animationDurationEv(const QSvgRenderer *self) {
  return self->animationDuration();
}

//  bool QSvgRenderer::isAnimationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgRenderer18isAnimationEnabledEv(
    const QSvgRenderer *self) {
  return self->isAnimationEnabled();
}

//  void QSvgRenderer::setAnimationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer19setAnimationEnabledEb(
    QSvgRenderer *self,
    bool enable) {
  self->setAnimationEnabled(enable);
}

//  QRectF QSvgRenderer::boundsOnElement(const QString &id) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSvgRenderer15boundsOnElementERK7QString(
    const QSvgRenderer *self,
    const QString *id) {
  return new QRectF(self->boundsOnElement(*id));
}

//  bool QSvgRenderer::elementExists(const QString &id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgRenderer13elementExistsERK7QString(
    const QSvgRenderer *self,
    const QString *id) {
  return self->elementExists(*id);
}

//  QTransform QSvgRenderer::transformForElement(const QString &id) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK12QSvgRenderer19transformForElementERK7QString(
    const QSvgRenderer *self,
    const QString *id) {
  return new QTransform(self->transformForElement(*id));
}

//  void QSvgRenderer::setDefaultOptions(QtSvg::Options flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer17setDefaultOptionsE6QFlagsIN5QtSvg6OptionEE(
    int flags) {
  QSvgRenderer::setDefaultOptions(QFlags<QtSvg::Option>::fromInt(flags));
}

//  bool QSvgRenderer::load(const QString &filename)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSvgRenderer4loadERK7QString(
    QSvgRenderer *self,
    const QString *filename) {
  return self->load(*filename);
}

//  bool QSvgRenderer::load(const QByteArray &contents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSvgRenderer4loadERK10QByteArray(
    QSvgRenderer *self,
    const QByteArray *contents) {
  return self->load(*contents);
}

//  bool QSvgRenderer::load(QXmlStreamReader *contents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSvgRenderer4loadEP16QXmlStreamReader(
    QSvgRenderer *self,
    QXmlStreamReader *contents) {
  return self->load(contents);
}

//  void QSvgRenderer::render(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer6renderEP8QPainter(
    QSvgRenderer *self,
    QPainter *p) {
  self->render(p);
}

//  void QSvgRenderer::render(QPainter *p, const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer6renderEP8QPainterRK6QRectF(
    QSvgRenderer *self,
    QPainter *p,
    const QRectF *bounds) {
  self->render(p, *bounds);
}

//  void QSvgRenderer::render(QPainter *p, const QString &elementId, const
//      QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer6renderEP8QPainterRK7QStringRK6QRectF(
    QSvgRenderer *self,
    QPainter *p,
    const QString *elementId,
    const QRectF *bounds) {
  self->render(p, *elementId, *bounds);
}

//  void QSvgRenderer::repaintNeeded()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgRenderer13repaintNeededEv(QSvgRenderer *self) {
  self->repaintNeeded();
}

//  QSvgRendererPrivate *QSvgRenderer::d_func()
extern "C" Q_DECL_EXPORT
QSvgRendererPrivate *ritual_ZN12QSvgRenderer6d_funcEv(QSvgRenderer *self) {
  return self->d_func();
}

//  const QSvgRendererPrivate *QSvgRenderer::d_func() const
extern "C" Q_DECL_EXPORT
const QSvgRendererPrivate *ritual_ZNK12QSvgRenderer6d_funcEv(
    const QSvgRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSvgRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgRenderer(
    QSvgRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgRenderer *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_SVGRENDERER)
