//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquicktextdocument.h>
#include <QtQuick/private/qquicktextdocument_p.h>
#include <QtQuick/private/qquicktextedit_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/quick/items/qquicktextdocument.cpp, line 594, as _ZN22QQuickTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11QTextFormat
inline QSizeF QQuickTextImageHandler::intrinsicSize(
        QTextDocument *doc, int, const QTextFormat &format)
{
    if (format.isImageFormat()) {
        QTextImageFormat imageFormat = format.toImageFormat();
        int width = qRound(qBound(qreal(INT_MIN), imageFormat.width(), qreal(INT_MAX)));
        const bool hasWidth = imageFormat.hasProperty(QTextFormat::ImageWidth) && width > 0;
        const int height = qRound(qBound(qreal(INT_MIN), imageFormat.height(), qreal(INT_MAX)));
        const bool hasHeight = imageFormat.hasProperty(QTextFormat::ImageHeight) && height > 0;
        const auto maxWidth = imageFormat.maximumWidth();
        const bool hasMaxWidth = imageFormat.hasProperty(QTextFormat::ImageMaxWidth) && maxWidth.type() != QTextLength::VariableLength;

        int effectiveMaxWidth = INT_MAX;
        if (hasMaxWidth) {
            if (maxWidth.type() == QTextLength::PercentageLength) {
                effectiveMaxWidth = (doc->pageSize().width() - 2 * doc->documentMargin()) * maxWidth.value(100) / 100;
            } else {
                effectiveMaxWidth = maxWidth.rawValue();
            }

            width = qMin(effectiveMaxWidth, width);
        }

        QSizeF size(width, height);
        if (!hasWidth || !hasHeight) {
            QVariant res = doc->resource(QTextDocument::ImageResource, QUrl(imageFormat.name()));
            QImage image = res.value<QImage>();
            if (image.isNull()) {
                // autotests expect us to reserve a 16x16 space for a "broken image" icon,
                // even though we don't actually display one
                if (!hasWidth)
                    size.setWidth(16);
                if (!hasHeight)
                    size.setHeight(16);
                return size;
            }
            QSize imgSize = image.size();
            if (imgSize.width()  > effectiveMaxWidth) {
                // image is bigger than effectiveMaxWidth, scale it down
                imgSize.setHeight(effectiveMaxWidth * imgSize.height() / (qreal) imgSize.width());
                imgSize.setWidth(effectiveMaxWidth);
            }

            if (!hasWidth) {
                if (!hasHeight)
                    size.setWidth(imgSize.width());
                else
                    size.setWidth(qMin(effectiveMaxWidth, qRound(height * (imgSize.width() / (qreal) imgSize.height()))));
            }
            if (!hasHeight) {
                if (!hasWidth)
                    size.setHeight(imgSize.height());
                else
                    size.setHeight(qRound(width * (imgSize.height() / (qreal) imgSize.width())));
            }
        }
        return size;
    }
    return QSizeF();
}
//  -----------------------------------------------------------------------

//  A QQuickTextImageHandler that Python can take functions over in. Every QQuickTextImageHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSizeF * (*CuteQQuickTextImageHandlerCall0)(const void *, QTextDocument *, int, const QTextFormat *, int *);
typedef void (*CuteQQuickTextImageHandlerCall1)(const void *, QPainter *, const QRectF *, QTextDocument *, int, const QTextFormat *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextImageHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextImageHandlerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextImageHandlerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextImageHandlerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextImageHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextImageHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextImageHandlerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextImageHandler : public QQuickTextImageHandler {
public:
  using QQuickTextImageHandler::QQuickTextImageHandler;
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

  //  QSizeF QQuickTextImageHandler::intrinsicSize(QTextDocument *doc, int
  //      posInDocument, const QTextFormat &format)
  QSizeF intrinsicSize(
      QTextDocument *doc,
      int posInDocument,
      const QTextFormat &format) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextImageHandlerCall0 call = reinterpret_cast<CuteQQuickTextImageHandlerCall0>(taken[0]);
      const QSizeF * given = call(this, doc, posInDocument, &format, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextImageHandler::intrinsicSize(doc, posInDocument, format);
  }

  //  void QQuickTextImageHandler::drawObject(QPainter *a0, const QRectF
  //      &a1, QTextDocument *a2, int a3, const QTextFormat &a4)
  void drawObject(
      QPainter *a0,
      const QRectF &a1,
      QTextDocument *a2,
      int a3,
      const QTextFormat &a4) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextImageHandlerCall1 call = reinterpret_cast<CuteQQuickTextImageHandlerCall1>(taken[1]);
      call(this, a0, &a1, a2, a3, &a4, &handled);
      if (handled) return;
    }
    QQuickTextImageHandler::drawObject(a0, a1, a2, a3, a4);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextImageHandlerCall2 call = reinterpret_cast<CuteQQuickTextImageHandlerCall2>(taken[2]);
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
      CuteQQuickTextImageHandlerCall3 call = reinterpret_cast<CuteQQuickTextImageHandlerCall3>(taken[3]);
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
      CuteQQuickTextImageHandlerCall4 call = reinterpret_cast<CuteQQuickTextImageHandlerCall4>(taken[4]);
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
      CuteQQuickTextImageHandlerCall5 call = reinterpret_cast<CuteQQuickTextImageHandlerCall5>(taken[5]);
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
      CuteQQuickTextImageHandlerCall6 call = reinterpret_cast<CuteQQuickTextImageHandlerCall6>(taken[6]);
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
      CuteQQuickTextImageHandlerCall7 call = reinterpret_cast<CuteQQuickTextImageHandlerCall7>(taken[7]);
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
      CuteQQuickTextImageHandlerCall8 call = reinterpret_cast<CuteQQuickTextImageHandlerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextImageHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickTextImageHandler10metaObjectEv(
    const QQuickTextImageHandler *self) {
  return self->metaObject();
}

//  void *QQuickTextImageHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickTextImageHandler11qt_metacastEPKc(
    QQuickTextImageHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextImageHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTextImageHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextImageHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickTextImageHandler::~QQuickTextImageHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextImageHandlerD1Ev(QQuickTextImageHandler *self) {
  delete self;
}

//  QSizeF QQuickTextImageHandler::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN22QQuickTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QQuickTextImageHandler *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(self->intrinsicSize(doc, posInDocument, *format));
}

//  void QQuickTextImageHandler::drawObject(QPainter *a0, const QRectF &a1,
//      QTextDocument *a2, int a3, const QTextFormat &a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextImageHandler10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QQuickTextImageHandler *self,
    QPainter *a0,
    const QRectF *a1,
    QTextDocument *a2,
    int a3,
    const QTextFormat *a4) {
  self->drawObject(a0, *a1, a2, a3, *a4);
}

//  QQuickTextImageHandler as the QTextObjectInterface it is built on
extern "C" Q_DECL_EXPORT
QTextObjectInterface *ritual_cast_QQuickTextImageHandler_QTextObjectInterface(
    QQuickTextImageHandler *self) {
  return static_cast<QTextObjectInterface *>(self);
}

//  a Python function taken by a CuteQQuickTextImageHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextImageHandler(
    QQuickTextImageHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextImageHandler *>(self)->take(key, call);
}

//  QSizeF QQuickTextImageHandler::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZN22QQuickTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QQuickTextImageHandler *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(
      self->QQuickTextImageHandler::intrinsicSize(
          doc,
          posInDocument,
          *format));
}

//  void QQuickTextImageHandler::drawObject(QPainter *a0, const QRectF &a1,
//      QTextDocument *a2, int a3, const QTextFormat &a4)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextImageHandler10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QQuickTextImageHandler *self,
    QPainter *a0,
    const QRectF *a1,
    QTextDocument *a2,
    int a3,
    const QTextFormat *a4) {
  self->QQuickTextImageHandler::drawObject(a0, *a1, a2, a3, *a4);
}
