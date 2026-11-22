//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsyntaxhighlighter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsyntaxhighlighter.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSyntaxHighlighter that Python can take functions over in. Every QSyntaxHighlighter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSyntaxHighlighterCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQSyntaxHighlighterCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSyntaxHighlighterCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSyntaxHighlighterCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQSyntaxHighlighterCall4)(const void *, QEvent *, int *);
typedef void (*CuteQSyntaxHighlighterCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSyntaxHighlighterCall6)(const void *, const QMetaMethod *, int *);
class CuteQSyntaxHighlighter : public QSyntaxHighlighter {
public:
  using QSyntaxHighlighter::QSyntaxHighlighter;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall0 call = reinterpret_cast<CuteQSyntaxHighlighterCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall1 call = reinterpret_cast<CuteQSyntaxHighlighterCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall2 call = reinterpret_cast<CuteQSyntaxHighlighterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall3 call = reinterpret_cast<CuteQSyntaxHighlighterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall4 call = reinterpret_cast<CuteQSyntaxHighlighterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall5 call = reinterpret_cast<CuteQSyntaxHighlighterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall6 call = reinterpret_cast<CuteQSyntaxHighlighterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSyntaxHighlighter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSyntaxHighlighter10metaObjectEv(
    const QSyntaxHighlighter *self) {
  return self->metaObject();
}

//  QString QSyntaxHighlighter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSyntaxHighlighter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSyntaxHighlighter::tr(s, c, n));
}

//  QSyntaxHighlighter::~QSyntaxHighlighter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighterD1Ev(QSyntaxHighlighter *self) {
  delete self;
}

//  void QSyntaxHighlighter::setDocument(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter11setDocumentEP13QTextDocument(
    QSyntaxHighlighter *self,
    QTextDocument *doc) {
  self->setDocument(doc);
}

//  QTextDocument *QSyntaxHighlighter::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK18QSyntaxHighlighter8documentEv(
    const QSyntaxHighlighter *self) {
  return self->document();
}

//  void QSyntaxHighlighter::rehighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter11rehighlightEv(QSyntaxHighlighter *self) {
  self->rehighlight();
}

//  void QSyntaxHighlighter::rehighlightBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter16rehighlightBlockERK10QTextBlock(
    QSyntaxHighlighter *self,
    const QTextBlock *block) {
  self->rehighlightBlock(*block);
}

//  a Python function taken by a CuteQSyntaxHighlighter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSyntaxHighlighter(
    QSyntaxHighlighter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSyntaxHighlighter *>(self)->take(key, call);
}
