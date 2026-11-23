//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextdocument.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qregularexpression.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextoption.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTextDocument may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextDocument : QTextDocument {
  using QTextDocument::createObject;
  using QTextDocument::loadResource;
};

//  A QTextDocument that Python can take functions over in. Every QTextDocument
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextDocumentCall0)(const void *, int *);
typedef void * (*CuteQTextDocumentCall1)(const void *, const QTextFormat *, int *);
typedef const QVariant * (*CuteQTextDocumentCall2)(const void *, int, const QUrl *, int *);
typedef bool (*CuteQTextDocumentCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQTextDocumentCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTextDocumentCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTextDocumentCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQTextDocumentCall7)(const void *, QEvent *, int *);
typedef void (*CuteQTextDocumentCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTextDocumentCall9)(const void *, const QMetaMethod *, int *);
class CuteQTextDocument : public QTextDocument {
public:
  using QTextDocument::QTextDocument;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QTextDocument5clearEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QTextDocument12createObjectERK11QTextFormat")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QTextDocument12loadResourceEiRK4QUrl")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QTextDocument::clear()
  void clear() override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextDocumentCall0 call = reinterpret_cast<CuteQTextDocumentCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QTextDocument::clear();
  }

  //  QTextObject *QTextDocument::createObject(const QTextFormat &f)
  QTextObject *createObject(const QTextFormat &f) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextDocumentCall1 call = reinterpret_cast<CuteQTextDocumentCall1>(taken[1]);
      void * given = call(this, &f, &handled);
      if (handled) return static_cast<QTextObject *>(given);
    }
    return QTextDocument::createObject(f);
  }

  //  QVariant QTextDocument::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextDocumentCall2 call = reinterpret_cast<CuteQTextDocumentCall2>(taken[2]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QTextDocument::loadResource(type, name);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextDocumentCall3 call = reinterpret_cast<CuteQTextDocumentCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextDocumentCall4 call = reinterpret_cast<CuteQTextDocumentCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextDocumentCall5 call = reinterpret_cast<CuteQTextDocumentCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextDocumentCall6 call = reinterpret_cast<CuteQTextDocumentCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextDocumentCall7 call = reinterpret_cast<CuteQTextDocumentCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextDocumentCall8 call = reinterpret_cast<CuteQTextDocumentCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextDocumentCall9 call = reinterpret_cast<CuteQTextDocumentCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTextDocument::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QTextDocument10metaObjectEv(
    const QTextDocument *self) {
  return self->metaObject();
}

//  QString QTextDocument::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QTextDocument2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextDocument::tr(s, c, n));
}

//  QTextDocument::QTextDocument(QObject *parent)
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZN13QTextDocumentC1EP7QObject(QObject *parent) {
  return new CuteQTextDocument(parent);
}

//  QTextDocument::QTextDocument(const QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZN13QTextDocumentC1ERK7QStringP7QObject(
    const QString *text,
    QObject *parent) {
  return new CuteQTextDocument(*text, parent);
}

//  QTextDocument::~QTextDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocumentD1Ev(QTextDocument *self) {
  delete self;
}

//  QTextDocument *QTextDocument::clone(QObject *parent) const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK13QTextDocument5cloneEP7QObject(
    const QTextDocument *self,
    QObject *parent) {
  return self->clone(parent);
}

//  bool QTextDocument::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument7isEmptyEv(const QTextDocument *self) {
  return self->isEmpty();
}

//  void QTextDocument::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument5clearEv(QTextDocument *self) {
  self->clear();
}

//  void QTextDocument::setUndoRedoEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument18setUndoRedoEnabledEb(
    QTextDocument *self,
    bool enable) {
  self->setUndoRedoEnabled(enable);
}

//  bool QTextDocument::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument17isUndoRedoEnabledEv(
    const QTextDocument *self) {
  return self->isUndoRedoEnabled();
}

//  bool QTextDocument::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument15isUndoAvailableEv(
    const QTextDocument *self) {
  return self->isUndoAvailable();
}

//  bool QTextDocument::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument15isRedoAvailableEv(
    const QTextDocument *self) {
  return self->isRedoAvailable();
}

//  int QTextDocument::availableUndoSteps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument18availableUndoStepsEv(
    const QTextDocument *self) {
  return self->availableUndoSteps();
}

//  int QTextDocument::availableRedoSteps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument18availableRedoStepsEv(
    const QTextDocument *self) {
  return self->availableRedoSteps();
}

//  int QTextDocument::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument8revisionEv(const QTextDocument *self) {
  return self->revision();
}

//  void QTextDocument::setDocumentLayout(QAbstractTextDocumentLayout
//      *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument17setDocumentLayoutEP27QAbstractTextDocumentLayout(
    QTextDocument *self,
    QAbstractTextDocumentLayout *layout) {
  self->setDocumentLayout(layout);
}

//  QAbstractTextDocumentLayout *QTextDocument::documentLayout() const
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZNK13QTextDocument14documentLayoutEv(
    const QTextDocument *self) {
  return self->documentLayout();
}

//  void QTextDocument::setMetaInformation(MetaInformation info, const
//      QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument18setMetaInformationENS_15MetaInformationERK7QString(
    QTextDocument *self,
    QTextDocument::MetaInformation info,
    const QString *a1) {
  self->setMetaInformation(info, *a1);
}

//  QString QTextDocument::metaInformation(MetaInformation info) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument15metaInformationENS_15MetaInformationE(
    const QTextDocument *self,
    QTextDocument::MetaInformation info) {
  return new QString(self->metaInformation(info));
}

//  QString QTextDocument::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument6toHtmlEv(const QTextDocument *self) {
  return new QString(self->toHtml());
}

//  void QTextDocument::setHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument7setHtmlERK7QString(
    QTextDocument *self,
    const QString *html) {
  self->setHtml(*html);
}

//  QString QTextDocument::toMarkdown(MarkdownFeatures features) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument10toMarkdownE6QFlagsINS_15MarkdownFeatureEE(
    const QTextDocument *self,
    int features) {
  return new QString(
      self->toMarkdown(
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}

//  void QTextDocument::setMarkdown(const QString &markdown, MarkdownFeatures
//      features)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument11setMarkdownERK7QString6QFlagsINS_15MarkdownFeatureEE(
    QTextDocument *self,
    const QString *markdown,
    int features) {
  self->setMarkdown(
      *markdown,
      QFlags<QTextDocument::MarkdownFeature>::fromInt(features));
}

//  QString QTextDocument::toRawText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument9toRawTextEv(const QTextDocument *self) {
  return new QString(self->toRawText());
}

//  QString QTextDocument::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument11toPlainTextEv(
    const QTextDocument *self) {
  return new QString(self->toPlainText());
}

//  void QTextDocument::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument12setPlainTextERK7QString(
    QTextDocument *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  QChar QTextDocument::characterAt(int pos) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK13QTextDocument11characterAtEi(
    const QTextDocument *self,
    int pos) {
  return new QChar(self->characterAt(pos));
}

//  QTextCursor QTextDocument::find(const QString &subString, int from,
//      FindFlags options) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK13QTextDocument4findERK7QStringi6QFlagsINS_8FindFlagEE(
    const QTextDocument *self,
    const QString *subString,
    int from,
    int options) {
  return new QTextCursor(
      self->find(
          *subString,
          from,
          QFlags<QTextDocument::FindFlag>::fromInt(options)));
}

//  QTextCursor QTextDocument::find(const QString &subString, const
//      QTextCursor &cursor, FindFlags options) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK13QTextDocument4findERK7QStringRK11QTextCursor6QFlagsINS_8FindFlagEE(
    const QTextDocument *self,
    const QString *subString,
    const QTextCursor *cursor,
    int options) {
  return new QTextCursor(
      self->find(
          *subString,
          *cursor,
          QFlags<QTextDocument::FindFlag>::fromInt(options)));
}

//  QTextCursor QTextDocument::find(const QRegularExpression &expr, int from,
//      FindFlags options) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK13QTextDocument4findERK18QRegularExpressioni6QFlagsINS_8FindFlagEE(
    const QTextDocument *self,
    const QRegularExpression *expr,
    int from,
    int options) {
  return new QTextCursor(
      self->find(
          *expr,
          from,
          QFlags<QTextDocument::FindFlag>::fromInt(options)));
}

//  QTextCursor QTextDocument::find(const QRegularExpression &expr, const
//      QTextCursor &cursor, FindFlags options) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK13QTextDocument4findERK18QRegularExpressionRK11QTextCursor6QFlagsINS_8FindFlagEE(
    const QTextDocument *self,
    const QRegularExpression *expr,
    const QTextCursor *cursor,
    int options) {
  return new QTextCursor(
      self->find(
          *expr,
          *cursor,
          QFlags<QTextDocument::FindFlag>::fromInt(options)));
}

//  QTextFrame *QTextDocument::frameAt(int pos) const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK13QTextDocument7frameAtEi(
    const QTextDocument *self,
    int pos) {
  return self->frameAt(pos);
}

//  QTextFrame *QTextDocument::rootFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK13QTextDocument9rootFrameEv(
    const QTextDocument *self) {
  return self->rootFrame();
}

//  QTextObject *QTextDocument::object(int objectIndex) const
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZNK13QTextDocument6objectEi(
    const QTextDocument *self,
    int objectIndex) {
  return self->object(objectIndex);
}

//  QTextObject *QTextDocument::objectForFormat(const QTextFormat &a0) const
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZNK13QTextDocument15objectForFormatERK11QTextFormat(
    const QTextDocument *self,
    const QTextFormat *a0) {
  return self->objectForFormat(*a0);
}

//  QTextBlock QTextDocument::findBlock(int pos) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument9findBlockEi(
    const QTextDocument *self,
    int pos) {
  return new QTextBlock(self->findBlock(pos));
}

//  QTextBlock QTextDocument::findBlockByNumber(int blockNumber) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument17findBlockByNumberEi(
    const QTextDocument *self,
    int blockNumber) {
  return new QTextBlock(self->findBlockByNumber(blockNumber));
}

//  QTextBlock QTextDocument::findBlockByLineNumber(int blockNumber) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument21findBlockByLineNumberEi(
    const QTextDocument *self,
    int blockNumber) {
  return new QTextBlock(self->findBlockByLineNumber(blockNumber));
}

//  QTextBlock QTextDocument::begin() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument5beginEv(const QTextDocument *self) {
  return new QTextBlock(self->begin());
}

//  QTextBlock QTextDocument::end() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument3endEv(const QTextDocument *self) {
  return new QTextBlock(self->end());
}

//  QTextBlock QTextDocument::firstBlock() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument10firstBlockEv(
    const QTextDocument *self) {
  return new QTextBlock(self->firstBlock());
}

//  QTextBlock QTextDocument::lastBlock() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK13QTextDocument9lastBlockEv(
    const QTextDocument *self) {
  return new QTextBlock(self->lastBlock());
}

//  void QTextDocument::setPageSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument11setPageSizeERK6QSizeF(
    QTextDocument *self,
    const QSizeF *size) {
  self->setPageSize(*size);
}

//  QSizeF QTextDocument::pageSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK13QTextDocument8pageSizeEv(const QTextDocument *self) {
  return new QSizeF(self->pageSize());
}

//  void QTextDocument::setDefaultFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument14setDefaultFontERK5QFont(
    QTextDocument *self,
    const QFont *font) {
  self->setDefaultFont(*font);
}

//  QFont QTextDocument::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QTextDocument11defaultFontEv(const QTextDocument *self) {
  return new QFont(self->defaultFont());
}

//  void QTextDocument::setSuperScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument22setSuperScriptBaselineEd(
    QTextDocument *self,
    qreal baseline) {
  self->setSuperScriptBaseline(baseline);
}

//  qreal QTextDocument::superScriptBaseline() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument19superScriptBaselineEv(
    const QTextDocument *self) {
  return self->superScriptBaseline();
}

//  void QTextDocument::setSubScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument20setSubScriptBaselineEd(
    QTextDocument *self,
    qreal baseline) {
  self->setSubScriptBaseline(baseline);
}

//  qreal QTextDocument::subScriptBaseline() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument17subScriptBaselineEv(
    const QTextDocument *self) {
  return self->subScriptBaseline();
}

//  void QTextDocument::setBaselineOffset(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument17setBaselineOffsetEd(
    QTextDocument *self,
    qreal baseline) {
  self->setBaselineOffset(baseline);
}

//  qreal QTextDocument::baselineOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument14baselineOffsetEv(
    const QTextDocument *self) {
  return self->baselineOffset();
}

//  int QTextDocument::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument9pageCountEv(const QTextDocument *self) {
  return self->pageCount();
}

//  bool QTextDocument::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument10isModifiedEv(const QTextDocument *self) {
  return self->isModified();
}

//  void QTextDocument::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QTextDocument5printEP17QPagedPaintDevice(
    const QTextDocument *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  QVariant QTextDocument::resource(int type, const QUrl &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QTextDocument8resourceEiRK4QUrl(
    const QTextDocument *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->resource(type, *name));
}

//  void QTextDocument::addResource(int type, const QUrl &name, const
//      QVariant &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument11addResourceEiRK4QUrlRK8QVariant(
    QTextDocument *self,
    int type,
    const QUrl *name,
    const QVariant *resource) {
  self->addResource(type, *name, *resource);
}

//  QList<QTextFormat> QTextDocument::allFormats() const
extern "C" Q_DECL_EXPORT
QList<QTextFormat> *ritual_ZNK13QTextDocument10allFormatsEv(
    const QTextDocument *self) {
  return new QList<QTextFormat>(self->allFormats());
}

//  void QTextDocument::markContentsDirty(int from, int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument17markContentsDirtyEii(
    QTextDocument *self,
    int from,
    int length) {
  self->markContentsDirty(from, length);
}

//  void QTextDocument::setUseDesignMetrics(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument19setUseDesignMetricsEb(
    QTextDocument *self,
    bool b) {
  self->setUseDesignMetrics(b);
}

//  bool QTextDocument::useDesignMetrics() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument16useDesignMetricsEv(
    const QTextDocument *self) {
  return self->useDesignMetrics();
}

//  void QTextDocument::setLayoutEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument16setLayoutEnabledEb(
    QTextDocument *self,
    bool b) {
  self->setLayoutEnabled(b);
}

//  bool QTextDocument::isLayoutEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextDocument15isLayoutEnabledEv(
    const QTextDocument *self) {
  return self->isLayoutEnabled();
}

//  void QTextDocument::drawContents(QPainter *painter, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument12drawContentsEP8QPainterRK6QRectF(
    QTextDocument *self,
    QPainter *painter,
    const QRectF *rect) {
  self->drawContents(painter, *rect);
}

//  void QTextDocument::setTextWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument12setTextWidthEd(
    QTextDocument *self,
    qreal width) {
  self->setTextWidth(width);
}

//  qreal QTextDocument::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument9textWidthEv(const QTextDocument *self) {
  return self->textWidth();
}

//  qreal QTextDocument::idealWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument10idealWidthEv(const QTextDocument *self) {
  return self->idealWidth();
}

//  qreal QTextDocument::indentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument11indentWidthEv(const QTextDocument *self) {
  return self->indentWidth();
}

//  void QTextDocument::setIndentWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument14setIndentWidthEd(
    QTextDocument *self,
    qreal width) {
  self->setIndentWidth(width);
}

//  qreal QTextDocument::documentMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QTextDocument14documentMarginEv(
    const QTextDocument *self) {
  return self->documentMargin();
}

//  void QTextDocument::setDocumentMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument17setDocumentMarginEd(
    QTextDocument *self,
    qreal margin) {
  self->setDocumentMargin(margin);
}

//  void QTextDocument::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument10adjustSizeEv(QTextDocument *self) {
  self->adjustSize();
}

//  QSizeF QTextDocument::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK13QTextDocument4sizeEv(const QTextDocument *self) {
  return new QSizeF(self->size());
}

//  int QTextDocument::blockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument10blockCountEv(const QTextDocument *self) {
  return self->blockCount();
}

//  int QTextDocument::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument9lineCountEv(const QTextDocument *self) {
  return self->lineCount();
}

//  int QTextDocument::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument14characterCountEv(const QTextDocument *self) {
  return self->characterCount();
}

//  void QTextDocument::setDefaultStyleSheet(const QString &sheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument20setDefaultStyleSheetERK7QString(
    QTextDocument *self,
    const QString *sheet) {
  self->setDefaultStyleSheet(*sheet);
}

//  QString QTextDocument::defaultStyleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextDocument17defaultStyleSheetEv(
    const QTextDocument *self) {
  return new QString(self->defaultStyleSheet());
}

//  void QTextDocument::undo(QTextCursor *cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument4undoEP11QTextCursor(
    QTextDocument *self,
    QTextCursor *cursor) {
  self->undo(cursor);
}

//  void QTextDocument::redo(QTextCursor *cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument4redoEP11QTextCursor(
    QTextDocument *self,
    QTextCursor *cursor) {
  self->redo(cursor);
}

//  void QTextDocument::clearUndoRedoStacks(Stacks historyToClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument19clearUndoRedoStacksENS_6StacksE(
    QTextDocument *self,
    QTextDocument::Stacks historyToClear) {
  self->clearUndoRedoStacks(historyToClear);
}

//  int QTextDocument::maximumBlockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextDocument17maximumBlockCountEv(
    const QTextDocument *self) {
  return self->maximumBlockCount();
}

//  void QTextDocument::setMaximumBlockCount(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument20setMaximumBlockCountEi(
    QTextDocument *self,
    int maximum) {
  self->setMaximumBlockCount(maximum);
}

//  QTextOption QTextDocument::defaultTextOption() const
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZNK13QTextDocument17defaultTextOptionEv(
    const QTextDocument *self) {
  return new QTextOption(self->defaultTextOption());
}

//  void QTextDocument::setDefaultTextOption(const QTextOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument20setDefaultTextOptionERK11QTextOption(
    QTextDocument *self,
    const QTextOption *option) {
  self->setDefaultTextOption(*option);
}

//  QUrl QTextDocument::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QTextDocument7baseUrlEv(const QTextDocument *self) {
  return new QUrl(self->baseUrl());
}

//  void QTextDocument::setBaseUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument10setBaseUrlERK4QUrl(
    QTextDocument *self,
    const QUrl *url) {
  self->setBaseUrl(*url);
}

//  Qt::CursorMoveStyle QTextDocument::defaultCursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK13QTextDocument22defaultCursorMoveStyleEv(
    const QTextDocument *self) {
  return self->defaultCursorMoveStyle();
}

//  void QTextDocument::setDefaultCursorMoveStyle(Qt::CursorMoveStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument25setDefaultCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QTextDocument *self,
    Qt::CursorMoveStyle style) {
  self->setDefaultCursorMoveStyle(style);
}

//  void QTextDocument::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument4undoEv(QTextDocument *self) {
  self->undo();
}

//  void QTextDocument::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument4redoEv(QTextDocument *self) {
  self->redo();
}

//  void QTextDocument::appendUndoItem(QAbstractUndoItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument14appendUndoItemEP17QAbstractUndoItem(
    QTextDocument *self,
    QAbstractUndoItem *a0) {
  self->appendUndoItem(a0);
}

//  void QTextDocument::setModified(bool m)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextDocument11setModifiedEb(QTextDocument *self, bool m) {
  self->setModified(m);
}

//  QTextObject *QTextDocument::createObject(const QTextFormat &f)
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZN13QTextDocument12createObjectERK11QTextFormat(
    QTextDocument *self,
    const QTextFormat *f) {
  return self->createObject(*f);
}

//  QVariant QTextDocument::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN13QTextDocument12loadResourceEiRK4QUrl(
    QTextDocument *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  a Python function taken by a CuteQTextDocument, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextDocument(
    QTextDocument *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextDocument *>(self)->take(key, call);
}

//  void QTextDocument::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QTextDocument5clearEv(QTextDocument *self) {
  self->QTextDocument::clear();
}

//  QTextObject *QTextDocument::createObject(const QTextFormat &f)
extern "C" Q_DECL_EXPORT
QTextObject *ritual_own_ZN13QTextDocument12createObjectERK11QTextFormat(
    QTextDocument *self,
    const QTextFormat *f) {
  return static_cast<OwnQTextDocument *>(self)->OwnQTextDocument::createObject(
      *f);
}

//  QVariant QTextDocument::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN13QTextDocument12loadResourceEiRK4QUrl(
    QTextDocument *self,
    int type,
    const QUrl *name) {
  return new QVariant(
      static_cast<OwnQTextDocument *>(self)->OwnQTextDocument::loadResource(
          type,
          *name));
}
