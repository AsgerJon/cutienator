//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
#include <QtWidgets/qplaintextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextlayout.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPlainTextDocumentLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlainTextDocumentLayout : QPlainTextDocumentLayout {
  using QPlainTextDocumentLayout::documentChanged;
};

//  A QPlainTextDocumentLayout that Python can take functions over in. Every QPlainTextDocumentLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textedit)
typedef void (*CuteQPlainTextDocumentLayoutCall0)(const void *, QPainter *, const QAbstractTextDocumentLayout::PaintContext *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef int (*CuteQPlainTextDocumentLayoutCall1)(const void *, const QPointF *, int, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef int (*CuteQPlainTextDocumentLayoutCall2)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef const QSizeF * (*CuteQPlainTextDocumentLayoutCall3)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef const QRectF * (*CuteQPlainTextDocumentLayoutCall4)(const void *, QTextFrame *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef const QRectF * (*CuteQPlainTextDocumentLayoutCall5)(const void *, const QTextBlock *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQPlainTextDocumentLayoutCall6)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(textedit)
typedef void (*CuteQPlainTextDocumentLayoutCall7)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQPlainTextDocumentLayoutCall8)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQPlainTextDocumentLayoutCall9)(const void *, QPainter *, const QRectF *, const QTextInlineObject *, int, const QTextFormat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlainTextDocumentLayoutCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlainTextDocumentLayoutCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextDocumentLayoutCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextDocumentLayoutCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextDocumentLayoutCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextDocumentLayoutCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextDocumentLayoutCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlainTextDocumentLayout : public QPlainTextDocumentLayout {
public:
  using QPlainTextDocumentLayout::QPlainTextDocumentLayout;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12PaintContextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout9pageCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout12documentSizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTextFrame")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTextBlock")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN27QAbstractTextDocumentLayout15documentChangedEiii")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
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

#if QT_CONFIG(textedit)
  //  void QPlainTextDocumentLayout::draw(QPainter *a0, const PaintContext
  //      &a1)
  void draw(
      QPainter *a0,
      const QAbstractTextDocumentLayout::PaintContext &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall0 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall0>(taken[0]);
      call(this, a0, &a1, &handled);
      if (handled) return;
    }
    QPlainTextDocumentLayout::draw(a0, a1);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
  //      Qt::HitTestAccuracy a1) const
  int hitTest(const QPointF &a0, Qt::HitTestAccuracy a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall1 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall1>(taken[1]);
      int given = call(this, &a0, static_cast<int>(a1), &handled);
      if (handled) return given;
    }
    return QPlainTextDocumentLayout::hitTest(a0, a1);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  int QPlainTextDocumentLayout::pageCount() const
  int pageCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall2 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPlainTextDocumentLayout::pageCount();
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  QSizeF QPlainTextDocumentLayout::documentSize() const
  QSizeF documentSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall3 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall3>(taken[3]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextDocumentLayout::documentSize();
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame *a0)
  //      const
  QRectF frameBoundingRect(QTextFrame *a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall4 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall4>(taken[4]);
      const QRectF * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextDocumentLayout::frameBoundingRect(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  QRectF QPlainTextDocumentLayout::blockBoundingRect(const QTextBlock
  //      &block) const
  QRectF blockBoundingRect(const QTextBlock &block) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall5 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall5>(taken[5]);
      const QRectF * given = call(this, &block, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextDocumentLayout::blockBoundingRect(block);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QPlainTextDocumentLayout::documentChanged(int from, int a1, int
  //      charsAdded)
  void documentChanged(int from, int a1, int charsAdded) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall6 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall6>(taken[6]);
      call(this, from, a1, charsAdded, &handled);
      if (handled) return;
    }
    QPlainTextDocumentLayout::documentChanged(from, a1, charsAdded);
  }
#endif  // QT_CONFIG(textedit)

  //  void
  //      QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject
  //      item, int posInDocument, const QTextFormat &format)
  void resizeInlineObject(
      QTextInlineObject item,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlainTextDocumentLayoutCall7 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall7>(taken[7]);
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
      CuteQPlainTextDocumentLayoutCall8 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall8>(taken[8]);
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
      CuteQPlainTextDocumentLayoutCall9 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall9>(taken[9]);
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
      CuteQPlainTextDocumentLayoutCall10 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall10>(taken[10]);
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
      CuteQPlainTextDocumentLayoutCall11 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall11>(taken[11]);
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
      CuteQPlainTextDocumentLayoutCall12 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall12>(taken[12]);
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
      CuteQPlainTextDocumentLayoutCall13 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall13>(taken[13]);
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
      CuteQPlainTextDocumentLayoutCall14 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall14>(taken[14]);
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
      CuteQPlainTextDocumentLayoutCall15 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall15>(taken[15]);
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
      CuteQPlainTextDocumentLayoutCall16 call = reinterpret_cast<CuteQPlainTextDocumentLayoutCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlainTextDocumentLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPlainTextDocumentLayout10metaObjectEv(
    const QPlainTextDocumentLayout *self) {
  return self->metaObject();
}

//  QString QPlainTextDocumentLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPlainTextDocumentLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlainTextDocumentLayout::tr(s, c, n));
}

//  QPlainTextDocumentLayout::QPlainTextDocumentLayout(QTextDocument
//      *document)
extern "C" Q_DECL_EXPORT
QPlainTextDocumentLayout *ritual_ZN24QPlainTextDocumentLayoutC1EP13QTextDocument(
    QTextDocument *document) {
  return new CuteQPlainTextDocumentLayout(document);
}

//  QPlainTextDocumentLayout::~QPlainTextDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayoutD1Ev(
    QPlainTextDocumentLayout *self) {
  delete self;
}

//  void QPlainTextDocumentLayout::draw(QPainter *a0, const PaintContext &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDocumentLayout12PaintContextE(
    QPlainTextDocumentLayout *self,
    QPainter *a0,
    const QAbstractTextDocumentLayout::PaintContext *a1) {
  self->draw(a0, *a1);
}

//  int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
//      Qt::HitTestAccuracy a1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QPlainTextDocumentLayout *self,
    const QPointF *a0,
    Qt::HitTestAccuracy a1) {
  return self->hitTest(*a0, a1);
}

//  int QPlainTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout9pageCountEv(
    const QPlainTextDocumentLayout *self) {
  return self->pageCount();
}

//  QSizeF QPlainTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK24QPlainTextDocumentLayout12documentSizeEv(
    const QPlainTextDocumentLayout *self) {
  return new QSizeF(self->documentSize());
}

//  QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame *a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QPlainTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QPlainTextDocumentLayout *self,
    QTextFrame *a0) {
  return new QRectF(self->frameBoundingRect(a0));
}

//  QRectF QPlainTextDocumentLayout::blockBoundingRect(const QTextBlock
//      &block) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QPlainTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  void QPlainTextDocumentLayout::ensureBlockLayout(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QPlainTextDocumentLayout17ensureBlockLayoutERK10QTextBlock(
    const QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  self->ensureBlockLayout(*block);
}

//  void QPlainTextDocumentLayout::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout14setCursorWidthEi(
    QPlainTextDocumentLayout *self,
    int width) {
  self->setCursorWidth(width);
}

//  int QPlainTextDocumentLayout::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout11cursorWidthEv(
    const QPlainTextDocumentLayout *self) {
  return self->cursorWidth();
}

//  void QPlainTextDocumentLayout::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout13requestUpdateEv(
    QPlainTextDocumentLayout *self) {
  self->requestUpdate();
}

//  void QPlainTextDocumentLayout::documentChanged(int from, int a1, int
//      charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout15documentChangedEiii(
    QPlainTextDocumentLayout *self,
    int from,
    int a1,
    int charsAdded) {
  self->documentChanged(from, a1, charsAdded);
}

//  void QPlainTextDocumentLayout::setTextWidth(qreal newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout12setTextWidthEd(
    QPlainTextDocumentLayout *self,
    qreal newWidth) {
  self->setTextWidth(newWidth);
}

//  qreal QPlainTextDocumentLayout::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QPlainTextDocumentLayout9textWidthEv(
    const QPlainTextDocumentLayout *self) {
  return self->textWidth();
}

//  void QPlainTextDocumentLayout::layoutBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout11layoutBlockERK10QTextBlock(
    QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  self->layoutBlock(*block);
}

//  qreal QPlainTextDocumentLayout::blockWidth(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN24QPlainTextDocumentLayout10blockWidthERK10QTextBlock(
    QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  return self->blockWidth(*block);
}

//  a Python function taken by a CuteQPlainTextDocumentLayout, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlainTextDocumentLayout(
    QPlainTextDocumentLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlainTextDocumentLayout *>(self)->take(key, call);
}

//  void QPlainTextDocumentLayout::draw(QPainter *a0, const PaintContext &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QPlainTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDocumentLayout12PaintContextE(
    QPlainTextDocumentLayout *self,
    QPainter *a0,
    const QAbstractTextDocumentLayout::PaintContext *a1) {
  self->QPlainTextDocumentLayout::draw(a0, *a1);
}

//  int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
//      Qt::HitTestAccuracy a1) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QPlainTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QPlainTextDocumentLayout *self,
    const QPointF *a0,
    Qt::HitTestAccuracy a1) {
  return self->QPlainTextDocumentLayout::hitTest(*a0, a1);
}

//  int QPlainTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QPlainTextDocumentLayout9pageCountEv(
    const QPlainTextDocumentLayout *self) {
  return self->QPlainTextDocumentLayout::pageCount();
}

//  QSizeF QPlainTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK24QPlainTextDocumentLayout12documentSizeEv(
    const QPlainTextDocumentLayout *self) {
  return new QSizeF(self->QPlainTextDocumentLayout::documentSize());
}

//  QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame *a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK24QPlainTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QPlainTextDocumentLayout *self,
    QTextFrame *a0) {
  return new QRectF(self->QPlainTextDocumentLayout::frameBoundingRect(a0));
}

//  QRectF QPlainTextDocumentLayout::blockBoundingRect(const QTextBlock
//      &block) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK24QPlainTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(
      self->QPlainTextDocumentLayout::blockBoundingRect(
          *block));
}

//  void QPlainTextDocumentLayout::documentChanged(int from, int a1, int
//      charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QPlainTextDocumentLayout15documentChangedEiii(
    QPlainTextDocumentLayout *self,
    int from,
    int a1,
    int charsAdded) {
  static_cast<OwnQPlainTextDocumentLayout *>(self)->OwnQPlainTextDocumentLayout::documentChanged(
      from,
      a1,
      charsAdded);
}

#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(textedit)
