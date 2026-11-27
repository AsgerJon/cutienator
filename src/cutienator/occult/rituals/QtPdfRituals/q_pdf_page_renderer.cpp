//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdfpagerenderer.h, Qt 6.12.0. Changes made here are lost.
#include <QtPdf/qpdfpagerenderer.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtPdf/qpdfdocumentrenderoptions.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPdfPageRenderer that Python can take functions over in. Every QPdfPageRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfPageRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfPageRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfPageRenderer : public QPdfPageRenderer {
public:
  using QPdfPageRenderer::QPdfPageRenderer;
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
      CuteQPdfPageRendererCall0 call = reinterpret_cast<CuteQPdfPageRendererCall0>(taken[0]);
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
      CuteQPdfPageRendererCall1 call = reinterpret_cast<CuteQPdfPageRendererCall1>(taken[1]);
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
      CuteQPdfPageRendererCall2 call = reinterpret_cast<CuteQPdfPageRendererCall2>(taken[2]);
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
      CuteQPdfPageRendererCall3 call = reinterpret_cast<CuteQPdfPageRendererCall3>(taken[3]);
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
      CuteQPdfPageRendererCall4 call = reinterpret_cast<CuteQPdfPageRendererCall4>(taken[4]);
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
      CuteQPdfPageRendererCall5 call = reinterpret_cast<CuteQPdfPageRendererCall5>(taken[5]);
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
      CuteQPdfPageRendererCall6 call = reinterpret_cast<CuteQPdfPageRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfPageRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPdfPageRenderer10metaObjectEv(
    const QPdfPageRenderer *self) {
  return self->metaObject();
}

//  void *QPdfPageRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QPdfPageRenderer11qt_metacastEPKc(
    QPdfPageRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfPageRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QPdfPageRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfPageRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfPageRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPdfPageRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPdfPageRenderer::tr(s, c, n));
}

//  QPdfPageRenderer::QPdfPageRenderer()
extern "C" Q_DECL_EXPORT
QPdfPageRenderer *ritual_ZN16QPdfPageRendererC1Ev() {
  return new CuteQPdfPageRenderer();
}

//  QPdfPageRenderer::QPdfPageRenderer(QObject *parent)
extern "C" Q_DECL_EXPORT
QPdfPageRenderer *ritual_ZN16QPdfPageRendererC1EP7QObject(QObject *parent) {
  return new CuteQPdfPageRenderer(parent);
}

//  QPdfPageRenderer::~QPdfPageRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRendererD1Ev(QPdfPageRenderer *self) {
  delete self;
}

//  RenderMode QPdfPageRenderer::renderMode() const
extern "C" Q_DECL_EXPORT
QPdfPageRenderer::RenderMode ritual_ZNK16QPdfPageRenderer10renderModeEv(
    const QPdfPageRenderer *self) {
  return self->renderMode();
}

//  void QPdfPageRenderer::setRenderMode(RenderMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRenderer13setRenderModeENS_10RenderModeE(
    QPdfPageRenderer *self,
    QPdfPageRenderer::RenderMode mode) {
  self->setRenderMode(mode);
}

//  QPdfDocument *QPdfPageRenderer::document() const
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZNK16QPdfPageRenderer8documentEv(
    const QPdfPageRenderer *self) {
  return self->document();
}

//  void QPdfPageRenderer::setDocument(QPdfDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRenderer11setDocumentEP12QPdfDocument(
    QPdfPageRenderer *self,
    QPdfDocument *document) {
  self->setDocument(document);
}

//  quint64 QPdfPageRenderer::requestPage(int pageNumber, QSize imageSize,
//      QPdfDocumentRenderOptions options)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QPdfPageRenderer11requestPageEi5QSize25QPdfDocumentRenderOptions(
    QPdfPageRenderer *self,
    int pageNumber,
    const QSize *imageSize,
    const QPdfDocumentRenderOptions *options) {
  return self->requestPage(pageNumber, *imageSize, *options);
}

//  void QPdfPageRenderer::documentChanged(QPdfDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRenderer15documentChangedEP12QPdfDocument(
    QPdfPageRenderer *self,
    QPdfDocument *document) {
  self->documentChanged(document);
}

//  void QPdfPageRenderer::renderModeChanged(QPdfPageRenderer::RenderMode
//      renderMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRenderer17renderModeChangedENS_10RenderModeE(
    QPdfPageRenderer *self,
    QPdfPageRenderer::RenderMode renderMode) {
  self->renderModeChanged(renderMode);
}

//  void QPdfPageRenderer::pageRendered(int pageNumber, QSize imageSize,
//      const QImage &image, QPdfDocumentRenderOptions options, quint64
//      requestId)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPdfPageRenderer12pageRenderedEi5QSizeRK6QImage25QPdfDocumentRenderOptionsy(
    QPdfPageRenderer *self,
    int pageNumber,
    const QSize *imageSize,
    const QImage *image,
    const QPdfDocumentRenderOptions *options,
    quint64 requestId) {
  self->pageRendered(pageNumber, *imageSize, *image, *options, requestId);
}

//  a Python function taken by a CuteQPdfPageRenderer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfPageRenderer(
    QPdfPageRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfPageRenderer *>(self)->take(key, call);
}
