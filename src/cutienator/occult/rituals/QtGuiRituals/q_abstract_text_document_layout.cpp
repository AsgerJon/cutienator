//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractTextDocumentLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractTextDocumentLayout : QAbstractTextDocumentLayout {
  using QAbstractTextDocumentLayout::resizeInlineObject;
  using QAbstractTextDocumentLayout::positionInlineObject;
  using QAbstractTextDocumentLayout::drawInlineObject;
};

//  A QAbstractTextDocumentLayout that Python can take functions over in. Every QAbstractTextDocumentLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractTextDocumentLayoutCall0)(const void *, QPainter *, const QAbstractTextDocumentLayout::PaintContext *, int *);
typedef int (*CuteQAbstractTextDocumentLayoutCall1)(const void *, const QPointF *, int, int *);
typedef int (*CuteQAbstractTextDocumentLayoutCall2)(const void *, int *);
typedef const QSizeF * (*CuteQAbstractTextDocumentLayoutCall3)(const void *, int *);
typedef const QRectF * (*CuteQAbstractTextDocumentLayoutCall4)(const void *, QTextFrame *, int *);
typedef const QRectF * (*CuteQAbstractTextDocumentLayoutCall5)(const void *, const QTextBlock *, int *);
typedef void (*CuteQAbstractTextDocumentLayoutCall6)(const void *, int, int, int, int *);
typedef void (*CuteQAbstractTextDocumentLayoutCall7)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQAbstractTextDocumentLayoutCall8)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQAbstractTextDocumentLayoutCall9)(const void *, QPainter *, const QRectF *, const QTextInlineObject *, int, const QTextFormat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTextDocumentLayoutCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTextDocumentLayoutCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTextDocumentLayoutCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTextDocumentLayoutCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTextDocumentLayoutCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTextDocumentLayoutCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTextDocumentLayoutCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractTextDocumentLayout : public QAbstractTextDocumentLayout {
public:
  using QAbstractTextDocumentLayout::QAbstractTextDocumentLayout;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12PaintContextE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout9pageCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout12documentSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTextFrame")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTextBlock")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout15documentChangedEiii")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE17QTextInlineObjectiRK11QTextFormat")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout20positionInlineObjectE17QTextInlineObjectiRK11QTextFormat")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRectF17QTextInlineObjectiRK11QTextFormat")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstractTextDocumentLayout::draw(QPainter *painter, const
  //      PaintContext &context)
  void draw(
      QPainter *painter,
      const QAbstractTextDocumentLayout::PaintContext &context) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall0 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall0>(taken[0]);
      call(this, painter, &context, &handled);
      if (handled) return;
    }
  }

  //  int QAbstractTextDocumentLayout::hitTest(const QPointF &point,
  //      Qt::HitTestAccuracy accuracy) const
  int hitTest(
      const QPointF &point,
      Qt::HitTestAccuracy accuracy) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall1 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall1>(taken[1]);
      int given = call(this, &point, static_cast<int>(accuracy), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractTextDocumentLayout::pageCount() const
  int pageCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall2 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSizeF QAbstractTextDocumentLayout::documentSize() const
  QSizeF documentSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall3 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall3>(taken[3]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QRectF QAbstractTextDocumentLayout::frameBoundingRect(QTextFrame
  //      *frame) const
  QRectF frameBoundingRect(QTextFrame *frame) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall4 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall4>(taken[4]);
      const QRectF * given = call(this, frame, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QRectF QAbstractTextDocumentLayout::blockBoundingRect(const
  //      QTextBlock &block) const
  QRectF blockBoundingRect(const QTextBlock &block) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall5 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall5>(taken[5]);
      const QRectF * given = call(this, &block, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAbstractTextDocumentLayout::documentChanged(int from, int
  //      charsRemoved, int charsAdded)
  void documentChanged(int from, int charsRemoved, int charsAdded) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall6 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall6>(taken[6]);
      call(this, from, charsRemoved, charsAdded, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject
  //      item, int posInDocument, const QTextFormat &format)
  void resizeInlineObject(
      QTextInlineObject item,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall7 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall7>(taken[7]);
      call(this, &item, posInDocument, &format, &handled);
      if (handled) return;
    }
    QAbstractTextDocumentLayout::resizeInlineObject(item, posInDocument, format);
  }

  //  void
  //      QAbstractTextDocumentLayout::positionInlineObject(QTextInlineObje
  //      ct item, int posInDocument, const QTextFormat &format)
  void positionInlineObject(
      QTextInlineObject item,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall8 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall8>(taken[8]);
      call(this, &item, posInDocument, &format, &handled);
      if (handled) return;
    }
    QAbstractTextDocumentLayout::positionInlineObject(item, posInDocument, format);
  }

  //  void QAbstractTextDocumentLayout::drawInlineObject(QPainter *painter,
  //      const QRectF &rect, QTextInlineObject object, int posInDocument,
  //      const QTextFormat &format)
  void drawInlineObject(
      QPainter *painter,
      const QRectF &rect,
      QTextInlineObject object,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall9 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall9>(taken[9]);
      call(this, painter, &rect, &object, posInDocument, &format, &handled);
      if (handled) return;
    }
    QAbstractTextDocumentLayout::drawInlineObject(painter, rect, object, posInDocument, format);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall10 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall11 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall12 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall13 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall14 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall15 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractTextDocumentLayoutCall16 call = reinterpret_cast<CuteQAbstractTextDocumentLayoutCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractTextDocumentLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QAbstractTextDocumentLayout10metaObjectEv(
    const QAbstractTextDocumentLayout *self) {
  return self->metaObject();
}

//  void *QAbstractTextDocumentLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QAbstractTextDocumentLayout11qt_metacastEPKc(
    QAbstractTextDocumentLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractTextDocumentLayout::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QAbstractTextDocumentLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractTextDocumentLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractTextDocumentLayout::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QAbstractTextDocumentLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTextDocumentLayout::tr(s, c, n));
}

//  QAbstractTextDocumentLayoutPrivate *QAbstractTextDocumentLayout::d_func()
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayoutPrivate *ritual_ZN27QAbstractTextDocumentLayout6d_funcEv(
    QAbstractTextDocumentLayout *self) {
  return self->d_func();
}

//  const QAbstractTextDocumentLayoutPrivate
//      *QAbstractTextDocumentLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractTextDocumentLayoutPrivate *ritual_ZNK27QAbstractTextDocumentLayout6d_funcEv(
    const QAbstractTextDocumentLayout *self) {
  return self->d_func();
}

//  QAbstractTextDocumentLayout::QAbstractTextDocumentLayout(QTextDocument
//      *doc)
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZN27QAbstractTextDocumentLayoutC1EP13QTextDocument(
    QTextDocument *doc) {
  return new CuteQAbstractTextDocumentLayout(doc);
}

//  QAbstractTextDocumentLayout::~QAbstractTextDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayoutD1Ev(
    QAbstractTextDocumentLayout *self) {
  delete self;
}

//  void QAbstractTextDocumentLayout::draw(QPainter *painter, const
//      PaintContext &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12PaintContextE(
    QAbstractTextDocumentLayout *self,
    QPainter *painter,
    const QAbstractTextDocumentLayout::PaintContext *context) {
  self->draw(painter, *context);
}

//  int QAbstractTextDocumentLayout::hitTest(const QPointF &point,
//      Qt::HitTestAccuracy accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QAbstractTextDocumentLayout *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->hitTest(*point, accuracy);
}

//  QString QAbstractTextDocumentLayout::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractTextDocumentLayout8anchorAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}

//  QString QAbstractTextDocumentLayout::imageAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractTextDocumentLayout7imageAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QString(self->imageAt(*pos));
}

//  QTextFormat QAbstractTextDocumentLayout::formatAt(const QPointF &pos)
//      const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK27QAbstractTextDocumentLayout8formatAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QTextFormat(self->formatAt(*pos));
}

//  QTextBlock QAbstractTextDocumentLayout::blockWithMarkerAt(const QPointF
//      &pos) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK27QAbstractTextDocumentLayout17blockWithMarkerAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QTextBlock(self->blockWithMarkerAt(*pos));
}

//  int QAbstractTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QAbstractTextDocumentLayout9pageCountEv(
    const QAbstractTextDocumentLayout *self) {
  return self->pageCount();
}

//  QSizeF QAbstractTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK27QAbstractTextDocumentLayout12documentSizeEv(
    const QAbstractTextDocumentLayout *self) {
  return new QSizeF(self->documentSize());
}

//  QRectF QAbstractTextDocumentLayout::frameBoundingRect(QTextFrame *frame)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QAbstractTextDocumentLayout *self,
    QTextFrame *frame) {
  return new QRectF(self->frameBoundingRect(frame));
}

//  QRectF QAbstractTextDocumentLayout::blockBoundingRect(const QTextBlock
//      &block) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QAbstractTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  void QAbstractTextDocumentLayout::setPaintDevice(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout14setPaintDeviceEP12QPaintDevice(
    QAbstractTextDocumentLayout *self,
    QPaintDevice *device) {
  self->setPaintDevice(device);
}

//  QPaintDevice *QAbstractTextDocumentLayout::paintDevice() const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK27QAbstractTextDocumentLayout11paintDeviceEv(
    const QAbstractTextDocumentLayout *self) {
  return self->paintDevice();
}

//  QTextDocument *QAbstractTextDocumentLayout::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK27QAbstractTextDocumentLayout8documentEv(
    const QAbstractTextDocumentLayout *self) {
  return self->document();
}

//  void QAbstractTextDocumentLayout::registerHandler(int objectType, QObject
//      *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout15registerHandlerEiP7QObject(
    QAbstractTextDocumentLayout *self,
    int objectType,
    QObject *component) {
  self->registerHandler(objectType, component);
}

//  void QAbstractTextDocumentLayout::unregisterHandler(int objectType,
//      QObject *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout17unregisterHandlerEiP7QObject(
    QAbstractTextDocumentLayout *self,
    int objectType,
    QObject *component) {
  self->unregisterHandler(objectType, component);
}

//  QTextObjectInterface *QAbstractTextDocumentLayout::handlerForObject(int
//      objectType) const
extern "C" Q_DECL_EXPORT
QTextObjectInterface *ritual_ZNK27QAbstractTextDocumentLayout16handlerForObjectEi(
    const QAbstractTextDocumentLayout *self,
    int objectType) {
  return self->handlerForObject(objectType);
}

//  void QAbstractTextDocumentLayout::update(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout6updateERK6QRectF(
    QAbstractTextDocumentLayout *self,
    const QRectF *a0) {
  self->update(*a0);
}

//  void QAbstractTextDocumentLayout::updateBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout11updateBlockERK10QTextBlock(
    QAbstractTextDocumentLayout *self,
    const QTextBlock *block) {
  self->updateBlock(*block);
}

//  void QAbstractTextDocumentLayout::documentSizeChanged(const QSizeF
//      &newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout19documentSizeChangedERK6QSizeF(
    QAbstractTextDocumentLayout *self,
    const QSizeF *newSize) {
  self->documentSizeChanged(*newSize);
}

//  void QAbstractTextDocumentLayout::pageCountChanged(int newPages)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout16pageCountChangedEi(
    QAbstractTextDocumentLayout *self,
    int newPages) {
  self->pageCountChanged(newPages);
}

//  QAbstractTextDocumentLayout::QAbstractTextDocumentLayout(QAbstractTextDoc
//      umentLayoutPrivate &a0, QTextDocument *a1)
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZN27QAbstractTextDocumentLayoutC1ER34QAbstractTextDocumentLayoutPrivateP13QTextDocument(
    QAbstractTextDocumentLayoutPrivate *a0,
    QTextDocument *a1) {
  return new CuteQAbstractTextDocumentLayout(*a0, a1);
}

//  void QAbstractTextDocumentLayout::documentChanged(int from, int
//      charsRemoved, int charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout15documentChangedEiii(
    QAbstractTextDocumentLayout *self,
    int from,
    int charsRemoved,
    int charsAdded) {
  self->documentChanged(from, charsRemoved, charsAdded);
}

//  void QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject
//      item, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  self->resizeInlineObject(*item, posInDocument, *format);
}

//  void QAbstractTextDocumentLayout::positionInlineObject(QTextInlineObject
//      item, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout20positionInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  self->positionInlineObject(*item, posInDocument, *format);
}

//  void QAbstractTextDocumentLayout::drawInlineObject(QPainter *painter,
//      const QRectF &rect, QTextInlineObject object, int posInDocument,
//      const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRectF17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    QPainter *painter,
    const QRectF *rect,
    const QTextInlineObject *object,
    int posInDocument,
    const QTextFormat *format) {
  self->drawInlineObject(painter, *rect, *object, posInDocument, *format);
}

//  int QAbstractTextDocumentLayout::formatIndex(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QAbstractTextDocumentLayout11formatIndexEi(
    QAbstractTextDocumentLayout *self,
    int pos) {
  return self->formatIndex(pos);
}

//  QTextCharFormat QAbstractTextDocumentLayout::format(int pos)
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZN27QAbstractTextDocumentLayout6formatEi(
    QAbstractTextDocumentLayout *self,
    int pos) {
  return new QTextCharFormat(self->format(pos));
}

//  a Python function taken by a CuteQAbstractTextDocumentLayout, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractTextDocumentLayout(
    QAbstractTextDocumentLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractTextDocumentLayout *>(self)->take(key, call);
}

//  void QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject
//      item, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQAbstractTextDocumentLayout *>(self)->OwnQAbstractTextDocumentLayout::resizeInlineObject(
      *item,
      posInDocument,
      *format);
}

//  void QAbstractTextDocumentLayout::positionInlineObject(QTextInlineObject
//      item, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAbstractTextDocumentLayout20positionInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQAbstractTextDocumentLayout *>(self)->OwnQAbstractTextDocumentLayout::positionInlineObject(
      *item,
      posInDocument,
      *format);
}

//  void QAbstractTextDocumentLayout::drawInlineObject(QPainter *painter,
//      const QRectF &rect, QTextInlineObject object, int posInDocument,
//      const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRectF17QTextInlineObjectiRK11QTextFormat(
    QAbstractTextDocumentLayout *self,
    QPainter *painter,
    const QRectF *rect,
    const QTextInlineObject *object,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQAbstractTextDocumentLayout *>(self)->OwnQAbstractTextDocumentLayout::drawInlineObject(
      painter,
      *rect,
      *object,
      posInDocument,
      *format);
}
