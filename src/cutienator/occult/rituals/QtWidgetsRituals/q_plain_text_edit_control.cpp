//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplaintextedit_p.h"
#include <qfont.h>
#include <qpainter.h>
#include <qevent.h>
#include <qdebug.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qclipboard.h>
#include <qmath.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <qstyle.h>
#include "private/qapplication_p.h"
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "qtextlist.h"
#include "qaccessible.h"
#include <qtextformat.h>
#include <qdatetime.h>
#include <qapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qplaintextedit.cpp, line 601, as _ZNK21QPlainTextEditControl8anchorAtERK7QPointF
inline QString QPlainTextEditControl::anchorAt(const QPointF &pos) const
{
    return textEdit->anchorAt(pos.toPoint());
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 496, as _ZNK21QPlainTextEditControl17firstVisibleBlockEv
inline QTextBlock QPlainTextEditControl::firstVisibleBlock() const
{
    return document()->findBlockByNumber(topBlock);
}
//  -----------------------------------------------------------------------

//  A QPlainTextEditControl that Python can take functions over in. Every QPlainTextEditControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef void * (*CuteQPlainTextEditControlCall0)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef bool (*CuteQPlainTextEditControlCall1)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef void (*CuteQPlainTextEditControlCall2)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef int (*CuteQPlainTextEditControlCall3)(const void *, const QPointF *, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef const QRectF * (*CuteQPlainTextEditControlCall4)(const void *, const QTextBlock *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef QString * (*CuteQPlainTextEditControlCall5)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef void (*CuteQPlainTextEditControlCall6)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
typedef const QVariant * (*CuteQPlainTextEditControlCall7)(const void *, int, const QUrl *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQPlainTextEditControlCall8)(const void *, QEvent *, const QTransform *, QWidget *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef const QVariant * (*CuteQPlainTextEditControlCall9)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQPlainTextEditControlCall10)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
typedef bool (*CuteQPlainTextEditControlCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlainTextEditControlCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextEditControlCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextEditControlCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextEditControlCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlainTextEditControlCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlainTextEditControl : public QPlainTextEditControl {
public:
  using QPlainTextEditControl::QPlainTextEditControl;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl8anchorAtERK7QPointF")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl19ensureCursorVisibleEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl12loadResourceEiRK4QUrl")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransformP7QWidget")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  QMimeData *QPlainTextEditControl::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlainTextEditControlCall0 call = reinterpret_cast<CuteQPlainTextEditControlCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QPlainTextEditControl::createMimeDataFromSelection();
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  bool QPlainTextEditControl::canInsertFromMimeData(const QMimeData
  //      *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlainTextEditControlCall1 call = reinterpret_cast<CuteQPlainTextEditControlCall1>(taken[1]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QPlainTextEditControl::canInsertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  void QPlainTextEditControl::insertFromMimeData(const QMimeData
  //      *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlainTextEditControlCall2 call = reinterpret_cast<CuteQPlainTextEditControlCall2>(taken[2]);
      call(this, source, &handled);
      if (handled) return;
    }
    QPlainTextEditControl::insertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  int QPlainTextEditControl::hitTest(const QPointF &point,
  //      Qt::HitTestAccuracy a1) const
  int hitTest(const QPointF &point, Qt::HitTestAccuracy a1) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlainTextEditControlCall3 call = reinterpret_cast<CuteQPlainTextEditControlCall3>(taken[3]);
      int given = call(this, &point, static_cast<int>(a1), &handled);
      if (handled) return given;
    }
    return QPlainTextEditControl::hitTest(point, a1);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  QRectF QPlainTextEditControl::blockBoundingRect(const QTextBlock
  //      &block) const
  QRectF blockBoundingRect(const QTextBlock &block) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlainTextEditControlCall4 call = reinterpret_cast<CuteQPlainTextEditControlCall4>(taken[4]);
      const QRectF * given = call(this, &block, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextEditControl::blockBoundingRect(block);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  QString QPlainTextEditControl::anchorAt(const QPointF &pos) const
  QString anchorAt(const QPointF &pos) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlainTextEditControlCall5 call = reinterpret_cast<CuteQPlainTextEditControlCall5>(taken[5]);
      QString * given = call(this, &pos, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlainTextEditControl::anchorAt(pos);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  void QPlainTextEditControl::ensureCursorVisible()
  void ensureCursorVisible() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlainTextEditControlCall6 call = reinterpret_cast<CuteQPlainTextEditControlCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QPlainTextEditControl::ensureCursorVisible();
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(textedit)
  //  QVariant QPlainTextEditControl::loadResource(int type, const QUrl
  //      &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlainTextEditControlCall7 call = reinterpret_cast<CuteQPlainTextEditControlCall7>(taken[7]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextEditControl::loadResource(type, name);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  void QWidgetTextControl::processEvent(QEvent *e, const QTransform
  //      &transform, QWidget *contextWidget)
  void processEvent(
      QEvent *e,
      const QTransform &transform,
      QWidget *contextWidget) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlainTextEditControlCall8 call = reinterpret_cast<CuteQPlainTextEditControlCall8>(taken[8]);
      call(this, e, &transform, contextWidget, &handled);
      if (handled) return;
    }
    QWidgetTextControl::processEvent(e, transform, contextWidget);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  QVariant QWidgetTextControl::inputMethodQuery(Qt::InputMethodQuery
  //      property, QVariant argument) const
  QVariant inputMethodQuery(
      Qt::InputMethodQuery property,
      QVariant argument) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlainTextEditControlCall9 call = reinterpret_cast<CuteQPlainTextEditControlCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(property), &argument, &handled);
      if (handled && given) return *given;
    }
    return QWidgetTextControl::inputMethodQuery(property, argument);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
  //  void QWidgetTextControl::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlainTextEditControlCall10 call = reinterpret_cast<CuteQPlainTextEditControlCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QWidgetTextControl::timerEvent(e);
  }
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
  //  bool QWidgetTextControl::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlainTextEditControlCall11 call = reinterpret_cast<CuteQPlainTextEditControlCall11>(taken[11]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QWidgetTextControl::event(e);
  }
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlainTextEditControlCall12 call = reinterpret_cast<CuteQPlainTextEditControlCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlainTextEditControlCall13 call = reinterpret_cast<CuteQPlainTextEditControlCall13>(taken[13]);
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
      CuteQPlainTextEditControlCall14 call = reinterpret_cast<CuteQPlainTextEditControlCall14>(taken[14]);
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
      CuteQPlainTextEditControlCall15 call = reinterpret_cast<CuteQPlainTextEditControlCall15>(taken[15]);
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
      CuteQPlainTextEditControlCall16 call = reinterpret_cast<CuteQPlainTextEditControlCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlainTextEditControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlainTextEditControl10metaObjectEv(
    const QPlainTextEditControl *self) {
  return self->metaObject();
}

//  QString QPlainTextEditControl::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPlainTextEditControl8anchorAtERK7QPointF(
    const QPlainTextEditControl *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}

//  QRectF QPlainTextEditControl::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QPlainTextEditControl10cursorRectERK11QTextCursor(
    const QPlainTextEditControl *self,
    const QTextCursor *cursor) {
  return new QRectF(self->cursorRect(*cursor));
}

//  QRectF QPlainTextEditControl::cursorRect()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN21QPlainTextEditControl10cursorRectEv(
    QPlainTextEditControl *self) {
  return new QRectF(self->cursorRect());
}

//  void QPlainTextEditControl::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditControl19ensureCursorVisibleEv(
    QPlainTextEditControl *self) {
  self->ensureCursorVisible();
}

//  QTextBlock QPlainTextEditControl::firstVisibleBlock() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK21QPlainTextEditControl17firstVisibleBlockEv(
    const QPlainTextEditControl *self) {
  return new QTextBlock(self->firstVisibleBlock());
}

//  QVariant QPlainTextEditControl::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN21QPlainTextEditControl12loadResourceEiRK4QUrl(
    QPlainTextEditControl *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  a Python function taken by a CuteQPlainTextEditControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlainTextEditControl(
    QPlainTextEditControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlainTextEditControl *>(self)->take(key, call);
}

//  QString QPlainTextEditControl::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QPlainTextEditControl8anchorAtERK7QPointF(
    const QPlainTextEditControl *self,
    const QPointF *pos) {
  return new QString(self->QPlainTextEditControl::anchorAt(*pos));
}

//  void QPlainTextEditControl::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlainTextEditControl19ensureCursorVisibleEv(
    QPlainTextEditControl *self) {
  self->QPlainTextEditControl::ensureCursorVisible();
}

//  QVariant QPlainTextEditControl::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN21QPlainTextEditControl12loadResourceEiRK4QUrl(
    QPlainTextEditControl *self,
    int type,
    const QUrl *name) {
  return new QVariant(
      self->QPlainTextEditControl::loadResource(
          type,
          *name));
}

#endif  // QT_CONFIG(textedit)
