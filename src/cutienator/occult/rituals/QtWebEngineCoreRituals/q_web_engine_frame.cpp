//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineCore/qwebengineframe.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qlist.h>
#include <QtCore/QWeakPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  QWebEngineFrame::QWebEngineFrame()
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameC1Ev() {
  return new QWebEngineFrame();
}

//  QWebEngineFrame::QWebEngineFrame(const QWebEngineFrame &other)
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameC1ERKS_(
    const QWebEngineFrame *other) {
  return new QWebEngineFrame(*other);
}

//  QWebEngineFrame &QWebEngineFrame::operator=(const QWebEngineFrame &other)
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameaSERKS_(
    QWebEngineFrame *self,
    const QWebEngineFrame *other) {
  return &(self->operator=(*other));
}

//  QWebEngineFrame::QWebEngineFrame(QWebEngineFrame &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameC1EOS_(QWebEngineFrame *other) {
  return new QWebEngineFrame(std::move(*other));
}

//  QWebEngineFrame &QWebEngineFrame::operator=(QWebEngineFrame &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameaSEOS_(
    QWebEngineFrame *self,
    QWebEngineFrame *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebEngineFrame::~QWebEngineFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrameD1Ev(QWebEngineFrame *self) {
  delete self;
}

//  bool QWebEngineFrame::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebEngineFrame7isValidEv(const QWebEngineFrame *self) {
  return self->isValid();
}

//  QString QWebEngineFrame::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWebEngineFrame4nameEv(const QWebEngineFrame *self) {
  return new QString(self->name());
}

//  QString QWebEngineFrame::htmlName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWebEngineFrame8htmlNameEv(
    const QWebEngineFrame *self) {
  return new QString(self->htmlName());
}

//  QList<QWebEngineFrame> QWebEngineFrame::children() const
extern "C" Q_DECL_EXPORT
QList<QWebEngineFrame> *ritual_ZNK15QWebEngineFrame8childrenEv(
    const QWebEngineFrame *self) {
  return new QList<QWebEngineFrame>(self->children());
}

//  QUrl QWebEngineFrame::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QWebEngineFrame3urlEv(const QWebEngineFrame *self) {
  return new QUrl(self->url());
}

//  QSizeF QWebEngineFrame::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QWebEngineFrame4sizeEv(const QWebEngineFrame *self) {
  return new QSizeF(self->size());
}

//  bool QWebEngineFrame::isMainFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebEngineFrame11isMainFrameEv(
    const QWebEngineFrame *self) {
  return self->isMainFrame();
}

//  void QWebEngineFrame::runJavaScript(const QString &script, quint32
//      worldId)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringj(
    QWebEngineFrame *self,
    const QString *script,
    quint32 worldId) {
  self->runJavaScript(*script, worldId);
}

#if QT_DEPRECATED_SINCE(6, 10)
//  void QWebEngineFrame::runJavaScript(const QString &script, const QJSValue
//      &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringRK8QJSValue(
    QWebEngineFrame *self,
    const QString *script,
    const QJSValue *callback) {
  self->runJavaScript(*script, *callback);
}
#endif  // QT_DEPRECATED_SINCE(6, 10)

#if QT_DEPRECATED_SINCE(6, 10)
//  void QWebEngineFrame::runJavaScript(const QString &script, quint32
//      worldId, const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame13runJavaScriptERK7QStringjRK8QJSValue(
    QWebEngineFrame *self,
    const QString *script,
    quint32 worldId,
    const QJSValue *callback) {
  self->runJavaScript(*script, worldId, *callback);
}
#endif  // QT_DEPRECATED_SINCE(6, 10)

//  void QWebEngineFrame::printToPdf(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame10printToPdfERK7QString(
    QWebEngineFrame *self,
    const QString *filePath) {
  self->printToPdf(*filePath);
}

//  void QWebEngineFrame::printToPdf(const std::function<void (const
//      QByteArray &)> &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame10printToPdfERKSt8functionIFvRK10QByteArrayEE(
    QWebEngineFrame *self,
    const std::function<void (const QByteArray &)> *callback) {
  self->printToPdf(*callback);
}

#if QT_DEPRECATED_SINCE(6, 10)
//  void QWebEngineFrame::printToPdf(const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame10printToPdfERK8QJSValue(
    QWebEngineFrame *self,
    const QJSValue *callback) {
  self->printToPdf(*callback);
}
#endif  // QT_DEPRECATED_SINCE(6, 10)

//  bool operator==(const QWebEngineFrame &lhs, const QWebEngineFrame &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QWebEngineFrameS1_(
    const QWebEngineFrame *lhs,
    const QWebEngineFrame *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QWebEngineFrame &lhs, const QWebEngineFrame &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QWebEngineFrameS1_(
    const QWebEngineFrame *lhs,
    const QWebEngineFrame *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QWebEngineFrame::runJavaScriptImpl(const QString &scriptSource,
//      quint32 worldId, QtPrivate::QSlotObjectBase *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebEngineFrame17runJavaScriptImplERK7QStringjPN9QtPrivate15QSlotObjectBaseE(
    QWebEngineFrame *self,
    const QString *scriptSource,
    quint32 worldId,
    QtPrivate::QSlotObjectBase *callback) {
  self->runJavaScriptImpl(*scriptSource, worldId, callback);
}

//  QWebEngineFrame::QWebEngineFrame(QWeakPointer<QtWebEngineCore::WebContent
//      sAdapter> adapter, quint64 id)
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_ZN15QWebEngineFrameC1E12QWeakPointerIN15QtWebEngineCore18WebContentsAdapterEEy(
    const QWeakPointer<QtWebEngineCore::WebContentsAdapter> *adapter,
    quint64 id) {
  return new QWebEngineFrame(*adapter, id);
}

//  QList<QWebEngineFrame>::QList()
extern "C" Q_DECL_EXPORT
QList<QWebEngineFrame> *ritual_list_make_QWebEngineFrame() {
  return new QList<QWebEngineFrame>();
}

//  void QList<QWebEngineFrame>::append(const QWebEngineFrame &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWebEngineFrame(
    QList<QWebEngineFrame> *self,
    const QWebEngineFrame *element) {
  self->append(*element);
}

//  qsizetype QList<QWebEngineFrame>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWebEngineFrame(
    const QList<QWebEngineFrame> *self) {
  return self->size();
}

//  const QWebEngineFrame &QList<QWebEngineFrame>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWebEngineFrame *ritual_list_at_QWebEngineFrame(
    const QList<QWebEngineFrame> *self,
    long long index) {
  return new QWebEngineFrame(self->at(index));
}

//  QList<QWebEngineFrame>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWebEngineFrame(QList<QWebEngineFrame> *self) {
  delete self;
}
