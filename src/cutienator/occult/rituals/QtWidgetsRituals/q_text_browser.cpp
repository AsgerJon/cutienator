//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtextbrowser.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtextbrowser.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QTextBrowser::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QTextBrowser10metaObjectEv(
    const QTextBrowser *self) {
  return self->metaObject();
}

//  QString QTextBrowser::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTextBrowser2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextBrowser::tr(s, c, n));
}

//  QTextBrowser::QTextBrowser(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextBrowser *ritual_ZN12QTextBrowserC1EP7QWidget(QWidget *parent) {
  return new QTextBrowser(parent);
}

//  QTextBrowser::~QTextBrowser()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowserD1Ev(QTextBrowser *self) {
  delete self;
}

//  QUrl QTextBrowser::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QTextBrowser6sourceEv(const QTextBrowser *self) {
  return new QUrl(self->source());
}

//  QTextDocument::ResourceType QTextBrowser::sourceType() const
extern "C" Q_DECL_EXPORT
QTextDocument::ResourceType ritual_ZNK12QTextBrowser10sourceTypeEv(
    const QTextBrowser *self) {
  return self->sourceType();
}

//  QVariant QTextBrowser::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QTextBrowser12loadResourceEiRK4QUrl(
    QTextBrowser *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  bool QTextBrowser::isBackwardAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser19isBackwardAvailableEv(
    const QTextBrowser *self) {
  return self->isBackwardAvailable();
}

//  bool QTextBrowser::isForwardAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser18isForwardAvailableEv(
    const QTextBrowser *self) {
  return self->isForwardAvailable();
}

//  void QTextBrowser::clearHistory()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser12clearHistoryEv(QTextBrowser *self) {
  self->clearHistory();
}

//  QString QTextBrowser::historyTitle(int a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QTextBrowser12historyTitleEi(
    const QTextBrowser *self,
    int a0) {
  return new QString(self->historyTitle(a0));
}

//  QUrl QTextBrowser::historyUrl(int a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QTextBrowser10historyUrlEi(
    const QTextBrowser *self,
    int a0) {
  return new QUrl(self->historyUrl(a0));
}

//  int QTextBrowser::backwardHistoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTextBrowser20backwardHistoryCountEv(
    const QTextBrowser *self) {
  return self->backwardHistoryCount();
}

//  int QTextBrowser::forwardHistoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTextBrowser19forwardHistoryCountEv(
    const QTextBrowser *self) {
  return self->forwardHistoryCount();
}

//  bool QTextBrowser::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser17openExternalLinksEv(
    const QTextBrowser *self) {
  return self->openExternalLinks();
}

//  void QTextBrowser::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser20setOpenExternalLinksEb(
    QTextBrowser *self,
    bool open) {
  self->setOpenExternalLinks(open);
}

//  bool QTextBrowser::openLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser9openLinksEv(const QTextBrowser *self) {
  return self->openLinks();
}

//  void QTextBrowser::setOpenLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser12setOpenLinksEb(QTextBrowser *self, bool open) {
  self->setOpenLinks(open);
}

//  void QTextBrowser::setSource(const QUrl &name,
//      QTextDocument::ResourceType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser9setSourceERK4QUrlN13QTextDocument12ResourceTypeE(
    QTextBrowser *self,
    const QUrl *name,
    QTextDocument::ResourceType type) {
  self->setSource(*name, type);
}

//  void QTextBrowser::backward()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser8backwardEv(QTextBrowser *self) {
  self->backward();
}

//  void QTextBrowser::forward()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser7forwardEv(QTextBrowser *self) {
  self->forward();
}

//  void QTextBrowser::home()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser4homeEv(QTextBrowser *self) {
  self->home();
}

//  void QTextBrowser::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser6reloadEv(QTextBrowser *self) {
  self->reload();
}
