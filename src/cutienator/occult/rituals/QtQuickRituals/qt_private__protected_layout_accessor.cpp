//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtPrivate::ProtectedLayoutAccessor that Python can take functions over in. Every QtPrivate::ProtectedLayoutAccessor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall0)(const void *, QPainter *, const QAbstractTextDocumentLayout::PaintContext *, int *);
typedef int (*CuteQtPrivate_ProtectedLayoutAccessorCall1)(const void *, const QPointF *, int, int *);
typedef int (*CuteQtPrivate_ProtectedLayoutAccessorCall2)(const void *, int *);
typedef const QSizeF * (*CuteQtPrivate_ProtectedLayoutAccessorCall3)(const void *, int *);
typedef const QRectF * (*CuteQtPrivate_ProtectedLayoutAccessorCall4)(const void *, QTextFrame *, int *);
typedef const QRectF * (*CuteQtPrivate_ProtectedLayoutAccessorCall5)(const void *, const QTextBlock *, int *);
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall6)(const void *, int, int, int, int *);
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall7)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall8)(const void *, const QTextInlineObject *, int, const QTextFormat *, int *);
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall9)(const void *, QPainter *, const QRectF *, const QTextInlineObject *, int, const QTextFormat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPrivate_ProtectedLayoutAccessorCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPrivate_ProtectedLayoutAccessorCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPrivate_ProtectedLayoutAccessorCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtPrivate_ProtectedLayoutAccessor : public QtPrivate::ProtectedLayoutAccessor {
public:
  using QtPrivate::ProtectedLayoutAccessor::ProtectedLayoutAccessor;
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
      CuteQtPrivate_ProtectedLayoutAccessorCall0 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall0>(taken[0]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall1 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall1>(taken[1]);
      int given = call(this, &point, static_cast<int>(accuracy), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractTextDocumentLayout::pageCount() const
  int pageCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtPrivate_ProtectedLayoutAccessorCall2 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSizeF QAbstractTextDocumentLayout::documentSize() const
  QSizeF documentSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtPrivate_ProtectedLayoutAccessorCall3 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall3>(taken[3]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall4 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall4>(taken[4]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall5 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall5>(taken[5]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall6 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall6>(taken[6]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall7 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall7>(taken[7]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall8 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall8>(taken[8]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall9 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall9>(taken[9]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall10 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall10>(taken[10]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall11 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall11>(taken[11]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall12 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall12>(taken[12]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall13 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall13>(taken[13]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall14 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall14>(taken[14]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall15 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall15>(taken[15]);
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
      CuteQtPrivate_ProtectedLayoutAccessorCall16 call = reinterpret_cast<CuteQtPrivate_ProtectedLayoutAccessorCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QTextCharFormat QtPrivate::ProtectedLayoutAccessor::formatAccessor(int
//      pos)
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZN9QtPrivate23ProtectedLayoutAccessor14formatAccessorEi(
    QtPrivate::ProtectedLayoutAccessor *self,
    int pos) {
  return new QTextCharFormat(self->formatAccessor(pos));
}

//  a Python function taken by a CuteQtPrivate_ProtectedLayoutAccessor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtPrivate_ProtectedLayoutAccessor(
    QtPrivate::ProtectedLayoutAccessor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtPrivate_ProtectedLayoutAccessor *>(self)->take(key, call);
}
