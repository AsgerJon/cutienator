//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsyntaxhighlighter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_SYNTAXHIGHLIGHTER)
#include <QtGui/qsyntaxhighlighter.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSyntaxHighlighter that Python can take functions over in. Every QSyntaxHighlighter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SYNTAXHIGHLIGHTER)
typedef void (*CuteQSyntaxHighlighterCall0)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_SYNTAXHIGHLIGHTER)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSyntaxHighlighterCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSyntaxHighlighterCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSyntaxHighlighterCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSyntaxHighlighterCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSyntaxHighlighterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSyntaxHighlighterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSyntaxHighlighterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSyntaxHighlighter : public QSyntaxHighlighter {
public:
  using QSyntaxHighlighter::QSyntaxHighlighter;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SYNTAXHIGHLIGHTER)
    if (!std::strcmp(key, "_ZN18QSyntaxHighlighter14highlightBlockERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SYNTAXHIGHLIGHTER)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_SYNTAXHIGHLIGHTER)
  //  void QSyntaxHighlighter::highlightBlock(const QString &text)
  void highlightBlock(const QString &text) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall0 call = reinterpret_cast<CuteQSyntaxHighlighterCall0>(taken[0]);
      call(this, &text, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_SYNTAXHIGHLIGHTER)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall1 call = reinterpret_cast<CuteQSyntaxHighlighterCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall2 call = reinterpret_cast<CuteQSyntaxHighlighterCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall3 call = reinterpret_cast<CuteQSyntaxHighlighterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall4 call = reinterpret_cast<CuteQSyntaxHighlighterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall5 call = reinterpret_cast<CuteQSyntaxHighlighterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall6 call = reinterpret_cast<CuteQSyntaxHighlighterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSyntaxHighlighterCall7 call = reinterpret_cast<CuteQSyntaxHighlighterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
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

//  void QSyntaxHighlighter::highlightBlock(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter14highlightBlockERK7QString(
    QSyntaxHighlighter *self,
    const QString *text) {
  self->highlightBlock(*text);
}

//  void QSyntaxHighlighter::setFormat(int start, int count, const
//      QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter9setFormatEiiRK15QTextCharFormat(
    QSyntaxHighlighter *self,
    int start,
    int count,
    const QTextCharFormat *format) {
  self->setFormat(start, count, *format);
}

//  void QSyntaxHighlighter::setFormat(int start, int count, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter9setFormatEiiRK6QColor(
    QSyntaxHighlighter *self,
    int start,
    int count,
    const QColor *color) {
  self->setFormat(start, count, *color);
}

//  void QSyntaxHighlighter::setFormat(int start, int count, const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter9setFormatEiiRK5QFont(
    QSyntaxHighlighter *self,
    int start,
    int count,
    const QFont *font) {
  self->setFormat(start, count, *font);
}

//  QTextCharFormat QSyntaxHighlighter::format(int pos) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK18QSyntaxHighlighter6formatEi(
    const QSyntaxHighlighter *self,
    int pos) {
  return new QTextCharFormat(self->format(pos));
}

//  int QSyntaxHighlighter::previousBlockState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSyntaxHighlighter18previousBlockStateEv(
    const QSyntaxHighlighter *self) {
  return self->previousBlockState();
}

//  int QSyntaxHighlighter::currentBlockState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSyntaxHighlighter17currentBlockStateEv(
    const QSyntaxHighlighter *self) {
  return self->currentBlockState();
}

//  void QSyntaxHighlighter::setCurrentBlockState(int newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter20setCurrentBlockStateEi(
    QSyntaxHighlighter *self,
    int newState) {
  self->setCurrentBlockState(newState);
}

//  void QSyntaxHighlighter::setCurrentBlockUserData(QTextBlockUserData
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter23setCurrentBlockUserDataEP18QTextBlockUserData(
    QSyntaxHighlighter *self,
    QTextBlockUserData *data) {
  self->setCurrentBlockUserData(data);
}

//  QTextBlockUserData *QSyntaxHighlighter::currentBlockUserData() const
extern "C" Q_DECL_EXPORT
QTextBlockUserData *ritual_ZNK18QSyntaxHighlighter20currentBlockUserDataEv(
    const QSyntaxHighlighter *self) {
  return self->currentBlockUserData();
}

//  QTextBlock QSyntaxHighlighter::currentBlock() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK18QSyntaxHighlighter12currentBlockEv(
    const QSyntaxHighlighter *self) {
  return new QTextBlock(self->currentBlock());
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

#endif  // !defined(QT_NO_SYNTAXHIGHLIGHTER)
