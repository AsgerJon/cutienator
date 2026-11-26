//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qsize.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qpalette.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtWidgets/QTextEdit>

//  Only a class built on QWidgetTextControl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWidgetTextControl : QWidgetTextControl {
  using QWidgetTextControl::timerEvent;
  using QWidgetTextControl::event;
};

//  A QWidgetTextControl that Python can take functions over in. Every QWidgetTextControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQWidgetTextControlCall0)(const void *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef const QVariant * (*CuteQWidgetTextControlCall1)(const void *, int, const QUrl *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef QString * (*CuteQWidgetTextControlCall2)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef int (*CuteQWidgetTextControlCall3)(const void *, const QPointF *, int, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef const QRectF * (*CuteQWidgetTextControlCall4)(const void *, const QTextBlock *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQWidgetTextControlCall5)(const void *, QEvent *, const QTransform *, QWidget *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef const QVariant * (*CuteQWidgetTextControlCall6)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef void * (*CuteQWidgetTextControlCall7)(const void *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef bool (*CuteQWidgetTextControlCall8)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQWidgetTextControlCall9)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
typedef void (*CuteQWidgetTextControlCall10)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
typedef bool (*CuteQWidgetTextControlCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(widgettextcontrol)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWidgetTextControlCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetTextControlCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetTextControlCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetTextControlCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetTextControlCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWidgetTextControl : public QWidgetTextControl {
public:
  using QWidgetTextControl::QWidgetTextControl;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl19ensureCursorVisibleEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl12loadResourceEiRK4QUrl")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl8anchorAtERK7QPointF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransformP7QWidget")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
    if (!std::strcmp(key, "_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData")) {
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
  //  void QWidgetTextControl::ensureCursorVisible()
  void ensureCursorVisible() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetTextControlCall0 call = reinterpret_cast<CuteQWidgetTextControlCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetTextControl::ensureCursorVisible();
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  QVariant QWidgetTextControl::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetTextControlCall1 call = reinterpret_cast<CuteQWidgetTextControlCall1>(taken[1]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QWidgetTextControl::loadResource(type, name);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  QString QWidgetTextControl::anchorAt(const QPointF &pos) const
  QString anchorAt(const QPointF &pos) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetTextControlCall2 call = reinterpret_cast<CuteQWidgetTextControlCall2>(taken[2]);
      QString * given = call(this, &pos, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QWidgetTextControl::anchorAt(pos);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  int QWidgetTextControl::hitTest(const QPointF &point,
  //      Qt::HitTestAccuracy accuracy) const
  int hitTest(
      const QPointF &point,
      Qt::HitTestAccuracy accuracy) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetTextControlCall3 call = reinterpret_cast<CuteQWidgetTextControlCall3>(taken[3]);
      int given = call(this, &point, static_cast<int>(accuracy), &handled);
      if (handled) return given;
    }
    return QWidgetTextControl::hitTest(point, accuracy);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  QRectF QWidgetTextControl::blockBoundingRect(const QTextBlock &block)
  //      const
  QRectF blockBoundingRect(const QTextBlock &block) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetTextControlCall4 call = reinterpret_cast<CuteQWidgetTextControlCall4>(taken[4]);
      const QRectF * given = call(this, &block, &handled);
      if (handled && given) return *given;
    }
    return QWidgetTextControl::blockBoundingRect(block);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  void QWidgetTextControl::processEvent(QEvent *e, const QTransform
  //      &transform, QWidget *contextWidget)
  void processEvent(
      QEvent *e,
      const QTransform &transform,
      QWidget *contextWidget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetTextControlCall5 call = reinterpret_cast<CuteQWidgetTextControlCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetTextControlCall6 call = reinterpret_cast<CuteQWidgetTextControlCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(property), &argument, &handled);
      if (handled && given) return *given;
    }
    return QWidgetTextControl::inputMethodQuery(property, argument);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  QMimeData *QWidgetTextControl::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetTextControlCall7 call = reinterpret_cast<CuteQWidgetTextControlCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QWidgetTextControl::createMimeDataFromSelection();
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  bool QWidgetTextControl::canInsertFromMimeData(const QMimeData
  //      *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetTextControlCall8 call = reinterpret_cast<CuteQWidgetTextControlCall8>(taken[8]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QWidgetTextControl::canInsertFromMimeData(source);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if QT_CONFIG(widgettextcontrol)
  //  void QWidgetTextControl::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetTextControlCall9 call = reinterpret_cast<CuteQWidgetTextControlCall9>(taken[9]);
      call(this, source, &handled);
      if (handled) return;
    }
    QWidgetTextControl::insertFromMimeData(source);
  }
#endif  // QT_CONFIG(widgettextcontrol)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(widgettextcontrol)
  //  void QWidgetTextControl::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetTextControlCall10 call = reinterpret_cast<CuteQWidgetTextControlCall10>(taken[10]);
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
      CuteQWidgetTextControlCall11 call = reinterpret_cast<CuteQWidgetTextControlCall11>(taken[11]);
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
      CuteQWidgetTextControlCall12 call = reinterpret_cast<CuteQWidgetTextControlCall12>(taken[12]);
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
      CuteQWidgetTextControlCall13 call = reinterpret_cast<CuteQWidgetTextControlCall13>(taken[13]);
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
      CuteQWidgetTextControlCall14 call = reinterpret_cast<CuteQWidgetTextControlCall14>(taken[14]);
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
      CuteQWidgetTextControlCall15 call = reinterpret_cast<CuteQWidgetTextControlCall15>(taken[15]);
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
      CuteQWidgetTextControlCall16 call = reinterpret_cast<CuteQWidgetTextControlCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWidgetTextControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWidgetTextControl10metaObjectEv(
    const QWidgetTextControl *self) {
  return self->metaObject();
}

//  void *QWidgetTextControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QWidgetTextControl11qt_metacastEPKc(
    QWidgetTextControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWidgetTextControl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWidgetTextControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QWidgetTextControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWidgetTextControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWidgetTextControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWidgetTextControl::tr(s, c, n));
}

//  QWidgetTextControlPrivate *QWidgetTextControl::d_func()
extern "C" Q_DECL_EXPORT
QWidgetTextControlPrivate *ritual_ZN18QWidgetTextControl6d_funcEv(
    QWidgetTextControl *self) {
  return self->d_func();
}

//  const QWidgetTextControlPrivate *QWidgetTextControl::d_func() const
extern "C" Q_DECL_EXPORT
const QWidgetTextControlPrivate *ritual_ZNK18QWidgetTextControl6d_funcEv(
    const QWidgetTextControl *self) {
  return self->d_func();
}

//  QWidgetTextControl::QWidgetTextControl(QObject *parent)
extern "C" Q_DECL_EXPORT
QWidgetTextControl *ritual_ZN18QWidgetTextControlC1EP7QObject(
    QObject *parent) {
  return new CuteQWidgetTextControl(parent);
}

//  QWidgetTextControl::QWidgetTextControl(const QString &text, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWidgetTextControl *ritual_ZN18QWidgetTextControlC1ERK7QStringP7QObject(
    const QString *text,
    QObject *parent) {
  return new CuteQWidgetTextControl(*text, parent);
}

//  QWidgetTextControl::QWidgetTextControl(QTextDocument *doc, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWidgetTextControl *ritual_ZN18QWidgetTextControlC1EP13QTextDocumentP7QObject(
    QTextDocument *doc,
    QObject *parent) {
  return new CuteQWidgetTextControl(doc, parent);
}

//  QWidgetTextControl::~QWidgetTextControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControlD1Ev(QWidgetTextControl *self) {
  delete self;
}

//  void QWidgetTextControl::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl11setDocumentEP13QTextDocument(
    QWidgetTextControl *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QWidgetTextControl::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK18QWidgetTextControl8documentEv(
    const QWidgetTextControl *self) {
  return self->document();
}

//  void QWidgetTextControl::setTextCursor(const QTextCursor &cursor, bool
//      selectionClipboard)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13setTextCursorERK11QTextCursorb(
    QWidgetTextControl *self,
    const QTextCursor *cursor,
    bool selectionClipboard) {
  self->setTextCursor(*cursor, selectionClipboard);
}

//  QTextCursor QWidgetTextControl::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK18QWidgetTextControl10textCursorEv(
    const QWidgetTextControl *self) {
  return new QTextCursor(self->textCursor());
}

//  void QWidgetTextControl::setTextInteractionFlags(Qt::TextInteractionFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QWidgetTextControl *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QWidgetTextControl::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetTextControl20textInteractionFlagsEv(
    const QWidgetTextControl *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QWidgetTextControl::mergeCurrentCharFormat(const QTextCharFormat
//      &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl22mergeCurrentCharFormatERK15QTextCharFormat(
    QWidgetTextControl *self,
    const QTextCharFormat *modifier) {
  self->mergeCurrentCharFormat(*modifier);
}

//  void QWidgetTextControl::setCurrentCharFormat(const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl20setCurrentCharFormatERK15QTextCharFormat(
    QWidgetTextControl *self,
    const QTextCharFormat *format) {
  self->setCurrentCharFormat(*format);
}

//  QTextCharFormat QWidgetTextControl::currentCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK18QWidgetTextControl17currentCharFormatEv(
    const QWidgetTextControl *self) {
  return new QTextCharFormat(self->currentCharFormat());
}

//  bool QWidgetTextControl::find(const QString &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl4findERK7QString6QFlagsIN13QTextDocument8FindFlagEE(
    QWidgetTextControl *self,
    const QString *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

#if QT_CONFIG(regularexpression)
//  bool QWidgetTextControl::find(const QRegularExpression &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl4findERK18QRegularExpression6QFlagsIN13QTextDocument8FindFlagEE(
    QWidgetTextControl *self,
    const QRegularExpression *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}
#endif  // QT_CONFIG(regularexpression)

//  QString QWidgetTextControl::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetTextControl11toPlainTextEv(
    const QWidgetTextControl *self) {
  return new QString(self->toPlainText());
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  QString QWidgetTextControl::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetTextControl6toHtmlEv(
    const QWidgetTextControl *self) {
  return new QString(self->toHtml());
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(textmarkdownwriter)
//  QString QWidgetTextControl::toMarkdown(QTextDocument::MarkdownFeatures
//      features) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetTextControl10toMarkdownE6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    const QWidgetTextControl *self,
    int features) {
  return new QString(
      self->toMarkdown(
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}
#endif  // QT_CONFIG(textmarkdownwriter)

//  void QWidgetTextControl::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl19ensureCursorVisibleEv(
    QWidgetTextControl *self) {
  self->ensureCursorVisible();
}

//  QVariant QWidgetTextControl::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18QWidgetTextControl12loadResourceEiRK4QUrl(
    QWidgetTextControl *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

#if !defined(QT_NO_CONTEXTMENU)
//  QMenu *QWidgetTextControl::createStandardContextMenu(const QPointF &pos,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN18QWidgetTextControl25createStandardContextMenuERK7QPointFP7QWidget(
    QWidgetTextControl *self,
    const QPointF *pos,
    QWidget *parent) {
  return self->createStandardContextMenu(*pos, parent);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  QTextCursor QWidgetTextControl::cursorForPosition(const QPointF &pos)
//      const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK18QWidgetTextControl17cursorForPositionERK7QPointF(
    const QWidgetTextControl *self,
    const QPointF *pos) {
  return new QTextCursor(self->cursorForPosition(*pos));
}

//  QRectF QWidgetTextControl::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QWidgetTextControl10cursorRectERK11QTextCursor(
    const QWidgetTextControl *self,
    const QTextCursor *cursor) {
  return new QRectF(self->cursorRect(*cursor));
}

//  QRectF QWidgetTextControl::cursorRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QWidgetTextControl10cursorRectEv(
    const QWidgetTextControl *self) {
  return new QRectF(self->cursorRect());
}

//  QRectF QWidgetTextControl::selectionRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QWidgetTextControl13selectionRectERK11QTextCursor(
    const QWidgetTextControl *self,
    const QTextCursor *cursor) {
  return new QRectF(self->selectionRect(*cursor));
}

//  QRectF QWidgetTextControl::selectionRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QWidgetTextControl13selectionRectEv(
    const QWidgetTextControl *self) {
  return new QRectF(self->selectionRect());
}

//  QString QWidgetTextControl::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetTextControl8anchorAtERK7QPointF(
    const QWidgetTextControl *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}

//  QPointF QWidgetTextControl::anchorPosition(const QString &name) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QWidgetTextControl14anchorPositionERK7QString(
    const QWidgetTextControl *self,
    const QString *name) {
  return new QPointF(self->anchorPosition(*name));
}

//  QString QWidgetTextControl::anchorAtCursor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetTextControl14anchorAtCursorEv(
    const QWidgetTextControl *self) {
  return new QString(self->anchorAtCursor());
}

//  QTextBlock QWidgetTextControl::blockWithMarkerAt(const QPointF &pos)
//      const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK18QWidgetTextControl17blockWithMarkerAtERK7QPointF(
    const QWidgetTextControl *self,
    const QPointF *pos) {
  return new QTextBlock(self->blockWithMarkerAt(*pos));
}

//  bool QWidgetTextControl::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl13overwriteModeEv(
    const QWidgetTextControl *self) {
  return self->overwriteMode();
}

//  void QWidgetTextControl::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl16setOverwriteModeEb(
    QWidgetTextControl *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  int QWidgetTextControl::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetTextControl11cursorWidthEv(
    const QWidgetTextControl *self) {
  return self->cursorWidth();
}

//  void QWidgetTextControl::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl14setCursorWidthEi(
    QWidgetTextControl *self,
    int width) {
  self->setCursorWidth(width);
}

//  bool QWidgetTextControl::acceptRichText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl14acceptRichTextEv(
    const QWidgetTextControl *self) {
  return self->acceptRichText();
}

//  void QWidgetTextControl::setAcceptRichText(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl17setAcceptRichTextEb(
    QWidgetTextControl *self,
    bool accept) {
  self->setAcceptRichText(accept);
}

#if QT_CONFIG(textedit)
//  void QWidgetTextControl::setExtraSelections(const
//      QList<QTextEdit::ExtraSelection> &selections)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl18setExtraSelectionsERK5QListIN9QTextEdit14ExtraSelectionEE(
    QWidgetTextControl *self,
    const QList<QTextEdit::ExtraSelection> *selections) {
  self->setExtraSelections(*selections);
}
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
//  QList<QTextEdit::ExtraSelection> QWidgetTextControl::extraSelections()
//      const
extern "C" Q_DECL_EXPORT
QList<QTextEdit::ExtraSelection> *ritual_ZNK18QWidgetTextControl15extraSelectionsEv(
    const QWidgetTextControl *self) {
  return new QList<QTextEdit::ExtraSelection>(self->extraSelections());
}
#endif  // QT_CONFIG(textedit)

//  void QWidgetTextControl::setTextWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl12setTextWidthEd(
    QWidgetTextControl *self,
    qreal width) {
  self->setTextWidth(width);
}

//  qreal QWidgetTextControl::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWidgetTextControl9textWidthEv(
    const QWidgetTextControl *self) {
  return self->textWidth();
}

//  QSizeF QWidgetTextControl::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18QWidgetTextControl4sizeEv(
    const QWidgetTextControl *self) {
  return new QSizeF(self->size());
}

//  void QWidgetTextControl::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl20setOpenExternalLinksEb(
    QWidgetTextControl *self,
    bool open) {
  self->setOpenExternalLinks(open);
}

//  bool QWidgetTextControl::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl17openExternalLinksEv(
    const QWidgetTextControl *self) {
  return self->openExternalLinks();
}

//  void QWidgetTextControl::setIgnoreUnusedNavigationEvents(bool ignore)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl31setIgnoreUnusedNavigationEventsEb(
    QWidgetTextControl *self,
    bool ignore) {
  self->setIgnoreUnusedNavigationEvents(ignore);
}

//  bool QWidgetTextControl::ignoreUnusedNavigationEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl28ignoreUnusedNavigationEventsEv(
    const QWidgetTextControl *self) {
  return self->ignoreUnusedNavigationEvents();
}

//  void QWidgetTextControl::moveCursor(QTextCursor::MoveOperation op,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10moveCursorEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QWidgetTextControl *self,
    QTextCursor::MoveOperation op,
    QTextCursor::MoveMode mode) {
  self->moveCursor(op, mode);
}

//  bool QWidgetTextControl::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl8canPasteEv(
    const QWidgetTextControl *self) {
  return self->canPaste();
}

//  void QWidgetTextControl::setCursorIsFocusIndicator(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl25setCursorIsFocusIndicatorEb(
    QWidgetTextControl *self,
    bool b) {
  self->setCursorIsFocusIndicator(b);
}

//  bool QWidgetTextControl::cursorIsFocusIndicator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl22cursorIsFocusIndicatorEv(
    const QWidgetTextControl *self) {
  return self->cursorIsFocusIndicator();
}

//  void QWidgetTextControl::setDragEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl14setDragEnabledEb(
    QWidgetTextControl *self,
    bool enabled) {
  self->setDragEnabled(enabled);
}

//  bool QWidgetTextControl::isDragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl13isDragEnabledEv(
    const QWidgetTextControl *self) {
  return self->isDragEnabled();
}

//  bool QWidgetTextControl::isWordSelectionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl22isWordSelectionEnabledEv(
    const QWidgetTextControl *self) {
  return self->isWordSelectionEnabled();
}

//  void QWidgetTextControl::setWordSelectionEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl23setWordSelectionEnabledEb(
    QWidgetTextControl *self,
    bool enabled) {
  self->setWordSelectionEnabled(enabled);
}

//  bool QWidgetTextControl::isPreediting()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl12isPreeditingEv(
    QWidgetTextControl *self) {
  return self->isPreediting();
}

//  void QWidgetTextControl::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QWidgetTextControl5printEP17QPagedPaintDevice(
    const QWidgetTextControl *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  int QWidgetTextControl::hitTest(const QPointF &point, Qt::HitTestAccuracy
//      accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QWidgetTextControl *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->hitTest(*point, accuracy);
}

//  QRectF QWidgetTextControl::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock(
    const QWidgetTextControl *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  QAbstractTextDocumentLayout::PaintContext
//      QWidgetTextControl::getPaintContext(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout::PaintContext *ritual_ZNK18QWidgetTextControl15getPaintContextEP7QWidget(
    const QWidgetTextControl *self,
    QWidget *widget) {
  return new QAbstractTextDocumentLayout::PaintContext(
      self->getPaintContext(
          widget));
}

//  void QWidgetTextControl::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl12setPlainTextERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->setPlainText(*text);
}

#if QT_CONFIG(textmarkdownreader)
//  void QWidgetTextControl::setMarkdown(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl11setMarkdownERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->setMarkdown(*text);
}
#endif  // QT_CONFIG(textmarkdownreader)

//  void QWidgetTextControl::setHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl7setHtmlERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->setHtml(*text);
}

#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetTextControl::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl3cutEv(QWidgetTextControl *self) {
  self->cut();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetTextControl::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl4copyEv(QWidgetTextControl *self) {
  self->copy();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetTextControl::paste(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl5pasteEN10QClipboard4ModeE(
    QWidgetTextControl *self,
    QClipboard::Mode mode) {
  self->paste(mode);
}
#endif  // !defined(QT_NO_CLIPBOARD)

//  void QWidgetTextControl::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl4undoEv(QWidgetTextControl *self) {
  self->undo();
}

//  void QWidgetTextControl::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl4redoEv(QWidgetTextControl *self) {
  self->redo();
}

//  void QWidgetTextControl::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl5clearEv(QWidgetTextControl *self) {
  self->clear();
}

//  void QWidgetTextControl::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl9selectAllEv(QWidgetTextControl *self) {
  self->selectAll();
}

//  void QWidgetTextControl::insertPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl15insertPlainTextERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->insertPlainText(*text);
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QWidgetTextControl::insertHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10insertHtmlERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->insertHtml(*text);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  void QWidgetTextControl::append(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl6appendERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->append(*text);
}

//  void QWidgetTextControl::appendHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10appendHtmlERK7QString(
    QWidgetTextControl *self,
    const QString *html) {
  self->appendHtml(*html);
}

//  void QWidgetTextControl::appendPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl15appendPlainTextERK7QString(
    QWidgetTextControl *self,
    const QString *text) {
  self->appendPlainText(*text);
}

//  void QWidgetTextControl::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10adjustSizeEv(QWidgetTextControl *self) {
  self->adjustSize();
}

//  void QWidgetTextControl::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl11textChangedEv(QWidgetTextControl *self) {
  self->textChanged();
}

//  void QWidgetTextControl::undoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13undoAvailableEb(
    QWidgetTextControl *self,
    bool b) {
  self->undoAvailable(b);
}

//  void QWidgetTextControl::redoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13redoAvailableEb(
    QWidgetTextControl *self,
    bool b) {
  self->redoAvailable(b);
}

//  void QWidgetTextControl::currentCharFormatChanged(const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl24currentCharFormatChangedERK15QTextCharFormat(
    QWidgetTextControl *self,
    const QTextCharFormat *format) {
  self->currentCharFormatChanged(*format);
}

//  void QWidgetTextControl::copyAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13copyAvailableEb(
    QWidgetTextControl *self,
    bool b) {
  self->copyAvailable(b);
}

//  void QWidgetTextControl::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl16selectionChangedEv(
    QWidgetTextControl *self) {
  self->selectionChanged();
}

//  void QWidgetTextControl::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl21cursorPositionChangedEv(
    QWidgetTextControl *self) {
  self->cursorPositionChanged();
}

//  void QWidgetTextControl::updateRequest(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13updateRequestERK6QRectF(
    QWidgetTextControl *self,
    const QRectF *rect) {
  self->updateRequest(*rect);
}

//  void QWidgetTextControl::documentSizeChanged(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl19documentSizeChangedERK6QSizeF(
    QWidgetTextControl *self,
    const QSizeF *a0) {
  self->documentSizeChanged(*a0);
}

//  void QWidgetTextControl::blockCountChanged(int newBlockCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl17blockCountChangedEi(
    QWidgetTextControl *self,
    int newBlockCount) {
  self->blockCountChanged(newBlockCount);
}

//  void QWidgetTextControl::visibilityRequest(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl17visibilityRequestERK6QRectF(
    QWidgetTextControl *self,
    const QRectF *rect) {
  self->visibilityRequest(*rect);
}

//  void QWidgetTextControl::microFocusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl17microFocusChangedEv(
    QWidgetTextControl *self) {
  self->microFocusChanged();
}

//  void QWidgetTextControl::linkActivated(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl13linkActivatedERK7QString(
    QWidgetTextControl *self,
    const QString *link) {
  self->linkActivated(*link);
}

//  void QWidgetTextControl::linkHovered(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl11linkHoveredERK7QString(
    QWidgetTextControl *self,
    const QString *a0) {
  self->linkHovered(*a0);
}

//  void QWidgetTextControl::blockMarkerHovered(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl18blockMarkerHoveredERK10QTextBlock(
    QWidgetTextControl *self,
    const QTextBlock *block) {
  self->blockMarkerHovered(*block);
}

//  void QWidgetTextControl::modificationChanged(bool m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl19modificationChangedEb(
    QWidgetTextControl *self,
    bool m) {
  self->modificationChanged(m);
}

//  QPalette QWidgetTextControl::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK18QWidgetTextControl7paletteEv(
    const QWidgetTextControl *self) {
  return new QPalette(self->palette());
}

//  void QWidgetTextControl::setPalette(const QPalette &pal)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10setPaletteERK8QPalette(
    QWidgetTextControl *self,
    const QPalette *pal) {
  self->setPalette(*pal);
}

//  void QWidgetTextControl::processEvent(QEvent *e, const QTransform
//      &transform, QWidget *contextWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransformP7QWidget(
    QWidgetTextControl *self,
    QEvent *e,
    const QTransform *transform,
    QWidget *contextWidget) {
  self->processEvent(e, *transform, contextWidget);
}

//  void QWidgetTextControl::processEvent(QEvent *e, const QPointF
//      &coordinateOffset, QWidget *contextWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl12processEventEP6QEventRK7QPointFP7QWidget(
    QWidgetTextControl *self,
    QEvent *e,
    const QPointF *coordinateOffset,
    QWidget *contextWidget) {
  self->processEvent(e, *coordinateOffset, contextWidget);
}

//  void QWidgetTextControl::drawContents(QPainter *painter, const QRectF
//      &rect, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl12drawContentsEP8QPainterRK6QRectFP7QWidget(
    QWidgetTextControl *self,
    QPainter *painter,
    const QRectF *rect,
    QWidget *widget) {
  self->drawContents(painter, *rect, widget);
}

//  void QWidgetTextControl::setFocus(bool focus, Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl8setFocusEbN2Qt11FocusReasonE(
    QWidgetTextControl *self,
    bool focus,
    Qt::FocusReason a1) {
  self->setFocus(focus, a1);
}

//  QVariant QWidgetTextControl::inputMethodQuery(Qt::InputMethodQuery
//      property, QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QWidgetTextControl *self,
    Qt::InputMethodQuery property,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(property, *argument));
}

//  QMimeData *QWidgetTextControl::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv(
    const QWidgetTextControl *self) {
  return self->createMimeDataFromSelection();
}

//  bool QWidgetTextControl::canInsertFromMimeData(const QMimeData *source)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData(
    const QWidgetTextControl *self,
    const QMimeData *source) {
  return self->canInsertFromMimeData(source);
}

//  void QWidgetTextControl::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData(
    QWidgetTextControl *self,
    const QMimeData *source) {
  self->insertFromMimeData(source);
}

//  bool QWidgetTextControl::setFocusToAnchor(const QTextCursor &newCursor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl16setFocusToAnchorERK11QTextCursor(
    QWidgetTextControl *self,
    const QTextCursor *newCursor) {
  return self->setFocusToAnchor(*newCursor);
}

//  bool QWidgetTextControl::setFocusToNextOrPreviousAnchor(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl30setFocusToNextOrPreviousAnchorEb(
    QWidgetTextControl *self,
    bool next) {
  return self->setFocusToNextOrPreviousAnchor(next);
}

//  bool QWidgetTextControl::findNextPrevAnchor(const QTextCursor &from, bool
//      next, QTextCursor &newAnchor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl18findNextPrevAnchorERK11QTextCursorbRS0_(
    QWidgetTextControl *self,
    const QTextCursor *from,
    bool next,
    QTextCursor *newAnchor) {
  return self->findNextPrevAnchor(*from, next, *newAnchor);
}

//  void QWidgetTextControl::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetTextControl10timerEventEP11QTimerEvent(
    QWidgetTextControl *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  bool QWidgetTextControl::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetTextControl5eventEP6QEvent(
    QWidgetTextControl *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQWidgetTextControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetTextControl(
    QWidgetTextControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetTextControl *>(self)->take(key, call);
}

//  void QWidgetTextControl::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWidgetTextControl19ensureCursorVisibleEv(
    QWidgetTextControl *self) {
  self->QWidgetTextControl::ensureCursorVisible();
}

//  QVariant QWidgetTextControl::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN18QWidgetTextControl12loadResourceEiRK4QUrl(
    QWidgetTextControl *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->QWidgetTextControl::loadResource(type, *name));
}

//  QString QWidgetTextControl::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QWidgetTextControl8anchorAtERK7QPointF(
    const QWidgetTextControl *self,
    const QPointF *pos) {
  return new QString(self->QWidgetTextControl::anchorAt(*pos));
}

//  int QWidgetTextControl::hitTest(const QPointF &point, Qt::HitTestAccuracy
//      accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QWidgetTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QWidgetTextControl *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->QWidgetTextControl::hitTest(*point, accuracy);
}

//  QRectF QWidgetTextControl::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK18QWidgetTextControl17blockBoundingRectERK10QTextBlock(
    const QWidgetTextControl *self,
    const QTextBlock *block) {
  return new QRectF(self->QWidgetTextControl::blockBoundingRect(*block));
}

//  void QWidgetTextControl::processEvent(QEvent *e, const QTransform
//      &transform, QWidget *contextWidget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWidgetTextControl12processEventEP6QEventRK10QTransformP7QWidget(
    QWidgetTextControl *self,
    QEvent *e,
    const QTransform *transform,
    QWidget *contextWidget) {
  self->QWidgetTextControl::processEvent(e, *transform, contextWidget);
}

//  QVariant QWidgetTextControl::inputMethodQuery(Qt::InputMethodQuery
//      property, QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QWidgetTextControl16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QWidgetTextControl *self,
    Qt::InputMethodQuery property,
    const QVariant *argument) {
  return new QVariant(
      self->QWidgetTextControl::inputMethodQuery(
          property,
          *argument));
}

//  QMimeData *QWidgetTextControl::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_own_ZNK18QWidgetTextControl27createMimeDataFromSelectionEv(
    const QWidgetTextControl *self) {
  return self->QWidgetTextControl::createMimeDataFromSelection();
}

//  bool QWidgetTextControl::canInsertFromMimeData(const QMimeData *source)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QWidgetTextControl21canInsertFromMimeDataEPK9QMimeData(
    const QWidgetTextControl *self,
    const QMimeData *source) {
  return self->QWidgetTextControl::canInsertFromMimeData(source);
}

//  void QWidgetTextControl::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWidgetTextControl18insertFromMimeDataEPK9QMimeData(
    QWidgetTextControl *self,
    const QMimeData *source) {
  self->QWidgetTextControl::insertFromMimeData(source);
}

//  void QWidgetTextControl::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWidgetTextControl10timerEventEP11QTimerEvent(
    QWidgetTextControl *self,
    QTimerEvent *e) {
  static_cast<OwnQWidgetTextControl *>(self)->OwnQWidgetTextControl::timerEvent(
      e);
}

//  bool QWidgetTextControl::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QWidgetTextControl5eventEP6QEvent(
    QWidgetTextControl *self,
    QEvent *e) {
  return static_cast<OwnQWidgetTextControl *>(self)->OwnQWidgetTextControl::event(
      e);
}

//  a QList<QTextEdit::ExtraSelection> a ritual of QWidgetTextControl gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWidgetTextControl__QList_QTextEdit_ExtraSelection(
    QList<QTextEdit::ExtraSelection> *self) {
  delete self;
}

#endif  // QT_CONFIG(widgettextcontrol)
#endif  // QT_CONFIG(widgettextcontrol)
