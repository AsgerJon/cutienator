//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextimagehandler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextimagehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTextImageHandler that Python can take functions over in. Every QTextImageHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSizeF * (*CuteQTextImageHandlerCall0)(const void *, QTextDocument *, int, const QTextFormat *, int *);
typedef void (*CuteQTextImageHandlerCall1)(const void *, QPainter *, const QRectF *, QTextDocument *, int, const QTextFormat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextImageHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextImageHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextImageHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextImageHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextImageHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextImageHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextImageHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextImageHandler : public QTextImageHandler {
public:
  using QTextImageHandler::QTextImageHandler;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK11QTextFormat")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSizeF QTextImageHandler::intrinsicSize(QTextDocument *doc, int
  //      posInDocument, const QTextFormat &format)
  QSizeF intrinsicSize(
      QTextDocument *doc,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextImageHandlerCall0 call = reinterpret_cast<CuteQTextImageHandlerCall0>(taken[0]);
      const QSizeF * given = call(this, doc, posInDocument, &format, &handled);
      if (handled && given) return *given;
    }
    return QTextImageHandler::intrinsicSize(doc, posInDocument, format);
  }

  //  void QTextImageHandler::drawObject(QPainter *p, const QRectF &rect,
  //      QTextDocument *doc, int posInDocument, const QTextFormat &format)
  void drawObject(
      QPainter *p,
      const QRectF &rect,
      QTextDocument *doc,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextImageHandlerCall1 call = reinterpret_cast<CuteQTextImageHandlerCall1>(taken[1]);
      call(this, p, &rect, doc, posInDocument, &format, &handled);
      if (handled) return;
    }
    QTextImageHandler::drawObject(p, rect, doc, posInDocument, format);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextImageHandlerCall2 call = reinterpret_cast<CuteQTextImageHandlerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextImageHandlerCall3 call = reinterpret_cast<CuteQTextImageHandlerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextImageHandlerCall4 call = reinterpret_cast<CuteQTextImageHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextImageHandlerCall5 call = reinterpret_cast<CuteQTextImageHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextImageHandlerCall6 call = reinterpret_cast<CuteQTextImageHandlerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextImageHandlerCall7 call = reinterpret_cast<CuteQTextImageHandlerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextImageHandlerCall8 call = reinterpret_cast<CuteQTextImageHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextImageHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QTextImageHandler10metaObjectEv(
    const QTextImageHandler *self) {
  return self->metaObject();
}

//  QString QTextImageHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QTextImageHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextImageHandler::tr(s, c, n));
}

//  QTextImageHandler::QTextImageHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QTextImageHandler *ritual_ZN17QTextImageHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQTextImageHandler(parent);
}

//  QSizeF QTextImageHandler::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN17QTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QTextImageHandler *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(self->intrinsicSize(doc, posInDocument, *format));
}

//  void QTextImageHandler::drawObject(QPainter *p, const QRectF &rect,
//      QTextDocument *doc, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextImageHandler10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QTextImageHandler *self,
    QPainter *p,
    const QRectF *rect,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  self->drawObject(p, *rect, doc, posInDocument, *format);
}

//  QImage QTextImageHandler::image(QTextDocument *doc, const
//      QTextImageFormat &imageFormat)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN17QTextImageHandler5imageEP13QTextDocumentRK16QTextImageFormat(
    QTextImageHandler *self,
    QTextDocument *doc,
    const QTextImageFormat *imageFormat) {
  return new QImage(self->image(doc, *imageFormat));
}

//  QTextImageHandler as the QTextObjectInterface it is built on
extern "C" Q_DECL_EXPORT
QTextObjectInterface *ritual_cast_QTextImageHandler_QTextObjectInterface(
    QTextImageHandler *self) {
  return static_cast<QTextObjectInterface *>(self);
}

//  a Python function taken by a CuteQTextImageHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextImageHandler(
    QTextImageHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextImageHandler *>(self)->take(key, call);
}

//  QSizeF QTextImageHandler::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZN17QTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QTextImageHandler *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(
      self->QTextImageHandler::intrinsicSize(
          doc,
          posInDocument,
          *format));
}

//  void QTextImageHandler::drawObject(QPainter *p, const QRectF &rect,
//      QTextDocument *doc, int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTextImageHandler10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QTextImageHandler *self,
    QPainter *p,
    const QRectF *rect,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  self->QTextImageHandler::drawObject(p, *rect, doc, posInDocument, *format);
}
